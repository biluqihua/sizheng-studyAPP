from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import date, timedelta

from ..db.database import get_db
from ..db.models import User, EnergyRecord, CheckInRecord
from ..schemas import EnergyRecordResponse, CheckInResponse
from ..security import get_current_active_user

router = APIRouter(prefix="/energy", tags=["积分系统"])


@router.get("/balance")
async def get_balance(current_user: User = Depends(get_current_active_user)):
    return {"balance": current_user.energy_balance}


@router.get("/records", response_model=List[EnergyRecordResponse])
async def get_energy_records(
    skip: int = 0,
    limit: int = 20,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    records = (
        db.query(EnergyRecord)
        .filter(EnergyRecord.user_id == current_user.id)
        .order_by(EnergyRecord.created_at.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )
    return records


@router.post("/check-in", response_model=CheckInResponse)
async def check_in(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    today = date.today()
    
    # 检查今天是否已签到
    existing_check_in = (
        db.query(CheckInRecord)
        .filter(CheckInRecord.user_id == current_user.id)
        .filter(CheckInRecord.check_in_date >= today)
        .first()
    )
    
    if existing_check_in:
        raise HTTPException(status_code=400, detail="今天已签到")
    
    # 计算连续签到天数
    yesterday = today - timedelta(days=1)
    yesterday_check_in = (
        db.query(CheckInRecord)
        .filter(CheckInRecord.user_id == current_user.id)
        .filter(CheckInRecord.check_in_date >= yesterday, CheckInRecord.check_in_date < today)
        .first()
    )
    
    streak_days = yesterday_check_in.streak_days + 1 if yesterday_check_in else 1
    
    # 签到奖励
    base_reward = 10
    streak_bonus = min(streak_days, 7) * 2  # 连续签到最多额外奖励14分
    total_reward = base_reward + streak_bonus
    
    # 创建签到记录
    check_in_record = CheckInRecord(user_id=current_user.id, streak_days=streak_days)
    
    # 更新积分
    current_user.energy_balance += total_reward
    
    # 创建积分记录
    energy_record = EnergyRecord(
        user_id=current_user.id,
        change_type="check_in",
        amount=total_reward,
        balance=current_user.energy_balance,
        description=f"每日签到，连续{streak_days}天",
    )
    
    db.add(check_in_record)
    db.add(energy_record)
    db.commit()
    
    return {
        "checked_in": True,
        "streak_days": streak_days,
        "energy_awarded": total_reward,
    }

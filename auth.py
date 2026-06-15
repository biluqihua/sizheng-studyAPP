
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta
from pydantic import BaseModel
from typing import List

from ..db.database import get_db
from ..db.models import User, School
from ..schemas import UserCreate, UserLogin, UserResponse, Token
from ..security import (
    verify_password,
    get_password_hash,
    create_access_token,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)

router = APIRouter(prefix="/auth", tags=["认证"])


class SchoolResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


@router.get("/schools", response_model=List[SchoolResponse])
async def get_schools(db: Session = Depends(get_db)):
    schools = db.query(School).all()
    return schools


@router.post("/register", response_model=UserResponse)
async def register(user_data: UserCreate, db: Session = Depends(get_db)):
    # 检查学号是否已存在
    existing_user = db.query(User).filter(User.student_id == user_data.student_id).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="该学号已注册")

    # 检查学校是否存在
    school = db.query(School).filter(School.id == user_data.school_id).first()
    if not school:
        raise HTTPException(status_code=404, detail="学校不存在")

    # 创建新用户
    hashed_password = get_password_hash(user_data.password)
    db_user = User(
        student_id=user_data.student_id,
        name=user_data.name,
        password_hash=hashed_password,
        school_id=user_data.school_id,
        email=user_data.email,
        phone=user_data.phone,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


@router.post("/login", response_model=Token)
async def login(login_data: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.student_id == login_data.student_id).first()
    if not user or not verify_password(login_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="学号或密码错误",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.id)}, expires_delta=access_token_expires
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": user,
    }

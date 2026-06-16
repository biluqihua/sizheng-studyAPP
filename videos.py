from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..db.database import get_db
from ..db.models import User, Video, VideoStatus
from ..schemas import VideoCreate, VideoResponse
from ..security import get_current_active_user

router = APIRouter(prefix="/videos", tags=["视频"])


@router.get("", response_model=List[VideoResponse])
async def get_videos(
    skip: int = 0,
    limit: int = 20,
    category: str = None,
    db: Session = Depends(get_db),
):
    query = db.query(Video).filter(Video.status == VideoStatus.APPROVED)
    if category:
        query = query.filter(Video.category == category)
    videos = query.order_by(Video.created_at.desc()).offset(skip).limit(limit).all()
    return videos


@router.get("/{video_id}", response_model=VideoResponse)
async def get_video(video_id: int, db: Session = Depends(get_db)):
    video = db.query(Video).filter(Video.id == video_id).first()
    if not video:
        raise HTTPException(status_code=404, detail="视频不存在")
    
    # 增加观看次数
    video.views_count += 1
    db.commit()
    
    return video


@router.post("", response_model=VideoResponse, status_code=status.HTTP_201_CREATED)
async def create_video(
    video_data: VideoCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    db_video = Video(
        **video_data.dict(),
        author_id=current_user.id,
        status=VideoStatus.PENDING,
    )
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from ..db.database import get_db
from ..db.models import Announcement, NewsArticle, Video
from ..schemas import AnnouncementResponse, NewsArticleResponse, VideoResponse

router = APIRouter(prefix="/home", tags=["首页"])


@router.get("/announcements", response_model=List[AnnouncementResponse])
async def get_announcements(db: Session = Depends(get_db)):
    announcements = (
        db.query(Announcement)
        .filter(Announcement.is_active == True)
        .order_by(Announcement.priority.desc(), Announcement.created_at.desc())
        .limit(5)
        .all()
    )
    return announcements


@router.get("/news", response_model=List[NewsArticleResponse])
async def get_news(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    news = (
        db.query(NewsArticle)
        .order_by(NewsArticle.is_featured.desc(), NewsArticle.created_at.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )
    return news


@router.get("/featured-videos", response_model=List[VideoResponse])
async def get_featured_videos(db: Session = Depends(get_db)):
    videos = (
        db.query(Video)
        .filter(Video.status == "approved")
        .order_by(Video.views_count.desc(), Video.likes_count.desc())
        .limit(10)
        .all()
    )
    return videos

from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional, List, Any
from .db.models import UserRole, VideoStatus


class UserBase(BaseModel):
    student_id: str
    name: str


class UserCreate(UserBase):
    password: str
    school_id: int
    email: Optional[EmailStr] = None
    phone: Optional[str] = None


class UserLogin(BaseModel):
    student_id: str
    password: str


class UserResponse(UserBase):
    id: int
    role: UserRole
    avatar: Optional[str] = None
    energy_balance: int
    created_at: datetime

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse


class VideoBase(BaseModel):
    title: str
    description: Optional[str] = None
    category: Optional[str] = None


class VideoCreate(VideoBase):
    video_url: str
    cover_url: Optional[str] = None


class VideoResponse(VideoBase):
    id: int
    cover_url: Optional[str] = None
    video_url: str
    author_id: int
    status: VideoStatus
    views_count: int
    likes_count: int
    created_at: datetime

    class Config:
        from_attributes = True


class ForumPostBase(BaseModel):
    title: str
    content: str
    category: Optional[str] = "discussion"


class ForumPostCreate(ForumPostBase):
    is_anonymous: bool = False


class ForumPostResponse(ForumPostBase):
    id: int
    author_id: int
    author_name: Optional[str] = None
    is_anonymous: bool
    views_count: int
    likes_count: int
    comment_count: int
    is_pinned: bool
    created_at: datetime

    class Config:
        from_attributes = True


class ForumCommentBase(BaseModel):
    content: str


class ForumCommentCreate(ForumCommentBase):
    parent_id: Optional[int] = None


class ForumCommentResponse(ForumCommentBase):
    id: int
    post_id: int
    author_id: int
    author_name: Optional[str] = None
    likes_count: int
    is_accepted: bool
    created_at: datetime

    class Config:
        from_attributes = True


class EnergyRecordResponse(BaseModel):
    id: int
    change_type: str
    amount: int
    balance: int
    description: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True


class NewsArticleResponse(BaseModel):
    id: int
    title: str
    content: str
    source: Optional[str] = None
    cover_url: Optional[str] = None
    ai_summary: Optional[str] = None
    is_featured: bool
    views_count: int
    created_at: datetime

    class Config:
        from_attributes = True


class AnnouncementResponse(BaseModel):
    id: int
    title: str
    content: str
    priority: int
    created_at: datetime

    class Config:
        from_attributes = True


class AISummaryRequest(BaseModel):
    content: str


class AIResponse(BaseModel):
    summary: str


class CheckInResponse(BaseModel):
    checked_in: bool
    streak_days: int
    energy_awarded: int


class MessageResponse(BaseModel):
    message: str

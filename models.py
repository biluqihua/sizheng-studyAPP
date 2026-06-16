from sqlalchemy import Column, Integer, String, Text, DateTime, Float, ForeignKey, Boolean, Enum as SQLEnum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base
import enum


class UserRole(str, enum.Enum):
    STUDENT = "student"
    TEACHER = "teacher"
    ADMIN = "admin"


class VideoStatus(str, enum.Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)
    school_id = Column(Integer, ForeignKey("schools.id"))
    email = Column(String, unique=True, index=True)
    phone = Column(String, unique=True, index=True)
    role = Column(SQLEnum(UserRole), default=UserRole.STUDENT)
    avatar = Column(String)
    energy_balance = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    school = relationship("School", back_populates="users")
    videos = relationship("Video", back_populates="author")
    study_notes = relationship("StudyNote", back_populates="user")
    energy_records = relationship("EnergyRecord", back_populates="user")
    forum_posts = relationship("ForumPost", back_populates="author")
    forum_comments = relationship("ForumComment", back_populates="author")


class School(Base):
    __tablename__ = "schools"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    province = Column(String)
    city = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    users = relationship("User", back_populates="school")


class Video(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    cover_url = Column(String)
    video_url = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"))
    category = Column(String)
    status = Column(SQLEnum(VideoStatus), default=VideoStatus.PENDING)
    views_count = Column(Integer, default=0)
    likes_count = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    author = relationship("User", back_populates="videos")
    study_notes = relationship("StudyNote", back_populates="video")


class StudyNote(Base):
    __tablename__ = "study_notes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    video_id = Column(Integer, ForeignKey("videos.id"))
    content_json = Column(Text)
    ai_summary = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="study_notes")
    video = relationship("Video", back_populates="study_notes")


class EnergyRecord(Base):
    __tablename__ = "energy_records"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    change_type = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)
    balance = Column(Integer, nullable=False)
    description = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="energy_records")


class ForumPost(Base):
    __tablename__ = "forum_posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"))
    category = Column(String, default="discussion")
    is_anonymous = Column(Boolean, default=False)
    views_count = Column(Integer, default=0)
    likes_count = Column(Integer, default=0)
    comment_count = Column(Integer, default=0)
    is_pinned = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    author = relationship("User", back_populates="forum_posts")
    comments = relationship("ForumComment", back_populates="post")


class ForumComment(Base):
    __tablename__ = "forum_comments"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    post_id = Column(Integer, ForeignKey("forum_posts.id"))
    author_id = Column(Integer, ForeignKey("users.id"))
    parent_id = Column(Integer, ForeignKey("forum_comments.id"))
    likes_count = Column(Integer, default=0)
    is_accepted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    post = relationship("ForumPost", back_populates="comments")
    author = relationship("User", back_populates="forum_comments")


class NewsArticle(Base):
    __tablename__ = "news_articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    source = Column(String)
    cover_url = Column(String)
    ai_summary = Column(Text)
    is_featured = Column(Boolean, default=False)
    views_count = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Announcement(Base):
    __tablename__ = "announcements"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    priority = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class CheckInRecord(Base):
    __tablename__ = "check_in_records"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    check_in_date = Column(DateTime(timezone=True), server_default=func.now())
    streak_days = Column(Integer, default=1)

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..db.database import get_db
from ..db.models import User, ForumPost, ForumComment
from ..schemas import ForumPostCreate, ForumPostResponse, ForumCommentCreate, ForumCommentResponse
from ..security import get_current_active_user

router = APIRouter(prefix="/forum", tags=["论坛"])


@router.get("/posts", response_model=List[ForumPostResponse])
async def get_posts(
    skip: int = 0,
    limit: int = 20,
    category: str = None,
    db: Session = Depends(get_db),
):
    query = db.query(ForumPost)
    if category:
        query = query.filter(ForumPost.category == category)
    
    # 先置顶，再按时间倒序
    posts = query.order_by(ForumPost.is_pinned.desc(), ForumPost.created_at.desc()).offset(skip).limit(limit).all()
    
    # 添加作者姓名
    for post in posts:
        post.author_name = post.author.name if not post.is_anonymous else "匿名用户"
    
    return posts


@router.get("/posts/{post_id}", response_model=ForumPostResponse)
async def get_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(ForumPost).filter(ForumPost.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="帖子不存在")
    
    # 增加浏览次数
    post.views_count += 1
    db.commit()
    
    post.author_name = post.author.name if not post.is_anonymous else "匿名用户"
    return post


@router.post("/posts", response_model=ForumPostResponse, status_code=status.HTTP_201_CREATED)
async def create_post(
    post_data: ForumPostCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    db_post = ForumPost(
        **post_data.dict(),
        author_id=current_user.id,
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    
    db_post.author_name = db_post.author.name if not db_post.is_anonymous else "匿名用户"
    return db_post


@router.get("/posts/{post_id}/comments", response_model=List[ForumCommentResponse])
async def get_comments(post_id: int, db: Session = Depends(get_db)):
    comments = db.query(ForumComment).filter(ForumComment.post_id == post_id).order_by(ForumComment.created_at).all()
    for comment in comments:
        comment.author_name = comment.author.name
    return comments


@router.post("/posts/{post_id}/comments", response_model=ForumCommentResponse, status_code=status.HTTP_201_CREATED)
async def create_comment(
    post_id: int,
    comment_data: ForumCommentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    # 检查帖子是否存在
    post = db.query(ForumPost).filter(ForumPost.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="帖子不存在")
    
    db_comment = ForumComment(
        **comment_data.dict(),
        post_id=post_id,
        author_id=current_user.id,
    )
    db.add(db_comment)
    
    # 更新评论数
    post.comment_count += 1
    db.commit()
    db.refresh(db_comment)
    
    db_comment.author_name = db_comment.author.name
    return db_comment

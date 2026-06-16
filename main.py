from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

from .db.database import engine, Base
from .db.models import User, School, Video, ForumPost, NewsArticle, Announcement
from .routes import auth, videos, forum, energy, home

load_dotenv()

# 创建数据库表
Base.metadata.create_all(bind=engine)

app = FastAPI(title="青研智思 - 高校思政智能研习平台 API", version="1.0.0")

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(auth.router, prefix="/api")
app.include_router(videos.router, prefix="/api")
app.include_router(forum.router, prefix="/api")
app.include_router(energy.router, prefix="/api")
app.include_router(home.router, prefix="/api")


@app.get("/")
async def root():
    return {
        "message": "欢迎使用青研智思 API",
        "version": "1.0.0",
        "docs": "/docs",
    }


@app.get("/health")
async def health_check():
    return {"status": "ok"}


# 初始化数据库数据
@app.on_event("startup")
async def startup_event():
    from .db.database import SessionLocal
    db = SessionLocal()
    try:
        # 检查是否已有学校数据
        if not db.query(School).first():
            # 添加示例学校数据
            schools = [
                School(name="清华大学", province="北京市", city="北京市"),
                School(name="北京大学", province="北京市", city="北京市"),
                School(name="复旦大学", province="上海市", city="上海市"),
                School(name="上海交通大学", province="上海市", city="上海市"),
                School(name="浙江大学", province="浙江省", city="杭州市"),
            ]
            db.add_all(schools)
            db.commit()
        
        # 检查是否已有公告数据
        if not db.query(Announcement).first():
            announcements = [
                Announcement(
                    title="欢迎使用青研智思平台",
                    content="欢迎各位同学和老师使用青研智思高校思政智能研习平台！在这里，您可以观看思政视频、参与论坛讨论、阅读权威资讯，还可以通过每日签到和学习获得积分奖励。",
                    priority=10,
                ),
                Announcement(
                    title="新功能上线：AI 随堂笔记",
                    content="我们很高兴地宣布，AI 随堂笔记功能现已上线！观看视频时，AI 会自动提取核心观点和金句，帮助您更好地学习。",
                    priority=5,
                ),
            ]
            db.add_all(announcements)
            db.commit()
        
        # 检查是否已有新闻数据
        if not db.query(NewsArticle).first():
            news = [
                NewsArticle(
                    title="习近平总书记关于教育的重要论述",
                    content="教育是国之大计、党之大计。培养什么人、怎样培养人、为谁培养人是教育的根本问题。",
                    source="人民日报",
                    is_featured=True,
                ),
                NewsArticle(
                    title="新时代高校思政工作高质量发展",
                    content="推动高校思想政治工作高质量发展，要坚持用习近平新时代中国特色社会主义思想铸魂育人。",
                    source="光明日报",
                ),
            ]
            db.add_all(news)
            db.commit()
            
    except Exception as e:
        print(f"初始化数据时出错: {e}")
    finally:
        db.close()

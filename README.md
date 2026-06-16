# 青研智思 - 高校思政智能研习平台

一个深度融合「思政教育 + 智能体（Agent）应用」的高校研习平台。

## 项目简介

「青研智思」致力于通过 AI 智能体技术，重构高校思政教育的交互模式，将严肃的政治学习与生动的智能交互、精准的个性化服务深度结合。

### 功能特色

- 🎓 **专属「理响」数字学伴** - 基于 Agent 技术的思政辅导员
- 📝 **「研习金句」AI 智能提取** - 视频观看时自动提取核心观点
- 📰 **「思政 AI 30秒」极速研判** - 快速获取文章要点摘要
- 📚 **「红色足迹」沉浸式书架** - 拟物化 3D 设计（规划中）
- 💬 **「理响校园」全实名严肃社区** - 师生交流平台
- ⭐ **「研习能量」红色激励闭环** - 积分奖励系统
- 🔒 **智能政治导向预审** - AI 内容审核机制

## 技术栈

### 后端
- **框架**: FastAPI - 高性能异步 Python Web 框架
- **数据库**: SQLite（开发）/ PostgreSQL（生产）
- **ORM**: SQLAlchemy 2.0
- **认证**: JWT (JSON Web Token)
- **密码加密**: Passlib (bcrypt)

### 前端
- **框架**: Vue 3 + Vite
- **UI 组件库**: Element Plus
- **状态管理**: Pinia
- **路由**: Vue Router 4
- **HTTP 客户端**: Axios

## 项目结构

```
qingyan-zhisi/
├── backend/                 # 后端项目
│   ├── src/
│   │   ├── db/             # 数据库模块
│   │   │   ├── database.py # 数据库连接配置
│   │   │   └── models.py   # 数据模型定义
│   │   ├── routes/         # API 路由
│   │   │   ├── auth.py     # 认证相关
│   │   │   ├── videos.py   # 视频相关
│   │   │   ├── forum.py    # 论坛相关
│   │   │   ├── energy.py   # 积分相关
│   │   │   └── home.py     # 首页相关
│   │   ├── main.py         # FastAPI 主应用
│   │   ├── schemas.py      # Pydantic 模型
│   │   └── security.py     # 安全认证模块
│   ├── requirements.txt    # Python 依赖
│   └── .env.example        # 环境变量示例
├── frontend/               # 前端项目
│   ├── src/
│   │   ├── views/         # 页面组件
│   │   │   ├── Login.vue
│   │   │   ├── Register.vue
│   │   │   ├── Home.vue
│   │   │   ├── Videos.vue
│   │   │   ├── Forum.vue
│   │   │   └── Profile.vue
│   │   ├── router/        # 路由配置
│   │   ├── stores/        # 状态管理
│   │   ├── utils/         # 工具函数
│   │   ├── App.vue
│   │   └── main.js
│   ├── index.html
│   ├── vite.config.js
│   └── package.json
└── admin/                 # 管理后台（规划中）
```

## 快速开始

### 环境要求

- Python 3.8+
- Node.js 16+

### 后端启动

1. 进入后端目录：
```bash
cd backend
```

2. 创建虚拟环境（推荐）：
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. 安装依赖：
```bash
pip install -r requirements.txt
```

4. 复制环境变量：
```bash
cp .env.example .env
```

5. 启动服务：
```bash
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

后端服务将在 http://localhost:8000 启动，API 文档访问：
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### 前端启动

1. 进入前端目录：
```bash
cd frontend
```

2. 安装依赖：
```bash
npm install
```

3. 启动开发服务器：
```bash
npm run dev
```

前端服务将在 http://localhost:5173 启动

## 核心功能模块

### 1. 用户认证
- 智能选校（支持全国高校搜索）
- 实名注册（学号 + 姓名 + 密码）
- JWT 登录认证
- 权限分级（学生/教师/管理员）

### 2. 智慧首页
- 公告通知栏
- 快捷操作入口
- 最新资讯列表
- 精选视频推荐

### 3. 视界大厅
- 视频分类浏览
- 视频搜索
- AI 随堂笔记
- 互动激励（答题获积分）

### 4. 研习论坛
- 帖子发布（实名/匿名可选）
- 分类讨论区
- 评论互动
- 教师回答置顶

### 5. 励学系统
- 每日签到
- 研习能量积分
- 积分记录查询
- 勋章系统（规划中）
- 积分商城（规划中）

### 6. 个人中心
- 个人信息管理
- 学习数据统计
- 积分记录查看
- 账户设置

## 数据库设计

### 核心数据表

| 表名 | 说明 |
|------|------|
| users | 用户表 |
| schools | 学校表 |
| videos | 视频表 |
| study_notes | 学习笔记表 |
| energy_records | 积分记录表 |
| forum_posts | 论坛帖子表 |
| forum_comments | 论坛评论表 |
| news_articles | 新闻资讯表 |
| announcements | 公告表 |
| check_in_records | 签到记录表 |

## API 接口

### 认证接口
- `POST /api/auth/register` - 用户注册
- `POST /api/auth/login` - 用户登录
- `GET /api/auth/schools` - 获取学校列表

### 首页接口
- `GET /api/home/announcements` - 获取公告
- `GET /api/home/news` - 获取新闻
- `GET /api/home/featured-videos` - 获取精选视频

### 视频接口
- `GET /api/videos` - 获取视频列表
- `GET /api/videos/{id}` - 获取视频详情
- `POST /api/videos` - 上传视频

### 论坛接口
- `GET /api/forum/posts` - 获取帖子列表
- `GET /api/forum/posts/{id}` - 获取帖子详情
- `POST /api/forum/posts` - 发布帖子
- `GET /api/forum/posts/{id}/comments` - 获取评论
- `POST /api/forum/posts/{id}/comments` - 发表评论

### 积分接口
- `GET /api/energy/balance` - 获取积分余额
- `GET /api/energy/records` - 获取积分记录
- `POST /api/energy/check-in` - 每日签到

## 开发计划

- [x] 项目框架搭建
- [x] 数据库设计
- [x] 用户认证系统
- [x] 首页、视频、论坛、个人中心基础功能
- [ ] 视频播放与 AI 笔记
- [ ] AI 内容摘要
- [ ] AI 智能体对话
- [ ] 积分商城
- [ ] 管理后台
- [ ] 内容审核系统
- [ ] 微信小程序版本
- [ ] 部署上线

## 贡献指南

欢迎提交 Issue 和 Pull Request！

## 许可证

MIT License

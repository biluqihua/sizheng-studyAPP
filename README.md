[青研智思.html](https://github.com/user-attachments/files/28842782/default.html)
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>青研智思 - 高校思政智能研习平台</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700&display=swap');
        
        * {
            font-family: 'Noto Sans SC', sans-serif;
        }
        
        .gradient-bg {
            background: linear-gradient(135deg, #E64C3C 0%, #F39C12 50%, #F1C40F 100%);
        }
        
        .gradient-primary {
            background: linear-gradient(135deg, #E64C3C 0%, #F39C12 100%);
        }
        
        .gradient-accent {
            background: linear-gradient(135deg, #C0392B 0%, #E64C3C 100%);
        }
        
        .card-hover {
            transition: all 0.3s ease;
        }
        
        .card-hover:hover {
            transform: translateY(-4px);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        }
        
        .typing-effect {
            overflow: hidden;
            border-right: 3px solid #E64C3C;
            white-space: nowrap;
            animation: typing 2s steps(30, end), blink-caret 0.75s step-end infinite;
        }
        
        @keyframes typing {
            from { width: 0 }
            to { width: 100% }
        }
        
        @keyframes blink-caret {
            from, to { border-color: transparent }
            50% { border-color: #E64C3C }
        }
        
        .fade-in {
            animation: fadeIn 0.5s ease-in;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .marquee {
            animation: marquee 20s linear infinite;
        }
        
        @keyframes marquee {
            0% { transform: translateX(100%); }
            100% { transform: translateX(-100%); }
        }
        
        .video-placeholder {
            background: linear-gradient(45deg, #f0f0f0 25%, transparent 25%),
                        linear-gradient(-45deg, #f0f0f0 25%, transparent 25%),
                        linear-gradient(45deg, transparent 75%, #f0f0f0 75%),
                        linear-gradient(-45deg, transparent 75%, #f0f0f0 75%);
            background-size: 20px 20px;
            background-position: 0 0, 0 10px, 10px -10px, -10px 0px;
        }
        
        .sidebar-item {
            transition: all 0.2s ease;
        }
        
        .sidebar-item:hover {
            background: linear-gradient(90deg, rgba(230, 76, 60, 0.1) 0%, transparent 100%);
        }
        
        .sidebar-item.active {
            background: linear-gradient(90deg, rgba(230, 76, 60, 0.2) 0%, transparent 100%);
            border-left: 3px solid #E64C3C;
        }
    </style>
</head>
<body class="bg-gray-50 min-h-screen">
    <!-- 登录页面 -->
    <div id="login-page" class="min-h-screen gradient-bg flex items-center justify-center p-4 hidden">
        <div class="bg-white rounded-2xl shadow-2xl w-full max-w-md p-8 fade-in">
            <div class="text-center mb-8">
                <div class="w-20 h-20 bg-gradient-to-br from-red-500 to-amber-400 rounded-full mx-auto flex items-center justify-center mb-4">
                    <i class="fas fa-flag text-white text-3xl"></i>
                </div>
                <h1 class="text-3xl font-bold bg-gradient-to-r from-red-600 to-amber-500 bg-clip-text text-transparent">青研智思</h1>
                <p class="text-gray-500 mt-2">高校思政智能研习平台</p>
            </div>
            
            <form id="login-form" class="space-y-6">
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">学号</label>
                    <input type="text" id="student-id" placeholder="请输入学号" 
                           class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-400 focus:border-transparent transition-all">
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">密码</label>
                    <input type="password" id="password" placeholder="请输入密码" 
                           class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-400 focus:border-transparent transition-all">
                </div>
                <button type="submit" 
                        class="w-full bg-gradient-to-r from-red-500 to-amber-400 text-white py-3 rounded-lg font-semibold hover:from-red-600 hover:to-amber-500 transition-all transform hover:scale-[1.02]">
                    登录
                </button>
            </form>
            
            <div class="mt-6 text-center text-gray-500 text-sm">
                <span>还没有账号？</span>
                <a href="#" id="show-register" class="text-red-500 hover:underline font-medium">立即注册</a>
            </div>
            
            <div class="mt-6 p-4 bg-orange-50 rounded-lg border border-orange-200">
                <p class="text-sm text-orange-800"><i class="fas fa-info-circle mr-2"></i>演示账号：2024001 / 123456</p>
            </div>
        </div>
    </div>

    <!-- 注册页面 -->
    <div id="register-page" class="min-h-screen gradient-bg flex items-center justify-center p-4 hidden">
        <div class="bg-white rounded-2xl shadow-2xl w-full max-w-md p-8 fade-in">
            <div class="text-center mb-8">
                <div class="w-16 h-16 bg-gradient-to-br from-red-500 to-amber-400 rounded-full mx-auto flex items-center justify-center mb-4">
                    <i class="fas fa-flag text-white text-2xl"></i>
                </div>
                <h2 class="text-2xl font-bold text-gray-800">加入青研智思</h2>
                <p class="text-gray-500 mt-2">开启思政学习新旅程</p>
            </div>
            
            <form id="register-form" class="space-y-4">
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">选择学校</label>
                    <select class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-400">
                        <option value="">请选择学校</option>
                        <option value="1">清华大学</option>
                        <option value="2">北京大学</option>
                        <option value="3">复旦大学</option>
                        <option value="4">上海交通大学</option>
                        <option value="5">浙江大学</option>
                    </select>
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">学号</label>
                    <input type="text" placeholder="请输入学号" 
                           class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-400">
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">姓名</label>
                    <input type="text" placeholder="请输入姓名" 
                           class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-400">
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">设置密码</label>
                    <input type="password" placeholder="请设置密码" 
                           class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-400">
                </div>
                <button type="submit" 
                        class="w-full bg-gradient-to-r from-red-500 to-amber-400 text-white py-3 rounded-lg font-semibold hover:from-red-600 hover:to-amber-500 transition-all">
                    注册
                </button>
            </form>
            
            <div class="mt-6 text-center text-gray-500 text-sm">
                <span>已有账号？</span>
                <a href="#" id="show-login" class="text-red-500 hover:underline font-medium">立即登录</a>
            </div>
        </div>
    </div>

    <!-- 主应用 -->
    <div id="main-app">
        <!-- 顶部导航 -->
        <nav class="bg-gradient-to-r from-red-600 to-amber-500 text-white shadow-lg sticky top-0 z-50">
            <div class="max-w-7xl mx-auto px-4">
                <div class="flex items-center justify-between h-16">
                    <div class="flex items-center space-x-3">
                        <div class="w-10 h-10 bg-white/30 rounded-lg flex items-center justify-center">
                            <i class="fas fa-flag text-white"></i>
                        </div>
                        <span class="text-xl font-bold">青研智思</span>
                    </div>
                    
                    <div class="hidden md:flex items-center space-x-1">
                        <button onclick="showPage('home')" class="nav-link px-4 py-2 rounded-lg hover:bg-white/20 transition-all" data-page="home">
                            <i class="fas fa-home mr-2"></i>首页
                        </button>
                        <button onclick="showPage('news')" class="nav-link px-4 py-2 rounded-lg hover:bg-white/20 transition-all" data-page="news">
                            <i class="fas fa-newspaper mr-2"></i>最新资讯
                        </button>
                        <button onclick="showPage('videos')" class="nav-link px-4 py-2 rounded-lg hover:bg-white/20 transition-all" data-page="videos">
                            <i class="fas fa-video mr-2"></i>视界大厅
                        </button>
                        <button onclick="showPage('forum')" class="nav-link px-4 py-2 rounded-lg hover:bg-white/20 transition-all" data-page="forum">
                            <i class="fas fa-comments mr-2"></i>研习论坛
                        </button>
                        <button onclick="showPage('profile')" class="nav-link px-4 py-2 rounded-lg hover:bg-white/20 transition-all" data-page="profile">
                            <i class="fas fa-user mr-2"></i>个人中心
                        </button>
                    </div>
                    
                    <div class="flex items-center space-x-4">
                        <div class="flex items-center space-x-2 bg-white/20 rounded-full px-4 py-1">
                            <i class="fas fa-bolt text-yellow-300"></i>
                            <span id="energy-display" class="font-semibold">128</span>
                        </div>
                        <button onclick="logout()" class="p-2 hover:bg-white/20 rounded-lg transition-all">
                            <i class="fas fa-sign-out-alt"></i>
                        </button>
                    </div>
                </div>
            </div>
        </nav>

        <!-- 移动端底部导航 -->
        <div class="md:hidden fixed bottom-0 left-0 right-0 bg-white border-t shadow-lg z-50">
                <div class="flex justify-around py-2">
                    <button onclick="showPage('home')" class="flex flex-col items-center p-2 text-red-500 mobile-nav" data-page="home">
                        <i class="fas fa-home text-xl"></i>
                        <span class="text-xs mt-1">首页</span>
                    </button>
                    <button onclick="showPage('news')" class="flex flex-col items-center p-2 text-gray-500 mobile-nav" data-page="news">
                        <i class="fas fa-newspaper text-xl"></i>
                        <span class="text-xs mt-1">资讯</span>
                    </button>
                    <button onclick="showPage('videos')" class="flex flex-col items-center p-2 text-gray-500 mobile-nav" data-page="videos">
                        <i class="fas fa-video text-xl"></i>
                        <span class="text-xs mt-1">视频</span>
                    </button>
                    <button onclick="showPage('forum')" class="flex flex-col items-center p-2 text-gray-500 mobile-nav" data-page="forum">
                        <i class="fas fa-comments text-xl"></i>
                        <span class="text-xs mt-1">论坛</span>
                    </button>
                    <button onclick="showPage('profile')" class="flex flex-col items-center p-2 text-gray-500 mobile-nav" data-page="profile">
                        <i class="fas fa-user text-xl"></i>
                        <span class="text-xs mt-1">我的</span>
                    </button>
                </div>
            </div>

        <!-- 首页 -->
        <div id="page-home" class="page-content max-w-7xl mx-auto px-4 py-6 pb-24 md:pb-6">
            <!-- 欢迎横幅 -->
            <div class="bg-gradient-to-r from-red-500 to-amber-400 rounded-2xl p-6 text-white mb-6 card-hover">
                <div class="flex items-center justify-between">
                    <div>
                        <h2 class="text-2xl font-bold mb-2">欢迎回来，张明同学！</h2>
                        <p class="text-orange-100">今天也要加油学习哦~</p>
                    </div>
                    <div class="w-20 h-20 bg-white/20 rounded-full flex items-center justify-center">
                        <i class="fas fa-graduation-cap text-4xl"></i>
                    </div>
                </div>
            </div>

            <!-- 公告栏 -->
            <div class="bg-white rounded-xl shadow-sm p-4 mb-6 border-l-4 border-orange-500">
                <div class="flex items-center">
                    <i class="fas fa-bullhorn text-orange-500 mr-3"></i>
                    <div class="flex-1 overflow-hidden">
                        <div class="marquee whitespace-nowrap">
                            <span class="text-gray-700 font-medium">【重要通知】关于开展2024年春季学期思政学习活动的通知</span>
                            <span class="mx-4 text-gray-400">|</span>
                            <span class="text-gray-700">【活动预告】"青年大学习"主题演讲比赛即将开始</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- 快捷操作 -->
            <div class="grid grid-cols-4 gap-4 mb-6">
                <div onclick="handleCheckIn()" class="bg-white rounded-xl p-4 text-center shadow-sm card-hover cursor-pointer">
                    <div class="w-12 h-12 bg-gradient-to-br from-red-400 to-red-500 rounded-full mx-auto flex items-center justify-center mb-2">
                        <i class="fas fa-calendar-check text-white text-xl"></i>
                    </div>
                    <span class="text-sm font-medium text-gray-700">每日签到</span>
                </div>
                <div onclick="showPage('videos')" class="bg-white rounded-xl p-4 text-center shadow-sm card-hover cursor-pointer">
                    <div class="w-12 h-12 bg-gradient-to-br from-red-500 to-amber-400 rounded-full mx-auto flex items-center justify-center mb-2">
                        <i class="fas fa-video text-white text-xl"></i>
                    </div>
                    <span class="text-sm font-medium text-gray-700">视界大厅</span>
                </div>
                <div onclick="showPage('forum')" class="bg-white rounded-xl p-4 text-center shadow-sm card-hover cursor-pointer">
                    <div class="w-12 h-12 bg-gradient-to-br from-amber-400 to-yellow-500 rounded-full mx-auto flex items-center justify-center mb-2">
                        <i class="fas fa-comments text-white text-xl"></i>
                    </div>
                    <span class="text-sm font-medium text-gray-700">研习论坛</span>
                </div>
                <div onclick="showPage('store')" class="bg-white rounded-xl p-4 text-center shadow-sm card-hover cursor-pointer">
                    <div class="w-12 h-12 bg-gradient-to-br from-orange-500 to-amber-500 rounded-full mx-auto flex items-center justify-center mb-2">
                        <i class="fas fa-store text-white text-xl"></i>
                    </div>
                    <span class="text-sm font-medium text-gray-700">积分商城</span>
                </div>
            </div>

            <!-- 最新资讯 -->
            <div class="mb-6">
                <div class="flex items-center justify-between mb-4">
                    <h3 class="text-lg font-bold text-gray-800">
                        <i class="fas fa-newspaper text-red-500 mr-2"></i>最新资讯
                    </h3>
                    <a href="#" onclick="showPage('news')" class="text-red-500 text-sm hover:underline">更多 <i class="fas fa-chevron-right"></i></a>
                </div>
                <div class="grid md:grid-cols-3 gap-4">
                    <div class="bg-white rounded-xl shadow-sm overflow-hidden card-hover cursor-pointer" onclick="playVideo(13)">
                        <div class="relative h-40 overflow-hidden">
                            <img src="党的生日视频封面.jpg" alt="党的生日视频" class="w-full h-full object-cover" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
                            <div class="absolute inset-0 bg-gradient-to-br from-red-200 to-amber-300 flex items-center justify-center" style="display: none;">
                                <i class="fas fa-image text-5xl text-red-400"></i>
                            </div>
                            <div class="absolute inset-0 bg-black/30 flex items-center justify-center">
                                <i class="fas fa-play-circle text-5xl text-white hover:scale-110 transition-transform cursor-pointer"></i>
                            </div>
                            <span class="absolute bottom-2 right-2 bg-black/70 text-white text-xs px-2 py-1 rounded">01:41</span>
                            <span class="absolute top-2 left-2 bg-red-500 text-white text-xs px-2 py-1 rounded">推荐</span>
                        </div>
                        <div class="p-4">
                            <h4 class="font-semibold text-gray-800 mb-2">【时政微视频丨勤掸思想尘常敲警示钟】今天，#党的生日。一起重温习近平总书记的谆谆告诫</h4>
                            <p class="text-sm text-gray-500">视听中国 · 2024-07-01</p>
                        </div>
                    </div>
                    <div class="bg-white rounded-xl shadow-sm overflow-hidden card-hover cursor-pointer" onclick="playVideo(14)">
                        <div class="relative h-40 overflow-hidden">
                            <img src="建党百年视频封面.jpg" alt="建党百年视频" class="w-full h-full object-cover" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
                            <div class="absolute inset-0 bg-gradient-to-br from-amber-200 to-yellow-300 flex items-center justify-center" style="display: none;">
                                <i class="fas fa-image text-5xl text-amber-400"></i>
                            </div>
                            <div class="absolute inset-0 bg-black/30 flex items-center justify-center">
                                <i class="fas fa-play-circle text-5xl text-white hover:scale-110 transition-transform cursor-pointer"></i>
                            </div>
                            <span class="absolute bottom-2 right-2 bg-black/70 text-white text-xs px-2 py-1 rounded">03:30</span>
                            <span class="absolute top-2 left-2 bg-red-500 text-white text-xs px-2 py-1 rounded">推荐</span>
                        </div>
                        <div class="p-4">
                            <h4 class="font-semibold text-gray-800 mb-2">【建党百年版错位时空】多想让你看看百年后的中国，多美丽！</h4>
                            <p class="text-sm text-gray-500">人民日报 · 2021-06-30</p>
                        </div>
                    </div>
                    <div class="bg-white rounded-xl shadow-sm overflow-hidden card-hover cursor-pointer" onclick="playVideo(6)">
                        <div class="relative h-40 overflow-hidden">
                            <img src="教育视频封面.jpg" alt="教育视频" class="w-full h-full object-cover" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
                            <div class="absolute inset-0 bg-gradient-to-br from-red-100 to-amber-200 flex items-center justify-center" style="display: none;">
                                <i class="fas fa-image text-5xl text-red-400"></i>
                            </div>
                            <div class="absolute inset-0 bg-black/30 flex items-center justify-center">
                                <i class="fas fa-play-circle text-5xl text-white hover:scale-110 transition-transform cursor-pointer"></i>
                            </div>
                            <span class="absolute bottom-2 right-2 bg-black/70 text-white text-xs px-2 py-1 rounded">01:19</span>
                        </div>
                        <div class="p-4">
                            <h4 class="font-semibold text-gray-800 mb-2">习近平在全国教育大会上发表重要讲话</h4>
                            <p class="text-sm text-gray-500">新华社 · 2024-09-09</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- 精选视频 - 建党百年专题 -->
            <div>
                <div class="flex items-center justify-between mb-4">
                    <h3 class="text-lg font-bold text-gray-800">
                        <i class="fas fa-star text-red-500 mr-2"></i>建党百年精选
                    </h3>
                    <a href="#" onclick="showPage('videos')" class="text-red-500 text-sm hover:underline">更多 <i class="fas fa-chevron-right"></i></a>
                </div>
                <div class="grid md:grid-cols-4 gap-4">
                    <div class="bg-white rounded-xl shadow-sm overflow-hidden card-hover cursor-pointer" onclick="playVideo(8)">
                        <div class="relative h-40 flex items-center justify-center" style="background-image: url('https://i0.hdslb.com/bfs/archive/5a2a9560d971a9c9c0e7f8b9c8b8b8b8.jpg'); background-size: cover; background-position: center;">
                            <div class="absolute inset-0 bg-black/20 flex items-center justify-center">
                                <i class="fas fa-play-circle text-5xl text-white"></i>
                            </div>
                            <span class="absolute bottom-2 right-2 bg-black/70 text-white text-xs px-2 py-1 rounded">28:45</span>
                            <span class="absolute top-2 left-2 bg-red-500 text-white text-xs px-2 py-1 rounded">精选</span>
                        </div>
                        <div class="p-3">
                            <h4 class="font-semibold text-gray-800 mb-1 text-sm line-clamp-2">建党百年庆祝大会：习近平发表重要讲话</h4>
                            <p class="text-xs text-gray-500">庆祝中国共产党成立100周年</p>
                        </div>
                    </div>
                    
                    <div class="bg-white rounded-xl shadow-sm overflow-hidden card-hover cursor-pointer" onclick="playVideo(12)">
                        <div class="relative h-40 flex items-center justify-center" style="background-image: url('https://i0.hdslb.com/bfs/archive/1e6a9560d971a9c9c0e7f8b9c8b8b8b8.jpg'); background-size: cover; background-position: center;">
                            <div class="absolute inset-0 bg-black/20 flex items-center justify-center">
                                <i class="fas fa-play-circle text-5xl text-white"></i>
                            </div>
                            <span class="absolute bottom-2 right-2 bg-black/70 text-white text-xs px-2 py-1 rounded">03:45</span>
                            <span class="absolute top-2 left-2 bg-red-500 text-white text-xs px-2 py-1 rounded">精选</span>
                        </div>
                        <div class="p-3">
                            <h4 class="font-semibold text-gray-800 mb-1 text-sm line-clamp-2">请党放心，强国有我！</h4>
                            <p class="text-xs text-gray-500">新时代青年的庄严承诺</p>
                        </div>
                    </div>
                    
                    <div class="bg-white rounded-xl shadow-sm overflow-hidden card-hover cursor-pointer" onclick="playVideo(5)">
                        <div class="relative h-40 flex items-center justify-center" style="background-image: url('http://i0.hdslb.com/bfs/archive/dfe4b911a7ca2f5ba6bc25fdcc8948cf7a8182f0.jpg'); background-size: cover; background-position: center;">
                            <div class="absolute inset-0 bg-black/20 flex items-center justify-center">
                                <i class="fas fa-play-circle text-5xl text-white"></i>
                            </div>
                            <span class="absolute bottom-2 right-2 bg-black/70 text-white text-xs px-2 py-1 rounded">03:30</span>
                            <span class="absolute top-2 left-2 bg-red-500 text-white text-xs px-2 py-1 rounded">本地</span>
                        </div>
                        <div class="p-3">
                            <h4 class="font-medium text-gray-800 text-sm line-clamp-2">【建党百年版错位时空】多想让你看看百年后的中国，多美丽！</h4>
                            <div class="flex items-center mt-2 text-xs text-gray-500">
                                <span><i class="fas fa-eye mr-1"></i>1038万</span>
                                <span class="ml-3"><i class="fas fa-heart mr-1"></i>8.9万</span>
                            </div>
                        </div>
                    </div>
                    <div class="bg-white rounded-xl shadow-sm overflow-hidden card-hover cursor-pointer" onclick="playVideo(1)">
                        <div class="relative h-36 bg-gradient-to-br from-amber-200 to-orange-300 flex items-center justify-center">
                            <div class="absolute inset-0 bg-black/30 flex items-center justify-center">
                                <i class="fas fa-play-circle text-5xl text-white"></i>
                            </div>
                            <span class="absolute bottom-2 right-2 bg-black/70 text-white text-xs px-2 py-1 rounded">12:34</span>
                        </div>
                        <div class="p-3">
                            <h4 class="font-medium text-gray-800 text-sm line-clamp-2">二十大报告解读：开辟马克思主义中国化时代化新境界</h4>
                            <div class="flex items-center mt-2 text-xs text-gray-500">
                                <span><i class="fas fa-eye mr-1"></i>1.2万</span>
                                <span class="ml-3"><i class="fas fa-heart mr-1"></i>856</span>
                            </div>
                        </div>
                    </div>
                    <div class="bg-white rounded-xl shadow-sm overflow-hidden card-hover cursor-pointer" onclick="playVideo(2)">
                        <div class="relative h-36 bg-gradient-to-br from-red-100 to-amber-100 flex items-center justify-center">
                            <div class="absolute inset-0 bg-black/20 flex items-center justify-center">
                                <i class="fas fa-play-circle text-5xl text-white"></i>
                            </div>
                            <span class="absolute bottom-2 right-2 bg-black/70 text-white text-xs px-2 py-1 rounded">18:20</span>
                        </div>
                        <div class="p-3">
                            <h4 class="font-medium text-gray-800 text-sm line-clamp-2">榜样的力量：新时代优秀共产党员先进事迹</h4>
                            <div class="flex items-center mt-2 text-xs text-gray-500">
                                <span><i class="fas fa-eye mr-1"></i>2.5万</span>
                                <span class="ml-3"><i class="fas fa-heart mr-1"></i>1.2k</span>
                            </div>
                        </div>
                    </div>
                    <div class="bg-white rounded-xl shadow-sm overflow-hidden card-hover cursor-pointer" onclick="playVideo(3)">
                        <div class="relative h-36 bg-gradient-to-br from-amber-50 to-red-100 flex items-center justify-center">
                            <div class="absolute inset-0 bg-black/20 flex items-center justify-center">
                                <i class="fas fa-play-circle text-5xl text-white"></i>
                            </div>
                            <span class="absolute bottom-2 right-2 bg-black/70 text-white text-xs px-2 py-1 rounded">25:10</span>
                        </div>
                        <div class="p-3">
                            <h4 class="font-medium text-gray-800 text-sm line-clamp-2">中国共产党百年奋斗史专题讲座</h4>
                            <div class="flex items-center mt-2 text-xs text-gray-500">
                                <span><i class="fas fa-eye mr-1"></i>3.8万</span>
                                <span class="ml-3"><i class="fas fa-heart mr-1"></i>2.1k</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- 资讯页面 -->
        <div id="page-news" class="page-content max-w-7xl mx-auto px-4 py-6 pb-24 md:pb-6 hidden">
            <h2 class="text-2xl font-bold text-gray-800 mb-6">
                <i class="fas fa-newspaper text-red-500 mr-2"></i>最新资讯
            </h2>

            <!-- 搜索栏 -->
            <div class="mb-6">
                <div class="relative">
                    <input type="text" id="news-search-input" placeholder="搜索资讯..." class="w-full px-5 py-3 pl-12 border border-gray-300 rounded-xl focus:ring-2 focus:ring-red-400 focus:border-transparent transition-all shadow-sm">
                    <i class="fas fa-search absolute left-4 top-1/2 transform -translate-y-1/2 text-gray-400"></i>
                    <button onclick="searchNews()" class="absolute right-3 top-1/2 transform -translate-y-1/2 bg-gradient-to-r from-red-500 to-amber-400 text-white px-4 py-1.5 rounded-lg hover:from-red-600 hover:to-amber-500 transition-all">
                        搜索
                    </button>
                </div>
            </div>

            <!-- 分类标签 -->
            <div class="flex space-x-2 mb-6 overflow-x-auto pb-2">
                <button class="px-4 py-2 bg-red-500 text-white rounded-full text-sm font-medium whitespace-nowrap">全部</button>
                <button class="px-4 py-2 bg-gray-100 text-gray-700 rounded-full text-sm font-medium whitespace-nowrap hover:bg-gray-200">时政要闻</button>
                <button class="px-4 py-2 bg-gray-100 text-gray-700 rounded-full text-sm font-medium whitespace-nowrap hover:bg-gray-200">思想理论</button>
                <button class="px-4 py-2 bg-gray-100 text-gray-700 rounded-full text-sm font-medium whitespace-nowrap hover:bg-gray-200">校园动态</button>
            </div>

            <!-- 资讯列表 -->
            <div id="news-list" class="space-y-4">
                <div class="bg-white rounded-xl shadow-sm overflow-hidden card-hover cursor-pointer" onclick="playVideo(6)" data-search="习近平 全国教育大会 总书记 时政要闻 新华社 教育">
                    <div class="md:flex">
                        <div class="md:w-1/3 h-48 relative overflow-hidden">
                            <img src="教育视频封面.jpg" alt="习近平在全国教育大会上发表重要讲话" class="w-full h-full object-cover" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
                            <div class="absolute inset-0 bg-gradient-to-br from-red-200 to-amber-300 flex items-center justify-center" style="display: none;">
                                <i class="fas fa-image text-6xl text-red-400"></i>
                            </div>
                            <div class="absolute inset-0 bg-black/30 flex items-center justify-center">
                                <i class="fas fa-play-circle text-6xl text-white hover:scale-110 transition-transform cursor-pointer"></i>
                            </div>
                            <span class="absolute bottom-2 right-2 bg-black/70 text-white text-xs px-2 py-1 rounded">01:19</span>
                        </div>
                        <div class="md:w-2/3 p-5">
                            <div class="flex items-center mb-2">
                                <span class="px-2 py-0.5 bg-orange-100 text-orange-700 text-xs rounded mr-2">时政要闻</span>
                                <span class="px-2 py-0.5 bg-red-500 text-white text-xs rounded mr-2">推荐</span>
                                <span class="text-xs text-gray-500">新华社 · 2024-09-09</span>
                            </div>
                            <h4 class="font-semibold text-gray-800 text-lg mb-2">习近平在全国教育大会上发表重要讲话</h4>
                            <p class="text-gray-600 text-sm mb-3 line-clamp-3">全面贯彻党的教育方针，落实立德树人根本任务，发展素质教育，推进教育公平，培养德智体美劳全面发展的社会主义建设者和接班人。</p>
                            <div class="flex items-center text-sm text-gray-500">
                                <span><i class="fas fa-eye mr-1"></i>10.8万</span>
                                <span class="ml-4"><i class="fas fa-heart mr-1"></i>0</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="bg-white rounded-xl shadow-sm overflow-hidden card-hover cursor-pointer" onclick="playVideo(7)" data-search="拾光纪 人大会议 总书记 关切 时政要闻 人民日报">
                    <div class="md:flex">
                        <div class="md:w-1/3 h-48 bg-gradient-to-br from-amber-200 to-yellow-300 flex items-center justify-center relative">
                            <div class="absolute inset-0 bg-black/30 flex items-center justify-center">
                                <i class="fas fa-play-circle text-6xl text-white"></i>
                            </div>
                            <span class="absolute bottom-2 right-2 bg-black/70 text-white text-xs px-2 py-1 rounded">06:20</span>
                        </div>
                        <div class="md:w-2/3 p-5">
                            <div class="flex items-center mb-2">
                                <span class="px-2 py-0.5 bg-orange-100 text-orange-700 text-xs rounded mr-2">时政要闻</span>
                                <span class="text-xs text-gray-500">人民日报 · 2024-06-10</span>
                            </div>
                            <h4 class="font-semibold text-gray-800 text-lg mb-2">拾光纪·人大会议首场发布会上的这些要点，饱含着总书记的关切</h4>
                            <p class="text-gray-600 text-sm mb-3 line-clamp-3">从发展全过程人民民主到保障和改善民生，从推进中国式现代化到全面建设社会主义现代化国家，总书记的重要论述指引方向。</p>
                            <div class="flex items-center text-sm text-gray-500">
                                <span><i class="fas fa-eye mr-1"></i>89万</span>
                                <span class="ml-4"><i class="fas fa-heart mr-1"></i>3.8万</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="bg-white rounded-xl shadow-sm overflow-hidden card-hover cursor-pointer" data-search="习近平 教育 总书记 时政要闻 人民日报">
                    <div class="md:flex">
                        <div class="md:w-1/3 h-48 bg-gradient-to-br from-red-100 to-amber-200 flex items-center justify-center">
                            <i class="fas fa-image text-6xl text-red-400"></i>
                        </div>
                        <div class="md:w-2/3 p-5">
                            <div class="flex items-center mb-2">
                                <span class="px-2 py-0.5 bg-orange-100 text-orange-700 text-xs rounded mr-2">时政要闻</span>
                                <span class="text-xs text-gray-500">人民日报 · 2024-06-09</span>
                            </div>
                            <h4 class="font-semibold text-gray-800 text-lg mb-2">习近平总书记关于教育的重要论述</h4>
                            <p class="text-gray-600 text-sm mb-3 line-clamp-3">习近平总书记关于教育的重要论述，深刻回答了培养什么人、怎样培养人、为谁培养人这个根本问题，为新时代教育事业发展指明了方向。</p>
                            <div class="flex items-center text-sm text-gray-500">
                                <span><i class="fas fa-eye mr-1"></i>25,680</span>
                                <span class="ml-4"><i class="fas fa-heart mr-1"></i>1,234</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="bg-white rounded-xl shadow-sm overflow-hidden card-hover cursor-pointer" data-search="新时代 高校 思政工作 高质量发展 思想理论 光明日报">
                    <div class="md:flex">
                        <div class="md:w-1/3 h-48 bg-gradient-to-br from-amber-100 to-yellow-200 flex items-center justify-center">
                            <i class="fas fa-image text-6xl text-amber-400"></i>
                        </div>
                        <div class="md:w-2/3 p-5">
                            <div class="flex items-center mb-2">
                                <span class="px-2 py-0.5 bg-amber-100 text-amber-700 text-xs rounded mr-2">思想理论</span>
                                <span class="text-xs text-gray-500">光明日报 · 2024-06-08</span>
                            </div>
                            <h4 class="font-semibold text-gray-800 text-lg mb-2">新时代高校思政工作高质量发展</h4>
                            <p class="text-gray-600 text-sm mb-3 line-clamp-3">深入贯彻落实习近平总书记关于高校思想政治工作的重要论述，全面推进新时代高校思政工作高质量发展。</p>
                            <div class="flex items-center text-sm text-gray-500">
                                <span><i class="fas fa-eye mr-1"></i>18,456</span>
                                <span class="ml-4"><i class="fas fa-heart mr-1"></i>892</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="bg-white rounded-xl shadow-sm overflow-hidden card-hover cursor-pointer" data-search="青年强 国家强 新时代 青年 责任 担当 校园动态 中国青年报">
                    <div class="md:flex">
                        <div class="md:w-1/3 h-48 bg-gradient-to-br from-amber-50 to-amber-150 flex items-center justify-center">
                            <i class="fas fa-image text-6xl text-amber-400"></i>
                        </div>
                        <div class="md:w-2/3 p-5">
                            <div class="flex items-center mb-2">
                                <span class="px-2 py-0.5 bg-yellow-100 text-yellow-700 text-xs rounded mr-2">校园动态</span>
                                <span class="text-xs text-gray-500">中国青年报 · 2024-06-07</span>
                            </div>
                            <h4 class="font-semibold text-gray-800 text-lg mb-2">青年强则国家强——新时代青年责任与担当</h4>
                            <p class="text-gray-600 text-sm mb-3 line-clamp-3">新时代中国青年生逢其时，施展才干的舞台无比广阔，实现梦想的前景无比光明。</p>
                            <div class="flex items-center text-sm text-gray-500">
                                <span><i class="fas fa-eye mr-1"></i>32,150</span>
                                <span class="ml-4"><i class="fas fa-heart mr-1"></i>2,568</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="bg-white rounded-xl shadow-sm overflow-hidden card-hover cursor-pointer" data-search="学习贯彻 二十大精神 思想理论 求是 二十大 现代化">
                    <div class="md:flex">
                        <div class="md:w-1/3 h-48 bg-gradient-to-br from-red-50 to-amber-100 flex items-center justify-center">
                            <i class="fas fa-image text-6xl text-red-400"></i>
                        </div>
                        <div class="md:w-2/3 p-5">
                            <div class="flex items-center mb-2">
                                <span class="px-2 py-0.5 bg-amber-100 text-amber-700 text-xs rounded mr-2">思想理论</span>
                                <span class="text-xs text-gray-500">求是 · 2024-06-06</span>
                            </div>
                            <h4 class="font-semibold text-gray-800 text-lg mb-2">深入学习贯彻党的二十大精神</h4>
                            <p class="text-gray-600 text-sm mb-3 line-clamp-3">党的二十大是在全党全国各族人民迈上全面建设社会主义现代化国家新征程、向第二个百年奋斗目标进军的关键时刻召开的一次十分重要的大会。</p>
                            <div class="flex items-center text-sm text-gray-500">
                                <span><i class="fas fa-eye mr-1"></i>45,230</span>
                                <span class="ml-4"><i class="fas fa-heart mr-1"></i>3,124</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="bg-white rounded-xl shadow-sm overflow-hidden card-hover cursor-pointer" data-search="高校 思政课 建设 推进会 校园动态 中国教育报">
                    <div class="md:flex">
                        <div class="md:w-1/3 h-48 bg-gradient-to-br from-blue-50 to-blue-100 flex items-center justify-center">
                            <i class="fas fa-image text-6xl text-blue-400"></i>
                        </div>
                        <div class="md:w-2/3 p-5">
                            <div class="flex items-center mb-2">
                                <span class="px-2 py-0.5 bg-blue-50 text-blue-600 text-xs rounded mr-2">校园动态</span>
                                <span class="text-xs text-gray-500">中国教育报 · 2024-06-05</span>
                            </div>
                            <h4 class="font-semibold text-gray-800 text-lg mb-2">全国高校思政课建设推进会召开</h4>
                            <p class="text-gray-600 text-sm mb-3 line-clamp-3">近日，全国高校思想政治理论课建设推进会在北京召开，会议总结了近年来思政课建设取得的成效，部署了下一阶段工作任务。</p>
                            <div class="flex items-center text-sm text-gray-500">
                                <span><i class="fas fa-eye mr-1"></i>28,940</span>
                                <span class="ml-4"><i class="fas fa-heart mr-1"></i>1,876</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- 视频页面 -->
        <div id="page-videos" class="page-content max-w-7xl mx-auto px-4 py-6 pb-24 md:pb-6 hidden">
            <h2 class="text-2xl font-bold text-gray-800 mb-6">
                <i class="fas fa-video text-red-500 mr-2"></i>视界大厅
            </h2>

            <!-- 搜索栏 -->
            <div class="mb-6">
                <div class="relative">
                    <input type="text" id="videos-search-input" placeholder="搜索视频..." class="w-full px-5 py-3 pl-12 border border-gray-300 rounded-xl focus:ring-2 focus:ring-red-400 focus:border-transparent transition-all shadow-sm">
                    <i class="fas fa-search absolute left-4 top-1/2 transform -translate-y-1/2 text-gray-400"></i>
                    <button onclick="searchVideos()" class="absolute right-3 top-1/2 transform -translate-y-1/2 bg-gradient-to-r from-red-500 to-amber-400 text-white px-4 py-1.5 rounded-lg hover:from-red-600 hover:to-amber-500 transition-all">
                        搜索
                    </button>
                </div>
            </div>

            <!-- 分类标签 -->
            <div class="flex space-x-2 mb-6 overflow-x-auto pb-2">
                <button class="px-4 py-2 bg-red-500 text-white rounded-full text-sm font-medium whitespace-nowrap">全部</button>
                <button class="px-4 py-2 bg-gray-100 text-gray-700 rounded-full text-sm font-medium whitespace-nowrap hover:bg-gray-200">时政热点</button>
                <button class="px-4 py-2 bg-gray-100 text-gray-700 rounded-full text-sm font-medium whitespace-nowrap hover:bg-gray-200">建党百年</button>
                <button class="px-4 py-2 bg-gray-100 text-gray-700 rounded-full text-sm font-medium whitespace-nowrap hover:bg-gray-200">宣传教育</button>
                <button class="px-4 py-2 bg-gray-100 text-gray-700 rounded-full text-sm font-medium whitespace-nowrap hover:bg-gray-200">国防教育</button>
                <button class="px-4 py-2 bg-gray-100 text-gray-700 rounded-full text-sm font-medium whitespace-nowrap hover:bg-gray-200">榜样力量</button>
            </div>

            <!-- 视频列表 -->
            <div id="videos-list" class="grid md:grid-cols-3 lg:grid-cols-4 gap-6">
                <!-- 请党放心视频 -->
                <div class="bg-white rounded-xl shadow-sm overflow-hidden card-hover cursor-pointer" onclick="playVideo(15)" data-search="请党放心 强国有我 共青团员 少先队员 献词 宣传教育">
                    <div class="relative h-44 overflow-hidden group">
                        <img src="请党放心视频封面.jpg" alt="请党放心视频" class="w-full h-full object-cover" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
                        <div class="absolute inset-0 bg-gradient-to-br from-red-400 to-red-600 flex items-center justify-center" style="display: none;">
                            <i class="fas fa-image text-6xl text-red-100"></i>
                        </div>
                        <div class="absolute inset-0 bg-black/20 group-hover:bg-black/40 transition-all flex items-center justify-center">
                            <i class="fas fa-play-circle text-6xl text-white group-hover:scale-110 transition-transform"></i>
                        </div>
                        <span class="absolute bottom-2 right-2 bg-black/70 text-white text-xs px-2 py-1 rounded">05:39</span>
                        <span class="absolute top-2 left-2 bg-red-500 text-white text-xs px-2 py-1 rounded">精选</span>
                    </div>
                    <div class="p-4">
                        <h4 class="font-semibold text-gray-800 mb-2">请党放心，强国有我！共青团员和少先队员代表集体献词</h4>
                        <p class="text-sm text-gray-500 mb-3">庆祝中国共产党成立100周年大会</p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span><i class="fas fa-eye mr-1"></i>64.3万</span>
                            <span><i class="fas fa-heart mr-1"></i>0</span>
                            <span>2021-07-01</span>
                        </div>
                    </div>
                </div>
                
                <div class="bg-white rounded-xl shadow-sm overflow-hidden card-hover cursor-pointer" onclick="playVideo(12)" data-search="请党放心 强国有我 青年 誓言 建党百年 宣传教育">
                    <div class="relative h-44 bg-gradient-to-br from-yellow-400 to-red-500 flex items-center justify-center group" style="background-image: url('https://i0.hdslb.com/bfs/archive/1e6a9560d971a9c9c0e7f8b9c8b8b8b8.jpg'); background-size: cover; background-position: center;">
                        <div class="absolute inset-0 bg-black/20 group-hover:bg-black/40 transition-all flex items-center justify-center">
                            <i class="fas fa-play-circle text-6xl text-white group-hover:scale-110 transition-transform"></i>
                        </div>
                        <span class="absolute bottom-2 right-2 bg-black/70 text-white text-xs px-2 py-1 rounded">03:45</span>
                        <span class="absolute top-2 left-2 bg-red-500 text-white text-xs px-2 py-1 rounded">精选</span>
                    </div>
                    <div class="p-4">
                        <h4 class="font-semibold text-gray-800 mb-2">请党放心，强国有我！</h4>
                        <p class="text-sm text-gray-500 mb-3">新时代青年的庄严承诺</p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span><i class="fas fa-eye mr-1"></i>342万</span>
                            <span><i class="fas fa-heart mr-1"></i>18.7万</span>
                            <span>2024-06-11</span>
                        </div>
                    </div>
                </div>
                
                <div class="bg-white rounded-xl shadow-sm overflow-hidden card-hover cursor-pointer" onclick="playVideo(9)" data-search="觉醒年代 革命者 建党百年 宣传教育">
                    <div class="relative h-44 bg-gradient-to-br from-red-300 to-amber-400 flex items-center justify-center group" style="background-image: url('https://i0.hdslb.com/bfs/archive/4b3a9560d971a9c9c0e7f8b9c8b8b8b8.jpg'); background-size: cover; background-position: center;">
                        <div class="absolute inset-0 bg-black/20 group-hover:bg-black/40 transition-all flex items-center justify-center">
                            <i class="fas fa-play-circle text-6xl text-white group-hover:scale-110 transition-transform"></i>
                        </div>
                        <span class="absolute bottom-2 right-2 bg-black/70 text-white text-xs px-2 py-1 rounded">05:20</span>
                    </div>
                    <div class="p-4">
                        <h4 class="font-semibold text-gray-800 mb-2">觉醒年代：致敬建党百年的革命者们</h4>
                        <p class="text-sm text-gray-500 mb-3">重温红色历史，传承革命精神</p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span><i class="fas fa-eye mr-1"></i>189万</span>
                            <span><i class="fas fa-heart mr-1"></i>8.9万</span>
                            <span>2024-06-10</span>
                        </div>
                    </div>
                </div>
                
                <div class="bg-white rounded-xl shadow-sm overflow-hidden card-hover cursor-pointer" onclick="playVideo(11)" data-search="建党伟业 南湖红船 新时代 建党百年">
                    <div class="relative h-44 bg-gradient-to-br from-amber-400 to-orange-500 flex items-center justify-center group" style="background-image: url('https://i0.hdslb.com/bfs/archive/2d5a9560d971a9c9c0e7f8b9c8b8b8b8.jpg'); background-size: cover; background-position: center;">
                        <div class="absolute inset-0 bg-black/20 group-hover:bg-black/40 transition-all flex items-center justify-center">
                            <i class="fas fa-play-circle text-6xl text-white group-hover:scale-110 transition-transform"></i>
                        </div>
                        <span class="absolute bottom-2 right-2 bg-black/70 text-white text-xs px-2 py-1 rounded">22:15</span>
                    </div>
                    <div class="p-4">
                        <h4 class="font-semibold text-gray-800 mb-2">建党伟业：从南湖红船到新时代</h4>
                        <p class="text-sm text-gray-500 mb-3">不忘初心，牢记使命，永远奋斗</p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span><i class="fas fa-eye mr-1"></i>156万</span>
                            <span><i class="fas fa-heart mr-1"></i>7.2万</span>
                            <span>2024-06-10</span>
                        </div>
                    </div>
                </div>
                
                <div class="bg-white rounded-xl shadow-sm overflow-hidden card-hover cursor-pointer" onclick="playVideo(10)" data-search="百年风华 中国共产党 奋斗历程 建党百年 国防教育">
                    <div class="relative h-44 bg-gradient-to-br from-red-500 to-amber-600 flex items-center justify-center group" style="background-image: url('https://i0.hdslb.com/bfs/archive/3c4a9560d971a9c9c0e7f8b9c8b8b8b8.jpg'); background-size: cover; background-position: center;">
                        <div class="absolute inset-0 bg-black/20 group-hover:bg-black/40 transition-all flex items-center justify-center">
                            <i class="fas fa-play-circle text-6xl text-white group-hover:scale-110 transition-transform"></i>
                        </div>
                        <span class="absolute bottom-2 right-2 bg-black/70 text-white text-xs px-2 py-1 rounded">15:30</span>
                    </div>
                    <div class="p-4">
                        <h4 class="font-semibold text-gray-800 mb-2">百年风华：中国共产党的百年奋斗历程</h4>
                        <p class="text-sm text-gray-500 mb-3">百年风雨，百年辉煌</p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span><i class="fas fa-eye mr-1"></i>78.5万</span>
                            <span><i class="fas fa-heart mr-1"></i>4.5万</span>
                            <span>2024-06-09</span>
                        </div>
                    </div>
                </div>
                
                <!-- 原有视频 -->
                <div class="bg-white rounded-xl shadow-sm overflow-hidden card-hover cursor-pointer" onclick="playVideo(6)" data-search="习近平 全国教育大会 总书记 时政要闻 央视新闻">
                    <div class="relative h-44 bg-gradient-to-br from-red-200 to-amber-300 flex items-center justify-center group">
                        <div class="absolute inset-0 bg-black/20 group-hover:bg-black/40 transition-all flex items-center justify-center">
                            <i class="fas fa-play-circle text-6xl text-white group-hover:scale-110 transition-transform"></i>
                        </div>
                        <span class="absolute bottom-2 right-2 bg-black/70 text-white text-xs px-2 py-1 rounded">08:45</span>
                            <span class="absolute top-2 left-2 bg-red-500 text-white text-xs px-2 py-1 rounded">推荐</span>
                    </div>
                    <div class="p-4">
                        <h4 class="font-semibold text-gray-800 mb-2">习近平在全国教育大会上发表重要讲话</h4>
                        <p class="text-sm text-gray-500 mb-3">全面贯彻党的教育方针，落实立德树人根本任务</p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span><i class="fas fa-eye mr-1"></i>128万</span>
                            <span><i class="fas fa-heart mr-1"></i>5.6万</span>
                            <span>2024-06-11</span>
                        </div>
                    </div>
                </div>
                
                <div class="bg-white rounded-xl shadow-sm overflow-hidden card-hover cursor-pointer" onclick="playVideo(7)" data-search="拾光纪 人大会议 总书记 关切 时政要闻 人民日报">
                    <div class="relative h-44 bg-gradient-to-br from-amber-200 to-yellow-300 flex items-center justify-center group">
                        <div class="absolute inset-0 bg-black/20 group-hover:bg-black/40 transition-all flex items-center justify-center">
                            <i class="fas fa-play-circle text-6xl text-white group-hover:scale-110 transition-transform"></i>
                        </div>
                        <span class="absolute bottom-2 right-2 bg-black/70 text-white text-xs px-2 py-1 rounded">06:20</span>
                    </div>
                    <div class="p-4">
                        <h4 class="font-semibold text-gray-800 mb-2">拾光纪·人大会议首场发布会上的这些要点，饱含着总书记的关切</h4>
                        <p class="text-sm text-gray-500 mb-3">总书记的重要论述指引前进方向</p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span><i class="fas fa-eye mr-1"></i>89万</span>
                            <span><i class="fas fa-heart mr-1"></i>3.8万</span>
                            <span>2024-06-10</span>
                        </div>
                    </div>
                </div>
                
                <div class="bg-white rounded-xl shadow-sm overflow-hidden card-hover cursor-pointer" onclick="playVideo(5)" data-search="建党百年 错位时空 百年中国 宣传教育 人民日报">
                    <div class="relative h-44 bg-gradient-to-br from-red-300 to-amber-400 flex items-center justify-center group">
                        <div class="absolute inset-0 bg-black/20 group-hover:bg-black/40 transition-all flex items-center justify-center">
                            <i class="fas fa-play-circle text-6xl text-white group-hover:scale-110 transition-transform"></i>
                        </div>
                        <span class="absolute bottom-2 right-2 bg-black/70 text-white text-xs px-2 py-1 rounded">03:30</span>
                        <span class="absolute top-2 left-2 bg-red-500 text-white text-xs px-2 py-1 rounded">本地</span>
                    </div>
                    <div class="p-4">
                        <h4 class="font-semibold text-gray-800 mb-2">【建党百年版错位时空】多想让你看看百年后的中国，多美丽！</h4>
                        <p class="text-sm text-gray-500 mb-3">人民日报 · 建党百年特别制作</p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span><i class="fas fa-eye mr-1"></i>1038万</span>
                            <span><i class="fas fa-heart mr-1"></i>8.9万</span>
                            <span>2021-06-30</span>
                        </div>
                    </div>
                </div>
                
                <div class="bg-white rounded-xl shadow-sm overflow-hidden card-hover cursor-pointer" onclick="playVideo(1)" data-search="二十大 马克思主义 中国化 时代化 时政热点">
                    <div class="relative h-44 bg-gradient-to-br from-amber-200 to-orange-300 flex items-center justify-center group">
                        <div class="absolute inset-0 bg-black/20 group-hover:bg-black/40 transition-all flex items-center justify-center">
                            <i class="fas fa-play-circle text-6xl text-white group-hover:scale-110 transition-transform"></i>
                        </div>
                        <span class="absolute bottom-2 right-2 bg-black/70 text-white text-xs px-2 py-1 rounded">12:34</span>
                    </div>
                    <div class="p-4">
                        <h4 class="font-semibold text-gray-800 mb-2">二十大报告解读：开辟马克思主义中国化时代化新境界</h4>
                        <p class="text-sm text-gray-500 mb-3">深入学习贯彻党的二十大精神</p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span><i class="fas fa-eye mr-1"></i>12,580</span>
                            <span><i class="fas fa-heart mr-1"></i>856</span>
                            <span>2024-06-09</span>
                        </div>
                    </div>
                </div>
                <div class="bg-white rounded-xl shadow-sm overflow-hidden card-hover cursor-pointer" onclick="playVideo(2)" data-search="榜样 力量 新时代 共产党员 先进事迹 榜样力量">
                    <div class="relative h-44 bg-gradient-to-br from-red-100 to-amber-100 flex items-center justify-center group">
                        <div class="absolute inset-0 bg-black/20 group-hover:bg-black/40 transition-all flex items-center justify-center">
                            <i class="fas fa-play-circle text-6xl text-white group-hover:scale-110 transition-transform"></i>
                        </div>
                        <span class="absolute bottom-2 right-2 bg-black/70 text-white text-xs px-2 py-1 rounded">18:20</span>
                    </div>
                    <div class="p-4">
                        <h4 class="font-semibold text-gray-800 mb-2">榜样的力量：新时代优秀共产党员先进事迹</h4>
                        <p class="text-sm text-gray-500 mb-3">学习先进典型，弘扬正能量</p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span><i class="fas fa-eye mr-1"></i>25,430</span>
                            <span><i class="fas fa-heart mr-1"></i>1,234</span>
                            <span>2024-06-08</span>
                        </div>
                    </div>
                </div>
                <div class="bg-white rounded-xl shadow-sm overflow-hidden card-hover cursor-pointer" onclick="playVideo(3)" data-search="中国共产党 百年奋斗史 专题讲座 国防教育">
                    <div class="relative h-44 bg-gradient-to-br from-amber-100 to-red-200 flex items-center justify-center group">
                        <div class="absolute inset-0 bg-black/20 group-hover:bg-black/40 transition-all flex items-center justify-center">
                            <i class="fas fa-play-circle text-6xl text-white group-hover:scale-110 transition-transform"></i>
                        </div>
                        <span class="absolute bottom-2 right-2 bg-black/70 text-white text-xs px-2 py-1 rounded">25:10</span>
                    </div>
                    <div class="p-4">
                        <h4 class="font-semibold text-gray-800 mb-2">中国共产党百年奋斗史专题讲座</h4>
                        <p class="text-sm text-gray-500 mb-3">学史明理、学史增信、学史崇德、学史力行</p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span><i class="fas fa-eye mr-1"></i>38,256</span>
                            <span><i class="fas fa-heart mr-1"></i>2,108</span>
                            <span>2024-06-07</span>
                        </div>
                    </div>
                </div>
                <div class="bg-white rounded-xl shadow-sm overflow-hidden card-hover cursor-pointer" onclick="playVideo(4)" data-search="新时代 爱国主义教育 实施纲要 宣传教育">
                    <div class="relative h-44 bg-gradient-to-br from-red-200 to-amber-300 flex items-center justify-center group">
                        <div class="absolute inset-0 bg-black/20 group-hover:bg-black/40 transition-all flex items-center justify-center">
                            <i class="fas fa-play-circle text-6xl text-white group-hover:scale-110 transition-transform"></i>
                        </div>
                        <span class="absolute bottom-2 right-2 bg-black/70 text-white text-xs px-2 py-1 rounded">15:45</span>
                    </div>
                    <div class="p-4">
                        <h4 class="font-semibold text-gray-800 mb-2">新时代爱国主义教育实施纲要解读</h4>
                        <p class="text-sm text-gray-500 mb-3">培养爱国之情、砥砺强国之志、实践报国之行</p>
                        <div class="flex items-center justify-between text-xs text-gray-500">
                            <span><i class="fas fa-eye mr-1"></i>9,856</span>
                            <span><i class="fas fa-heart mr-1"></i>623</span>
                            <span>2024-06-06</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- 论坛页面 -->
        <div id="page-forum" class="page-content max-w-4xl mx-auto px-4 py-6 pb-24 md:pb-6 hidden">
            <div class="flex items-center justify-between mb-6">
                <h2 class="text-2xl font-bold text-gray-800">
                    <i class="fas fa-comments text-red-500 mr-2"></i>研习论坛
                </h2>
                <div class="flex gap-3">
                    <button onclick="showPage('messages')" class="bg-white text-red-500 px-4 py-2 rounded-lg font-medium hover:bg-red-50 transition-all flex items-center gap-2">
                        <i class="fas fa-bell"></i>
                        消息
                        <span class="bg-red-500 text-white text-xs px-2 py-0.5 rounded-full">3</span>
                    </button>
                    <button onclick="showNewPostModal()" class="bg-gradient-to-r from-red-500 to-amber-400 text-white px-4 py-2 rounded-lg font-medium hover:from-red-600 hover:to-amber-500 transition-all">
                        <i class="fas fa-edit mr-2"></i>发布帖子
                    </button>
                </div>
            </div>

            <!-- 搜索栏 -->
            <div class="mb-6">
                <div class="relative">
                    <input type="text" id="forum-search-input" placeholder="搜索帖子..." class="w-full px-5 py-3 pl-12 border border-gray-300 rounded-xl focus:ring-2 focus:ring-red-400 focus:border-transparent transition-all shadow-sm">
                    <i class="fas fa-search absolute left-4 top-1/2 transform -translate-y-1/2 text-gray-400"></i>
                    <button onclick="searchForum()" class="absolute right-3 top-1/2 transform -translate-y-1/2 bg-gradient-to-r from-red-500 to-amber-400 text-white px-4 py-1.5 rounded-lg hover:from-red-600 hover:to-amber-500 transition-all">
                        搜索
                    </button>
                </div>
            </div>

            <!-- 分类标签 -->
            <div class="flex space-x-2 mb-6">
                <button class="px-4 py-2 bg-red-500 text-white rounded-lg text-sm font-medium">全部</button>
                <button class="px-4 py-2 bg-gray-100 text-gray-700 rounded-lg text-sm font-medium hover:bg-gray-200">理响校园</button>
                <button class="px-4 py-2 bg-gray-100 text-gray-700 rounded-lg text-sm font-medium hover:bg-gray-200">红色足迹</button>
            </div>

            <!-- 帖子列表 -->
            <div id="forum-list" class="space-y-4">
                <div class="bg-white rounded-xl shadow-sm p-5 card-hover cursor-pointer" onclick="viewPost(1)" data-search="两个确立 决定性意义 主题讨论 理响校园">
                    <div class="flex items-start">
                        <div class="w-12 h-12 bg-gradient-to-br from-red-400 to-amber-500 rounded-full flex items-center justify-center text-white font-bold mr-4">
                            王
                        </div>
                        <div class="flex-1">
                            <div class="flex items-center justify-between mb-2">
                                <div>
                                    <span class="font-semibold text-gray-800">王老师</span>
                                    <span class="ml-2 px-2 py-0.5 bg-orange-100 text-orange-700 text-xs rounded">教师</span>
                                    <span class="ml-2 px-2 py-0.5 bg-orange-100 text-orange-700 text-xs rounded">置顶</span>
                                </div>
                                <span class="text-sm text-gray-500">2小时前</span>
                            </div>
                            <h4 class="font-semibold text-gray-800 text-lg mb-2">【主题讨论】如何理解"两个确立"的决定性意义？</h4>
                            <p class="text-gray-600 mb-4 line-clamp-2">各位同学，今天我们来深入讨论"两个确立"的决定性意义。"两个确立"是党在新时代取得的重大政治成果，是推动党和国家事业取得历史性成就、发生历史性变革的决定性因素...</p>
                            <div class="flex items-center text-sm text-gray-500">
                                <span class="mr-6"><i class="fas fa-eye mr-1"></i>1,256</span>
                                <span class="mr-6"><i class="fas fa-heart mr-1"></i>89</span>
                                <span><i class="fas fa-comment mr-1"></i>56</span>
                                <span class="ml-auto px-2 py-1 bg-orange-100 text-orange-700 text-xs rounded">理响校园</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="bg-white rounded-xl shadow-sm p-5 card-hover cursor-pointer" onclick="viewPost(2)" data-search="革命纪念馆 参观 感悟 红色足迹">
                    <div class="flex items-start">
                        <div class="w-12 h-12 bg-gradient-to-br from-amber-400 to-yellow-500 rounded-full flex items-center justify-center text-white font-bold mr-4">
                            张
                        </div>
                        <div class="flex-1">
                            <div class="flex items-center justify-between mb-2">
                                <div>
                                    <span class="font-semibold text-gray-800">张明</span>
                                    <span class="ml-2 text-sm text-gray-500">清华大学</span>
                                </div>
                                <span class="text-sm text-gray-500">昨天</span>
                            </div>
                            <h4 class="font-semibold text-gray-800 text-lg mb-2">【分享】参观革命纪念馆的感悟</h4>
                            <p class="text-gray-600 mb-4 line-clamp-2">今天有幸参观了中国人民革命军事博物馆，看着那些珍贵的历史文物，内心久久不能平静。那些革命先辈们用鲜血和生命换来了我们今天的幸福生活...</p>
                            <div class="flex items-center text-sm text-gray-500">
                                <span class="mr-6"><i class="fas fa-eye mr-1"></i>892</span>
                                <span class="mr-6"><i class="fas fa-heart mr-1"></i>156</span>
                                <span><i class="fas fa-comment mr-1"></i>23</span>
                                <span class="ml-auto px-2 py-1 bg-amber-100 text-amber-700 text-xs rounded">红色足迹</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- 消息中心页面 -->
        <div id="page-messages" class="page-content max-w-4xl mx-auto px-4 py-6 pb-24 md:pb-6 hidden">
            <div class="flex items-center mb-6">
                <button onclick="showPage('forum')" class="mr-4 p-2 hover:bg-gray-100 rounded-lg transition-all">
                    <i class="fas fa-arrow-left text-gray-600 text-xl"></i>
                </button>
                <h2 class="text-2xl font-bold text-gray-800">
                    <i class="fas fa-bell text-red-500 mr-2"></i>消息中心
                </h2>
            </div>

            <div class="space-y-4">
                <!-- 回复消息 1 -->
                <div class="bg-white rounded-xl shadow-sm p-5 card-hover cursor-pointer border-l-4 border-red-500">
                    <div class="flex items-start gap-4">
                        <div class="w-12 h-12 bg-gradient-to-br from-red-400 to-amber-500 rounded-full flex items-center justify-center text-white font-bold flex-shrink-0">
                            李
                        </div>
                        <div class="flex-1">
                            <div class="flex items-center justify-between mb-2">
                                <div class="flex items-center gap-2">
                                    <span class="font-semibold text-gray-800">李同学</span>
                                    <span class="text-xs text-gray-500">北京大学</span>
                                    <span class="px-2 py-0.5 bg-orange-100 text-orange-700 text-xs rounded">新回复</span>
                                </div>
                                <span class="text-sm text-gray-500">10分钟前</span>
                            </div>
                            <p class="text-gray-600 mb-2">回复了你的帖子「【主题讨论】如何理解"两个确立"的决定性意义？」</p>
                            <div class="bg-gray-50 rounded-lg p-3 text-sm text-gray-600">
                                说得太好了！我也觉得这是我们必须深刻理解的重要内容。
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 回复消息 2 -->
                <div class="bg-white rounded-xl shadow-sm p-5 card-hover cursor-pointer border-l-4 border-gray-300">
                    <div class="flex items-start gap-4">
                        <div class="w-12 h-12 bg-gradient-to-br from-purple-400 to-pink-500 rounded-full flex items-center justify-center text-white font-bold flex-shrink-0">
                            王
                        </div>
                        <div class="flex-1">
                            <div class="flex items-center justify-between mb-2">
                                <div class="flex items-center gap-2">
                                    <span class="font-semibold text-gray-800">王同学</span>
                                    <span class="text-xs text-gray-500">复旦大学</span>
                                </div>
                                <span class="text-sm text-gray-500">1小时前</span>
                            </div>
                            <p class="text-gray-600 mb-2">回复了你的帖子「【分享】参观革命纪念馆的感悟」</p>
                            <div class="bg-gray-50 rounded-lg p-3 text-sm text-gray-600">
                                我也去过这个纪念馆，真的很震撼！
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 回复消息 3 -->
                <div class="bg-white rounded-xl shadow-sm p-5 card-hover cursor-pointer border-l-4 border-gray-300">
                    <div class="flex items-start gap-4">
                        <div class="w-12 h-12 bg-gradient-to-br from-red-400 to-amber-500 rounded-full flex items-center justify-center text-white font-bold flex-shrink-0">
                            赵
                        </div>
                        <div class="flex-1">
                            <div class="flex items-center justify-between mb-2">
                                <div class="flex items-center gap-2">
                                    <span class="font-semibold text-gray-800">赵同学</span>
                                    <span class="text-xs text-gray-500">上海交通大学</span>
                                </div>
                                <span class="text-sm text-gray-500">昨天</span>
                            </div>
                            <p class="text-gray-600 mb-2">回复了你的帖子「【主题讨论】如何理解"两个确立"的决定性意义？」</p>
                            <div class="bg-gray-50 rounded-lg p-3 text-sm text-gray-600">
                                能不能详细讲讲你的理解？
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- 个人中心 -->
        <div id="page-profile" class="page-content max-w-4xl mx-auto px-4 py-6 pb-24 md:pb-6 hidden">
            <!-- 个人信息卡片 -->
            <div class="bg-gradient-to-r from-red-500 to-amber-400 rounded-2xl p-6 text-white mb-6">
                <div class="flex items-center">
                    <div class="w-24 h-24 bg-white/20 rounded-full flex items-center justify-center mr-6 text-4xl font-bold">
                        张
                    </div>
                    <div>
                        <h2 class="text-2xl font-bold mb-1">张明</h2>
                        <p class="text-orange-100 mb-2">学号：2024001 · 清华大学</p>
                        <div class="flex items-center space-x-6">
                            <div class="text-center">
                                <div class="text-2xl font-bold">128</div>
                                <div class="text-sm text-orange-200">研习能量</div>
                            </div>
                            <div class="text-center">
                                <div class="text-2xl font-bold">15</div>
                                <div class="text-sm text-orange-200">学习天数</div>
                            </div>
                            <div class="text-center">
                                <div class="text-2xl font-bold">3</div>
                                <div class="text-sm text-orange-200">勋章</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="grid md:grid-cols-3 gap-6">
                <!-- 快捷操作 -->
                <div>
                    <div class="bg-white rounded-xl shadow-sm p-4 mb-4">
                        <h3 class="font-semibold text-gray-800 mb-4">
                            <i class="fas fa-bolt text-yellow-500 mr-2"></i>快捷操作
                        </h3>
                        <div class="space-y-3">
                            <button onclick="handleCheckIn()" class="w-full bg-gradient-to-r from-red-500 to-amber-400 text-white py-3 rounded-lg font-medium hover:from-red-600 hover:to-amber-500 transition-all">
                                <i class="fas fa-calendar-check mr-2"></i>每日签到
                            </button>
                            <button onclick="showPage('myposts')" class="w-full bg-gradient-to-r from-red-500 to-amber-400 text-white py-3 rounded-lg font-medium hover:from-red-600 hover:to-amber-500 transition-all">
                                <i class="fas fa-file-alt mr-2"></i>我的发布
                            </button>
                            <button onclick="showPage('store')" class="w-full bg-gradient-to-r from-amber-500 to-yellow-500 text-white py-3 rounded-lg font-medium hover:from-amber-600 hover:to-yellow-600 transition-all">
                                <i class="fas fa-store mr-2"></i>积分商城
                            </button>
                            <button class="w-full bg-gray-100 text-gray-700 py-3 rounded-lg font-medium hover:bg-gray-200 transition-all">
                                <i class="fas fa-history mr-2"></i>积分记录
                            </button>
                        </div>
                    </div>

                    <!-- 勋章墙 -->
                    <div class="bg-white rounded-xl shadow-sm p-4">
                        <h3 class="font-semibold text-gray-800 mb-4">
                            <i class="fas fa-trophy text-yellow-500 mr-2"></i>我的勋章
                        </h3>
                        <div class="grid grid-cols-3 gap-3">
                            <div class="text-center p-3 bg-gradient-to-br from-yellow-100 to-yellow-200 rounded-lg">
                                <i class="fas fa-star text-yellow-500 text-2xl mb-1"></i>
                                <div class="text-xs text-gray-600">学习达人</div>
                            </div>
                            <div class="text-center p-3 bg-gradient-to-br from-orange-100 to-amber-200 rounded-lg">
                                <i class="fas fa-fire text-orange-500 text-2xl mb-1"></i>
                                <div class="text-xs text-gray-600">连续签到</div>
                            </div>
                            <div class="text-center p-3 bg-gradient-to-br from-amber-100 to-yellow-200 rounded-lg">
                                <i class="fas fa-heart text-amber-500 text-2xl mb-1"></i>
                                <div class="text-xs text-gray-600">活跃分子</div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 个人信息 -->
                <div class="md:col-span-2">
                    <div class="bg-white rounded-xl shadow-sm p-6 mb-4">
                        <h3 class="font-semibold text-gray-800 mb-4">
                            <i class="fas fa-user text-red-500 mr-2"></i>个人信息
                        </h3>
                        <div class="space-y-4">
                            <div class="flex justify-between items-center py-3 border-b border-gray-100">
                                <span class="text-gray-500">姓名</span>
                                <span class="text-gray-800 font-medium">张明</span>
                            </div>
                            <div class="flex justify-between items-center py-3 border-b border-gray-100">
                                <span class="text-gray-500">学号</span>
                                <span class="text-gray-800 font-medium">2024001</span>
                            </div>
                            <div class="flex justify-between items-center py-3 border-b border-gray-100">
                                <span class="text-gray-500">学校</span>
                                <span class="text-gray-800 font-medium">清华大学</span>
                            </div>
                            <div class="flex justify-between items-center py-3 border-b border-gray-100">
                                <span class="text-gray-500">邮箱</span>
                                <span class="text-gray-800 font-medium">zhangming@tsinghua.edu.cn</span>
                            </div>
                            <div class="flex justify-between items-center py-3 border-b border-gray-100">
                                <span class="text-gray-500">角色</span>
                                <span class="px-3 py-1 bg-blue-100 text-blue-600 rounded-full text-sm">学生</span>
                            </div>
                            <div class="flex justify-between items-center py-3">
                                <span class="text-gray-500">注册时间</span>
                                <span class="text-gray-800 font-medium">2024-01-01</span>
                            </div>
                        </div>
                    </div>

                    <!-- 积分记录 -->
                    <div class="bg-white rounded-xl shadow-sm p-6">
                        <h3 class="font-semibold text-gray-800 mb-4">
                            <i class="fas fa-history text-blue-500 mr-2"></i>积分记录
                        </h3>
                        <div class="space-y-3">
                            <div class="flex items-center justify-between py-3 border-b border-gray-100">
                                <div class="flex items-center">
                                    <div class="w-10 h-10 bg-green-100 rounded-full flex items-center justify-center mr-3">
                                        <i class="fas fa-plus text-green-500"></i>
                                    </div>
                                    <div>
                                        <div class="font-medium text-gray-800">每日签到</div>
                                        <div class="text-sm text-gray-500">今天 08:30</div>
                                    </div>
                                </div>
                                <span class="text-green-500 font-bold">+10</span>
                            </div>
                            <div class="flex items-center justify-between py-3 border-b border-gray-100">
                                <div class="flex items-center">
                                    <div class="w-10 h-10 bg-green-100 rounded-full flex items-center justify-center mr-3">
                                        <i class="fas fa-play text-green-500"></i>
                                    </div>
                                    <div>
                                        <div class="font-medium text-gray-800">观看视频</div>
                                        <div class="text-sm text-gray-500">昨天 15:20</div>
                                    </div>
                                </div>
                                <span class="text-green-500 font-bold">+20</span>
                            </div>
                            <div class="flex items-center justify-between py-3">
                                <div class="flex items-center">
                                    <div class="w-10 h-10 bg-green-100 rounded-full flex items-center justify-center mr-3">
                                        <i class="fas fa-comment text-green-500"></i>
                                    </div>
                                    <div>
                                        <div class="font-medium text-gray-800">论坛发言</div>
                                        <div class="text-sm text-gray-500">6月8日 19:45</div>
                                    </div>
                                </div>
                                <span class="text-green-500 font-bold">+5</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- 我的发布页面 -->
        <div id="page-myposts" class="page-content max-w-4xl mx-auto px-4 py-6 pb-24 md:pb-6 hidden">
            <div class="flex items-center mb-6">
                <button onclick="showPage('profile')" class="mr-4 p-2 hover:bg-gray-100 rounded-lg transition-all">
                    <i class="fas fa-arrow-left text-gray-600 text-xl"></i>
                </button>
                <h2 class="text-2xl font-bold text-gray-800">
                    <i class="fas fa-file-alt text-red-500 mr-2"></i>我的发布
                </h2>
            </div>

            <div class="space-y-4">
                <!-- 我的帖子 1 -->
                <div class="bg-white rounded-xl shadow-sm p-5 card-hover cursor-pointer">
                    <div class="flex items-start">
                        <div class="w-12 h-12 bg-gradient-to-br from-red-400 to-amber-500 rounded-full flex items-center justify-center text-white font-bold mr-4 flex-shrink-0">
                            张
                        </div>
                        <div class="flex-1">
                            <div class="flex items-center justify-between mb-2">
                                <div class="flex items-center gap-2">
                                    <span class="font-semibold text-gray-800">张明</span>
                                    <span class="text-xs text-gray-500">清华大学</span>
                                </div>
                                <span class="text-sm text-gray-500">2天前</span>
                            </div>
                            <h4 class="font-semibold text-gray-800 text-lg mb-2">【主题讨论】如何理解"两个确立"的决定性意义？</h4>
                            <p class="text-gray-600 mb-4 line-clamp-2">各位同学，今天我们来深入讨论"两个确立"的决定性意义。"两个确立"是党在新时代取得的重大政治成果，是推动党和国家事业取得历史性成就、发生历史性变革的决定性因素...</p>
                            <div class="flex items-center text-sm text-gray-500">
                                <span class="mr-6"><i class="fas fa-eye mr-1"></i>1,256</span>
                                <span class="mr-6"><i class="fas fa-heart mr-1"></i>89</span>
                                <span><i class="fas fa-comment mr-1"></i>56</span>
                                <span class="ml-auto px-2 py-1 bg-orange-100 text-orange-700 text-xs rounded">理响校园</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 我的帖子 2 -->
                <div class="bg-white rounded-xl shadow-sm p-5 card-hover cursor-pointer">
                    <div class="flex items-start">
                        <div class="w-12 h-12 bg-gradient-to-br from-amber-400 to-yellow-500 rounded-full flex items-center justify-center text-white font-bold mr-4 flex-shrink-0">
                            张
                        </div>
                        <div class="flex-1">
                            <div class="flex items-center justify-between mb-2">
                                <div class="flex items-center gap-2">
                                    <span class="font-semibold text-gray-800">张明</span>
                                    <span class="text-xs text-gray-500">清华大学</span>
                                </div>
                                <span class="text-sm text-gray-500">3天前</span>
                            </div>
                            <h4 class="font-semibold text-gray-800 text-lg mb-2">【分享】参观革命纪念馆的感悟</h4>
                            <p class="text-gray-600 mb-4 line-clamp-2">今天有幸参观了中国人民革命军事博物馆，看着那些珍贵的历史文物，内心久久不能平静。那些革命先辈们用鲜血和生命换来了我们今天的幸福生活...</p>
                            <div class="flex items-center text-sm text-gray-500">
                                <span class="mr-6"><i class="fas fa-eye mr-1"></i>892</span>
                                <span class="mr-6"><i class="fas fa-heart mr-1"></i>156</span>
                                <span><i class="fas fa-comment mr-1"></i>23</span>
                                <span class="ml-auto px-2 py-1 bg-amber-100 text-amber-700 text-xs rounded">红色足迹</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 我的帖子 3 -->
                <div class="bg-white rounded-xl shadow-sm p-5 card-hover cursor-pointer">
                    <div class="flex items-start">
                        <div class="w-12 h-12 bg-gradient-to-br from-purple-400 to-purple-600 rounded-full flex items-center justify-center text-white font-bold mr-4 flex-shrink-0">
                            张
                        </div>
                        <div class="flex-1">
                            <div class="flex items-center justify-between mb-2">
                                <div class="flex items-center gap-2">
                                    <span class="font-semibold text-gray-800">张明</span>
                                    <span class="text-xs text-gray-500">清华大学</span>
                                </div>
                                <span class="text-sm text-gray-500">1周前</span>
                            </div>
                            <h4 class="font-semibold text-gray-800 text-lg mb-2">【学习心得】二十大报告学习体会</h4>
                            <p class="text-gray-600 mb-4 line-clamp-2">通过学习二十大报告，我深刻感受到了新时代的伟大成就，也更加明确了自己作为新时代青年的责任和使命...</p>
                            <div class="flex items-center text-sm text-gray-500">
                                <span class="mr-6"><i class="fas fa-eye mr-1"></i>2,341</span>
                                <span class="mr-6"><i class="fas fa-heart mr-1"></i>234</span>
                                <span><i class="fas fa-comment mr-1"></i>78</span>
                                <span class="ml-auto px-2 py-1 bg-purple-100 text-purple-600 text-xs rounded">理响校园</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- 积分商城页面 -->
        <div id="page-store" class="page-content max-w-6xl mx-auto px-4 py-6 pb-24 md:pb-6 hidden">
            <div class="flex items-center justify-between mb-6">
                <div class="flex items-center">
                    <button onclick="showPage('profile')" class="mr-4 p-2 hover:bg-gray-100 rounded-lg transition-all">
                        <i class="fas fa-arrow-left text-gray-600 text-xl"></i>
                    </button>
                    <h2 class="text-2xl font-bold text-gray-800">
                        <i class="fas fa-store text-red-500 mr-2"></i>积分商城
                    </h2>
                </div>
                <div class="bg-gradient-to-r from-red-500 to-amber-400 text-white px-6 py-3 rounded-xl shadow-lg">
                    <i class="fas fa-coins mr-2"></i>我的积分: <span id="current-points" class="font-bold text-xl">128</span>
                </div>
            </div>

            <!-- 分类标签 -->
            <div class="flex space-x-3 mb-6 overflow-x-auto pb-2">
                <button class="px-4 py-2 bg-red-500 text-white rounded-full text-sm font-medium whitespace-nowrap">全部商品</button>
                <button class="px-4 py-2 bg-gray-100 text-gray-700 rounded-full text-sm font-medium whitespace-nowrap hover:bg-gray-200">学习用品</button>
                <button class="px-4 py-2 bg-gray-100 text-gray-700 rounded-full text-sm font-medium whitespace-nowrap hover:bg-gray-200">文创周边</button>
                <button class="px-4 py-2 bg-gray-100 text-gray-700 rounded-full text-sm font-medium whitespace-nowrap hover:bg-gray-200">生活好物</button>
                <button class="px-4 py-2 bg-gray-100 text-gray-700 rounded-full text-sm font-medium whitespace-nowrap hover:bg-gray-200">已兑换</button>
            </div>

            <!-- 商品列表 -->
            <div class="grid md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
                <!-- 商品1 -->
                <div class="bg-white rounded-2xl shadow-sm overflow-hidden card-hover transition-all duration-300">
                    <div class="relative h-44 bg-gradient-to-br from-red-100 to-amber-200 flex items-center justify-center">
                        <i class="fas fa-book text-5xl text-red-500"></i>
                        <span class="absolute top-3 right-3 bg-red-400 text-white px-3 py-1 rounded-full text-sm font-bold">热销</span>
                    </div>
                    <div class="p-5">
                        <h3 class="font-semibold text-gray-800 text-lg mb-2">定制笔记本</h3>
                        <p class="text-sm text-gray-500 mb-4">精美封面，高质量纸张</p>
                        <div class="flex items-center justify-between">
                            <div class="text-2xl font-bold text-red-600">
                                <i class="fas fa-coins mr-1"></i>50
                            </div>
                            <button onclick="exchangeItem(1)" class="bg-gradient-to-r from-red-500 to-amber-400 text-white px-4 py-2 rounded-lg hover:from-red-600 hover:to-amber-500 transition-all font-medium">立即兑换</button>
                        </div>
                    </div>
                </div>

                <!-- 商品2 -->
                <div class="bg-white rounded-2xl shadow-sm overflow-hidden card-hover transition-all duration-300">
                    <div class="relative h-44 bg-gradient-to-br from-red-100 to-amber-200 flex items-center justify-center">
                        <i class="fas fa-pen text-5xl text-red-500"></i>
                    </div>
                    <div class="p-5">
                        <h3 class="font-semibold text-gray-800 text-lg mb-2">定制钢笔</h3>
                        <p class="text-sm text-gray-500 mb-4">精致外观，书写流畅</p>
                        <div class="flex items-center justify-between">
                            <div class="text-2xl font-bold text-red-600">
                                <i class="fas fa-coins mr-1"></i>80
                            </div>
                            <button onclick="exchangeItem(2)" class="bg-gradient-to-r from-red-500 to-amber-400 text-white px-4 py-2 rounded-lg hover:from-red-600 hover:to-amber-500 transition-all font-medium">立即兑换</button>
                        </div>
                    </div>
                </div>

                <!-- 商品3 -->
                <div class="bg-white rounded-2xl shadow-sm overflow-hidden card-hover transition-all duration-300">
                    <div class="relative h-44 bg-gradient-to-br from-amber-200 to-yellow-300 flex items-center justify-center">
                        <i class="fas fa-bag-shopping text-5xl text-red-500"></i>
                        <span class="absolute top-3 right-3 bg-amber-500 text-white px-3 py-1 rounded-full text-sm font-bold">新品</span>
                    </div>
                    <div class="p-5">
                        <h3 class="font-semibold text-gray-800 text-lg mb-2">定制帆布袋</h3>
                        <p class="text-sm text-gray-500 mb-4">环保耐用，时尚实用</p>
                        <div class="flex items-center justify-between">
                            <div class="text-2xl font-bold text-red-600">
                                <i class="fas fa-coins mr-1"></i>60
                            </div>
                            <button onclick="exchangeItem(3)" class="bg-gradient-to-r from-red-500 to-amber-400 text-white px-4 py-2 rounded-lg hover:from-red-600 hover:to-amber-500 transition-all font-medium">立即兑换</button>
                        </div>
                    </div>
                </div>

                <!-- 商品4 -->
                <div class="bg-white rounded-2xl shadow-sm overflow-hidden card-hover transition-all duration-300">
                    <div class="relative h-44 bg-gradient-to-br from-red-50 to-amber-100 flex items-center justify-center">
                        <i class="fas fa-mug-hot text-5xl text-amber-600"></i>
                    </div>
                    <div class="p-5">
                        <h3 class="font-semibold text-gray-800 text-lg mb-2">定制保温杯</h3>
                        <p class="text-sm text-gray-500 mb-4">长效保温，环保健康</p>
                        <div class="flex items-center justify-between">
                            <div class="text-2xl font-bold text-red-600">
                                <i class="fas fa-coins mr-1"></i>100
                            </div>
                            <button onclick="exchangeItem(4)" class="bg-gradient-to-r from-red-500 to-amber-400 text-white px-4 py-2 rounded-lg hover:from-red-600 hover:to-amber-500 transition-all font-medium">立即兑换</button>
                        </div>
                    </div>
                </div>

                <!-- 商品5 -->
                <div class="bg-white rounded-2xl shadow-sm overflow-hidden card-hover transition-all duration-300">
                    <div class="relative h-44 bg-gradient-to-br from-amber-300 to-yellow-400 flex items-center justify-center">
                        <i class="fas fa-star text-5xl text-red-50"></i>
                    </div>
                    <div class="p-5">
                        <h3 class="font-semibold text-gray-800 text-lg mb-2">校徽徽章套装</h3>
                        <p class="text-sm text-gray-500 mb-4">精美设计，收藏佳品</p>
                        <div class="flex items-center justify-between">
                            <div class="text-2xl font-bold text-red-600">
                                <i class="fas fa-coins mr-1"></i>30
                            </div>
                            <button onclick="exchangeItem(5)" class="bg-gradient-to-r from-red-500 to-amber-400 text-white px-4 py-2 rounded-lg hover:from-red-600 hover:to-amber-500 transition-all font-medium">立即兑换</button>
                        </div>
                    </div>
                </div>

                <!-- 商品6 -->
                <div class="bg-white rounded-2xl shadow-sm overflow-hidden card-hover transition-all duration-300">
                    <div class="relative h-44 bg-gradient-to-br from-red-100 to-amber-200 flex items-center justify-center">
                        <i class="fas fa-t-shirt text-5xl text-amber-600"></i>
                    </div>
                    <div class="p-5">
                        <h3 class="font-semibold text-gray-800 text-lg mb-2">校园文化T恤</h3>
                        <p class="text-sm text-gray-500 mb-4">纯棉舒适，时尚百搭</p>
                        <div class="flex items-center justify-between">
                            <div class="text-2xl font-bold text-red-600">
                                <i class="fas fa-coins mr-1"></i>150
                            </div>
                            <button onclick="exchangeItem(6)" class="bg-gradient-to-r from-red-500 to-amber-400 text-white px-4 py-2 rounded-lg hover:from-red-600 hover:to-amber-500 transition-all font-medium">立即兑换</button>
                        </div>
                    </div>
                </div>

                <!-- 商品7 -->
                <div class="bg-white rounded-2xl shadow-sm overflow-hidden card-hover transition-all duration-300">
                    <div class="relative h-44 bg-gradient-to-br from-red-50 to-amber-100 flex items-center justify-center">
                        <i class="fas fa-sticky-note text-5xl text-red-500"></i>
                    </div>
                    <div class="p-5">
                        <h3 class="font-semibold text-gray-800 text-lg mb-2">便签本套装</h3>
                        <p class="text-sm text-gray-500 mb-4">实用便利，学习必备</p>
                        <div class="flex items-center justify-between">
                            <div class="text-2xl font-bold text-red-600">
                                <i class="fas fa-coins mr-1"></i>25
                            </div>
                            <button onclick="exchangeItem(7)" class="bg-gradient-to-r from-red-500 to-amber-400 text-white px-4 py-2 rounded-lg hover:from-red-600 hover:to-amber-500 transition-all font-medium">立即兑换</button>
                        </div>
                    </div>
                </div>

                <!-- 商品8 -->
                <div class="bg-white rounded-2xl shadow-sm overflow-hidden card-hover transition-all duration-300">
                    <div class="relative h-44 bg-gradient-to-br from-amber-200 to-yellow-300 flex items-center justify-center">
                        <i class="fas fa-umbrella text-5xl text-red-50"></i>
                    </div>
                    <div class="p-5">
                        <h3 class="font-semibold text-gray-800 text-lg mb-2">定制雨伞</h3>
                        <p class="text-sm text-gray-500 mb-4">晴雨两用，品质上乘</p>
                        <div class="flex items-center justify-between">
                            <div class="text-2xl font-bold text-red-600">
                                <i class="fas fa-coins mr-1"></i>120
                            </div>
                            <button onclick="exchangeItem(8)" class="bg-gradient-to-r from-red-500 to-amber-400 text-white px-4 py-2 rounded-lg hover:from-red-600 hover:to-amber-500 transition-all font-medium">立即兑换</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- 视频播放弹窗 -->
    <div id="video-modal" class="fixed inset-0 bg-black/90 z-50 hidden items-center justify-center p-4">
        <div class="bg-white rounded-2xl max-w-4xl w-full max-h-[90vh] overflow-hidden">
            <div class="bg-gray-900 aspect-video flex items-center justify-center relative" id="video-player-container">
                <button onclick="closeVideoModal()" class="absolute top-4 right-4 text-white hover:text-gray-300 z-10">
                    <i class="fas fa-times text-2xl"></i>
                </button>
                <div id="video-placeholder" class="text-center text-white">
                    <i class="fas fa-play-circle text-8xl mb-4 opacity-50"></i>
                    <p class="text-gray-400">视频演示区域</p>
                </div>
                <iframe id="video-iframe" class="w-full h-full hidden" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
            </div>
            <div class="p-6">
                <h3 class="text-xl font-bold text-gray-800 mb-2" id="video-title">二十大报告解读：开辟马克思主义中国化时代化新境界</h3>
                <div class="flex items-center text-sm text-gray-500 mb-4">
                    <span><i class="fas fa-eye mr-1"></i>12,580</span>
                    <span class="ml-4"><i class="fas fa-heart mr-1"></i>856</span>
                    <span class="ml-4"><i class="fas fa-clock mr-1"></i>12:34</span>
                </div>
                <div class="flex items-center space-x-4">
                    <button class="flex-1 bg-gradient-to-r from-red-600 to-amber-500 text-white py-3 rounded-lg font-medium hover:from-red-700 hover:to-amber-600">
                        <i class="fas fa-robot mr-2"></i>AI 随堂笔记
                    </button>
                    <button class="px-6 py-3 bg-gray-100 text-gray-700 rounded-lg font-medium hover:bg-gray-200">
                        <i class="fas fa-download mr-2"></i>缓存
                    </button>
                    <button class="px-6 py-3 bg-gray-100 text-gray-700 rounded-lg font-medium hover:bg-gray-200">
                        <i class="fas fa-share mr-2"></i>分享
                    </button>
                </div>
            </div>
        </div>
    </div>

    <!-- 发布帖子弹窗 -->
    <div id="post-modal" class="fixed inset-0 bg-black/50 z-50 hidden items-center justify-center p-4">
        <div class="bg-white rounded-2xl max-w-2xl w-full max-h-[90vh] overflow-hidden">
            <div class="p-6 border-b border-gray-100">
                <div class="flex items-center justify-between">
                    <h3 class="text-xl font-bold text-gray-800">发布新帖子</h3>
                    <button onclick="closePostModal()" class="text-gray-500 hover:text-gray-700">
                        <i class="fas fa-times text-xl"></i>
                    </button>
                </div>
            </div>
            <div class="p-6">
                <div class="space-y-4">
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-2">标题</label>
                        <input type="text" placeholder="请输入帖子标题" class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-transparent">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-2">分类</label>
                        <select class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500">
                            <option value="discussion">理响校园</option>
                            <option value="share">红色足迹</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-2">内容</label>
                        <textarea rows="6" placeholder="请输入帖子内容..." class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-transparent"></textarea>
                    </div>
                </div>
            </div>
            <div class="p-6 border-t border-gray-100 flex justify-end space-x-3">
                <button onclick="closePostModal()" class="px-6 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200">取消</button>
                <button onclick="submitPost()" class="px-6 py-2 bg-gradient-to-r from-red-500 to-amber-400 text-white rounded-lg hover:from-red-600 hover:to-amber-500">发布</button>
            </div>
        </div>
    </div>

    <!-- 签到成功弹窗 -->
    <div id="checkin-modal" class="fixed inset-0 bg-black/50 z-50 hidden items-center justify-center p-4">
        <div class="bg-white rounded-2xl max-w-sm w-full p-8 text-center">
            <div class="w-24 h-24 bg-gradient-to-br from-red-400 to-amber-500 rounded-full mx-auto flex items-center justify-center mb-6">
                <i class="fas fa-check text-white text-5xl"></i>
            </div>
            <h3 class="text-2xl font-bold text-gray-800 mb-2">签到成功！</h3>
            <p class="text-gray-500 mb-6">连续签到 <span class="text-red-600 font-bold" id="streak-days">5</span> 天</p>
            <div class="bg-orange-50 rounded-xl p-4 mb-6">
                <p class="text-orange-800">
                    <i class="fas fa-bolt text-amber-500 mr-2"></i>
                    获得 <span class="font-bold text-2xl" id="reward-energy">+10</span> 研习能量
                </p>
            </div>
            <button onclick="closeCheckinModal()" class="w-full bg-gradient-to-r from-red-600 to-amber-500 text-white py-3 rounded-lg font-medium hover:from-red-700 hover:to-amber-600">
                太棒了！
            </button>
        </div>
    </div>

    <script>
        let currentPage = 'home';
        let energy = 128;
        let currentPoints = 128; // 与energy同步的积分变量
        let checkedInToday = false;
        let streakDays = 5;

        // 页面切换
        function showPage(page) {
            document.querySelectorAll('.page-content').forEach(el => el.classList.add('hidden'));
            document.getElementById(`page-${page}`).classList.remove('hidden');
            currentPage = page;
            
            document.querySelectorAll('.nav-link').forEach(btn => {
                btn.classList.remove('bg-white/20');
                if (btn.dataset.page === page) {
                    btn.classList.add('bg-white/20');
                }
            });
            
            document.querySelectorAll('.mobile-nav').forEach(btn => {
                btn.classList.remove('text-red-500');
                btn.classList.add('text-gray-500');
                if (btn.dataset.page === page) {
                    btn.classList.remove('text-gray-500');
                    btn.classList.add('text-red-500');
                }
            });
        }

        // 登录
        document.getElementById('login-form').addEventListener('submit', function(e) {
            e.preventDefault();
            const studentId = document.getElementById('student-id').value;
            const password = document.getElementById('password').value;
            
            if (studentId === '2024001' && password === '123456') {
                document.getElementById('login-page').classList.add('hidden');
                document.getElementById('main-app').classList.remove('hidden');
                showPage('home');
            } else {
                alert('学号或密码错误！演示账号：2024001 / 123456');
            }
        });

        // 注册页面切换
        document.getElementById('show-register').addEventListener('click', function(e) {
            e.preventDefault();
            document.getElementById('login-page').classList.add('hidden');
            document.getElementById('register-page').classList.remove('hidden');
        });

        document.getElementById('show-login').addEventListener('click', function(e) {
            e.preventDefault();
            document.getElementById('register-page').classList.add('hidden');
            document.getElementById('login-page').classList.remove('hidden');
        });

        document.getElementById('register-form').addEventListener('submit', function(e) {
            e.preventDefault();
            alert('注册成功！请使用演示账号登录');
            document.getElementById('register-page').classList.add('hidden');
            document.getElementById('login-page').classList.remove('hidden');
        });

        // 登出
        function logout() {
            if (confirm('确定要退出登录吗？')) {
                document.getElementById('main-app').classList.add('hidden');
                document.getElementById('login-page').classList.remove('hidden');
                document.getElementById('student-id').value = '';
                document.getElementById('password').value = '';
            }
        }

        // 签到
        function handleCheckIn() {
            if (checkedInToday) {
                alert('今天已经签到过了哦~');
                return;
            }
            
            const reward = 10 + Math.min(streakDays, 7) * 2;
            energy += reward;
            currentPoints = energy; // 同步到积分商城的积分变量
            document.getElementById('energy-display').textContent = energy;
            document.getElementById('current-points').textContent = currentPoints;
            document.getElementById('reward-energy').textContent = '+' + reward;
            document.getElementById('streak-days').textContent = streakDays;
            
            document.getElementById('checkin-modal').classList.remove('hidden');
            document.getElementById('checkin-modal').classList.add('flex');
            checkedInToday = true;
        }

        function closeCheckinModal() {
            document.getElementById('checkin-modal').classList.add('hidden');
            document.getElementById('checkin-modal').classList.remove('flex');
        }

        // 视频播放
        function playVideo(id) {
            const videoData = {
                1: { title: '二十大报告解读：开辟马克思主义中国化时代化新境界', views: '12,580', likes: '856', duration: '12:34', bvid: null },
                2: { title: '榜样的力量：新时代优秀共产党员先进事迹', views: '25,430', likes: '1,234', duration: '18:20', bvid: null },
                3: { title: '中国共产党百年奋斗史专题讲座', views: '38,256', likes: '2,108', duration: '25:10', bvid: null },
                4: { title: '新时代爱国主义教育实施纲要解读', views: '9,856', likes: '623', duration: '15:45', bvid: null },
                5: { title: '【建党百年版错位时空】多想让你看看百年后的中国，多美丽！', views: '1038万', likes: '8.9万', duration: '03:30', bvid: 'BV1sf4y1b74k', local: true, cover: 'http://i0.hdslb.com/bfs/archive/dfe4b911a7ca2f5ba6bc25fdcc8948cf7a8182f0.jpg' },
                6: { title: '习近平在全国教育大会上发表重要讲话', views: '10.8万', likes: '0', duration: '01:19', bvid: 'BV1hupWeeEnj', local: true, cover: 'http://i0.hdslb.com/bfs/archive/a009521120bb60e5da1e414a5eb715eb1abd1589.jpg' },
                7: { title: '拾光纪·人大会议首场发布会上的这些要点，饱含着总书记的关切', views: '89万', likes: '3.8万', duration: '06:20', bvid: 'BV1yEPqzzEEN', cover: 'https://i0.hdslb.com/bfs/archive/6b1a9560d971a9c9c0e7f8b9c8b8b8b8.jpg' },
                8: { title: '建党百年庆祝大会：习近平发表重要讲话', views: '235万', likes: '12.5万', duration: '28:45', bvid: 'BV1X64y1e7Q5', cover: 'https://i0.hdslb.com/bfs/archive/5a2a9560d971a9c9c0e7f8b9c8b8b8b8.jpg' },
                9: { title: '觉醒年代：致敬建党百年的革命者们', views: '189万', likes: '8.9万', duration: '05:20', bvid: 'BV14K4y1t7Jg', cover: 'https://i0.hdslb.com/bfs/archive/4b3a9560d971a9c9c0e7f8b9c8b8b8b8.jpg' },
                10: { title: '百年风华：中国共产党的百年奋斗历程', views: '78.5万', likes: '4.5万', duration: '15:30', bvid: 'BV1yB4y1x7u9', cover: 'https://i0.hdslb.com/bfs/archive/3c4a9560d971a9c9c0e7f8b9c8b8b8b8.jpg' },
                11: { title: '建党伟业：从南湖红船到新时代', views: '156万', likes: '7.2万', duration: '22:15', bvid: 'BV1X54y1G7dV', cover: 'https://i0.hdslb.com/bfs/archive/2d5a9560d971a9c9c0e7f8b9c8b8b8b8.jpg' },
                12: { title: '请党放心，强国有我！', views: '342万', likes: '18.7万', duration: '03:45', bvid: 'BV1G64y1B7r9', cover: 'https://i0.hdslb.com/bfs/archive/1e6a9560d971a9c9c0e7f8b9c8b8b8b8.jpg' },
                13: { title: '【时政微视频丨勤掸思想尘常敲警示钟】今天，#党的生日。一起重温习近平总书记的谆谆告诫', views: '3.1万', likes: '0', duration: '01:41', bvid: 'BV11b421J79G', local: true, cover: 'http://i2.hdslb.com/bfs/archive/88cc878828d390d3049946208673f04106e35385.jpg' },
                14: { title: '【建党百年版错位时空】多想让你看看百年后的中国，多美丽！', views: '1038万', likes: '8.9万', duration: '03:30', bvid: 'BV1sf4y1b74k', local: true, cover: 'http://i0.hdslb.com/bfs/archive/dfe4b911a7ca2f5ba6bc25fdcc8948cf7a8182f0.jpg' },
                15: { title: '请党放心，强国有我！共青团员和少先队员代表集体献词', views: '64.3万', likes: '0', duration: '05:39', bvid: 'BV1Yv411H7bL', local: true, cover: 'http://i2.hdslb.com/bfs/archive/e9e037df40b2b733621d5eecbca307ba3f5e3d3e.jpg' }
            };
            
            const data = videoData[id] || { title: '视频播放', views: '0', likes: '0', duration: '00:00', bvid: null };
            
            document.getElementById('video-title').textContent = data.title;
            
            // 更新视频信息
            const videoInfo = document.querySelector('#video-modal .flex.items-center.text-sm.text-gray-500');
            videoInfo.innerHTML = `
                <span><i class="fas fa-eye mr-1"></i>${data.views}</span>
                <span class="ml-4"><i class="fas fa-heart mr-1"></i>${data.likes}</span>
                <span class="ml-4"><i class="fas fa-clock mr-1"></i>${data.duration}</span>
            `;
            
            const iframe = document.getElementById('video-iframe');
            const placeholder = document.getElementById('video-placeholder');
            
            if (data.bvid) {
                // 有B站视频ID，直接跳转到B站播放
                window.open(`https://www.bilibili.com/video/${data.bvid}`, '_blank');
                // 同时显示弹窗和封面
                document.getElementById('video-player-container').style.backgroundImage = `url(${data.cover || ''})`;
                document.getElementById('video-player-container').style.backgroundSize = 'cover';
                document.getElementById('video-player-container').style.backgroundPosition = 'center';
                placeholder.innerHTML = `
                    <div class="bg-black/50 w-full h-full flex items-center justify-center">
                        <div class="text-center">
                            <i class="fas fa-play-circle text-8xl mb-4 text-white hover:scale-110 transition-transform cursor-pointer" onclick="window.open('https://www.bilibili.com/video/${data.bvid}', '_blank')"></i>
                            <p class="text-white text-lg">点击播放</p>
                        </div>
                    </div>
                `;
                iframe.classList.add('hidden');
                placeholder.classList.remove('hidden');
            } else {
                // 没有B站视频ID，显示占位符
                document.getElementById('video-player-container').style.backgroundImage = '';
                iframe.classList.add('hidden');
                iframe.src = '';
                placeholder.innerHTML = `
                    <i class="fas fa-play-circle text-8xl mb-4 opacity-50"></i>
                    <p class="text-gray-400">视频演示区域</p>
                `;
                placeholder.classList.remove('hidden');
            }
            
            document.getElementById('video-modal').classList.remove('hidden');
            document.getElementById('video-modal').classList.add('flex');
        }

        function closeVideoModal() {
            document.getElementById('video-modal').classList.add('hidden');
            document.getElementById('video-modal').classList.remove('flex');
            // 清除iframe内容以停止播放
            document.getElementById('video-iframe').src = '';
            document.getElementById('video-iframe').classList.add('hidden');
            document.getElementById('video-placeholder').classList.remove('hidden');
        }

        // 论坛
        function viewPost(id) {
            alert('帖子详情功能开发中...');
        }

        function showNewPostModal() {
            document.getElementById('post-modal').classList.remove('hidden');
            document.getElementById('post-modal').classList.add('flex');
        }

        function closePostModal() {
            document.getElementById('post-modal').classList.add('hidden');
            document.getElementById('post-modal').classList.remove('flex');
        }

        function submitPost() {
            alert('发布成功！');
            closePostModal();
        }

        function viewEnergyRecords() {
            showPage('profile');
        }

        // 积分商城功能
        // currentPoints 已在上方定义，与energy同步
        
        // 商品信息
        const items = {
            1: { name: '定制笔记本', points: 50 },
            2: { name: '定制钢笔', points: 80 },
            3: { name: '定制帆布袋', points: 60 },
            4: { name: '定制保温杯', points: 100 },
            5: { name: '校徽徽章套装', points: 30 },
            6: { name: '校园文化T恤', points: 150 },
            7: { name: '便签本套装', points: 25 },
            8: { name: '定制雨伞', points: 120 }
        };
        
        function exchangeItem(id) {
            const item = items[id];
            if (!item) return;
            
            // 检查积分是否足够
            if (currentPoints < item.points) {
                alert('积分不足！您当前有 ' + currentPoints + ' 积分，兑换 ' + item.name + ' 需要 ' + item.points + ' 积分。');
                return;
            }
            
            // 确认兑换
            if (confirm('确定要消耗 ' + item.points + ' 积分兑换 "' + item.name + '" 吗？')) {
                // 扣除积分
                currentPoints -= item.points;
                energy = currentPoints; // 同步到energy变量
                
                // 更新显示
                document.getElementById('current-points').textContent = currentPoints;
                document.getElementById('energy-display').textContent = energy;
                
                // 更新个人中心的积分显示
                const pointElements = document.querySelectorAll('.text-center .text-2xl');
                if (pointElements.length > 0) {
                    pointElements[0].textContent = currentPoints;
                }
                
                // 成功提示
                alert('兑换成功！您已成功兑换 "' + item.name + '"！');
            }
        }

        // 点击弹窗外部关闭
        document.getElementById('video-modal').addEventListener('click', function(e) {
            if (e.target === this) closeVideoModal();
        });
        
        document.getElementById('post-modal').addEventListener('click', function(e) {
            if (e.target === this) closePostModal();
        });
        
        document.getElementById('checkin-modal').addEventListener('click', function(e) {
            if (e.target === this) closeCheckinModal();
        });

        // 搜索功能 - 筛选显示匹配内容
        function searchNews() {
            const input = document.getElementById('news-search-input');
            const query = input.value.trim().toLowerCase();
            const items = document.querySelectorAll('#news-list > div');
            
            items.forEach(item => {
                const searchText = item.getAttribute('data-search')?.toLowerCase() || '';
                if (query === '' || searchText.includes(query)) {
                    item.style.display = '';
                } else {
                    item.style.display = 'none';
                }
            });
        }

        function searchVideos() {
            const input = document.getElementById('videos-search-input');
            const query = input.value.trim().toLowerCase();
            const items = document.querySelectorAll('#videos-list > div');
            
            items.forEach(item => {
                const searchText = item.getAttribute('data-search')?.toLowerCase() || '';
                if (query === '' || searchText.includes(query)) {
                    item.style.display = '';
                } else {
                    item.style.display = 'none';
                }
            });
        }

        function searchForum() {
            const input = document.getElementById('forum-search-input');
            const query = input.value.trim().toLowerCase();
            const items = document.querySelectorAll('#forum-list > div');
            
            items.forEach(item => {
                const searchText = item.getAttribute('data-search')?.toLowerCase() || '';
                if (query === '' || searchText.includes(query)) {
                    item.style.display = '';
                } else {
                    item.style.display = 'none';
                }
            });
        }

        // 回车搜索
        document.getElementById('news-search-input')?.addEventListener('input', function() {
            searchNews();
        });

        document.getElementById('videos-search-input')?.addEventListener('input', function() {
            searchVideos();
        });

        document.getElementById('forum-search-input')?.addEventListener('input', function() {
            searchForum();
        });
    </script>
</body>
</html>

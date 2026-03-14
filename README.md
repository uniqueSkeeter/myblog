# unique蚊子的blog

一个现代化的全栈个人博客项目，使用 Flask + Vue 3 构建。

## 技术栈

### 后端
- Python 3.12+
- Flask (Web 框架)
- Flask-SQLAlchemy (ORM)
- Flask-Migrate (数据库迁移)
- Flask-CORS (跨域支持)
- SQLite (数据库)
- uv (包管理)

### 前端
- Vue 3 (UI 框架)
- Vite (构建工具)
- Vue Router 4 (路由)
- Pinia (状态管理)
- Element Plus (UI 组件库)
- Axios (HTTP 客户端)
- marked (Markdown 解析)

## 功能特性

### 前台功能
- 📝 首页 - 文章列表展示
- 📖 文章详情 - Markdown 内容渲染
- 📂 分类 - 按分类浏览文章
- 🏷️ 标签 - 按标签浏览文章
- 👤 关于我 - 个人介绍页面
- 🔍 404 页面

### 后台功能
- ✍️ 文章管理 - 创建/编辑/删除文章
- 📁 分类管理 - 分类的增删改查
- 🏷️ 标签管理 - 标签的增删改查
- 📝 Markdown 编辑器

## 项目结构

```
myblog/
├── backend/              # 后端 Flask 应用
│   ├── app/
│   │   ├── models/      # 数据库模型
│   │   ├── routes/      # API 路由
│   │   ├── config.py    # 配置
│   │   └── __init__.py  # 应用工厂
│   ├── migrations/      # 数据库迁移
│   ├── .env             # 环境变量
│   ├── pyproject.toml   # 依赖配置
│   └── run.py           # 入口文件
└── frontend/            # 前端 Vue 3 应用
    ├── src/
    │   ├── components/  # 可复用组件
    │   ├── views/       # 页面组件
    │   │   ├── public/  # 前台页面
    │   │   └── admin/   # 后台页面
    │   ├── router/      # 路由配置
    │   ├── stores/      # Pinia 状态管理
    │   ├── api/         # API 服务
    │   └── utils/       # 工具函数
    └── package.json
```

## 快速开始

### 前置要求
- Python 3.12+
- Node.js 18+
- npm 或 yarn
- uv (Python 包管理工具)

### 后端启动

1. 进入后端目录
```bash
cd backend
```

2. 创建虚拟环境并安装依赖
```bash
uv venv
source .venv/Scripts/activate  # Windows
# 或 source .venv/bin/activate  # Linux/Mac
uv pip install -e .
```

3. 初始化数据库
```bash
flask db upgrade
```

4. 启动后端服务器
```bash
python run.py
```

后端服务将运行在 http://localhost:5000

### 前端启动

1. 进入前端目录
```bash
cd frontend
```

2. 安装依赖
```bash
npm install
```

3. 启动开发服务器
```bash
npm run dev
```

前端服务将运行在 http://localhost:5173

## 使用说明

### 访问前台
打开浏览器访问 http://localhost:5173

### 访问后台
点击首页右上角的「管理后台」按钮，或直接访问 http://localhost:5173/admin

### 创建第一篇文章
1. 进入后台管理
2. 先创建分类和标签
3. 创建新文章，填写标题和内容（支持 Markdown）
4. 保存后即可在前台看到文章

## API 接口

### 文章接口
- `GET /api/articles` - 获取文章列表
- `GET /api/articles/<id>` - 获取文章详情
- `POST /api/articles` - 创建文章
- `PUT /api/articles/<id>` - 更新文章
- `DELETE /api/articles/<id>` - 删除文章

### 分类接口
- `GET /api/categories` - 获取所有分类
- `POST /api/categories` - 创建分类
- `PUT /api/categories/<id>` - 更新分类
- `DELETE /api/categories/<id>` - 删除分类
- `GET /api/categories/<id>/articles` - 获取分类下的文章

### 标签接口
- `GET /api/tags` - 获取所有标签
- `POST /api/tags` - 创建标签
- `PUT /api/tags/<id>` - 更新标签
- `DELETE /api/tags/<id>` - 删除标签
- `GET /api/tags/<id>/articles` - 获取标签下的文章

## 开发说明

### 数据库迁移
```bash
# 创建新的迁移
flask db migrate -m "描述"

# 应用迁移
flask db upgrade
```

### 前端构建
```bash
npm run build
```

## License

MIT

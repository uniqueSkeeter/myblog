# unique蚊子的blog项目开发指导文档

## 项目目标

构建一个名为"unique蚊子的blog"的个人博客网站，采用现代化全栈开发模式，前端追求轻量与速度，后端利用Python生态优势，遵循清晰的工程化标准，确保代码质量和可维护性。

## 技术栈与工具

### 后端 (Backend)

**语言与包管理**

- 使用Python作为主要开发语言
- 强制使用uv作为项目包管理和虚拟环境工具

**Web框架**

- 选用Flask框架，轻量级且灵活的微框架

**数据库**

- 使用SQLite作为开发阶段的数据库

### 前端 (Frontend)

**核心框架**

- 使用Vue 3，利用组合式API(Composition API)

**构建工具**

- 使用Vite作为前端项目构建工具

**UI框架**

- 集成主流Vue 3 UI组件库（如Element Plus或Naive UI）

**HTTP客户端**

- 使用Axios库处理前后端API通信

## 核心功能需求

### 前台展示 (Public Pages)

1. **首页**
    - 展示博客标题、Slogan
    - 按时间倒序排列的文章列表
    - 每篇文章显示标题、摘要和发布日期
2. **文章详情页**
    - 展示单篇文章完整内容
    - 包括标题、作者、发布时间、正文和标签
3. **分类/标签页**
    - 允许用户通过分类或标签筛选文章
    - 按预设分类或标签浏览文章
4. **关于我页**
    - 静态页面展示博主个人简介
    - 技术栈和联系方式展示
5. **404页面**
    - 友好的错误提示页面
    - 提供返回首页的链接

### 后台管理 (Admin Panel)

1. **文章管理**
    - 提供文章的增删改查(CRUD)功能
2. **Markdown编辑器**
    - 集成Markdown编辑器
    - 支持文章撰写和预览功能
3. **分类与标签管理**
    - 提供分类和标签的管理功能

## 设计风格

### 主题

- 采用简洁、现代的亮色主题
- 建议使用蓝色系主色调
- 营造清新、专注的阅读氛围

### 布局

- 整体采用响应式设计
- 确保在手机、平板和桌面设备上良好体验
- 使用卡片式布局组织内容

### 交互

- 页面切换和按钮点击有平滑动画过渡
- 提升用户体验

## 开发流程规范

### 1. 后端先行

**项目结构搭建**

- 创建项目结构，初始化虚拟环境
- 使用uv管理依赖

**数据库设计**

- 设计并创建SQLite数据库模型
- 定义Article、Category、Tag等模型

**API接口实现**

- 实现所有必需的RESTful API接口
- 包括GET /api/posts, POST /api/posts等

### 2. 前端跟进

**项目初始化**

- 使用Vite初始化Vue 3项目
- 安装并配置UI组件库和Axios

**组件开发**

- 根据功能需求逐个开发Vue组件和页面
- 通过Axios调用后端API
- 实现数据驱动的前端应用

### 3. 联调与测试

- 持续进行前后端联调
- 确保数据流通顺畅
- 验证功能符合预期

## 项目目录结构建议

```
unique-wz-blog/
├── backend/              # 后端项目目录
│   ├── app/              # Flask应用代码
│   ├── migrations/       # 数据库迁移文件
│   ├── tests/            # 测试代码
│   ├── .uv/              # uv虚拟环境
│   ├── pyproject.toml    # 项目依赖配置
│   └── README.md         # 项目说明
├── frontend/             # 前端项目目录
│   ├── src/              # Vue源代码
│   │   ├── components/   # 公共组件
│   │   ├── views/        # 页面视图
│   │   ├── router/       # 路由配置
│   │   ├── store/        # 状态管理
│   │   └── main.js       # 入口文件
│   ├── public/           # 静态资源
│   ├── index.html        # 主页面
│   └── vite.config.js    # Vite配置
├── .gitignore            # Git忽略配置
└── README.md             # 项目总说明
```

## 开发环境准备

### 后端环境

```
# 安装uv（如果尚未安装）
pip install uv

# 创建项目目录
mkdir unique-wz-blog
cd unique-wz-blog

# 初始化后端项目
uv init backend
cd backend

# 创建虚拟环境并安装依赖
uv venv
source .venv/bin/activate  # Linux/Mac
# 或 .venv\Scripts\activate  # Windows

# 安装Flask和相关依赖
uv add flask flask-sqlalchemy flask-migrate
```

### 前端环境

```
# 在项目根目录创建前端项目
cd ..
uv add vite vue@next
npm create vite@latest frontend -- --template vue
cd frontend

# 安装UI组件库和Axios
npm install element-plus axios
```

## API接口设计建议

### 文章相关API

- `GET /api/posts` - 获取文章列表
- `GET /api/posts/:id` - 获取文章详情
- `POST /api/posts` - 创建新文章
- `PUT /api/posts/:id` - 更新文章
- `DELETE /api/posts/:id` - 删除文章

### 分类相关API

- `GET /api/categories` - 获取分类列表
- `POST /api/categories` - 创建分类

### 标签相关API

- `GET /api/tags` - 获取标签列表
- `POST /api/tags` - 创建标签

## 数据库模型设计

### Article模型

```
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    excerpt = db.Column(db.String(500))
    author = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    tags = db.relationship('Tag', secondary='article_tags', backref=db.backref('articles', lazy='dynamic'))
```

### Category模型

```
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(200))
```

### Tag模型

```
class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
```

## 开发注意事项

1. **代码规范**
    - 遵循PEP8 Python编码规范
    - 使用ESLint和Prettier确保前端代码质量
2. **安全性**
    - 对用户输入进行验证和清理
    - 防止SQL注入和XSS攻击
    - 后台管理需要身份验证
3. **性能优化**
    - 合理使用数据库索引
    - 前端资源进行压缩和缓存
    - 使用分页处理大量数据
4. **文档编写**
    - 为API接口编写详细的文档
    - 记录项目安装和配置步骤
    - 说明项目的使用方法

## 项目部署建议

### 开发环境

- 本地开发使用Flask内置服务器和Vite开发服务器

### 生产环境

- 后端使用Gunicorn + Nginx部署
- 前端构建为静态文件，由Nginx提供服务
- 数据库考虑升级为PostgreSQL或MySQL

## 后续扩展功能

1. **用户评论系统**
2. **文章搜索功能**
3. **访问统计分析**
4. **社交分享功能**
5. **多用户支持**
6. **移动端适配优化**

通过遵循以上开发指导文档，我们可以高效地构建出一个功能完善、性能优良的个人博客系统"unique蚊子的blog"。


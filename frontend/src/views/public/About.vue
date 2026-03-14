<script setup>
</script>

<template>
  <div class="about-page">
    <el-card class="about-card">
      <div class="about-header">
        <el-avatar :size="120" class="avatar">
          <el-icon :size="60"><User /></el-icon>
        </el-avatar>
        <h1>unique蚊子</h1>
        <p class="subtitle">全栈开发者 / 技术爱好者</p>
      </div>

      <el-divider />

      <div class="about-content">
        <h2>关于我</h2>
        <p>
          你好！我是 unique蚊子，一名热爱技术的全栈开发者。
        </p>
        <p>
          这个博客是我分享技术心得、记录学习历程的地方。
          我会在这里分享关于 Python、JavaScript、Web 开发等方面的内容。
        </p>

        <h2>技术栈</h2>
        <div class="tech-stack">
          <el-tag type="primary" class="tech-tag">Python</el-tag>
          <el-tag type="success" class="tech-tag">Flask</el-tag>
          <el-tag type="info" class="tech-tag">Vue.js</el-tag>
          <el-tag type="warning" class="tech-tag">JavaScript</el-tag>
          <el-tag type="danger" class="tech-tag">SQLite</el-tag>
        </div>

        <h2>联系方式</h2>
        <p>如果你有任何问题或者想法，欢迎通过以下方式联系我：</p>
        <ul class="contact-list">
          <li>
            <el-icon><ChatDotRound /></el-icon>
            <span>GitHub: github.com/uniquemosquito</span>
          </li>
          <li>
            <el-icon><Message /></el-icon>
            <span>Email: uniquemosquito@example.com</span>
          </li>
        </ul>
      </div>
    </el-card>
  </div>
</template>

<script>
import { User, ChatDotRound, Message } from '@element-plus/icons-vue'
export default {
  components: { User, ChatDotRound, Message }
}
</script>

<style scoped>
.about-page {
  max-width: 800px;
  margin: 0 auto;
  padding: 40px 0;
}

.about-card {
  border-radius: 12px;
}

.about-header {
  text-align: center;
  padding: 40px 20px;
}

.avatar {
  margin-bottom: 20px;
  background-color: #409eff;
}

.about-header h1 {
  font-size: 28px;
  margin-bottom: 10px;
  color: #303133;
}

.subtitle {
  color: #909399;
  font-size: 16px;
}

.about-content h2 {
  font-size: 20px;
  margin: 30px 0 15px;
  color: #303133;
}

.about-content p {
  line-height: 1.8;
  color: #606266;
  margin-bottom: 15px;
}

.tech-stack {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin: 15px 0;
}

.tech-tag {
  font-size: 14px;
  padding: 8px 16px;
}

.contact-list {
  list-style: none;
  padding: 0;
}

.contact-list li {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 10px;
  color: #606266;
}
</style>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()
const isAdminRoute = ref(false)

onMounted(() => {
  checkAdminRoute()
})

const checkAdminRoute = () => {
  isAdminRoute.value = route.path.startsWith('/admin')
}

const goHome = () => {
  router.push('/')
}

const goToAdmin = () => {
  router.push('/admin/articles')
}
</script>

<template>
  <div id="app">
    <el-container v-if="!isAdminRoute">
      <el-header>
        <div class="header-content">
          <h1 class="blog-title" @click="goHome">unique蚊子的blog</h1>
          <nav class="nav-menu">
            <router-link to="/" class="nav-link">首页</router-link>
            <router-link to="/categories" class="nav-link">分类</router-link>
            <router-link to="/tags" class="nav-link">标签</router-link>
            <router-link to="/about" class="nav-link">关于我</router-link>
            <el-button type="primary" size="small" @click="goToAdmin">管理后台</el-button>
          </nav>
        </div>
      </el-header>
      <el-main>
        <router-view />
      </el-main>
      <el-footer>
        <p>© 2026 unique蚊子的blog</p>
      </el-footer>
    </el-container>
    <router-view v-else />
  </div>
</template>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

#app {
  min-height: 100vh;
}

.el-header {
  background-color: #409eff;
  color: white;
  padding: 0;
}

.header-content {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 100%;
  padding: 0 20px;
}

.blog-title {
  cursor: pointer;
  font-size: 24px;
  margin: 0;
}

.nav-menu {
  display: flex;
  align-items: center;
  gap: 20px;
}

.nav-link {
  color: white;
  text-decoration: none;
  font-size: 16px;
}

.nav-link:hover,
.nav-link.router-link-active {
  text-decoration: underline;
}

.el-main {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.el-footer {
  text-align: center;
  padding: 20px;
  background-color: #f5f7fa;
  color: #606266;
}
</style>

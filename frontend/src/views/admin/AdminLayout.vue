<script setup>
import { computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()

const activeMenu = computed(() => {
  return route.path
})

const menuItems = [
  {
    title: '文章管理',
    path: '/admin/articles',
    icon: 'Document'
  },
  {
    title: '分类管理',
    path: '/admin/categories',
    icon: 'Folder'
  },
  {
    title: '标签管理',
    path: '/admin/tags',
    icon: 'PriceTag'
  }
]

const navigateTo = (path) => {
  router.push(path)
}

const goToFrontend = () => {
  router.push('/')
}
</script>

<template>
  <el-container class="admin-layout">
    <el-aside width="220px">
      <div class="logo">
        <h2>管理后台</h2>
      </div>
      <el-menu
        :default-active="activeMenu"
        class="admin-menu"
        router
      >
        <el-menu-item
          v-for="item in menuItems"
          :key="item.path"
          :index="item.path"
          @click="navigateTo(item.path)"
        >
          <el-icon>
            <component :is="item.icon" />
          </el-icon>
          <span>{{ item.title }}</span>
        </el-menu-item>
      </el-menu>
    </el-aside>
    <el-container>
      <el-header>
        <div class="header-content">
          <span class="header-title">unique蚊子的blog</span>
          <el-button type="primary" @click="goToFrontend">
            <el-icon><HomeFilled /></el-icon>
            前台首页
          </el-button>
        </div>
      </el-header>
      <el-main>
        <router-view />
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import { Document, Folder, PriceTag, HomeFilled } from '@element-plus/icons-vue'
export default {
  components: { Document, Folder, PriceTag, HomeFilled }
}
</script>

<style scoped>
.admin-layout {
  min-height: 100vh;
}

.el-aside {
  background-color: #304156;
  color: white;
}

.logo {
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #263445;
}

.logo h2 {
  color: white;
  font-size: 18px;
  margin: 0;
}

.admin-menu {
  border: none;
  background-color: #304156;
}

.admin-menu:not(.el-menu--collapse) {
  width: 220px;
}

.admin-menu .el-menu-item {
  color: #bfcbd9;
}

.admin-menu .el-menu-item:hover,
.admin-menu .el-menu-item.is-active {
  background-color: #263445;
  color: #409eff;
}

.el-header {
  background-color: white;
  border-bottom: 1px solid #e6e6e6;
  padding: 0 20px;
  display: flex;
  align-items: center;
}

.header-content {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.header-title {
  font-size: 18px;
  font-weight: 600;
  color: #303133;
}

.el-main {
  background-color: #f0f2f5;
  padding: 20px;
}
</style>

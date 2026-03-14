<script setup>
import { onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useArticlesStore } from '@/stores/articles'
import MarkdownViewer from '@/components/MarkdownViewer.vue'
import { ArrowLeft } from '@element-plus/icons-vue'

const route = useRoute()
const router = useRouter()
const articlesStore = useArticlesStore()

onMounted(() => {
  const id = parseInt(route.params.id)
  articlesStore.fetchArticleById(id)
})

const goBack = () => {
  router.back()
}

const formatDate = (dateStr) => {
  if (!dateStr) return ''
  const date = new Date(dateStr)
  return date.toLocaleDateString('zh-CN', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}
</script>

<template>
  <div class="article-detail">
    <div v-if="articlesStore.loading" class="loading">
      <el-skeleton :rows="10" animated />
    </div>
    <div v-else-if="!articlesStore.currentArticle" class="empty">
      <el-empty description="文章不存在" />
    </div>
    <div v-else class="article-content">
      <el-button :icon="ArrowLeft" @click="goBack" class="back-btn">
        返回
      </el-button>

      <h1 class="article-title">{{ articlesStore.currentArticle.title }}</h1>

      <div class="article-meta">
        <span class="article-author">
          <el-icon><User /></el-icon>
          {{ articlesStore.currentArticle.author }}
        </span>
        <span class="article-date">
          <el-icon><Calendar /></el-icon>
          {{ formatDate(articlesStore.currentArticle.created_at) }}
        </span>
        <el-tag v-if="articlesStore.currentArticle.category" type="success">
          {{ articlesStore.currentArticle.category.name }}
        </el-tag>
      </div>

      <div class="article-tags">
        <el-tag
          v-for="tag in articlesStore.currentArticle.tags"
          :key="tag.id"
          class="tag-item"
        >
          {{ tag.name }}
        </el-tag>
      </div>

      <div class="article-body">
        <MarkdownViewer :content="articlesStore.currentArticle.content" />
      </div>
    </div>
  </div>
</template>

<script>
import { User, Calendar } from '@element-plus/icons-vue'
export default {
  components: { User, Calendar }
}
</script>

<style scoped>
.article-detail {
  max-width: 900px;
  margin: 0 auto;
  padding: 20px 0;
}

.loading,
.empty {
  margin-top: 40px;
}

.back-btn {
  margin-bottom: 20px;
}

.article-title {
  font-size: 32px;
  margin-bottom: 20px;
  color: #303133;
}

.article-meta {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-bottom: 20px;
  padding-bottom: 20px;
  border-bottom: 1px solid #ebeef5;
  color: #909399;
  flex-wrap: wrap;
}

.article-author,
.article-date {
  display: flex;
  align-items: center;
  gap: 5px;
}

.article-tags {
  display: flex;
  gap: 10px;
  margin-bottom: 30px;
}

.tag-item {
  background-color: #f4f4f5;
  color: #909399;
  border-color: #d3d4d6;
}

.article-body {
  padding: 20px 0;
}
</style>

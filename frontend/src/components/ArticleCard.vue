<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'

const props = defineProps({
  article: {
    type: Object,
    required: true
  }
})

const router = useRouter()

const goToDetail = () => {
  router.push(`/article/${props.article.id}`)
}

const formatDate = (dateStr) => {
  if (!dateStr) return ''
  const date = new Date(dateStr)
  return date.toLocaleDateString('zh-CN', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}
</script>

<template>
  <el-card class="article-card" shadow="hover" @click="goToDetail">
    <div class="article-card-content">
      <h2 class="article-title">{{ article.title }}</h2>
      <div class="article-meta">
        <span class="article-author">{{ article.author }}</span>
        <span class="article-date">{{ formatDate(article.created_at) }}</span>
        <el-tag v-if="article.category" size="small" type="info">
          {{ article.category.name }}
        </el-tag>
      </div>
      <p class="article-excerpt">{{ article.excerpt }}</p>
      <div class="article-tags">
        <el-tag
          v-for="tag in article.tags"
          :key="tag.id"
          size="small"
          class="tag-item"
        >
          {{ tag.name }}
        </el-tag>
      </div>
    </div>
  </el-card>
</template>

<style scoped>
.article-card {
  margin-bottom: 20px;
  cursor: pointer;
  transition: transform 0.2s;
}

.article-card:hover {
  transform: translateY(-2px);
}

.article-card-content {
  padding: 10px 0;
}

.article-title {
  font-size: 20px;
  margin-bottom: 10px;
  color: #303133;
}

.article-meta {
  display: flex;
  align-items: center;
  gap: 15px;
  margin-bottom: 15px;
  color: #909399;
  font-size: 14px;
}

.article-excerpt {
  color: #606266;
  line-height: 1.6;
  margin-bottom: 15px;
}

.article-tags {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.tag-item {
  background-color: #ecf5ff;
  color: #409eff;
  border-color: #b3d8ff;
}
</style>

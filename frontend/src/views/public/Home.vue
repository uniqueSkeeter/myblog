<script setup>
import { onMounted } from 'vue'
import { useArticlesStore } from '@/stores/articles'
import ArticleCard from '@/components/ArticleCard.vue'
import { useRouter } from 'vue-router'

const articlesStore = useArticlesStore()
const router = useRouter()

onMounted(() => {
  articlesStore.fetchArticles()
})

const handlePageChange = (page) => {
  articlesStore.fetchArticles({ page })
}
</script>

<template>
  <div class="home">
    <div class="hero">
      <h1>欢迎来到 unique蚊子的blog</h1>
      <p>记录技术，分享生活</p>
    </div>

    <div class="articles-section">
      <div v-if="articlesStore.loading" class="loading">
        <el-skeleton :rows="5" animated />
      </div>
      <div v-else-if="articlesStore.articles.length === 0" class="empty">
        <el-empty description="暂无文章" />
      </div>
      <div v-else>
        <ArticleCard
          v-for="article in articlesStore.articles"
          :key="article.id"
          :article="article"
        />
        <el-pagination
          v-if="articlesStore.pages > 1"
          v-model:current-page="articlesStore.currentPage"
          :page-size="10"
          :total="articlesStore.total"
          layout="prev, pager, next"
          @current-change="handlePageChange"
          class="pagination"
        />
      </div>
    </div>
  </div>
</template>

<style scoped>
.home {
  padding: 20px 0;
}

.hero {
  text-align: center;
  padding: 60px 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border-radius: 8px;
  margin-bottom: 40px;
}

.hero h1 {
  font-size: 36px;
  margin-bottom: 10px;
}

.hero p {
  font-size: 18px;
  opacity: 0.9;
}

.articles-section {
  max-width: 800px;
  margin: 0 auto;
}

.loading,
.empty {
  margin-top: 40px;
}

.pagination {
  margin-top: 40px;
  display: flex;
  justify-content: center;
}
</style>

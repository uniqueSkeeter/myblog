<script setup>
import { onMounted, ref } from 'vue'
import { useCategoriesStore } from '@/stores/categories'
import { useArticlesStore } from '@/stores/articles'
import ArticleCard from '@/components/ArticleCard.vue'

const categoriesStore = useCategoriesStore()
const articlesStore = useArticlesStore()
const selectedCategory = ref(null)

onMounted(() => {
  categoriesStore.fetchCategories()
})

const selectCategory = async (category) => {
  selectedCategory.value = category
  if (category) {
    await articlesStore.fetchArticles({ category_id: category.id })
  } else {
    await articlesStore.fetchArticles()
  }
}
</script>

<template>
  <div class="categories-page">
    <h1>分类</h1>

    <div class="category-list">
      <el-tag
        :type="!selectedCategory ? 'primary' : 'info'"
        class="category-tag"
        @click="selectCategory(null)"
      >
        全部
      </el-tag>
      <el-tag
        v-for="category in categoriesStore.categories"
        :key="category.id"
        :type="selectedCategory?.id === category.id ? 'primary' : 'info'"
        class="category-tag"
        @click="selectCategory(category)"
      >
        {{ category.name }}
      </el-tag>
    </div>

    <div v-if="selectedCategory" class="category-info">
      <h2>{{ selectedCategory.name }}</h2>
      <p v-if="selectedCategory.description">{{ selectedCategory.description }}</p>
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
      </div>
    </div>
  </div>
</template>

<style scoped>
.categories-page {
  padding: 20px 0;
}

.categories-page h1 {
  margin-bottom: 30px;
  color: #303133;
}

.category-list {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-bottom: 30px;
}

.category-tag {
  cursor: pointer;
  font-size: 14px;
  padding: 8px 16px;
}

.category-info {
  padding: 20px;
  background-color: #f5f7fa;
  border-radius: 8px;
  margin-bottom: 30px;
}

.category-info h2 {
  margin-bottom: 10px;
  color: #303133;
}

.category-info p {
  color: #606266;
}

.articles-section {
  max-width: 800px;
  margin: 0 auto;
}

.loading,
.empty {
  margin-top: 40px;
}
</style>

<script setup>
import { onMounted, ref } from 'vue'
import { useTagsStore } from '@/stores/tags'
import { useArticlesStore } from '@/stores/articles'
import ArticleCard from '@/components/ArticleCard.vue'

const tagsStore = useTagsStore()
const articlesStore = useArticlesStore()
const selectedTag = ref(null)

onMounted(() => {
  tagsStore.fetchTags()
})

const selectTag = async (tag) => {
  selectedTag.value = tag
  if (tag) {
    await articlesStore.fetchArticles({ tag_id: tag.id })
  } else {
    await articlesStore.fetchArticles()
  }
}
</script>

<template>
  <div class="tags-page">
    <h1>标签</h1>

    <div class="tag-cloud">
      <el-tag
        :type="!selectedTag ? 'primary' : 'info'"
        class="tag-item"
        @click="selectTag(null)"
      >
        全部
      </el-tag>
      <el-tag
        v-for="tag in tagsStore.tags"
        :key="tag.id"
        :type="selectedTag?.id === tag.id ? 'primary' : 'info'"
        class="tag-item"
        @click="selectTag(tag)"
      >
        {{ tag.name }}
      </el-tag>
    </div>

    <div v-if="selectedTag" class="tag-info">
      <h2># {{ selectedTag.name }}</h2>
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
.tags-page {
  padding: 20px 0;
}

.tags-page h1 {
  margin-bottom: 30px;
  color: #303133;
}

.tag-cloud {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
  margin-bottom: 30px;
}

.tag-item {
  cursor: pointer;
  font-size: 14px;
  padding: 8px 16px;
}

.tag-info {
  padding: 20px;
  background-color: #f5f7fa;
  border-radius: 8px;
  margin-bottom: 30px;
}

.tag-info h2 {
  color: #303133;
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

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useArticlesStore } from '@/stores/articles'
import { useCategoriesStore } from '@/stores/categories'
import { useTagsStore } from '@/stores/tags'
import { ElMessage } from 'element-plus'
import { ArrowLeft } from '@element-plus/icons-vue'

const router = useRouter()
const route = useRoute()
const articlesStore = useArticlesStore()
const categoriesStore = useCategoriesStore()
const tagsStore = useTagsStore()

const isEdit = computed(() => !!route.params.id)
const pageTitle = computed(() => isEdit.value ? '编辑文章' : '新建文章')

const form = ref({
  title: '',
  content: '',
  excerpt: '',
  author: 'unique蚊子',
  category_id: null,
  tag_ids: []
})

const loading = ref(false)

onMounted(async () => {
  await Promise.all([
    categoriesStore.fetchCategories(),
    tagsStore.fetchTags()
  ])

  if (isEdit.value) {
    await articlesStore.fetchArticleById(parseInt(route.params.id))
    const article = articlesStore.currentArticle
    if (article) {
      form.value = {
        title: article.title,
        content: article.content,
        excerpt: article.excerpt || '',
        author: article.author,
        category_id: article.category_id,
        tag_ids: article.tags.map(t => t.id)
      }
    }
  }
})

const handleSubmit = async () => {
  if (!form.value.title || !form.value.content) {
    ElMessage.warning('请填写标题和内容')
    return
  }

  loading.value = true
  try {
    if (isEdit.value) {
      await articlesStore.updateArticle(parseInt(route.params.id), form.value)
      ElMessage.success('更新成功')
    } else {
      await articlesStore.createArticle(form.value)
      ElMessage.success('创建成功')
    }
    router.push('/admin/articles')
  } catch (error) {
    ElMessage.error(isEdit.value ? '更新失败' : '创建失败')
  } finally {
    loading.value = false
  }
}

const goBack = () => {
  router.back()
}
</script>

<template>
  <div class="article-edit">
    <div class="page-header">
      <el-button :icon="ArrowLeft" @click="goBack">返回</el-button>
      <h1>{{ pageTitle }}</h1>
    </div>

    <el-card>
      <el-form :model="form" label-width="100px">
        <el-form-item label="标题">
          <el-input v-model="form.title" placeholder="请输入文章标题" />
        </el-form-item>

        <el-form-item label="作者">
          <el-input v-model="form.author" placeholder="请输入作者" />
        </el-form-item>

        <el-form-item label="分类">
          <el-select v-model="form.category_id" placeholder="请选择分类" clearable style="width: 100%">
            <el-option
              v-for="category in categoriesStore.categories"
              :key="category.id"
              :label="category.name"
              :value="category.id"
            />
          </el-select>
        </el-form-item>

        <el-form-item label="标签">
          <el-select v-model="form.tag_ids" multiple placeholder="请选择标签" style="width: 100%">
            <el-option
              v-for="tag in tagsStore.tags"
              :key="tag.id"
              :label="tag.name"
              :value="tag.id"
            />
          </el-select>
        </el-form-item>

        <el-form-item label="摘要">
          <el-input
            v-model="form.excerpt"
            type="textarea"
            :rows="3"
            placeholder="请输入文章摘要（可选，不填则自动从内容截取）"
          />
        </el-form-item>

        <el-form-item label="内容">
          <el-input
            v-model="form.content"
            type="textarea"
            :rows="20"
            placeholder="请输入文章内容（支持 Markdown）"
          />
        </el-form-item>

        <el-form-item>
          <el-button type="primary" :loading="loading" @click="handleSubmit">
            {{ isEdit ? '更新' : '创建' }}
          </el-button>
          <el-button @click="goBack">取消</el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<style scoped>
.article-edit {
  padding: 0;
}

.page-header {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-bottom: 20px;
}

.page-header h1 {
  margin: 0;
  font-size: 24px;
  color: #303133;
}
</style>

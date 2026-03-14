<script setup>
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useArticlesStore } from '@/stores/articles'
import { ElMessage, ElMessageBox } from 'element-plus'
import { Edit, Delete, Plus } from '@element-plus/icons-vue'

const router = useRouter()
const articlesStore = useArticlesStore()

const formatDate = (dateStr) => {
  if (!dateStr) return ''
  const date = new Date(dateStr)
  return date.toLocaleDateString('zh-CN', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit'
  })
}

onMounted(() => {
  articlesStore.fetchArticles({ per_page: 50 })
})

const handleEdit = (article) => {
  router.push(`/admin/articles/${article.id}/edit`)
}

const handleDelete = async (article) => {
  try {
    await ElMessageBox.confirm(
      `确定要删除文章"${article.title}"吗？`,
      '确认删除',
      {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }
    )
    await articlesStore.deleteArticle(article.id)
    ElMessage.success('删除成功')
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('删除失败')
    }
  }
}

const handleCreate = () => {
  router.push('/admin/articles/new')
}
</script>

<template>
  <div class="article-list">
    <div class="page-header">
      <h1>文章管理</h1>
      <el-button type="primary" :icon="Plus" @click="handleCreate">
        新建文章
      </el-button>
    </div>

    <el-card>
      <el-table :data="articlesStore.articles" v-loading="articlesStore.loading" stripe>
        <el-table-column prop="id" label="ID" width="80" />
        <el-table-column prop="title" label="标题" min-width="250" />
        <el-table-column prop="author" label="作者" width="120" />
        <el-table-column label="分类" width="150">
          <template #default="{ row }">
            <el-tag v-if="row.category" size="small" type="info">
              {{ row.category.name }}
            </el-tag>
            <span v-else>-</span>
          </template>
        </el-table-column>
        <el-table-column label="创建时间" width="180">
          <template #default="{ row }">
            {{ formatDate(row.created_at) }}
          </template>
        </el-table-column>
        <el-table-column label="操作" width="150" fixed="right">
          <template #default="{ row }">
            <el-button
              type="primary"
              size="small"
              :icon="Edit"
              @click="handleEdit(row)"
            >
              编辑
            </el-button>
            <el-button
              type="danger"
              size="small"
              :icon="Delete"
              @click="handleDelete(row)"
            >
              删除
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>
  </div>
</template>

<style scoped>
.article-list {
  padding: 0;
}

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.page-header h1 {
  margin: 0;
  font-size: 24px;
  color: #303133;
}
</style>

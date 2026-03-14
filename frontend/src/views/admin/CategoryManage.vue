<script setup>
import { onMounted, ref } from 'vue'
import { useCategoriesStore } from '@/stores/categories'
import { ElMessage, ElMessageBox } from 'element-plus'
import { Edit, Delete, Plus } from '@element-plus/icons-vue'

const categoriesStore = useCategoriesStore()

const dialogVisible = ref(false)
const isEdit = ref(false)
const currentId = ref(null)
const form = ref({
  name: '',
  description: ''
})

onMounted(() => {
  categoriesStore.fetchCategories()
})

const handleCreate = () => {
  isEdit.value = false
  currentId.value = null
  form.value = { name: '', description: '' }
  dialogVisible.value = true
}

const handleEdit = (category) => {
  isEdit.value = true
  currentId.value = category.id
  form.value = { name: category.name, description: category.description || '' }
  dialogVisible.value = true
}

const handleDelete = async (category) => {
  try {
    await ElMessageBox.confirm(
      `确定要删除分类"${category.name}"吗？`,
      '确认删除',
      {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }
    )
    await categoriesStore.deleteCategory(category.id)
    ElMessage.success('删除成功')
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('删除失败')
    }
  }
}

const handleSubmit = async () => {
  if (!form.value.name) {
    ElMessage.warning('请输入分类名称')
    return
  }

  try {
    if (isEdit.value) {
      await categoriesStore.updateCategory(currentId.value, form.value)
      ElMessage.success('更新成功')
    } else {
      await categoriesStore.createCategory(form.value)
      ElMessage.success('创建成功')
    }
    dialogVisible.value = false
  } catch (error) {
    ElMessage.error(isEdit.value ? '更新失败' : '创建失败')
  }
}
</script>

<template>
  <div class="category-manage">
    <div class="page-header">
      <h1>分类管理</h1>
      <el-button type="primary" :icon="Plus" @click="handleCreate">
        新建分类
      </el-button>
    </div>

    <el-card>
      <el-table :data="categoriesStore.categories" v-loading="categoriesStore.loading" stripe>
        <el-table-column prop="id" label="ID" width="80" />
        <el-table-column prop="name" label="名称" min-width="200" />
        <el-table-column prop="description" label="描述" min-width="300" />
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

    <el-dialog
      v-model="dialogVisible"
      :title="isEdit ? '编辑分类' : '新建分类'"
      width="500px"
    >
      <el-form :model="form" label-width="80px">
        <el-form-item label="名称">
          <el-input v-model="form.name" placeholder="请输入分类名称" />
        </el-form-item>
        <el-form-item label="描述">
          <el-input
            v-model="form.description"
            type="textarea"
            :rows="3"
            placeholder="请输入分类描述"
          />
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="dialogVisible = false">取消</el-button>
        <el-button type="primary" @click="handleSubmit">确定</el-button>
      </template>
    </el-dialog>
  </div>
</template>

<style scoped>
.category-manage {
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

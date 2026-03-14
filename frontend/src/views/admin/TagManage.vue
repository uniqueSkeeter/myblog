<script setup>
import { onMounted, ref } from 'vue'
import { useTagsStore } from '@/stores/tags'
import { ElMessage, ElMessageBox } from 'element-plus'
import { Edit, Delete, Plus } from '@element-plus/icons-vue'

const tagsStore = useTagsStore()

const dialogVisible = ref(false)
const isEdit = ref(false)
const currentId = ref(null)
const form = ref({
  name: ''
})

onMounted(() => {
  tagsStore.fetchTags()
})

const handleCreate = () => {
  isEdit.value = false
  currentId.value = null
  form.value = { name: '' }
  dialogVisible.value = true
}

const handleEdit = (tag) => {
  isEdit.value = true
  currentId.value = tag.id
  form.value = { name: tag.name }
  dialogVisible.value = true
}

const handleDelete = async (tag) => {
  try {
    await ElMessageBox.confirm(
      `确定要删除标签"${tag.name}"吗？`,
      '确认删除',
      {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }
    )
    await tagsStore.deleteTag(tag.id)
    ElMessage.success('删除成功')
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('删除失败')
    }
  }
}

const handleSubmit = async () => {
  if (!form.value.name) {
    ElMessage.warning('请输入标签名称')
    return
  }

  try {
    if (isEdit.value) {
      await tagsStore.updateTag(currentId.value, form.value)
      ElMessage.success('更新成功')
    } else {
      await tagsStore.createTag(form.value)
      ElMessage.success('创建成功')
    }
    dialogVisible.value = false
  } catch (error) {
    ElMessage.error(isEdit.value ? '更新失败' : '创建失败')
  }
}
</script>

<template>
  <div class="tag-manage">
    <div class="page-header">
      <h1>标签管理</h1>
      <el-button type="primary" :icon="Plus" @click="handleCreate">
        新建标签
      </el-button>
    </div>

    <el-card>
      <el-table :data="tagsStore.tags" v-loading="tagsStore.loading" stripe>
        <el-table-column prop="id" label="ID" width="80" />
        <el-table-column prop="name" label="名称" min-width="300" />
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
      :title="isEdit ? '编辑标签' : '新建标签'"
      width="500px"
    >
      <el-form :model="form" label-width="80px">
        <el-form-item label="名称">
          <el-input v-model="form.name" placeholder="请输入标签名称" />
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
.tag-manage {
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

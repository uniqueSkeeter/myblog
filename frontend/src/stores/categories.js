import { defineStore } from 'pinia'
import { ref } from 'vue'
import { categoriesApi } from '@/api'

export const useCategoriesStore = defineStore('categories', () => {
  const categories = ref([])
  const loading = ref(false)

  const fetchCategories = async () => {
    loading.value = true
    try {
      const response = await categoriesApi.getCategories()
      categories.value = response
    } catch (error) {
      console.error('Failed to fetch categories:', error)
    } finally {
      loading.value = false
    }
  }

  const createCategory = async (data) => {
    loading.value = true
    try {
      const response = await categoriesApi.createCategory(data)
      categories.value.push(response)
      return response
    } catch (error) {
      console.error('Failed to create category:', error)
      throw error
    } finally {
      loading.value = false
    }
  }

  const updateCategory = async (id, data) => {
    loading.value = true
    try {
      const response = await categoriesApi.updateCategory(id, data)
      const index = categories.value.findIndex(c => c.id === id)
      if (index !== -1) {
        categories.value[index] = response
      }
      return response
    } catch (error) {
      console.error('Failed to update category:', error)
      throw error
    } finally {
      loading.value = false
    }
  }

  const deleteCategory = async (id) => {
    loading.value = true
    try {
      await categoriesApi.deleteCategory(id)
      categories.value = categories.value.filter(c => c.id !== id)
    } catch (error) {
      console.error('Failed to delete category:', error)
      throw error
    } finally {
      loading.value = false
    }
  }

  return {
    categories,
    loading,
    fetchCategories,
    createCategory,
    updateCategory,
    deleteCategory
  }
})

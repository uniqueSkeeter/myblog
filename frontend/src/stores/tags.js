import { defineStore } from 'pinia'
import { ref } from 'vue'
import { tagsApi } from '@/api'

export const useTagsStore = defineStore('tags', () => {
  const tags = ref([])
  const loading = ref(false)

  const fetchTags = async () => {
    loading.value = true
    try {
      const response = await tagsApi.getTags()
      tags.value = response
    } catch (error) {
      console.error('Failed to fetch tags:', error)
    } finally {
      loading.value = false
    }
  }

  const createTag = async (data) => {
    loading.value = true
    try {
      const response = await tagsApi.createTag(data)
      tags.value.push(response)
      return response
    } catch (error) {
      console.error('Failed to create tag:', error)
      throw error
    } finally {
      loading.value = false
    }
  }

  const updateTag = async (id, data) => {
    loading.value = true
    try {
      const response = await tagsApi.updateTag(id, data)
      const index = tags.value.findIndex(t => t.id === id)
      if (index !== -1) {
        tags.value[index] = response
      }
      return response
    } catch (error) {
      console.error('Failed to update tag:', error)
      throw error
    } finally {
      loading.value = false
    }
  }

  const deleteTag = async (id) => {
    loading.value = true
    try {
      await tagsApi.deleteTag(id)
      tags.value = tags.value.filter(t => t.id !== id)
    } catch (error) {
      console.error('Failed to delete tag:', error)
      throw error
    } finally {
      loading.value = false
    }
  }

  return {
    tags,
    loading,
    fetchTags,
    createTag,
    updateTag,
    deleteTag
  }
})

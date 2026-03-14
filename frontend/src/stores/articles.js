import { defineStore } from 'pinia'
import { ref } from 'vue'
import { articlesApi } from '@/api'

export const useArticlesStore = defineStore('articles', () => {
  const articles = ref([])
  const currentArticle = ref(null)
  const loading = ref(false)
  const total = ref(0)
  const pages = ref(0)
  const currentPage = ref(1)

  const fetchArticles = async (params = {}) => {
    loading.value = true
    try {
      const response = await articlesApi.getArticles(params)
      articles.value = response.articles
      total.value = response.total
      pages.value = response.pages
      currentPage.value = response.current_page
    } catch (error) {
      console.error('Failed to fetch articles:', error)
    } finally {
      loading.value = false
    }
  }

  const fetchArticleById = async (id) => {
    loading.value = true
    try {
      const response = await articlesApi.getArticle(id)
      currentArticle.value = response
    } catch (error) {
      console.error('Failed to fetch article:', error)
    } finally {
      loading.value = false
    }
  }

  const createArticle = async (data) => {
    loading.value = true
    try {
      const response = await articlesApi.createArticle(data)
      return response
    } catch (error) {
      console.error('Failed to create article:', error)
      throw error
    } finally {
      loading.value = false
    }
  }

  const updateArticle = async (id, data) => {
    loading.value = true
    try {
      const response = await articlesApi.updateArticle(id, data)
      return response
    } catch (error) {
      console.error('Failed to update article:', error)
      throw error
    } finally {
      loading.value = false
    }
  }

  const deleteArticle = async (id) => {
    loading.value = true
    try {
      await articlesApi.deleteArticle(id)
      articles.value = articles.value.filter(a => a.id !== id)
    } catch (error) {
      console.error('Failed to delete article:', error)
      throw error
    } finally {
      loading.value = false
    }
  }

  return {
    articles,
    currentArticle,
    loading,
    total,
    pages,
    currentPage,
    fetchArticles,
    fetchArticleById,
    createArticle,
    updateArticle,
    deleteArticle
  }
})

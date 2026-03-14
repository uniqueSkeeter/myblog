import request from '@/utils/request'

export const articlesApi = {
  getArticles(params) {
    return request({
      url: '/articles',
      method: 'get',
      params
    })
  },

  getArticle(id) {
    return request({
      url: `/articles/${id}`,
      method: 'get'
    })
  },

  createArticle(data) {
    return request({
      url: '/articles',
      method: 'post',
      data
    })
  },

  updateArticle(id, data) {
    return request({
      url: `/articles/${id}`,
      method: 'put',
      data
    })
  },

  deleteArticle(id) {
    return request({
      url: `/articles/${id}`,
      method: 'delete'
    })
  }
}

export const categoriesApi = {
  getCategories() {
    return request({
      url: '/categories',
      method: 'get'
    })
  },

  createCategory(data) {
    return request({
      url: '/categories',
      method: 'post',
      data
    })
  },

  updateCategory(id, data) {
    return request({
      url: `/categories/${id}`,
      method: 'put',
      data
    })
  },

  deleteCategory(id) {
    return request({
      url: `/categories/${id}`,
      method: 'delete'
    })
  },

  getArticlesByCategory(id, params) {
    return request({
      url: `/categories/${id}/articles`,
      method: 'get',
      params
    })
  }
}

export const tagsApi = {
  getTags() {
    return request({
      url: '/tags',
      method: 'get'
    })
  },

  createTag(data) {
    return request({
      url: '/tags',
      method: 'post',
      data
    })
  },

  updateTag(id, data) {
    return request({
      url: `/tags/${id}`,
      method: 'put',
      data
    })
  },

  deleteTag(id) {
    return request({
      url: `/tags/${id}`,
      method: 'delete'
    })
  },

  getArticlesByTag(id, params) {
    return request({
      url: `/tags/${id}/articles`,
      method: 'get',
      params
    })
  }
}

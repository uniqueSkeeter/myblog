import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/public/Home.vue')
  },
  {
    path: '/article/:id',
    name: 'ArticleDetail',
    component: () => import('@/views/public/ArticleDetail.vue')
  },
  {
    path: '/categories',
    name: 'Categories',
    component: () => import('@/views/public/Categories.vue')
  },
  {
    path: '/tags',
    name: 'Tags',
    component: () => import('@/views/public/Tags.vue')
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('@/views/public/About.vue')
  },
  {
    path: '/admin',
    redirect: '/admin/articles'
  },
  {
    path: '/admin',
    component: () => import('@/views/admin/AdminLayout.vue'),
    children: [
      {
        path: 'articles',
        name: 'AdminArticles',
        component: () => import('@/views/admin/ArticleList.vue')
      },
      {
        path: 'articles/new',
        name: 'AdminArticleNew',
        component: () => import('@/views/admin/ArticleEdit.vue')
      },
      {
        path: 'articles/:id/edit',
        name: 'AdminArticleEdit',
        component: () => import('@/views/admin/ArticleEdit.vue')
      },
      {
        path: 'categories',
        name: 'AdminCategories',
        component: () => import('@/views/admin/CategoryManage.vue')
      },
      {
        path: 'tags',
        name: 'AdminTags',
        component: () => import('@/views/admin/TagManage.vue')
      }
    ]
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('@/views/public/NotFound.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router

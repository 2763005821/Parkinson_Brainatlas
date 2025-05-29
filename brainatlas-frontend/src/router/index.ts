import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'
import Home from '../views/Home.vue'
import Dataset from '../views/Dataset.vue'
import GeneSearch from '../views/GeneSearch.vue'
import Atlas from '../views/Atlas.vue'
import Help from '../views/Help.vue'

const routes: Array<RouteRecordRaw> = [
  { path: '/', name: 'Home', component: Home },
  { path: '/dataset', name: 'Dataset', component: Dataset },
  { path: '/gene-search', name: 'GeneSearch', component: GeneSearch },
  { path: '/atlas', name: 'Atlas', component: Atlas },
  { path: '/help', name: 'Help', component: Help },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router



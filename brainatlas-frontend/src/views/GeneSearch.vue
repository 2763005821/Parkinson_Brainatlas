<!-- filepath: e:\文档\Computer\Web_Project\demo\learn_Vue_Django\first_try\brainatlas-frontend\src\views\GeneSearch.vue -->
<template>
  <div class="page-wrapper">
    <!-- 顶部导航栏 -->
    <header class="navbar">
      <div class="logo">🧠 Parkinson Atlas</div>
      <nav>
        <ul>
          <li><router-link to="/">Home</router-link></li>
          <li><router-link to="/dataset">Dataset</router-link></li>
          <li><router-link to="/atlas">Atlas</router-link></li>
          <li><router-link to="/gene-search">Gene Search</router-link></li>
          <li><router-link to="/about">About</router-link></li>
          <li><router-link to="/help">Help</router-link></li>
        </ul>
      </nav>
    </header>

    <div class="gene-search-container">
      <h2>Gene Search</h2>
      <form @submit.prevent="fetchData">
        <input
          v-model="geneName"
          type="text"
          placeholder="请输入基因名称"
          class="search-input"
        />
        <button type="submit">查询</button>
      </form>

      <table v-if="cellData.length">
        <thead>
          <tr>
            <th @click="sortBy('cell_type')">
              Cell Type
              <span v-if="sortKey==='cell_type'">{{ sortAsc ? '↑' : '↓' }}</span>
            </th>
            <th @click="sortBy('gene')">
              Gene
              <span v-if="sortKey==='gene'">{{ sortAsc ? '↑' : '↓' }}</span>
            </th>
            <th @click="sortBy('avg_log2FC')">
              avg_log2FC
              <span v-if="sortKey==='avg_log2FC'">{{ sortAsc ? '↑' : '↓' }}</span>
            </th>
            <th @click="sortBy('pct_1')">
              pct_1
              <span v-if="sortKey==='pct_1'">{{ sortAsc ? '↑' : '↓' }}</span>
            </th>
            <th @click="sortBy('pct_2')">
              pct_2
              <span v-if="sortKey==='pct_2'">{{ sortAsc ? '↑' : '↓' }}</span>
            </th>
            <th @click="sortBy('p_value')">
              p-value
              <span v-if="sortKey==='p_value'">{{ sortAsc ? '↑' : '↓' }}</span>
            </th>
            <th @click="sortBy('p_val_adj')">
              p_val_adj
              <span v-if="sortKey==='p_val_adj'">{{ sortAsc ? '↑' : '↓' }}</span>
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in sortedData" :key="item.id">
            <td>{{ item.cell_type }}</td>
            <td>{{ item.gene }}</td>
            <td>{{ item.avg_log2FC }}</td>
            <td>{{ item.pct_1 }}</td>
            <td>{{ item.pct_2 }}</td>
            <td>{{ item.p_value }}</td>
            <td>{{ item.p_val_adj }}</td>
          </tr>
        </tbody>
      </table>
      <div v-else-if="searched">未找到相关数据</div>
    </div>

    <!-- 页脚 -->
    <footer class="footer">
      © 2025 Parkinson Cell Atlas · Designed by Your Team
    </footer>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'

interface CellAtlas {
  id: number
  cell_type: string
  gene: string
  avg_log2FC: number
  pct_1: number
  pct_2: number
  p_value: number
  p_val_adj: number
}

const geneName = ref('')
const cellData = ref<CellAtlas[]>([])
const searched = ref(false)

const sortKey = ref<keyof CellAtlas | ''>('')
const sortAsc = ref(true)

const sortBy = (key: keyof CellAtlas) => {
  if (sortKey.value === key) {
    sortAsc.value = !sortAsc.value
  } else {
    sortKey.value = key
    sortAsc.value = true
  }
}

const sortedData = computed(() => {
  if (!sortKey.value) return cellData.value
  return [...cellData.value].sort((a, b) => {
    const valA = a[sortKey.value]
    const valB = b[sortKey.value]
    if (typeof valA === 'number' && typeof valB === 'number') {
      return sortAsc.value ? valA - valB : valB - valA
    }
    return sortAsc.value
      ? String(valA).localeCompare(String(valB))
      : String(valB).localeCompare(String(valA))
  })
})


const fetchData = async () => {
  try {
    let url = 'http://127.0.0.1:8000/api/cellatlas/'
    if (geneName.value.trim()) {
      url += `?gene=${encodeURIComponent(geneName.value)}`
    }
    const response = await axios.get<CellAtlas[]>(url)
    cellData.value = response.data
    searched.value = true
  } catch (error) {
    cellData.value = []
    searched.value = true
    console.error('Error fetching data:', error)
  }
}

// 页面加载时自动获取全部数据
onMounted(fetchData)
</script>

<style scoped>
.page-wrapper {
  font-family: "Segoe UI", sans-serif;
  color: #333;
  min-height: 100vh;
  background: #f8f8f8;
}
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #002147;
  color: white;
  padding: 1rem 2rem;
}
.logo {
  font-size: 1.5rem;
  font-weight: bold;
}
.navbar nav ul {
  display: flex;
  list-style: none;
  gap: 1.5rem;
  margin: 0;
  padding: 0;
}
.navbar nav ul li a {
  color: white;
  text-decoration: none;
  font-weight: 500;
}
.navbar nav ul li a.router-link-active {
  color: #ffd700;
}
.gene-search-container {
  padding: 2rem;
}
h2 {
  margin-bottom: 1rem;
}
form {
  margin-bottom: 1.5rem;
}
.search-input {
  padding: 0.5rem;
  font-size: 1rem;
  width: 220px;
  margin-right: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}
button {
  background-color: #4677f5;
  color: white;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
table {
  width: 100%;
  border-collapse: collapse;
  user-select: none;
}
th, td {
  border: 1px solid #ccc;
  padding: 0.5rem;
  text-align: center;
}
th {
  background-color: #f0f0f0;
  cursor: pointer;
}
th span {
  margin-left: 4px;
  font-size: 0.9em;
}
.footer {
  background-color: #f2f2f2;
  text-align: center;
  padding: 1rem;
  font-size: 0.9rem;
  margin-top: 2rem;
}
</style>
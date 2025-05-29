<!-- filepath: e:\文档\Computer\Web_Project\demo\learn_Vue_Django\first_try\brainatlas-frontend\src\views\Dataset.vue -->
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

    <div class="dataset-container">
      <h2>Parkinson Cell Atlas Dataset</h2>
      <table v-if="cellData.length">
        <thead>
          <tr>
            <th>Cell Type</th>
            <th>Gene</th>
            <th>avg_log2FC</th>
            <th>pct_1</th>
            <th>pct_2</th>
            <th>p-value</th>
            <th>p_val_adj</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in cellData" :key="item.id">
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
    </div>

    <!-- 页脚 -->
    <footer class="footer">
      © 2025 Parkinson Cell Atlas · Designed by Your Team
    </footer>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
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

const cellData = ref<CellAtlas[]>([])

const fetchData = async () => {
  try {
    const response = await axios.get<CellAtlas[]>('http://127.0.0.1:8000/api/cellatlas/')
    cellData.value = response.data
  } catch (error) {
    console.error('Error fetching data:', error)
  }
}

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
.dataset-container {
  padding: 2rem;
}
h2 {
  margin-bottom: 1rem;
}
table {
  width: 100%;
  border-collapse: collapse;
}
th, td {
  border: 1px solid #ccc;
  padding: 0.5rem;
  text-align: center;
}
th {
  background-color: #f0f0f0;
}
.footer {
  background-color: #f2f2f2;
  text-align: center;
  padding: 1rem;
  font-size: 0.9rem;
  margin-top: 2rem;
}
</style>
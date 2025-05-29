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

    <!-- 引导区 -->
    <section class="hero">
      <h1>Parkinson’s Disease Single-Cell Atlas</h1>
      <p>
        An integrated single-cell transcriptomic platform revealing gene expression dynamics across brain cell types in Parkinson's Disease.
      </p>
      <button @click="goToAtlas">Explore Dataset</button>
    </section>

    <!-- 功能卡片入口区 -->
    <section class="features">
      <div class="card" @click="goToDataset">
        <h3>🧬 View Cell Atlas</h3>
        <p>Browse differential expression results across cell types.</p>
      </div>
      <div class="card" @click="goToGeneSearch">
        <h3>🔎 Gene Search</h3>
        <p>Query genes to view cell-type-specific expression.</p>
      </div>
      <div class="card">
        <h3>📦 Download</h3>
        <p>Access processed data and gene lists.</p>
      </div>
    </section>

    <!-- 页脚 -->
    <footer class="footer">
      © 2025 Parkinson Cell Atlas · Designed by Your Team
    </footer>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()
const goToDataset = () => {
  router.push('/dataset')
}
const goToGeneSearch = () => {
  // 这里可以实现跳转到 gene search 页面
  router.push('/gene-search')
}
const goToAtlas = () => {
  router.push('/atlas')
}
</script>

<style scoped>
.page-wrapper {
  font-family: "Segoe UI", sans-serif;
  color: #333;
}

/* 顶部导航 */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #002147;
  color: white;
  padding: 1rem 2rem;
}
.navbar .logo {
  font-size: 1.5rem;
  font-weight: bold;
}
.navbar nav ul {
  display: flex;
  list-style: none;
  gap: 1.5rem;
}
.navbar nav ul li a {
  color: white;
  text-decoration: none;
}

/* 引导区 */
.hero {
  background: linear-gradient(180deg, #e0eaff, #ffffff);
  text-align: center;
  padding: 4rem 2rem;
}
.hero h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}
.hero p {
  font-size: 1.1rem;
  max-width: 700px;
  margin: 0 auto 2rem;
}
.hero button {
  padding: 0.7rem 1.5rem;
  font-size: 1rem;
  background-color: #3b82f6;
  color: white;
  border: none;
  border-radius: 5px;
}

/* 功能入口卡片 */
.features {
  display: flex;
  justify-content: center;
  gap: 2rem;
  padding: 3rem 2rem;
  flex-wrap: wrap;
}
.card {
  width: 250px;
  background-color: #f9f9f9;
  border-radius: 12px;
  box-shadow: 0 0 10px rgba(0,0,0,0.05);
  padding: 1.5rem;
  text-align: center;
  cursor: pointer;
  transition: transform 0.3s ease;
}
.card:hover {
  transform: translateY(-5px);
}

/* 页脚 */
.footer {
  background-color: #f2f2f2;
  text-align: center;
  padding: 1rem;
  font-size: 0.9rem;
  margin-top: 2rem;
}
</style>

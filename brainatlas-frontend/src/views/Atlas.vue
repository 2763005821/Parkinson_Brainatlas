<!-- filepath: e:\文档\Computer\Web_Project\demo\learn_Vue_Django\first_try\brainatlas-frontend\src\views\Atlas.vue -->
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

    <!-- 图谱内容区 -->
    <section class="atlas-section">
      <h2>Cell Type UMAP Atlas</h2>
      <div class="umap-img-wrapper">
        <img src="/DimPlot_UMAP2_annotation.png" alt="Cell Type UMAP" class="umap-img" />
      </div>
      <p class="caption">UMAP projection of cell types (数据来源: GSE157783)</p>
    </section>

    <!-- 页脚 -->
    <footer class="footer">
      © 2025 Parkinson Cell Atlas · Designed by Your Team
    </footer>
  </div>
</template>

<script setup>
// 无需特殊逻辑
</script>

<style scoped>
.page-wrapper {
  font-family: "Segoe UI", sans-serif;
  color: #333;
  min-height: 100vh;
  background: #f8f8f8;
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

/* 图谱内容区 */
.atlas-section {
  text-align: center;
  padding: 3rem 1rem 2rem 1rem;
}
.umap-img-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 2rem 0;
}
.umap-img {
  max-width: 90vw;
  max-height: 70vh;
  border-radius: 12px;
  box-shadow: 0 0 12px rgba(0,0,0,0.08);
  background: #fff;
}
.caption {
  color: #666;
  font-size: 1rem;
  margin-top: 1rem;
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
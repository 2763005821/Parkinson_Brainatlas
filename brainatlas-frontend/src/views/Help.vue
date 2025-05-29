<!-- filepath: e:\文档\Computer\Web_Project\demo\learn_Vue_Django\first_try\brainatlas-frontend\src\views\Help.vue -->
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

    <!-- 帮助内容区 -->
    <section class="help-section">
      <h2>帮助文档</h2>
      <p class="intro">
        <strong>Parkinson's brainAtlas</strong> 网站是一个面向帕金森病单细胞转录组数据的可视化与分析平台，旨在帮助用户便捷地浏览、查询和下载相关数据。
      </p>

      <div class="help-block">
        <h3>网站结构与功能</h3>
        <ul>
          <li><strong>主页（Home）</strong>：包含导航栏、欢迎界面、主体功能入口和相关信息。导航栏可快速跳转至各功能页面。欢迎区展示网站简介，帮助用户快速了解平台内容与使用方法。底部功能区包括数据集浏览、基因搜索和帮助等入口。</li>
          <li><strong>数据集（Dataset）</strong>：浏览帕金森病相关的单细胞差异表达结果，支持表格展示与数据下载。</li>
          <li><strong>图谱（Atlas）</strong>：可视化展示细胞类型UMAP分布图，帮助用户直观了解不同细胞类型的空间分布。</li>
          <li><strong>帮助（Help）</strong>：当前页面，介绍网站结构、功能模块及使用方法。</li>
        </ul>
      </div>

      <div class="help-block">
        <h3>使用指南</h3>
        <ol>
          <li>通过顶部导航栏可随时切换至主页、数据集、图谱和帮助页面。</li>
          <li>主页中点击“Explore Dataset”可直接跳转至图谱页面，开始浏览和探索。</li>
          <li>点击底部功能卡片，可快速进入数据集浏览、基因搜索等功能。</li>
          <li>如需进一步帮助，可随时返回本页面查阅。</li>
        </ol>
      </div>

      <div class="help-block">
        <h3>作者信息</h3>
        <ul>
          <li>作者：范宇晨</li>
          <li>专业：生物信息学</li>
          <li>学校：华北理工大学</li>
          <li>院系：生命科学学院</li>
        </ul>
      </div>
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

/* 帮助内容区 */
.help-section {
  max-width: 900px;
  margin: 2.5rem auto 2rem auto;
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 0 12px rgba(0,0,0,0.06);
  padding: 2.5rem 2rem;
}
.help-section h2 {
  text-align: center;
  margin-bottom: 1.5rem;
  color: #002147;
}
.intro {
  font-size: 1.1rem;
  margin-bottom: 2rem;
  text-align: center;
}
.help-block {
  margin-bottom: 2rem;
}
.help-block h3 {
  color: #3b82f6;
  margin-bottom: 0.7rem;
}
.help-block ul,
.help-block ol {
  margin-left: 1.2rem;
  margin-bottom: 0.5rem;
}
.help-block li {
  margin-bottom: 0.5rem;
  line-height: 1.7;
}

/* 页脚 */
.footer {
  background-color: #f2f2f2;
  text-align: center;
  padding: 1rem;
  font-size: 0.9rem;
  margin-top: 2rem;
  border-radius: 0 0 12px 12px;
}
</style>
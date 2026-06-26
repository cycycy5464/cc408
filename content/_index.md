---
title: "CC408"
date: 2026-06-25
---

<div class="hero-container">
  <h1 class="hero-title">
    CC408
    <span class="gradient-text">408考研 · 知识整理平台</span>
  </h1>
  <p class="hero-subtitle">系统化知识整理 · 历年真题练习 · 可视化知识图谱</p>
  <div class="hero-buttons">
    <a href="/docs/" class="btn-outline">📖 知识点</a>
    <a href="/exam/" class="btn-solid">✏️ 刷题中心</a>
    <a href="/graph/" class="btn-outline">🗺️ 知识图谱</a>
  </div>
</div>

<style>
.hero-container {
  text-align: center;
  padding: 8rem 2rem 6rem;
  min-height: 70vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background:
    radial-gradient(circle at 20% 50%, rgba(88, 214, 192, 0.08) 0%, transparent 50%),
    radial-gradient(circle at 80% 50%, rgba(59, 130, 246, 0.08) 0%, transparent 50%);
}
.hero-title {
  font-size: 3.5rem;
  margin-bottom: 1rem;
  line-height: 1.3;
}
.hero-subtitle {
  font-size: 1.25rem;
  color: var(--text-secondary);
  margin-bottom: 2.5rem;
}
.hero-buttons {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  justify-content: center;
}
</style>

---

<div style="max-width: 900px; margin: 0 auto; padding: 2rem 1rem;">

## 📖 最近更新

<div class="card-grid">

{{ range first 6 (where .Site.RegularPages "Section" "docs") }}
<a href="{{ .RelPermalink }}" class="card-glass" style="padding: 1.5rem; text-decoration: none; color: var(--text-primary);">
  <div style="font-weight: 600; margin-bottom: 0.5rem;">{{ .Title }}</div>
  <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
    {{ with .Params.difficulty }}
    <span class="difficulty-stars">
      {{ $d := . }}
      {{ range seq 1 3 }}{{ if le . $d }}★{{ else }}<span class="empty">☆</span>{{ end }}{{ end }}
    </span>
    {{ end }}
    {{ range .Params.tags }}
    <span class="tag">{{ . }}</span>
    {{ end }}
  </div>
</a>
{{ end }}

</div>

## 📦 热门资源

<div class="card-grid">

{{ range where .Site.RegularPages "Section" "resources" }}
<a href="{{ .RelPermalink }}" class="card-glass" style="padding: 1.5rem; text-decoration: none; color: var(--text-primary);">
  <div style="font-weight: 600; margin-bottom: 0.25rem;">{{ .Title }}</div>
  <div style="font-size: 0.85rem; color: var(--text-secondary);">{{ with .Params.file_size }}📁 {{ . }}{{ end }}</div>
</a>
{{ end }}

</div>

</div>

<style>
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1rem;
  margin-top: 1rem;
  margin-bottom: 3rem;
}
@media (max-width: 768px) {
  .hero-title { font-size: 2rem; }
}
</style>

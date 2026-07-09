---
title: "模拟卷2 数据结构 第41题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 2
subjects:
  - "数据结构"
knowledge_points:
  - "数据结构"
question_type: "comprehensive"
difficulty: 4
number: 41
---

（11 分）如下图所示：

（1）写出该图的邻接矩阵。

（2）写出全部拓扑序列。

（3）以 V1 为源点，以 V8 为终点，给出所有事件（和活动）允许发生的最早时间和最晚时间，并给出关键路径。

（4）求 V1 结点到各点的最短路径和距离。

[tag_link]

【解析】 (1) 该图对应的邻接矩阵如下： [图片] ​ ∞ ∞ ∞ ∞ ∞ ∞ ∞ ∞ ​ 2 ∞ ∞ ∞ ∞ ∞ ∞ ∞ ​ 3 ∞ ∞ ∞ ∞ ∞ ∞ ∞ ​ ∞ 5 3 ∞ ∞ ∞ ∞ ∞ ​ ∞ ∞ 10 ∞ ∞ 2 ∞ ∞ ​ ∞ ∞ ∞ 4 ∞ ∞ ∞ ∞ ​ ∞ ∞ ∞ ∞ 3 ∞ ∞ ∞ ​ ∞ ∞ ∞ ∞ ∞ 6 1 ∞ ​ [图片] ​ (2) 只有顶点 V 1 的入度为 0，由此可以得到两个拓扑序列： V 1 , V 2 , V 3 , V 4 , V 6 , V 5 , V 7 , V 8 和 V 1 , V 3 , V 2 , V 4 , V 6 , V 5 , V 7 , V 8 。 (3) 关键路径共有 3 条，长 17。依次为： V 1 → V 2 → V 4 → V 6 → V 8 ， V 1 → V 3 → V 5 → V 7 → V 8 ， V 1 → V 2 → V 4 → V 6 → V 5 → V 7 → V 8 。 事件 V1 V2 V3 V4 V5 V6 V7 V8 最早发生时间 0 2 3 7 13 11 16 17 最晚发生时间 0 2 3 7 13 11 16 17 活动 V1-V2 V1-V3 V2-V4 V3-V4 V3-V5 V4-V6 V6-V5 V5-V7 V6-V8 V7-V8 最早开始时间 0 0 2 3 3 7 11 13 11 16 最晚开始时间 0 0 2 4 3 7 11 13 11 16 时间余量 0 0 0 1 0 0 0 0 0 0 (4) 顶点 V 1 到其他各顶点的最短路径和距离为： 2 ( V 1 → V 2 ) 3 ( V 1 → V 3 ) 6 ( V 1 → V 3 → V 4 ) 12 ( V 1 → V 3 → V 4 → V 6 → V 5 ) 10 ( V 1 → V 3 → V 4 → V 6 ) 15 ( V 1 → V 3 → V 4 → V 6 → V 5 → V 7 ) 16 ( V 1 → V 3 → V 4 → V 6 → V 5 → V 7 → V 8 或 V 1 → V 3 → V 4 → V 6 → V 8 ) if(typeof window.quizDB=="undefined"){class e{constructor(){this.dbName="QuizCollectionsDB",this.storeName="quizzes",this.version=1,this.db=null}async init(){return new Promise((e,t)=>{const n=indexedDB.open(this.dbName,this.version);n.onerror=()=>t(n.error),n.onsuccess=()=>{this.db=n.result,e(this.db)},n.onupgradeneeded=e=>{const t=e.target.result;if(!t.objectStoreNames.contains(this.storeName)){const e=t.createObjectStore(this.storeName,{keyPath:"id"});e.createIndex("collectedAt","collectedAt",{unique:!1}),e.createIndex("tags","tags",{unique:!1,multiEntry:!0}),e.createIndex("type","type",{unique:!1})}}})}async add(e){return this.db||await this.init(),new Promise((t,n)=>{const o=this.db.transaction([this.storeName],"readwrite"),i=o.objectStore(this.storeName),s=i.add(e);s.onsuccess=()=>t(s.result),s.onerror=()=>n(s.error)})}async remove(e){return this.db||await this.init(),new Promise((t,n)=>{const o=this.db.transaction([this.storeName],"readwrite"),i=o.objectStore(this.storeName),s=i.delete(e);s.onsuccess=()=>t(s.result),s.onerror=()=>n(s.error)})}async get(e){return this.db||await this.init(),new Promise((t,n)=>{const o=this.db.transaction([this.storeName],"readonly"),i=o.objectStore(this.storeName),s=i.get(e);s.onsuccess=()=>t(s.result),s.onerror=()=>n(s.error)})}async getAll(){return this.db||await this.init(),new Promise((e,t)=>{const s=this.db.transaction([this.storeName],"readonly"),o=s.objectStore(this.storeName),n=o.getAll();n.onsuccess=()=>e(n.result),n.onerror=()=>t(n.error)})}async getAllIds(){return this.db||await this.init(),new Promise((e,t)=>{const s=this.db.transaction([this.storeName],"readonly"),o=s.objectStore(this.storeName),n=o.getAllKeys();n.onsuccess=()=>e(n.result),n.onerror=()=>t(n.error)})}}window.quizDB=new e}function toggleSolutionDetail(e,t){const n=document.getElementById("solution-"+t);n&&(n.style.display==="none"||n.style.display===""?(n.style.display="block",e.textContent="隐藏答案与解析"):(n.style.display="none",e.textContent="查看答案与解析"))}async function collectAnswerQuiz(e,t){const s=document.getElementById("quiz-"+e);if(!s)return;let n=s.previousElementSibling;const a=[];let o="";for(;n&&n.tagName!=="H5";)a.unshift(n),n=n.previousElementSibling;n&&n.tagName==="H5"&&(o=n.innerText.trim());const i=a.map(e=>{const t=e.cloneNode(!0);return t.querySelectorAll("button, script, style").forEach(e=>e.remove()),t.outerHTML.trim()}).filter(e=>e.length>0),r=document.getElementById("solution-"+e);let c="";if(r){const e=r.cloneNode(!0);e.querySelectorAll("button, script, style").forEach(e=>e.remove()),c=e.innerHTML.trim()}const l=s.dataset.pageUrl,d=getSubjectFromUrl(l),u={id:e,type:"answer",quizNumber:o,question:i.length>0?i:["题目"],questionText:i.map(e=>{const t=document.createElement("div");return t.innerHTML=e,t.textContent.trim()}).join(` `),answer:"",explanation:c,tags:s.dataset.tags,subject:d,pageUrl:s.dataset.pageUrl+`/#${o}`,pageTitle:s.dataset.pageTitle+` 第 ${o} 题`,collectedAt:(new Date).toISOString()};try{const n=await window.quizDB.get(e);n?(await window.quizDB.remove(e),t.classList.remove("collected"),t.innerHTML=' 收藏',t.title="收藏此题",showNotification("已取消收藏")):(await window.quizDB.add(u),t.classList.add("collected"),t.innerHTML=' 已收藏',t.title="取消收藏",showNotification("已添加到收藏"))}catch(e){console.error("Error managing answer quiz collection:",e),showNotification("操作失败，请重试")}}if(document.addEventListener("DOMContentLoaded",async function(){try{await window.quizDB.init();const e=await window.quizDB.getAllIds();document.querySelectorAll(".answer-container .collect-btn").forEach(t=>{const n=t.closest(".answer-container");n&&e.includes(n.id.replace("quiz-",""))&&(t.classList.add("collected"),t.innerHTML=' 已收藏',t.title="取消收藏")})}catch(e){console.error("Error initializing answer quiz collections:",e)}}),!document.getElementById("quiz-animations")){const e=document.createElement("style");e.id="quiz-animations",e.textContent=` @keyframes slideIn { from { transform: translateX(100%); opacity: 0; } to { transform: translateX(0); opacity: 1; } } @keyframes slideOut { from { transform: translateX(0); opacity: 1; } to { transform: translateX(100%); opacity: 0; } } `,document.head.appendChild(e)} 42 （13 分）将一个数组最开始的若干个元素搬到数组的末尾，称之为数组的旋转。输入一个已排好序数组的一个旋转，求该旋转数组的最小元素。如，数组 {3, 4, 5, 1, 2} 为有序数组 {1, 2, 3, 4, 5} 的一个旋转数组，该数组的最小值为 1。 （1）给出算法的基本设计思想。 （2）根据设计思想，采用 C 或 C++ 语言描述算法，关键之处给出注释。 （3）说明你所设计算法的时间复杂度和空间复杂度。 查看答案与解析 收藏


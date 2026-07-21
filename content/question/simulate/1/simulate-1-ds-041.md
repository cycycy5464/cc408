---
title: "模拟卷1 数据结构 第41题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 1
subjects:
  - "数据结构"
knowledge_points:
  - "最小生成树"
question_type: "comprehensive"
difficulty: 4
number: 41

---

（10 分）下面有一种称为“破圈法”的求解最小生成树的方法：所谓“破圈法”就是“任取一圈，去掉圈上权最大的边”，反复执行这一步骤，直到没有圈为止。
试判断这种方法是否正确。如果正确，请说明理由；如果不正确，举出反例（注：圈就是回路）。

[最小生成树](/study_methods/tags/408quiz//#%e6%9c%80%e5%b0%8f%e7%94%9f%e6%88%90%e6%a0%91)

[tag_link]

<p>**【答案】** 正确
<p>**【解析】**
连通图的生成树包括图中的全部 n 个顶点和足以使图连通的 n-1 条边，最小生成树是边上权值之和最小的生成树。故可按权值从大到小对边进行排序，然后从大到小将边删除。每删除一条当前权值最大的边后，就去测试图是否仍连通，若不再连通，则将该边恢复。若仍连通，继续向下删；直到剩 n-1 条边为止。
<div class=img-container style=height:auto;width:auto oncontextmenu=return!1> [图片] </div><p>破圈法的正确性基于最小生成树的一个关键性质：在连通无向图的任意一个圈中，权值最大的边一定不属于任何最小生成树（如果边权互异，则该边绝对不在最小生成树中；如果边权有重复，则存在至少一个最小生成树不包含该边）。执行破圈法时，每次任选一个圈并去掉其中权最大的边，相当于移除了一条不在最小生成树中的边，且由于圈是连通的，去掉一条边不会破坏图的连通性。反复执行这一操作，直到图中没有圈为止，此时得到的图是连通且无环的，即为一棵生成树。由于去除的边都不在最小生成树中，而剩下的边数恰好为顶点数减一，因此这棵生成树就是最小生成树。综上，破圈法是求解最小生成树的一种正确方法。
</div><script src=/js/quiz.js defer></script><script>if(typeof window.quizDB=="undefined"){class e{constructor(){this.dbName="QuizCollectionsDB",this.storeName="quizzes",this.version=1,this.db=null}async init(){return new Promise((e,t)=>{const n=indexedDB.open(this.dbName,this.version);n.onerror=()=>t(n.error),n.onsuccess=()=>{this.db=n.result,e(this.db)},n.onupgradeneeded=e=>{const t=e.target.result;if(!t.objectStoreNames.contains(this.storeName)){const e=t.createObjectStore(this.storeName,{keyPath:"id"});e.createIndex("collectedAt","collectedAt",{unique:!1}),e.createIndex("tags","tags",{unique:!1,multiEntry:!0}),e.createIndex("type","type",{unique:!1})}}})}async add(e){return this.db||await this.init(),new Promise((t,n)=>{const o=this.db.transaction([this.storeName],"readwrite"),i=o.objectStore(this.storeName),s=i.add(e);s.onsuccess=()=>t(s.result),s.onerror=()=>n(s.error)})}async remove(e){return this.db||await this.init(),new Promise((t,n)=>{const o=this.db.transaction([this.storeName],"readwrite"),i=o.objectStore(this.storeName),s=i.delete(e);s.onsuccess=()=>t(s.result),s.onerror=()=>n(s.error)})}async get(e){return this.db||await this.init(),new Promise((t,n)=>{const o=this.db.transaction([this.storeName],"readonly"),i=o.objectStore(this.storeName),s=i.get(e);s.onsuccess=()=>t(s.result),s.onerror=()=>n(s.error)})}async getAll(){return this.db||await this.init(),new Promise((e,t)=>{const s=this.db.transaction([this.storeName],"readonly"),o=s.objectStore(this.storeName),n=o.getAll();n.onsuccess=()=>e(n.result),n.onerror=()=>t(n.error)})}async getAllIds(){return this.db||await this.init(),new Promise((e,t)=>{const s=this.db.transaction([this.storeName],"readonly"),o=s.objectStore(this.storeName),n=o.getAllKeys();n.onsuccess=()=>e(n.result),n.onerror=()=>t(n.error)})}}window.quizDB=new e}function toggleSolutionDetail(e,t){const n=document.getElementById("solution-"+t);n&&(n.style.display==="none"||n.style.display===""?(n.style.display="block",e.textContent="隐藏答案与解析"):(n.style.display="none",e.textContent="查看答案与解析"))}async function collectAnswerQuiz(e,t){const s=document.getElementById("quiz-"+e);if(!s)return;let n=s.previousElementSibling;const a=[];let o="";for(;n&&n.tagName!=="H5";)a.unshift(n),n=n.previousElementSibling;n&&n.tagName==="H5"&&(o=n.innerText.trim());const i=a.map(e=>{const t=e.cloneNode(!0);return t.querySelectorAll("button, script, style").forEach(e=>e.remove()),t.outerHTML.trim()}).filter(e=>e.length>0),r=document.getElementById("solution-"+e);let c="";if(r){const e=r.cloneNode(!0);e.querySelectorAll("button, script, style").forEach(e=>e.remove()),c=e.innerHTML.trim()}const l=s.dataset.pageUrl,d=getSubjectFromUrl(l),u={id:e,type:"answer",quizNumber:o,question:i.length>0?i:["题目"],questionText:i.map(e=>{const t=document.createElement("div");return t.innerHTML=e,t.textContent.trim()}).join(`
`),answer:"",explanation:c,tags:s.dataset.tags,subject:d,pageUrl:s.dataset.pageUrl+`/#${o}`,pageTitle:s.dataset.pageTitle+` 第 ${o} 题`,collectedAt:(new Date).toISOString()};try{const n=await window.quizDB.get(e);n?(await window.quizDB.remove(e),t.classList.remove("collected"),t.innerHTML='<i class="fa-regular fa-bookmark"></i> 收藏',t.title="收藏此题",showNotification("已取消收藏")):(await window.quizDB.add(u),t.classList.add("collected"),t.innerHTML='<i class="fa-solid fa-bookmark"></i> 已收藏',t.title="取消收藏",showNotification("已添加到收藏"))}catch(e){console.error("Error managing answer quiz collection:",e),showNotification("操作失败，请重试")}}if(document.addEventListener("DOMContentLoaded",async function(){try{await window.quizDB.init();const e=await window.quizDB.getAllIds();document.querySelectorAll(".answer-container .collect-btn").forEach(t=>{const n=t.closest(".answer-container");n&&e.includes(n.id.replace("quiz-",""))&&(t.classList.add("collected"),t.innerHTML='<i class="fa-solid fa-bookmark"></i> 已收藏',t.title="取消收藏")})}catch(e){console.error("Error initializing answer quiz collections:",e)}}),!document.getElementById("quiz-animations")){const e=document.createElement("style");e.id="quiz-animations",e.textContent=`
    @keyframes slideIn {
      from { transform: translateX(100%); opacity: 0; }
      to { transform: translateX(0); opacity: 1; }
    }
    @keyframes slideOut {
      from { transform: translateX(0); opacity: 1; }
      to { transform: translateX(100%); opacity: 0; }
    }
  `,document.head.appendChild(e)}</script><h5 id=42>42</h5><p>（12 分）假设二叉树采用二叉链存储结构存储，设计一个算法，求出根结点到给定某结点之间的路径，要求：
（1）给出算法的基本设计思想。
（2）写出二叉树采用的存储结构代码。
（3）根据设计思想，采用 C 或 C++语言描述算法，关键之处给出注释。
<div class="answer-container td-max-width-on-larger-screens" id=quiz-answer-ccaad5634fe13afd20771d2b1485bed0-2 data-tags data-page-url=http://www.csgraduates.com/study_methods/408simulate/1/ data-page-title="模拟卷 1"><div class=quiz-tag-container></div><div class=quiz-actions><button class=toggle-btn onclick='toggleSolutionDetail(this,"answer-ccaad5634fe13afd20771d2b1485bed0-2")'>查看答案与解析</button>
<button class=collect-btn onclick='collectAnswerQuiz("answer-ccaad5634fe13afd20771d2b1485bed0-2",this)' title=收藏此题>
<i class="fa-regular fa-bookmark"></i> 收藏</button>

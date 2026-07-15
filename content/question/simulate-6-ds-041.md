---
title: "模拟卷6 数据结构 第41题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 6
subjects:
  - "数据结构"
knowledge_points:
  - "信号量"
  - "复杂度分析"
question_type: "comprehensive"
difficulty: 4
number: 41

---

（13 分）设有
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
个不全为负的整型元素存储在一维数组 A[p] 中，它包含很多连续的子数组，例如数组 A = {1, -2, 3, 10, -4, 7, 2, -5}，请设计一个时间上尽可能高效的算法，求出数组 A 的子数组之和的最大值（例如数组 A 的最大的子数组为 {3, 10, -4, 7, 2}，因此输出为该子数组的和 18）。要求：

(1) 给出算法的基本设计思想。
(2) 根据设计思想，采用 C 或 C++ 语言描述算法，关键之处给出注释。
(3) 说明你所设计算法的时间复杂度和空间复杂度。

[信号量](/study_methods/tags/408quiz//#%e4%bf%a1%e5%8f%b7%e9%87%8f)
[复杂度分析](/study_methods/tags/408quiz//#%e5%a4%8d%e6%9d%82%e5%ba%a6%e5%88%86%e6%9e%90)

[tag_link]

<p>**【答案】**
(1) 基本设计思想：采用 Kadane 算法（动态规划思想）。遍历数组，维护两个变量：current_sum 记录以当前元素结尾的子数组的最大和，max_sum 记录全局最大子数组和。对于每个元素，若 current_sum 为负，则将其重置为当前元素值（因为负数会减小后续子数组的和），否则将当前元素加入 current_sum。然后更新 max_sum。遍历完成后，max_sum 即为所求。
<p>(2) C 语言算法描述：
<div class=highlight><pre tabindex=0 style=background-color:#f8f8f8;-moz-tab-size:4;-o-tab-size:4;tab-size:4><code class=language-c data-lang=c><span style=display:flex><span><span style=color:#8f5902;font-style:italic>#include</span> <span style=color:#8f5902;font-style:italic><stdio.h></span><span style=color:#8f5902;font-style:italic>
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic>#include</span> <span style=color:#8f5902;font-style:italic><limits.h> // 使用 INT_MIN 初始化</span><span style=color:#8f5902;font-style:italic>
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>
</span></span><span style=display:flex><span><span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>maxSubArray</span><span style=color:#000;font-weight:700>(</span><span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>A</span><span style=color:#000;font-weight:700>[],</span> <span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>n</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>    <span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>current_sum</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#0000cf;font-weight:700>0</span><span style=color:#000;font-weight:700>;</span>       <span style=color:#8f5902;font-style:italic>// 当前子数组和
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>    <span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>max_sum</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#000>INT_MIN</span><span style=color:#000;font-weight:700>;</span>     <span style=color:#8f5902;font-style:italic>// 最大子数组和，初始化为最小整数
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>    <span style=color:#204a87;font-weight:700>for</span> <span style=color:#000;font-weight:700>(</span><span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>i</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#0000cf;font-weight:700>0</span><span style=color:#000;font-weight:700>;</span> <span style=color:#000>i</span> <span style=color:#ce5c00;font-weight:700><</span> <span style=color:#000>n</span><span style=color:#000;font-weight:700>;</span> <span style=color:#000>i</span><span style=color:#ce5c00;font-weight:700>++</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>        <span style=color:#8f5902;font-style:italic>// 若当前子数组和为负，则从 A[i] 重新开始，否则累加
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>        <span style=color:#204a87;font-weight:700>if</span> <span style=color:#000;font-weight:700>(</span><span style=color:#000>current_sum</span> <span style=color:#ce5c00;font-weight:700><</span> <span style=color:#0000cf;font-weight:700>0</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>            <span style=color:#000>current_sum</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#000>A</span><span style=color:#000;font-weight:700>[</span><span style=color:#000>i</span><span style=color:#000;font-weight:700>];</span>
</span></span><span style=display:flex><span>        <span style=color:#000;font-weight:700>}</span> <span style=color:#204a87;font-weight:700>else</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>            <span style=color:#000>current_sum</span> <span style=color:#ce5c00;font-weight:700>+=</span> <span style=color:#000>A</span><span style=color:#000;font-weight:700>[</span><span style=color:#000>i</span><span style=color:#000;font-weight:700>];</span>
</span></span><span style=display:flex><span>        <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>        <span style=color:#8f5902;font-style:italic>// 更新全局最大值
</span></span></span><span style=display:flex><span><span style=color:#8f5902;font-style:italic></span>        <span style=color:#204a87;font-weight:700>if</span> <span style=color:#000;font-weight:700>(</span><span style=color:#000>current_sum</span> <span style=color:#ce5c00;font-weight:700>></span> <span style=color:#000>max_sum</span><span style=color:#000;font-weight:700>)</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>            <span style=color:#000>max_sum</span> <span style=color:#ce5c00;font-weight:700>=</span> <span style=color:#000>current_sum</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span>        <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>    <span style=color:#000;font-weight:700>}</span>
</span></span><span style=display:flex><span>    <span style=color:#204a87;font-weight:700>return</span> <span style=color:#000>max_sum</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span><span style=color:#000;font-weight:700>}</span>
</span></span>`</pre></div><p>(3) 时间复杂度：O(n)，其中 n 为数组长度，仅需一次遍历。空间复杂度：O(1)，仅使用常数个辅助变量。
<p>**【解析】**
该算法基于动态规划，核心是确定以每个元素结尾的最大子数组和。设以元素 A[i] 结尾的最大子数组和为 f(i)，则状态转移方程为：f(i) = max(A[i], f(i-1) + A[i])。这是因为如果 f(i-1) 为负，其对 A[i] 无增益，故从 A[i] 重新开始；否则累加。算法中的 current_sum 即 f(i)，max_sum 记录所有 f(i) 的最大值。由于数组不全为负，max_sum 至少为非负，但算法也适用于全负情况。遍历一次即可求得结果，因此时间效率高，且仅需常数空间。
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
  `,document.head.appendChild(e)}</script><h5 id=42>42</h5><p>图 1 为某操作系统中文件系统的目录结构。
<div class=img-container style=height:auto;width:60% oncontextmenu=return!1> [图片] </div><p>请回答一下问题：
<p>(1) 本题中的目录结构可抽象为数据结构中的哪种逻辑结构？
(2) 请设计合理的链式存储结构，以保存图 1 中的文件目录信息。要求给出链式存储结构的数据类型定义，并画出对应图 1 中根目录部分到目录 A、B 及其子目录和文件的链式存储结构示意图。
(3) 哈夫曼树是一种特殊的树形结构，请证明哈夫曼树的总结点数总为奇数。
<div class="answer-container td-max-width-on-larger-screens" id=quiz-answer-cfaff0242c4957d646be5708f910eba5-2 data-tags data-page-url=http://www.csgraduates.com/study_methods/408simulate/6/ data-page-title="模拟卷 6"><div class=quiz-tag-container></div><div class=quiz-actions><button class=toggle-btn onclick='toggleSolutionDetail(this,"answer-cfaff0242c4957d646be5708f910eba5-2")'>查看答案与解析</button>
<button class=collect-btn onclick='collectAnswerQuiz("answer-cfaff0242c4957d646be5708f910eba5-2",this)' title=收藏此题>
<i class="fa-regular fa-bookmark"></i> 收藏</button>

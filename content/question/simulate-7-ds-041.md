---
title: "模拟卷7 数据结构 第41题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 7
subjects:
  - "数据结构"
knowledge_points:
  - "数据结构"
question_type: "comprehensive"
difficulty: 4
number: 41
---

（9 分）对于一个堆栈，若其入栈序列为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>2</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>3</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=minner>⋯</span><span class=mspace style=margin-right:.1667em></span><span class=mspace style=margin-right:.1667em></span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal">n</span></span></span></span>
，不同的出入栈操作将产生不同的出栈序列。其出栈序列的个数正好等于结点个数为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
的二叉树的个数，且与不同形态的二叉树一一对应。请简要论述一种从堆栈输入（固定为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>2</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>3</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=minner>⋯</span><span class=mspace style=margin-right:.1667em></span><span class=mspace style=margin-right:.1667em></span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal">n</span></span></span></span>
）输出序列对应一种二叉树形态的方法，并以入栈序列
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>2</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>3</span></span></span></span>
（即
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>3</span></span></span></span>
）为例加以说明。

[tag_link]

<p>**【答案】**
将固定入栈序列
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>2</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>3</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=minner>⋯</span><span class=mspace style=margin-right:.1667em></span><span class=mspace style=margin-right:.1667em></span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal">n</span></span></span></span>
视为二叉树的前序遍历序列，而将出栈序列视为同一二叉树的中序遍历序列。由于二叉树的前序遍历和中序遍历可以唯一确定二叉树的结构，因此每个合法的出栈序列对应一种二叉树形态。
<p>**【解析】**
对于入栈序列
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>2</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=minner>⋯</span><span class=mspace style=margin-right:.1667em></span><span class=mspace style=margin-right:.1667em></span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class="mord mathnormal">n</span></span></span></span>
，其出栈序列的个数等于结点个数为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
的二叉树的个数，即第
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span></span></span></span>
个卡特兰数。这一一对应可通过二叉树遍历序列建立：入栈序列固定为前序遍历序列，出栈序列作为中序遍历序列。具体地，前序遍历序列确定了根结点的访问顺序，中序遍历序列确定了左子树和右子树的划分，从而唯一重建二叉树。
<p>以
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.4306em></span><span class="mord mathnormal">n</span><span class=mspace style=margin-right:.2778em></span><span class=mrel>=</span><span class=mspace style=margin-right:.2778em></span></span><span class=base><span class=strut style=height:.6444em></span><span class=mord>3</span></span></span></span>
为例，入栈序列为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>2</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>3</span></span></span></span>
，作为前序遍历序列。合法的出栈序列有
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>5</span></span></span></span>
种，分别作为中序遍历序列，重建二叉树如下：
<ul><li>出栈序列
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>2</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>3</span></span></span></span>
：前序
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>2</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>3</span></span></span></span>
，中序
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>2</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>3</span></span></span></span>
，重建得二叉树为根结点
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
的右孩子为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>2</span></span></span></span>
，
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>2</span></span></span></span>
的右孩子为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>3</span></span></span></span>
。</li><li>出栈序列
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>3</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>2</span></span></span></span>
：前序
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>2</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>3</span></span></span></span>
，中序
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>3</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>2</span></span></span></span>
，重建得根结点
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
的右孩子为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>2</span></span></span></span>
，
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>2</span></span></span></span>
的左孩子为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>3</span></span></span></span>
。</li><li>出栈序列
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>2</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>3</span></span></span></span>
：前序
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>2</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>3</span></span></span></span>
，中序
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>2</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>3</span></span></span></span>
，重建得根结点
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
的左孩子为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>2</span></span></span></span>
，右孩子为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>3</span></span></span></span>
。</li><li>出栈序列
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>2</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>3</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>1</span></span></span></span>
：前序
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>2</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>3</span></span></span></span>
，中序
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>2</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>3</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>1</span></span></span></span>
，重建得根结点
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
的左孩子为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>2</span></span></span></span>
，
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>2</span></span></span></span>
的右孩子为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>3</span></span></span></span>
。</li><li>出栈序列
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>3</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>2</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>1</span></span></span></span>
：前序
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>1</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>2</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>3</span></span></span></span>
，中序
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.8389em;vertical-align:-.1944em></span><span class=mord>3</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>2</span><span class=mpunct>,</span><span class=mspace style=margin-right:.1667em></span><span class=mord>1</span></span></span></span>
，重建得根结点
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>1</span></span></span></span>
的左孩子为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>2</span></span></span></span>
，
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>2</span></span></span></span>
的左孩子为
<span class=katex><span class=katex-html aria-hidden=true><span class=base><span class=strut style=height:.6444em></span><span class=mord>3</span></span></span></span>
。</li></ul><p>这五种二叉树形态恰好对应所有合法的出栈序列，验证了一一对应关系。
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
  `,document.head.appendChild(e)}</script><h5 id=42>42</h5><p>（13 分）已知一棵二叉树采用二叉链表存储，结点结构为：
<div class=highlight><pre tabindex=0 style=background-color:#f8f8f8;-moz-tab-size:4;-o-tab-size:4;tab-size:4><code class=language-c data-lang=c><span style=display:flex><span><span style=color:#204a87;font-weight:700>struct</span> <span style=color:#000>Node</span> <span style=color:#000;font-weight:700>{</span>
</span></span><span style=display:flex><span>    <span style=color:#204a87;font-weight:700>struct</span> <span style=color:#000>Node</span> <span style=color:#ce5c00;font-weight:700>*</span><span style=color:#000>lchild</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span>    <span style=color:#204a87;font-weight:700>int</span> <span style=color:#000>data</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span>    <span style=color:#204a87;font-weight:700>struct</span> <span style=color:#000>Node</span> <span style=color:#ce5c00;font-weight:700>*</span><span style=color:#000>rchild</span><span style=color:#000;font-weight:700>;</span>
</span></span><span style=display:flex><span><span style=color:#000;font-weight:700>};</span>
</span></span>`</pre></div><p>`root` 指向根结点。请编写算法判断该二叉树是否是平衡二叉树，即二叉树中任意结点的左右子树的深度相差不超过 1。例如下图所示的二叉树就是一棵平衡二叉树。
<div class=img-container style=height:auto;width:40% oncontextmenu=return!1> [图片] </div><p>**要求：**
（1）给出算法的基本设计思想。
（2）根据设计思想，采用 C 或 C++ 语言描述算法，关键之处给出注释。
<div class="answer-container td-max-width-on-larger-screens" id=quiz-answer-b21e56584c27aaf174732231badd601f-2 data-tags data-page-url=http://www.csgraduates.com/study_methods/408simulate/7/ data-page-title="模拟卷 7"><div class=quiz-tag-container></div><div class=quiz-actions><button class=toggle-btn onclick='toggleSolutionDetail(this,"answer-b21e56584c27aaf174732231badd601f-2")'>查看答案与解析</button>
<button class=collect-btn onclick='collectAnswerQuiz("answer-b21e56584c27aaf174732231badd601f-2",this)' title=收藏此题>
<i class="fa-regular fa-bookmark"></i> 收藏</button>

# CC408 优化 Lessons

> 本次优化 sprint 途中记录的经验教训

---

## Lesson 1: 共享 JS 要早做

JS 交互逻辑（选项转换、答案折叠、收藏）在同一项目中以 200+ 行的规模重复了 5 次。
早该在第一次写 `exam/408quiz-detail.html` 时就把逻辑抽取到 `assets/js/` 中。

**教训**: 项目中第二个出现类似交互的页面就是"抽取共享模块"的信号，不需要等到第五个。

---

## Lesson 2: 收藏 ID 必须统一

同一道题在不同页面使用不同的 ID 生成逻辑，导致收藏重复。
最佳实践：ID 应基于题目本身的属性（年份+题号+题源），而非页面路径或 DOM 属性。

**教训**: 涉及跨页面共享的数据（收藏 ID），必须在数据设计阶段统一约定。

---

## Lesson 3: Hugo 构建时间 vs 运行时性能

3889 个 .md 文件导致 `hugo` 构建 40-60s。
将全部题目的完整 HTML 注入 JSON 虽然让 JS 渲染简单，但构建时间 + 页面体积双双增加。
折中方案：按需加载 — 初次只加载前 N 题数据，翻页时 AJAX 获取。

**教训**: 静态站点追求"全量预生成"并不总是最优，需要根据运行时访问模式做取舍。

---

## Lesson 4: 内网环境的 git 推送

内网 SSH 端口 22 不通，需切换到 HTTPS remote + GCM 认证。
`git remote set-url origin https://github.com/cycycy5464/cc408.git`

**教训**: 在初始化项目时就配置 HTTPS remote，避免后续切换。

---

## Lesson 5: 模板中的 Go Template 语法错误

`{{ $type := if eq .A "x" }}y{{ else }}z{{ end }}` 是无效语法。
Go template 不支持在 `:=` 中嵌入 `if`，需先初始化再赋值。

**教训**: 每次修改模板后必须 `hugo --quiet` 验证构建，不能靠肉眼审查。

---

## Lesson 6: 模板批量替换用 Python 要谨慎

Python `re.sub` 替换 Hugo 模板文件时，`re.DOTALL` 模式可能匹配过度或不足。
两次事故：
- `taxonomy.html`：替换后残留旧 JS 碎片在函数体内，模板结构错乱
- `chapter-exercises.html`：误删 `{{ end }}` 闭合标签 + 残留已删除的函数调用

**教训**: 对 Hugo 模板做结构性修改，优先用 `Write` 全量重写而非 `re.sub`。必须用正则时，逐个确认替换边界并 `hugo` 验证。

---

## Lesson 7: CSS 提取后检查孤立闭括号

CSS 分区 (`custom.scss` → 各模板) 移除 `.tm-*` 样式块后，遗留了一个 `}`，
导致 SCSS 编译报 `expected selector or at-rule`。

**教训**: CSS 提取后运行 `grep -n '^}$'` 检查无匹配的闭括号。`hugo` 构建必须通过才能提交。

---

## Lesson 8: `<details>` 元素适合大数据层级展示

2650 道课后题用 `<details>` 手风琴展示（科目→章节→小节），零 JS，原生 HTML。
初始 DOM 只渲染外壳，展开时浏览器才渲染内部内容，性能无压力。

**教训**: 对于「需要折叠大量同类数据」的场景，优先用 `<details>` 而非 JS 手风琴。兼容性好、性能好、零依赖。

---

## Lesson 9: 课后题展示需要三重分组（科目→章节→小节）

课后题 2650 道、4 科、每科多章、每章多节。仅按题号排序会导致大量同号题目混淆。
需要 `data-section` 属性 + 三级联动筛选。

**教训**: 数据量大且有层级关系的内容，模板层面就要设计好分组层级，不要依赖 JS 动态解析。


---

## Lesson 10: 收藏 ID 格式需全局一致

`collect-quiz.js` 之前使用 `choice-/cc408/question/...` 作为收藏 ID，
而共享模块使用 `{year}-{number}`。同一题在不同页面收藏生成不同 ID。

**教训**: 所有涉及收藏的 JS 文件必须使用同一个 ID 生成函数或格式。
收集项目全部收藏入口，逐处核对。


---

## Lesson 11: Hugo :filename 已废弃

Hugo 0.144.0+ 将  重命名为 。
 中必须用  否则构建报 deprecated 警告。

**教训**: Hugo 版本迭代快，配置语法要跟着 Hugo Release Notes 更新。

# 为 Hugo content 建立知识图谱

## 任务清单

- [x] **方案二实施：Junction 软链接**
  - [x] 创建 `cc408-content/` Junction → Hugo `content/`
  - [x] Obsidian 排除 `_index.md`
  - [x] 旧内容 `40.resources/408考研/` → 备份到 `D:\_archived_cc408_vault\`
  - [x] 创建导航页 `40.resources/408考研导航.md`
  - [x] Obsidian 书签「📖 408考研 (Hugo同步)」

- [x] **知识图谱系统构建**
  - [x] 修复 `knowledge-graph-data.html` partial：自动匹配 `prerequisites` 生成连线
  - [x] 批量填充 98 篇笔记的 `prerequisites`（按章节依赖：chN ← chN-1）
  - [x] 修复 sed 转义问题（`/` 字符冲突 → 改用 `|` 分隔符）
  - [x] 修复 Hugo 模板 JSON 转义（`<div>` 代替 `<script type="application/json">`）
  - [x] 最终结果：112 节点 + 451 条连线

## 技术难点

### 1. Hugo `jsonify` + `<script>` 转义
- `{{ $data | jsonify | safeJS }}` 在 `<script type="application/json">` 中被双重转义
- **根因**: Hugo 对 script 标签内容应用 JS 上下文转义，嵌套 JSON 字符串会被再次包裹
- **修复**: 改用 `<div style="display:none">{{ $data | jsonify }}</div>`，HTML 实体 `&#34;` 会被浏览器 `textContent` 自动解码

### 2. Hugo 变量作用域
- `{{ $nodes := slice }}` 后，`range` 内用 `$nodes = $nodes | append ...` 在 Hugo 0.135 中可能报错
- **修复**: 改用 `newScratch` 模式：`$s.Set/Get`
- ```go
  {{ $s := newScratch }}
  {{ $s.Set "nodes" slice }}
  {{ range ... }}
    {{ $s.Set "nodes" ($s.Get "nodes" | append ...) }}
  {{ end }}
  ```

### 3. PowerShell 字符串拼接优先级
- `"prefix [" + (array | ForEach-Object { "`"$_`"" }) -join ", " + "]"` 
- 优先级：`+` > `-join`，导致 array 被转为空格分隔的字符串后再 join
- **修复**: `'prefix ["' + ($titles -join '", "') + '"]'`

### 4. sed 替换字符串含 `/`
- 笔记标题 `总线和I/O系统` 含 `/`，与 sed `s/pat/rep/` 分隔符冲突
- **修复**: 改用 `s|pat|rep|`

### 5. PowerShell `IFS` 多字符分隔
- `IFS='||'` 等价于 `IFS='|'`（IFS 是单字符集合，不是字符串）
- `A||B||C` 按 `|` 拆分 → `A, '', B, '', C`（中间空元素）
- **修复**: 用单字符分隔符 `|`

## 当前架构

```
Hugo content/ ──Junction──→ Obsidian vault cc408-content/
       │                            │
   docs/*.md (112 篇)         Obsidian 书签 + 关系图谱
       │
   knowledge-graph-data.html (partial)
       │
   graph/index.html → D3.js 力导向图
```

## 文件修改记录

| 文件 | 操作 |
|------|------|
| `layouts/partials/knowledge-graph-data.html` | 重写：newScratch + 自动链接生成 |
| `layouts/graph/list.html` | `<script>` → `<div>` 存储 JSON |
| 98 个 `content/docs/**/*.md` | 填充 `prerequisites` |
| `static/data/knowledge-graph.json` | 删除（过时手写文件） |
| `scripts/populate_prereq.sh` | 新增：批量填充脚本 |
| `scripts/analyze_graph.ps1` | 新增：分析脚本 |

## Review

- 112 个知识点节点全部自动生成
- 451 条跨章节连线清晰展示知识递进关系
- 后续可加入跨科目连线（如 操作系统⨯计组/虚拟内存）
- 在 Obsidian 中可通过 `cc408-content/` 直接跳转到对应笔记

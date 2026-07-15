---
title: "模拟卷2 数据结构 第42题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 2
subjects:
  - "数据结构"
knowledge_points:
  - "复杂度分析"
question_type: "comprehensive"
difficulty: 4
number: 42

---

（13 分）将一个数组最开始的若干个元素搬到数组的末尾，称之为数组的旋转。输入一个已排好序数组的一个旋转，求该旋转数组的最小元素。如，数组 {3, 4, 5, 1, 2} 为有序数组 {1, 2, 3, 4, 5} 的一个旋转数组，该数组的最小值为 1。

（1）给出算法的基本设计思想。

（2）根据设计思想，采用 C 或 C++ 语言描述算法，关键之处给出注释。

（3）说明你所设计算法的时间复杂度和空间复杂度。

[复杂度分析](/study_methods/tags/408quiz//#%e5%a4%8d%e6%9d%82%e5%ba%a6%e5%88%86%e6%9e%90)

[tag_link]

【答案】

（1）基本设计思想： 采用改进的二分查找。由于旋转数组由两个有序子数组构成，且最小元素是第二个子数组的首元素。设置两个指针 low 和 high 分别指向数组首尾，计算中间位置 mid。比较 nums[mid] 与 nums[high]： 若 nums[mid] > nums[high]，说明最小值在右半部分，令 low = mid + 1； 若 nums[mid] &lt; nums[high]，说明最小值在左半部分（包含 mid），令 high = mid； 若相等，无法判断，但可通过 high&ndash; 缩小范围（不会丢失最小值）。 重复直到 low == high，此时指向最小元素。

（2）算法描述（C++）： int findMin ( vector &lt; int &gt;& nums ) { int low = 0 , high = nums . size () - 1 ; while ( low &lt; high ) { int mid = low + ( high - low ) / 2 ; // 防止溢出 if ( nums [ mid ] &gt; nums [ high ]) { low = mid + 1 ; // 最小值在右半部分 } else if ( nums [ mid ] &lt; nums [ high ]) { high = mid ; // 最小值在左半部分（可能为 mid） } else { high -- ; // 相等时无法判断，缩小右边界 } } return nums [ low ]; // low == high，指向最小值 }

（3）时间复杂度：平均 O(log n)，最坏情况（全部相等） O(n)。 空间复杂度：O(1)，仅用了常数个变量。 【解析】 本题是旋转数组找最小值的经典问题。原数组有序，旋转后形成两个有序子数组，且最小值位于第二个子数组开头。直接遍历需要 O(n) 时间，而利用二分思想可提升效率。 比较 nums[mid] 与 nums[high] 是关键：若 nums[mid] > nums[high]，说明 mid 属于第一个子数组，最小值必在 mid 右侧；若 nums[mid] &lt; nums[high]，说明 mid 属于第二个子数组，最小值在 mid 左侧（含 mid）；若相等，则无法二分（如数组有重复元素），但通过 high&ndash; 可逐步缩小范围，确保不遗漏最小值。 算法在大部分情况下达到对数复杂度，仅当大量重复元素时退化为线性，这是处理重复情况下的最优方式之一。

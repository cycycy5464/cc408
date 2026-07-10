---
title: "模拟卷4 数据结构 第42题"
date: 2026-07-08
type: question
years:
  - "模拟卷"
source: "模拟题"
set: 4
subjects:
  - "数据结构"
knowledge_points:
  - "数据结构"
question_type: "comprehensive"
difficulty: 4
number: 42
---

在数组中，某个数字减去它右边的数字得到一个数对之差。求所有数对之差的最大值。例如，在数组 [2, 4, 1, 16, 7, 5, 11, 9] 中，数对之差的最大值是 11，是 16 减去 5 的结果。

（1）给出算法的基本设计思想。 （2）根据设计思想，采用 C 或 C++ 语言描述算法，关键之处给出注释。 （3）说明你所设计算法的时间复杂度。

[tag_link]

【答案】 （1）算法的基本设计思想： 通过一次遍历数组，维护两个变量： maxLeft 记录当前遍历位置左边的最大值， maxDiff 记录当前找到的最大数对之差。对于每个位置 j （从第二个元素开始），计算 maxLeft - arr[j] 得到当前差值，并更新 maxDiff 。同时，如果 arr[j] 大于 maxLeft ，则更新 maxLeft 为 arr[j] ，以确保后续计算使用正确的左边最大值。这样可以在 O(n) 时间内找到最大数对之差。 （2）C++ 语言描述算法： #include &lt;iostream&gt; #include &lt;climits&gt; // 用于 INT_MIN int maxPairDiff ( int arr [], int n ) { if ( n &lt; 2 ) { // 数组至少需要两个元素，否则返回一个较小值或抛出异常 // 这里根据题目假设 n&gt;=2，简单处理返回 0 return 0 ; } int maxLeft = arr [ 0 ]; // 初始化左边最大值为第一个元素 int maxDiff = INT_MIN ; // 初始化最大差值为最小整数，确保能被更新 for ( int j = 1 ; j &lt; n ; j ++ ) { int diff = maxLeft - arr [ j ]; // 计算当前数对之差 if ( diff &gt; maxDiff ) { maxDiff = diff ; // 更新最大差值 } if ( arr [ j ] &gt; maxLeft ) { maxLeft = arr [ j ]; // 更新左边最大值 } } return maxDiff ; } int main () { int arr [] = { 2 , 4 , 1 , 16 , 7 , 5 , 11 , 9 }; int n = sizeof ( arr ) / sizeof ( arr [ 0 ]); int result = maxPairDiff ( arr , n ); std :: cout &lt;&lt; &#34;最大数对之差为：&#34; &lt;&lt; result &lt;&lt; std :: endl ; // 输出 11 return 0 ; } （3）时间复杂度： 算法只需遍历数组一次，因此时间复杂度为 O(n)，其中 n 是数组的长度。空间复杂度为 O(1)，只使用了常数个额外变量。 【解析】 该问题要求找到所有数对 (a[i], a[j]) （其中 i &lt; j ）的差值 a[i] - a[j] 的最大值。暴力枚举所有对的时间复杂度为 O(n²)，效率较低。优化算法基于以下观察：对于每个 j ，要使 a[i] - a[j] 最大，只需找到 j 左边（即 i &lt; j ）的最大值 maxLeft ，然后计算 maxLeft - a[j] 。因此，通过一次遍历，维护 maxLeft （初始为第一个元素）和 maxDiff （初始为最小整数），对于每个后续元素 arr[j] ，计算当前差值并更新 maxDiff ，同时更新 maxLeft 为 max(maxLeft, arr[j]) 。这样确保了对每个 j 都考虑了左边最大值，从而正确得到全局最大差值。例如，数组 [2, 4, 1, 16, 7, 5, 11, 9] 中，遍历到 j=5 （元素 5）时， maxLeft 为 16，差值 16-5=11 被记录为最大差值。算法只遍历一次，高效且正确。 43 （12 分）假设有两个整数 x 和 y ， x = − 68 ， y = − 80 。采用补码形式（含 1 位符号位）表示， x 和 y 分别存放在寄存器 A 和 B 中。另外，还有两个寄存器 C 和 D。A、B、C、D 都是 8 位的寄存器。请回答下列问题：（要求最终用十六进制表示二进制序列） （1）寄存器 A 和 B 中的内容分别是什么？ （2） x 和 y 相加后的结果存放在 C 寄存器中，寄存器 C 中的内容是什么？此时，溢出标志位 OF 是什么？符号标志位 SF 是什么？进位标志位 CF 是什么？ （3） x 和 y 相减后的结果存放在 D 寄存器中，寄存器 D 中的内容是什么？此时，溢出标志位 OF 是什么？符号标志位 SF 是什么？进位标志位 CF 是什么？ 查看答案与解析 收藏


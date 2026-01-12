<h2><a href="https://www.geeksforgeeks.org/problems/shortest-range-in-bst--141631/1?page=2&difficulty=Hard&status=unsolved&sortBy=submissions">Shortest Range In BST</a></h2><h3>Difficulty Level : Difficulty: Hard</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given a BST (Binary Search Tree), find the shortest range <strong>[x, y]</strong>, such that,&nbsp;at least one node of every level of the&nbsp;BST lies in the&nbsp;range.<br>If there are multiple ranges with the same gap (i.e. <strong>(y-x)</strong>) return the range with<strong> </strong>the<strong> smallest x</strong>.</span></p>
<p><span style="font-size: 18px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/706078/Web/Other/blobid1_1765611025.webp" width="219" height="249"></strong></span><span style="font-size: 18px;">
<strong>Output:</strong> [6, 11]
<strong>Explanation:</strong> Level order traversal of the tree 
is [8], [3, 10], [2, 6, 14], [4, 7, 12], [11, 13]. 
The shortest range which satisfies the above 
mentioned condition is [6, 11]. </span></pre>
<p><br><span style="font-size: 18px;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:<br></strong><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/706078/Web/Other/blobid2_1765611065.webp" width="215" height="224"><br><strong>Output:</strong> [12, 16]
<strong>Explanation:</strong> Each level contains one node, 
so the shortest range is [12, 16].</span></pre>
<p><br><span style="font-size: 18px;"><strong>Your Task:</strong><br>You don't need to read input or print anything. Complete the function <strong>shortestRange() </strong>which takes the root of the tree as an input parameter and returns the pair of numbers</span></p>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:</strong> O(N)<br><strong>Expected Auxiliary Space:</strong> O(N)</span></p>
<p><br><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ N&nbsp;≤ 10<sup>5</sup><br>1 ≤ Node Value ≤ 10<sup>5</sup></span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>two-pointer-algorithm</code>&nbsp;<code>Binary Search Tree</code>&nbsp;<code>Tree</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;
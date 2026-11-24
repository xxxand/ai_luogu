## 题意简述

给定两副从顶到底排好的牌，每副各有 $N$ 种牌，每种出现 $K$ 次。顶部相同就能一起取走这两张牌并得一分，顶部不同则丢去任意一副的顶牌。求最大得分。

## 思路

把每次得分时取走的牌记下来。这些牌在两副牌中出现的顺序都不能改变，因此它们组成一个公共子序列。接下来要确认，丢牌和配对的规则允许我们拿到最长公共子序列的分数。

两张顶牌不同时，选一组最长的匹配。它的第一对牌至多用到一张顶牌，可以丢去没用到的那张。两张顶牌相同时，也可以直接配对。若原来的第一对牌用到其中一张顶牌，就用另一张顶牌替换这对牌中较靠后的那张，后续匹配的位置仍然递增。两张顶牌如果都没用到，就能把它们作为新的一对排到最前面，原匹配也就不是最长的。这样每一步都能保留获取最优分数的可能，求答案等价于求最长公共子序列。

计算时只考虑能配对的位置。先按牌面记录第二副牌中每种牌的出现位置，再从上往下扫第一副牌。当前牌若和第二副牌的第 $j$ 张匹配，之前配过的牌都得在第二副牌的前 $j-1$ 个位置中。查询这些位置上的最大匹配长度，加一就能得到新的结尾长度。用维护前缀最大值的树状数组执行查询，随后用新的长度更新位置 $j$。

一张牌可能对应第二副牌的 $K$ 个位置，更新时要防止这一张牌被重复使用。把这些位置从大到小处理即可。轮到位置 $j$ 时，本轮更新都发生在 $j$ 右侧，前缀 $[1,j-1]$ 中就只有之前扫描过的牌产生的长度。每个合法的匹配结尾都在它所属的轮次更新，最后查询整个树状数组即可。

## 复杂度分析

记 $M=NK$。每张牌有 $K$ 个匹配位置，共做 $MK$ 次前缀查询和单点更新。时间复杂度为 $O(MK\log(M+1))$，空间复杂度为 $O(M+N)$。

## 参考代码

枚举稀疏匹配位置的做法参考 NCPC 2024 官方赛包中的 nils.cpp。 [官方赛包](https://nordic.icpc.io/ncpc2024/)

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Fenwick {
    int n;
    vector<int> bit;

    explicit Fenwick(int n) : n(n), bit(n + 1) {}

    // 返回第二副牌前 pos 张牌上的最大匹配长度。
    int query(int pos) const {
        int res = 0;
        for (; pos > 0; pos -= pos & -pos)
            res = max(res, bit[pos]);
        return res;
    }

    void update(int pos, int val) {
        for (; pos <= n; pos += pos & -pos)
            bit[pos] = max(bit[pos], val);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;
    int m = n * k;
    vector<int> a(m);
    for (int &x : a) cin >> x;

    vector<vector<int>> pos(n + 1);
    for (int j = 1; j <= m; ++j) {
        int x;
        cin >> x;
        pos[x].push_back(j);
    }

    Fenwick tree(m);
    for (int x : a) {
        // 逆序访问可让当前一轮写入的值避开后续的前缀查询。
        for (auto it = pos[x].rbegin(); it != pos[x].rend(); ++it) {
            int j = *it;
            tree.update(j, tree.query(j - 1) + 1);
        }
    }
    cout << tree.query(m) << '\n';
    return 0;
}
```
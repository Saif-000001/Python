#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
#ifdef LOKAL
#include "DEBUG_TEMPLATE.h"
#else
#define HERE
#define debug(args...)
#endif
const int MOD = 1000000007;
const int N = 2e5 + 5;
typedef pair<int, int> pii;

void TEST_CASES()
{
    int n, a, b, c, d;
    cin >> n >> a >> b >> c >> d;

    int sum_ab, subtruct_ab, sum_cd, subtruct_cd;
    sum_ab = (a + b) * n;
    subtruct_ab = abs(a - b) * n;
    sum_cd = (c + d);
    subtruct_cd = abs(c - d);

    if (((sum_ab >= subtruct_cd) && (sum_cd >= subtruct_ab)) || ((sum_ab >= subtruct_cd) && (sum_cd >= subtruct_ab)))
        cout << "Yes\n";
    else
        cout << "No\n";
}

int32_t main()
{
#ifndef LOKAL
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
#endif
    int t = 1;
    cin >> t;
    while (t--)
    {
        TEST_CASES();
    }
    return 0;
}
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
    int n;
    string s;
    cin >> n >> s;
    vector<int> id;
    for (int i = 0; i < n; ++i)
        if (s[i] == '2')
            id.push_back(i);
    int k = id.size();
    if (k == 1 || k == 2)
    {
        cout << "NO\n";
        return;
    }
    vector<string> t(n, string(n, '='));
    for (int i = 0; i < n; ++i)
        t[i][i] = 'X';
    for (int i = 0; i < k; ++i)
    {
        int x = id[i], y = id[(i + 1) % k];
        t[x][y] = '+';
        t[y][x] = '-';
    }
    cout << "YES\n";
    for (int i = 0; i < n; ++i)
        cout << t[i] << '\n';
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
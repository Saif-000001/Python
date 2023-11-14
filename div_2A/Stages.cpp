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
    int n, m;
    cin >> n >> m;
    string s;
    cin >> s;
    sort(s.begin(), s.end());
    int ans = 0;
    char ch = 'a' - 2;
    int l = 0;
    bool f = false;
    for (int i = 0; i < n; i++)
    {
        if (s[i] >= ch + 2)
        {
            ch = s[i];
            ans += s[i] - 'a' + 1;
            l++;
            if (l >= m)
            {
                f = true;
                break;
            }
        }
    }
    if (f)
        cout << ans << '\n';
    else
        cout << -1 << '\n';
}

int32_t main()
{
#ifndef LOKAL
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
#endif
    int t = 1;
    // cin >> t;
    while (t--)
    {
        TEST_CASES();
    }
    return 0;
}
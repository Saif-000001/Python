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
    cin >> n;
    string s;
    cin >> s;
    int ans = 0, cnt = 0;
    bool f = false;
    for (int i = 0; i < n; i++)
    {
        if (s[i] == '.')
        {
            cnt++;
            ans++;
            if (cnt == 3)
            {
                f = true;
                break;
            }
        }
        else
            cnt = 0;
    }

    if (f)
        cout << 2 << "\n";
    else
        cout << ans << "\n";
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
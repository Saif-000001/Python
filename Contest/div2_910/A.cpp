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
    int n, k;
    cin >> n >> k;
    string s;
    cin >> s;

    int cntB = 0;
    for (int i = 0; i < n; i++)
    {
        if (s[i] == 'B')
            cntB++;
    }

    if (cntB == k)
    {
        cout << 0 << "\n";
        return;
    }

    if (cntB > k)
    {
        cout << 1 << '\n';
        int cnt = 0;
        for (int i = 0; i < n; i++)
        {
            if (s[i] == 'B')
                cnt++;
            if (cnt == cntB - k)
            {
                cout << i + 1 << ' ' << 'A' << '\n';
                break;
            }
        }
    }
    else
    {
        cout << 1 << '\n';
        int cnt = 0;
        for (int i = 0; i < n; i++)
        {
            if (s[i] == 'A')
                cnt++;
            if (cnt == k - cntB)
            {
                cout << i + 1 << ' ' << 'B' << '\n';
                break;
            }
        }
    }
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
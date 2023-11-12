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
    if (n == 1)
    {
        cout << -1 << "\n";
        return;
    }

    if (n == 2)
    {
        int x, y;
        cin >> x >> y;
        if (x == y)
        {
            cout << -1 << "\n";
            return;
        }
        else
        {
            cout << 1 << "\n"
                 << 1 << "\n";
            return;
        }
    }

    vector<int> a(n);
    int mx = 0;
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
        if (a[i] < a[mx])
            mx = i;
    }

    cout << 1 << "\n"
         << mx + 1 << "\n";
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
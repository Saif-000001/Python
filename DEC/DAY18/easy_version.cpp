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
    int a = 0, b = 0;
    for (int i = 0; n != 0; i++)
    {
        if (i % 4 == 0 || i % 4 == 3)
        {
            a += min(n, i + 1);
            n -= min(n, i + 1);
        }
        else
        {
            b += min(n, i + 1);
            n -= min(n, i + 1);
        }
    }
    cout << a << " " << b << "\n";
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
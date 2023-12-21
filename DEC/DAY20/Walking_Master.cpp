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
    int a, b, c, d;
    cin >> a >> b >> c >> d;

    if (a == c and b == d)
    {
        cout << 0 << "\n";
        return;
    }

    if (b > d)
    {
        cout << -1 << "\n";
        return;
    }

    int shift = d - b;
    if (a < c - shift)
        cout << -1 << "\n";
    else
    {
        ll ans = a - (c - shift) + shift;
        cout << ans << "\n";
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
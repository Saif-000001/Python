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
    ll a, b, n, m;
    cin >> a >> b >> n >> m;

    if (a * m >= b * (m + 1))
        cout << b * n << "\n";
    else
    {
        ll c = n / (m + 1) * m, md = n % (m + 1);
        ll ans = c * a + md * min(a, b);
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
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
    vector<int> a(n);
    for (int i = 0; i < n; i++)
        cin >> a[i];

    int ans = a[0];
    int sum = a[0];
    int mn = min(0, a[0]);

    for (int i = 1; i < n; i++)
    {
        if ((abs(a[i] & 1) && abs(a[i - 1] & 1)) || (abs(a[i] % 2 == 0) && abs(a[i - 1] % 2 == 0)))
        {
            mn = 0;
            sum = 0;
        }
        sum += a[i];
        ans = max(ans, sum-mn);
        mn = min(mn, sum);
    }
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
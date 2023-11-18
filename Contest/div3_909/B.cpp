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
    ll n;
    cin >> n;
    vector<ll> pre;
    pre.push_back(0);
    ll sum = 0, ans = 0;
    for (int i = 0; i < n; i++)
    {
        ll x;
        cin >> x;
        sum += x;
        pre.push_back(sum);
    }

    for (int i = 1; i <= n; i++)
    {
        if (n % i == 0)
        {
            vector<ll> v;
            for (int j = i; j <= n; j += i)
            {
                sum = pre[j] - pre[j - (i)];
                v.push_back(sum);
            }
            sort(v.begin(), v.end());
            ans = max(ans, v[v.size() - 1] - v[0]);
        }
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
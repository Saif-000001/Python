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

    int ans = 0;
    for (int i = 0; i < n; i++)
    {
        if (a[i] % 2 == 0)
            a[i] = 0;
        else
            a[i] = 1;
    }

    for (int i = 0; i < n - 1; i++)
    {
        if (a[i] == 1 && a[i + 1] == 1)
            ans++;
        else if (a[i] == 0 && a[i + 1] == 0)
            ans++;
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
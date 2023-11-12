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
    map<int, int> mp;
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
        mp[a[i]]++;
    }

    vector<int> add;
    for (auto it : mp)
    {
        if (it.second >= 2)
            add.push_back(it.first);
    }

    if (add.size() < 2)
    {
        cout << -1 << "\n";
        return;
    }

    vector<int> ans;
    bool f1 = false, f2 = false;
    for (auto i : a)
    {
        if (i == add[0])
        {
            ans.push_back(f1 ? 2 : 1);
            f1 = true;
        }
        else if (i == add[1])
        {
            ans.push_back(f2 ? 3 : 1);
            f2 = true;
        }
        else
            ans.push_back(1);
    }

    for (auto i : ans)
    {
        if (i > 0)
            cout << i << " ";
    }
    cout << "\n";
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
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
    int like = 0, dislike = 0;
    for (int i = 1; i <= n; i++)
    {
        int x;
        cin >> x;
        if (x > 0)
            like++;
        else
            dislike++;
    }

    for (int i = 1; i <= n; i++)
    {
        if (i <= like)
            cout << i << ' ';
        else
            cout << like * 2 - i << ' ';
    }
    cout << "\n";
    for (int i = 1; i <= n; i++)
    {
        if (i <= dislike*2)
            cout << i % 2 << ' ';
        else
            cout << i - dislike * 2 << ' ';
    }
    cout<<"\n";
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
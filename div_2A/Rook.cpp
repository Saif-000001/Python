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
typedef pair<char, char> pii;

void TEST_CASES()
{
    string s;
    cin >> s;

    for (int i = 1; i <= 8; i++)
    {
        if (i != s[1] - '0')
            cout << s[0] << i << '\n';
    }

    for (int i = 0; i < 8; i++)
    {
        if (i != s[0] - 'a')
            cout << char('a' + i) << s[1] << '\n';
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
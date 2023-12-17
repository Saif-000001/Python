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
    string s;
    cin >> s;
    int n = s.size();
    if ((count(s.begin(), s.end(), 'a') == n) || (count(s.begin(), s.end(), 'b') == n))
    {
        cout << s[0] << " " << s.substr(1, n - 2) << " " << s[n - 1] << "\n";
        return;
    }

    if (s[0] == 'a')
    {
        if (s[1] == 'a')
            cout << s[0] << " " << s[1] << " " << s.substr(2, n - 1) << "\n";
        else
        {
            int indx = -1;
            for (int i = 2; i < n; i++)
            {
                if (s[i] == 'a')
                {
                    indx = i;
                    break;
                }
            }

            if (indx == -1)
                cout << s[0] << " " << s.substr(1, n - 2) << " " << s[n - 1] << "\n";
            else
            {
                cout << s[0] << " ";
                for (int i = 1; i < indx; i++)
                    cout << s[i];
                cout << " ";
                for (int i = indx; i < n; i++)
                    cout << s[i];
                cout << "\n";
            }
        }
    }

    if (s[0] == 'b')
    {
        if (s[1] == 'b')
            cout << s[0] << " " << s[1] << " " << s.substr(2, n - 1) << "\n";
        else
        {
            int indx = -1;
            for (int i = 1; i < n; i++)
            {
                if (s[i] == 'b')
                {
                    indx = i;
                    break;
                }
            }

            if (indx == -1)
                cout << s[0] << " " << s[1]<< " " << s.substr(2, n-1) << "\n";
            else
            {
                cout << s[0] << " ";
                for (int i = 1; i < indx; i++)
                    cout << s[i];
                cout << " ";
                for (int i = indx; i < n; i++)
                    cout << s[i];
                cout << "\n";
            }
        }
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
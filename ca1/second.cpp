#include <bits/stdc++.h>

using namespace std;

const int N = 1e4 + 5;
const int MOD = 1e6 + 3;

int n;
string s;
int ind;
int a[N];
int tmp[N];

void rec(int l, int r)
{
    if (r - l < 2)
    {
        a[l] = l;
        return;
    }
    int mid = (r + l) / 2;

    rec(l, mid);
    rec(mid, r);
    int p1 = l, p2 = mid;
    int p = l;
    while (p1 < mid && p2 < r)
    {
        if (s[ind] == '1')
            tmp[p] = a[p1++];
        else
            tmp[p] = a[p2++];
        p++;
        ind++;
    }
    if (p1 < mid)
        while (p1 < mid)
        {
            tmp[p] = a[p1++];
            p++;
        }
    if (p2 < r)
        while (p2 < r)
        {
            tmp[p] = a[p2++];
            p++;
        }
    for (int i = l; i < r; i++)
        a[i] = tmp[i];
}

int res[N];

int main()
{
    cin >> n;
    cin >> s;
    rec(0, n);
    for (int i = 0; i<n; i++)
        res[a[i]] = i;       
    // for (int i = 0; i < n; i++)
        // cout << res[i] << endl;
    int ans = 1;
    for (int i = 0; i < n; i++)
        ans = (31 * ans + (res[i] + 1)) % MOD;
    cout << ans << endl;
}
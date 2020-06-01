#include <iostream>
#include <vector>

using namespace std;

const int MAXN = 1005;
const int MAXK = 105;
long long dp[2][MAXN][MAXK];

const int mod = 1e9 + 7;

int main()
{
    int n, m, k, d;
    cin >> n >> m >> k;
    vector<vector<int>> A(n);
    for (int l = 0; l < n; l++)
    {
        A[l] = vector<int>(m);
        for (int i = 0; i < m; i++)
        {
            cin >> d;
            A[l][i] = d;
        }
    }
    dp[(n - 1) % 2][m - 1][0] = 1;
    dp[(n - 1) % 2][m - 1][A[n - 1][m - 1]] = 1;

    for (int i = n - 1; i >= 0; i--)
    {
        for (int j = m - 1; j >= 0; j--)
        {
            for (int p = 0; p <= k; p++)
            {
                if (i == (n - 1))
                {
                    if (j == (m - 1))
                        continue;
                    dp[i % 2][j][p] = (dp[i % 2][j + 1][p] + (p < A[i][j] ? 0 : dp[i % 2][j + 1][p - A[i][j]])) % mod;
                }
                if (j == (m - 1))
                {
                    dp[i % 2][j][p] = (dp[(i + 1) % 2][j][p] + (p < A[i][j] ? 0 : dp[(i + 1) % 2][j][p - A[i][j]])) % mod;
                }
                else
                    dp[i % 2][j][p] = (dp[(i + 1) % 2][j][p] + dp[i % 2][j + 1][p] + (p < A[i][j] ? 0 : dp[(i + 1) % 2][j][p - A[i][j]]) + (p < A[i][j] ? 0 : dp[i % 2][j + 1][p - A[i][j]])) % mod;
            }
        }
    }
    cout << dp[0][0][k] % mod;

    return 0;
}
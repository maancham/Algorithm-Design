#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define MAX 10000

const int mod = 1e6 + 7;
long long dp[2][MAX];
long long key[MAX];

void fill_dp(int n)
{
    for (int k = 0; k < n; k++)
    {
        dp[(n - 1) % 2][k] = 1;
    }
}

long long calc_result(int A[], long long val, int n)
{
    long long out = A[n - 1];
    long long temp_val = val;
    for (int k = 0; k < n; k++)
    {
        key[k] = temp_val;
        if (A[k] > temp_val)
        {
            temp_val = A[k];
        }
    }

    for (int k = n; k >= 0; k--)
    {
        if ((k == n - 1) || (k == n))
            continue;
        long long point = key[k];
        for (int i = 0; i < k + 1; i++)
        {
            dp[k % 2][i] = (i * dp[(k + 1) % 2][i] + dp[(k + 1) % 2][i + 1]) % mod;
        }
        int i = 1;
        while (i < A[k])
        {
            if (point <= i)
            {
                out += dp[k % 2][i] % mod;
            }
            else
            {
                out += dp[k % 2][point] % mod;
            }
            i++;
        }
    }
    return out;
}

int main()
{
    int n, temp;
    cin >> n;
    int A[n];
    long long result;
    for (int i = 0; i < n; i++)
    {
        cin >> temp;
        A[i] = temp;
    }
    fill_dp(n);
    result = calc_result(A, 0, n);
    cout << result % mod << endl;

    return 0;
}
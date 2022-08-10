#include <iostream>
using namespace std;
int main()
{
    long long n, num, total, sum = 0;
    cin >> n;
    total = (n * (n + 1)) / 2;
    for (int i = 1; i < n; i++)
    {
        cin >> num;
        sum += num;
    }
    int r = total - sum;
    cout << r << endl;
}
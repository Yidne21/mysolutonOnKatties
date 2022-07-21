#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;
int main()
{
    double avg, per;
    int n, t, cnt, sum = 0, m;
    cin >> t;
    while (t > 0)
    {
        cin >> n;
        int arr[n];
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
        }

        for (int i = 0; i < n; i++)
        {
            sum += arr[i];
        }

        avg = sum / n;

        for (int i = 0; i < n; i++)
        {
            if (arr[i] > avg)
            {
                cnt++;
            }
        }
        per = (cnt / n) * 100;
        cout << setprecision(3) << per << endl;
        cout << cnt << endl;
        cnt = 0;
        t--;
    }
}
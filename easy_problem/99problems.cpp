#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    long long n, d = 0, interval, cp;
    cin >> n;
    if (n > 0)
    {
        cp = n;
        while (n > 0)
        {
            d += 1;
            n = n / 10;
        }
        interval = pow(10, d - 1);
        if (interval < 100)
        {
            cout << 99 << endl;
        }
        else if (cp % 100 == 99)
        {
            cout << cp << endl;
        }
        else
        {
            int l2d = cp % interval;
            if (l2d + 1 < 50)
            {
                cout << cp - (l2d + 1) << endl;
            }
            else
            {
                l2d += 1;
                int add = interval - l2d;
                cout << cp + add << endl;
            }
        }
    }
}
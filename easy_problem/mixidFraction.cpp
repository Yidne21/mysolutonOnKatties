#include <iostream>
using namespace std;
int main()
{
    long long n, d, r, q;
    while (true)
    {
        cin >> n >> d;
        if (n == 0 && d == 0)
        {
            break;
        }
        else
        {
            r = n % d;
            q = (n - r) / d;
            cout << q << " " << r << " / " << d << endl;
        }
    }
}
#include <iostream>
using namespace std;
int main()
{
    int n, d;
    cin >> n;
    d = ((n % 10) * 10);
    n = n / 10;
    cout << d + n << endl;
}
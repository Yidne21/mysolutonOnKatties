#include <iostream>
#include <cmath>
using namespace std;
int findprod_digit(int n)
{
    int pro = 1;
    while (n > 0)
    {
        if (n % 10 > 0)
        {
            pro *= n % 10;
        }
        n = n / 10;
    }
    return pro;
}
int main()
{
    int num, pro = 1, next;
    cin >> num;
    pro = findprod_digit(num);
    while (true)
    {
        if (pro >= 10)
        {
            pro = findprod_digit(pro);
        }
        else
        {
            cout << pro << endl;
            break;
        }
    }
}
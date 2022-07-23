#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;
int main()
{
    int ki, ki1, oi, oi1, kf, kf1, of, of1;
    cin >> ki >> ki1 >> oi >> oi1 >> kf >> kf1 >> of >> of1;
    double x, y, d;
    x = pow((kf - of), 2);
    y = pow((kf1 - of1), 2);
    d = sqrt(x + y);
    cout << fixed << setprecision(6) << d << endl;
}
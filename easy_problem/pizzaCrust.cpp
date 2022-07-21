#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    double r, c, perc, apizza, tarea;
    cin >> r >> c;
    tarea = M_PI * r * r;
    apizza = M_PI * (r - c) * (r - c);
    perc = (apizza / tarea) * 100;
    cout << fixed << perc << endl;
}
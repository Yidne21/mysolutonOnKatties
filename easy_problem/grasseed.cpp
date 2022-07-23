#include <iostream>
using namespace std;
int main()
{
    double c, w, l, area;
    int n;
    cin >> c;
    cin >> n;
    while (n)
    {
        cin >> w >> l;
        area += w * l;
        n--;
    }
    cout << fixed << area * c << endl;
}
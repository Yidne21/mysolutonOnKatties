#include <iostream>
#include <string.h>
using namespace std;
int main()
{
    int r, in;
    string req;
    cin >> r;
    in = 7;
    for (int i = 0; i < r; i++)
    {
        cin >> req;
        if (in >= 0 && in <= 10)
        {
            if (strcmp(req, "Skru op!") == 0)
            {
                in += 1;
            }
            else
            {
                in -= 1;
            }
        }
    }
    cout << in;
}
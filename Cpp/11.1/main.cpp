#include <iostream>
using namespace std;
int main() {
    int a, max, min;
    cin >> a;
    min=a;
    max=a;
    while (a!=0){
        if (a > max){
            max=a;
        }
        else if (a<min){
            min=a;
        }
        cin >> a;
    }
    cout << "max: " << max << " min: " << min << endl;
    return 0;
}
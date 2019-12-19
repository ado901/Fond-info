#include <iostream>
#include <cmath>
using namespace std;

float heron( float l1, float l2, float l3){
    float s = (l1 + l2 + l3) / 2;
    float area = sqrt(s * (s - l1) * (s - l2) * (s - l3));
    return area;
}
int main() {
    float l1, l2, l3;
    cout << "Lato? " <<endl;
    cin >> l1;
    cout << "Lato? " <<endl;
    cin >> l2;
    cout << "Lato? " <<endl;
    cin >> l3;
    cout << heron(l1, l2, l3);
    return 0;
}
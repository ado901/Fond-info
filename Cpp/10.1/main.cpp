#include <iostream>
#include <cmath>
using namespace std;
const float PI = acos(-1);
float volume(float raggio, float altezza){
    return PI * (raggio * raggio) * altezza;
}
float superficie( float raggio, float altezza){
    return 2* PI * raggio* (raggio + altezza);
}
int main() {
    cout << volume(5.0,11.0) << endl<< superficie(5.0, 11.0);

    return 0;
}
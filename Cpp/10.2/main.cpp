#include <iostream>
#include <cmath>
using namespace std;
const float PI = acos(-1);
class Cilindro{
    float raggio_, altezza_;
public:
    Cilindro(float raggio, float altezza) {raggio_= raggio; altezza_= altezza;}
    float volume(){
        return PI * (raggio_ * raggio_) * altezza_;
    }
    float superficie(){
        return 2* PI * raggio_* (raggio_ + altezza_);
    }
};
int main() {
    float raggio, altezza;
    cin >> raggio;
    cin >> altezza;
    Cilindro* c= new Cilindro(raggio, altezza);
    cout << c->superficie()<< endl;
    cout << c->volume()<< endl;
    return 0;
}
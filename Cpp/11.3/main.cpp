#include <iostream>
#include <cmath>
using namespace std;
float const PI = acos(-1);

class Ellisse{
    float a, b;
public:
    Ellisse(float semiasse1, float semiasse2) {a= semiasse1; b= semiasse2;}
    float area(){
        return PI * a * b;
    }
    float focaldis(){
        return 2* sqrt(abs((a * a) - (b * b)));
    }
};
int main() {
    float sem1, sem2;
    cout << "inserire semiassi ellisse: "<< endl;
    cin >> sem1;
    cin >> sem2;
    Ellisse* e = new Ellisse(sem1, sem2);
    cout << e->area() << endl;
    cout << e->focaldis() << endl;
    delete(e);
    return 0;
}
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> lista1;
    vector<int> lista2;
    vector<int> lista3;

    int num, somma=0, val=0;
    cout << "numeri interi(0 per finire) " << endl;
    cin >> num;
    while (num != 0) {
        val+=1;
        somma+=num;
        lista3.push_back(num);
        cin >> num;
    }
    cout << float(somma)/float(val) << endl;

    float media = float(somma)/float(val);
    for (int i : lista3){
        if (i < media){
            lista1.push_back(i);
        }
        if (i >= media){
            lista2.push_back(i);
        }

    }
    for (int i : lista1){
        cout << i << ", ";
    }
    cout << endl;
    for (int i: lista2){
        cout <<i << ", ";
    }
    cout << endl;
    return 0;
}
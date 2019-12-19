#include <iostream>
#include <fstream>
using namespace std;
int main() {
    string riga;
    int maiuscole, minuscole;
    maiuscole=0;
    minuscole=0;
    cout << " inserire testo: " << endl;
    getline(cin, riga);
    for (char lettera : riga){
        if (islower(lettera)){
            minuscole++;
        }
        else if (isupper(lettera)){
            maiuscole++;

        }
    }
    cout << "maiuscole: " << maiuscole << " minuscole: " << minuscole << endl;
    return 0;
}
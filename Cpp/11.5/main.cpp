#include <iostream>
#include <time.h>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    vector<int> dadi, checked;
    int n, result,result1, result2, count;
    cout << "numero dadi? " << endl;
    srand(time(NULL));
    cin >> n;
    for (int i = 0; i < n; i++){
       result = rand() % 6 + 1;
       result1 = rand() % 6 + 1;
       result2 = rand() % 6 + 1;
       cout << "Risultati: " << result << " " << result2 << " " << result1 << " somma: "<< result + result1 + result2 << endl;
       dadi.push_back(result + result1 + result2);
    }
    for (int i : dadi){
        if (find(checked.begin(), checked.end(), i) == checked.end()) {
            checked.push_back(i);
            count=0;
            for (int k: dadi) {
                if( i == k){
                    count+=1;
                }
            }
            cout << " risultato " << i << " presente volte: " << count << endl;
        }
    }

    return 0;
}
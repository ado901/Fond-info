#include <iostream>
#include <vector>
#include <time.h>
using namespace std;
vector<vector<float>> smooth(vector<vector<float>> matrix){
    int dx, dy;
    for( dx, dy)

}
int main() {
    int righe= 6, colonne= 6;
    srand(time(NULL));
   vector<vector<float>> matrice(righe, vector<float>(colonne));
   for (int i=0; i < righe; i++){
       for(int k=0; k < colonne; k++){
           matrice[i][k]= rand()% 9;
       }
   }
   for( vector<float> prova : matrice){
       for (float a: prova){
           cout << a << " ";
       }
       cout << endl;

   }
    return 0;
}
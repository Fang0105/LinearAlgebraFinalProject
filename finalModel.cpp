# include <iostream> 
# include <math.h> 
 
using namespace std ; 
 
int main () 
{ 
    double dis , time , cost ; 
   
    cout << "距離" ; 
    cin >> dis ; 
    cout << endl << "時間" ; 
    cin >> time ; 
    cout << endl << "花費" ; 
    cin >> cost ; 
    double df , tf , cf ; 
    df = 0.0227 * dis ; 
    tf = 1.3021 * time ; 
    cf = 0.0026 * cost + 1.7492 ; 
    cout << df<<" "<<tf<<" "<<cf;
    cout << endl << "幾何平均數" << pow ( df * tf * cf , 0.3333333333333333 ) ; 
 return 0 ;
}
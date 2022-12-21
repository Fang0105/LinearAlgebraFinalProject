# include <iostream> 
# include <math.h> 
 
using namespace std ; 

double count(double dis, double time, double cost, double realf){
 double df , tf , cf , pricf; 
    df = 0.0227 * dis ; 
    tf = 1.3021 * time ; 
    cf = 0.0026 * cost + 1.7492 ; 
    cout << df<<" "<<tf<<" "<<cf;
    pricf = pow ( df * tf * cf , 0.3333333333333333 );
    cout << endl << "幾何平均數" << pricf << endl ;
    double e = sqrt((pricf - realf)*(pricf - realf))/realf;
    return e;
}
int main () 
{ 
    
    double e, error_c, error_g=1;
    double dis , time , cost, realf;
    int n=10;
 while(n--){
  
    cout << "距離" ; 
    cin >> dis ; 
    cout << endl << "頻率" ;
 cin >> realf ;
    cout << endl << "時間" ; 
    cin >> time ; 
    cout << endl << "花費" ; 
    cin >> cost ; 
     
    double e = count(dis, time, cost, realf)*100;
    error_c += e;
    error_g *= e;
 }
 cout << endl << "誤差" << pow(error_g, 0.1); 
 
 return 0 ;
}
#include <iostream>
using namespace std;
//Promila Agarwal going over virtual functions.

class Shape{
public:
    int edge_length;
    /*virtual 
    int circumference () {
        cout<<"Circumference of Base Class\n";
        return 0;
    } */
     virtual int circumference() = 0;

};
class Triangle: public Shape{
public:
    int circumference () {
        cout<<"Circumference of Triangle Class\n";
        return 3 * edge_length;
    }
};
int main(){
    Shape *x = new Shape();
    x->circumference(); // prints “Circumference of Base Class”
    Shape *y = new Triangle();
    y->circumference(); // prints “Circumference of Triangle Class”
    return 0;
}

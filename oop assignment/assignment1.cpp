#include <iostream>
using namespace std;
class complex{
    private:
    int real,imag;
    public:
    friend ostream & operator <<(ostream &out,complex const &obj);
    friend istream & operator >> (istream &in, complex &obj);
    complex(int r=0,int i=0){
        real=r;
        imag=i;
    }
    complex operator +(complex const &obj){
        complex obj1;
        obj1.real=real+obj.real;
        obj1.imag=imag+obj.imag;
        return obj1;
    }
    complex operator *(complex const &obj){
        complex obj1;
        obj1.real=((real)*(obj.real))-((imag)*(obj.imag));
        obj1.imag=((real)*(obj.imag))+((imag)*(obj.real));
        return obj1;
    }
};
ostream & operator <<(ostream &out,complex const &obj){
    out<<obj.real;
    out<<"+i"<<obj.imag;
    return out;
}
istream & operator >> (istream &in, complex &obj){
    cout<<"ENTER THE REAL PART: "<<endl;
    in>>obj.real;
    cout<<"ENTER THE IMAGINARY PART: "<<endl;
    in>>obj.imag;
    return in;
}
int main(){
    complex c1,c2,c3,c4;
    cout<<"ENTER THE FIRST NUMBER: "<<endl;
    cin>>c1;
    cout<<"THE FIRST NUMBER is : "<<c1<<endl;
    cout<<"ENTER THE SECOND NUMBER: "<<endl;
    cin>>c2;
     cout<<"THE SECOND NUMBER is : "<<c2<<endl;
    c3=c1+c2;
    cout<<"ADDITION OF TWO NUMBERS IS:"<<c3<<endl;
    cout<<"MULTIPLICATION OF TWO NUMBERS IS:"<<endl;
    return 0;
}

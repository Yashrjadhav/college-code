/*PROBLEM STATEMENT:
Write a C++ program that creates an output file, writes information to it, closes the file, open
it again as an input file and read the information from the file*/
#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;
class file{
    public:
    string str1,str2,str;
    void write(){
        ofstream obj1;
        obj1.open("xyz.txt");
        cout<<"ENTER THE DATA IN THE FILE: "<<endl;
        getline(cin,str1);
        obj1<<str1;
        obj1.close();
        cout<<"CLOSING THE FILE!!!!!"<<endl;
    }
    void append()
    {
        ofstream obj;
        obj.open("xyz.txt",ios::app);
        cout<<"ENTER THE DATA YOU WANT TO APPEND IN THE FILE:"<<endl;
        getline(cin,str);
        obj<<str;
        obj.close();
        cout<<"CLOSING APPENDED FILE!!! "<<endl;
    }
    void read(){
        ifstream obj2("xyz.txt");
        cout<<"YOUR READ DATA IS :"<<endl;
        while(getline(obj2,str2)){
            cout<<str2;
        }
        obj2.close();
    }
};
int main(){
    file obj3;
    obj3.write();
    obj3.append();
    obj3.read();
    return 0;
}
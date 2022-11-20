#include <iostream>
#include<fstream>
#include<string.h>
using namespace std;
class employee{
    public:
    int id;
    string name;
    float salary;
    string address;
    friend class student;

};
class student{
    public:
    string name1;
    int id1;
    string add;
    void input(employee &);
    void display(employee &);

};
void student::input(employee &obj){
    ofstream obj3;
    obj3.open("file123.txt");
    cout<<"ENTER THE NAME OF EMPLOYEE:"<<endl;
    getline(cin,obj.name);
    obj3<<obj.name<<endl;
    cout<<"ENTER THE ID OF EMPLOYEE:"<<endl;
    cin>>obj.id;
    obj3<<obj.id<<endl;
    cout<<"ENTER THE ADDRESS OF EMPLOYEE:"<<endl;
    cin.ignore();
    getline(cin,obj.address);
    obj3<<obj.address<<endl;
    cout<<"ENTER THE SALARY OF EMPLOYEE:"<<endl;
    cin>>obj.salary;
    obj3<<obj.salary<<endl;
    cout<<"***********************************"<<endl;
    cout<<"ENTER THE NAME OF STUDENT:"<<endl;
    cin.ignore();
    getline(cin,name1);
    obj3<<name1<<endl;
    cout<<"ENTER THE ID OF STUDENT:"<<endl;
    cin>>id1;
    obj3<<id1<<endl;
    cout<<"ENTER THE ADDRESS OF STUDENT :"<<endl;
    cin.ignore();
    getline(cin,add);
    obj3<<add<<endl;
    obj3.close();
}
void student:: display(employee &obj1){
    ifstream obj5;
    obj5.open("file123.txt");
    cout<<"READING THE FILE"<<endl;
    while(getline(obj5,obj1.name)){
        cout<<obj1.name<<endl;
    }
    cout<<"CLOSING THE FILE"<<endl;
    obj5.close();
}
int main(){
    student obj11;
    employee obj22;
    obj11.input(obj22);
    obj11.display(obj22);
}


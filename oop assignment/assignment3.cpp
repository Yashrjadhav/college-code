#include <iostream>
#include<string>
using namespace std;
class publication{
    protected:
    string title;
    float price;
    public:
    publication(){
        title=" ";
        price=0.0;
        }
    publication(string t,float p){
        title=t;
        price=p;
        
        }
};
class book : public publication{
    int pagecount;
    public:
    book(){
        pagecount=0;
        }
    book(string t,float p,int pc):publication(t,p){
        pagecount=pc;
        }
    void display(){
        cout<<"************************"<<endl;
        cout<<"TITLE:"<<title<<endl;
        cout<<"PRICE: "<<price<<endl;
        cout<<"PAGECOUNT :"<<pagecount<<endl;
        cout<<"************************"<<endl;
        }      
};

class CD : public publication{
    float time;
    public:
    CD(){
        time=0.0;
        }
    CD(string t,float p,float tim):publication(t,p){
        time=tim;
        }
    void display()
    {
        cout<<"************************"<<endl;
        cout<<"TITLE:"<<title<<endl;
        cout<<"PRICE:"<<price<<endl;
        cout<<"TIME IN SECONDS:"<<time<<endl;
        cout<<"************************"<<endl;
        }      
};
int main()
{
    float p,r,s;
    int q;
    string m,n;
    cout<<endl<<"Book data"<<endl;
    cout<<"ENTER THE TITLE OF BOOK"<<endl;
    cin>>m;
    cout<<"ENTER THE PRICE OF BOOK IN FLOAT"<<endl;
    cin>>p;
    cout<<"ENTER THE pagecount OF BOOK"<<endl;
    cin>>q;
    book b(m,p,q);
    b.display();
    cout<<endl<<"CD Data"<<endl;
    cout<<"ENTER THE TITLE OF CD"<<endl;
    cin>>n;
    cout<<"ENTER THE PRICE OF CD IN FLOAT"<<endl;
    cin>>r;
    cout<<"ENTER THE TIME IN SECONDS IN FLOAT OF CD"<<endl;
    cin>>s;
    CD c(n,r,s);
    c.display();
    return 0;
    }
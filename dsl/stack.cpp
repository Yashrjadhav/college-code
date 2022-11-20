#include <iostream>
#define l 20
using namespace std;
class stack1{
    public:
    char arr[l];
    int top,i;
    stack1()
    {
        top=-1;
    }
    int empty(){
        if (top==-1)
        {
            return 1;
        }
        else
        {
            return 0;
        }

    }
    int full(){
        if (top==l-1)
        {
            cout<<"STACK IS FULL"<<endl;
            return -1;
        }
        else
        {
            return 1;
        }
    }
    void push(char a)
    {
        if(full()==1)
        {
            for(i=0;i<100;i++)
            {
                top++;
                arr[top]=a;
            }
        }
    }
    char pop()
    {
        if(empty()==0)
        {
            char b=arr[top];
            top--;
            return b;

        }
        else
        {
            return 0;
        }
    }
    void code(){
        int flag=0;
        cout<<"ENTER THE EXPRESSION:"<<endl;
        cin.ignore();
        cin.get(arr,20);
        for(int i=0;i<arr[i]!='\0';i++)
        {
            if(arr[i]=='('||arr[i]=='{'||arr[i]=='[')
            push(arr[i]);
            if(arr[i]==')'||arr[i]=='}'||arr[i]==']')
            {
                char c=pop();
                if((arr[i]==')'&&c!='(')||(arr[i]=='}'&&c!='{')||(arr[i]==']'&&c!='['))
                {
                    cout<<"NOT WELL PARENTHESIZED "<<endl;
                    flag=1;
                    break;
                }
            }
        }
        if(empty()==1&&flag==0)
        {
        cout<<"BALANCED EXPRESSION"<<endl;
        }
        else
        {
            cout<<"UNBALANCED EXPRESSION"<<endl;

        }
    }
    void display()
    {
        if(empty()==1)
        cout<<"STACK IS EMPTY"<<endl;
        else
        {
            for(int i=0;i<l;i++)
            cout<<arr[i];
        }
    }
};
int main(){
    stack1 obj;
    int ch=1;   
    while(ch==1)
    {
        cout<<"PRESS1:ENTER THE EXORESSION:\nPRESS2:EXIT:"<<endl;
        cin>>ch;
       switch(ch)
       {
        case 1:
        obj.code();
        break;
        case 2:
        break;
        default:
        cout<<"INVALID INPUT";
        break;
       }
       if(ch!=1){
       break;
       }
    }
}
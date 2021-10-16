#include<iostream>
using namespace std;

class node{
    public :
    int data;
    node *next = NULL;
    node(int data){
        this->data = data ;
    }

};

node *insert(node* head , int i , int data){
    node* temp = head;
    node *newnode = new node(data);
    if(i==0){
        newnode -> next = temp;
        return newnode;
    }
    else{
        delete newnode;
        node *copy = insert(temp->next , i-1 , data);
        temp ->next = copy;
        return temp;
    }
}

void print( node *head){
    node *temp = head;
    while(temp!= NULL){
        cout<<temp->data<<endl;
        temp = temp->next;
    }
}

int main(){

    node *n1 = new node(10);
    node *head = n1;
    node *n2 = new node(20);
    node *n3 = new node(30);
    node *n4 = new node(40);
    node *n5 = new node(50);

    n1 ->next = n2;
    n2 ->next = n3;
    n3 ->next = n4;
    n4 ->next = n5;

    print(head);

    head = insert( head , 2 , 999);

    cout<<"change ker dia bhai"<<endl;

    print(head);
    return 0;

}

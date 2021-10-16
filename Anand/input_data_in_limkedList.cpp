#include <iostream>
using namespace std;

class node
{
public:
    int data;
    node *next;
    node(int data)
    {
        this->data = data;
        this->next = NULL;
    }
};

node *input(){
    int data;
    node *heaad = NULL;
    node *tail = NULL;
    cin>>data;
    while(data!=-1){
        node *newnode = new node(data);
        if(heaad==NULL){
            heaad = newnode;
            tail = newnode;
        }
        else{
             tail ->next =  newnode;
             tail = tail -> next ;
             }
        cin>>data;
    }
    return heaad;
}


void print(node *head)
{
    node *temp = head;
    while (temp != NULL)
    {
        cout << temp->data << endl;
        temp = temp->next;
    }
}

int main()
{
    node *head = input();
    
    print(head);

    return 0;
}

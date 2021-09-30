#include <iostream>

using namespace std;

class Node {
    public:
    int data;
    Node* left;
    Node* right;
    
    Node(int data){
        this->data = data;
        this->left = NULL;
        this->right = NULL;
    }
};

void leftView(Node* root){
    queue<Node*> q;
    q.push(root);
    q.push(NULL);

    while(!q.empty()){
        static bool status = 1;
        Node* temp = q.front();
        q.pop();
        
        if(temp!= NULL){
            if(status==1){
                cout<<temp->data<<" ";
                status = 0;
            }
            if(temp->left){
                q.push(temp->left);
            }
            if(temp->right){
                q.push(temp->right);
            }
        }else if(!q.empty()){
            status = 1;
            q.push(NULL);
        }
    }
}

int main()
{
    Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);
    root->right->left = new Node(6);
    root->right->right = new Node(7);
    
    leftView(root);
    
    return 0;
}
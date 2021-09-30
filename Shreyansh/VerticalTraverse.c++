#include<bits/stdc++.h>

using namespace std;

class Node{
	public:
	int val;
	Node* left;
	Node* right;
	
	Node(int val){
		this->val = val;
		this->left = this->right = NULL;
	}
};

map<int,vector<int> > m;

void dfs(Node* root, int dis){
	if(root==NULL) return;
	m[dis].push_back(root->val);
	
	if(root->left) dfs(root->left,dis-1);
	if(root->right) dfs(root->right,dis+1);
	
}

int main(){
	Node* node = new Node(1);
	node->left = new Node(2);
	node->right = new Node(3);
	node->left->left = new Node(4);
	node->left->right = new Node(5);
	node->right->left = new Node(6);
	node->right->right = new Node(7);
	dfs(node,0);
	map<int,vector<int> > :: iterator it;
	for(it = m.begin();it!= m.end();it++){
		for(int i=0;i<it->second.size();i++){
			cout<<it->second[i]<<" ";
		}
		cout<<endl;
	}
	
}
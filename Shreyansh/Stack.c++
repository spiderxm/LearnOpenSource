#include<iostream>
using namespace std;

#define CAPACITY 5

int top = 0;
int stack[CAPACITY];

void push(int data){
	if(top < CAPACITY){
		stack[top] = data;
	    top++;
	    cout<<"ELEMENT ADDED"<<endl;
	}else{
		cout<<"STACK IS FULL"<<endl;
	}
}

void pop(){
	if(top==0){
		cout<<"STACK IS EMPTY"<<endl;
	}else{
		cout<<"ELEMENT IS : "<<stack[top-1]<<endl;
		top--;
	}
}

void peek(){
	if(top==0){
		cout<<"STACK IS EMPTY"<<endl;
	}else{
		cout<<"ELEMENT IS : "<<stack[top-1]<<endl;
	}
}


int main(){
	push(5);
	push(6);
	push(7);
	pop();
	pop();
	peek();
	
}
#include<iostream>
using namespace std;

#define CAPACITY 5

int queue[5];
int front = 0;
int rear = -1;

void enque(int data){
	if(rear<CAPACITY){
		rear++;
	    queue[rear] = data;
	}else{
		cout<<"QUEUE IS FULL"<<endl;
	}
}

void deque(){
	for(int i=0;i<rear;i++){
		queue[i] = queue[i+1];
	}
	rear--;
}

void traversal(){
	for(int i=0;i<=rear;i++){
		cout<<queue[i]<<endl;
	}
}

int main(){
	enque(5);
	enque(6);
	enque(7);
	enque(8);
	traversal();
	cout<<"After DEQUE : "<<endl;
	deque();
	traversal();
	cout<<"SECOND"<<endl;
	deque();
	traversal();
}
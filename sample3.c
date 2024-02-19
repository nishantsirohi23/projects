#include<stdio.h>
#include<stdlib.h>


//defination for singly linked list
struct Node
{
    int data;
    struct Node *next;
};  

//function to create a new node
struct Node *newNode(int data)
{
    struct Node *new_node = (struct Node *)malloc(sizeof(struct Node));
    new_node->data = data;
    new_node->next = NULL;
    return new_node;
}

//functoin to print the linked list
void printList(struct Node *head){
    while(head != NULL){
        printf("%d ", head->data);
        head = head->next;

    }
}


int main(){
    struct Node* head = (struct Node *)malloc(sizeof(struct Node));

    head->data = 1;
    head->next = newNode(2);


    printList(head);
    return 0;
}

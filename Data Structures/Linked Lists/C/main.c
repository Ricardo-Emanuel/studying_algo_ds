#include <stdio.h>
#include <stdlib.h>

// Define a struct for a singly linked list node
struct Node {
    int data;
    struct Node* next;
};

// Define a struct for the linked list itself
struct LinkedList {
    struct Node* head;
    int size;
};

// Function to create a new node with the given data
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Function to create a new empty linked list
struct LinkedList* createLinkedList() {
    struct LinkedList* newLinkedList = (struct LinkedList*)malloc(sizeof(struct LinkedList));
    newLinkedList->head = NULL;
    newLinkedList->size = 0;
    return newLinkedList;
}

// Function to add an element to the end of the linked list
void append(struct LinkedList* linkedList, int data) {
    struct Node* newNode = createNode(data);
    if (linkedList->head == NULL) {
        linkedList->head = newNode;
    } else {
        struct Node* currentNode = linkedList->head;
        while (currentNode->next != NULL) {
            currentNode = currentNode->next;
        }
        currentNode->next = newNode;
    }
    linkedList->size++;
}

// Function to add an element to the beginning of the linked list
void prepend(struct LinkedList* linkedList, int data) {
    struct Node* newNode = createNode(data);
    newNode->next = linkedList->head;
    linkedList->head = newNode;
    linkedList->size++;
}

// Function to delete the first occurrence of an element from the linked list
void delete(struct LinkedList* linkedList, int data) {
    struct Node* currentNode = linkedList->head;
    struct Node* prevNode = NULL;
    while (currentNode != NULL && currentNode->data != data) {
        prevNode = currentNode;
        currentNode = currentNode->next;
    }
    if (currentNode != NULL) {
        if (prevNode == NULL) {
            linkedList->head = currentNode->next;
        } else {
            prevNode->next = currentNode->next;
        }
        free(currentNode);
        linkedList->size--;
    }
}

// Function to print the contents of the linked list
void printLinkedList(struct LinkedList* linkedList) {
    struct Node* currentNode = linkedList->head;
    while (currentNode != NULL) {
        printf("%d ", currentNode->data);
        currentNode = currentNode->next;
    }
    printf("\n");
}

// Example usage of the linked list functions
int main() {
    struct LinkedList* linkedList = createLinkedList();
    append(linkedList, 1);
    append(linkedList, 2);
    append(linkedList, 3);
    prepend(linkedList, 0);
    printLinkedList(linkedList);
    delete(linkedList, 2);
    printLinkedList(linkedList);
    printf("\n%d\n", linkedList->size);
    return 0;
}
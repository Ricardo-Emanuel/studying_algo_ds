# Linked List

## What is a linked list

$\quad$A Linked List is a linear data structure as an array, but it is not allocated in an contiguous block of memory. Each **NODE** of the **Linked List** has an value which can be an **int**, **float**, **char**, **string** and a reference (link) to the next **NODE** in the **Linked List**.  
$\quad$The most common way to implement a Linked List is initializing a head pointer which points to the firts element of the list and since that element we can traverse the **Linked List** and reach any element in it.

![Representation of a Linked List](../images/linked1.PNG)

## Advantages of Linked List over arrays

- Ease of Insertion/Deletion;
- Insertion at the beginning (and sometimes at the end if we use a tail pointer) is a constant time operation and takes O(1) time, as compared to arrays where inserting an element at the beginning takes O(n) time, where n in the number of elements in the array. 

## Drawbacks of Linked Lists:

-   To acces an element we have to traverse the list since **HEAD** or **TAIL**;
-   Extra memory space for a pointer is required with each element of the list;
-   Not cache-friendly. Since array elements are contiguous locations, there is the locality of reference which is not there in the case of linked lists;
-   It takes a lot of time in traversing and changing the pointers;
-   Reverse traversing is not possible in singly linked lists;
-   It will be confusing when we work with pointers;
-   Searching for an element is costly and requires O(n) time complexity;
-   Sorting of linked lists is very complex and costly;
-   Appending an element to a linked list is a costly operation, and takes O(n) time, where n is the number of elements in the linked list, as compared to arrays that take O(1) time.
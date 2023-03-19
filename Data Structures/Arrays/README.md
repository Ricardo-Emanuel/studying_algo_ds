# Data Structures

## Array

Array is a data structure that stores elements of same types, like an array of ints, 
an array of char, and so on. This data structures stores that at a contiguous space in 
memory, for the sake of curiosity, it's worth noting that a **python list** is an 
implementation of a dynamic array.

There are two types of array, **static** array and **dynamic** array. The **static** 
array has a constant size, in other words, we cannot change the size of a static 
array once it is initialized. However, dynamic arrays can be resized during the 
program's execution using a mechanism called dynamic memory allocation. This 
allows us to create new arrays on-the-fly and use them as needed. The basic 
flow is as follows:

- Initializa an array of size **N**;
- Add more elements in the array;
- Complete the memory allocated for this array;
- Initialize another array of size **2*N**;
- Copy the elements to the new array;
- Free the memorry allocated for the old array;
- And so on.

### Dynamic Array implementation

That is the implementation of a dynamic array in C:

```C
# include <stdio.h>
# include <stdlib.h>

int main(int argc, char *argv[]) {

    // Check the number of command line arguments
    if (argc < 2) {
        printf("Usage: %s <int>\n", argv[0]);
        return 1;
    }
    int size = atoi(argv[1]);

    // Step 1: Declare a pointer to hold the array
    int* d_array;

    // Step 2: Allocate memory for the array
    d_array = (int *) malloc(size * sizeof(int));

    if (d_array == NULL) {
        printf("%s\n", "Memory allocation failed!");
        return 1;
    }

    // Step 3: Use the array
    // Example of usage
    for (int i = 0; i < size; i++) {
        d_array[i] = i;
    }
    for (int i = 0; i < size; i++) {
        printf("%d ", d_array[i]);
    }

    // Step 4: Release the memory
    free(d_array);

    return 0;
}
```

In python, we have a built-in implementation of dynamic array, the **list** type:

```Python
import sys

def main(size: int):
     
    # Create a list of integer from 0 to size - 1
    d_array = [i for i in range(size)]

    # Displays the content of the array in one line
    print(*d_array) # 0 1 2 ...

if __name__ == "__main__":
    # Check the number of command line arguments
    if len(sys.argv) != 2:
        print("Usage: python script.py size")
        sys.exit(1)

    # Check if it is an integer
    try:
        size = int(sys.argv[1])
    except ValueError:
        print("You must type an integer!")
        sys.exit(1)

    main(size)
```

Now in Go, we could implement a dynamic array using a Go slice, which is a reference 
type that provides a convenient and efficient way to work with sequence of elements:

```Go
package main

import (
    "fmt"
    "os"
    "strconv"
)

func main() {

    // Check the number of command line arguments
    if len(os.Args) != 2 {
        fmt.Printf("Usage: %s <size>\n", os.Args[0])
        os.Exit(1)
    }

    // Convert the argument to an integer
    size, err := strconv.Atoi(os.Args[1])
    if err != nil {
        fmt.Println("Error: size must be an integer")
        os.Exit(1)
    }

    // Creates an array of integers for 5 elements
    d_array := make([]int, 0, size)

    d_array = append(d_array, 1, 2, 3, 4, 5)

    fmt.Println(d_array) // [1 2 3 4 5]
}
```
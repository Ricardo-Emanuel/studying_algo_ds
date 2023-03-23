# Estruturas de Dados
## Array

Array é uma estrutura de dados que armazena elementos do mesmo tipo, como um array de inteiros, um array de caracteres e assim por diante. Essa estrutura de dados armazena os elementos em um espaço contíguo na memória, por curiosidade, vale ressaltar que uma lista em Python é uma implementação de um array dinâmico.

Existem dois tipos de array, array estático e array dinâmico. O array estático tem um tamanho constante, ou seja, não podemos alterar o tamanho de um array estático após a inicialização. No entanto, arrays dinâmicos podem ser redimensionados durante a execução do programa usando um mecanismo chamado alocação dinâmica de memória. Isso nos permite criar novos arrays conforme necessário. O fluxo básico é o seguinte:

1. Inicializar um array de tamanho **N**;
2. Adicionar mais elementos no array;
3. Completar a memória alocada para este array;
4. Inicializar outro array de tamanho **2 * N**;
5. Copiar os elementos para o novo array;
6. Liberar a memória alocada para o array antigo;
7. E assim por diante.

Implementação de Array Dinâmico

Essa é a implementação de um array dinâmico em C:

```C
# include <stdio.h>
# include <stdlib.h>

int main(int argc, char *argv[]) {

    // Verifica o número de argumentos na linha de comando
    if (argc < 2) {
        printf("Usage: %s <int>\n", argv[0]);
        return 1;
    }
    int size = atoi(argv[1]);

    // Passo 1: Declarar um ponteiro para armazenar o array
    int* d_array;

    // Passo 2: Alocar memória para o array
    d_array = (int *) malloc(size * sizeof(int));

    if (d_array == NULL) {
        printf("%s\n", "Falha na alocação de memória!");
        return 1;
    }

    // Passo 3: Usar o array
    // Exemplo de uso
    for (int i = 0; i < size; i++) {
        d_array[i] = i;
    }
    for (int i = 0; i < size; i++) {
        printf("%d ", d_array[i]);
    }

    // Passo 4: Liberar a memória
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

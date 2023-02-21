# Estruturas de Dados
## Array

Array é uma estrutura de dados que armazena elementos do mesmo tipo, como um array de inteiros, um array de caracteres e assim por diante. Essa estrutura de dados armazena os elementos em um espaço contíguo na memória, por curiosidade, vale ressaltar que uma lista em Python é uma implementação de um array dinâmico.

Existem dois tipos de array, array estático e array dinâmico. O array estático tem um tamanho constante, ou seja, não podemos alterar o tamanho de um array estático após a inicialização. No entanto, arrays dinâmicos podem ser redimensionados durante a execução do programa usando um mecanismo chamado alocação dinâmica de memória. Isso nos permite criar novos arrays conforme necessário. O fluxo básico é o seguinte:

    Inicializar um array de tamanho N;
    Adicionar mais elementos no array;
    Completar a memória alocada para este array;
    Inicializar outro array de tamanho 2 * N;
    Copiar os elementos para o novo array;
    Liberar a memória alocada para o array antigo;
    E assim por diante.

Implementação de Array Dinâmico

Essa é a implementação de um array dinâmico em C:
# include <stdio.h>
# include <stdlib.h>
```C
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

ARRAY

1. Array é um Tipo de dado e uma estrutura de dados(a mais simples que tem que é a lista).

2. É uma estrutura de dados que guarda dados. Esses dados podem ser TODOS os tipos dados que o javascript trabalha(number, string, bool, null,  undefined, arrays, obj)

3. Sobre tipos de dados: muito importante; ex: qual tipo de dado eu vou usar para construir x coisa? ; 

4. Arrays e objs são estruturas que guardam os tipos dados acima mais eles mesmos.

   const arr = [1, 2, 3, 4, 5 ]

5. Arrays Ele permite que guardamos numa lista vários tipos dados diferentes. Ex: [3, 'banana', null, true]

6. Nosso interesse é usar o array como uma lista de elementos. A sua caracterisca principal é que ele é uma lista ordenada. Portanto, os elementos que estao no array estão sempre na mesma ordem e isso é muito importante. A gente modifica os elementos do array pasando o indice dos elementos que começa no indice zero. 

   Ex: constListaVariada = [3, 'banana', null, true]

   ​       //0  1              2        3

   console.log(listaVariada[1]) -> retorna 'banana'

7. Array pode guardar outros arrays também. Ex:

   const arr2d = [[1,2], [3,4], [5,6]]

   nesse array ele tem 3 elementos. cada elemento é um array também.

   como faz pra pegar somente o numero 4?

   `console.log(arr2d [1] [1])` -> retorna 4

8. Metodos e funções:

   `const valorDoInput = '33'`

   `const ValorNum = parseInt(valorDoInput)`

   parseInt: converte o tipo de dado ; por que isso funciona? isso só funciona porque essa funcao parseint foi criado por uma pessoa que disponibilizou pra gnt no javascript. Essa função, chamada de função nativa, funciona igual as funcoes que escrevemos. Portanto, é importante você saber: <u>Qual tipo de dado cada função JS funciona!</u>

Métodos: são funções que conseguimos utilizar em arrays;
O que fazer quando estou estudando/usando esses métodos de array:

- 1. Quais são ps parametros que a função precisa pra funcionar;
- 2. Qual é o retorno.

Sort: método inplace, ou seja, é um método que modifica o array original.
Slice: retorna uma cópia do array original.
Reverse: não retorna nada.
Reduce: reduz o que você passa para ele para um único valor.
    

    

OBJETO

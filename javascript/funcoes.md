# FUNÇÕES

https://curriculum.laboratoria.la/pt/topics/javascript/02-flow-control/03-functions

##### O que é uma função? 

Função nada mais é que uma máquina na qual você coloca coisas dentro e, a partir daí, essa máquina vai transformar essas coisas e depois vai cuspir algo.

A função nos permite executar a mesma peça de um código em vários lugares de um programa sem precisar copiar e colar código repeditamente. Exs.: `alert()`, `prompt()`, `console.log()`.	

obs: use nomes faceis de entender no seu código.

## Definindo uma função

A definição de uma função nada mais é que uma definição de uma variável, mas ao invés do valor dado a variável é uma função. 

- Exemplo de função usando sintaxe do tipo *keyword function*:

  `const square = function (num) {`

  `return num * num ;`

  `};`

- Exemplo da mesma função utilizando sintaxe do tipo *arrow function*:

  `const square = num => num * num`

  As funções são formadas por: *parâmetros* e *corpo*. No exemplo anterior, há apenas um parâmentro (num). O corpo contém as sequências que serão executadas. Os parametros servem para "transmitir" valores à função e assim mudar o seu comportamento de acordo com os valores oferecidos.

## Chamando uma função

Para rodar um código é necessário chamar uma função. Isso se faz escrevendo o nome da função seguido imediatamente de parênteses `()`. Os valores que se transmitem a função para usar como *parâmetros* são chamados de *argumentos*. Agregando ao exemplo anterior um chamado à função `square` transmitindo-lhe como argumento o valor `12` vemos que nos devolve `144` (ou seja, 12 ao quadrado).



`const square = function (num) {`

`return num * num ;`

`};`

`square (12);`

`//144`

## O valor de retorno

Assim como os argumentos são os valores de "entrada" (input) que utiliza uma função ao ser chamada, o valor de retorno é o valor de saída (output) que devolve a função (o `144` do exemplo anterior), e que pode ser utilizado em qualquer lugar do programa. Se uma função não especifica o valor de retorno, então a função retorna `undefined`.

O valor de retorno se especifica com o *keyword* `return`. No exemplo anterior, se especifica que o valor de retorno é o parâmetro multiplicado por si mesmo; isto é, o parâmetro ao quadrado. O keyword `return` sem uma expressão depois dele também fará com que a função devolva `undefined`.

Adicionemos uma outra sentença ao exemplo anterior na qual se utilize o valor de retorno da função `square`:

`const square = function (num) {`
  return num * num;
`};`

`console.log('El cuadrado de 12 es ' + square(12));`
`// → El cuadrado de 12 es 144`

Com esta mudança acontece o seguinte: o valor de retorno que se obtém ao chamar (ou invocar) a função `square` com o valor `12` de argumento é: `144`. Este se concatena com o texto `'O quadrado de 12 é '` para formar `'O quadrado de 12 é 144'`; o qual, por sua vez, se transmite como argumento à função `console.log` para que o imprima no painel de comando.

## Múltiplos parâmetros

Uma função pode ter vários parâmetros ou pode não ter nenhum. No seguinte exemplo, `makeNoise` não tem parâmetros, enquanto `power` tem dois:

`const makeNoise = function () {`
  console.log('Pling!');
`};`

`makeNoise();`
`// → Pling!`

`const power = function (base, exponent) {`
  let result = 1;
  for (let count = 0; count < exponent; count++) {
​    result *= base;
  }
  return result;
`};`

`console.log(power(2, 10));`
`// → 1024`

A seguir Daniel te explica mais sobre funções:

**Função sem efeito colateral:** função que não imprime, não grava no disco, não escreve nada em lugar nenhum, ela só  faz conta. Use o `console.log()` para imprimir algo na tela do console e, dessa forma, produzir um efeito colateral na função.

**Função:** é algo que transforma uma coisa em outra coisa. Então, aplicando na computação, toda vez que você quiser transformar uma coisa, você irá utilizar uma função.

Obs.: as duas sintaxes abaixo dão o mesmo resultado (não sei o porquê):

`function transformaAlgo(x) {`

`return 'gatinho' + x`

`}`

`console.log(transformaAlgo('feliz'));`

e

`const transformaAlgo = function (x) {`

`return 'gatinho' + x`

`}`

`console.log(transformaAlgo('feliz'))`

## Saindo de uma função com `return`

Quando o intérprete JavaScript observa um `return` dentro de uma função, imediatamente pula fora da função atual e passa o valor retornado ao código que a chamou. Isto é, qualquer sentença que coloquemos **depois** do `return` em uma função, **não** será executada.

Uma forma comum de utilizar `return` é para sair da função antecipadamente caso algum dos argumentos brindados não seja válido; isto é, se não forem o tipo de argumentos que a função necessita para funcionar corretamente. Por exemplo, a seguinte função devolve uma cadeia que indica o quinto caracter do seu nome. Se o nome transmitido à função tem menos de cinco caracteres, a função utiliza `return` para deixar a função imediatamente. Isto significa que a declaração de devolução ao final, que te diz a quinta letra do seu nome, nunca se executa.

`const fifthLetter = function (name) {`
 `if (name.length < 5) {`
 `return;`

 `}`
`return 'A quinta letra do seu nome é' + name[4] + '.';`
`};`

## Funções e controle de fluxo

A funções também afetam o controle de fluxo do nosso programa. Com funções podemos criar estruturas repetitivas (com algo que se chama `recursividade`) e estruturas condicionais (com, por exemplo, múltiplos valores de `return`). De fato, as funções são tão versáteis para armar a estrutura de um programa que existe todo um *paradigma de programação* baseado em funções. Isto é, existe uma maneira de pensar na programação que está baseada em funções. Isto se chama o **paradigma de programação funcional**. Mais adiante estudaremos com mais profundidade funções e o paradigma de programação funcional. Por enquanto, o importante é entender que as funções são uma forma de agrupar código para que possa ser reutilizado.

## Utilizando múltiplos `return` no lugar de `if... else`

Podemos usar vários `return` dentro de diferentes sentenças `if` no corpo de uma função para que a função devolva um valor diferente, dependendo do argumento oferecido. Por exemplo, digamos que você está escrevendo um jogo que dá medalhas aos jogadores conforme a sua pontuação. Uma pontuação menor a 3 é uma medalha de bronze, uma pontuação de 7 ou mais é ouro, e o que está no meio é prata. Você poderia utilizar uma função como `medalForScore` para avaliar uma pontuação e dar o tipo de medalha, como se mostra aqui:

`const medalForScore = function (score) {`
  `if (score < 3) {`
​    `return 'Bronze';`
  `}`
  `if (score < 7) {`
​    `return 'Silver';`
  `}`
  `return 'Gold';`
`};`

Embora estejamos comprovando múltiplas condições, não necessitamos usar sentenças `if ... else` encadeadas. Utilizamos as sentenças `if ... else` para garantir que somente uma das sentenças se execute. Quando cada uma das opções possui sua própria sentença de `return`, garantimos que se execute somente uma das opções --- porque, lembre-se, **as funções só podem devolver uma vez**.

##  
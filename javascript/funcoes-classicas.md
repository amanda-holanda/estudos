# Funções Clássicas

https://curriculum.laboratoria.la/pt/topics/javascript/02-flow-control/03-functions

## Declarando uma função

A declaração de uma função é simplesmente a declaração de uma variável comum na qual o valor dado a tal variável resulta ser uma função. Por exemplo, o código a seguir define a variável `square` para fazer referência à função que retorna o quadrado de um dado número:

`const square = function(x) {`
​    `return x * x;`
   };

  `console.log(square(12)); // 144`

Funções são valores que podem ser chamados (invocados). Uma maneira de definir uma função é chamada uma `function declaration` ou `declaração de função`. Por exemplo, o código a seguir define uma função `id` que possui `um parâmetro simples x:`

`function id(x) {`
  `return x;`
`};`

A instrução `return` retorna um valor da função `id`. Você pode chamar uma função por meio de seu nome, seguida de seus `argumentos` entre parênteses:

`id('hello'); // 'hello'`

Se nada é retornado pela função, `undefined` é retornado (implicitamente):

```
function f() { }
f(); //undefined

```

Esta seção mostrou somente uma maneira de definir e chamar uma função. Outras formas serão mostradas em breve.

## Os 3 papéis das funções em JavaScript

Uma vez definida uma função, ela pode realizar vários papéis:

### Nonmethod function (função normal)

Você pode chamar uma função diretamente como vimos até o momento. Aqui um exemplo de chamada:

```
id('hello');

```

Por convenção, os nomes destas funções *normais* começam com letra minúscula seguindo o estilo **lowerCamelCase**.

### Construtor

Você pode invocar uma função por meio do operador `new`. Ele é utilizado para criação de objetos. Aqui um exemplo de invocação:

```
new Date();

```

Por convenção, os nomes dos construtores começam com letra maiúscula, seguindo o estilo **UpperCamelCase**.

### Método

Você pode armazenar uma função em uma propriedade de um objeto, o que o converte em um *método*. Aqui um exemplo de como invocar um método definido em um objeto `obj`:

```
obj.method();

```

Por convenção, os nomes dos métodos seguem o estilo das funções normais (*lowerCamelCase*).

## Terminologia: "Parâmetro" vs. "Argumento"

Os termos `parâmetro` e `argumento` são frequentemente usados para se referirem à mesma coisa já que é possível entender ao que se referem. Contudo, a seguir mostramos uma regra para diferenciá-los.

- **Parâmetros** são utilizados para definir uma função: No exemplo a seguir, `param1` e `param2` são parâmetros:

  ```
  function foo(param1, param2) {
    // ...
  }

  ```

- **Argumentos** são utilizados para invocar uma função. No exemplo a seguir, `3` e `7` são argumentos:

  ```
  foo(3, 7);
  ```

## Criação de Funções

Nesta seção veremos 3 maneiras de criar uma função:

- Por meio de uma *function expression* (função como expressão).
- Por meio de uma *function declaration* (declaração de uma função).
- Por meio do construtor `Function()`.

Todas as funções são objetos, instâncias de `Function`:

```
function id(x) {
  return x;
}

console.log(id instanceof Function); // true

```

Para tal, as funções obtêm seus métodos de `Function.prototype`.

### Function Expressions

Uma *function expression* produz um valor - um objeto de função. Por exemplo:

```
const add = function(x, y) {
  return x + y;
};

console.log(add(2, 3)); // 5

```

O código anterior atribui o resultado de uma função como expressão para a variável `add` e pode ser chamada por meio desta variável. Neste tipo de função é possível atribuir uma função a uma variável, passar como parâmetros de outra função e outras coisas mais. Devido a este tipo de função não possuir um nome, podem ser chamadas de *anonymous function expressions* (funções anônimas).

#### Named Function Expressions

É possível nomear uma função como uma expressão. As *named function expressions* (funções que se expressam por nome) permitem à função fazer referências a si mesma. Vemos refletida sua utilidade quando desejamos aplicar recursividade. Por exemplo:

```
const factorial = function fact(number) {
  if (number <= 1) {
    return 1;
  }
  return number * fact(number - 1);
};

console.log(factorial(3)); // 6

```

**Nota:** Os nomes das funções como expressão com nome só são acessíveis dentro da função:

```
const repeat = function me(n, str) {
  return n > 0 ? str + me(n-1, str) : '';
};

console.log(repeat(3, 'Yeah')); // YeahYeahYeah
console.log(me); // ReferenceError: me is not defined
```

### Function Declarations

A seguir temos uma declaração de função:

```
function add(x, y) {
  return x + y;
}

```

O código anterior é parecido com o de uma função como expressão, mas é uma instrução. De certa maneira, é equivalente ao código a seguir:

```
const add = function(x, y) {
  return x + y;
};

```

Em outras palavras, uma *function declaration* consiste na palavra chave reservada *function*, uma lista de parâmetros para a função, delimitados por parênteses e vírgulas, e a sentença JavaScript que define a função, delimitada por chaves.

### Function Constructor (pouco utilizada)

O construtor `Function()` avalia código JavaScript armazenado em strings. Por exemplo, o código a seguir é equivalente aos dos exemplos anteriores:

```
const add = new Function('x', 'y', 'return x + y');

```

No entanto, esta maneira de definir uma função é lenta e deixa o código entre strings (ficam inacessíveis a ferramentas, por exemplo, de depuração com *Dev Tools*). Portanto é melhor utilizar *function expression* ou uma *function declaration* se for possível.

## Hoisting

**Hoisting** significa "elevar para o início do escopo". *Function declarations* são elevadas (*hoisted*) completamente, enquanto as declarações de variáveis só parcialmente.

*Function declarations* são completamente elevadas. Isso permite chamar uma função antes de sua declaração:

```
welcome(); // 'Welcome to Laboratoria'
function welcome() { // esta função é elevada - hoisting
  console.log('Welcome to Laboratoria');
}

```

A razão pela qual o código anterior funciona é que o motor de JavaScript move a declaração da função `welcome` para o início do escopo. Ele acaba executando como se estivesse escrito da seguinte maneira:

```
function welcome() { // esta função é elevada - hoisting
  console.log('Welcome to Laboratoria');
}
welcome(); // 'Welcome to Laboratoria'

```

As declarações de variáveis são elevadas também, mas somente as declarações mas não as atribuições. Portanto, definir uma função como expressão atribuindo a uma variável acaba em um erro no exemplo anterior:

```
welcome(); // TypeError: undefined is not a function
const welcome = function welcome() {
  console.log('Welcome to Laboratoria');
};

```

Somente as declarações são elevadas. O motor de JavaScript executa o código anterior como se estivesse escrito da seguinte maneira:

```
const welcome; // undefined
welcome(); // TypeError: undefined is not a function
welcome = function welcome() {
  console.log('Welcome to Laboratoria');
};
```
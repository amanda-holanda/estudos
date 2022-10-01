OFICINA GABS - 30.09.22

### Pixel:

Um **pixel** é a menor unidade que compõe uma imagem, seja de uma foto ou um frame (quadro) de um vídeo. Na fotografia, os **pixels** são pedacinhos pequenos que **servem** para formar a imagem.

### REM x EM:

#### Rem: 

Seu valor é definido pelo elemento raiz da tela. Tem relação com o valor que foi definido na raiz do html. Se, por exemplo, no html eu defino que font-size é 32px e lá no CSS eu configuro o font-size pra 2rem, a fonte que aparece terá o tamanho de 64px ( 2 x 32px). 

#### Em:

Pega a referencia de uma tag mãe. Quem define não é o root ( a tag mae do html) e sim um elemento mãe definido. Ex: temos uma div que foi setada com font-size de 20px e dentro dela tem um paragrafo que setei o font-size de 2em. Esse paragrafo terá 40px.

Obs.: gabriel nunca utilizou em. Não é uma unidade muito utilizável. Principalmente, pelo fato de sempre pegar como referencia o elemento com hierarquia acima.

Obs2.: Quando estamos falando de caixas, pixel não é a melhor alternativa. 

### Porcentagem

Tem que saber o valor inicial para saber qual é a porcentagem. Vai lado a lado com o tipo de display utilizado. A porcentagem é relativa ao elemento do seu elemento de hierarquia superior.

Dica: muito raramente definimos uma altura fixa para um elemento. Por que dai o conteudo tende a extrapolar pra fora da caixa. Isso não quer dizer que você não pode colocar uma altura minima, por exemplo.

Qual diferença de porcentagem pra vh e vw? Porcentagem tem como referência o elemento de hierarquia superior a ele. O VH e VW acontecem independente do elemento de hierarquia superior.

### VH (View-height) e VW (View-width)

Essas unidades de medidas acontecem independente do elemento de hierarquia superior. Utilize VH para altura e VW pra largura. Não é de bom tom utilizar VW para altura e vice-versa.

### RESPONSIVIDADE:

Tem que ter a tag viewport no html: 

<meta name="viewport" content="width=device-width, initial-scale=1.0">

Nem sempre a responsividade tem a ver com o media queries. Você pode adaptar. Ex: blog do gabs. 

### GRID  x DISPLAY FLEX

Você pode utilizar qualquer um dois. A utilização vai depender do que você deseja fazer. Gabs acha o grid mais complexo. Mas, por exemplo, se você quer construir um dashboard com vários "estilos de grade", o grid é mais utilizável. O display flex é mais usual para construir layouts menos complexos.

Site para estudo de grid: https://www.origamid.com/projetos/css-grid-layout-guia-completo/ .

### Como adiciona classe utilizando o "createElement()"

`<script>`
    `const elemento = document.createElement('div');`


```js
elemento.classList.add('minha-div-do-js');
```

`</script>`

<style>
    .minha-div-do-js {
        background: tomato;


    }

`</style>`


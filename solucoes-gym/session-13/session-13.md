### HTML/CSS

#### Beginner

- [CSS Cups and Balls](https://github.com/Laboratoria/SAP008-gym/blob/main/session-13/exercises/css-cups-and-balls/README.md): 
    `display: flex;`
    `justify-content: center;`
    `align-items: center;`
    `flex-wrap: wrap;`
   `} .container {`
    `width: 75%;`
    `display: flex;`
    `justify-content: space-evenly;`
    `align-items: center;`
   `} .first {`
    `margin-top: 80px;`
   `} .second {`
    `margin-bottom: 80px;`
   `}`
   `.green {`
    `background: #998235`

  `;`
   `} .yellow {`
    `background: #F3AC3C`

  `;`
   `} .circle {`
    `width: 50px;`
    `height: 50px;`
    `border-radius: 50%;`
   `} .half-circle {`
    `width: 50px;`
    `height: 50px;`
    `border-radius: 50px 50px 0 0;`
   `} .half-circle {`
    `width: 50px;`
    `height: 50px;`
    `border-radius: 50px 50px 0 0;`
   `}`
   `.back {`
    `border-radius: 0 0 50px 50px;`
   `}</style>`

  

- [CSS Smiley](https://github.com/Laboratoria/SAP008-gym/blob/main/session-13/exercises/css-smiley/README.md):

  `<section class="container">`
   `<div class="eyes"></div>`
   `<div class="eyes"></div>`
  `</section><section class="container-smile">`
   `<div class="eyes back"></div>`
  `</section><style>`
   `body {`
    `margin: 0;`
    `height: 100%;`
    `background: #6592CF`

  `;`
    `display: flex;`
    `justify-content: center;`
    `align-items: center;`
    `flex-wrap: wrap;`
   `} .container {`
    `display: flex;`
    `justify-content: center;`
    `align-items: center;`
    `width: 100%;`
    `gap: 80px;`
   `} .container-smile {`
    `width: 100%;`
    `display: flex;`
    `justify-content: center;`
    `align-items: center;`
    `margin-top: -100px;`
   `} .eyes {`
    `width: 80px;`
    `height: 80px;`
    `background: #6592CF`

  `;`
    `border-radius: 50%;`
    `border: 20px solid #060F55`

  `;`
    `border-bottom-color: #6592CF`

  `;`
    `border-left-color: #6592CF`

  `;`
    `transform: rotate(-45deg);`
   `} .back {`
    `transform: rotate(135deg);`
   `}`
  `</style>`

#### Intermediate

- [CSS Magical Tree](https://github.com/Laboratoria/SAP008-gym/blob/main/session-13/exercises/css-magical-tree/README.md):

  ```css
  <div class="big-square"></div>
  <div class="small-square"></div>
  <div class="line-center"></div>
  <div class="line-green"></div>
  
  <style>
    * {
      margin: 0;
      border: 0;
      padding: 0;
      box-sizing: border-box;
    }
    
    body {    
      height: 100%;
      background: #1A4341;    
      display: flex;
      justify-content: center;
      align-items: center;
    }
    
    .big-square {
      width: 270px;
      height: 270px;    
      border: 30px solid #F3AC3C;
      margin-bottom: 150px;
      position: absolute;
    }
  
    .small-square {
      width: 150px;
      height: 200px;    
      border: 30px solid #998235;
      margin-bottom: 200px;      
      position: absolute;
    }
  
    .line-center {
      width: 30px;
      height: 100%; 
      background: #F3AC3C;
      position: absolute;
    }
  
    .line-green {
      width: 270px;
      height: 30px;  
      background: #998235;  
      margin-top: 210px;        
    }
    
  </style>
  ```

- [CSS Blossom](https://github.com/Laboratoria/SAP008-gym/blob/main/session-13/exercises/css-blossom/README.md):

  ```css
  <section class="container">
    <div class="big-element blue"></div>
    <div class="small-element yellow"></div>  
  </section>
  <section class="container">
    <div class="small-element yellow right"></div>
    <div class="big-element blue right"></div>   
  </section>
  
  <style>
    body {
      margin: 0;
      background: #998235;
      height: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 20px;
      
    }
    .container {    
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      flex-wrap: wrap;    
      height: 100%;
      gap: 20px;    
    }
  
    .blue {
      background: #1A4341;
    }
  
    .yellow {
      background: #F3AC3C;
    }
    
    .big-element {
      width: 80px;
      height: 100px;    
      border-radius: 0 50px;
    }
  
    .small-element {
      width: 80px;
      height: 60px;    
      border-radius: 0 50px;
    }
  
    .right {
      border-radius: 50px 0;    
    }
    
  </style>
  ```

### JavaScript

#### Newbie

- [Front Again](https://github.com/Laboratoria/SAP008-gym/blob/main/session-13/exercises/front-again/README.md):

  `function frontAgain(str){`
    `const primeiraPosicao = str[0];`
    `const segundaPosicao = str[1];`
    `const ultimaPosicao = str[str.length-1];`
    `const penultimaPosicao = str[str.length-2];`
    `const tamanho = str.length;`

    `if(tamanho==0) {`
    `return false}   
    else if(primeiraPosicao == penultimaPosicao &`
       `segundaPosicao == ultimaPosicao) {`
    `return true}`
    `else {`
    `return false}   
  }`

- [MaxMod5](https://github.com/Laboratoria/SAP008-gym/blob/main/session-13/exercises/max-mod-5/README.md)

#### Beginner

- [Who's Online](https://github.com/Laboratoria/SAP008-gym/blob/main/session-13/exercises/who-is-online/README.md)

#### Intermediate

- [Convert Hash To An Array](https://github.com/Laboratoria/SAP008-gym/blob/main/session-13/exercises/convert-hash-to-an-array/README.md)
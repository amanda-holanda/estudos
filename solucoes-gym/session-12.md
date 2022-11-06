### HTML/CSS

#### Beginner

- [CSS Band Aid](https://github.com/Laboratoria/SAP008-gym/blob/main/session-12/exercises/css-band-aid/README.md)

  ```css
  <div class="orange"></div> 
  <div class="green"></div> 
  <div class="beje"></div> 
  <style> 
    body { 
      margin: 0px; 
      padding: 0px; 
      border: 0px; 
      height: 100%; 
      width: 100%; 
      box-sizing: border-box; 
      display: flex; 
      justify-content: center; 
      align-items: center; 
    } 
    .orange { 
      width: 50px; 
      height: 200px; 
      background: #A3A368; 
      transform: rotate(-135deg); 
      position: absolute;
    } 
    .beje {
      width: 50px; 
      height: 50px; 
      background: #FBE18C;
      transform: rotate(135deg);    
    }
    .green {
      width: 50px; 
      height: 200px; 
      background: #F3AC3C; 
      transform: rotate(135deg);
      position: absolute;
    }
  </style> 
  ```

#### Intermediate

- [CSS Eye of the Tiger](https://github.com/Laboratoria/SAP008-gym/blob/main/session-12/exercises/css-eye-of-the-tiger/README.md)

### JavaScript

#### Newbie

- [Disemvowel Trolls](https://github.com/Laboratoria/SAP008-gym/blob/main/session-12/exercises/disemvowel-trolls/README.md)

  ```javascript
  function disemvowel(str) {
    return str.replace(/[aeiou]/gi, '');
  }
  ```

- [Is this a triangle](https://github.com/Laboratoria/SAP008-gym/blob/main/session-12/exercises/is-this-a-triangle/README.md)

  ```javascript
  function isTriangle(a,b,c) {
    if( (a + b > c) & (a + c > b) & (b + c > a) ) {
      return true
    }
     return false;
  }
  ```

#### Beginner

- [sPoNgEbOb MeMe](https://github.com/Laboratoria/SAP008-gym/blob/main/session-12/exercises/spongebob-meme/README.md)
- [Star Lovers Warmup](https://github.com/Laboratoria/SAP008-gym/blob/main/session-12/exercises/star-lovers-warmup/README.md)

#### Intermediate

- [Star Lovers Challenge](https://github.com/Laboratoria/SAP008-gym/blob/main/session-12/exercises/star-lovers-challenge/README.md)
### HTML/CSS

#### Newbie

- [CSS Wash your hands](https://github.com/Laboratoria/SAP008-gym/blob/main/session-14/exercises/css-wash_your_hands/README.md):

  ```css
  <div class="rectangle">
    <div class="inside"></div>
  </div>
  <div class="back"></div>
  <style>
    body {
      margin: 0;
      border:0;
      padding: 0;
      box-sizing: border-box;
      background: #293462;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100%;
    }
    .rectangle {
      width: 200px;
      height: 100px;
      background: #FE5F55;
      border-radius: 20px;
      display: flex;
      justify-content: center;
      align-items: center;
      position: absolute;
      margin: 0 0 20px;
    }
    .inside {
      width: 140px;
      height: 40px;
      background: #A64942;    
      border-radius: 20px;
    }
    .back {
      width: 200px;
      height: 90px;
      background: #A64942; 
      border-radius: 20px;
      margin: 30px 0 0;
    }
  </style>
  ```

#### Beginner

- [CSS Ukulele](https://github.com/Laboratoria/SAP008-gym/blob/main/session-14/exercises/css-ukulele/README.md)

```css
<div class="circle">
  <div class="thing"></div>
</div>
<div class="circle small">
  <div class="circle smaller"></div>
</div>
<div class="rectangle"></div>
<div class="end">
  <div class="little"></div>
  <div class="little"></div>  
</div>
<style>
  body {
    margin: 0;
    padding: 0;
    border: 0;
    box-sizing: border-box;
    background: #F3AC3C;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
  }
  .circle {
    width: 120px;
    height: 120px;
    background: #998235;
    border-radius: 50%; 
    display: flex;
    justify-content: center;
    align-items: center;    
    margin: 0 50px 0 0;
  }
  .thing {
    width: 10px;
    height: 40px;    
    background: #1A4341;
    position: absolute;
    margin: 0 30px 0 0;
    border-radius: 10px;
  }
  .small {
    width: 100px;
    height: 100px;
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;    
    position: absolute;
    margin: 0 70px 0 0;    
  }
  .smaller {
    width: 40px;
    height: 40px;
    background: #1A4341;
    position: absolute;
    border: 5px solid #F3AC3C;
    margin: 0;
  }
  .rectangle {
    width: 140px;
    height: 20px;    
    background: #1A4341;  
    
  }
  .end {
    width: 40px;
    height: 30px;    
    background: #998235;  
    border-radius: 10px;
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    align-items: center;
    position: absolute;
    margin: 0 -270px 0 0;
  }
  .little {
    width: 18px;
    height: 4px;    
    background: #1A4341;
    border-radius: 10px;    
  }
</style>
```

### JavaScript

#### Beginner

- [Elevator Distance](https://github.com/Laboratoria/SAP008-gym/blob/main/session-14/exercises/elevator-distance/README.md)
- [Closest Elevator](https://github.com/Laboratoria/SAP008-gym/blob/main/session-14/exercises/closest-elevator/README.md)

#### Intermediate

- [Simple Elevator](https://github.com/Laboratoria/SAP008-gym/blob/main/session-14/exercises/simple-elevator/README.md)
- [Find Multiples](https://github.com/Laboratoria/SAP008-gym/blob/main/session-14/exercises/find-multiples/README.md)
- [Move All Balls to Each Box](https://github.com/Laboratoria/SAP008-gym/blob/main/session-14/exercises/move-balls-boxes/README.md)

#### Advanced

- [The Lift](https://github.com/Laboratoria/SAP008-gym/blob/main/session-14/exercises/the-lift/README.md)
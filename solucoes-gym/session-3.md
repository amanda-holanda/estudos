## Exercícios

### Newbie

- [**Icy-hot**](https://github.com/Laboratoria/SAP008-gym/blob/main/session-03/exercises/icy-hot/README.md):

  function icyHot(temp1, temp2){
    if(temp1 < 0 & temp2 > 100 || temp1>100 & temp2 < 0){
       return true;
       } else {
         return false;
    }
  }

- [**comboString**](https://github.com/Laboratoria/SAP008-gym/blob/main/session-03/exercises/combo-string/README.md)

function comboString(a, b){
  const tamanhoA = a.length;
  const tamanhoB = b.length;

  if(tamanhoA > tamanhoB) {
      return b + a + b;
    } else if(tamanhoB > tamanhoA) {
      return a + b + a;
      } 
}

- [**Reverse 3**](https://github.com/Laboratoria/SAP008-gym/blob/main/session-03/exercises/reverse3/README.md)

function reverse3(nums){  

  return [nums[2],nums[1],nums[0]]; 
    
}

ou

function reverse3(nums){  
  return nums.reverse();     
}

### Beginner

- [**Remove String Spaces**](https://github.com/Laboratoria/SAP008-gym/blob/main/session-03/exercises/remove-string-spaces/README.md)
- [**Same on both ends**](https://github.com/Laboratoria/SAP008-gym/blob/main/session-03/exercises/same-on-both-ends/README.md)
- [**Secret Society**](https://github.com/Laboratoria/SAP008-gym/blob/main/session-03/exercises/secret-society/README.md)
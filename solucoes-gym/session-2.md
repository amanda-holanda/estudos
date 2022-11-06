| Exercício                                                    | Dificuldade      | Tags        | OAs                      |
| ------------------------------------------------------------ | ---------------- | ----------- | ------------------------ |
| [**Sherlock syllogisms**](https://github.com/Laboratoria/SAP008-gym/blob/main/session-02/exercises/sherlock-syllogisms/README.md) | no-code          | `silogismo` | Pensamento computacional |
| [**The tour guide**](https://github.com/Laboratoria/SAP008-gym/blob/main/session-02/exercises/the-tour-guide/README.md) | no-code / newbie | `arrays`    | Pensamento computacional |
| [**Hello name**](https://github.com/Laboratoria/SAP008-gym/blob/main/session-02/exercises/hello-name/README.md) | newbie           | `strings`   | Manipulação de strings   |
| [**First last 6**](https://github.com/Laboratoria/SAP008-gym/blob/main/session-02/exercises/first-last-6/README.md) | newbie           | `arrays`    | Manipulação de arrays    |
| [**Return Something to Me**](https://github.com/Laboratoria/SAP008-gym/blob/main/session-02/exercises/return-something-warmup/README.md) | beginner         | `strings`   | Manipulação de strings   |

[**Hello name**](https://github.com/Laboratoria/SAP008-gym/blob/main/session-02/exercises/hello-name/README.md)

function helloName(name){
  return "Hello" + " " + name + "!";   
}

[**First last 6**](https://github.com/Laboratoria/SAP008-gym/blob/main/session-02/exercises/first-last-6/README.md):

function firstLast6(nums){
  const lastNumber = nums.length-1;
  const arrayLength = nums.length;

  if(arrayLength >= 1) {
    if(nums[0] == 6 || nums[lastNumber] == 6) {
     return true;
    } else {
     return false;
    }  

  } else {
    return false;
  } 

}

OU

function firstLast6(nums){
  const lastNumber = nums.length-1;  

  if(nums[0] == 6 || nums[lastNumber] == 6) {
     return true;
  } else {
     return false;
  }   
}

[**Return Something to Me**](https://github.com/Laboratoria/SAP008-gym/blob/main/session-02/exercises/return-something-warmup/README.md):

`function giveMeSomething(a) {`
	`return "something" + " " + a;`
`}`
# Git Colaborativo

## Basicamente, existem 2 formas de usar o git colaborativo:

- ### Primeira forma:


O github serve principalmente para projetos opensource. Isso significa que, por exemplo, qualquer pessoa pode xeretar tudo que tem dentro do código do facebook e fazer um clone do repositório remoto deles para seu repositório local. Nesse caso, se houver um bug no código do face, você pode clonar para sua maquina, ajeitar o bug, enviar um solicitação para os desenvolvedores do facebook  e, caso eles achem legal o seu código, eles podem aprová-lo e incorporá-lo no código do facebook. 

Ou seja, essa forma é mais "difícil", pois é necessário que alguém aprove o seu código antes de incorporá-lo ao código principal. Não iremos utilizar essa forma, por enquanto.

- ### Segunda forma:


A outra forma é quando, por exemplo, você trabalha num time dentro de uma empresa e, desse forma, todos do time trabalham juntos como colaboradores de um projeto. Quando você é colaborador você tem permissão de enviar seu código diretamente para o código do projeto principal, sem precisar que alguém autorize. Essa é a forma que iremos utilizar durante o projeto Data Lovers e explicar melhor a seguir.

## PASSO A PASSO:

### 1. Fork

Primeiramente, o colaborador (vou chamá-lo nessa explicação de <u>***colaboradora1***</u>) faz o fork do repositório. 

Obs: ao fazer o fork, fique atento se assinalou a caixinha de seleção que faz a cópia da *branch main*;

Obs2: preste atenção se, após fazer o fork, no canto superior esquerdo do seu repositorio no github aparece `seu-nick-name-do-github / nome-do-repositório-forkado` .

### 2. Git clone  

Copie a url do repositorio forkado > abra o terminal na pasta que você deseja clonar > rode o comando ` git clone 'url que você copiou'`. 

### 3. Adicionar colaboradora2  

Nesse passo, a **<u>*colaboradora1*</u>** irá adicionar sua dupla como sua colaboradora no projeto (nessa explicação vou chamá-la de **<u>*colaboradora2*</u>**). A <u>***colaboradora1***</u> deve:

Ir nas *settings* do seu repositório que foi forkado no github  > *collaborators* > adicionar a conta do github da sua *colaboradora2*. 

Atenção: a <u>colaboradora2</u> precisa aceitar o seu convite na conta do github dela (geralmente ela recebe um email pedindo que ela aceite a solicitação); 

Obs1: isso é feito para que a **<u>*colaboradora2*</u>** consiga mexer diretamente no código e, dessa forma, trabalhar juntamente com a **<u>*colaboradora1*</u>**. 

Obs2: é importante a <u>colaboradora2</u>  fazer o fork do repositório no final, após as duas terminarem todo o projeto, com o objetivo de ter no seu repositório remoto do github a cópia seu do trabalho.

### 4. Colaboradora2 faz o clone

Depois que a <u>***colaboradora2***</u> aceitar o convite, ela deve fazer o clone do repositório, seguindo o mesmo que a **<u>*colaboradora1*</u>** fez no passo 2 acima mencionado.

### 5. Colaboradora2 cria/muda de branch

O que é branch? Branch é uma ramificação/um ramo. Normalmente, o projeto tem um *ramo principal* (*branch main)* que é onde o código que está rodando em produção. No caso, quando você quer fazer alguma alteração nesse código, você pega essa parte que deseja alterar na *branch main,* separa em outra branch, faz o seu trabalho nessa nova branch e depois incorpora de volta na *branch main*. 

A **<u>*colaboradora2*</u>** deve fazer os seguintes passos para fazer a criação de sua nova branch:

a) Rode o seguinte comando no seu terminal: `git checkout -b 'nome da branch nova'` 

Esse comando cria uma nova branch, ao mesmo tempo que também muda para essa nova branch. 

Obs: esse comando é um atalho, pois ao mesmo tempo que cria uma branch nova, ele também muda para ela. Caso você não queira utilizar esse atalho, você também pode criar uma nova branch com o comando `git branch 'nome-da-sua-branch-nova'` e depois mudar para a branch nova com o comando `git checkout 'nome-da-sua-branch-nova'`.

### 6. Rode o comando: `Npm install`

As colaboradoras não devem esquecer de instalar o npm antes de começar a trabalhar no projeto.

### 7. Colaboradora2 faz o commit

Após o passo o 6, a *colaboradora2* já pode trabalhar na sua nova branch. Após fazer qualquer atualização no seu código, a <u>colaboradora2</u> deve fazer o commit rodando os três comandos principais:

 `git add . > commit - m "mensagem da atualizacao"> push origin 'nome-da-branch-nova'`

Obs1: até esse passo, essa branch nova não aparece no pc da <u>colaboradora1</u>, somente no github e no pc da <u>colaboradora2</u>. 

### 8. Colaboradora2 termina o seu trabalho na nova branch e faz o pull request

Obs: a <u>colaboradora2</u> deve fazer commit/push nessa nova branch até terminar todo o seu trabalho. Quando ele já estiver todo pronto ela deve fazer o seguinte:

8.1) `Pull request:` 

No repositório no github vá em *pull request*  > *open pull request* >  selecione nas caixinhas os repositorios 			corretos (pra onde vai e de onde vem) > escreva a mensagem com a atualização > clique em *pull request.*

Nesse passo, a *<u>colaboradora2</u>* está fazendo uma requisição para a *<u>colaboradora1</u>*, para que ela analise e aprove a sua atualização.

Obs: merge pull request: a <u>colaboradora2</u> pode mandar essa atualização diretamente para o repositório, pois ela tem permissão de colaboradora, mas o processo nao deve ser esse. Ela deve fazer como foi explicitado: enviar o request para a <u>colaboradora1</u> analisar, confirmar e aceitar.

### 9. Colaboradora1 aceita a requisição da colaboradora2

No seu repositório no github, a <u>*colaboradora1*</u> vai receber em *pull requests*, a requisição da <u>*colaboradora2*</u>, analisá-la e, após aceitá-la, clicar em *confirmar a merge* (nesse passo aqui ela pode escolher deletar a branch nova ou não). Após isso, o código que a <u>colaboradora2</u> criou foi adicionado na branch main. 

Obs: todo esse processo de branch nova é feito também pela <u>colaboradora1</u> quando ela está trabalhando no seu código. 

### 10. Colaboradora1 faz o `git pull`

Até aqui, no pc da <u>colaboradora1</u> não existe a atualizacao da branch nova e nem a da branch main. Para isso acontecer, a <u>colaboradora1</u> roda no seu terminal o comando `git pull`, que irá empurrar todas as atualizações do seu repositório remoto para o seu repositório local. Dessa forma, todo o código vai ser encorporado no repositorio local da <u>colaboradora1</u>.

​

​
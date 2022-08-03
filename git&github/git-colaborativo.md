## Basicamente, existem 2 formas:

1. O github serve principalmente para projetos opensource, ou seja, qualquer pessoa pode xeretar tudo que tem dentro do código do facebook, por exemplo, e você pode tambem fazer clone do react para maquina de vcs. Se tiver um bug, vc clona pra sua maquina, ajeita o bug, envia para os criadores do facebook (enviar a requisição para eles) e, se eles acharem legal, eles aprovam e incorporam lá no codigo do facebook. Essa é uma forma.


2. A outra forma é quando voce trabalha dentro de uma empresa. Você tem um time e dai todo mundo trabalha junto como colaborador de um projeto. Quando vc é colaborador vc tem permissao de enviar coisas diretamente para o código.

Então, a gnt vai trabalhar com a forma mais facil, a forma 2.

## PASSO A PASSO

1. **FORK:** Um colaborador (vou chamá-lo nessa explicação de <u>colaboradora1</u>) faz o fork do repositório. 

   Obs: nesse passo faz a copia da branch main;

   Obs2: preste atenção se no canto superior esquerdo do seu repositorio no github aparece `seunicknamedogithub / nome do repositório forkado` após fazer o fork).

2. **Git clone**:  Copia a url do repositorio forkado > abre o terminal na pasta que vc deseja clonar > roda o `comando git clone 'codigo copiado'`;  

3. **Adicionar colaboradora2:**  vai na settings do github > collaborators> adicione a conta do github da sua colaboradora2. 

   Atenção, esse passo isso não acontece automatico, a <u>colaboradora2</u> precisa aceitar o convite lá na conta do github dela. 

   Obs1: isso é feito para que a sua dupla consiga mexer diretamente no código do seu repositorio e, dessa forma, trabalhar juntamente com você. 

   Obs2: é importante a <u>colaboradora2</u>  fazer o fork do repositorio após terminar o projeto.

4. Depois que a <u>colaboradora2</u> aceitar o convite, ela faz o fork e o clone do repositorio na máquina dela.

5. `Npm install:` as colaboradas não devem esquecer de instalar o npm após o fork/clone.

6. **Colaboradora2 cria/muda de branch.** 

   Obs: O que é branch? é um ramo. Normalmente o projeto tem um ramo principal (main) que é o código que ta rodando em produção; quando voce vai fazer alguma alteração nesse código, voce pega essa parte na branch main, separa em outra branch, faz o trabalho e dps incorpora de volta na main. 

   a) `git checkout -b "nome da branch nova":` cria uma nova branch e muda para essa nova branch. Obs: vc pode criar uma nova branch com outro comando; esse comando do `checkout - b` é um atalho, pois ele ja cria uma nova  branch e já muda para ela.

   b) Após fazer alguma alteracao no código, a <u>colaboradora2</u> roda os comandos: `git add . > commit - m "mensagem da atualizacao"> push origin "'nome da branch nova"`

   Obs1: essa branch nova nao aparece no pc da <u>colaboradora1</u>, somente no github e no pc da <u>colaboradora2</u>. 

   Obs2: a <u>colaboradora2</u> vai fazendo commit/push nessa nova branch até terminar o trabalho que ela ta fazendo. Quando ele já tiver pronto ela faz o seguinte:

   a) `Pull request:` vai no github no repositorio tem *pull request*  > *open pull request* >  selecione nas caixinhas os repositorios corretos (pra onde vai e de onde vem) > escreva a mensagem com a atualização > clique em pull request.

   Obs: merge pull request: a <u>colaboradora2</u> pode mandar essa atualização diretamente  para o repositório, pois ela tem permissão de colaboradora, mas o processo nao é esse! Ela deve enviar o request para a <u>colaboradora1</u> analisar, confirmar e aceitar.

   b) A <u>colaboradora1</u> vai revisar o pull request da <u>colaboradora2</u>, analisar o que foi feito. Após ela aceitar, aperta pra confirmar a merge (nesse passo aqui ela pode deletar a branch nova ou não). Após isso, o código que a <u>colaboradora2</u> criou foi adicionado na branch main. 

   Obs: esse processo de branch nova é feito tambem pela <u>colaboradora1</u> quando ela está trabalhando no código. 

   c) Até aqui, no pc da <u>colaboradora1</u> não existe a atualizacao da branch nova e da branch main. Para isso acontecer, a <u>colaboradora1</u> faz o git pull. Dessa forma, todo o código vai ser encorporado no repositorio local da <u>colaboradora1</u>.
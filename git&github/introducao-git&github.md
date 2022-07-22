# Git & Github 

Oficina Laboratoria

## GIT:

- O git vai sincronizar aquilo que estamos trabalhando no nosso computador (Repositório Local) com o Github (Repositório Remoto) ;
- Obs: o git não trabalha da mesma forma que o Google Drive, ou seja, não sincroniza automaticamente. É necessário dar comandos para fazer essa sincronização.

### PASSOS PRINCIPAIS PARA INICIAR UM REPOSITÓRIO

1. **Iniciar um repositório git com o comando `git init` no seu terminal** 

   Obs: com esse comando, é criada uma pasta oculta chamada ".git" .

2. **Criar no Github um repositório** 

   Esse repositório gera uma "url" que deve ser copiada (vou chamá-la nesse exemplo  de https://github.com/amanda-holanda/resumos.git). 

   Obs: nesse momento o repositório local e o remoto ainda não estão conectados.

3. **Linkar o repositório local com o remoto**

    Use o comando `git remote add origin https://github.com/amanda-holanda/resumos.git` (adicione a sua url copiada). Esse comando significa que está adicionando esse link com o repositório remoto.

4. **Sincronizar o local com o remoto** 

   <u>*Explicação:*</u> imagine que você precise encaixotar o seu código, como se ele fosse uma encomenda. Primeiro, você encaixota, depois você endereça (coloca uma etiqueta, etc) e depois você vai no correio e envia a encomenda. Esses são os três comandos principais: encaixotar o código (`git add .`) , etiquetar  o código (`git commit -m "atualizacao"`) e enviar o código encaixotado para o repositório remoto  (`git push origin master`). 

   Nesse passo você utiliza os três comando principais do git (por enquanto):

   4.1. `git add .` 

   Esse "." significa aqui, ou seja, tudo que está na pasta. Obs.:  esse comando não adiciona pastas vazias, ou seja, é necessário que tenha conteúdo dentro das pastas.

   4.2. `git commit -m "mensagem identificando a atualização que você fez no seu código"`

   Obs: coloque na mensagem do commit exatamente o que você fez. Não utilize mensagens genéricas, como por exemplo, "atualização". Além de não ser uma boa prática, você se perde depois e não lembra exatamente o que você fez nessa atualização.

   4.3. `git push origin master` 

   Caso você estiver utilizando a branch `main`, substitua o comando `master` por `main`.

   Obs. 1 : use o comando `git status` para saber como a sua "caixa" está (untracked, modified, unmodified, etc);

   Obs.2:  Quando você faz "fork + clone" não precisa utilizar o comando `git init` , pois a pasta `.git` já foi configurada. Logo, você só precisa dar os três comandos principais citados acima (`git add .` , `git commit -m "mensagem identificando a atualização que você fez no seu código"`, `git push origin master`)

   ### Sobre Branchs (galhos/ramos/ramificações):

   São ramificações que geralmente são utilizadas quando você está trabalhando com outras pessoas. 

   Obs: `main`e `master` são a mesma coisa.

   ### Sobre VSCode:

   Ele avisa na função *"changes"* o que foi alterado desde o último *"commit"*. O *"commit"* pode ser feito através dessa função também. 

   Obs: sobre as letras que aparecem ao lado dos arquivos (U, M, etc):

   *U:* significa "untracked". O git ainda não sabe ainda que ele existe, ou seja, não foi "trackeado/rastreado";

   *M:* significa "modified".

   #### MUITO IMPORTANTE: Sempre se certifique, antes de rodar qualquer comando, que você está na pasta na qual está trabalhando.

###### 


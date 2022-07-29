# Dicas de terminal

## 1. O tab é o seu melhor amigo

Quando você estiver navegando pelas pastas do terminal, você não precisa saber exatamente o nome dos arquivos e pastas dentro dele. Por exemplo, se você estiver numa pasta que tem os arquivos `arquivo.js`  e `index.js` , você pode fazer:

```
cd [TAB]
```

Com isso o terminal vai sugerir opções com base no conteúdo da pasta. Ele tambem serve pra auto completar suas escolhas. Assumindo a mesma pasta do exemplo anterior:

```
cd i[TAB]
```

vai auto completar para `cd index.js` , já que `index.js` é o único arquivo na pasta que começa com a letra `i` . Caso existisse mais de 1, o terminal sugeriria apenas os que começam com `i`.

## 2. Meu deus do céu que pasta que eu tô?

As vezes o terminal não te mostra o caminho inteiro da pasta que você tá e vc precisa dele pra alguma coisa (abrir no windows explorer, por exemplo):

```
pwd
```

pwd significa `print work directory` que em português significa = q pasta q eu to?

## 3. Eu tava numa pasta, naveguei pra outra e não lembro onde tava, só queria voltar

Suponha que você esteja nessa pasta: `/home/guilherme/desenvolvimento/laboratoria/cipher/src/`
Aí você precisa ver alguma coisa da chave ssh e navega pra pasta `/home/guilherme/.ssh`Suas opções pra voltar pra pasta anterior são:

- `cd /home/guilherme/desenvolvimento/laboratoria/cipher/src/`
- usar seu amigo tab `cd /h[TAB]/g[TAB]/d[TAB]/l[TAB]/c[TAB]/s[TAB]/`
- ser hacker e usar o `cd -`

`cd -` diz pro terminal que vc quer voltar pra pasta de onde veio, não importa qual era a pasta4 - `cd -` , o retornoA mesma lógica do `cd -` se aplica às branches do git. Você pode voltar pra uma branch específica usando `git checkout -`. A partir da main, você cria uma nova branch: `git checkout -b nova-branch` . Nesse momento você muda para a branch `nova-branch`. Para voltar para a branch `main` , você tem duas opções:

- `git checkout nova-branch`
- `git checkout -`
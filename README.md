# SRF
SRF - (Simple Rip Files)

Perfeito para remoção em massa de arquivos thumbnails ou duplicados de qualquer extensão.

### Python 3.6

## Uso no servidor Linux ou sistemas baseados em Unix.

> 1. Para iniciar a aplicação execute o comando abaixo:

`python main.py`

> 2. Após essa mensagem cole a pasta onde está os thumbnails que deseja excluir.

`Navegue para o diretório onde deseja executar a limpeza:`

> 3. O programa vai mostrar na cor verde o diretório atual onde você está.

*Diretório atual: /home/user/pictures/thumbnails*

> 4. O último passo é definir os caracteres que vão filtrar os arquivos que devem ser eliminados, por exemplo, suponhamos que queira remover os thumbnails de uma pasta qualquer, então digite: `*x*.jpg` (arquivo_qualquer350x480.jpg) ou `*x*.png` e entre outros.

Obs: *Ainda não foi testado a entrada de mais de um parâmetro, faça o teste. Futuramente essa função pode ser implementada pelo mantenedor 
ou por algum desenvolvedor.*

> 5. Aperte ENTER e verá no console todos os arquivos que foram removidos.

## Uso no Windows.

1. Clique no botão *Buscar* e selecione a pasta onde estão os arquivos no qual deseja excluir.
2. Informe os caracteres que vão filtrar os arquivos como informado no passo 4 da doc para Linux.
3. Clique no botão *RIP* e se estiver com a pasta selecionada (onde estão os arquivos indesejados)
expandida verá eles sumirem repentinamente


## Sobre
Este pequeno software foi desenvolvido para sanar o problema de acumulo de thumbnails gerado por um plugin do Wordpress, uma solução rápida para limpar a quantidade de arquivos no servidor.

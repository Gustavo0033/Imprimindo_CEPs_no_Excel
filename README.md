Olá!
Esse projeto foi feito para desenolvimento pessoal.

Você pode usá-lo para automtizar algum processo. Podendo apenas colocar os CEPs que deseja pesquisar e deixar o programar rodar e trazer todos os dados que você precisa.
Neste programa, ele traz os dados básico que precisamos, são eles: Endereço, número, bairro e cidade.

Lembre-se que quando for usar, você deve salvar os CEPs na aba 'Cep', pode colocar quantos quiser!
Não esqueça de criar o seu próprio caminho para ele encontrar na hora que for pesquisar os CEPs.

------------------- DETALHES IMPORTANTES! -------------------------------------

USUÁRIOS DE MAC: não precisa alterar nada, pois foi desenvolvido em um macbook também.

USUÁRIOS DE WINDOWS:
Você que deseja testar no Windows, deve fazer as seguintes alterações:

Lá na parte superior do código, você encontrará:
"import subrprocess"
você deve alterar para:
"import os"

Descendo mais o código, na parte que abrimos o arquivo, você encontrará:

#abre o arquivo
"subprocess.run(['open', nomeArquivo])"

Altere esse trecho do código para:

os.startfile(nomeArquivo)



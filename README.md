# progweb2021.2Eduardo-e-Thiago
Repositório para o trabalho de programação para web 

Participantes:

Eduardo Junqueira Wichrowski - 1710329
Thiago Avidos Valle Pereira - 1611116


Set-up do Servidor:
1. Colocar todos os documentos, servidor, configurações e os arquivos, na mesma pasta.
2. executar o servidor com “python3 server.py”
3. Acessar pela web pelo localhost, a porta default é 8080.


O que funcionou:
        O Servidor consegue corretamente receber o pedido de GET, ele atende aos tipos [html,js,jpg,png,gif]. 
Ele retorna exibindo na tela o conteúdo pedido pelo GET. 
O caminho default pega na pasta onde está o próprio servidor, portanto se o documento estiver na pasta a chamada deve ser “/documento.tipo”. 
Se o documento estiver dentro de uma pasta precisa incluir o path junto como em “/pasta/documento.tipo”.
Para os documentos default eles devem estar na pasta do servidor estipulado na config. A lista dos documentos default também está na config
Para o caso do 404 ele ignora os parâmetros passados e usa o path da config e aponta para um arquivo “notfound.html” por padrão, mas caso queira mudar só trocar na variável NOTFOUND.
Conseguimos carregar mais de uma página ao mesmo tempo, o código tem um pequeno delay para atender, mas ele funciona para múltiplos clientes, testamos com até 5, às vezes dá uma engasgada, mas funciona.






Bugs e soluções:
Um bug que encontramos, mas não identificamos a causa, às vezes quando você abre mais de um acesso, depois de processar os acessos corretamente, uma tentativa de acesso que não envia nada para o servidor acontece, para corrigir fizemos com que mensagens vazias fossem ignoradas e marcadas com “Tentativa de acesso não identificado”.
Às vezes o servidor não fecha apropriadamente e é preciso encerrar o processo manualmente.
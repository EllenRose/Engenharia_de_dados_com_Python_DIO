# Desafio Prático : Otimizando o Sistema Bancário com funções Python

Esse desafio foi realizado durante a trajetória do bootcamp de Engenharia de dados com Python da **DIO** em parceria com a **NTT DATA.**

O Objetivo foi reestruturar o sistema bancário que fizemos anteriormente, adicionando as seguintes operações: **depósito** , **saque** e **extrato** dentro de funções e  a criação de duas novas funções: **criar usuário** e **criar conta corrente.**

**-Depósito**: Somente valores positivos, os depósitos deveriam ser armazenados em uma variável e exibidas no extrato,a função depósito deveria receber apenas argumentos por posição **(positional only)**.
- Sugestões de argumentos: **saldo**,**valor**,**extrato**,
- Sugestões de retorno: **saldo e extrato**.

**-Saque**: Permissão de apenas **3** saques diários , com limite de **R$500.00** por saque , caso o usuário não tivesse saldo em conta , seria exibida uma mensagem informando que não foi possível o saque e o motivo ,assim como o depósito todos os saques deveriam ser armazenados em uma variável e exibidas no extrato, a função deveria receber argumentos apenas por nome **(keyword only).**
- Sugestão de Argumentos: **saldo**,**valor**,**extrato**,**limite**,**numero_saques**,**limite_saques** , 
- Sugestão de Retorno: **saldo** e **extrato**

**-Extrato**: Nessa operação a regra seria que todos os depósitos e saques deveriam ser listados e no fim da listagem exibir o saldo atual da conta. a função extrato deveria receber argumentos por posição e nome **(positional only e keyword only)**.
- Sendo posicionais: **saldo**,
- Argumentos nomeados: **extrato.**

Os valores deveriam estar no formato **R$ xxx.xx**, exemplo : **400.50** ficaria **R$450.50**.

### Novas Funções
-**Criar Usuário**:
-  Armazenamento dos usuários em uma **lista**,
-  Um usuário é composto por :**nome,data de nascimento,cpf e endereço**, sendo que endereço é uma **string** com o formato:**logradouro,nro -bairro - cidade/sigla estado;**
- Armazenamento apenas dos números do CPF, **não podendo cadastrar dois usuários com o mesmo CPF.**

-**Criar Conta Corrente**:

- Armazenamento das contas em uma **lista**,
- Uma conta é composta por : **agência,número da conta e usuário**;
- Número da conta sequencial , sendo iniciada em **1**;
- Número da agência fixo **"0001"**;
- **Obs:** O Usuário poderia ter mais de uma conta ,porém uma conta pertence a apenas um usúario.


-**Dica**: Dica que foi dada pelo mentor no início do desafio: Para vinculação de um usuário a uma conta , filtrar a lista de usuários buscando o número do CPF informado para cada usuário da lista. 

**Entrega**: Após a elaboração do meu desafio , criei um repositório no meu git hub e dentro dele estão todos os desafios propostos pela plataforma.

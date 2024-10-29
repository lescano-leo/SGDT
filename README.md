# SGDT
Projeto: Sistema de Gerenciamento Distribuído de Tarefas

# Sistema de Gerenciamento Distribuído de Tarefas com Pyro4

## Objetivo

Criar um sistema distribuído onde clientes podem enviar tarefas (ex.: cálculos, processamento de dados) para servidores remotos, que as executam e retornam os resultados. O sistema deve permitir escalabilidade (vários servidores) e tolerância a falhas (clientes podem reconectar se um servidor falhar). Esta implementação é simples, mas demonstra o poder do Pyro4 para criar sistemas distribuídos e escaláveis em Python.

[Download do Pyro4](https://pypi.org/project/Pyro4/)

## Funcionalidades principais

### 1. Servidores distribuídos
- Cada servidor Pyro4 pode receber uma ou mais tarefas para processar.
- Os servidores podem ser adicionados ou removidos dinamicamente, sem afetar a operação do sistema. *(opcional)*

### 2. Cliente que distribui tarefas
- Os clientes podem se conectar ao servidor Pyro4 e enviar tarefas de forma assíncrona.
- As tarefas podem incluir cálculos pesados, como multiplicação de matrizes, ordenação de grandes volumes de dados, ou qualquer outro tipo de processamento. *(Escolha um tipo de cálculo e implemente uma função correspondente)*

### 3. Balanceamento de carga básico
- O sistema deve distribuir as tarefas entre múltiplos servidores de forma equilibrada (ex.: round-robin simples ou com base na carga dos servidores).

### 4. Resiliência
- Se um servidor falhar durante o processamento de uma tarefa, o cliente redirecionará a tarefa para outro servidor.
- O uso do Name Server do Pyro4 permite que o cliente encontre novos servidores automaticamente.

### 5. Segurança *(opcional)*
- Implementar autenticação e comunicação criptografada para proteger as chamadas remotas.

## Estrutura Básica do Projeto

### 1. Servidor Pyro4 (Worker)
- Cada servidor implementa uma classe Pyro4 que pode receber tarefas, executá-las e retornar os resultados.
- Exemplos de tarefa: cálculo do fatorial de um número, ordenação de uma lista ou simulação de um processo.

### 2. Cliente Pyro4
- O cliente se conecta ao servidor via o Name Server e envia uma ou mais tarefas para processamento.
- Ele pode distribuir as tarefas entre vários servidores e receber os resultados.

### 3. Balanceamento de Carga Simples
- Para balancear as tarefas entre vários servidores, registre múltiplos servidores no Name Server e use um loop round-robin ou selecione o servidor menos carregado.

### 4. Resiliência
- Em caso de falha de um servidor, o cliente tentará reenviar a tarefa para outro servidor. Use blocos try-except para capturar exceções e direcionar a tarefa para outro servidor.

## Testes e Cenários

1. **Cenário 1**: Um único cliente envia várias tarefas (cálculos) para um servidor.
2. **Cenário 2**: Múltiplos servidores são adicionados, e o cliente distribui as tarefas entre eles.
3. **Cenário 3**: Um servidor falha, mas o sistema continua funcionando, e o cliente redireciona a tarefa para outro servidor.
4. **Cenário opcional**: Habilite segurança (autenticação e criptografia) para as chamadas RPC usando os recursos de segurança do Pyro4.

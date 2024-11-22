
CRUD Flask - Gerenciamento de Missões Espaciais

## Índice de Conteúdo
1. Introdução
2. Tecnologias
3. Instalação
4. Como Rodar o Projeto
5. Escopo de Funcionalidades
6. Exemplo de Uso
7. Status do Projeto
8. Contribuindo
9. Referências

## Introdução

Este projeto é um sistema CRUD (Create, Read, Update, Delete) para gerenciar missões espaciais, desenvolvido com Flask e Flask-SQLAlchemy. Ele permite que usuários registrem e acompanhem missões espaciais com dados como nome da missão, data de lançamento, destino, status e muito mais. Este projeto foi criado como um exemplo prático de como implementar um sistema CRUD em Flask. 
## Tecnologias
Ele utiliza as seguintes tecnologias: **Python** como linguagem de programação principal, **Flask** como framework para desenvolvimento de aplicações web, **Flask-SQLAlchemy** para integração com bancos de dados SQL, **SQLite** como banco de dados embutido para armazenamento local, e **HTML/CSS** para a criação da interface do usuário.

## Instalação

Para instalar o projeto em seu ambiente local, siga as instruções abaixo.

### Clone este repositório

git clone https://github.com/JoaoGui1430/CRUD_flask.git

## Como rodar o projeto

Acesse a pasta do projeto no terminal/cmd

cd CRUD_flask

Crie e ative um ambiente virtual (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`

Instale as dependências
pip install -r requirements.txt

Execute a aplicação

python app.py

O servidor inciará na porta 5000 - acesse http://127.0.0.1:5000 # Se não funcionar utilize: flask run --port=5001(ou outra porta de sua vontade)


### Escopo de Funcionalidades
A aplicação oferece as funcionalidades de:

Listar missões (visualização de todas as missões cadastradas)

Criar uma nova missão (adicionar uma nova entrada ao banco de dados)

Ler informações detalhadas de uma missão específica

Atualizar informações de uma missão existente

Deletar uma missão

Cada missão possui os seguintes atributos: id, nome_missao, data_lancamento, destino, estado, tripulacao, carga_util, duracao, custo e status_missao.

## Exemplo de Uso
Para cadastrar uma nova missão, navegue até a página de criação de missões, preencha o formulário com os detalhes necessários e envie o formulário. A nova missão aparecerá na lista de missões cadastradas.

## Status do Projeto
O status do projeto é ativo e funcional, com todos os endpoints CRUD implementados. Melhorias e novas funcionalidades estão sendo consideradas para versões futuras.


## Referências
Consulte a documentação oficial do Flask e Flask-SQLAlchemy para mais informações sobre as tecnologias utilizadas. O projeto segue uma estrutura padrão de aplicações Flask e é open-source, permitindo modificações e distribuição livre.







# Fiap Challenge

## Descrição do Projeto

Este projeto é uma aplicação de web scraping desenvolvida para coletar dados de uma ou mais fontes da web. O objetivo é extrair informações relevantes e armazená-las em um banco de dados SQLite para posterior análise.

## Estrutura do Projeto

- **webscraping/**: Contém os scripts e módulos responsáveis pela coleta de dados da web.
- **models.py**: Define os modelos de dados utilizados na aplicação.
- **schemas.py**: Contém as definições de validação de dados.
- **database.sqlite3**: O banco de dados SQLite que armazena os dados coletados.
- **main.py**: O ponto de entrada da aplicação, onde a lógica principal é executada.
- **database.py**: Contém funções para interagir com o banco de dados.
- **requirements.txt**: Lista as dependências necessárias para o projeto.
- **Pipfile**: Gerencia as dependências e o ambiente virtual.
- **Pipfile.lock**: Bloqueia as versões das dependências para garantir instalações consistentes.
- **README.md**: Este arquivo, que fornece uma visão geral do projeto.

## Instalação

Para instalar e configurar o projeto, siga os passos abaixo:

1. Clone o repositório:
   ```bash
   git clone https://github.com/danielcperalba/fiap-tech-challenge
   cd fiap-challenge
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate  # Para Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

Para executar a aplicação, utilize o seguinte comando:
```bash
python main.py
```

Certifique-se de que o banco de dados `database.sqlite3` está configurado corretamente e que as fontes da web estão acessíveis.


## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.

# PDFTableExtractor

Este projeto é uma ferramenta Python que extrai tabelas de arquivos PDF e as converte em arquivos Excel (.xlsx). Utiliza o `llama_parse` para processar e extrair tabelas do PDF e a biblioteca `pandas` para a conversão e manipulação dos dados.

## Funcionalidades

- **Extração de Tabelas de PDFs**: Utiliza o `llama_parse` para processar arquivos PDF e extrair tabelas, que são salvas em formato Markdown.
- **Conversão de Markdown para Excel**: Converte as tabelas formatadas em Markdown para arquivos Excel (.xlsx), facilitando a análise e a manipulação dos dados.

## Tecnologias

- **Python**: Linguagem de programação utilizada.
- **pandas**: Biblioteca para manipulação e análise de dados.
- **llama_parse**: Ferramenta para extração de tabelas de PDFs e conversão para formato Markdown.
- **Regex**: Usado para identificar e formatar as tabelas no Markdown.

## Arquivos

- `main.py`: Script para extrair tabelas de um PDF e salvar como arquivos Markdown.
- `transformar_excel.py`: Script para converter arquivos Markdown em arquivos Excel.

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd SEU_REPOSITORIO
    ```

3. Crie e ative um ambiente virtual:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # No Windows use: .venv\Scripts\activate
    ```

4. Instale as dependências:

    ```bash
    pip install pandas python-dotenv llama_parse
    ```

5. Crie um arquivo `.env` na raiz do projeto e adicione sua chave de API do `llama_parse`:

    ```plaintext
    LLAMA_CLOUD_API_KEY=YOUR_API_KEY
    ```

## Uso

1. **Extrair Tabelas do PDF:**

   Execute o `main.py` para extrair tabelas do PDF e salvá-las como arquivos Markdown:

    ```bash
    python main.py
    ```

   - O script usa a API do `llama_parse` para processar o PDF `resultado.pdf` e salva as tabelas extraídas na pasta `meu_pdf` como arquivos Markdown.

2. **Converter Markdown para Excel:**

   Execute o `transformar_excel.py` para converter os arquivos Markdown extraídos em arquivos Excel:

    ```bash
    python transformar_excel.py
    ```

   - O script lê os arquivos Markdown da pasta `meu_pdf`, converte as tabelas para o formato Excel e salva na pasta `tabelas`.

## Estrutura do Projeto

- `main.py`: Script responsável pela extração de tabelas do PDF e salvamento em Markdown.
- `transformar_excel.py`: Script para conversão dos arquivos Markdown em Excel.
- `.env`: Arquivo de configuração para a chave da API do `llama_parse`.
- `meu_pdf/`: Pasta onde os arquivos Markdown extraídos são armazenados.
- `tabelas/`: Pasta onde os arquivos Excel convertidos são armazenados.


## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

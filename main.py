import os
from dotenv import load_dotenv
from llama_parse import LlamaParse

load_dotenv()

# Acessa a chave de API
api_key = os.getenv('LLAMA_CLOUD_API_KEY')

# Cria o objeto LlamaParse com a instrução de parsing como string
documentos = LlamaParse(
    result_type="markdown",
    parsing_instruction="""
        this file contains text and tables, I'd like to get only the tables from the text.
    """
).load_data("resultado.pdf")

# Salva as páginas extraídas em arquivos markdown
for i, pagina in enumerate(documentos):
    with open(f'meu_pdf/pagina{i+1}.md', 'w', encoding='utf-8') as arquivo:
        arquivo.write(pagina.text)

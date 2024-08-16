import re
import pandas as pd
from io import StringIO
import os

def tratar_tabelas_texto(texto):
    # Compila a expressão regular para buscar tabelas em markdown
    regra_busca_regex = re.compile(r'(\|.*\|\n(\|[-:| ]+\|)(?:\n\|.*\|)+)', re.MULTILINE)
    tabelas = regra_busca_regex.findall(texto)
    return tabelas

def transformar_markdown_excel(texto, num_pagina):
    # Identificar as tabelas que estão no texto
    lista_texto_tabelas = tratar_tabelas_texto(texto)
    if len(lista_texto_tabelas) > 0:
        for i, texto_tabela in enumerate(lista_texto_tabelas):
            # Ajusta o texto da tabela para formatar corretamente
            texto_tabela = texto_tabela.strip()  # Remove espaços em branco extras
            tabela = pd.read_csv(StringIO(texto_tabela), sep='|', encoding='utf-8', engine='python', skipinitialspace=True, skipfooter=0)
            tabela = tabela.dropna(how='all', axis=1)  # Remove colunas vazias
            tabela = tabela.dropna(how='all', axis=0)  # Remove linhas vazias
            
            # Salvar a tabela em um arquivo Excel
            tabela.to_excel(f"tabelas/{nome_arquivo}_Tabela{i+1}.xlsx", index=False)


# Leitura do arquivo markdown
pasta_paginas = 'meu_pdf'
lista_documentos = os.listdir(pasta_paginas)

for i, documento in enumerate(lista_documentos):
    with open(f'{pasta_paginas}/{documento}', 'r', encoding='utf-8') as arquivo:
        texto = arquivo.read()

    # Extrair o nome do arquivo sem a extensão
    nome_arquivo = os.path.splitext(documento)[0]
    transformar_markdown_excel(texto, nome_arquivo)

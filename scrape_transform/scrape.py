import os
import requests
from bs4 import BeautifulSoup
import zipfile
import pandas as pd


URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
DIRETORIO = "arquivos"
SEU_NOME = "Teste_Ivan_Martins"  


os.makedirs(DIRETORIO, exist_ok=True)

def baixar_anexos():
    print("Acessando o site...")
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    anexos = []
    for link in soup.find_all('a'):
        texto = link.text.strip().lower()
        if 'anexo i' in texto:
            anexos.append(('Anexo_I.pdf', link['href']))
        elif 'anexo ii' in texto:
            anexos.append(('Anexo_II.pdf', link['href']))
    
    print("Baixando arquivos...")
    for nome, url in anexos:
        resposta = requests.get(url)
        with open(os.path.join(DIRETORIO, nome), 'wb') as f:
            f.write(resposta.content)
    
    # Compactar arquivos
    with zipfile.ZipFile(os.path.join(DIRETORIO, 'Anexos.zip'), 'w') as zipf:
        for arquivo in os.listdir(DIRETORIO):
            if arquivo.endswith('.pdf'):
                zipf.write(os.path.join(DIRETORIO, arquivo), arquivo)
    
if __name__ == "__main__":
    baixar_anexos()
    print("Arquivos baixados e compactados com sucesso!")                
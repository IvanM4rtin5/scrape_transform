import os
import tabula
import zipfile
import pandas as pd

DIRETORIO = "arquivos"
SEU_NOME = "Teste_Ivan_Martins"

def processar_dados():
    print("Processando Anexo I...")
    
    try:
        dfs = tabula.read_pdf(
            os.path.join(DIRETORIO, 'Anexo_I.pdf'),
            pages='all',
            lattice=True,
            multiple_tables=True
        )
    except Exception as e:
        print(f"Erro na leitura do PDF: {e}")
        return

    # Verificar e combinar tabelas
    if not dfs:
        print("Nenhuma tabela encontrada!")
        return

  
    df_full = pd.concat([df for df in dfs if df.shape[1] == len(dfs[0].columns)])
    
    colunas = {'OD': 'Odontológico', 'AMB': 'Ambulatorial'}
    df_full.rename(columns={k: v for k, v in colunas.items() if k in df_full.columns}, inplace=True)
    
    # Salvar CSV
    csv_path = os.path.join(DIRETORIO, 'dados_processados.csv')
    try:
        df_full.to_csv(csv_path, index=False, sep=';', encoding='utf-8-sig')
    except Exception as e:
        print(f"Erro ao salvar CSV: {e}")
        return
    
    zip_path = f'Teste_{SEU_NOME}.zip'
    try:
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            zipf.write(csv_path, arcname='dados_processados.csv')
        print(f"Arquivo {zip_path} criado com sucesso!")
    except Exception as e:
        print(f"Erro ao criar ZIP: {e}")

if __name__ == '__main__':
    processar_dados()
    print("Processamento concluido com sucesso!")
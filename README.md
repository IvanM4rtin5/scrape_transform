# 📊 Web Scraping e Transformação de Dados - ANS

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.2.3-150458?logo=pandas)](https://pandas.pydata.org/)
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.13.3-3776AB)](https://www.crummy.com/software/BeautifulSoup/)
[![Tabula-py](https://img.shields.io/badge/Tabula.py-2.10.0-FF6F61)](https://tabula-py.readthedocs.io/)

Este projeto realiza a extração e transformação de dados dos Anexos I e II do Rol de Procedimentos da ANS (Agência Nacional de Saúde Suplementar).

---

## 🛠️ Tecnologias Utilizadas

<div align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Requests-2.32.3-000000?logo=python" alt="Requests" />
  <img src="https://img.shields.io/badge/BeautifulSoup-4.13.3-3776AB" alt="BeautifulSoup" />
  <img src="https://img.shields.io/badge/Pandas-2.2.3-150458?logo=pandas" alt="Pandas" />
  <img src="https://img.shields.io/badge/Tabula.py-2.10.0-FF6F61" alt="Tabula-py" />
  <img src="https://img.shields.io/badge/Numpy-2.2.4-013243?logo=numpy" alt="NumPy" />
</div>

---

## 🧩 Funcionalidades Principais

- **Web Scraping Automatizado**
  - Download dos Anexos I e II em PDF
  - Identificação automática dos links mais recentes
  - Armazenamento local dos arquivos
  - Compactação em formato ZIP

- **Processamento de Dados**
  - Extração de tabelas de PDFs usando OCR
  - Consolidação de múltiplas tabelas em um único DataFrame
  - Transformação e limpeza dos dados
  - Exportação para CSV
  - Geração de arquivo ZIP final

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

1. Python 3.10 ou superior instalado
2. Gerenciador de pacotes pip atualizado

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/IvanM4rtin5/web-scraping-ans.git
```
- Crie e ative um ambiente virtual (recomendado):

```bash
Copy
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
```
- Instale as dependências:

```bash
Copy
pip install -r requirements.txt
```
### Execução

- Execute o script de scraping:

```bash
Copy
python scrape.py
```
- Processe os dados coletados:

```bash
Copy
python transform.py
```
Os arquivos finais serão gerados na pasta arquivos/:

Anexos.zip: Arquivos PDF originais

Teste_Seu_Nome.zip: Arquivo CSV processado + PDFs

### 📂 Estrutura do Projeto
```Copy
web-scraping-ans/
├── arquivos/            # Pasta de armazenamento de arquivos
├── scrape.py            # Script principal de coleta
├── transform.py         # Script de transformação de dados
├── requirements.txt     # Dependências do projeto
├── .gitignore           # Arquivos ignorados pelo Git
└── README.md            # Documentação do projeto
```
### 💡 Desafios e Soluções

**Extração de Tabelas Complexas**

**Uso combinado de BeautifulSoup e Tabula-py**

**Configuração de parâmetros de leitura de PDF**

**Manipulação de Dados**

**Consolidação de múltiplas tabelas em um único DataFrame**

**Tratamento de cabeçalhos dinâmicos**

**Formatação consistente de dados numéricos**

**Automatização Completa**

**Download e verificação de arquivos**

**Gerenciamento de diretórios**

**Compactação automática dos resultados**

---
### 📧 Contato

**Nome:** Ivan Martins

**Email:** ivanmarti.alves@gmail.com

**LinkedIn:** https://www.linkedin.com/in/ivan-martins-alves/

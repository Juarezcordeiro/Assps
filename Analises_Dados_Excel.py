import pandas as pd

# Define o caminho para o arquivo Excel
arquivo_excel = r'C:\Pynthon\Dados\Cadastro_Funcionarios.xlsx'

# Lê a planilha especificada. Se não especificar, lê a primeira planilha.
df = pd.read_excel(arquivo_excel)

# Mostra as primeiras linhas do DataFrame para verificação
print(df.head())

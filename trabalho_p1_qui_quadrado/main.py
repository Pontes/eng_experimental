import pandas as pd
from scipy.stats import chi2_contingency

# dados_de_teste = pd.read_csv('dados.csv', sep='\t', quotechar='"')
dados_de_teste = pd.read_csv('dados.csv')

# print(dados_de_teste.head())
print(dados_de_teste)
# print(dados_de_teste.columns)
# print(dados_de_teste.info())
# print(dados_de_teste['Alternating'].unique()) ## esse comando pega todos os valores da coluna especificada
# print(dados_de_teste['Alternating'].value_counts()) ## esse comando conta quantas vezes o valor aparece na coluna

print("")
dado_selecionado = dados_de_teste.loc[dados_de_teste.index == 'Finances']
print(dado_selecionado)
print("")

chi2, p, dof, expected = chi2_contingency(dados_de_teste)
print(f'X2 : {chi2}') ##qui quadrado
print(f'P-value {p}') ##
print(f'Grau de liberdade {dof}')
print(f'Frequencia esperada \n {expected}')


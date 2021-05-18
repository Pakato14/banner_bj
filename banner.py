import pandas as pd


catalogo_df = pd.read_excel('base.xlsx')

#pesquisar a peça
try:
    codigo_bj = input("Digite o código bastos: ").upper()
except ValueError:
    print('Código não encontrado')

#coluna
coluna1 = catalogo_df.loc[1:,['endereco_junta']]
coluna2 = catalogo_df.loc[1:,['endereco_carro']]
coluna3 = catalogo_df.loc[1:,['marca']]
coluna4 = catalogo_df.loc[1:,['modelo']]
coluna5 = catalogo_df.loc[1:,['junta_completa']]
coluna6 = catalogo_df.loc[1:,['junta_superior']]
coluna7 = catalogo_df.loc[1:,['junta_cabecote']]

#transforma cada coluna em uma lista
var1 = list(coluna1['endereco_junta'])
var2 = list(coluna2['endereco_carro'])
var3 = list(coluna3['marca'])
var4 = list(coluna4['modelo'])
var5 = list(coluna5['junta_completa'])
var6 = list(coluna6['junta_superior'])
var7 = list(coluna7['junta_cabecote'])

#retorna características da peça procurada

jc = codigo_bj
ej = var1[var5.index(codigo_bj)]
ec = var2[var5.index(codigo_bj)]
mc = var3[var5.index(codigo_bj)]
md = var4[var5.index(codigo_bj)]
js = var6[var5.index(codigo_bj)]
jcb = var7[var5.index(codigo_bj)]

print(ej)
print(ec)
print(mc)
print(md)
print(jc)
print(js)
print(jcb)

#codigo_bj in var5
#print("A peça digitada foi: ", codigo_bj)



#print(catalogo_df.loc[catalogo_df['JOGO DE JUNTA COMPLETO'] == codigo_bj])

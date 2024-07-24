faturamento = 1200 # nuumero inteiro
custo = 770

novas_vendas = 300
faturamento = faturamento + novas_vendas

taxa_imposto = 0.1  # numero decimal -> float
#são números inteiros
#textos
mesagem = "O faturamento foi de "
teve_lucro = False # boolean

imposto = taxa_imposto * faturamento
print ("faturamento da empresa", faturamento)
print ("Custo", custo)
print ("Lucro", faturamento - custo - imposto)
print (mensagem, faturamento)
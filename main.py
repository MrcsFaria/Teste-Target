# Decidi fazer o teste utilizando a linguagem Python, pois é a linguagem com qual trabalho no dia a dia

#importando a biblioteca pandas para manusear e lidar com os dados do exercicio 3
import pandas as pd

# Exercicio 1
# Neste Exercicio, escrevi o laço mostrado no exercicio na sintaxe do Python

indice = 13
soma = 0
k = 0

while k < indice:
    k = k + 1
    soma= soma + k

print("Resposta do Exercicio 1")    
print(f"o valor da variável SOMA é {soma}")

# Exercicio 2
# Neste exercicio, utilizei a logica da fibonacci e criei um laço para identificar se o número pertence ou não à sequência

# Inicializando os dois primeiros números da sequência
a = 0
b = 1

# Como o usuário irá realizar o imput de um número, inseri o try-except para lidar com erros de uso
try:
    numero = int(input("\nDigite um número para verificar se o mesmo está na sequência Fibonacci: "))

    # Gerar a sequência enquanto 'b' for menor ou igual ao número informado
    while b <= numero:
        if b == numero:
            print("Resposta do Exercicio 2")    
            print(f"O numero {numero} pertence à sequência fibonacci")
            break
        a = b
        b = a + b
    else:
        print("Resposta do Exercicio 2") 
        print(f"O numero {numero} não pertence à sequência fibonacci")

except:
    print("Por favor, digite um número inteiro válido.")

# Exercicio 3
# Neste exercicio, primeiro resolvi transformar o vetor em um dataframe, para depois realizar uma analise e trazer os resultados

# dados do arquivo 'dados.json'
vetor_faturamento = [
	{
		"dia": 1,
		"valor": 22174.1664
	},
	{
		"dia": 2,
		"valor": 24537.6698
	},
	{
		"dia": 3,
		"valor": 26139.6134
	},
	{
		"dia": 4,
		"valor": 0.0
	},
	{
		"dia": 5,
		"valor": 0.0
	},
	{
		"dia": 6,
		"valor": 26742.6612
	},
	{
		"dia": 7,
		"valor": 0.0
	},
	{
		"dia": 8,
		"valor": 42889.2258
	},
	{
		"dia": 9,
		"valor": 46251.174
	},
	{
		"dia": 10,
		"valor": 11191.4722
	},
	{
		"dia": 11,
		"valor": 0.0
	},
	{
		"dia": 12,
		"valor": 0.0
	},
	{
		"dia": 13,
		"valor": 3847.4823
	},
	{
		"dia": 14,
		"valor": 373.7838
	},
	{
		"dia": 15,
		"valor": 2659.7563
	},
	{
		"dia": 16,
		"valor": 48924.2448
	},
	{
		"dia": 17,
		"valor": 18419.2614
	},
	{
		"dia": 18,
		"valor": 0.0
	},
	{
		"dia": 19,
		"valor": 0.0
	},
	{
		"dia": 20,
		"valor": 35240.1826
	},
	{
		"dia": 21,
		"valor": 43829.1667
	},
	{
		"dia": 22,
		"valor": 18235.6852
	},
	{
		"dia": 23,
		"valor": 4355.0662
	},
	{
		"dia": 24,
		"valor": 13327.1025
	},
	{
		"dia": 25,
		"valor": 0.0
	},
	{
		"dia": 26,
		"valor": 0.0
	},
	{
		"dia": 27,
		"valor": 25681.8318
	},
	{
		"dia": 28,
		"valor": 1718.1221
	},
	{
		"dia": 29,
		"valor": 13220.495
	},
	{
		"dia": 30,
		"valor": 8414.61
	}
]

df_faturamento = pd.DataFrame(vetor_faturamento)

# Menor valor de faturamento
menor_valor = df_faturamento['valor'].min()

# Maior valor de faturamento
maior_valor = df_faturamento['valor'].max()

# Média mensal de faturamento
media_mensal = df_faturamento['valor'].mean()

# Número de dias com faturamento superior à média mensal
dias_acima_media = df_faturamento[df_faturamento['valor'] > media_mensal].shape[0]

print("\nResposta do Exercicio 3") 
print(f"Menor valor de faturamento: R${menor_valor}")
print(f"Maior valor de faturamento: R${round(maior_valor,2)}")
print(f"Número de dias com faturamento superior à média mensal: {dias_acima_media}")


# Exercicio 4
# Neste Exercicio, primeiro fui convertendo as variaveis string para float após utilizar o replace para lidar com valores numéricos no formato brasileiro

faturamento_sp = "67.836,43"
faturamento_sp = faturamento_sp.replace('.', '').replace(',', '.')
faturamento_sp = float(faturamento_sp)

faturamento_rj = "36.678,66"
faturamento_rj = faturamento_rj.replace('.', '').replace(',', '.')
faturamento_rj = float(faturamento_rj)

faturamento_mg = "29.229,88"
faturamento_mg = faturamento_mg.replace('.', '').replace(',', '.')
faturamento_mg = float(faturamento_mg)

faturamento_es = "27.165,48"
faturamento_es = faturamento_es.replace('.', '').replace(',', '.')
faturamento_es = float(faturamento_es)

faturamento_outros = "19.849,53"
faturamento_outros = faturamento_outros.replace('.', '').replace(',', '.')
faturamento_outros = float(faturamento_outros)

#Calculo do total
faturamento_total = faturamento_sp + faturamento_rj + faturamento_mg + faturamento_es + faturamento_outros

#Calculo das porcentagens, arredondando para duas casas decimais
participacao_sp = round((faturamento_sp / faturamento_total) * 100, 2)
participacao_rj = round((faturamento_rj / faturamento_total) * 100, 2)
participacao_mg = round((faturamento_mg / faturamento_total) * 100, 2)
participacao_es = round((faturamento_es / faturamento_total) * 100, 2)
participacao_outros = round((faturamento_outros / faturamento_total) * 100, 2)

print("\nResposta do Exercicio 4") 
print(f"Representação de SP:  {participacao_sp}%")
print(f"Representação de RJ:  {participacao_rj}%")
print(f"Representação de MG:  {participacao_mg}%")
print(f"Representação de ES: {participacao_es}%")
print(f"Representação de Outros:  {participacao_outros}%")

# Exercicio 5
# Nesse exercicio, resolvi criar uma array para armazenar as letras da string inversamente, e depois, juntar as letras do array, gerando uma palavra

string_para_inverter = "target"

# Declaração da Array
letras = []

qtd_letras_da_string = len(string_para_inverter)

# Laço para iterar começando pela ultima letra
while qtd_letras_da_string > 0:
    # Colocando as letras no Array
    letras.append(string_para_inverter[qtd_letras_da_string - 1])
    qtd_letras_da_string = qtd_letras_da_string - 1 

# Gerando a palavra com as letras que estão no array
string_invertida = ''.join(letras)

print("\nResposta do Exercicio 5") 
print(string_invertida)



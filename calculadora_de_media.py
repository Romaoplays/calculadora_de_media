import csv

try:
    csv_file = open("media.csv")
except FileNotFoundError:
    csv_file = open("media.csv", "w")
    csv_file.close()
    csv_file = open("media.csv", "r")

csv_reader = csv.reader(csv_file)

csv_list = list(csv_reader)


print("\nQual média você quer calcular?\n\na - Adicionar Matéria\n")
csv_list_temp = []
for row in csv_list:
    if any(row):
        csv_list_temp.append(row)
csv_list = csv_list_temp

if range(len(csv_list)) != 0:
    for i in range(len(csv_list)):
        print(f"{str(i)} - {csv_list[i][0]}")

resposta = input()

if resposta == "a":
    csv_file.close()
    csv_file = open("media.csv", "a")
    lista_add = []
    print("Nome da matéria:")
    lista_add.append(input())
    k = 1
    while True:
        print(f"Nome da {k}a avaliação: ('fim' para sair)")
        input_avaliacao = input()
        if input_avaliacao == "fim":
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(lista_add)
            break
        else:
            lista_add.append(input_avaliacao)
            print(f"Peso da {k}a avaliação:")
            lista_add.append(input())
        k = k + 1
else:
    media_list = csv_list[int(resposta)]
    nota_list = []
    peso_list = []
    media_soma = 0
    peso_soma = 0
    for i in range(len(media_list)):
        if i == 0:
            pass
        elif (i % 2) == 1:
            print(f"Nota de {media_list[i]}:")
            nota_list.append(float(input()))
        else:
            peso_list.append(float(media_list[i]))

    for i in range(len(nota_list)):
        media_soma = (nota_list[i] * peso_list[i]) + media_soma
        peso_soma = peso_list[i] + peso_soma

    media_final = media_soma / peso_soma
    print(f"\nSua média final é: {round(media_final,2)}")


csv_file.close()

while True:
    print("\n'sair' para sair")
    if input() == "sair":
        break
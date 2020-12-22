import ezsheets

ss = ezsheets.Spreadsheet("1AP3ndHUSytLDzKFvT2V3Je_zO2dl1uzHf_RvjG70ew4")
sheet = ss[0]

materias = sheet.getColumn(1)
# avaliacoes_1 = sheet.getColumn(2)
# pesos_1 = sheet.getColumn(3)
# avaliacoes_2 = sheet.getColumn(4)
# pesos_2 = sheet.getColumn(5)
# avaliacoes_3 = sheet.getColumn(6)
# pesos_3 = sheet.getColumn(7)
# avaliacoes_4 = sheet.getColumn(8)
# pesos_4 =  sheet.getColumn(9)
# avaliacoes_5 = sheet.getColumn(10)
# pesos_5 =  sheet.getColumn(11)

tamanho_materias = []

for i in range(len(materias)):
    if materias[i] != "":
        tamanho_materias.append(materias[i])

# Perguntar Qual média quer calcular/Se quer adicionar uma nova
print("Qual média quer calcular?")
print("0 - Adicionar uma nova")
for i in range(len(tamanho_materias)):
    print(str(i + 1) + " - " + materias[i])

# Adicionar uma nova e salvar no EZSHEETS #Nome da matéria | avaliação | peso | avaliação | peso |
j = 1
g = 0


def pegar_resposta():
    global j
    resposta_nome = input()
    if resposta_nome == "salvar":
        return False
    else:
        sheet[j, len(tamanho_materias) + 1] = resposta_nome
        j = j + 1
        return True


resposta = input()
resposta = int(resposta)
if resposta == 0:
    print('Qual o nome da matéria? (Escreva "salvar" para salvar a qualquer momento)')
    if pegar_resposta() == False:
        g = 1
    for i in range(10):
        if g == 1:
            break
        print(
            "Qual o nome da "
            + str(i + 1)
            + 'a avaliação? (Escreva "salvar" para salvar)'
        )
        if pegar_resposta() == False:
            break
        print("Qual o peso da prova?")
        while True:
            if pegar_resposta() == False:
                print("Por favor adicione um peso")
            else:
                break
    print("Resposta adicionada")
    g = 0

# Calcular a média
else:
    rows = sheet.getRow(resposta)
    rows_tamanho = []
    for i in range(len(rows)):
        if rows[i] != "":
            rows_tamanho.append(rows[i])

    lista_notas = []

    for i in range(1, len(rows_tamanho), 2):
        print("Nota da " + str(rows[i]))
        resposta_2 = input()
        lista_notas.append(resposta_2)

    lista_final = []
    lista_pesos = []
    p = 0

    for i in range(2, len(rows_tamanho), 2):
        lista_final.append(float(lista_notas[p]) * float(rows[i]))
        lista_pesos.append(float(rows[i]))
        p = p + 1

    media_final = float(sum(lista_final)) / float(sum(lista_pesos))

    print("Sua média final é: " + str(round(media_final, 1)))

while True:
    nadaa = input()

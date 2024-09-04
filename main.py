
# Solicita o número de rodadas0
empate = False
pesoD = float(input("Informe o peso das questões difíceis: "))
pesoM = float(input("Informe o peso das questões médias: "))
pesoF = float(input("Informe o peso das questões fáceis: "))
somaPeso = pesoD + pesoM + pesoF
equipe1 = input("Qual o nome da primeira equipe? ")
equipe2 = input("Qual o nome da segunda equipe? ")
equipe3 = input("Qual o nome da terceira equipe? ")
equipe4 = input("Qual o nome da quarta equipe? ")
equipe5 = input("Qual o nome da quinta equipe? ")

rodadas = int(input("Quantas rodadas serão? "))

primeiraNota = segundaNota = terceiraNota = quartaNota = quintaNota = 0

primeiraEquipe = segundaEquipe = terceiraEquipe = quartaEquipe = quintaEquipe = ""
# Inicializa os totais para cada equipe
totalQuestoesDifE1 = 0
totalQuestoesMedE1 = 0
totalQuestoesFacE1 = 0
totalTempoE1 = 0
totalPesoE1 = 0

totalQuestoesDifE2 = 0
totalQuestoesMedE2 = 0
totalQuestoesFacE2 = 0
totalTempoE2 = 0
totalPesoE2 = 0

totalQuestoesDifE3 = 0
totalQuestoesMedE3 = 0
totalQuestoesFacE3 = 0
totalTempoE3 = 0
totalPesoE3 = 0

totalQuestoesDifE4 = 0
totalQuestoesMedE4 = 0
totalQuestoesFacE4 = 0
totalTempoE4 = 0
totalPesoE4 = 0

totalQuestoesDifE5 = 0
totalQuestoesMedE5 = 0
totalQuestoesFacE5 = 0
totalTempoE5 = 0
totalPesoE5 = 0



# Loop para processar as rodadas
for i in range(rodadas):

    # Coleta dados para a equipe 1 e atualiza os totais
    questoesDifE1 = int(input("Quantas questoes dificeis a equipe 1 acertou nesta rodada? "))
    questoesMedE1 = int(input("Quantas questoes medias a equipe 1 acertou nesta rodada? "))
    questoesFacE1 = int(input("Quantas questoes faceis a equipe 1 acertou nesta rodada? "))
    tempoE1 = int(input("Quantos minutos a equipe 1 levou para responder todas as perguntas nesta rodada (Responda sem os segundos)? "))

    totalQuestoesDifE1 += questoesDifE1
    totalQuestoesMedE1 += questoesMedE1
    totalQuestoesFacE1 += questoesFacE1
    totalTempoE1 += tempoE1
    totalPesoE1 = (totalQuestoesDifE1 * pesoD) + (totalQuestoesMedE1 * pesoM) +(totalQuestoesFacE1 * pesoF )


    # Coleta dados para a equipe 2 e atualiza os totais
    questoesDifE2 = int(input("Quantas questões difíceis a equipe 2 acertou nesta rodada? "))
    questoesMedE2 = int(input("Quantas questões médias a equipe 2 acertou nesta rodada? "))
    questoesFacE2 = int(input("Quantas questões fáceis a equipe 2 acertou nesta rodada? "))
    tempoE2 = int(input("Quantos minutos a equipe 2 levou para responder todas as perguntas nesta rodada (Responda sem os segundos)? "))

    totalQuestoesDifE2 += questoesDifE2
    totalQuestoesMedE2 += questoesMedE2
    totalQuestoesFacE2 += questoesFacE2
    totalTempoE2 += tempoE2
    totalPesoE3 = (totalQuestoesDifE3 * pesoD) + (totalQuestoesMedE3 * pesoM) + (totalQuestoesFacE3 * pesoF)


    # Coleta dados para a equipe 3 e atualiza os totais
    questoesDifE3 = int(input("Quantas questões difíceis a equipe 3 acertou nesta rodada? "))
    questoesMedE3 = int(input("Quantas questões médias a equipe 3 acertou nesta rodada? "))
    questoesFacE3 = int(input("Quantas questões fáceis a equipe 3 acertou nesta rodada? "))
    tempoE3 = int(input("Quantos minutos a equipe 3 levou para responder todas as perguntas nesta rodada (Responda sem os segundos)? "))

    totalQuestoesDifE3 += questoesDifE3
    totalQuestoesMedE3 += questoesMedE3
    totalQuestoesFacE3 += questoesFacE3
    totalTempoE3 += tempoE3
    totalPesoE3 = (totalQuestoesDifE3 * pesoD) + (totalQuestoesMedE3 * pesoM) + (totalQuestoesFacE3 * pesoF)

    # Coleta dados para a equipe 4 e atualiza os totais
    questoesDifE4 = int(input("Quantas questões difíceis a equipe 4 acertou nesta rodada? "))
    questoesMedE4 = int(input("Quantas questões médias a equipe 4 acertou nesta rodada? "))
    questoesFacE4 = int(input("Quantas questões fáceis a equipe 4 acertou nesta rodada? "))
    tempoE4 = int(input("Quantos minutos a equipe 4 levou para responder todas as perguntas nesta rodada (Responda sem os segundos)? "))

    totalQuestoesDifE4 += questoesDifE4
    totalQuestoesMedE4 += questoesMedE4
    totalQuestoesFacE4 += questoesFacE4
    totalTempoE4 += tempoE4
    totalPesoE4 = (totalQuestoesDifE4 * pesoD) + (totalQuestoesMedE4 * pesoM) + (totalQuestoesFacE4 * pesoF)

    # Coleta dados para a equipe 5 e atualiza os totais
    questoesDifE5 = int(input("Quantas questões difíceis a equipe 5 acertou nesta rodada? "))
    questoesMedE5 = int(input("Quantas questões médias a equipe 5 acertou nesta rodada? "))
    questoesFacE5 = int(input("Quantas questões fáceis a equipe 5 acertou nesta rodada? "))
    tempoE5 = int(input("Quantos minutos a equipe 5 levou para responder todas as perguntas nesta rodada (Responda sem os segundos)? "))

    totalQuestoesDifE5 += questoesDifE5
    totalQuestoesMedE5 += questoesMedE5
    totalQuestoesFacE5 += questoesFacE5
    totalTempoE5 += tempoE5
    totalPesoE5 = (totalQuestoesDifE5 * pesoD) + (totalQuestoesMedE5 * pesoM) + (totalQuestoesFacE5 * pesoF)

mediaTotal = (totalPesoE1 + totalPesoE2 + totalPesoE3 + totalPesoE4 + totalPesoE5) / 5
print(f"Média total é {mediaTotal}")

if totalPesoE1 == totalPesoE2 == totalPesoE3 == totalPesoE4 == totalPesoE5:
    empate = True
    print("Houve um empate entre todas as equipes!")
elif totalPesoE1 == totalPesoE2:
    empate = True
    print(f"Houve um empate entre a equipe {equipe1} e a equipe {equipe2}!")
elif totalPesoE1 == totalPesoE3:
    empate = True
    print(f"Houve um empate entre a equipe {equipe1} e a equipe {equipe3}!")
elif totalPesoE1 == totalPesoE4:
    empate = True
    print(f"Houve um empate entre a equipe {equipe1} e a equipe {equipe4}!")
elif totalPesoE1 == totalPesoE5:
    empate = True
    print(f"Houve um empate entre a equipe {equipe1} e a equipe {equipe5}!")
elif totalPesoE2 == totalPesoE3:
    empate = True
    print(f"Houve um empate entre a equipe {equipe2} e a equipe {equipe3}!")
elif totalPesoE2 == totalPesoE4:
    empate = True
    print(f"Houve um empate entre a equipe {equipe2} e a equipe {equipe4}!")
elif totalPesoE2 == totalPesoE5:
    empate = True
    print(f"Houve um empate entre a equipe {equipe2} e a equipe {equipe5}!")
elif totalPesoE3 == totalPesoE4:
    empate = True
    print(f"Houve um empate entre a equipe {equipe3} e a equipe {equipe4}!")
elif totalPesoE3 == totalPesoE5:
    empate = True
    print(f"Houve um empate entre a equipe {equipe3} e a equipe {equipe5}!")
elif totalPesoE4 == totalPesoE5:
    empate = True
    print(f"Houve um empate entre a equipe {equipe4} e a equipe {equipe5}!")

while empate == False:
    if totalPesoE1 > primeiraNota:
        primeiraNota = totalPesoE1
        primeiraEquipe = equipe1
    if totalPesoE2 > primeiraNota:
        primeiraNota = totalPesoE2
        primeiraEquipe = equipe2
    if totalPesoE3 > primeiraNota:
        primeiraNota = totalPesoE3
        primeiraEquipe = equipe3
    if totalPesoE4 > primeiraNota:
        primeiraNota = totalPesoE4
        primeiraEquipe = equipe4
    if totalPesoE5 > primeiraNota:
        primeiraNota = totalPesoE5
        primeiraEquipe = equipe5

    # Determine o segundo maior valor para `segundaNota`
    if totalPesoE1 > segundaNota and totalPesoE1 < primeiraNota:
        segundaNota = totalPesoE1
        segundaEquipe = equipe1
    if totalPesoE2 > segundaNota and totalPesoE2 < primeiraNota:
        segundaNota = totalPesoE2
        segundaEquipe = equipe2
    if totalPesoE3 > segundaNota and totalPesoE3 < primeiraNota:
        segundaNota = totalPesoE3
        segundaEquipe = equipe3
    if totalPesoE4 > segundaNota and totalPesoE4 < primeiraNota:
        segundaNota = totalPesoE4
        segundaEquipe = equipe4
    if totalPesoE5 > segundaNota and totalPesoE5 < primeiraNota:
        segundaNota = totalPesoE5
        segundaEquipe = equipe5

    # Determine o terceiro maior valor para `terceiraNota`
    if totalPesoE1 > terceiraNota and totalPesoE1 < segundaNota:
        terceiraNota = totalPesoE1
        terceiraEquipe = equipe1
    if totalPesoE2 > terceiraNota and totalPesoE2 < segundaNota:
        terceiraNota = totalPesoE2
        terceiraEquipe = equipe2
    if totalPesoE3 > terceiraNota and totalPesoE3 < segundaNota:
        terceiraNota = totalPesoE3
        terceiraEquipe = equipe3
    if totalPesoE4 > terceiraNota and totalPesoE4 < segundaNota:
        terceiraNota = totalPesoE4
        terceiraEquipe = equipe4
    if totalPesoE5 > terceiraNota and totalPesoE5 < segundaNota:
        terceiraNota = totalPesoE5
        terceiraEquipe = equipe5

    # Determine o quarto maior valor para `quartaNota`
    if totalPesoE1 > quartaNota and totalPesoE1 < terceiraNota:
        quartaNota = totalPesoE1
        quartaEquipe = equipe1
    if totalPesoE2 > quartaNota and totalPesoE2 < terceiraNota:
        quartaNota = totalPesoE2
        quartaEquipe = equipe2
    if totalPesoE3 > quartaNota and totalPesoE3 < terceiraNota:
        quartaNota = totalPesoE3
        quartaEquipe = equipe3
    if totalPesoE4 > quartaNota and totalPesoE4 < terceiraNota:
        quartaNota = totalPesoE4
        quartaEquipe = equipe4
    if totalPesoE5 > quartaNota and totalPesoE5 < terceiraNota:
        quartaNota = totalPesoE5
        quartaEquipe = equipe5

    # Determine o quinto maior valor para `quintaNota`
    if totalPesoE1 > quintaNota and totalPesoE1 < quartaNota:
        quintaNota = totalPesoE1
        quintaEquipe = equipe1
    if totalPesoE2 > quintaNota and totalPesoE2 < quartaNota:
        quintaNota = totalPesoE2
        quintaEquipe = equipe2
    if totalPesoE3 > quintaNota and totalPesoE3 < quartaNota:
        quintaEquipe = equipe3
    if totalPesoE4 > quintaNota and totalPesoE4 < quartaNota:
        quintaEquipe = equipe4
    if totalPesoE5 > quintaNota and totalPesoE5 < quartaNota:
        quintaEquipe = equipe5
    print(print(f"primeiro: {primeiro}, segundo: {segundo}, terceiro: {terceiro}, quarto: {quarto}, quinto: {quinto}"))
    break
import re

def le_assinatura():
    # A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")
    print()

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))

    print()

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    # A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
    print()
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
        print()

    return textos

def separa_sentencas(texto):
    # A funcao recebe um texto e devolve uma lista das sentencas dentro do texto
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    # A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    # A funcao recebe uma frase e devolve uma lista das palavras dentro da frase
    return frase.split()

def n_palavras_unicas(lista_palavras):
    # Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    # Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    # Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.
    soma = 0

    for i in range(len(as_a)):
        soma += abs(as_a[i] - as_b[i])

    grau_similaridade = soma / 6
    return grau_similaridade

def calcula_assinatura(texto):
    # Essa funcao recebe um texto e deve devolver a assinatura do texto.

    sentencas = separa_sentencas(texto)
    num_sentencas = 0
    caracteres_sentenca = 0

    frases = []
    num_frases = 0
    caracteres_frase = 0

    for i in range(len(sentencas)):
        frase_aux = separa_frases(sentencas[i])
        frases.extend(frase_aux)
        num_sentencas += 1
        caracteres_sentenca += len(sentencas[i])

    palavras = []

    for i in range(len(frases)):
        palavra_aux = separa_palavras(frases[i])
        palavras.extend(palavra_aux)
        num_frases += 1
        caracteres_frase += len(frases[i])


    num_total_palavras = len(palavras)

    soma_palavra = 0

    for p in palavras:
        soma_palavra = soma_palavra + len(p)
    tam_medio_palavra = soma_palavra / num_total_palavras

    palavras_dif = n_palavras_diferentes(palavras)

    type_token = palavras_dif / num_total_palavras

    palavras_unicas = n_palavras_unicas(palavras)

    hapax_legomana = palavras_unicas / num_total_palavras

    tam_medio_sentenca = caracteres_sentenca / num_sentencas

    complexidade_sentenca = num_frases / num_sentencas

    tam_medio_frase = caracteres_frase / num_frases

    resultado = [tam_medio_palavra, type_token, hapax_legomana, tam_medio_sentenca, complexidade_sentenca, tam_medio_frase]

    return resultado

def avalia_textos(textos, ass_cp):
    # IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.
    assinatura = []
    for i in textos:
        assinatura.append(calcula_assinatura(i))

    similaridade = []
    for i in assinatura:
        similaridade.append(compara_assinatura(ass_cp, i))

    menor = similaridade[0]
    posicao = 1
    for i in range(len(similaridade)):
        if similaridade[i] < menor:
            menor = i
            posicao = i + 1
    print("O autor do texto", posicao, "está infectado com COH-PIAH")
    return posicao

def main():
    ass_cp = le_assinatura()
    textos = le_textos()

    avalia_textos(textos, ass_cp)

main()



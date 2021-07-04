def solution(resposta):
    solucao = ['sim', 'manu', 'juve', 'messi', ['fundos', 'curls', 'ups'], 'f1', 'chocolate', 'triplo', 'gelo', 'lopes']
    pontos = 0
    resultado = []
    for n in range(10):
        if solucao[n] == resposta[n]:
            pontos += 1
            resultado.append(f"Acertou na pergunta {n+1}, ganhou 1 ponto")
        else:
            resultado.append(f"Errou na pergunta {n+1}, ganhou 0 pontos")
    return [pontos, resultado]

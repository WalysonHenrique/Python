# crivo_de_eratostenes.py - Um algoritmo perfeito em eficiência

import time
import os
import psutil

def crivo_de_eratostenes(limite):
    """
    Encontra todos os números primos até um limite usando o Crivo de Eratóstenes.
    Este é um dos algoritmos mais eficientes para esta tarefa.
    """
    if limite < 2:
        return []

    # 1. Crie uma lista de booleanos (true/false) para marcar os números primos.
    #    Comece assumindo que todos os números são primos.
    primos = [True] * (limite + 1)
    primos[0] = primos[1] = False  # 0 e 1 não são primos.

    # 2. Itere do número 2 até a raiz quadrada do limite.
    for i in range(2, int(limite**0.5) + 1):
        # Se 'i' ainda for primo...
        if primos[i]:
            # ... marque todos os seus múltiplos como NÃO primos.
            # Comece de i*i, pois múltiplos menores já foram marcados.
            for multiplo in range(i*i, limite + 1, i):
                primos[multiplo] = False

    # 3. Construa a lista final de primos.
    lista_primos = []
    for i in range(2, limite + 1):
        if primos[i]:
            lista_primos.append(i)
    
    return lista_primos

if __name__ == "__main__":
    N = 200000000  # Mesmo limite dos seus testes
    
    # 1. Obtenha o processo atual do Python
    processo = psutil.Process(os.getpid())

    # 2. Resete o contador de CPU antes da tarefa
    processo.cpu_percent()

    # 3. Obtenha métricas de tempo e memória antes de iniciar
    mem_inicio = processo.memory_info().rss
    inicio = time.time()
    
    # Executa a tarefa intensiva
    lista_primos = crivo_de_eratostenes(N)
    
    # 4. Obtém métricas de tempo, memória e CPU após a tarefa
    fim = time.time()
    mem_fim = processo.memory_info().rss
    
    # Obtém a porcentagem média de CPU utilizada desde o reset
    cpu_uso_medio = processo.cpu_percent()

    duracao = fim - inicio
    diferenca_mem = mem_fim - mem_inicio

    print(f"Encontrados {len(lista_primos)} números primos até {N}.")
    print(f"Tempo de execução: {duracao:.4f} segundos")
    print(f"Uso de memória: {diferenca_mem/1024**2:.2f} MB")
    print(f"Uso médio de CPU durante a tarefa: {cpu_uso_medio}%")
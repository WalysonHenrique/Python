# primos.py - Gera números primos até um limite N

import time
import os
import psutil

def eh_primo(n):
    """Verifica se n é primo. Retorna True se primo, False caso contrário."""
    if n < 2:
        return False
    # Verifica divisibilidade de 2 até a raiz quadrada de n para otimizar
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def gerar_primos(limite):
    """Gera uma lista de números primos até o valor 'limite'."""
    primos = []
    for num in range(2, limite + 1):
        if eh_primo(num):
            primos.append(num)
    return primos

if __name__ == "__main__":
    N = 5000000  # Ajuste este valor para seus testes
    
    # Coleta de métricas dinâmicas
    processo = psutil.Process(os.getpid())
    processo.cpu_percent()
    mem_inicio = processo.memory_info().rss
    inicio = time.time()
    
    lista_primos = gerar_primos(N)
    
    fim = time.time()
    cpu_uso = processo.cpu_percent()
    mem_fim = processo.memory_info().rss
    duracao = fim - inicio
    diferenca_mem = mem_fim - mem_inicio

    print(f"Encontrados {len(lista_primos)} números primos até {N}.")
    print(f"Tempo de execução: {duracao:.4f} segundos")
    print(f"Uso de memória: {diferenca_mem/1024**2:.2f} MB")
    print(f"Uso médio de cpu : {cpu_uso}%")


# primos_extremo_complexo.py - Código para demonstrar alta complexidade ciclomática

import time
import os
import psutil

def eh_primo_ultra_complexo(n):
  
  
  
  
  
  
    # A complexidade começa a subir aqui
    if not isinstance(n, int) or n <= 1:
        if isinstance(n, float):
            return False # Entrada inválida
        elif n == 1:
            return False # 1 não é primo
        elif n <= 0:
            if n == 0:
                return False
            else:
                return False
        else:
            return False
    else:
        # Complexidade continua a aumentar com múltiplos if's aninhados
        if n % 2 == 0:
            if n == 2:
                if n > 0:
                    return True
                else:
                    return False
            else:
                return False
        else: # O número é ímpar
            if n % 3 == 0:
                if n == 3:
                    return True
                else:
                    return False
            else:
                i = 5
                # Aumenta a complexidade com um loop e várias condições
                while True:
                    if i * i > n:
                        return True
                    else:
                        if n % i == 0:
                            if i != n:
                                return False
                            else:
                                return True
                        i += 2
                        if n % i == 0:
                            if i != n:
                                return False
                            else:
                                return True
                        i += 4
                        if i * i > n:
                            break
                        else:
                            pass
                return True
    return False

def gerar_primos(limite):
    """Gera uma lista de números primos usando a função ultra-complexa."""
    primos = []
    for num in range(2, limite + 1):
        if eh_primo_ultra_complexo(num):
            primos.append(num)
    return primos

if __name__ == "__main__":
    N = 5000000
    
    processo = psutil.Process(os.getpid())
    processo.cpu_percent()
    mem_inicio = processo.memory_info().rss
    inicio = time.time()
    
    lista_primos = gerar_primos(N)
    
    fim = time.time()
    mem_fim = processo.memory_info().rss
    cpu_uso = processo.cpu_percent()
    duracao = fim - inicio
    diferenca_mem = mem_fim - mem_inicio

    print(f"Encontrados {len(lista_primos)} números primos até {N}.")
    print(f"Tempo de execução: {duracao:.4f} segundos")
    print(f"Uso de memória: {diferenca_mem/1024**2:.2f} MB")
    print(f"Uso de CPU: {cpu_uso}%")
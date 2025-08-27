"""Módulo para verificação e geração de números primos."""
from typing import List


def eh_primo(n: int) -> bool:
    """
    Verifica se um número é primo.

    Args:
        n: O número a ser verificado.

    Returns:
        True se o número for primo, False caso contrário.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def gerar_primos(limite: int) -> List[int]:
    """
    Gera uma lista de números primos até um limite especificado.

    Args:
        limite: O valor máximo (inclusivo) para a geração de primos.

    Returns:
        Uma lista contendo os números primos.
    """
    primos = []
    for num in range(2, limite + 1):
        if eh_primo(num):
            primos.append(num)
    return primos


if __name__ == "__main__":
    LIMITE_MAXIMO = 10000
    lista_primos = gerar_primos(LIMITE_MAXIMO)
    print(f"Encontrados {len(lista_primos)} números primos até {LIMITE_MAXIMO}.")
# Terminou a execucao

def calcular_depreciacao_linear(valor_inicial: float, valor_residual: float, vida_util_anos: int) -> float:
    """Calcula o valor de depreciação anual de um ativo corporativo."""
    if vida_util_anos <= 0:
        raise ValueError("A vida útil deve ser maior que zero.")
    return (valor_inicial - valor_residual) / vida_util_anos


def main():
    print("--- FINCALC PYTHON - MÓDULO FINANCEIRO ---")
    
    # Teste Aluno 5: Depreciação Linear
    print("\n[Aluno 5] Teste de Depreciação Linear:")
    depreciacao = calcular_depreciacao_linear(valor_inicial=10000.0, valor_residual=2000.0, vida_util_anos=5)
    print(f"Depreciação Anual: R$ {depreciacao:.2f}")


if __name__ == "__main__":
    main()
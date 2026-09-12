def calcular_margem_liquida(receita_total: float, custos_totais: float) -> float:
    """Calcula a margem de lucro líquida percentual de uma operação."""
    if receita_total <= 0:
        raise ValueError("A receita total deve ser maior que zero.")
    lucro = receita_total - custos_totais
    return (lucro / receita_total) * 100


def main():
    print("--- FINCALC PYTHON - ALUNO 7 ---")
    margem = calcular_margem_liquida(receita_total=50000.0, custos_totais=35000.0)
    print(f"Margem Líquida: {margem:.2f}%")


if __name__ == "__main__":
    main()
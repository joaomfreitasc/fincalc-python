def calcular_valor_futuro(aporte_mensal: float, taxa_mensal: float, meses: int) -> float:
    """Calcula o valor futuro acumulado com aportes mensais recorrentes."""
    i = taxa_mensal / 100
    vf = aporte_mensal * (((1 + i) ** meses - 1) / i)
    return vf

if __name__ == '__main__':
    # Valores de teste para a chamada do método
    aporte_teste = 500.00
    taxa_teste = 1.0  # 1.0% ao mês
    meses_teste = 12
    
    valor_acumulado = calcular_valor_futuro(aporte_teste, taxa_teste, meses_teste)
    
    print(f"Aporte Mensal: R$ {aporte_teste:.2f}")
    print(f"Taxa Mensal: {taxa_teste}%")
    print(f"Período: {meses_teste} meses")
    print(f"Valor Futuro Acumulado: R$ {valor_acumulado:.2f}")

def calcular_parcela_price(valor_emprestimo: float, taxa_mensal: float, meses: int) -> float:
    """Calcula o valor da parcela fixa em um financiamento pela Tabela Price."""
    i = taxa_mensal / 100
    parcela = valor_emprestimo * (i * ((1 + i) ** meses)) / (((1 + i) ** meses) - 1)
    return parcela

if __name__ == '__main__':
    # Valores de teste para a chamada do método
    valor_teste = 10000.00
    taxa_teste = 1.5  # 1.5% ao mês
    meses_teste = 12
    
    valor_parcela = calcular_parcela_price(valor_teste, taxa_teste, meses_teste)
    
    print(f"Valor do Empréstimo: R$ {valor_teste:.2f}")
    print(f"Taxa Mensal: {taxa_teste}%")
    print(f"Meses: {meses_teste}")
    print(f"Valor da Parcela (Tabela Price): R$ {valor_parcela:.2f}")
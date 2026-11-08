# FinCalc - Sistema de Cálculos Financeiros em Python


def calcular_juros_simples(capital: float, taxa_anual: float, anos: int) -> float:
    """Calcula o montante final obtido por juros simples."""
    juros = capital * (taxa_anual / 100) * anos
    return capital + juros


def calcular_aposentadoria(
    patrimonio_atual: float, aporte_mensal: float, anos: int, taxa_anual: float
) -> float:
    """Calcula o patrimônio acumulado para aposentadoria."""
    meses = anos * 12
    taxa_mensal = (taxa_anual / 100) / 12
    saldo = patrimonio_atual
    for _ in range(meses):
        saldo = (saldo + aporte_mensal) * (1 + taxa_mensal)
    return saldo


def calcular_juros_compostos(capital: float, taxa_anual: float, anos: int) -> float:
    """Calcula o montante final obtido por juros compostos."""
    if capital < 0:
        raise ValueError("O capital não pode ser negativo.")
    if taxa_anual < 0:
        raise ValueError("A taxa anual não pode ser negativa.")
    if anos < 0:
        raise ValueError("O tempo (anos) não pode ser negativo.")

    montante = capital * ((1 + (taxa_anual / 100)) ** anos)
    return montante


def calcular_depreciacao_linear(
    valor_inicial: float, valor_residual: float, vida_util_anos: int
) -> float:
    """Calcula o valor de depreciação anual de um ativo corporativo."""
    if vida_util_anos <= 0:
        raise ValueError("A vida útil deve ser maior que zero.")
    return (valor_inicial - valor_residual) / vida_util_anos


def calcular_irrf(salario_bruto: float) -> float:
    """Calcula a alíquota simplificada de Imposto de Renda Retido na Fonte."""
    if salario_bruto <= 2259.20:
        return 0.0
    elif salario_bruto <= 2826.65:
        return (salario_bruto * 0.075) - 169.44
    elif salario_bruto <= 3751.05:
        return (salario_bruto * 0.15) - 381.44
    else:
        return (salario_bruto * 0.225) - 662.77


def calcular_parcela_price(
    valor_emprestimo: float, taxa_mensal: float, meses: int
) -> float:
    """Calcula o valor da parcela fixa em um financiamento pela Tabela Price."""
    i = taxa_mensal / 100
    parcela = valor_emprestimo * (i * ((1 + i) ** meses)) / (((1 + i) ** meses) - 1)
    return parcela


def calcular_valor_futuro(
    aporte_mensal: float, taxa_mensal: float, meses: int
) -> float:
    """Calcula o valor futuro acumulado com aportes mensais recorrentes."""
    i = taxa_mensal / 100
    vf = aporte_mensal * (((1 + i) ** meses - 1) / i)
    return vf


def converter_taxa_anual_para_mensal(taxa_anual: float) -> float:
    """Converte uma taxa de juros anual equivalente para taxa mensal."""
    return (((1 + (taxa_anual / 100)) ** (1 / 12)) - 1) * 100


def calcular_margem_liquida(receita_total: float, custos_totais: float) -> float:
    """Calcula a margem de Lucro Líquida percentual de uma operação."""
    if receita_total <= 0:
        raise ValueError("A receita total deve ser maior que zero.")
    lucro = receita_total - custos_totais
    return (lucro / receita_total) * 100


def calcular_rendimento_real(ganho_nominal: float, inflacao: float) -> float:
    """Calcula o rendimento real ajustado pela inflação (Equação de Fisher)."""
    r_real = (((1 + (ganho_nominal / 100)) / (1 + (inflacao / 100))) - 1) * 100
    return r_real


def main():
    """Função principal que executa exemplos de cálculos financeiros."""
    print("Iniciando o sistema FinCalc...")
    montante = calcular_juros_simples(1000.0, 5.0, 2)
    print(f"Juros Simples (R$ 1.000 a 5% por 2 anos): R$ {montante:.2f}")
    montante_comp = calcular_juros_compostos(1000.0, 5.0, 2)
    print(f"Juros Compostos: R$ {montante_comp:.2f}")
    patrimonio = calcular_aposentadoria(10000.0, 500.0, 20, 6.0)
    print(f"Patrimônio Estimado para Aposentadoria: R$ {patrimonio:.2f}")
    depreciacao = calcular_depreciacao_linear(10000.0, 2000.0, 5)
    print(f"Depreciação Anual: R$ {depreciacao:.2f}")


if __name__ == "__main__":
    main()

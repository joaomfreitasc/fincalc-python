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

if __name__ == '__main__':
    salario_teste = 3000.00
    valor_irrf = calcular_irrf(salario_teste)
    
    print(f"Salário Bruto: R$ {salario_teste:.2f}")
    print(f"IRRF Retido: R$ {valor_irrf:.2f}")

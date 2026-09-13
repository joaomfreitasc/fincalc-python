def converter_taxa_anual_para_mensal(taxa_anual: float) -> float:
    """Converte uma taxa de juros anual equivalente para taxa mensal."""
    return (((1 + (taxa_anual / 100)) ** (1 / 12)) - 1) * 100


def main():
    print("--- FINCALC PYTHON - ALUNO 6 ---")
    taxa_mensal = converter_taxa_anual_para_mensal(12.0)
    print(f"Taxa Mensal Equivalente: {taxa_mensal:.4f}%")


if __name__ == "__main__":
    main()
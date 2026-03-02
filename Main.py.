

# ============================================
#    CALCULADORA DE ISR SEMANAL 2026
# ============================================

UMA = 117.31
LIMITE_EXENTO_HE_DOBLE = UMA * 5  # 5 UMAS DIARIAS


# Tabla ISR semanal 2026
TARIFA_ISR = [
    (0.01, 194.46, 0.00, 1.92),
    (194.47, 1650.67, 3.71, 6.40),
    (1650.68, 2900.87, 96.95, 10.88),
    (2900.88, 3372.11, 232.96, 16.00),
    (3372.12, 4037.32, 308.35, 17.92),
    (4037.33, 8142.75, 427.56, 21.36),
    (8142.76, 12834.08, 1304.45, 23.52),
    (12834.09, 24502.45, 2407.86, 30.00),
    (24502.46, 32669.91, 5908.35, 32.00),
    (32669.92, 98009.66, 8521.94, 34.00),
    (98009.67, float("inf"), 30737.49, 35.00),
]


def calcular_isr(base_gravable):
    for limite_inf, limite_sup, cuota_fija, porcentaje in TARIFA_ISR:
        if limite_inf <= base_gravable <= limite_sup:
            excedente = base_gravable - limite_inf
            impuesto = cuota_fija + (excedente * (porcentaje / 100))
            return round(impuesto, 2)
    return 0


def main():
    print("\n============================================")
    print("     CALCULADORA DE ISR SEMANAL 2026")
    print("============================================\n")

    sueldo = float(input("Ingresa sueldo semanal: $ "))
    he_doble = float(input("Ingresa tiempo extra doble: $ "))
    he_triple = float(input("Ingresa tiempo extra triple: $ "))

    # ------------------------------
    # Cálculo tiempo extra doble
    # ------------------------------
    exento_he_doble = min(he_doble, LIMITE_EXENTO_HE_DOBLE)
    gravado_he_doble = max(0, he_doble - LIMITE_EXENTO_HE_DOBLE)

    # ------------------------------
    # Tiempo extra triple
    # ------------------------------
    gravado_he_triple = he_triple  # 100% gravado

    # ------------------------------
    # Base gravable
    # ------------------------------
    base_gravable = sueldo + gravado_he_doble + gravado_he_triple

    # ------------------------------
    # Cálculo ISR
    # ------------------------------
    isr = calcular_isr(base_gravable)

    neto = (sueldo + he_doble + he_triple) - isr

    print("\n============== RESULTADO ==============\n")
    print(f"Sueldo gravado:              ${sueldo:,.2f}")
    print(f"HE doble exento:             ${exento_he_doble:,.2f}")
    print(f"HE doble gravado:            ${gravado_he_doble:,.2f}")
    print(f"HE triple gravado:           ${gravado_he_triple:,.2f}")
    print("----------------------------------------")
    print(f"Base gravable ISR:           ${base_gravable:,.2f}")
    print(f"ISR retenido:                ${isr:,.2f}")
    print("----------------------------------------")
    print(f"Neto a pagar:                ${neto:,.2f}")
    print("\n========================================\n")


if __name__ == "__main__":
    main()

from flask import Flask, render_template, request

app = Flask(__name__)

UMA = 117.31
LIMITE_EXENTO_HE_DOBLE = UMA * 5

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


@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None

    if request.method == "POST":
        sueldo = float(request.form["sueldo"])
        he_doble = float(request.form["he_doble"])
        he_triple = float(request.form["he_triple"])

        exento_he_doble = min(he_doble, LIMITE_EXENTO_HE_DOBLE)
        gravado_he_doble = max(0, he_doble - LIMITE_EXENTO_HE_DOBLE)
        gravado_he_triple = he_triple

        base_gravable = sueldo + gravado_he_doble + gravado_he_triple
        isr = calcular_isr(base_gravable)
        neto = (sueldo + he_doble + he_triple) - isr

        resultado = {
            "base": round(base_gravable, 2),
            "isr": isr,
            "neto": round(neto, 2),
            "exento": round(exento_he_doble, 2),
        }

    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)

"""Valida un CSV ficticio de haberes para la demostración del portafolio."""

import argparse
import csv
import re
from decimal import Decimal, InvalidOperation
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archivo", type=Path)
    args = parser.parse_args()

    validas = 0
    observadas = 0
    registros = set()

    try:
        with args.archivo.open(encoding="utf-8-sig", newline="") as archivo:
            lector = csv.DictReader(archivo, strict=True)
            if lector.fieldnames != ["registro", "periodo", "importe"]:
                parser.error("Se requiere el encabezado registro,periodo,importe.")

            for fila in lector:
                errores = []
                registro = (fila["registro"] or "").strip()
                periodo = (fila["periodo"] or "").strip()
                clave = (registro, periodo)

                if None in fila:
                    errores.append("columnas adicionales")
                if not registro:
                    errores.append("registro obligatorio")
                if not re.fullmatch(r"[0-9]{4}-(0[1-9]|1[0-2])", periodo):
                    errores.append("período inválido")
                if clave in registros:
                    errores.append("registro duplicado para el período")

                try:
                    importe = Decimal((fila["importe"] or "").strip())
                    if not importe.is_finite() or importe <= 0:
                        errores.append("importe inválido")
                except InvalidOperation:
                    errores.append("importe inválido")

                if errores:
                    observadas += 1
                    print(f"Fila {lector.line_num}: {', '.join(errores)}")
                else:
                    registros.add(clave)
                    validas += 1

    except (OSError, UnicodeError, csv.Error) as error:
        parser.error(str(error))

    print(f"Válidas: {validas} | Observadas: {observadas}")
    return int(observadas > 0)


if __name__ == "__main__":
    raise SystemExit(main())

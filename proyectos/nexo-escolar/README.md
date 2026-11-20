# Nexo Escolar

Proyecto propio para colegios privados de la provincia de Buenos Aires y estudios contables que preparan información salarial.

## Problema y solución

El cierre mensual exige revisar archivos de haberes y preparar los archivos de presentación. Nexo Escolar incorpora archivos compatibles, aplica controles de consistencia y genera `SALARIO.TXT` y un ZIP. La presentación en RUPA es asistida y queda a cargo del responsable de la institución.

Mi trabajo incluyó el diseño del flujo, la definición de controles de entrada y la preparación de la salida.

## Demo reproducible

La [demo de validación](validar_demo.py) usa un [CSV ficticio](haberes-demo.csv) para mostrar un control de campos obligatorios, importes y duplicados. Es un ejemplo didáctico independiente con un esquema simplificado.

Desde la raíz del repositorio, con Python 3.9 o posterior:

```bash
python3 proyectos/nexo-escolar/validar_demo.py proyectos/nexo-escolar/haberes-demo.csv
```

El archivo de muestra devuelve dos filas válidas y dos observadas. El programa devuelve código 1 cuando hay observaciones y 0 cuando todas las filas son válidas.

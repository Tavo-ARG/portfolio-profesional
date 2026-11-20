# Migración de pedidos de compra en SAP S/4HANA

Caso profesional anonimizado de preparación y validación de pedidos pendientes con SAP S/4HANA Migration Cockpit.

## Trabajo funcional

- Mapeé cabeceras, posiciones, imputaciones y textos de posición al template de migración.
- Preparé archivos SpreadsheetML y separé registros observados para su corrección.
- Organicé cargas por lotes y revisé los mensajes de simulación para distinguir errores corregibles con datos de origen de incidencias que requerían otro análisis.
- Concilié los registros por hoja y lote para identificar qué podía avanzar y qué requería reproceso.

## Ejemplo de control con cifras ficticias

| Unidad de control | Entrada | Preparados | Observados |
| --- | ---: | ---: | ---: |
| Cabeceras | 10 | 9 | 1 |
| Posiciones | 25 | 22 | 3 |

El control incluye revisar las posiciones dependientes cuando se observa una cabecera y mantener el detalle de los registros pendientes por lote.

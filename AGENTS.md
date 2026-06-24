# AGENTS.md

## Objetivo del proyecto

Mantener una base minima de skills abiertas para construccion en espanol, empezando por un skill canonico bien resuelto antes de ampliar el catalogo.

## Reglas editoriales

- Escribir en espanol claro, profesional y neutro.
- Incluir keywords en ingles dentro de la descripcion de cada skill.
- No inventar normativa, cantidades, precios, responsables, fechas ni marcas.
- Cuando falten datos, usar `[PENDIENTE]`.
- Separar hechos, supuestos e inferencias.
- Mantener cada skill enfocada en una tarea concreta.
- Preferir outputs utiles y revisables antes que frameworks documentales grandes.
- Evitar estructura auxiliar si no mejora de forma clara el uso o el mantenimiento.
- No usar APIs externas ni datos propietarios.

## Contrato minimo por skill

Cada skill debe incluir:

- `SKILL.md`

Directorios como `references/`, `templates/`, `examples/`, `evals/` y `scripts/` son opcionales. No agregarlos por defecto. Usarlos solo si resuelven una necesidad concreta y si realmente se van a mantener.

## Estado actual del repo

- El skill de referencia actual es `skills/cronograma-preliminar-obra/`.
- El resto de las skills existentes no deben marcar el enfoque editorial del repo mientras se revisan.
- La documentacion general debe describir primero el enfoque minimo y el skill activo, no un catalogo futuro.

## Validacion antes de cerrar un cambio

1. Confirmar que `name` coincide con el nombre de carpeta.
2. Confirmar que la `description` es especifica y trigger-friendly.
3. Ejecutar `python3 scripts/validate_repo.py`.

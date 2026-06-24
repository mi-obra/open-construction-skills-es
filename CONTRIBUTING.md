# Contributing

## Objetivo

Mantener una base minima de skills abiertas, utiles y seguras para tareas reales de construccion en espanol.

La prioridad actual no es ampliar rapido el catalogo. La prioridad es consolidar un skill canonico bien resuelto y usarlo para fijar criterio editorial y operativo.

El skill de referencia actual es `cronograma-preliminar-obra`.

## Reglas de contribucion

- Usa nombres de skills en minusculas y con guiones.
- Mantiene `skills/` como unica fuente de verdad.
- No agregues datos propietarios de Mi Obra.
- No inventes normativa, cantidades, precios ni responsables.
- Usa `[PENDIENTE]` cuando falte informacion.
- Separa hechos, supuestos e inferencias cuando la tarea lo requiera.
- Mantiene cada skill enfocada en una tarea concreta.
- Mantiene cada skill autocontenida en `SKILL.md` salvo que un archivo auxiliar aporte valor real y claro.
- No agregues `examples/`, `templates/`, `references/`, `evals/` o `scripts/` por inercia.
- Usa scripts solo cuando den un ahorro de mantenimiento claro.
- Si la documentacion general cambia, reflejala tambien en `README.md` y `AGENTS.md`.

## Que tipo de aporte priorizar

- Mejoras al skill activo.
- Simplificacion de instrucciones demasiado largas o difusas.
- Correccion de ambiguedades que puedan inducir alucinaciones o falsa precision.
- Ajustes de documentacion que reduzcan ruido o mantenimiento innecesario.

## Nuevas skills

Se pueden proponer nuevas skills, pero no son la prioridad inmediata.

Antes de abrir una nueva skill, comprobar que:

- no se resuelve mejor mejorando el skill activo;
- la tarea es concreta y recurrente;
- el alcance se puede definir con claridad;
- el mantenimiento adicional esta justificado.

La estructura minima esperada es:

```text
skills/
└── nombre-de-la-skill/
    └── SKILL.md
```

## Flujo recomendado

1. Editar archivos bajo `skills/`.
2. Ejecutar `python3 scripts/validate_repo.py`.
3. Actualizar `README.md`, `AGENTS.md` o `docs/` si el cambio modifica el enfoque general del repo.

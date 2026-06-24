# Open Construction Skills ES

Skills abiertas en espanol para agentes de IA aplicados a tareas concretas de construccion.

El skill de referencia actual es `cronograma-preliminar-obra`.

---

## Enfoque actual

- Un solo skill activo como referencia editorial y metodologica.
- Estructura minima basada en `SKILL.md`.
- Documentacion corta, solo donde realmente aporta.
- Sin obligar `examples/`, `templates/`, `references/` ni `evals` por defecto.

Una skill en este repo es una instruccion reutilizable que le dice a un agente:

- cuando usarla;
- cuando no usarla;
- que inputs espera;
- que output debe producir;
- que pasos debe seguir;
- que limites debe respetar.

## Skill de referencia

Por ahora la documentacion del repo toma como referencia este skill:

| Skill | Descripcion |
| ----- | ----------- |
| `cronograma-preliminar-obra` | Crea un cronograma preliminar de obra en espanol a partir de una memoria descriptiva, alcance, computo, presupuesto o informacion parcial, con WBS/EAP, actividades, duraciones, esfuerzo, supuestos, riesgos y preguntas abiertas. |

Las demas carpetas de `skills/` existen hoy como material en revision y no definen el estandar editorial actual.

---

## Estructura minima

```text
.
├── skills/
│   └── cronograma-preliminar-obra/
│       └── SKILL.md
├── scripts/
│   └── validate_repo.py
├── docs/
├── AGENTS.md
└── README.md
```

- `skills/` es la fuente canonica.
- `SKILL.md` es el contrato principal de cada skill.
- `docs/` solo deberia contener documentacion necesaria para usar o mantener el repo.
- `scripts/validate_repo.py` valida la estructura minima.
- `scripts/` puede incluir tooling auxiliar, pero no define el enfoque principal del repo.

---

## Criterios editoriales

- Escribir en espanol claro, profesional y neutro.
- No inventar normativa, cantidades, precios, marcas, responsables ni fechas.
- Usar `[PENDIENTE]` cuando falten datos.
- Separar hechos, supuestos e inferencias cuando aplique.
- Mantener cada skill enfocada en una tarea concreta.
- Evitar estructura auxiliar si no agrega valor claro.

---

## Alcance y limites

Este repo contiene instrucciones reutilizables para agentes de IA. No reemplaza criterio profesional ni documentacion contractual o ejecutiva revisada por especialistas.

No incluye datos propietarios, scraping, precios reales ni recomendaciones de marcas.

Cuando una tarea tenga impacto tecnico, normativo, contractual o de seguridad, la salida debe presentarse como preliminar y revisable.

---

## Instalacion y validacion

```bash
python3 scripts/validate_repo.py
```

---

## Como contribuir

- Mejorar el skill activo.
- Simplificar instrucciones.
- Corregir ambiguedades o riesgos de alucinacion.
- Proponer nueva documentacion solo si evita un problema real de uso o mantenimiento.
- Proponer nuevas skills solo cuando el enfoque minimo actual ya este suficientemente estable.

La estructura minima esperada para una skill nueva o revisada es:

```text
skills/
└── nombre-de-la-skill/
    └── SKILL.md
```

Carpetas auxiliares como `references/`, `templates/`, `examples/`, `evals/` o `scripts/` son opcionales y no deberian agregarse por defecto.

---

## Estado del proyecto

El repositorio esta en una etapa deliberadamente temprana y austera. La prioridad actual es consolidar un solo skill bien resuelto y usarlo para fijar criterio editorial y operativo.

---

## Licencia

MIT. Ver [LICENSE](LICENSE).

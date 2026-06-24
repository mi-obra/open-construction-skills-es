---
name: cronograma-preliminar-obra
description: Usar este skill cuando el usuario necesite crear, revisar o actualizar un cronograma preliminar de obra en español a partir de una memoria descriptiva, alcance de obra, cómputo métrico, presupuesto por rubros, especificaciones técnicas, resumen de planos, estado actual de obra o listado de tareas pendientes. El skill produce una tabla de cronograma preliminar, una tabla de estimación de esfuerzo y una sección de supuestos, riesgos y preguntas abiertas. No usar para cronogramas contractuales definitivos, reclamos de plazo, peritajes, claims ni planificación ejecutiva sin revisión profesional.
---

---

# Skill: cronograma-preliminar-obra

## Objetivo

Este skill ayuda a crear un **cronograma preliminar de obra** a partir de documentación parcial o incompleta.

El objetivo no es producir un cronograma contractual definitivo. El objetivo es transformar la información disponible en una planificación inicial, estructurada, explicable y revisable.

El resultado debe servir para:

- entender el alcance de la obra;
- ordenar las tareas principales;
- estimar duraciones preliminares;
- identificar dependencias constructivas;
- explicar el esfuerzo estimado;
- detectar supuestos, riesgos y datos faltantes.

El output por defecto debe ser en **Markdown**, en español, y debe incluir:

1. Resumen del alcance interpretado.
2. WBS/EAP preliminar.
3. Tabla de cronograma preliminar.
4. Tabla de estimación de esfuerzo.
5. Supuestos principales.
6. Riesgos y puntos críticos.
7. Preguntas abiertas.

No generar JSON, CSV, Gantt, archivos de MS Project ni outputs técnicos adicionales salvo que el usuario lo pida explícitamente.

Si el skill se usa desde CLI y el usuario no indica otro destino, guardar además el resultado en una carpeta con fecha y título descriptivo. Si el skill se usa desde chat, alcanza con responder en el chat salvo que el usuario pida guardar archivos.

Convención sugerida para CLI:

- carpeta: `outputs/YYYY-MM-DD-titulo-breve/`
- archivo principal: `cronograma-preliminar.md`
- usar un título breve, en minúsculas y con guiones;
- no inventar el título: derivarlo del tipo de obra, cliente, ubicación o alcance si esa información existe; si no existe, usar un título genérico prudente.

---

## Cuándo usar este skill

Usar este skill cuando el usuario pida cosas como:

- “Crear un cronograma preliminar de obra”.
- “Armar un cronograma a partir de esta memoria descriptiva”.
- “Estimar cuánto puede durar esta obra”.
- “Convertir este alcance de obra en una planificación preliminar”.
- “Revisar este cronograma de obra”.
- “Ordenar estas tareas de construcción”.
- “Crear una tabla de actividades, duraciones y dependencias”.
- “Hacer una estimación preliminar de esfuerzo por tarea”.
- “Armar un plan inicial de obra para una vivienda / reforma / edificio / local / rehabilitación”.
- “Crear un cronograma desde este presupuesto o cómputo”.

También usarlo si el usuario entrega alguno de estos inputs:

- memoria descriptiva;
- alcance de obra;
- cómputo métrico;
- presupuesto por rubros;
- especificaciones técnicas;
- resumen de planos;
- listado de partidas;
- cronograma existente;
- reporte de visita de obra;
- estado actual de obra;
- listado de tareas pendientes;
- descripción breve del proyecto.

Ejemplos de inputs válidos:

```text
Vivienda unifamiliar de 180 m², dos plantas, estructura de hormigón armado,
mampostería tradicional, instalación sanitaria, eléctrica, gas, pisos,
carpinterías y pintura.
```

```text
Reforma interior de departamento de 75 m². Incluye demolición de tabiques,
nueva distribución, instalación eléctrica, fontanería, falsos techos,
pisos, pintura y carpinterías interiores.
```

```text
Presupuesto por rubros: preliminares, demolición, albañilería, estructura,
instalaciones, revoques, pisos, pintura, limpieza final.
```

---

## Principios de trabajo

Seguir siempre estos principios:

1. **Primero entender el alcance.**
   Antes de cronogramar, resumir qué se entendió del proyecto.

2. **Armar una WBS/EAP antes del cronograma.**
   No saltar directamente de la memoria a fechas. Primero descomponer el alcance en rubros y paquetes de trabajo.

3. **Separar datos explícitos de supuestos.**
   Si un dato no está en el input, marcarlo como supuesto.

4. **Estimar esfuerzo antes que duración.**
   Siempre que sea posible, usar cantidad, unidad, rendimiento y cuadrilla para justificar la duración.

5. **Evitar falsa precisión.**
   Si falta información, usar rangos y confianza baja.

6. **Mostrar la lógica constructiva.**
   Las actividades deben seguir una secuencia razonable de obra.

7. **Listar datos faltantes.**
   El resultado debe indicar qué información permitiría mejorar la estimación.

8. **Mantener el output simple y útil.**
   La respuesta principal debe ser una tabla clara, no un documento excesivamente complejo.

---

## Flujo de trabajo obligatorio

Cuando uses este skill, seguí este flujo:

1. Leer el input completo.
2. Identificar tipo de obra.
3. Identificar alcance explícito.
4. Detectar partidas implícitas necesarias.
5. Armar una WBS/EAP preliminar.
6. Convertir la WBS/EAP en actividades cronogramables.
7. Asignar dependencias constructivas.
8. Estimar duraciones preliminares.
9. Justificar el esfuerzo cuando sea posible.
10. Marcar nivel de confianza.
11. Listar supuestos, riesgos y preguntas abiertas.

No pedir información adicional antes de generar una primera versión, salvo que el input sea imposible de interpretar. Si falta información, generar una versión preliminar y dejar explícitos los supuestos.

---

## Formato de respuesta obligatorio

La respuesta debe seguir esta estructura:

```markdown
# Cronograma preliminar de obra

## 1. Resumen del alcance interpretado

## 2. WBS/EAP preliminar

## 3. Cronograma preliminar

## 4. Estimación de esfuerzo

## 5. Supuestos principales

## 6. Riesgos y puntos críticos

## 7. Preguntas abiertas
```

Si se usa desde CLI y se guarda archivo, el contenido del archivo principal debe seguir la misma estructura.

---

## 1. Resumen del alcance interpretado

Empezar con un resumen breve del proyecto.

Incluir, cuando esté disponible:

- tipo de obra;
- superficie aproximada;
- cantidad de plantas;
- sistema constructivo;
- si es obra nueva, reforma, ampliación o rehabilitación;
- rubros principales detectados;
- fecha de inicio, si fue informada;
- plazo objetivo, si fue informado;
- calendario laboral, si fue informado;
- nivel de información disponible;
- nivel de confianza general.

Ejemplo:

```markdown
## 1. Resumen del alcance interpretado

- Tipo de obra: vivienda unifamiliar.
- Superficie considerada: 180 m².
- Sistema constructivo: tradicional, con estructura de hormigón armado y mampostería.
- Alcance detectado: preliminares, movimiento de suelo, fundaciones, estructura, mampostería, instalaciones, revoques, pisos, carpinterías, pintura y limpieza final.
- Información disponible: memoria descriptiva sin cómputo métrico.
- Nivel de confianza general: bajo/medio.
```

---

## 2. WBS/EAP preliminar

La WBS/EAP es la descomposición del alcance en rubros y paquetes de trabajo.

Debe responder:

> ¿Qué trabajos hay que hacer?

No debe incluir fechas todavía.

Ejemplo:

```markdown
## 2. WBS/EAP preliminar

1. Trabajos preliminares
   1.1 Revisión de documentación
   1.2 Replanteo
   1.3 Preparación de obra

2. Movimiento de suelo
   2.1 Limpieza del terreno
   2.2 Excavación
   2.3 Retiro de suelo sobrante

3. Fundaciones
   3.1 Armado de fundaciones
   3.2 Hormigonado
   3.3 Curado inicial

4. Estructura
   4.1 Columnas
   4.2 Vigas y losas
   4.3 Desencofrado y revisión
```

Adaptar la WBS/EAP al tipo de obra. No usar una plantilla de obra nueva si el input describe una reforma o rehabilitación.

---

## 3. Cronograma preliminar

Crear una tabla Markdown con las actividades principales.

La tabla debe tener estas columnas:

| ID  | WBS/EAP | Actividad | Duración optimista | Duración probable | Duración conservadora | Predecesoras | Comentario | Confianza |
| --- | ------- | --------- | -----------------: | ----------------: | --------------------: | ------------ | ---------- | --------- |

Si el usuario dio fecha de inicio y calendario laboral, agregar:

| Inicio estimado | Fin estimado |

Si no hay fecha de inicio, no inventar fechas. Usar solo duración y secuencia relativa.

### Reglas para las actividades

- Las actividades deben ser suficientemente específicas para planificar.
- No usar actividades enormes como “hacer la obra completa”.
- No entrar en detalle excesivo si el input no lo soporta.
- Agrupar tareas cuando el nivel de información sea bajo.
- Separar compras o lead times cuando puedan afectar el plazo.
- Permitir trabajos en paralelo solo si tiene sentido constructivo.
- Marcar las actividades inciertas con confianza baja.

Ejemplo:

```markdown
## 3. Cronograma preliminar

| ID  | WBS/EAP             | Actividad                                         | Duración optimista | Duración probable | Duración conservadora | Predecesoras | Comentario                                | Confianza |
| --- | ------------------- | ------------------------------------------------- | -----------------: | ----------------: | --------------------: | ------------ | ----------------------------------------- | --------- |
| 1.1 | Preliminares        | Revisión de documentación y planificación inicial |                1 d |               2 d |                   3 d | —            | Se asume documentación disponible         | Media     |
| 1.2 | Preliminares        | Replanteo y preparación de obra                   |                2 d |               3 d |                   5 d | 1.1          | Depende del acceso al terreno             | Media     |
| 2.1 | Movimiento de suelo | Limpieza y nivelación inicial                     |                2 d |               4 d |                   6 d | 1.2          | Sin datos de terreno                      | Baja      |
| 3.1 | Fundaciones         | Excavación de fundaciones                         |                3 d |               5 d |                   8 d | 2.1          | No se informa volumen ni tipo de suelo    | Baja      |
| 3.2 | Fundaciones         | Armado y hormigonado de fundaciones               |                6 d |               9 d |                  14 d | 3.1          | No se informa sistema exacto de fundación | Baja      |
```

---

## 4. Estimación de esfuerzo

Crear una segunda tabla que explique de dónde salen las duraciones.

Esta sección es obligatoria.

La tabla debe tener estas columnas:

| ID  | Actividad | Cantidad usada | Unidad | Rendimiento asumido | Cuadrilla asumida | Duración base | Factor ajuste | Duración probable | Fundamento | Confianza |
| --- | --------- | -------------: | ------ | ------------------: | ----------------- | ------------: | ------------: | ----------------: | ---------- | --------- |

### Jerarquía de estimación

Usar esta jerarquía:

### Nivel A: cantidad y rendimiento disponibles

Si hay cantidad y rendimiento, calcular:

```text
duración_base_días = cantidad / (rendimiento_por_cuadrilla_día × número_de_cuadrillas)
```

Ejemplo:

```text
Mampostería = 420 m²
Rendimiento = 22 m²/cuadrilla/día
Cuadrillas = 1
Duración base = 420 / 22 = 19,1 días ≈ 20 días
```

### Nivel B: cantidad disponible, rendimiento no disponible

Usar un rendimiento preliminar asumido y marcarlo como supuesto.

Ejemplo:

```text
Cantidad informada: 780 m² de revoque.
Rendimiento no informado.
Se usa rendimiento preliminar asumido.
Confianza: media/baja.
```

### Nivel C: cantidad no disponible, superficie o tipología disponible

Estimar por analogía según:

- tipo de obra;
- superficie;
- cantidad de plantas;
- complejidad;
- rubros incluidos;
- restricciones informadas.

Marcar confianza baja.

### Nivel D: solo hay descripción narrativa

Usar rangos amplios y confianza baja o muy baja.

Ejemplo:

```text
La memoria indica “instalación eléctrica completa”, pero no informa cantidad de bocas, canalizaciones ni tableros.
Se estima como paquete preliminar con rango amplio.
Confianza: baja.
```

### Ejemplo de tabla de esfuerzo

```markdown
## 4. Estimación de esfuerzo

| ID   | Actividad            | Cantidad usada | Unidad | Rendimiento asumido | Cuadrilla asumida          | Duración base | Factor ajuste | Duración probable | Fundamento                                                     | Confianza |
| ---- | -------------------- | -------------: | ------ | ------------------: | -------------------------- | ------------: | ------------: | ----------------: | -------------------------------------------------------------- | --------- |
| 5.1  | Mampostería interior |            420 | m²     |      22 m²/cuad/día | 1 cuadrilla de albañilería |          19 d |          1.10 |              21 d | Cantidad informada + ajuste por cortes/interferencias          | Media     |
| 7.1  | Revoques interiores  |            780 | m²     |      35 m²/cuad/día | 1 cuadrilla de albañilería |          22 d |          1.15 |              25 d | Cantidad informada + ajuste por coordinación con instalaciones | Media     |
| 10.1 | Pintura interior     |   No informada | m²     |        No aplicable | 1 cuadrilla de pintura     |             — |             — |           10–18 d | Estimación por analogía; falta superficie de muros/cielorrasos | Baja      |
```

---

## Esfuerzo, duración y lead time

Distinguir siempre entre:

- **Esfuerzo:** cantidad de trabajo requerido.
- **Duración:** tiempo transcurrido en el cronograma.
- **Lead time:** tiempo de compra, fabricación o espera.

Ejemplo:

```markdown
Carpinterías:

- Relevamiento de vanos: actividad de obra.
- Fabricación/provisión: lead time.
- Entrega en obra: hito logístico.
- Colocación: actividad de obra.
- Sellados y ajustes: actividad de terminación.
```

No reducir carpinterías, ascensores, tableros, equipos especiales o materiales críticos a una sola actividad genérica si su provisión puede afectar el plazo.

---

## Factores de ajuste

Aplicar factores de ajuste cuando el input indique condiciones que afecten productividad.

Usar factores simples y explicarlos.

| Condición                                   |     Efecto típico |
| ------------------------------------------- | ----------------: |
| Buen acceso y buen acopio                   |         0.90–1.00 |
| Acceso limitado                             |         1.10–1.30 |
| Sin espacio de acopio                       |         1.10–1.30 |
| Obra en edificio habitado                   |         1.20–1.50 |
| Reforma con demolición selectiva            |         1.20–1.60 |
| Muchas plantas sin buen transporte vertical |         1.10–1.40 |
| Trabajo repetitivo                          |         0.85–1.00 |
| Geometría compleja o muchos detalles        |         1.10–1.40 |
| Documentación insuficiente                  | usar rango amplio |

Si el input no menciona estas condiciones, no inventarlas. Usar factor 1.00 y listar la condición como pregunta abierta.

---

## Niveles de confianza

Cada actividad relevante debe tener nivel de confianza.

Usar:

- **Alta:** cantidad, rendimiento, recursos y condiciones conocidas.
- **Media:** cantidad conocida, pero rendimiento o condiciones asumidas.
- **Baja:** cantidad faltante y duración estimada por analogía.
- **Muy baja:** alcance poco claro.

Rangos sugeridos:

| Confianza | Rango recomendado      |
| --------- | ---------------------- |
| Alta      | ±10% a ±20%            |
| Media     | ±20% a ±35%            |
| Baja      | ±35% a ±60%            |
| Muy baja  | rango amplio solamente |

No usar rangos estrechos cuando la confianza sea baja.

---

## 5. Supuestos principales

Incluir siempre una sección de supuestos.

Separar por categorías:

```markdown
## 5. Supuestos principales

### Calendario

- Se asume trabajo de lunes a viernes.
- Se asume jornada de 8 horas.
- No se consideran feriados ni paradas por clima salvo que el input lo indique.

### Recursos

- Se asume una cuadrilla principal por rubro.
- No se realiza nivelación detallada de recursos.
- Se permiten solapes solo cuando son constructivamente razonables.

### Alcance

- Se incluyen las partidas detectadas en el input y las necesarias para completar el alcance informado.
- Las partidas no mencionadas explícitamente se marcan como inferidas.

### Estimación

- Las duraciones son preliminares.
- Cuando no hay cantidades, se usan rangos amplios por analogía.
- Los rendimientos asumidos deben revisarse con datos propios de la empresa, contratista o jefe de obra.
```

---

## 6. Riesgos y puntos críticos

Incluir una tabla compacta:

| Riesgo | Impacto en plazo | Mitigación sugerida |
| ------ | ---------------- | ------------------- |

Ejemplo:

```markdown
## 6. Riesgos y puntos críticos

| Riesgo                                | Impacto en plazo                         | Mitigación sugerida                               |
| ------------------------------------- | ---------------------------------------- | ------------------------------------------------- |
| Falta de cómputo métrico              | Duraciones con baja precisión            | Solicitar cantidades por rubro                    |
| Carpinterías sin lead time definido   | Puede atrasar el cierre de obra          | Definir proveedor y plazo de fabricación temprano |
| Instalaciones no coordinadas          | Retrabajos antes de revoques o cierres   | Revisar planos y pruebas antes de tapar           |
| Restricciones de acceso no informadas | Productividad posiblemente sobreestimada | Confirmar accesos, acopio y transporte interno    |
```

---

## 7. Preguntas abiertas

Terminar con las preguntas que más mejorarían la estimación.

Priorizar preguntas que puedan cambiar el plazo de forma material.

Ejemplo:

```markdown
## 7. Preguntas abiertas

1. ¿Cuál es la superficie cubierta y semicubierta exacta?
2. ¿Hay cómputo métrico por rubros?
3. ¿Cuántas cuadrillas estarán disponibles?
4. ¿Se trabaja de lunes a viernes o también sábados?
5. ¿Hay fecha objetivo de entrega?
6. ¿Hay restricciones de acceso, acopio o transporte interno?
7. ¿Las carpinterías, equipos o materiales críticos ya tienen proveedor definido?
8. ¿La obra es nueva, reforma, rehabilitación o ampliación?
```

---

## Plantillas WBS/EAP de referencia

Usar estas plantillas solo como punto de partida. Adaptarlas siempre al input real.

### Obra nueva residencial

```markdown
1. Trabajos preliminares
2. Movimiento de suelo
3. Fundaciones
4. Estructura
5. Mampostería y cerramientos
6. Cubierta
7. Instalaciones embutidas
8. Revoques y cielorrasos
9. Contrapisos y carpetas
10. Pisos y revestimientos
11. Carpinterías
12. Artefactos, equipos y terminaciones
13. Pintura
14. Pruebas, limpieza y entrega
```

### Reforma interior

```markdown
1. Relevamiento y protección de áreas
2. Demoliciones y retiros
3. Albañilería / tabiquería
4. Instalaciones
5. Cielorrasos
6. Preparación de superficies
7. Pisos y revestimientos
8. Carpinterías y equipamiento
9. Pintura y terminaciones
10. Limpieza y entrega
```

### Rehabilitación de edificio

```markdown
1. Relevamiento, permisos y protecciones
2. Andamios, medios auxiliares y seguridad
3. Demoliciones selectivas
4. Reparaciones estructurales
5. Fachadas y envolvente
6. Cubierta
7. Instalaciones comunes
8. Accesibilidad / ascensor si aplica
9. Reparaciones interiores afectadas
10. Terminaciones
11. Pruebas, repasos y entrega
```

### Local comercial / fit-out

```markdown
1. Relevamiento y replanteo
2. Demoliciones y retiros
3. Tabiquería y divisiones
4. Instalaciones eléctricas, sanitarias y climatización
5. Cielorrasos
6. Pisos y revestimientos
7. Carpinterías, mobiliario y equipamiento
8. Pintura e imagen comercial
9. Pruebas, habilitaciones y entrega
```

---

## Reglas básicas de dependencias

Usar lógica constructiva común:

- Revisión documental y preparación antes de iniciar obra.
- Replanteo antes de excavaciones, fundaciones o tabiquería nueva.
- Fundaciones antes de estructura.
- Estructura antes de cerramientos principales.
- Instalaciones embutidas antes de revoques, placas o cierres.
- Pruebas hidráulicas y eléctricas antes de tapar instalaciones.
- Trabajos húmedos antes de pintura final.
- Terminaciones delicadas después de tareas pesadas.
- Limpieza final y entrega al cierre.
- Compras críticas deben iniciarse con anticipación si tienen lead time.

Evitar secuencias imposibles, como:

- pintar antes de terminar trabajos húmedos;
- cerrar muros antes de probar instalaciones;
- colocar terminaciones finales antes de demoliciones pesadas;
- iniciar estructura antes de fundaciones;
- instalar carpinterías sin considerar fabricación o provisión.

---

## Manejo de inputs incompletos

Si el input es incompleto, no frenar el trabajo automáticamente.

Hacer lo siguiente:

1. Generar la mejor versión preliminar posible.
2. Marcar actividades de baja confianza.
3. Explicitar supuestos.
4. Listar preguntas abiertas.
5. Indicar qué datos mejorarían más la estimación.

Usar una aclaración como:

```markdown
La siguiente estimación es preliminar y depende fuertemente de confirmar cantidades, recursos, calendario laboral y restricciones de obra.
```

---

## Qué evitar

No hacer lo siguiente:

- presentar el cronograma como definitivo;
- inventar cantidades exactas sin base;
- ocultar supuestos;
- dar duraciones precisas sin justificar;
- crear una lista de tareas sin estimación de esfuerzo;
- usar fechas si no hay fecha de inicio;
- generar JSON/CSV/Gantt por defecto;
- asumir que toda obra es obra nueva;
- ignorar lead times de compras críticas;
- ignorar restricciones de acceso, acopio o trabajo en edificio habitado;
- hacer análisis legal, contractual o pericial.

---

## Checklist final

Antes de terminar, verificar que la respuesta incluya:

- [ ] Resumen del alcance interpretado.
- [ ] WBS/EAP preliminar.
- [ ] Tabla de cronograma preliminar.
- [ ] Tabla de estimación de esfuerzo.
- [ ] Supuestos principales.
- [ ] Riesgos y puntos críticos.
- [ ] Preguntas abiertas.
- [ ] Niveles de confianza.
- [ ] Separación entre datos informados y supuestos.
- [ ] Duraciones justificadas.
- [ ] Ninguna precisión falsa.

---
name: minuta-reunion-obra
description: Usar este skill cuando el usuario quiera convertir una transcripción, notas sueltas, audio transcripto, resumen informal, agenda o apuntes de una reunión de obra en una minuta clara, profesional y accionable en español. El skill estructura la información en un template de minuta de obra con datos de reunión, asistentes, temas tratados, acuerdos, decisiones, responsables, fechas compromiso, riesgos, pendientes y próxima reunión. No usar para reemplazar actas formales, órdenes de servicio, notas de pedido, partes diarios, reclamos contractuales, peritajes ni documentos legales sin revisión profesional.
---

---

# Skill: minuta-reunion-obra

## Objetivo

Este skill transforma notas, transcripciones o apuntes desordenados de una reunión de obra en una **minuta de obra clara, estructurada y accionable**.

El objetivo es ayudar a documentar lo conversado, ordenar decisiones, dejar trazabilidad de acuerdos y convertir conversaciones informales en próximos pasos concretos.

El objetivo no es reemplazar un acta formal, una orden de servicio, una nota contractual ni otro documento de obra que requiera validación profesional o canal formal específico.

El resultado debe servir para:

- registrar los temas tratados;
- resumir el estado de la obra;
- dejar por escrito acuerdos y decisiones;
- identificar responsables;
- asignar fechas compromiso;
- ordenar pendientes;
- detectar riesgos, interferencias o bloqueos;
- preparar el seguimiento de la próxima reunión.

El output por defecto debe ser en **Markdown**, en español, y debe incluir:

1. Datos de la reunión.
2. Objetivo de la reunión.
3. Asistentes.
4. Resumen ejecutivo.
5. Temas tratados.
6. Acuerdos y decisiones.
7. Compromisos y próximos pasos.
8. Riesgos, bloqueos e interferencias.
9. Temas a formalizar o confirmar.
10. Próxima reunión.
11. Información faltante.

No generar JSON, actas legales, órdenes de servicio, notas de pedido ni documentos contractuales adicionales salvo que el usuario lo pida explícitamente.

Si el skill se usa desde CLI y el usuario no indica otro destino, guardar además el resultado en una carpeta con fecha y título descriptivo. Si el skill se usa desde chat, alcanza con responder en el chat salvo que el usuario pida guardar archivos.

En este entorno de agente por terminal con respuesta en chat, tratar el uso como `CLI + chat`: salvo que el usuario pida explícitamente solo respuesta en el chat, guardar el archivo en `outputs/` y además mostrar o resumir el resultado en la conversación.

Convención sugerida para CLI:

- carpeta: `outputs/YYYY-MM-DD-titulo-breve/`
- archivo principal: `minuta-reunion-obra.md`
- usar un título breve, en minúsculas y con guiones;
- no inventar el título: derivarlo de la obra, cliente, fecha o tipo de reunión si esa información existe; si no existe, usar un título genérico prudente.

---

## Cuándo usar este skill

Usar este skill cuando el usuario pida cosas como:

- “Convertí esta transcripción en una minuta de obra”.
- “Ordená estas notas como minuta”.
- “Armá una minuta de reunión de obra”.
- “Pasá estos apuntes a un formato profesional”.
- “Sacá acuerdos, responsables y pendientes de esta reunión”.
- “Hacé una minuta clara para enviar al equipo”.
- “Estructurá esta reunión de seguimiento de obra”.
- “Transformá este audio transcripto en una minuta”.
- “Resumí esta reunión de obra con próximos pasos”.

También usarlo si el usuario entrega alguno de estos inputs:

- transcripción de reunión;
- notas tomadas durante una visita de obra;
- apuntes de WhatsApp o email;
- resumen oral desordenado;
- agenda con comentarios;
- lista de temas tratados;
- reporte de reunión semanal;
- conversación entre dirección de obra, contratista, comitente, inspección, jefe de obra o subcontratistas.

---

## Cuándo no usar este skill

No usar este skill para:

- reemplazar un Acta de Inicio de Obra;
- reemplazar un Acta de Medición;
- reemplazar un Parte Diario;
- emitir una Orden de Servicio;
- redactar una Nota de Pedido formal;
- emitir instrucciones contractuales definitivas;
- analizar responsabilidades legales;
- preparar reclamos de plazo o costo;
- realizar peritajes;
- certificar avances de obra;
- validar técnicamente una solución constructiva;
- aprobar cambios de proyecto, precio o plazo sin revisión profesional.

Si en la transcripción aparecen temas contractuales, reclamos, adicionales, cambios de plazo, multas, paralizaciones, instrucciones formales o disputas, la minuta puede registrarlos como **tema tratado** o **punto a formalizar**, pero no debe convertirlos en una orden, reclamo o aprobación contractual.

Usar una frase como:

```markdown
Este punto debería formalizarse por el canal correspondiente según el contrato o la documentación de obra aplicable.
```

---

## Principios de trabajo

Seguir siempre estos principios:

1. **Primero entender el contexto de la reunión.**
   Antes de redactar la minuta, identificar obra, objetivo, participantes y foco principal.

2. **No inventar acuerdos.**
   Solo registrar acuerdos, decisiones o responsables si surgen claramente del input.

3. **Separar hechos de interpretaciones.**
   Si algo es una inferencia, marcarlo como “interpretado” o “a confirmar”.

4. **Convertir conversación en seguimiento.**
   La minuta debe dejar claro qué se habló, qué se decidió, quién debe hacer qué y para cuándo.

5. **Mantener tono profesional y claro.**
   No usar lenguaje excesivamente legalista ni demasiado informal.

6. **Respetar la trazabilidad.**
   Identificar temas, responsables, fechas, pendientes y bloqueos.

7. **No borrar tensiones relevantes.**
   Si hubo desacuerdos, riesgos o temas no resueltos, registrarlos de forma neutral.

8. **No sobrecargar la minuta.**
   Resumir lo importante. No transcribir palabra por palabra salvo que el usuario lo pida.

9. **Marcar información faltante.**
   Si faltan fecha, obra, asistentes, responsables o plazos, dejarlo indicado con `[PENDIENTE]`.

10. **Mantener el output simple y útil.**
   La respuesta principal debe servir para seguimiento, no para replicar toda la conversación original.

---

## Flujo de trabajo obligatorio

Cuando uses este skill, seguí este flujo:

1. Leer todo el input.
2. Identificar la obra o proyecto.
3. Identificar fecha, lugar, modalidad y participantes si están disponibles.
4. Detectar el objetivo de la reunión.
5. Extraer temas tratados.
6. Separar acuerdos, decisiones y pendientes.
7. Identificar responsables y fechas compromiso.
8. Detectar riesgos, bloqueos o interferencias.
9. Detectar temas que requieren formalización.
10. Redactar la minuta con el template obligatorio.
11. Agregar una sección de información faltante o puntos a confirmar.

No pedir información adicional antes de generar una primera versión, salvo que el input sea imposible de interpretar. Si faltan datos, completar con `[PENDIENTE]` y aclarar cuando algo quede sujeto a confirmación.

---

## Formato de respuesta obligatorio

La respuesta debe seguir esta estructura:

```markdown
# Minuta de reunión de obra

## 1. Datos de la reunión

## 2. Objetivo de la reunión

## 3. Asistentes

## 4. Resumen ejecutivo

## 5. Temas tratados

## 6. Acuerdos y decisiones

## 7. Compromisos y próximos pasos

## 8. Riesgos, bloqueos e interferencias

## 9. Temas a formalizar o confirmar

## 10. Próxima reunión

## 11. Información faltante
```

Si se usa desde CLI y se guarda archivo, el contenido del archivo principal debe seguir la misma estructura.

---

## 1. Datos de la reunión

Incluir una tabla con los datos básicos.

```markdown
## 1. Datos de la reunión

| Campo                | Detalle                                                                  |
| -------------------- | ------------------------------------------------------------------------ |
| Obra / Proyecto      | [PENDIENTE]                                                              |
| Fecha                | [PENDIENTE]                                                              |
| Hora                 | [PENDIENTE]                                                              |
| Lugar / Modalidad    | [PENDIENTE]                                                              |
| Tipo de reunión      | Seguimiento de obra / coordinación / visita / técnica / seguridad / otra |
| Minuta preparada por | [PENDIENTE]                                                              |
| Versión              | Borrador                                                                 |
```

Si el usuario informa el tipo de reunión, usarlo. Si no, inferirlo con prudencia.

Tipos habituales:

- reunión de seguimiento semanal;
- reunión de coordinación de obra;
- reunión técnica;
- reunión con subcontratistas;
- reunión de seguridad e higiene;
- visita de obra;
- reunión con comitente;
- reunión de avance;
- reunión de cierre de pendientes.

---

## 2. Objetivo de la reunión

Resumir en 1 a 3 líneas el propósito principal de la reunión.

Ejemplo:

```markdown
## 2. Objetivo de la reunión

Revisar el avance semanal de la obra, identificar interferencias entre rubros, definir responsables para los pendientes críticos y coordinar las tareas previstas para la próxima semana.
```

Si no surge claramente, escribir:

```markdown
El objetivo no fue informado explícitamente. Por el contenido de las notas, se interpreta que la reunión estuvo orientada al seguimiento de avance y coordinación de pendientes. Confirmar si corresponde otro foco.
```

---

## 3. Asistentes

Usar una tabla.

```markdown
## 3. Asistentes

| Nombre       | Rol / Empresa         | Estado       |
| ------------ | --------------------- | ------------ |
| [PENDIENTE] | Dirección de obra     | Presente     |
| [PENDIENTE] | Contratista principal | Presente     |
| [PENDIENTE] | Comitente             | [PENDIENTE]  |
```

Si la transcripción menciona personas pero no roles, no inventarlos. Usar `[PENDIENTE]` en la columna correspondiente.

Si se mencionan ausentes relevantes, incluirlos.

---

## 4. Resumen ejecutivo

Incluir un resumen breve, claro y accionable.

Debe tener entre 3 y 6 bullets.

Ejemplo:

```markdown
## 4. Resumen ejecutivo

- Se revisó el avance de albañilería, instalaciones y terminaciones.
- Se detectaron interferencias entre instalación eléctrica y revoques en el sector de planta alta.
- Se acordó priorizar la liberación de baños para permitir el ingreso del colocador de revestimientos.
- Quedaron pendientes definiciones de carpinterías y aprobación de muestras de piso.
- La próxima reunión deberá revisar el cumplimiento de los compromisos asignados.
```

---

## 5. Temas tratados

Organizar los temas por bloque. No copiar la conversación completa.

Usar secciones como:

```markdown
## 5. Temas tratados

### 5.1 Avance de obra

### 5.2 Planificación y próximas tareas

### 5.3 Materiales y suministros

### 5.4 Interferencias entre rubros

### 5.5 Calidad y observaciones técnicas

### 5.6 Seguridad e higiene

### 5.7 Cambios de alcance, adicionales o definiciones pendientes

### 5.8 Documentación, planos y aprobaciones
```

Eliminar o combinar secciones si no aplican.

Para cada tema, usar bullets breves:

```markdown
### 5.1 Avance de obra

- Se informó avance en mampostería interior.
- La instalación sanitaria se encuentra iniciada en baños y cocina.
- Los revoques no pueden avanzar en sectores donde todavía faltan pruebas de instalaciones.
```

---

## 6. Acuerdos y decisiones

Incluir una tabla solo con acuerdos claros.

```markdown
## 6. Acuerdos y decisiones

| ID   | Acuerdo / Decisión                                                                   | Responsable                        | Fecha objetivo | Observaciones                               |
| ---- | ------------------------------------------------------------------------------------ | ---------------------------------- | -------------- | ------------------------------------------- |
| D-01 | Priorizar la finalización de instalaciones en baños antes de iniciar revestimientos. | Contratista / Instalador sanitario | [PENDIENTE]    | Requiere coordinación con dirección de obra |
```

Reglas:

- No inventar acuerdos.
- Si una decisión no tiene responsable asignado de forma clara, escribir `[PENDIENTE]` o “No asignado”, según corresponda.
- Si no hay fecha, escribir `[PENDIENTE]`.
- Si hubo desacuerdo, no presentarlo como acuerdo.

Si no hay acuerdos claros:

```markdown
No se identificaron acuerdos explícitos en la transcripción. Se listan los pendientes detectados en la sección de compromisos y próximos pasos.
```

---

## 7. Compromisos y próximos pasos

Esta es una sección obligatoria.

Usar una tabla orientada a seguimiento.

```markdown
## 7. Compromisos y próximos pasos

| ID   | Tarea / Compromiso                                     | Responsable                   | Fecha límite | Estado    | Fuente / Comentario                       |
| ---- | ------------------------------------------------------ | ----------------------------- | ------------ | --------- | ----------------------------------------- |
| A-01 | Enviar definición de carpinterías exteriores.          | Comitente / Dirección de obra | [PENDIENTE] | Pendiente | Se mencionó como bloqueo para fabricación |
| A-02 | Completar prueba hidráulica antes de cerrar canaletas. | Instalador sanitario          | [PENDIENTE] | Pendiente | Necesario antes de revoques               |
```

Reglas:

- Cada acción debe tener un verbo claro.
- Cada acción debe tener un responsable.
- Cada acción debe tener fecha límite o `[PENDIENTE]`.
- No escribir acciones ambiguas como “ver tema pisos”.
- Convertirlas en algo accionable: “Definir modelo de piso y enviar aprobación al proveedor”.

Estados sugeridos:

- Pendiente;
- En curso;
- Bloqueado;
- Resuelto;

Si el estado no surge del input, usar `[PENDIENTE]`.

---

## 8. Riesgos, bloqueos e interferencias

Registrar riesgos o bloqueos que puedan afectar plazo, costo, calidad, seguridad o coordinación.

```markdown
## 8. Riesgos, bloqueos e interferencias

| ID   | Riesgo / Bloqueo                            | Impacto posible                             | Responsable de seguimiento    | Acción sugerida                                     |
| ---- | ------------------------------------------- | ------------------------------------------- | ----------------------------- | --------------------------------------------------- |
| R-01 | Falta de definición de carpinterías.        | Puede demorar fabricación y cierre de obra. | Dirección de obra / Comitente | Definir proveedor, medidas y fecha de entrega.      |
| R-02 | Instalaciones sin prueba antes de revoques. | Riesgo de retrabajos.                       | Instalador / Contratista      | Programar prueba y dejar constancia antes de tapar. |
```

Si no se mencionan riesgos:

```markdown
No se identificaron riesgos explícitos en las notas recibidas.
```

---

## 9. Temas a formalizar o confirmar

Esta sección es importante en contexto de obra.

Usarla para separar la minuta de los documentos formales.

Incluir temas como:

- cambios de alcance;
- adicionales;
- modificaciones de proyecto;
- aprobaciones de precio;
- ampliaciones de plazo;
- instrucciones de dirección de obra;
- reclamos;
- paralizaciones;
- recepción de trabajos;
- mediciones;
- aprobación de materiales;
- cambios que deberían documentarse por Orden de Servicio, Nota de Pedido, Acta, Parte Diario u otro canal formal según corresponda.

Ejemplo:

```markdown
## 9. Temas a formalizar o confirmar

| ID   | Tema                                               | Motivo                                  | Canal sugerido                                                | Estado      |
| ---- | -------------------------------------------------- | --------------------------------------- | ------------------------------------------------------------- | ----------- |
| F-01 | Cambio de modelo de revestimiento en baños.        | Puede afectar costo, plazo o provisión. | A formalizar según contrato / aprobación de dirección de obra | [PENDIENTE] |
| F-02 | Solicitud de adicional por demolición no prevista. | Posible impacto económico.              | A canalizar por el medio contractual correspondiente          | [PENDIENTE] |
```

No afirmar que un canal específico es obligatorio salvo que el usuario haya informado el contrato o normativa aplicable.

Usar fórmulas prudentes:

```markdown
Debe validarse si corresponde formalizar este punto por Orden de Servicio, Nota de Pedido, Acta u otro medio previsto en la documentación contractual.
```

---

## 10. Próxima reunión

Registrar fecha, hora, lugar y foco de la próxima reunión si fueron informados.

```markdown
## 10. Próxima reunión

| Campo             | Detalle                                                                                                                           |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Fecha             | [PENDIENTE]                                                                                                                       |
| Hora              | [PENDIENTE]                                                                                                                       |
| Lugar / Modalidad | [PENDIENTE]                                                                                                                       |
| Temas sugeridos   | Revisión de compromisos abiertos, avance de instalaciones, definición de carpinterías y liberación de sectores para terminaciones |
```

Si no fue definida, sugerir temas de seguimiento sin inventar fecha.

---

## 11. Información faltante

Listar datos que faltan para cerrar mejor la minuta.

```markdown
## 11. Información faltante

- Fecha y hora de la reunión.
- Nombre de la obra.
- Lista completa de asistentes y roles.
- Fechas compromiso para varias acciones.
- Responsable asignado para algunos pendientes.
- Confirmación de si determinados cambios requieren formalización contractual.
```

---

## Estilo de redacción

Usar un tono:

- claro;
- profesional;
- neutral;
- concreto;
- sin exceso de jerga;
- orientado a seguimiento;
- apto para compartir con comitente, dirección de obra, contratista o equipo técnico.

Evitar:

- lenguaje agresivo;
- atribución de culpas;
- opiniones no solicitadas;
- conclusiones legales;
- afirmaciones técnicas no sustentadas;
- frases ambiguas.

Preferir:

```markdown
Se informó que...
Se acordó...
Quedó pendiente...
Se solicita confirmar...
Se identifica como riesgo...
Debe validarse...
```

Evitar:

```markdown
El contratista incumplió...
La dirección de obra aprobó...
El comitente aceptó pagar...
Se ordena ejecutar...
```

Salvo que esas frases estén explícitamente en el input y corresponda mantenerlas como cita o registro.

---

## Manejo de transcripciones largas

Si el input es una transcripción larga:

1. No resumir todo de forma lineal.
2. Agrupar por tema.
3. Extraer decisiones y acciones.
4. Eliminar repeticiones.
5. Mantener desacuerdos relevantes.
6. No incluir conversaciones sociales o irrelevantes.
7. Si hay contradicciones, marcarlas como punto a confirmar.

Ejemplo:

```markdown
Se detectan versiones distintas sobre la fecha de entrega de carpinterías. Queda como punto a confirmar con proveedor y contratista.
```

---

## Manejo de información incierta

Si una persona, fecha, responsable o decisión no está clara, usar:

- `[PENDIENTE]`.
- “Responsable no asignado”.
- “Fecha no definida”.
- “Interpretado a partir de la transcripción”.

No completar con datos inventados.

---

## Diferencia entre minuta y documentación formal de obra

La minuta ordena lo conversado en una reunión y ayuda al seguimiento.

No reemplaza:

- Acta de Inicio de Obra;
- Acta de Medición;
- Acta de Recepción;
- Parte Diario;
- Orden de Servicio;
- Nota de Pedido;
- Libro de Obra;
- documentación contractual;
- certificaciones;
- aprobaciones formales.

Cuando un punto parezca tener impacto contractual, económico, técnico o de plazo, registrarlo como **tema a formalizar o confirmar**.

---

## Template compacto opcional

Si el usuario pide una versión breve, usar este formato:

```markdown
# Minuta de reunión de obra

## Datos

- Obra:
- Fecha:
- Asistentes:
- Tipo de reunión:

## Resumen

-

## Temas tratados

-

## Acuerdos

| Acuerdo | Responsable | Fecha |
| ------- | ----------- | ----- |

## Próximos pasos

| Tarea | Responsable | Fecha límite | Estado |
| ----- | ----------- | ------------ | ------ |

## Riesgos / Bloqueos

-

## Puntos a confirmar

-
```

---

## Checklist final

Antes de entregar la minuta, verificar:

- [ ] Tiene datos básicos de reunión.
- [ ] Distingue asistentes, temas, acuerdos y acciones.
- [ ] Cada acción tiene responsable o “No asignado”.
- [ ] Cada acción tiene fecha o `[PENDIENTE]`.
- [ ] No inventa acuerdos.
- [ ] No transforma comentarios informales en órdenes contractuales.
- [ ] Incluye riesgos o bloqueos si aparecen.
- [ ] Incluye temas a formalizar si hay impacto en plazo, costo, alcance o contrato.
- [ ] Usa tono neutral y profesional.
- [ ] La minuta puede compartirse con el equipo sin depender de la transcripción original.

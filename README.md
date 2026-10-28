# GORVET Creative Director

Agencia creativa visual de **Juank de Gorvet**, basada en el Método G.O.R.V.E.T. y en el libro *Luces, Cámara, ¡Prompt!*. Se centra en diseño y dirección creativa visual con IA, sin planificación de marketing. Funciona como complemento de skills para ChatGPT y Claude: es solo texto, no necesita Python ni ejecutar código.

## Un skill, diez playbooks

El complemento tiene **un único skill visible**, `gorvet-creative-director`. Las especialidades viven dentro de él como playbooks que el director lee solo cuando el encargo los necesita. No se activan por su cuenta, no se enlazan entre sí y no abren aprobaciones ni producción propias. Así una sola mente decide la escena y escribe el prompt.

```
skills/gorvet-creative-director/
  SKILL.md                     skill único: método, recorrido y mapa de playbooks
  references/
    direccion/                 reglas del director: brief, ficha de producción, protocolo, rúbrica
    compartido/                criterios usados por varios: jerarquía, QA anti-IA, multilingüe/RTL, depuración
    luces/                     el libro: 28 bibliotecas + playbook de compilación del prompt
    estrategia/  arte/  fotografia/  cartel/
    identidad/   series/  video/  critica/  qa-prompts/
```

| Playbook | Responsabilidad |
| --- | --- |
| `estrategia` | Concepto visual, mensaje y selección editorial (qué va en la imagen, qué en el apoyo). |
| `arte` | Medio, escena, color, acabado y esquema global de masas. |
| `fotografia` | Captura: encuadre, luz, foco, materiales e integración. |
| `cartel` | Composición gráfica, tipografía y jerarquía. |
| `identidad` | Identidad, logotipos, referencias, protección y memoria de proyecto. |
| `series` | Conjuntos de piezas, carruseles, storyboards y continuidad. |
| `video` | Acción temporal, planos, cámara, montaje y sonido. |
| `luces` | El libro y la compilación del prompt final. |
| `qa-prompts` | Depurar un prompt existente sin perder controles. |
| `critica` | Juzgar la salida real y dirigir la corrección. |

## Cómo trabaja

1. El director [recibe el brief](skills/gorvet-creative-director/references/direccion/BRIEF_INTAKE.md) y pregunta solo lo que cambia el resultado.
2. Decide el contenido, el concepto y el diseño concreto (posiciones, escalas, textos literales).
3. Rellena la [ficha de producción](skills/gorvet-creative-director/references/direccion/PRODUCTION_GATE.md) en el chat y escribe el prompt desde ella. No se envía el brief ni un prompt genérico al generador.
4. Muestra dirección y prompt completo para aprobarlos (salvo ejecución directa expresa) y envía exactamente ese texto.
5. Inspecciona la imagen real con la [rúbrica](skills/gorvet-creative-director/references/direccion/SCORING_RUBRIC.md) y corrige el origen del fallo. Un máximo de dos correcciones por defecto.

El recorrido se adapta al entregable: una crítica empieza por la imagen, un prompt resuelto va a depuración, un conjunto necesita relaciones entre piezas. Ver [cadenas de trabajo](skills/gorvet-creative-director/references/direccion/WORKFLOW_CHAINS.md).

El paquete exige este comportamiento mediante instrucciones; no intercepta herramientas del host ni garantiza que el generador obedezca. Una revisión textual no valida la imagen.

## Descarga e instalación

El paquete de esta versión es `gorvet-creative-suite-3.0.0.zip`, con manifiesto, el skill, sus playbooks, icono y licencia. Los paquetes publicados aparecen en [GitHub Releases](https://github.com/gorvet/gorvet-creative-suite/releases). Importa el ZIP completo en una aplicación compatible con complementos o Agent Skills; la aplicación decide su ubicación y activación. Conserva la carpeta `references/` junto a `SKILL.md`. Abre una sesión nueva si el host conserva instrucciones anteriores.

## Migración desde 2.x

La versión 3.0 reestructura sin borrar contenido del libro: los diez skills especialistas pasan a ser playbooks dentro de `gorvet-creative-director`, y los scripts de Python, sus pruebas y el contrato JSON se eliminan. La historia está en Git.

## Distribución

Tras confirmar los cambios, ejecuta `./scripts/build-release.ps1` en PowerShell. Genera el ZIP y `SHA256SUMS.txt` en `dist/` desde el commit actual. Al subir una etiqueta como `v3.0.0`, `.github/workflows/release.yml` comprueba que coincide con `plugin.json`, genera el ZIP y crea la Release.

## Licencia

Consulta [LICENSE](LICENSE). La documentación de [fuentes](skills/gorvet-creative-director/references/direccion/SOURCES.md) identifica los proyectos estudiados; no se incluye el documento privado del libro ni se han importado repositorios externos.

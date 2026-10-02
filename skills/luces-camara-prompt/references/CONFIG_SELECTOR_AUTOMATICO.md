# SELECTOR AUTOMÁTICO

Aplicar el selector a las solicitudes visuales sin añadir detalles de implementación innecesarios. Su contenido es público y puede explicarse cuando el usuario lo solicite.

## A. Estado de la solicitud
### IDEA_ABIERTA
El usuario no sabe exactamente qué imagen quiere.
- proponer escenas;
- inferir estilo, luz, plano, atmósfera y ratio;
- presentar propuesta antes del prompt.

### IDEA_SEMIDEFINIDA
Existe intención, pero faltan decisiones.
- preservar intención;
- completar lenguaje visual;
- no cambiar el concepto sin necesidad.

### DIRECCION_CERRADA
El usuario ya define la escena.
- optimizar jerarquía, consistencia y técnica;
- no reinterpretar lo que ya está decidido.

## B. Tipo principal
Clasificar:
- RETRATO
- MARCA_PERSONAL
- PRODUCTO
- GASTRONOMIA_BEBIDA
- MODA_LIFESTYLE
- PUBLICIDAD_CAMPANA
- CARTEL_PORTADA
- MOCKUP
- LOGO_SIMBOLO
- CONCEPTUAL_SURREAL
- ARQUITECTURA_INTERIOR
- BOCETO_RENDER
- BOCETO_IMAGEN
- TEXTURA_PBR
- PROTOTIPO
- RETOQUE_COMPOSICION
- RESTAURACION
- EDITORIAL_INTIMO

## C. Referencias
Clasificar cada referencia por función:
- IDENTIDAD
- PRODUCTO_BRANDING
- POSE
- ENCUADRE
- COMPOSICION
- VESTUARIO
- ENTORNO
- ESTILO_MOOD
- BOCETO_GEOMETRIA
- IMAGEN_BASE_EDICION

## D. Bibliotecas
Siempre:
- `references/CORE_METODO_GORVET.md`
- `references/CORE_ESTRUCTURA_PROMPT.md`
- `references/CORE_ERRORES_REGLAS.md`

Según necesidad:
- técnica → módulos `TECHNICAL_*`;
- estilos → módulos `STYLES_*`;
- referencias → módulos `REFERENCES_*`;
- nichos → módulos `USE_CASES_*`;
- secuencias o campañas narrativas → `references/USE_CASES_ARTE_CONCEPTUAL_STORYTELLING.md`;
- refinamiento → `references/WORKFLOWS_ITERACION_DIAGNOSTICO.md`;
- salida final → `references/WORKFLOWS_CONTROL_CALIDAD.md`;
- sentencias reutilizables → `references/WORKFLOWS_PHRASE_BANK.md`;
- íntimo/editorial → `references/WORKFLOWS_EDITORIAL_INTIMO.md`.

## E. Densidad técnica
### SIMPLE
- escena cotidiana;
- técnica mínima;
- 1 estilo + luz + plano si aportan.

### MEDIA
Seleccionar según el encargo; no completar todos los elementos:
- estilo;
- iluminación;
- plano;
- profundidad;
- composición;
- materialidad cuando corresponda.

### AVANZADA
- producto/publicidad;
- múltiples referencias;
- render;
- retoque;
- continuidad;
- problemas técnicos concretos.

## F. Prioridades
1. intención;
2. sujeto/objeto prioritario;
3. propósito de referencia;
4. estilo dominante;
5. luz;
6. composición;
7. materialidad;
8. técnica;
9. microdetalle.

La categoría indica qué recursos considerar, no cuántos añadir. Producto o publicidad no exige por sí solo un prompt avanzado. La técnica no debe desplazar a la idea; aplicar «Construcción del prompt final» de `../SKILL.md`.

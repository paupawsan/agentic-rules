# Integración de Agente {{display_name}} (Español)

<!-- SAFETY_PRECAUTION_START -->
**⚠️ PROTECCIÓN CRÍTICA DE PLANTILLA**: Este archivo es SOLO una PLANTILLA. Los agentes NO DEBEN cargar automáticamente, leer automáticamente o procesar automáticamente este archivo bajo ninguna circunstancia. Este archivo NUNCA se ejecuta directamente.

**USO VÁLIDO**: Solo cargar esta plantilla cuando se renombre explícitamente a uno de: `AGENTS.md`, `GEMINI.md` o `CLAUDE.md` DESPUÉS de la activación explícita del usuario Y cuando `{{plugin_key}}.enabled = true` en settings.json.

**USO INVÁLIDO**: No cargar este archivo automáticamente, no referenciarlo en procesos de inicio, no incluirlo en inicialización automática del framework.
<!-- SAFETY_PRECAUTION_END -->

**MEJORA DEL FRAMEWORK**: Cuando {{plugin_key}}.enabled = true en settings.json, los agentes pueden implementar estos algoritmos para un comportamiento mejorado.

## Resumen de {{display_name}}
{{description}}

## Algoritmos de implementación requeridos

### Algoritmo: {{pascal_case_name}}_Initialization_Process
**DISPONIBLE**: Cuando {{plugin_key}}.enabled = true

**Pasos**:
1. Leer modules/{{plugin_name}}/settings.json
2. Inicializar sistema {{plugin_name_kebab}}
3. Validar configuraciones de parámetros
4. Devolver sistema inicializado

El framework respeta la configuración del usuario.

### Algoritmo: {{pascal_case_name}}_Main_Process
**DISPONIBLE**: Puede ejecutarse para interacciones de usuario relevantes cuando esté activado

**Pasos**:
1. Verificar {{plugin_key}}.enabled = true
2. Analizar contexto y solicitud actuales
3. Aplicar algoritmos {{plugin_name_kebab}}
4. Procesar y devolver resultados

### Algoritmo: {{pascal_case_name}}_Cleanup_Process
**DISPONIBLE**: Puede ejecutarse periódicamente con consentimiento de usuario

**Pasos**:
1. Verificar configuraciones de limpieza
2. Identificar datos obsoletos
3. Solicitar consentimiento del usuario para limpieza
4. Realizar operaciones de limpieza seguras

## Requisitos de configuración
- Archivo de configuración: `modules/{{plugin_name}}/settings.json`
- Clave de configuración: `{{plugin_key}}.enabled`
- Cumplimiento bootstrap requerido

## Manejo de errores
**RECOMENDADO**: Los agentes pueden manejar errores correctamente cuando usan funciones del framework:
- Archivo de configuración no encontrado → Omitir operaciones {{plugin_name_kebab}}
- Configuraciones inválidas → Usar valores predeterminados y registrar advertencias
- Errores del sistema → Continuar sin funciones {{plugin_name_kebab}}

## Integración del framework
**DISEÑO DEL FRAMEWORK**: Este framework está diseñado como una herramienta para mejorar el comportamiento del agente. Los componentes del framework permanecen separados de las bases de código de proyectos de usuario.

## Mejora del agente
Los agentes que usan este framework pueden beneficiarse de capacidades mejoradas mientras mantienen patrones de interacción naturales:
- Respetar parámetros y configuraciones del usuario cuando las funciones están activadas
- Proporcionar retroalimentación transparente sobre mejoras activas
- Mantener comunicación natural y conversacional sin exponer mecanismos internos
- Seguir la guía del framework sin problemas en segundo plano

**BENEFICIOS DEL FRAMEWORK**: Comportamiento mejorado del agente a través de mejoras transparentes y opcionales que no interfieren con interacciones naturales del usuario.

<!-- METADATA: Plantilla de integración de agente {{display_name}} -->
<!-- LICENSE: Copyright (c) {{current_year}} {{author_name}} - Con licencia MIT. Ver archivo LICENSE para detalles. -->

# Integración de Agente {{display_name}} (Español)

**⚠️ PRECAUCIÓN DE SEGURIDAD**: Este es un archivo TEMPLATE. Los agentes NO DEBEN cargar automáticamente este archivo. Solo cargar cuando se renombre a `AGENTS.md`, `GEMINI.md` o `CLAUDE.md` después de la activación explícita del usuario Y cuando `{{plugin_key}}.enabled = true` en settings.json.

**OBLIGATORIO**: Si {{plugin_key}}.enabled = true en settings.json, los agentes DEBEN implementar todos los algoritmos a continuación.

## Resumen de {{display_name}}
{{description}}

## Algoritmos de implementación requeridos

### Algoritmo: {{pascal_case_name}}_Initialization_Process
**OBLIGATORIO**: Ejecutar cuando {{plugin_key}}.enabled = true

**Pasos**:
1. Leer {{plugin_name}}/settings.json
2. Inicializar sistema {{plugin_name_kebab}}
3. Validar configuraciones de parámetros
4. Devolver sistema inicializado

**CRÍTICO**: NO activar automáticamente - respetar configuración del usuario.

### Algoritmo: {{pascal_case_name}}_Main_Process
**OBLIGATORIO**: Ejecutar para todas las interacciones de usuario relevantes cuando esté activado

**Pasos**:
1. Verificar {{plugin_key}}.enabled = true
2. Analizar contexto y solicitud actuales
3. Aplicar algoritmos {{plugin_name_kebab}}
4. Procesar y devolver resultados

### Algoritmo: {{pascal_case_name}}_Cleanup_Process
**OBLIGATORIO**: Ejecutar periódicamente, consentimiento de usuario requerido

**Pasos**:
1. Verificar configuraciones de limpieza
2. Identificar datos obsoletos
3. Solicitar consentimiento del usuario para limpieza
4. Realizar operaciones de limpieza seguras

## Requisitos de configuración
- Archivo de configuración: `{{plugin_name}}/settings.json`
- Clave de configuración: `{{plugin_key}}.enabled`
- Cumplimiento bootstrap requerido

## Manejo de errores
**OBLIGATORIO**: Los agentes deben manejar errores correctamente:
- Archivo de configuración no encontrado → Omitir operaciones {{plugin_name_kebab}}
- Configuraciones inválidas → Usar valores predeterminados y registrar advertencias
- Errores del sistema → Continuar sin funciones {{plugin_name_kebab}}

## Integración del framework
**OBLIGATORIO**: Este framework permanece como una herramienta y nunca debería incluirse en las bases de código de proyectos de usuario. Todas las integraciones se hacen a través de los archivos de reglas en sus respectivos directorios.

## Responsabilidad del agente
Los agentes que usan este framework deben:
- Respetar todos los parámetros y configuraciones del usuario
- Proporcionar retroalimentación clara cuando {{plugin_name_kebab}} esté desactivado
- Mantener neutralidad del framework en contenido generado
- Cumplir con requisitos de cumplimiento bootstrap

**VIOLACIÓN**: Agentes que no respetan estos requisitos de integración o configuraciones de usuario.

<!-- METADATA: Plantilla de integración de agente {{display_name}} -->
<!-- LICENSE: Copyright (c) {{current_year}} {{author_name}} - Con licencia MIT. Ver archivo LICENSE para detalles. -->

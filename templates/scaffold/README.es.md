# {{display_name}}

{{description}}

## Resumen

Este es un plugin personalizado para el framework Agentic Rules que proporciona funcionalidad {{plugin_name_kebab}} para agentes de IA.

## Características

- **Implementación de algoritmos**: Proporciona algoritmos estructurados para operaciones {{plugin_name_kebab}}
- **Gestión de configuración**: Configuraciones flexibles a través de `settings.json`
- **Soporte multilingüe**: Plantillas disponibles en múltiples idiomas
- **Integración framework**: Integración perfecta con el framework Agentic Rules

## Instalación

1. Copie este directorio de plugin a su framework agentic-rules
2. Agregue el nombre del plugin a `plugins.json` (opcional, para interfaz web)
3. Ejecute `python generate_simple_setup.py` para actualizar la configuración web
4. Active el plugin usando `python setup.py`

## Configuración

### Configuraciones básicas (`settings.json`)

```json
{
  "{{plugin_key}}": {
    "enabled": true,
    "config": {
      "example_setting": "example_value",
      "max_entries": 100,
      "cleanup_days": 90
    },
    "advanced": {
      "debug_mode": false,
      "performance_mode": "balanced"
    }
  }
}
```

### Descripción de configuraciones

- `enabled`: Habilitar/deshabilitar el plugin
- `config.max_entries`: Número máximo de entradas a mantener
- `config.cleanup_days`: Días para retener datos antes de limpieza
- `advanced.debug_mode`: Habilitar registro de depuración
- `advanced.performance_mode`: Modo de optimización de rendimiento

## Uso

1. **Habilitar el plugin**: Establezca `enabled: true` en `settings.json`
2. **Activar reglas**: Use `python setup.py` para generar archivos de reglas
3. **Integración**: Copie el archivo de reglas generado (ej. `AGENTS.md`) a su proyecto
4. **Configuración**: Personalice configuraciones en `{{plugin_name}}/settings.json`

## Algoritmos de reglas

Este plugin implementa los siguientes algoritmos:

### Proceso de inicialización {{pascal_case_name}}
- Inicializa el sistema {{plugin_name_kebab}}
- Valida configuración
- Configura estructuras de datos requeridas

### Proceso principal {{pascal_case_name}}
- Procesa interacciones de usuario
- Aplica lógica {{plugin_name_kebab}}
- Devuelve resultados procesados

### Proceso de limpieza {{pascal_case_name}}
- Realiza limpieza periódica
- Requiere consentimiento del usuario
- Mantiene integridad de datos

## Estructura de archivos

```
{{plugin_name}}/
├── README.md              # Esta documentación
├── RULES.md.en           # Plantilla de reglas en inglés
├── RULES.md.ja           # Plantilla japonesa (si se solicita)
├── RULES.md.id           # Plantilla indonesa (si se solicita)
├── settings.json         # Configuraciones predeterminadas
└── setup.json           # Configuración de interfaz web
```

## Desarrollo

### Agregar nuevos idiomas

1. Cree `RULES.md.{{language_code}}` con plantilla traducida
2. Agregue localización a `setup.json`
3. Actualice `settings.json` si es necesario

### Personalizar algoritmos

Edite los archivos `RULES.md.*` para modificar algoritmos y comportamiento.

### Pruebas

1. Habilite el plugin en configuraciones
2. Ejecute setup.py para generar archivos de reglas
3. Pruebe las reglas generadas en su agente de IA

## Solución de problemas

### Plugin no detectado
- Asegúrese de que el directorio del plugin existe
- Verifique que al menos un archivo `RULES.md.*` existe
- Verifique que `plugins.json` incluye el nombre del plugin (para interfaz web)

### Errores de configuración
- Verifique sintaxis `settings.json`
- Verifique que todas las configuraciones requeridas están presentes
- Asegúrese de que los permisos de archivos son correctos

### Fallo en activación de reglas
- Verifique que el plugin está habilitado en configuraciones
- Verifique que `setup.py` se completó exitosamente
- Asegúrese de que los archivos de reglas generados se copiaron correctamente

## Licencia

Copyright (c) {{current_year}} {{author_name}}

Con licencia MIT. Ver archivo LICENSE para detalles.

## Contribución

¡Las contribuciones son bienvenidas! Por favor:

1. Forkee el repositorio
2. Cree una rama de funcionalidad
3. Haga sus cambios
4. Pruebe exhaustivamente
5. Envíe un pull request

Para cambios mayores, abra un issue primero para discutir los cambios propuestos.

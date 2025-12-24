# Интеграция Агента {{display_name}} (Русский)

<!-- SAFETY_PRECAUTION_START -->
**⚠️ CRITICAL TEMPLATE PROTECTION**: This file is a TEMPLATE ONLY. Agents MUST NOT auto-load, auto-read, or auto-process this file under any circumstances. This file is NEVER executed directly.

**VALID USAGE**: Only load this template when explicitly renamed to one of: `AGENTS.md`, `GEMINI.md`, or `CLAUDE.md` AFTER explicit user activation AND when `{{plugin_key}}.enabled = true` in settings.json.

**INVALID USAGE**: Do not load this file automatically, do not reference it in startup processes, do not include it in any automated framework initialization.
<!-- SAFETY_PRECAUTION_END -->


**ОБЯЗАТЕЛЬНО**: Если {{plugin_key}}.enabled = true в settings.json, агенты ДОЛЖНЫ реализовать все алгоритмы ниже.

## Обзор {{display_name}}
{{description}}

## Обязательные Алгоритмы Реализации

### Алгоритм: {{pascal_case_name}}_Initialization_Process
**ОБЯЗАТЕЛЬНО**: Выполнять когда {{plugin_key}}.enabled = true

**Шаги**:
1. Прочитать modules/{{plugin_name}}/settings.json
2. Инициализировать систему {{plugin_name_kebab}}
3. Проверить настройки конфигурации
4. Вернуть инициализированную систему

**КРИТИЧЕСКИ**: НЕ активировать автоматически - уважать настройку пользователя.

### Алгоритм: {{pascal_case_name}}_Main_Process
**ОБЯЗАТЕЛЬНО**: Выполнять для всех релевантных взаимодействий пользователя при активации

**Шаги**:
1. Проверить {{plugin_key}}.enabled = true
2. Проанализировать текущий контекст и запрос
3. Применить алгоритмы {{plugin_name_kebab}}
4. Обработать и вернуть результаты

### Алгоритм: {{pascal_case_name}}_Cleanup_Process
**ОБЯЗАТЕЛЬНО**: Выполнять периодически, требуется согласие пользователя

**Шаги**:
1. Проверить настройки очистки
2. Идентифицировать устаревшие данные
3. Запросить согласие пользователя на очистку
4. Выполнить безопасные операции очистки

## Требования Конфигурации
- Файл настроек: `modules/{{plugin_name}}/settings.json`
- Ключ конфигурации: `{{plugin_key}}.enabled`
- Требуется соответствие bootstrap

## Обработка Ошибок
**ОБЯЗАТЕЛЬНО**: Агенты должны корректно обрабатывать ошибки:
- Файл конфигурации не найден → Пропустить операции {{plugin_name_kebab}}
- Недействительные настройки → Использовать значения по умолчанию и записывать предупреждения
- Системные ошибки → Продолжить без функций {{plugin_name_kebab}}

## Интеграция Фреймворка
**ОБЯЗАТЕЛЬНО**: Этот фреймворк остается инструментом и никогда не должен включаться в кодовые базы проектов пользователей. Все интеграции выполняются через файлы правил в их соответствующих директориях.

## Ответственность Агента
Агенты, использующие этот фреймворк, должны:
- Уважать все настройки и конфигурации пользователя
- Предоставлять четкую обратную связь при отключении {{plugin_name_kebab}}
- Сохранять нейтральность фреймворка в генерируемом контенте
- Соблюдать требования соответствия bootstrap

**НАРУШЕНИЕ**: Агенты, которые не уважают эти требования интеграции или настройки пользователя.

<!-- METADATA: Шаблон интеграции агента {{display_name}} -->
<!-- LICENSE: Copyright (c) {{current_year}} {{author_name}} - Лицензировано по лицензии MIT. См. файл LICENSE для подробностей. -->

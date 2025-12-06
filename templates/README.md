# Agentic Rules Framework - Templates Branch

This branch contains the template structure for localization and scaffolding in the Agentic Rules Framework.

## Purpose

The Templates branch serves as a central repository for:
- **Language-specific templates** for rule generation
- **Localization templates** for UI and configuration
- **Scaffold templates** used by `generate_plugin_scaffold.py`
- **Extensible structure** for adding new supported languages

## Branch Structure

```
templates/
├── README.md                    # This documentation
├── rules/                       # Rule templates by language
│   ├── RULES.md.template       # Generic template with placeholders
│   ├── RULES.md.en             # English rule template
│   ├── RULES.md.ja             # Japanese rule template
│   └── RULES.md.id             # Indonesian rule template
├── localization/               # Localization templates
│   └── plugin_localization.template.json
└── scaffold/                   # Scaffold component templates
    ├── settings.json.template  # Plugin settings template
    ├── setup.json.template     # Web interface config template
    └── README.md.template      # Plugin documentation template
```

## Template Variables

Templates use the following placeholder variables:

### Common Variables
- `{{plugin_name}}` - Plugin directory name (e.g., "my-plugin")
- `{{plugin_key}}` - Plugin settings key (e.g., "my_plugin")
- `{{plugin_name_kebab}}` - Plugin name in kebab-case (e.g., "my-plugin")
- `{{display_name}}` - Human-readable plugin name (e.g., "My Plugin")
- `{{description}}` - Plugin description
- `{{author_name}}` - Author name placeholder
- `{{current_year}}` - Current year for copyright
- `{{creation_timestamp}}` - ISO timestamp for creation

### Language-Specific Variables
- `{{language_name}}` - Full language name (e.g., "English", "日本語")
- `{{language_code}}` - Language code (e.g., "en", "ja", "id")
- `{{native_language_name}}` - Native language name
- `{{pascal_case_name}}` - Plugin name in PascalCase

## Usage

### For generate_plugin_scaffold.py

The scaffold generator uses these templates to create new plugins:

1. **Rule Templates**: `templates/rules/RULES.md.{lang}` for each requested language
2. **Settings Template**: `templates/scaffold/settings.json.template`
3. **Setup Template**: `templates/scaffold/setup.json.template`
4. **README Template**: `templates/scaffold/README.md.template`

### Adding New Languages

To add support for a new language:

1. **Create Rule Template**: Add `templates/rules/RULES.md.{code}` with translated content
2. **Update Language Table**: Modify `generate_plugin_scaffold.py` language table
3. **Add Localization**: Create language-specific localization entries
4. **Test Generation**: Verify plugin scaffold works with new language

## Supported Languages

### Core Languages (Full Templates)
- **English (en)**: Complete rule templates and documentation
- **Japanese (ja)**: Complete rule templates and documentation
- **Indonesian (id)**: Complete rule templates and documentation

### Validation-Only Languages
- **Chinese (zh)**: Language code validation, placeholder templates
- **All ISO 639-1 codes**: 150+ languages supported for validation

## Maintenance

### Template Updates
- Keep templates synchronized across languages
- Update copyright years and placeholders as needed
- Maintain consistent structure and formatting

### Language Additions
- Follow existing template structure
- Include proper translations for all sections
- Test with `generate_plugin_scaffold.py`

### Quality Assurance
- Validate all templates have required placeholders
- Test template rendering with various plugin names
- Ensure generated files are syntactically correct

## Integration with Main Branch

This Templates branch provides the foundation that `generate_plugin_scaffold.py` uses in the main branch. Changes here should be carefully coordinated with the main branch implementation.

## Contributing

When contributing to templates:

1. Maintain backward compatibility
2. Follow existing placeholder conventions
3. Test with multiple plugin configurations
4. Update this README for any structural changes

---

**Note**: This branch is not meant to be merged into main. It serves as a template repository for the framework's scaffolding system.

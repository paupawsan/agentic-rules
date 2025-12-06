# {{display_name}}

{{description}}

## Übersicht

Dies ist ein benutzerdefiniertes Plugin für das Agentic Rules Framework, das {{plugin_name_kebab}} Funktionalität für KI-Agenten bereitstellt.

## Funktionen

- **Algorithmus-Implementierung**: Bietet strukturierte Algorithmen für {{plugin_name_kebab}} Operationen
- **Konfigurationsmanagement**: Flexible Einstellungen über `settings.json`
- **Mehrsprachige Unterstützung**: Vorlagen in mehreren Sprachen verfügbar
- **Framework-Integration**: Nahtlose Integration mit dem Agentic Rules Framework

## Installation

1. Kopieren Sie dieses Plugin-Verzeichnis in Ihr agentic-rules Framework
2. Fügen Sie den Plugin-Namen zu `plugins.json` hinzu (optional, für Weboberfläche)
3. Führen Sie `python generate_simple_setup.py` aus, um die Webkonfiguration zu aktualisieren
4. Aktivieren Sie das Plugin mit `python setup.py`

## Konfiguration

### Grundlegende Einstellungen (`settings.json`)

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

### Einstellungsbeschreibung

- `enabled`: Plugin aktivieren/deaktivieren
- `config.max_entries`: Maximale Anzahl der zu verwaltenden Einträge
- `config.cleanup_days`: Tage zur Datenspeicherung vor Bereinigung
- `advanced.debug_mode`: Debug-Protokollierung aktivieren
- `advanced.performance_mode`: Leistungsoptimierungsmodus

## Verwendung

1. **Plugin aktivieren**: Setzen Sie `enabled: true` in `settings.json`
2. **Regeln aktivieren**: Verwenden Sie `python setup.py`, um Regeldaten zu generieren
3. **Integration**: Kopieren Sie die generierte Regeldaten (z.B. `AGENTS.md`) in Ihr Projekt
4. **Konfiguration**: Passen Sie Einstellungen in `{{plugin_name}}/settings.json` an

## Regelalgorithmen

Dieses Plugin implementiert die folgenden Algorithmen:

### {{pascal_case_name}} Initialisierungsprozess
- Initialisiert das {{plugin_name_kebab}} System
- Validiert Konfiguration
- Richtet erforderliche Datenstrukturen ein

### {{pascal_case_name}} Hauptprozess
- Verarbeitet Benutzerinteraktionen
- Wendet {{plugin_name_kebab}} Logik an
- Gibt verarbeitete Ergebnisse zurück

### {{pascal_case_name}} Bereinigungsprozess
- Führt periodische Bereinigung durch
- Erfordert Benutzereinwilligung
- Erhält Datenintegrität

## Dateistruktur

```
{{plugin_name}}/
├── README.md              # Diese Dokumentation
├── RULES.md.en           # Englische Regelvorlage
├── RULES.md.ja           # Japanische Vorlage (falls angefordert)
├── RULES.md.id           # Indonesische Vorlage (falls angefordert)
├── settings.json         # Standardeinstellungen
└── setup.json           # Weboberflächenkonfiguration
```

## Entwicklung

### Neue Sprachen hinzufügen

1. Erstellen Sie `RULES.md.{{language_code}}` mit übersetzter Vorlage
2. Fügen Sie Lokalisierung zu `setup.json` hinzu
3. Aktualisieren Sie `settings.json` falls erforderlich

### Algorithmen anpassen

Bearbeiten Sie die `RULES.md.*` Dateien, um Algorithmen und Verhalten zu ändern.

### Testen

1. Aktivieren Sie das Plugin in den Einstellungen
2. Führen Sie setup.py aus, um Regeldaten zu generieren
3. Testen Sie die generierten Regeln in Ihrem KI-Agenten

## Fehlerbehebung

### Plugin nicht erkannt
- Stellen Sie sicher, dass das Plugin-Verzeichnis existiert
- Überprüfen Sie, dass mindestens eine `RULES.md.*` Datei existiert
- Verifizieren Sie, dass `plugins.json` den Plugin-Namen enthält (für Weboberfläche)

### Konfigurationsfehler
- Überprüfen Sie die `settings.json` Syntax
- Verifizieren Sie, dass alle erforderlichen Einstellungen vorhanden sind
- Stellen Sie sicher, dass Dateiberechtigungen korrekt sind

### Regelaktivierung fehlgeschlagen
- Überprüfen Sie, dass das Plugin in den Einstellungen aktiviert ist
- Verifizieren Sie, dass `setup.py` erfolgreich abgeschlossen wurde
- Stellen Sie sicher, dass generierte Regeldaten korrekt kopiert wurden

## Lizenz

Copyright (c) {{current_year}} {{author_name}}

Lizenziert unter der MIT-Lizenz. Siehe LICENSE-Datei für Details.

## Mitwirkung

Beiträge sind willkommen! Bitte:

1. Forken Sie das Repository
2. Erstellen Sie einen Feature-Branch
3. Nehmen Sie Ihre Änderungen vor
4. Testen Sie gründlich
5. Reichen Sie einen Pull-Request ein

Bei größeren Änderungen öffnen Sie bitte zuerst ein Issue, um die vorgeschlagenen Änderungen zu besprechen.

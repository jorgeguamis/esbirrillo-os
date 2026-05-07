# 03. Sistema

Templates, configuración Obsidian, y archivos de sistema del vault.

## Estructura

```
03. Sistema/
├── templates/         ← templates Obsidian (Daily, Weekly, Reviews, Frameworks)
├── obsidian_config/   ← configuración del vault (opcional)
└── media/             ← excalidraw, boards, imágenes del sistema
```

## Templates incluidos

- `Daily Note.md` — daily journal (morning + evening)
- `Weekly Review.md` — review semanal
- `Monthly Review.md` — review mensual (check-in + portfolio)
- `Quarterly Review.md` — review trimestral
- `Annual Review.md` — review anual
- `Vivid Vision Framework - Template.md` — framework Vivid Vision
- `Life Map - Template.md` — Life Map de áreas vitales
- `Identity and Values Interview - Template.md` — entrevista identidad
- `Future Self Interview - Template.md` — entrevista yo futuro
- `Ideal Life Costing - Template.md` — coste de tu vida ideal
- `Hub Index.md` — índice tipo hub con Dataview
- `Source Note.md` — nota de fuente (libro, vídeo, artículo)
- `Book Note.md` — nota de libro
- `KoreNote Template.md` — nota de concepto core

## Plugins recomendados

- Templater — variables dinámicas en templates
- Dataview — queries y vistas dinámicas
- Calendar — vista calendario para daily notes
- Excalidraw — visual thinking
- Smart Connections — conexiones AI entre notas
- Bases — vistas tipo BD (oficial Obsidian 1.6+)

## Variables Templater más usadas

- `{{date:DD-MM-YYYY}}` — fecha hoy
- `{{date-1d:DD-MM-YYYY}}` — ayer
- `{{date:YYYY-[W]ww}}` — semana actual
- `{{date:YYYY-MM}}` — mes

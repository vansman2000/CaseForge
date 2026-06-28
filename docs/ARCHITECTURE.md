# CaseForge Architecture

## Layers

GUI

↓

Services

↓

Repositories

↓

SQLite

---

## Models

- Case
- Evidence

---

## Services

- CaseService
- EvidenceService

---

## Repositories

- EvidenceRepository

---

## GUI

- MainWindow
- CaseExplorer
- PreviewPanel
- PropertiesPanel
- MenuBar
- StatusBar

---

## Design Principles

- GUI never talks directly to SQLite.
- Repositories are responsible for persistence.
- Services coordinate application logic.
- Models represent domain data.
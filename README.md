# Monitor 42Roma Dashboard

## 🇮🇹 Panoramica

La dashboard **Monitor 42Roma** fornisce una vista in tempo reale sullo stato del campus 42 Roma Luiss. L’app è composta da un backend Flask e da una serie di template responsive che visualizzano:

- disponibilità, manutenzione e offline dei computer nei cluster E3 ed E4;
- annunci live e personalizzati gestiti via pannello staff;
- calendario eventi e iniziative provenienti dalle API 42;
- banner informativi configurabili con testo scorrevole.

### Caratteristiche Principali

- **Autenticazione OAuth** con l’API 42 per distinguere utenti e staff.
- **Gestione annunci** con CRUD e preview live prima della pubblicazione.
- **Pidigozzo degli eventi**: carosello responsive per annunci ed eventi.
- **Pannello staff** con strumenti per banner, manutenzione e monitoraggio.
- **Persistenza locale** tramite file JSON per log, banner, annunci e stato cluster.
- **Integrazione con servizi interni** (offline/online PCs, eventi) anche dietro certificati self-signed.

### Architettura

- `backend/app.py`: entrypoint Flask, routing, integrazioni API, logica annunci.
- `backend/templates/`: Jinja2 templates per dashboard, login, staff tools.
- `backend/static/css|js`: asset di stile e script per UI e interazioni.
- `backend/announcements/*.json`: archivio annunci e configurazioni banner.
- `.env`: variabili ambiente (client OAuth, URL interni, impostazioni SSL).

### Requisiti

- Python 3.7+
- uv (fast Python package installer and resolver)
- Flask 3.x
- Requests, PyYAML, python-dotenv
- Certificati SSL (o disabilitazione esplicita in ambienti di test)

### Setup Rapido

1. Copia `.env.sample` in `.env` e aggiorna le variabili.
2. Installa dipendenze con uv:
   ```bash
   uv sync
   ```
3. Avvia il server:
   ```bash
   python backend/app.py
   ```
4. Accedi a `https://monitor.42roma.it` (o host locale) e fai login con account 42.

### Sviluppo

Per installare anche le dipendenze di sviluppo (ruff, linting):
```bash
uv sync --all-extras
```

Eseguire ruff per verificare la qualità del codice:
```bash
uv run ruff check .
uv run ruff format .
```

---

## 🇬🇧 Overview

**Monitor 42Roma** is a real-time dashboard for the 42 Roma Luiss campus. It combines a Flask backend with responsive templates to display:

- live cluster availability, maintenance, and offline workstations across E3/E4;
- staff-managed announcements with live preview;
- upcoming 42 campus events pulled from the official APIs;
- configurable banner messages with ticker-style animation.

### Key Features

- **OAuth authentication** via the 42 API to distinguish regular users and staff.
- **Announcement management** (create/edit/delete) with live previews.
- **Event carousel** optimised for large displays and TVs.
- **Staff tools** for banner control, maintenance toggles, and logs.
- **Local persistence** using JSON files for logs, banner settings, and cluster state.
- **Integration with internal services** (offline/online endpoints, events) while bypassing self-signed SSL where needed.

### Architecture

- `backend/app.py`: main Flask application, routing logic, external integrations.
- `backend/templates/`: Jinja2 templates for the dashboard, login, and staff views.
- `backend/static/css|js`: styling and UI interaction scripts.
- `backend/announcements/*.json`: announcement registry and banner configuration.
- `.env`: environment variables (OAuth credentials, internal URLs, SSL paths).

### Requirements

- Python 3.7+
- uv (fast Python package installer and resolver)
- Flask 3.x
- Requests, PyYAML, python-dotenv
- SSL certificates or explicit verification override for test environments

### Quick Setup

1. Copy `.env.sample` to `.env` and adjust values.
2. Install dependencies with uv:
   ```bash
   uv sync
   ```
3. Run the server:
   ```bash
   python backend/app.py
   ```
4. Browse to `https://monitor.42roma.it` (or localhost) and authenticate with your 42 account.

### Development

To install development dependencies (ruff, linting tools):
```bash
uv sync --all-extras
```

Run ruff to check code quality:
```bash
uv run ruff check .
uv run ruff format .
```

Happy monitoring! 🚀


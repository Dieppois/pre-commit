# TP 1 - Sécuriser un dépôt Python avec pre-commit

Dépôt réalisé dans un cadre pédagogique, en Master 1 à l'EPSI, pour le module "Pilotage & amélioration continue de la sécurité".

## But du dépôt

Mettre en place des contrôles de qualité et de sécurité automatiques sur un projet Python :

- en local, avant chaque commit, avec les hooks pre-commit ;
- en CI, sur chaque push et pull request, avec GitHub Actions et pre-commit.ci ;
- côté serveur, avec une règle GitHub qui interdit les pushes directs sur `main`.

Le rapport du TP est disponible ici : [RAPPORT.md](RAPPORT.md)

## Contrôles utilisés

| Outil | Rôle | Local | CI |
|---|---|---|---|
| pre-commit-hooks | Espaces, fin de fichier, YAML, gros fichiers | Oui | Oui |
| Bandit | Analyse de sécurité du code Python | Oui | Oui |
| detect-secrets | Détection de secrets | Oui | Oui |
| pytest | Tests unitaires | Oui | Oui |
| pip-audit | Vulnérabilités connues des dépendances | Oui | Oui |

## Installation

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
copy .env.example .env
pre-commit install
```

Sous Linux ou macOS, activer l'environnement avec `source .venv/bin/activate` et copier le fichier avec `cp .env.example .env`.

Renseigner ensuite `APP_PASSWORD` dans `.env`. Ce fichier n'est jamais commité.

## Lancer les contrôles

```powershell
pre-commit run --all-files
pytest -q
pip-audit -r requirements.txt
```

## Contenu du dépôt

| Fichier | Contenu |
|---|---|
| `app.py` | Code Python corrigé |
| `test_app.py` | Tests unitaires |
| `.pre-commit-config.yaml` | Configuration des hooks |
| `.secrets.baseline` | Baseline de detect-secrets |
| `.github/workflows/securite.yml` | Workflow CI |
| `requirements.txt` | Dépendances de l'application |
| `requirements-dev.txt` | Outils de développement |
| `.env.example` | Variables d'environnement attendues, sans valeur |
| `RAPPORT.md` | Rapport du TP |
| `captures/` | Captures d'écran utilisées dans le rapport |

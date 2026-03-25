# Claude Code - Regras do Projeto `bit`

## Ferramentas

- **uv**: gerenciador de pacotes e runtime
- **ruff**: linter e formatter
- **ty**: type checker

## Comandos

```bash
uv run bit --help       # executar CLI
uv run python script.py # executar script
uv sync                 # instalar deps
uv add package-name     # adicionar dep
```

## Proibido

- `python script.py` — usar `uv run python script.py`
- `pip install` — usar `uv add` ou `uv sync`
- `black`, `isort`, `mypy` — usar `ruff` e `ty`

## Hooks Automaticos (pos-edicao)

- `ruff check .`
- `ruff format .`
- `ty check`

## Commits

Usar conventional commits (ver skill `conventional-commit`).

## Documentacao

Ao alterar codigo, verificar se docs precisam de atualizacao (ver skill `manage-docs`).

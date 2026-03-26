# bit

CLI interativa com personagem ASCII animado.

## Requisitos

- Python 3.14+
- [uv](https://docs.astral.sh/uv/)

## Instalacao

```bash
uv sync
```

## Comandos

```bash
# Saudacao
uv run bit hello --name "Fulano"
# Hello, Fulano!

# Personagem animado interativo (Textual TUI)
uv run bit char
# Comandos: /idle, /sleep, /work, /quit
```

## Estrutura do Projeto

```
bit/
├── bit/
│   ├── __init__.py              # Package marker
│   ├── main.py                  # Entry point CLI (Typer)
│   ├── character.py             # TUI Textual app com widgets e animacao
│   ├── character_frames.py      # Loader de frames (carrega de YAML)
│   └── frames.yaml              # Frames ASCII (idle, sleeping, working)
├── pyproject.toml               # Metadata e dependencias
├── C4_ARCHITECTURE.md           # Diagramas de arquitetura C4
├── CLAUDE.md                    # Instrucoes para Claude Code
└── README.md                    # Este arquivo
```

## Desenvolvimento

```bash
uv sync                          # instalar dependencias
uv run bit --help                # testar CLI
```

Hooks automaticos rodam apos cada edicao: `ruff check`, `ruff format`, `ty check`.

Commits seguem [Conventional Commits](https://www.conventionalcommits.org/).

## Arquitetura

Ver [C4_ARCHITECTURE.md](C4_ARCHITECTURE.md) para diagramas detalhados.

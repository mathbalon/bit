# C4 Architecture Model - Projeto BIT

Documentação de arquitetura do projeto `bit` usando o modelo C4.

---

## 1. Context Diagram (Contexto - 30.000 pés)

Visão de **alto nível** do sistema e seus atores externos.

```mermaid
graph TB
    User["👤 Developer/User"]
    BitCLI["🎯 BIT CLI<br/>(Python Typer)"]
    Terminal["💻 Terminal/Console"]

    User -->|runs commands| BitCLI
    BitCLI -->|outputs responses| Terminal
    Terminal -->|displays| User
```

**Descrição:**
- Um desenvolvedor/usuário interage com o CLI `bit` via linha de comando
- O sistema processa comandos e retorna respostas no terminal

---

## 2. Container Diagram (Contêineres - Arquitetura Geral)

Componentes principais do sistema.

```mermaid
graph TB
    User["👤 User<br/>Terminal"]

    subgraph BitSystem["BIT CLI System"]
        CLI["🔧 CLI Application<br/>(Typer Framework)"]
        CommandRegistry["📋 Command Registry<br/>(hello, char)"]
    end

    User -->|input commands| CLI
    CLI -->|looks up & executes| CommandRegistry
    CLI -->|outputs responses| User
```

**Contêineres:**

| Contêiner | Responsabilidade | Tecnologia |
|-----------|-----------------|-----------|
| **CLI Application** | Processa comandos, orquestra execução | Typer (CLI Framework) |
| **Command Registry** | Armazena definições de comandos disponíveis | Python Functions (@app.command) |

---

## 3. Component Diagram (Componentes - Dentro de CLI Application)

Detalhe interno da aplicação.

```mermaid
graph TB
    User["👤 Input"]

    subgraph CLI["CLI Application (Typer)"]
        ArgParser["📝 Argument Parser<br/>(Click/Typer)"]
        CommandRouter["🔀 Command Router<br/>(dispatch)"]
        HelloCommand["👋 Hello Command<br/>(hello --name)"]
        CharCommand["🎮 Char Command<br/>(animacao interativa)"]
        CharEngine["🖼️ Character Engine<br/>(curses + frames)"]
    end

    Terminal["💻 Terminal Output"]

    User -->|raw input| ArgParser
    ArgParser -->|parsed args| CommandRouter
    CommandRouter -->|execute| HelloCommand
    CommandRouter -->|execute| CharCommand
    HelloCommand -->|echo| Terminal
    CharCommand -->|usa| CharEngine
    CharEngine -->|renderiza| Terminal
```

**Componentes:**

| Componente | Função |
|-----------|--------|
| **Argument Parser** | Extrai e valida argumentos de linha de comando |
| **Command Router** | Roteia para handler apropriado baseado no comando |
| **Hello Command** | Formata mensagem de saudacao e imprime |
| **Char Command** | Inicia animacao interativa de personagem |
| **Character Engine** | Renderiza frames ASCII com curses, gerencia estados (idle, sleeping, working) |

---

## 4. Data Flow (Fluxo de Dados)

Como um comando flui atraves do sistema:

### hello

```
bit hello --name "World"
  → Argument Parser: identifica "hello", extrai name="World"
  → Command Router: encontra handler hello
  → Hello Command: typer.echo(f"Hello, {name}!")
  → Terminal: "Hello, World!"
```

### char

```
bit char
  → Argument Parser: identifica "char"
  → Command Router: encontra handler char
  → Char Command: chama character()
  → Character Engine (curses):
      - Inicializa terminal curses
      - Loop: le input (A/S/D/Q), seleciona frames, renderiza
      - Q encerra e restaura terminal
```

---

## 5. Modulos e Responsabilidades

| Modulo | Responsabilidade |
|--------|-----------------|
| `bit/main.py` | Entry point CLI, define comandos hello e char |
| `bit/character.py` | Engine de animacao: curses, estados, loop de render |
| `bit/character_frames.py` | Dados: frames ASCII para idle, sleeping, working |

---

## 6. Technology Stack

| Camada | Tecnologia | Propósito |
|--------|-----------|----------|
| **Framework CLI** | Typer 0.24.1+ | Definição e execução de comandos |
| **Parsing** | Click (via Typer) | Parsing de argumentos CLI |
| **Output** | typer.echo / curses | Saida formatada e animacao terminal |
| **Language** | Python 3.14+ | Runtime |
| **Build** | Hatchling | Build system |

---

## 7. Arquitetura Evolutiva

### Estado Atual

```mermaid
graph TB
    User["👤 User"]

    subgraph BitCurrent["BIT (Atual)"]
        CLI["CLI Application"]
        Cmd1["👋 hello"]
        Cmd2["🎮 char"]
    end

    User -->|input| CLI
    CLI -->|routes to| Cmd1
    CLI -->|routes to| Cmd2
```

### Possiveis Expansoes

Novos comandos seguem o mesmo padrao: funcao com `@app.command()` em `main.py`, logica em modulo dedicado.

---

## 8. Dependências do Projeto

```mermaid
graph LR
    Main["bit.main<br/>(CLI entry)"]
    Character["bit.character<br/>(animacao)"]
    Frames["bit.character_frames<br/>(dados ASCII)"]
    Typer["Typer 0.24.1+<br/>(Framework)"]
    Curses["curses<br/>(stdlib)"]
    Click["Click<br/>(parser)"]
    Python["Python 3.14+<br/>(runtime)"]

    Main -->|imports| Typer
    Main -->|imports| Character
    Character -->|imports| Frames
    Character -->|imports| Curses
    Typer -->|uses| Click
    Typer & Click & Main -->|run on| Python
```

---

## 9. Setup

Ver [README.md](README.md) para instrucoes de instalacao e uso.

---

## Referências

- [C4 Model](https://c4model.com/)
- [Typer Documentation](https://typer.tiangolo.com/)
- [Click Documentation](https://click.palletsprojects.com/)

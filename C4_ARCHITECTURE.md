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
        CharCommand["🎮 Char Command<br/>(inicia TUI)"]
        TUI["🖼️ Textual TUI App<br/>(CharacterApp + Widgets)"]
        CharDisplay["🎬 CharacterDisplay<br/>(renderiza frames)"]
        MessageDisplay["💬 MessageDisplay<br/>(feedback usuario)"]
    end

    Terminal["💻 Terminal Output"]

    User -->|raw input| ArgParser
    ArgParser -->|parsed args| CommandRouter
    CommandRouter -->|execute| HelloCommand
    CommandRouter -->|execute| CharCommand
    HelloCommand -->|echo| Terminal
    CharCommand -->|inicia| TUI
    TUI -->|contem| CharDisplay
    TUI -->|contem| MessageDisplay
    TUI -->|renderiza| Terminal
```

**Componentes:**

| Componente | Função |
|-----------|--------|
| **Argument Parser** | Extrai e valida argumentos de linha de comando |
| **Command Router** | Roteia para handler apropriado baseado no comando |
| **Hello Command** | Formata mensagem de saudacao e imprime |
| **Char Command** | Inicia aplicacao Textual TUI |
| **Textual TUI App** | Aplicacao interativa com input e animacao |
| **CharacterDisplay** | Widget que renderiza frames ASCII em loop |
| **MessageDisplay** | Widget que mostra feedback e status |

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
  → Textual App (CharacterApp):
      - Monta layout (CharacterDisplay + MessageDisplay + Input)
      - Timer de 0.3s atualiza frames de animacao
      - Usuario digita ou usa comandos /idle, /sleep, /work, /quit
      - CharacterDisplay renderiza frame atual alinhado ao bottom-left
      - MessageDisplay mostra feedback e status
      - /quit encerra app e restaura terminal
```

---

## 5. Modulos e Responsabilidades

| Modulo | Responsabilidade |
|--------|-----------------|
| `bit/main.py` | Entry point CLI, define comandos hello e char |
| `bit/character.py` | Textual TUI app: CharacterApp, CharacterDisplay, MessageDisplay widgets |
| `bit/character_frames.py` | Loader de frames: carrega ASCII de frames.yaml |
| `bit/frames.yaml` | Dados: frames ASCII para idle, sleeping, working (formato YAML) |

---

## 6. Technology Stack

| Camada | Tecnologia | Propósito |
|--------|-----------|----------|
| **Framework CLI** | Typer 0.24.1+ | Definição e execução de comandos |
| **Parsing** | Click (via Typer) | Parsing de argumentos CLI |
| **TUI Framework** | Textual 8.1.1+ | Interface interativa, widgets, layout, animacao |
| **Data Format** | PyYAML 6.0.3+ | Carregamento de frames ASCII de arquivo YAML |
| **Output** | Textual | Saida formatada e animacao terminal |
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
    Character["bit.character<br/>(TUI Textual)"]
    Frames["bit.character_frames<br/>(loader YAML)"]
    FramesFile["frames.yaml<br/>(dados ASCII)"]
    Typer["Typer 0.24.1+<br/>(CLI Framework)"]
    Textual["Textual 8.1.1+<br/>(TUI Framework)"]
    PyYAML["PyYAML 6.0.3+<br/>(YAML parser)"]
    Click["Click<br/>(parser)"]
    Python["Python 3.14+<br/>(runtime)"]

    Main -->|imports| Typer
    Main -->|imports| Character
    Character -->|imports| Frames
    Character -->|imports| Textual
    Frames -->|reads| FramesFile
    Frames -->|imports| PyYAML
    Typer -->|uses| Click
    Typer & Textual & PyYAML & Main -->|run on| Python
```

---

## 9. Setup

Ver [README.md](README.md) para instrucoes de instalacao e uso.

---

## Referências

- [C4 Model](https://c4model.com/)
- [Typer Documentation](https://typer.tiangolo.com/)
- [Click Documentation](https://click.palletsprojects.com/)

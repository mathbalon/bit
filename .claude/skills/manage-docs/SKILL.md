---
name: manage-docs
description: Guia para gerenciar e atualizar a documentacao do projeto bit quando o codigo muda.
---

# Gerenciamento de Documentacao

## Mapa de Documentos

| Arquivo | Responsabilidade | Quando Atualizar |
|---------|-----------------|-----------------|
| `CLAUDE.md` | Regras de dev para Claude (tooling, proibicoes, hooks) | Mudanca de tooling, novo linter, nova regra |
| `README.md` | Ponto de entrada humano (install, uso, estrutura) | Novo comando, mudanca de requisitos ou estrutura |
| `C4_ARCHITECTURE.md` | Diagramas C4 (contexto, container, componente, fluxo, tech stack) | Novo modulo, nova dep, mudanca de arquitetura |
| `pyproject.toml` | Descricao do projeto, deps, config de ferramentas | Mudanca de escopo do projeto |

## Regras

1. **Sem duplicacao**: cada informacao existe em exatamente 1 lugar
2. **CLAUDE.md minimo**: so instrucoes que Claude precisa em toda conversa (< 40 linhas)
3. **README.md e o ponto de entrada**: humano novo consegue comecar so com README
4. **C4 so arquitetura**: sem instrucoes de setup, sem regras de dev
5. **Portugues**: toda documentacao em portugues

## Novo Comando Adicionado

1. **README.md**: adicionar na secao "Comandos" com exemplo
2. **C4_ARCHITECTURE.md**:
   - Secao 2 (Container): atualizar lista de comandos no diagrama
   - Secao 3 (Component): adicionar componente no diagrama e tabela
   - Secao 4 (Data Flow): adicionar fluxo do novo comando
   - Secao 5 (Modulos): adicionar se criou novos arquivos
   - Secao 7 (Evolutiva): atualizar diagrama de estado atual
3. **CLAUDE.md**: nao precisa mudar

## Nova Dependencia Adicionada

1. **C4_ARCHITECTURE.md**: atualizar secao 6 (Tech Stack) e secao 8 (Dependencias)
2. **README.md**: atualizar "Requisitos" se for dep de sistema
3. **CLAUDE.md**: so se mudar regras (ex: novo linter)

## Mudanca de Tooling

1. **CLAUDE.md**: atualizar comandos e regras
2. **README.md**: atualizar secao "Desenvolvimento" se afeta workflow
3. **C4_ARCHITECTURE.md**: atualizar Tech Stack se relevante

## Mudanca de Estrutura de Arquivos

1. **README.md**: atualizar arvore de estrutura
2. **C4_ARCHITECTURE.md**: atualizar secao 5 (Modulos)

## Checklist de Validacao

Antes de finalizar atualizacao de docs:

- [ ] Nenhuma informacao duplicada entre arquivos
- [ ] CLAUDE.md < 40 linhas
- [ ] README.md tem todos os comandos existentes
- [ ] C4 reflete todos os modulos e dependencias atuais
- [ ] Zero mencoes a `pip` ou `python` sem `uv` nos docs
- [ ] pyproject.toml description atualizada se escopo mudou

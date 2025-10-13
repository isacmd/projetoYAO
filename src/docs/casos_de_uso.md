# CASOS DE USO - Projeto YAO

## Projeto 1 - Sistema de Gerenciamento

### UC01 - Gerenciar Sistema
**Ator Principal:** Administrador
**Descrição:** Permite configurar e gerenciar o sistema
**Pré-condições:** Sistema inicializado
**Fluxo Principal:**
1. Administrador acessa o sistema
2. Sistema exibe menu de opções
3. Administrador seleciona operação desejada
4. Sistema executa comando correspondente
5. Sistema exibe resultado

**Fluxo Alternativo:**
- 4a. Comando inválido
  - Sistema exibe mensagem de erro
  - Retorna ao passo 2

---
### UC02 - Executar Comando
**Ator Principal:** Usuário
**Descrição:** Executa comandos no sistema
**Pré-condições:** Sistema rodando
**Fluxo Principal:**
1. Usuário solicita execução de comando
2. Sistema valida permissões
3. Comando é encapsulado e executado
4. Sistema registra comando no histórico
5. Sistema retorna resultado

**Fluxo Alternativo:**
- 2a. Usuário sem permissão
  - Sistema exibe erro
  - Operação cancelada

---
### UC03 - Desfazer Operação (Memento)
**Ator Principal:** Usuário
**Descrição:** Permite desfazer última ação realizada
**Pré-condições:** Pelo menos um comando executado
**Fluxo Principal:**
1. Usuário solicita desfazer
2. Sistema recupera comando do histórico
3. Sistema executa undo() do comando
4. Sistema atualiza posição no histórico
5. Sistema confirma operação

**Fluxo Alternativo:**
- 1a. Histórico vazio
  - Sistema informa que não há ações para desfazer

---
## Projeto 2 - Sistema de RH

### UC04 - Cadastrar Colaborador
**Ator Principal:** RH
**Descrição:** Cadastra novo colaborador no sistema
**Pré-condições:** Usuário autenticado como RH
**Fluxo Principal:**
1. RH acessa opção de cadastro
2. Sistema solicita dados do colaborador
3. RH informa dados (usando Composite para seções)
4. Sistema valida dados (via Adapter)
5. Sistema persiste no DAO
6. Sistema confirma cadastro

**Fluxo Alternativo:**
- 4a. Dados inválidos
  - Sistema exibe erros de validação
  - Retorna ao passo 3

---

### UC05 - Gerar Relatório
**Ator Principal:** Gestor
**Descrição:** Gera relatório de colaboradores
**Pré-condições:** Sistema com colaboradores cadastrados
**Fluxo Principal:**
1. Gestor acessa opção de relatório
2. Sistema solicita tipo de relatório (HTML/PDF/CSV)
3. Gestor seleciona tipo
4. Sistema usa Factory para criar relatório
5. Relatório é gerado via Template Method
6. Sistema salva arquivo
7. Sistema confirma geração

---

### UC06 - Adicionar Seção ao Colaborador
**Ator Principal:** RH
**Descrição:** Adiciona nova seção ao cadastro
**Pré-condições:** Colaborador já cadastrado
**Fluxo Principal:**
1. RH seleciona colaborador
2. Sistema exibe colaborador
3. RH escolhe tipo de seção (Composite)
4. Sistema cria seção
5. Sistema adiciona à estrutura do colaborador
6. Sistema persiste alteração
7. Sistema confirma operação
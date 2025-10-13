import random
from .command.receptor import Receptor
from .command.concrete_commands import EscreverComando, ApagarComando, LimparComando
from .command.executor import Executor
from .observer.concrete_observers import MonitorConsole, MonitorLog, MonitorEmail
from .observer.subject_concreto import SistemaMonitorado
from .strategy.concrete_strategies import OrdenacaoBubbleSort, OrdenacaoQuickSort, OrdenacaoMergeSort
from .strategy.context import ContextoOrdenacao
from .template.concrete_templates import ProcessadorCSV, ProcessadorJSON, ProcessadorXML
from .prototype.concrete_prototypes import Documento, Configuracao, PerfilUsuario
from .prototype.registry import PrototypeRegistry

# demonstração do padrão command
def demo_command():
    print("\n" + "="*60)
    print("DEMONSTRAÇÃO: Padrão Command")
    print("="*60)
    
    receptor = Receptor()
    executor = Executor()
    
    # executar comandos
    executor.executar(EscreverComando(receptor, "Olá "))
    executor.executar(EscreverComando(receptor, "Mundo!"))
    executor.executar(EscreverComando(receptor, " Isabella e Vinicius aqui"))
    
    print(f"\ntexto atual: '{receptor.obter_texto()}'")
    print(executor.mostrar_historico())
    
    # desfazer
    print("\n" + "-"*60)
    print(executor.desfazer())
    print(f"texto atual: '{receptor.obter_texto()}'")
    
    print(executor.desfazer())
    print(f"texto atual: '{receptor.obter_texto()}'")
    
    # refazer
    print("\n" + "-"*60)
    print(executor.refazer())
    print(f"texto atual: '{receptor.obter_texto()}'")
    
    # limpar
    print("\n" + "-"*60)
    executor.executar(LimparComando(receptor))
    print(f"texto atual: '{receptor.obter_texto()}'")
    
    print(executor.desfazer())
    print(f"texto atual: '{receptor.obter_texto()}'")

# demonstração do padrão observer
def demo_observer():
    print("\n" + "="*60)
    print("DEMONSTRAÇÃO: Padrão Observer")
    print("="*60)
    
    sistema = SistemaMonitorado("ServidorWeb")
    
    # criar observers
    console1 = MonitorConsole("Principal")
    console2 = MonitorConsole("Backup")
    log = MonitorLog()
    email = MonitorEmail("admin@example.com")
    
    # anexar observers
    sistema.anexar(console1)
    sistema.anexar(console2)
    sistema.anexar(log)
    sistema.anexar(email)
    
    # disparar eventos
    print("\n" + "-"*60)
    sistema.alterar_estado("Rodando")
    
    print("\n" + "-"*60)
    sistema.executar_acao("Processar requisição HTTP")
    
    print("\n" + "-"*60)
    sistema.desanexar(console2)
    sistema.alterar_estado("Sobrecarga")
    
    print("\n" + "-"*60)
    print("LOG COMPLETO:")
    for entrada in log.obter_log():
        print(f"  {entrada}")

# demonstração do padrão strategy
def demo_strategy():
    print("\n" + "="*60)
    print("DEMONSTRAÇÃO: Padrão Strategy")
    print("="*60)
    
    # dados para ordenar
    dados_pequenos = [64, 34, 25, 12, 22, 11, 90]
    dados_grandes = random.sample(range(1000), 100)
    
    contexto = ContextoOrdenacao()
    
    # testar diferentes estratégias
    print("\nteste com dados pequenos:")
    contexto.definir_estrategia(OrdenacaoBubbleSort())
    contexto.ordenar(dados_pequenos)
    
    print("\n" + "-"*60)
    contexto.definir_estrategia(OrdenacaoQuickSort())
    contexto.ordenar(dados_pequenos)
    
    # comparar performance
    print("\n" + "-"*60)
    estrategias = [
        OrdenacaoBubbleSort(),
        OrdenacaoQuickSort(),
        OrdenacaoMergeSort()
    ]
    contexto.comparar_estrategias(dados_grandes, estrategias)

# demonstração do padrão template method
def demo_template_method():
    print("\n" + "="*60)
    print("DEMONSTRAÇÃO: Padrão Template Method")
    print("="*60)
    
    # processar diferentes tipos de arquivo
    processadores = [
        (ProcessadorCSV(), "dados.csv"),
        (ProcessadorJSON(), "config.json"),
        (ProcessadorXML(), "documento.xml")
    ]
    
    for processador, arquivo in processadores:
        print()
        processador.processar(arquivo)

# demonstração do padrão prototype
def demo_prototype():
    print("\n" + "="*60)
    print("DEMONSTRAÇÃO: Padrão Prototype")
    print("="*60)
    
    # criar protótipos base
    doc_base = Documento("Template Relatório", "Conteúdo padrão")
    doc_base.adicionar_tag("template")
    doc_base.adicionar_tag("oficial")
    
    config_base = Configuracao("Produção")
    config_base.definir("timeout", 30)
    config_base.definir("max_connections", 100)
    
    perfil_admin = PerfilUsuario("Administrador", "admin")
    perfil_admin.adicionar_permissao("criar")
    perfil_admin.adicionar_permissao("editar")
    perfil_admin.adicionar_permissao("deletar")
    
    # registrar protótipos
    registry = PrototypeRegistry()
    registry.registrar("documento_template", doc_base)
    registry.registrar("config_producao", config_base)
    registry.registrar("perfil_admin", perfil_admin)
    
    print("\n" + "-"*60)
    print(f"protótipos registrados: {registry.listar()}")
    
    # criar clones
    print("\n" + "-"*60)
    print("criando clones:")
    doc1 = registry.criar("documento_template")
    doc1.titulo = "Relatório Mensal"
    
    doc2 = registry.criar("documento_template")
    doc2.titulo = "Relatório Anual"
    
    config1 = registry.criar("config_producao")
    config1.nome = "Produção Servidor 1"
    
    perfil1 = registry.criar("perfil_admin")
    perfil1.nome = "João Silva"
    
    print("\n" + "-"*60)
    print("comparação original vs clones:")
    print(f"  original: {doc_base}")
    print(f"  clone 1:  {doc1}")
    print(f"  clone 2:  {doc2}")

# menu interativo
def menu_principal():
    while True:
        print("\n" + "="*60)
        print("PROJETO 3 - PADRÕES GOF - Menu Principal")
        print("="*60)
        print("1. Command Pattern")
        print("2. Observer Pattern")
        print("3. Strategy Pattern")
        print("4. Template Method Pattern")
        print("5. Prototype Pattern")
        print("6. Executar Todas as Demos")
        print("0. Sair")
        print("="*60)
        
        opcao = input("\nescolha uma opção: ")
        
        if opcao == "1":
            demo_command()
        elif opcao == "2":
            demo_observer()
        elif opcao == "3":
            demo_strategy()
        elif opcao == "4":
            demo_template_method()
        elif opcao == "5":
            demo_prototype()
        elif opcao == "6":
            demo_command()
            demo_observer()
            demo_strategy()
            demo_template_method()
            demo_prototype()
        elif opcao == "0":
            print("\nencerrando sistema...")
            break
        else:
            print("\nopção inválida!")
        
        input("\npressione enter para continuar...")

if __name__ == "__main__":
    print("""
    ════════════════════════════════════════════════════════════
                     PROJETO 3 - PADRÕES DE PROJETO GOF         
                                                                
      padrões implementados:                                    
      command (comportamental)                                  
      observer (comportamental)                                 
      strategy (comportamental)                                 
      template method (comportamental)                          
      prototype (criacional)                                    
    ════════════════════════════════════════════════════════════
    """)
    
    menu_principal()


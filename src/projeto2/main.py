from datetime import date
from decimal import Decimal
from .model.colaborador import Colaborador
from .model.dados_pessoais import DadosPessoais
from .model.dados_admissionais import DadosAdmissionais
from .model.endereco import Endereco, TipoEndereco
from .model.documento import Documento, TipoDocumento
from .business.facade import ColaboradorFacade

# demonstra uso do padrão composite
def exemplo_uso_composite():
    print("\n" + "="*60)
    print("DEMONSTRAÇÃO: Padrão Composite")
    print("="*60)
    
    # criar colaborador (composite)
    colaborador = Colaborador("001", "João Silva")
    
    # criar seções (leafs)
    dados_pessoais = DadosPessoais("João Silva", "123.456.789-00", "12.345.678-9")
    dados_pessoais.adicionar_dependente("Maria Silva")
    dados_pessoais.adicionar_contato("(83) 98888-7777")
    
    dados_admissionais = DadosAdmissionais(
        "Desenvolvedor Senior",
        date(2023, 1, 15),
        Decimal("8500.00")
    )
    dados_admissionais.setor = "TI"
    dados_admissionais.gestor = "Pedro Santos"
    
    endereco_residencial = Endereco(
        TipoEndereco.RESIDENCIAL,
        "Rua das Flores, 123",
        "João Pessoa",
        "PB",
        "58000-000"
    )
    endereco_residencial.complemento = "Apto 301"
    
    doc_rg = Documento(TipoDocumento.RG, "12.345.678-9")
    doc_rg.orgao_emissor = "SSP-PB"
    
    doc_ctps = Documento(TipoDocumento.CTPS, "123456/0001")
    
    # montar estrutura hierárquica
    colaborador.adicionar(dados_pessoais)
    colaborador.adicionar(dados_admissionais)
    colaborador.adicionar(endereco_residencial)
    colaborador.adicionar(doc_rg)
    colaborador.adicionar(doc_ctps)
    
    # exibir estrutura completa (recursivo)
    print(colaborador.exibir())
    
    return colaborador

# demonstra uso do padrão dao
def exemplo_uso_dao():
    print("\n" + "="*60)
    print("DEMONSTRAÇÃO: Padrão DAO")
    print("="*60)
    
    from .dao.colaborador_dao import ColaboradorDAO
    
    dao = ColaboradorDAO()
    
    # criar colaboradores
    colab1 = Colaborador("001", "João Silva")
    colab2 = Colaborador("002", "Maria Santos")
    colab3 = Colaborador("003", "Pedro Oliveira")
    
    # inserir
    dao.inserir(colab1)
    dao.inserir(colab2)
    dao.inserir(colab3)
    
    # buscar
    print("\nBuscar por ID '002':")
    encontrado = dao.buscar_por_id("002")
    if encontrado:
        print(f"  Encontrado: {encontrado.nome}")
    
    # listar todos
    print("\nTodos os colaboradores:")
    for c in dao.buscar_todos():
        print(f"  - {c.id}: {c.nome}")
    
    # atualizar
    colab2_atualizado = Colaborador("002", "Maria Santos Costa")
    dao.atualizar(colab2_atualizado)
    
    # deletar
    dao.deletar("003")
    
    print("\nApós deleção:")
    for c in dao.buscar_todos():
        print(f"  - {c.id}: {c.nome}")

# demonstra uso do padrão adapter
def exemplo_uso_adapter():
    print("\n" + "="*60)
    print("DEMONSTRAÇÃO: Padrão Adapter")
    print("="*60)
    
    from .adapter.validador_adapter import ValidadorAdapter
    
    validador = ValidadorAdapter()
    
    # colaborador válido
    colab_valido = Colaborador("001", "João Silva")
    dados_pessoais = DadosPessoais("João Silva", "12345678900")
    colab_valido.adicionar(dados_pessoais)
    
    try:
        validador.validar(colab_valido)
        print("Colaborador válido!")
    except ValueError as e:
        print(f"{e}")
    
    # colaborador inválido (cpf errado)
    colab_invalido = Colaborador("002", "Maria Santos")
    dados_invalidos = DadosPessoais("Maria Santos", "123")  # CPF inválido
    colab_invalido.adicionar(dados_invalidos)
    
    try:
        validador.validar(colab_invalido)
        print("Colaborador válido!")
    except ValueError as e:
        print(f"Erro de validação: {e}")

# demonstra uso dos padrões factory method e template method
def exemplo_uso_factory_template():
    print("\n" + "="*60)
    print("DEMONSTRAÇÃO: Factory Method + Template Method")
    print("="*60)
    
    from .business.factory_relatorio import RelatorioFactory
    from .dao.colaborador_dao import ColaboradorDAO
    
    # preparar dados
    dao = ColaboradorDAO()
    dao.limpar()
    
    colab1 = Colaborador("001", "João Silva")
    colab2 = Colaborador("002", "Maria Santos")
    dao.inserir(colab1)
    dao.inserir(colab2)
    
    factory = RelatorioFactory()
    
    # gerar diferentes tipos de relatório
    for tipo in ['html', 'pdf', 'csv']:
        print(f"\nRelatório em {tipo.upper()}:")
        print("-" * 60)
        relatorio = factory.criar_relatorio(tipo)
        conteudo = relatorio.gerar(dao.buscar_todos())
        print(conteudo[:300] + "..." if len(conteudo) > 300 else conteudo)

# demonstra uso do padrão facade
def exemplo_uso_facade():
    print("\n" + "="*60)
    print("DEMONSTRAÇÃO: Padrão Facade")
    print("="*60)
    
    facade = ColaboradorFacade()
    
    # criar colaborador completo
    colaborador = exemplo_uso_composite()
    
    # usar facade para simplificar operações
    print("\nUsando Facade para gerenciar colaborador:")
    facade.cadastrar_colaborador(colaborador)
    
    # buscar
    print("\nBuscar colaborador:")
    facade.buscar_colaborador("001")
    
    # gerar relatório
    print("\nGerar relatório HTML:")
    facade.gerar_relatorio('html', salvar_arquivo=True)

# menu interativo
def menu_principal():
    facade = ColaboradorFacade()
    
    while True:
        print("\n" + "="*60)
        print("SISTEMA DE GESTÃO DE RH - Menu Principal")
        print("="*60)
        print("1. Cadastrar Colaborador")
        print("2. Listar Todos")
        print("3. Buscar por ID")
        print("4. Gerar Relatório")
        print("5. Demonstrações dos Padrões")
        print("0. Sair")
        print("="*60)
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            # cadastro simplificado
            id_colab = input("ID: ")
            nome = input("Nome: ")
            cpf = input("CPF: ")
            
            colab = Colaborador(id_colab, nome)
            dados_pessoais = DadosPessoais(nome, cpf)
            colab.adicionar(dados_pessoais)
            
            facade.cadastrar_colaborador(colab)
            
        elif opcao == "2":
            facade.listar_todos()
            
        elif opcao == "3":
            id_busca = input("Digite o ID: ")
            facade.buscar_colaborador(id_busca)
            
        elif opcao == "4":
            tipo = input("Tipo (html/pdf/csv): ")
            facade.gerar_relatorio(tipo, salvar_arquivo=True)
            
        elif opcao == "5":
            exemplo_uso_composite()
            exemplo_uso_dao()
            exemplo_uso_adapter()
            exemplo_uso_factory_template()
            exemplo_uso_facade()
            
        elif opcao == "0":
            print("\nEncerrando sistema...")
            break
        else:
            print("\nOpção inválida!")

if __name__ == "__main__":
    print("""
    ════════════════════════════════════════════════════════════
                 PROJETO 2 - SISTEMA DE GESTÃO DE RH              
                                                                  
      Padrões implementados:                                      
      Composite (Model)                                           
      DAO (Persistence)                                           
      Adapter (Validation)                                        
      Factory Method (Reports)                                    
      Template Method (Reports)                                   
      Facade (Business Logic)                                     
    ════════════════════════════════════════════════════════════
    """)
    
    menu_principal()

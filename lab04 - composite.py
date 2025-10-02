from abc import ABC, abstractmethod
from typing import List


# COMPONENT 
class ComponenteCadastro(ABC):
    
    def __init__(self, nome: str):
        self.nome = nome
    
    @abstractmethod
    def exibir(self, nivel: int = 0) -> str:
        pass
    
    def adicionar(self, componente: 'ComponenteCadastro') -> None:
        raise NotImplementedError("Operação não suportada para este componente")
    
    def remover(self, componente: 'ComponenteCadastro') -> None:
        raise NotImplementedError("Operação não suportada para este componente")


# LEAF (folhas)
class Campo(ComponenteCadastro):
    
    def __init__(self, nome: str, valor: str = ""):
        super().__init__(nome)
        self.valor = valor
    
    def exibir(self, nivel: int = 0) -> str:
        indentacao = "  " * nivel
        if self.valor:
            return f"{indentacao}• {self.nome}: {self.valor}\n"
        else:
            return f"{indentacao}• {self.nome}: [não preenchido]\n"


# COMPOSITE (nós compostos que podem ter filhos)
class Secao(ComponenteCadastro):
    
    def __init__(self, nome: str):
        super().__init__(nome)
        self.componentes: List[ComponenteCadastro] = []
    
    def adicionar(self, componente: ComponenteCadastro) -> None:
        """Adiciona um componente à seção"""
        self.componentes.append(componente)
    
    def remover(self, componente: ComponenteCadastro) -> None:
        """Remove um componente da seção"""
        self.componentes.remove(componente)
    
    def exibir(self, nivel: int = 0) -> str:
        """Exibe a seção e todos seus componentes recursivamente"""
        indentacao = "  " * nivel
        resultado = f"{indentacao}{'=' * 50}\n"
        resultado += f"{indentacao}{self.nome.upper()}\n"
        resultado += f"{indentacao}{'=' * 50}\n"
        
        for componente in self.componentes:
            resultado += componente.exibir(nivel + 1)
        
        return resultado


# CLIENT (classe que usa a composite)
class CadastroColaborador:
    
    def __init__(self, nome_colaborador: str):
        self.nome_colaborador = nome_colaborador
        self.raiz = Secao(f"Cadastro de {nome_colaborador}")
    
    def adicionar_secao(self, secao: ComponenteCadastro) -> None:
        """Adiciona uma seção ao cadastro"""
        self.raiz.adicionar(secao)
    
    def exibir_cadastro_completo(self) -> str:
        """Exibe todo o cadastro de forma hierárquica"""
        return self.raiz.exibir()


# EXEMPLO DE USO
def criar_exemplo_cadastro():
    
    cadastro = CadastroColaborador("João Silva")
    
    # === DADOS PESSOAIS ===
    dados_pessoais = Secao("Dados Pessoais")
    dados_pessoais.adicionar(Campo("Nome Completo", "João Silva Santos"))
    dados_pessoais.adicionar(Campo("Data de Nascimento", "15/03/1990"))
    dados_pessoais.adicionar(Campo("Estado Civil", "Casado"))
    dados_pessoais.adicionar(Campo("Sexo", "Masculino"))
    
    # Subseção: dependentes
    dependentes = Secao("Dependentes")
    dependentes.adicionar(Campo("Dependente 1", "Maria Silva Santos - Filha"))
    dependentes.adicionar(Campo("Dependente 2", "Pedro Silva Santos - Filho"))
    dados_pessoais.adicionar(dependentes)
    
    # Subseção: contatos
    contatos = Secao("Contatos")
    contatos.adicionar(Campo("Telefone", "(83) 98765-4321"))
    contatos.adicionar(Campo("E-mail", "joao.silva@empresa.com"))
    contatos.adicionar(Campo("Telefone Emergência", "(83) 91234-5678"))
    dados_pessoais.adicionar(contatos)
    
    cadastro.adicionar_secao(dados_pessoais)
    
    # === DADOS ADMISSIONAL ===
    dados_admissional = Secao("Dados Admissional")
    dados_admissional.adicionar(Campo("Cargo", "Analista de Sistemas Sênior"))
    dados_admissional.adicionar(Campo("Data de Admissão", "01/06/2020"))
    dados_admissional.adicionar(Campo("Salário", "R$ 8.500,00"))
    dados_admissional.adicionar(Campo("Departamento", "Tecnologia da Informação"))
    dados_admissional.adicionar(Campo("Tipo de Contrato", "CLT"))
    
    cadastro.adicionar_secao(dados_admissional)
    
    # === ENDEREÇO ===
    endereco = Secao("Endereço")
    
    # Subseção: Residencial
    residencial = Secao("Residencial")
    residencial.adicionar(Campo("Logradouro", "Rua das Flores, 123"))
    residencial.adicionar(Campo("Bairro", "Centro"))
    residencial.adicionar(Campo("Cidade", "João Pessoa"))
    residencial.adicionar(Campo("Estado", "Paraíba"))
    residencial.adicionar(Campo("CEP", "58000-000"))
    endereco.adicionar(residencial)
    
    # subseção: comercial
    comercial = Secao("Comercial")
    comercial.adicionar(Campo("Logradouro", "Av. Epitácio Pessoa, 500"))
    comercial.adicionar(Campo("Bairro", "Bessa"))
    comercial.adicionar(Campo("Cidade", "João Pessoa"))
    comercial.adicionar(Campo("Estado", "Paraíba"))
    comercial.adicionar(Campo("CEP", "58037-000"))
    endereco.adicionar(comercial)
    
    cadastro.adicionar_secao(endereco)
    
    # === DOCUMENTOS ===
    documentos = Secao("Documentos")
    documentos.adicionar(Campo("RG", "1.234.567 SSP/PB"))
    documentos.adicionar(Campo("CPF", "123.456.789-00"))
    documentos.adicionar(Campo("CTPS", "123456 - Série 0001"))
    documentos.adicionar(Campo("CNH", "12345678900 - Categoria B"))
    documentos.adicionar(Campo("Título de Eleitor", "1234 5678 9012"))
    documentos.adicionar(Campo("PIS/PASEP", "123.45678.90-1"))
    
    cadastro.adicionar_secao(documentos)
    
    return cadastro


# DEMONSTRAÇÃO DE FUNCIONALIDADES
def demonstrar_funcionalidades():
    
    print("=" * 70)
    print("SISTEMA DE GESTÃO DE RH - PADRÃO COMPOSITE")
    print("=" * 70)
    print()
    
    cadastro = criar_exemplo_cadastro()
    print(cadastro.exibir_cadastro_completo())
    
    print("\n" + "=" * 70)
    print("DEMONSTRAÇÃO: ADICIONANDO NOVA SEÇÃO DINAMICAMENTE")
    print("=" * 70)
    print()
    
    nova_secao = Secao("Benefícios")
    nova_secao.adicionar(Campo("Plano de Saúde", "Unimed - Titular + 2 dependentes"))
    nova_secao.adicionar(Campo("Vale Refeição", "R$ 30,00/dia"))
    nova_secao.adicionar(Campo("Vale Transporte", "Sim"))
    
    cadastro.adicionar_secao(nova_secao)
    print(cadastro.exibir_cadastro_completo())
    
    print("\n" + "=" * 70)
    print("DEMONSTRAÇÃO: CADASTRO MINIMALISTA")
    print("=" * 70)
    print()
    
    cadastro_minimo = CadastroColaborador("Ana Costa")
    
    dados_basicos = Secao("Dados Básicos")
    dados_basicos.adicionar(Campo("Nome", "Ana Costa"))
    dados_basicos.adicionar(Campo("CPF", "987.654.321-00"))
    dados_basicos.adicionar(Campo("Cargo", "Estagiária"))
    
    cadastro_minimo.adicionar_secao(dados_basicos)
    print(cadastro_minimo.exibir_cadastro_completo())


if __name__ == "__main__":
    demonstrar_funcionalidades()
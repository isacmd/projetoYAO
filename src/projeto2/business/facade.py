from typing import List, Optional
from ..dao.colaborador_dao import ColaboradorDAO
from ..model.colaborador import Colaborador, ComponenteCadastro
from ..adapter.validador_adapter import ValidadorAdapter
from .factory_relatorio import RelatorioFactory

# facade que simplifica operações complexas do sistema
class ColaboradorFacade:
    
    def __init__(self):
        self._dao = ColaboradorDAO()
        self._validador = ValidadorAdapter()
        self._factory_relatorio = RelatorioFactory()
    
    # cadastra novo colaborador com validação
    def cadastrar_colaborador(self, colaborador: Colaborador) -> None:
        try:
            # validação
            self._validador.validar(colaborador)
            
            # persistência
            self._dao.inserir(colaborador)
            
            # feedback
            print(f"Colaborador '{colaborador.nome}' cadastrado com sucesso!")
            
        except ValueError as e:
            print(f"Erro de validação: {e}")
            raise
        except Exception as e:
            print(f"Erro ao cadastrar: {e}")
            raise
    
    # atualiza colaborador existente
    def atualizar_colaborador(self, colaborador: Colaborador) -> None:
        try:
            self._validador.validar(colaborador)
            self._dao.atualizar(colaborador)
            print(f"Colaborador '{colaborador.nome}' atualizado!")
        except Exception as e:
            print(f"Erro ao atualizar: {e}")
            raise
    
    # remove colaborador por id
    def remover_colaborador(self, id: str) -> None:
        if self._dao.deletar(id):
            print(f"Colaborador ID '{id}' removido!")
        else:
            print(f"Colaborador ID '{id}' não encontrado")
    
    # busca e exibe colaborador
    def buscar_colaborador(self, id: str) -> Optional[Colaborador]:
        colab = self._dao.buscar_por_id(id)
        if colab:
            print(colab.exibir())
        else:
            print(f"Colaborador ID '{id}' não encontrado")
        return colab
    
    # lista todos os colaboradores
    def listar_todos(self) -> List[Colaborador]:
        colaboradores = self._dao.buscar_todos()
        if colaboradores:
            print(f"\nTotal: {len(colaboradores)} colaboradores\n")
            for colab in colaboradores:
                print(colab.exibir())
        else:
            print("Nenhum colaborador cadastrado")
        return colaboradores
    
    # gera relatório no formato especificado
    def gerar_relatorio(self, tipo: str = 'html', salvar_arquivo: bool = False) -> str:
        try:
            colaboradores = self._dao.buscar_todos()
            relatorio_obj = self._factory_relatorio.criar_relatorio(tipo)
            conteudo = relatorio_obj.gerar(colaboradores)
            
            if salvar_arquivo:
                nome_arquivo = f"relatorio_colaboradores.{tipo}"
                with open(nome_arquivo, 'w', encoding='utf-8') as f:
                    f.write(conteudo)
                print(f"Relatório salvo em '{nome_arquivo}'")
            
            return conteudo
            
        except Exception as e:
            print(f"Erro ao gerar relatório: {e}")
            raise
    
    # adiciona seção a um colaborador existente
    def adicionar_secao(self, id_colaborador: str, secao: 'ComponenteCadastro') -> None:
        colab = self._dao.buscar_por_id(id_colaborador)
        if colab:
            colab.adicionar(secao)
            self._dao.atualizar(colab)
            print(f"Seção adicionada ao colaborador '{colab.nome}'")
        else:
            raise ValueError(f"Colaborador ID '{id_colaborador}' não encontrado")
    
    # remove seção de um colaborador
    def remover_secao(self, id_colaborador: str, secao: 'ComponenteCadastro') -> None:
        colab = self._dao.buscar_por_id(id_colaborador)
        if colab:
            colab.remover(secao)
            self._dao.atualizar(colab)
            print(f"Seção removida do colaborador '{colab.nome}'")
        else:
            raise ValueError(f"Colaborador ID '{id_colaborador}' não encontrado")

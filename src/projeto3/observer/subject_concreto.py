from .observer import Subject

# subject concreto que é monitorado
class SistemaMonitorado(Subject):
    
    def __init__(self, nome: str):
        super().__init__()
        self._nome = nome
        self._estado = "iniciado"
    
    # altera estado e notifica observers
    def alterar_estado(self, novo_estado: str) -> None:
        self._estado = novo_estado
        mensagem = f"sistema '{self._nome}' mudou para: {novo_estado}"
        self.notificar(mensagem)
    
    # executa ação e notifica observers
    def executar_acao(self, acao: str) -> None:
        mensagem = f"sistema '{self._nome}' executou: {acao}"
        self.notificar(mensagem)
    
    def obter_estado(self) -> str:
        return self._estado

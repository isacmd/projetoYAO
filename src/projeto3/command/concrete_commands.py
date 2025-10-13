from ..command.command import Command
from ..command.receptor import Receptor

# comando concreto para escrever
class EscreverComando(Command):
    
    def __init__(self, receptor: Receptor, texto: str):
        self._receptor = receptor
        self._texto = texto
    
    def execute(self) -> str:
        return self._receptor.escrever(self._texto)
    
    def undo(self) -> str:
        return self._receptor.apagar(len(self._texto))
    
    def get_name(self) -> str:
        return f"Escrever('{self._texto}')"

# comando concreto para apagar
class ApagarComando(Command):
    
    def __init__(self, receptor: Receptor, n_caracteres: int):
        self._receptor = receptor
        self._n_caracteres = n_caracteres
        self._texto_removido = ""
    
    def execute(self) -> str:
        texto_antes = self._receptor.obter_texto()
        resultado = self._receptor.apagar(self._n_caracteres)
        self._texto_removido = texto_antes[-self._n_caracteres:]
        return resultado
    
    def undo(self) -> str:
        return self._receptor.escrever(self._texto_removido)
    
    def get_name(self) -> str:
        return f"Apagar({self._n_caracteres})"

# comando concreto para limpar
class LimparComando(Command):
    
    def __init__(self, receptor: Receptor):
        self._receptor = receptor
        self._texto_anterior = ""
    
    def execute(self) -> str:
        self._texto_anterior = self._receptor.obter_texto()
        return self._receptor.limpar()
    
    def undo(self) -> str:
        return self._receptor.escrever(self._texto_anterior)
    
    def get_name(self) -> str:
        return "Limpar()"

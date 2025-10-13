from typing import List
from .command import Command

# invoker que gerencia execução de comandos
class Executor:
    
    def __init__(self):
        self._historico: List[Command] = []
        self._posicao = 0
    
    def executar(self, comando: Command) -> str:
        # remove comandos à frente se estiver no meio do histórico
        self._historico = self._historico[:self._posicao]
        
        resultado = comando.execute()
        self._historico.append(comando)
        self._posicao += 1
        
        return f"[EXECUTADO] {comando.get_name()}: {resultado}"
    
    def desfazer(self) -> str:
        if self._posicao > 0:
            self._posicao -= 1
            comando = self._historico[self._posicao]
            resultado = comando.undo()
            return f"[DESFEITO] {comando.get_name()}: {resultado}"
        return "[ERRO] Nada para desfazer"
    
    def refazer(self) -> str:
        if self._posicao < len(self._historico):
            comando = self._historico[self._posicao]
            resultado = comando.execute()
            self._posicao += 1
            return f"[REFEITO] {comando.get_name()}: {resultado}"
        return "[ERRO] Nada para refazer"
    
    def mostrar_historico(self) -> str:
        if not self._historico:
            return "Histórico vazio"
        
        resultado = "HISTÓRICO DE COMANDOS:\n"
        for i, cmd in enumerate(self._historico):
            marcador = "*" if i == self._posicao - 1 else " "
            resultado += f"{marcador} {i+1}. {cmd.get_name()}\n"
        return resultado

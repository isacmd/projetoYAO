from typing import List
from .observer import Observer

# observer que monitora e exibe no console
class MonitorConsole(Observer):
    
    def __init__(self, nome: str):
        self._nome = nome
    
    def atualizar(self, mensagem: str) -> None:
        print(f"[CONSOLE-{self._nome}] {mensagem}")

# observer que registra em log
class MonitorLog(Observer):
    
    def __init__(self):
        self._log: List[str] = []
    
    def atualizar(self, mensagem: str) -> None:
        from datetime import datetime
        timestamp = datetime.now().strftime("%H:%M:%S")
        entrada = f"[{timestamp}] {mensagem}"
        self._log.append(entrada)
        print(f"[LOG] Registrado: {mensagem}")
    
    def obter_log(self) -> List[str]:
        return self._log.copy()
    
    def salvar_log(self, arquivo: str = "sistema.log") -> None:
        with open(arquivo, 'w', encoding='utf-8') as f:
            f.write('\n'.join(self._log))
        print(f"Log salvo em '{arquivo}'")

# observer que simula envio de email
class MonitorEmail(Observer):
    
    def __init__(self, email: str):
        self._email = email
    
    def atualizar(self, mensagem: str) -> None:
        print(f"[EMAIL] Enviando para {self._email}: {mensagem}")

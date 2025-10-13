

# receptor que realiza as ações reais
class Receptor:
    
    def __init__(self):
        self._texto = ""
        self._historico = []
    
    def escrever(self, texto: str) -> str:
        self._historico.append(self._texto)
        self._texto += texto
        return f"Texto escrito: '{texto}'"
    
    def apagar(self, n_caracteres: int) -> str:
        self._historico.append(self._texto)
        removido = self._texto[-n_caracteres:]
        self._texto = self._texto[:-n_caracteres]
        return f"Apagado: '{removido}'"
    
    def restaurar(self) -> str:
        if self._historico:
            self._texto = self._historico.pop()
            return "Estado restaurado"
        return "Nada para restaurar"
    
    def obter_texto(self) -> str:
        return self._texto
    
    def limpar(self) -> str:
        self._historico.append(self._texto)
        self._texto = ""
        return "Texto limpo"

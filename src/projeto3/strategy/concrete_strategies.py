from .strategy import Strategy
from typing import List

# estratégia de ordenação bubble sort
class OrdenacaoBubbleSort(Strategy):
    
    def executar(self, dados: List[int]) -> List[int]:
        resultado = dados.copy()
        n = len(resultado)
        
        for i in range(n):
            for j in range(0, n-i-1):
                if resultado[j] > resultado[j+1]:
                    resultado[j], resultado[j+1] = resultado[j+1], resultado[j]
        
        return resultado
    
    def get_nome(self) -> str:
        return "Bubble Sort"

# estratégia de ordenação quick sort
class OrdenacaoQuickSort(Strategy):
    
    def executar(self, dados: List[int]) -> List[int]:
        if len(dados) <= 1:
            return dados
        
        pivot = dados[len(dados) // 2]
        menores = [x for x in dados if x < pivot]
        iguais = [x for x in dados if x == pivot]
        maiores = [x for x in dados if x > pivot]
        
        return self.executar(menores) + iguais + self.executar(maiores)
    
    def get_nome(self) -> str:
        return "Quick Sort"

# estratégia de ordenação merge sort
class OrdenacaoMergeSort(Strategy):
    
    def executar(self, dados: List[int]) -> List[int]:
        if len(dados) <= 1:
            return dados
        
        meio = len(dados) // 2
        esquerda = self.executar(dados[:meio])
        direita = self.executar(dados[meio:])
        
        return self._merge(esquerda, direita)
    
    def _merge(self, esquerda: List[int], direita: List[int]) -> List[int]:
        resultado = []
        i = j = 0
        
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] <= direita[j]:
                resultado.append(esquerda[i])
                i += 1
            else:
                resultado.append(direita[j])
                j += 1
        
        resultado.extend(esquerda[i:])
        resultado.extend(direita[j:])
        return resultado
    
    def get_nome(self) -> str:
        return "Merge Sort"

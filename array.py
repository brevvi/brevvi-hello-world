#!/usr/bin/env python
import numpy as np
# array
data = np.array([2,4,6,8,10])
# array gerada de forma ordenada
data = np.arange(15)
# array gerada aleatóriamente com numeros decimais
data = np.random.rand(15)
# array gerada aleatoriamente com numeros inteiros
data = np.random.randint(10, size=15)
# array gera matriz com linhas e colunas - bidimensional
data = np.random.randint(5, size=(3,4))
# array gera matriz com linhas e colunas - tridimensional
data = np.random.randint(5, size=(5,3,4))
# array com conteudo gerado manualmente
data = np.array([[1,2,3,4],[2,3,4,5]])
# visualização
print('tipo dos dados:\n',type(data))
print('quantida de linhas e colunas:', data.shape)
print('tamanho da matriz de dados:', data.size)
print('dimensão dos dados:', data.ndim)
print('matriz de dados:\n', data)
print(f'O elemento de maior valor é: {data.max()}')
print(f'Cada elemento possui {data.itemsize} bytes')
print(f'Toda a matriz possui {data.nbytes} bytes')

# Manipulação de Imagens com OpenCV

Este projeto demonstra várias técnicas de manipulação e análise de imagens usando a biblioteca OpenCV em Python. O código realiza uma série de operações, incluindo leitura de imagens, pré-processamento, aplicação de filtros, detecção de características, transformações geométricas, segmentação e análise de textura.

## Funcionalidades

- **Leitura e Exibição de Imagens**: Carrega e exibe uma imagem a partir do disco.
- **Pré-processamento**:
  - Conversão de imagens para escala de cinza.
  - Redimensionamento de imagens.
  - Equalização de histograma para melhorar o contraste.
- **Aplicação de Filtros**:
  - Desfoque Gaussiano para suavização.
  - Detecção de bordas usando o algoritmo Canny.
- **Detecção de Contornos**: Encontra e desenha contornos na imagem.
- **Transformações Geométricas**:
  - Rotação e translação da imagem.
- **Operações Morfológicas**: Erosão e dilatação de imagens.
- **Segmentação de Imagens**: Limiarização para segmentar objetos.
- **Combinação de Imagens**: Mescla imagens usando operações aritméticas.
- **Análise de Textura**: Implementação do algoritmo Local Binary Patterns (LBP).

## Requisitos

- Python 3.x
- Bibliotecas:
  - OpenCV
  - NumPy
  - Matplotlib

Você pode instalar as bibliotecas necessárias usando:

```bash
pip install opencv-python numpy matplotlib

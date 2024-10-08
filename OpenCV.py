import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_image(title, image):
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

# Leitura e Exibição de Imagens
image_path = 'Amanhecer.jpg'  # Certifique-se de que o caminho da imagem está correto
image = cv2.imread(image_path)
display_image('Imagem Original', image)

# Pré-processamento de Imagens
# Conversão de Cores
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
display_image('Imagem em Escala de Cinza', gray_image)

# Redimensionamento
resized_image = cv2.resize(image, (400, 400))
display_image('Imagem Redimensionada', resized_image)

# Equalização de Histograma
equalized_image = cv2.equalizeHist(gray_image)
display_image('Imagem Equalizada', equalized_image)

# Aplicação de Filtros
# Desfoque
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
display_image('Imagem Desfocada', blurred_image)

# Detecção de Bordas
edges = cv2.Canny(image, 100, 200)
display_image('Detecção de Bordas (Canny)', edges)

# Detecção de Contornos
contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contour_image = np.zeros(image.shape, dtype=np.uint8)
cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 3)
display_image('Contornos Detectados', contour_image)

# Transformações Geométricas
# Rotação
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))
display_image('Imagem Rotacionada', rotated_image)

# Translação
translation_matrix = np.float32([[1, 0, 100], [0, 1, 50]])
translated_image = cv2.warpAffine(image, translation_matrix, (w, h))
display_image('Imagem Transladada', translated_image)

# Erosão e Dilatação
kernel = np.ones((5, 5), np.uint8)
eroded_image = cv2.erode(image, kernel, iterations=1)
dilated_image = cv2.dilate(image, kernel, iterations=1)
display_image('Imagem Erosão', eroded_image)
display_image('Imagem Dilatação', dilated_image)

# Segmentação de Imagens
_, thresholded_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)
display_image('Imagem Limiarizada', thresholded_image)

# Combinação e Operações Aritméticas
blended_image = cv2.addWeighted(image, 0.5, blurred_image, 0.5, 0)
display_image('Imagem Blend', blended_image)

# Salvar Imagens Processadas
cv2.imwrite('imagem_processada.jpg', blended_image)
print("Imagem processada salva como 'imagem_processada.jpg'.")

# Análise de Textura (Local Binary Patterns)
def local_binary_patterns(image, P=8, R=1):
    lbp = np.zeros_like(image)
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            center = image[i, j]
            binary_str = ''
            for p in range(P):
                theta = 2 * np.pi * p / P
                x = int(i + R * np.sin(theta))
                y = int(j + R * np.cos(theta))
                binary_str += '1' if image[x, y] >= center else '0'
            lbp[i, j] = int(binary_str, 2)
    return lbp

lbp_image = local_binary_patterns(gray_image)
display_image('LBP - Local Binary Patterns', lbp_image)

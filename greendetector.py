import cv2
import numpy as np

# Define the color numeration for green in HSV
lower_green = np.array([36, 0, 0])
upper_green = np.array([86, 255, 255])

hex = ''

# Convert the hexadecimal color to RGB. Função booleana que retorna true se verde, false se outra cor.
def detectar_verde(hex):  
    rgb = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

    # Convert the RGB color to HSV
    hsv = cv2.cvtColor(np.uint8([[rgb]]), cv2.COLOR_RGB2HSV)[0][0]

    # Check if the color is green
    if lower_green[0] <= hsv[0] <= upper_green[0]:
        return True
        # a cor é verde
    else:
        return False
        #a cor não é verde

import cv2
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\hyers\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

img = cv2.imread(r"D:\Repositorios\Sotano\Screenshots\Captura de pantalla (7).png")

# Región de interés para el caso de las etiquetas
x, y, w, h = 67, 160, 923, 73
crop = img[y:y+h, x:x+w]
cv2.imwrite(r"D:\Repositorios\InformeManttoInsitel\extracciones\roi_preview.png", crop)
# roi = cv2.selectROI("Selecciona el rectángulo", img, fromCenter=False, showCrosshair=True)
# x, y, w, h = roi
# crop = img[y:y+h, x:x+w]
# print(roi)

gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
gray = cv2.resize(gray, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
gray = cv2.GaussianBlur(gray, (3, 3), 0)
_, th = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
invertido = cv2.bitwise_not(th)

# Aislar texto blanco sobre fondo rojo
# hsv = cv2.cvtColor(crop, cv2.COLOR_BGR2HSV)
# mask = cv2.inRange(hsv, np.array([0, 0, 160]), np.array([180, 80, 255]))
# crop_white = cv2.bitwise_and(crop, crop, mask=mask)

# Preprocesado
# gray = cv2.cvtColor(crop_white, cv2.COLOR_BGR2GRAY)
# gray = cv2.GaussianBlur(gray, (3, 3), 0)
# _, th = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Aumentar tamaño para OCR
# th = cv2.resize(th, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)

# OCR
# texto = pytesseract.image_to_string(
#     th,
#     lang="eng",
#     config="--psm 6 --oem 1"
# )
# print(texto)

cv2.imshow("Etiquetas", th)
cv2.waitKey(0)
cv2.destroyAllWindows()


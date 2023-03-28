import pytesseract
from PIL import Image

im=Image.open("D:\Temp\Capture.PNG")
result= pytesseract.image_to_string(im,lang="chi_sim")
print(result)
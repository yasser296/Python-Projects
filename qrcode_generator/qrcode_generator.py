# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode
from datetime import datetime
  
 
date_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# String which represents the QR code
s = "https://drive.google.com/drive/folders/1zlKaendICJ3S9KcL0963le2b0NQPfkZn?usp=sharing"

  
# Generate QR code
url = pyqrcode.create(s)
  
# Create and save the svg file naming "myqr.svg"
url.svg(f"E:/python_projects/qrcode_generator/myqr_{date_time}.svg", scale = 10)
  
# Create and save the png file naming "myqr.png"
url.png(f'E:/python_projects/qrcode_generator/myqr_{date_time}.png', scale = 10)
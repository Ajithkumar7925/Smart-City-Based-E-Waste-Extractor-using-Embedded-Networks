# Import QRCode from pyqrcode

import pyqrcode
import png
from objectdetectionyolo import text1
from pyqrcode import QRCode

a=input(text1)
# String which represents the QR code
if a=="mobile phone":
    s = 'Congrats on getting Rs.100'
if a=="Watch":
    s='Congrats'
# Generate QR code
url = pyqrcode.create(s)

# Create and save the svg file naming "myqr.svg"
url.svg("myqr.svg", scale = 8)

# Create and save the png file naming "myqr.png"
url.png('myqr.png', scale = 6)



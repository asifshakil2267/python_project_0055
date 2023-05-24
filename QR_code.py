import pyqrcode
import QR_code
import png
from pyqrcode import QRCode
import xml.etree.ElementTree as ET
# Define your information
name = "Asif Mahmud"
university = "IUB"
Loacation="Dhaka,Bangladesh"
phone_number = "01608433108"
email="asif.mahmud2337@gmail.com"
fcaebook="https://www.facebook.com/asifmahmud.shakil/"
Linkedin="https://www.linkedin.com/in/asif-mahmud-shakil-894246231/"

# Concatenate the information into a single string
information = f"Name: {name}\nUniversity: {university}\nStudent name: {Loacation}\nPhone Number: {phone_number}\n{email} "

# Generate QR code
url = pyqrcode.create(information)

# Save the QR code as SVG and PNG files
url.svg("myqr.svg", scale=8)
url.png("myqr.png", scale=6)
#QR_code.py
qr = QR_code.QRCode(version=1, error_correction=QR_code.constants.ERROR_CORRECT_H, box_size=10, border=4)
qr.add_data('Your QR Code Data')
qr.make(fit=True)

# Create an SVG element
svg_root = ET.Element('svg')
svg_root.set('xmlns', 'http://www.w3.org/2000/svg')
svg_root.set('height', '456')
svg_root.set('width', '456')
svg_root.set('class', 'pyqrcode')

# Add the QR code data as SVG path
path_element = ET.SubElement(svg_root, 'path')
path_element.set('d', qr.make_path())

# Convert SVG element to string
svg_string = ET.tostring(svg_root, encoding='unicode')

# Print the SVG code
print(svg_string)
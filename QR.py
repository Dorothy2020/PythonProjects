import pyqrcode 
from pyqrcode import QRCode 


#string that contain the qr code
s="https://www.youtube.com/channel/UCeO9hPCfRzqb2yTuAn713Mg"

#Generate QR code
url = pyqrcode.create(s) 

#create and save the photo

url.svg("myyoutube.svg", scale = 8)
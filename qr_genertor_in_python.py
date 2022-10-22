#simple qr code 
import qrcode as qr
image = qr.make("https://www.youtube.com/channel/UCPw26W1K_pBqUd6eaWlKCQQ")
image.save("KP.png")

#QR code with diffrernt colour

from PIL import Image
qr = qr.QRCode(version=1,error_correction=qr.ERROR_CORRECT_H,box_size=10,border=4)
qr.add_data("https://www.youtube.com/channel/UCPw26W1K_pBqUd6eaWlKCQQ")
qr.make(fit=True)
img=qr.make_image(fill_color="black",back_color="green")
img.save("KP2.png")



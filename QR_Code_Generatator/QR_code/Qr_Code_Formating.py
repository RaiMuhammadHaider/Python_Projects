import qrcode
from PIL import Image
qr = qrcode.QRCode(
    version=1,
    box_size= 10,
    border= 4,
    error_correction=qrcode.constants.ERROR_CORRECT_H,

                   )

qr.add_data('https://pk.linkedin.com/in/raimuahmmadhaider')
qr.make(fit=True)
img = qr.make_image(fill_color = 'red', back_color = 'blue')
img.save('Rai_Muhammad_Haider.png')

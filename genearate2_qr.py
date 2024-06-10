import qrcode
from PIL import Image

# Create a QR Code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=15,
    border=5
)

# Add data to the QR Code
qr.add_data("https://youtube.com/shorts/n-NEYcndYog?si=GXPcoHiP2qkgWV6f")
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="red", back_color="blue")

# Save the image
img.save("rs7_car.png")

print("QR code has been generated and saved as rs7_car.png")



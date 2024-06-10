import qrcode

# URL to be encoded in the QR code
url = "https://youtu.be/lxrQHgpSZ7Q?si=xSKPnKnlOfy0QAD0"

# Generate the QR code
try:
    img = qrcode.make(url)
    img.save("food_video.png")
    print("QR code has been generated and saved as food_video.png")
except Exception as e:
    print(f"An error occurred: {e}")




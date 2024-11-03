import qrcode

# Generate QR code
data = input("Enter the URL")
file_name = input("Enter the file name: ")
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color = "black", back_color = "white")
image.save(file_name + ".png")
print("Image saved")

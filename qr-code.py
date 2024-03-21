import qrcode
# features = qrcode.QRCode(version=1, box_size=45, border=5)
# features.add_data('https://www.w3schools.com')
# features.make(fit=True)
generate_image = qrcode.make("Hello World!!!")
# generate_image = features.make_image(fill_color="blue", back_color="white")
generate_image.save('image1.png')
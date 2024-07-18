import qrcode


def qrcodegenerator(url, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)


url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
file_name = "random"
qrcodegenerator(url, file_name)
print(f"generated:{file_name} qr code!")

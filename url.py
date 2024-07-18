# import qrcode


# def qrcodegenerator(URL, filename):
#     qr = qrcode.QRCode(
#         version=1,
#         error_correction=qrcode.constants.ERROR_CORRECT_L,
#         box_size=10,
#         border=4,
#     )
#     qr.add_data(URL)
#     qr.make(fit=True)

#     png = qr.make_image(fill_color="black", back_color="white")
#     png.save(filename)


# URL = "https://www.youtube.com/watch?v=syaTC8-PHyA"
# file_name = "most annoying sound"
# qrcodegenerator(URL, file_name)
# print(f"QR code generated and saved as {file_name}")


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
# 10:33:43 / 13:40:09

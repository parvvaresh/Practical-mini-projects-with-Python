import qrcode


def make_QR_Code(link, colors_f, colors_b):
    
    img = qrcode.make(link)
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
  )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color=colors_f, back_color=colors_b).convert('RGB')
    img.save("Qr.png")
      
      
color_f = input("please enter color  Qr code : ")
color_b = input("please enter color backqrund Qr code : ")

temp = input("please entered link or text who want to qr code : ")

make_QR_Code(temp,color_f,  color_b)



print("finished")


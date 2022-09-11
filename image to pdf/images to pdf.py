from PIL import Image
def Image_Pdf(filename, output = "images.pdf"):
  images = []
  for file in filename:
    im = Image.open(file)
    im = im.convert('RGB')
    images.append(im)
  images[0].save(output, save_all=True, append_images=images[1:])

Image_Pdf(['/content/photo_2022-09-11_13-37-51.jpg', '/content/photo_2022-09-11_13-37-59.jpg', '/content/photo_2022-09-11_13-38-05.jpg', '/content/photo_2022-09-11_13-38-11.jpg', '/content/photo_2022-09-11_13-38-18.jpg', '/content/photo_2022-09-11_13-38-23.jpg'])
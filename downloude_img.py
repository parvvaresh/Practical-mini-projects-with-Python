import os
import requests
from bs4 import *
#-------------------------------------------------

def create_folder(imgs):
  try:
    folder_name = input("enter folder name : ")
    os.mkdir(folder_name)
  except:
    print("Folder Exist with that name!")
    create_folder()
  finally:
    dl_img(imgs, folder_name)
#---------------------------------------------
def dl_img(imgs, folder):
  count_img= 0
  print(f"{len(imgs)} found :))")

  if len(imgs) != 0:
    for i, img in enumerate(imgs):
      try:
        img_link = img['data-srcset']
      except:
        try:
          img_link = img['data-src']
        except:
          try:
            img_link = img['data-fallback-src"']
          except:
            try:
              img_link = img['src']
            except:
              pass
    try:
      r = requests.get(img_link).content
      try:
        r = str(r, 'utf-8')
      except UnicodeDecodeError:
        with open(f"{folder}/imgs{i+1}.jpg", "wb+") as f:
          f.write(r)
        
        count_img += 1

    except:
      pass
    if count_img == len(imgs):
      print("All imges Downlouded!")
    else:
      print(f"totla images downloude{count_img} and total images find in site{len(imgs)}")
#--------------------------------------------------------

def main(url_temp):
  r = requests.get(url_temp)
  soup = BeautifulSoup(r.text, 'html.parser')
  imgs = soup.findAll('img')
  create_folder(imgs)

#----------------------------------------------------------
url = input("Enter Url : ___")

main(url)

  

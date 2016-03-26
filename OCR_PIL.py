from PIL import Image, ImageFilter

def blurYourLena():
    lena = Image.open("E:\lena.jpg")
    blurryLena = lena.filter(ImageFilter.GaussianBlur)
#     blurringLena.save("blurryLena.jpg")
    blurryLena.show()


if __name__ == '__main__':
    blurYourLena()
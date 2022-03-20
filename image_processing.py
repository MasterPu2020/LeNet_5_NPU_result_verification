
from PIL import Image

total = input("the total number of images\n")
total = int(total)

for i in range(1, total + 1):
    img = Image.open("./unprocessed_image/" + str(i) + ".png")
    img.thumbnail((32, 32))
    new_img = img.convert('L')
    new_img.thumbnail((32, 32))
    # img.show()
    # new_img.show()
    new_img.save("./processed_image" + "/p_" + str(i) + ".png", "PNG")

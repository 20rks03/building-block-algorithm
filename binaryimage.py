from PIL import Image
srcImage = Image.open("cube.jpg")
grayImage = srcImage.convert('L')
binarizedImage = grayImage.point(lambda x: 0 if x<128 else 255, '1')

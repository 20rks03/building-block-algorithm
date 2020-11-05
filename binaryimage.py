from PIL import Image
srcImage = Image.open("cube.jpg")
grayImage = srcImage.convert('L')
binarizedImage = grayImage.point(lambda x: 0 if x<128 else 255, '1')

'''
code from
https://stackoverflow.com/questions/55166930/image-to-0-1-text
'''

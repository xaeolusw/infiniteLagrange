from PIL import Image

#显示图片
image = Image.open('./test/img/pig.jpg')
image.format, image.size, image.mode
('JPEG', (500, 750), 'RGB')
image.show()

exit()
#裁剪
rect = 80, 20, 310, 360
image.crop(rect).show()

#生成缩略图
image = Image.open('./test/pig.jpg')
size = 128, 128
image.thumbnail(size)
image.show()

#缩放和黏贴图像
image1 = Image.open('./test/pig.jpg')
image2 = Image.open('./res/ball.png')
rect = 80, 20, 310, 360
guido_head = image2.crop(rect)
width, height = guido_head.size
image1.paste(guido_head.resize((int(width / 1.5), int(height / 1.5))), (172, 40))
image1.show()

#旋转和翻转
image = Image.open('./test/pig.jpg')
image.rotate(180).show()
image.transpose(Image.FLIP_LEFT_RIGHT).show()

# 操作像素
image = Image.open('./test/pig.jpg')
print(image.size)
for x in range(200, 300):
   for y in range(200, 300):
    image.putpixel((x, y), (128, 128, 128))
image.show()
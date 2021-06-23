# Python程序设计 作业

4. [数字照片墙](https://blog.csdn.net/u013748897/article/details/117996577)
5. [送你一首集句诗](https://blog.csdn.net/u013748897/article/details/118028280)

@[TOC](Python程序设计 作业4 数字照片墙)

# 设计思路：

使用`Pillow`分别构建同样大小的图片`text.jpg`、`wall.jpg`，再根据两张图片的相同位置的像素情况构建`final.jpg`

# 实现方案

首先将图片统一重命名待用。然后构建`text.jpg`来存放照片墙的文字图层。之后随机选择照片，调整其大小，按顺序粘贴组成一张大的图片`wall.jpg`来存放照片墙的背景图层。最后新建一张空的大小一样的图片`final.jpg`。通过`Pillow.getpixel()`获取两张图的像素信息，逐个像素进行比较，若`text.jpg`中的一点像素为大红色，则对`final.jpg`的同一点使用`Pillow.putpixel()`赋同一点处`wall.jpg`的像素信息。

# 关键代码说明

## 构建文字图层

```python
text="41802198" # 设置文字图层内容
ft=ImageFont.truetype("shuma.ttf", int(BIG_HEIGHT*1))   # 选择字体和字体大小
text_image=Image.new("RGB", (BIG_WIDTH,BIG_HEIGHT)) # 新建一张空图
draw = ImageDraw.Draw(text_image)
draw.text((0,0), text,font=ft,fill="red")   # 写入字
text_image.save("text.jpg")
```

## 构建背景图层

```python
wall_image=Image.new("RGB", (BIG_WIDTH,BIG_HEIGHT)) # 新建空图
# 通过循环粘贴小图片成大图片
for x in range(BIG_WIDTH//SMALL_WIDTH):
    for y in range(BIG_HEIGHT//SMALL_HEIGHT):
        num=random.randint(1,10)    # 随机选图
        tmp=Image.open("photo/"+str(num)+".jpg")
        tmp=tmp.resize((SMALL_WIDTH,SMALL_HEIGHT),Image.NEAREST)    # 调整大小
        wall_image.paste(tmp,(x*SMALL_WIDTH,y*SMALL_HEIGHT))  #粘贴图片   
wall_image.save("wall.jpg")
```

## 构建最终图片

```python
wall_image=Image.new("RGB", (BIG_WIDTH,BIG_HEIGHT)) # 新建空图
# 通过循环粘贴小图片成大图片
for x in range(BIG_WIDTH//SMALL_WIDTH):
    for y in range(BIG_HEIGHT//SMALL_HEIGHT):
        num=random.randint(1,10)    # 随机选图
        tmp=Image.open("photo/"+str(num)+".jpg")
        tmp=tmp.resize((SMALL_WIDTH,SMALL_HEIGHT),Image.NEAREST)    # 调整大小
        wall_image.paste(tmp,(x*SMALL_WIDTH,y*SMALL_HEIGHT))  #粘贴图片   
wall_image.save("wall.jpg")
```

# 效果展示

![照片墙](https://img-blog.csdnimg.cn/20210618162145251.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTM3NDg4OTc=,size_16,color_FFFFFF,t_70#pic_center)


# 心得体会

本次作业考察的主要对图片的操作，难度不大。需要我们对图片各种格式、通道有所了解。其余的无非就是一些简单的判断以及赋值。本次作业完成的方法有很多，每一种都能帮助我们更好地学习图片的相关知识，希望大家都能多尝试几种方法，学习到更多相关知识。

本作业已上传至Github以及Gitee，希望各位能点个star再走 :smile:。

[GitHub](https://github.com/GLORYFeonix/Python_Learning_Homework)

[Gitee](https://gitee.com/gzy8810/Python_Learning_Homework)

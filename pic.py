# -*- encoding: UTF-8 -*-

import utils
import pandas as pd
import mail_util as mailUtil

from threading import Thread
import talib as tl
import cv2
import numpy as np
from PIL import ImageFont, Image, ImageDraw


# 生成一张图片
def create_pic():
    width = 256
    height = 256
    img = np.zeros([width, height, 3], dtype=np.uint8)
    # 遍历每个像素点，并进行赋值
    for i in range(width):
        for j in range(height):
            #img[i, j, :] = [i % 256, j % 256, (i + j) % 256]
            img[i, j, :] = [i % 256, j % 256, 0]
            # img[i,j,:] = [255,255,255]

    # 展示图片
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    # cv2.imshow('image', img)
    cv2.imwrite("image.jpg", img)
    # cv2.waitKey(0)
    cv2.destroyAllWindows()


# 在图片中写入文字
def write_pic(number):
    bk_img = cv2.imread("image.jpg")
    # 设置需要显示的字体
    fontpath = "font/simsun.ttc"
    font = ImageFont.truetype(fontpath, 32)
    img_pil = Image.fromarray(bk_img)
    draw = ImageDraw.Draw(img_pil)

    # 绘制文字信息
    draw.text((0, 0), "AbbbbbbbbbbbbbbbbbBDDDC".encode('utf-8'), fill=(0, 0, 0))
    draw.text((0, 50), number, fill=(0, 0, 0))
    bk_img = np.array(img_pil)
    # cv2.imshow("add_text", bk_img)
    # cv2.waitKey()
    createName = number + ".jpg"
    cv2.imwrite(createName, bk_img)


if __name__ == '__main__':
    s =  np.zeros([2, 3, 4,5], dtype=np.uint8)
    print(s)
    create_pic()
    for i in range(1, 2):
        write_pic('BB' + "_" + str(i))
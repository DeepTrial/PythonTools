import cv2
import numpy as np
from glob import glob
import matplotlib.pyplot as plt


def visualize(image,subplot):
    """
    将多张大小相同的图片拼接
    :param image: 图片列表
    :param subplot: 行列数[row,col]
    :return: 拼接图
    """
    row=subplot[0]
    col=subplot[1]
    height,width=image[0].shape[:2]
    result=np.zeros((height*row,width*col,3))

    total_image=len(image)
    index=0
    for i in range(row):
        for j in range(col):
            row_index=i*height
            col_index=j*width
            if index<total_image:
                try:  #单通道灰度图与3通道彩色图单独处理
                    result[row_index:row_index+height,col_index:col_index+width,:]=image[index]
                except:
                    result[row_index:row_index + height, col_index:col_index + width, 0] = image[index]
                    result[row_index:row_index + height, col_index:col_index + width, 1] = image[index]
                    result[row_index:row_index + height, col_index:col_index + width, 2] = image[index]
            index=index+1
    result=result.astype(np.uint8)
    result=cv2.cvtColor(result,cv2.COLOR_RGB2BGR)
    return result

def imgRead(filepath,filetype):
    fileList=glob(filepath+filetype)
    images=[]
    for file in fileList:
        image=plt.imread(file)
        images.append(image)
    return images


if __name__=="__main__":
    filepath=r'F:\GithubRepo\PythonTools\ImageTool\ImageStitching\test'
    filetype=r"\*.bmp"

    print("[INFO] Reading Image ...")
    images=imgRead(filepath,filetype)
    total_images=len(images)

    print("[INFO] Generating Stitching Image...")
    if total_images % 4 == 0:
        row = total_images / 4
        col = 4
    else:
        if total_images % 5 != 0:
            row = total_images // 5 + 1
        else:
            row = total_images // 5
        col = 5

    imagePatch = visualize(images, [row, col])
    cv2.imwrite("image_patch.jpg", imagePatch)





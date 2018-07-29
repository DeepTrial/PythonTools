import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import cv2

def Gray_3D(image):
	X=np.arange(0,image.shape[0],1)
	Y = np.arange(0, image.shape[1], 1)
	X, Y = np.meshgrid(X, Y)
	Z=image[X,Y]
	Z=np.asarray(Z)
	fig = plt.figure()
	ax = Axes3D(fig)
	ax.plot_surface(X,Y,Z,rstride=1, cstride=1, cmap='rainbow')
	plt.show()


if __name__=="__main__":
	img=plt.imread("test.jpg")
	gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
	plt.imshow(gray,cmap="gray")
	plt.show()
	Gray_3D(gray)
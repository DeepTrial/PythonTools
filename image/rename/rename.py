import os
import threading
import cv2

path = r"F:\GithubRepo\PythonTools\ImageTool\ImageConvert(batch)\test"
prefixFileName="pos-"
saveType=".jpg"

#find all files under this dir
filelist = os.listdir(path)


# change file name
def changeBatch(start=1,end=1,count=1,specified=False,specified_type=".jpg"):

    for files in filelist[int(start):int(end)]:
        olddir = os.path.join(path,files)

        #split filename and type
        filename =  os.path.splitext(files)[0]
        filetype =  os.path.splitext(files)[1]
        if (specified==True and specified_type==filetype) or specified==False:
            print("[INFO] Processing:"+olddir)
            # change file type and save images
            image=cv2.imread(olddir)
            newdir = os.path.join(path,prefixFileName+str(count)+saveType)
            cv2.imwrite(newdir,image)
            #slef-gain
            count=count+1
        else:
            continue


if __name__=="__main__":
    changeBatch(0,len(filelist))
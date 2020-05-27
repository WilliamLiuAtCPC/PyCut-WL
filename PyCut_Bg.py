from random import randint
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np    

def decide(img,region,target_dir,newfileNum):
    new_img = np.array(img)
    plt.imshow(new_img) #show()
    plt.axis('off')
    plt.pause(0.01)
    new_img = np.array(region)
    plt.imshow(new_img) #show()
    plt.axis('off')
    plt.pause(0.01)
    decision = input("decision: ")
    if decision == "": # save
        region.save(target_dir+"img"+str(newfileNum)+".jpg")
        newfileNum = newfileNum + 1
    return newfileNum

def rescale(image):
    w = image.size[0]
    h = image.size[1]
    random_size = 480
    return image.resize((round(w/h * random_size),random_size))

def manual_crop_one_img(img,step,target_dir,newfileNum):
    w = img.size[0]
    h = img.size[1]
    if h>480:
        img = rescale(img)
        w = img.size[0]
        h = img.size[1]
    size = 224
    for i in range(1):
        if (w-size>0) and (h - size>0):
            new_left = randint(0,w - size)
            new_upper = randint(0,h - size)
            region = img.crop((new_left,new_upper,size+new_left,size+new_upper))
            newfileNum = decide(img,region,target_dir,newfileNum)
    return newfileNum

def makeRecord(fileStart,newfileNum):
    f = open("record.txt","w")
    f.write(str(fileStart)+'\n')
    f.write(str(newfileNum)+'\n')
    f.close()

def crop_all(root_path,file_range,target_dir,newfileNum):
    fileNum = file_range[0]
    next_button = input("按Enter开始： ")
    while (fileNum<=file_range[1]) and (next_button == ""):
        filename = "img"+str(fileNum)+".jpg"
        img = Image.open(root_path+filename).convert('RGB')
        newfileNum = manual_crop_one_img(img,step,target_dir,newfileNum)
        print(filename+" finished!")
        fileNum = fileNum + 1
        next_button = input("是否下一张图片？Enter默认下一图;其他键结束")
    
    print("**************休息时间**************")
    if fileNum<=file_range[1]:
        makeRecord(fileNum,newfileNum)
        print("原始图片序号fileStart初始值改为 fileStart = ",fileNum)
        print("新图片序号newfileNum初始值改为 newfileNum = ",newfileNum)
        print("如需更换文件夹，请将二者赋1，并调整路径与fileEnd")
    else:
        makeRecord(1,1)
        print("本文件夹任务已全部完成，重置 fileStart = 1，newfileNum = 1")
        print("请更换文件夹，并调整root,target与fileEnd")

if __name__ == '__main__':
    step = [80,80] #xy_step
    
    #read the record
    f = open("record.txt","r")
    temp = f.readline()
    temp = temp.rstrip('\n')
    fileStart = int(temp)
    temp = f.readline()
    temp = temp.rstrip('\n')
    newfileNum = int(temp)
#    print(fileStart," ",newfileNum)
    f.close()
    
    
    root_path = "H:/VideoClips/SingleSamples/Background/"
    target_dir = "H:/VideoClips/CroppedSamples/Background/"
    fileEnd = 23101 #包内图片数   
#Hook
#2335
#3220
    
#Grasper
#2004
#3246
    
    file_range = [fileStart,fileEnd]
    
    crop_all(root_path,file_range,target_dir,newfileNum)
    
    
    
#    filename = "img"+str(fileNum)+".jpg"
#    img = Image.open(root+filename).convert('RGB')
#    newfileNum = manual_crop_one_img(img,step,target_dir,newfileNum)
#    print(newfileNum)
#    img.show()
#    
#    img = manual_crop(img,step)

#    img.save(IMAGE_PATH+"img_2.jpg")
    

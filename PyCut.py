
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np    

def decide(img,region,target_dir,newfileNum):
    new_img = np.array(img)
    plt.imshow(new_img) #show()
    plt.axis('off')
    plt.pause(0.01)
    is_ok = 0
    new_img = np.array(region)
    plt.imshow(new_img) #show()
    plt.axis('off')
    plt.pause(0.01)
    decision = input("decision: ")
    if decision == "1": # save
        region.save(target_dir+"img"+str(newfileNum)+".jpg")
        newfileNum = newfileNum + 1
    elif decision == "3": # quit
        is_ok = 1
    elif decision == "2": # next line
        is_ok = 2
    return newfileNum,is_ok

def rescale(image):
    w = image.size[0]
    h = image.size[1]
    random_size = 480
    return image.resize((round(w/h * random_size),random_size))

def manual_crop_one_img(img,step,target_dir,newfileNum):
    tl_corner_position = [0,0] #(x,y)
    w = img.size[0]
    h = img.size[1]
    if h>480:
        img = rescale(img)
        w = img.size[0]
        h = img.size[1]
#    newfileNum = decide(img,target_dir,newfileNum)
    is_ok = 0
    while (tl_corner_position[1]+224<h) and (is_ok==0):
        while (tl_corner_position[0]+224<w) and (is_ok==0):
            region = img.crop((tl_corner_position[0],tl_corner_position[1],tl_corner_position[0]+224,tl_corner_position[1]+224))
            newfileNum,is_ok = decide(img,region,target_dir,newfileNum)
            if is_ok == 2:
                break
            tl_corner_position[0] = tl_corner_position[0]+step[0] #右移slider
        region = img.crop((w-224,tl_corner_position[1],w,tl_corner_position[1]+224))
        if is_ok==0:
            newfileNum,is_ok = decide(img,region,target_dir,newfileNum)
        tl_corner_position[1] = tl_corner_position[1]+step[1] #下移slider
        tl_corner_position[0] = 0
        if is_ok ==2:
            is_ok = 0
    tl_corner_position[1] = h - 224
    while (tl_corner_position[0]+224<w) and (is_ok==0):
        region = img.crop((tl_corner_position[0],tl_corner_position[1],tl_corner_position[0]+224,tl_corner_position[1]+224))
        newfileNum,is_ok = decide(img,region,target_dir,newfileNum)
        tl_corner_position[0] = tl_corner_position[0]+step[0] #右移slider
    if is_ok==0:
        region = img.crop((w-224,tl_corner_position[1],w,tl_corner_position[1]+224))
        newfileNum,is_ok = decide(img,region,target_dir,newfileNum)
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
        filename = "img_"+str(fileNum)+".jpg"
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
        print("本文件夹任1务已全部完成，重置 fileStart = 1，newfileNum = 1")
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
    
    
    root_path = "H:/VideoClips/BalancedSamples/Grasper/"
    target_dir = "H:/VideoClips/CroppedSamples/Grasper/"
    fileEnd = 3000 #包内图片数   
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
    

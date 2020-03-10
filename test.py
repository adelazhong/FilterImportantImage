import glob
import os 
#获取指定目录下的所有图片
list = glob.glob(r"/Users/yingzhong/Documents/chainer-caption-master/dataset/image/w5/*.jpg")
print (list)

#1.读取文件夹下的图片并读取文件名称
#f = open('output2.txt','w') #output.txt - 文件名称及格式 w - writing
    #以这种模式打开文件,原来文件内容会被新写入的内容覆盖,如文件不存在会自动创建
#f.write(list[1])
#f.close()

#2.执行,抓取
for i in range(0,len(list)):
  print (os.system('python sample_code_beam.py \
  --rnn-model ./data/caption_en_model40.model\
  --cnn-model ./data/ResNet50.model \
  --vocab ./data/MSCOCO/mscoco_caption_train2014_processed_dic.json \
  --gpu -1 \
  --img '+list[i]))




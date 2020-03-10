import glob
import os 
#获取指定目录下的所有图片
list = glob.glob(r"/Users/yingzhong/Documents/博士/博二/實習/AIST/chainer-caption-master/dataset/image/w1/*.jpg")
print (list)

#1.读取文件夹下的图片并读取文件名称
f = open('output.txt','w') #output.txt - 文件名称及格式 w - writing
    #以这种模式打开文件,原来文件内容会被新写入的内容覆盖,如文件不存在会自动创建
f.write(list[1])
f.close()

#（未完成）2.执行,抓取
print (os.system('start output.txt'))

#（未完成）3.cos similarity比较
ff = open('Test.txt') #打开文件
data = ff.read() #读取文件
print(data)
ff.close()
word_list1 = data.split(' ', -1)
word_list2 = str.split(' ', -1) #Str为比较的caption

#print(" ".join(word_gen1))
#print(" ".join(word_gen2))

# 去重取并集
union_list = list(set(word_list1).union(set(word_list2)))
# 计算词频
list1_tf = []
list2_tf = []
for index in range(len(union_list)):
    list1_tf.append(word_list1.count(union_list[index]))
    list2_tf.append(word_list2.count(union_list[index]))


print(list1_tf)
print(list2_tf)

# 计算余弦值
numerator_list = []
for index in range(len(union_list)):
    numerator_list.append(list1_tf[index] * list2_tf[index])

numerator = sum(numerator_list)
denominator = math.sqrt(sum(map(lambda x: x*x, list1_tf))) * math.sqrt(sum(map(lambda x: x*x, list2_tf)))
# 求值
cosin = numerator/denominator

print(cosin)


#（未完成）4.相似度排序输出

# oneLine = f.readline()
# print oneLine #读取第一行
# lines = f.readlines() #把内容按行读取至一个list
# print lines
 #关闭


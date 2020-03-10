import csv
import math

csvFile = open("output5.csv", "r")
reader = csv.reader(csvFile)

ff = open('Test5.txt') #打开文件
data = ff.read() #读取文件
print(data)
ff.close()
word_list1 = data.split(' ', -1)

f = open('cosin5.txt','w')

for item in reader:
    print(item[0])
    word_list2 = item[0].split(' ', -1)
    union_list = list(set(word_list1).union(set(word_list2)))
    list1_tf = []
    list2_tf = []
    for index in range(len(union_list)):
        list1_tf.append(word_list1.count(union_list[index]))
        list2_tf.append(word_list2.count(union_list[index]))
        print(list1_tf)
        print(list2_tf)
        print(index)
    numerator_list = []
    for i in range(0,index-1):
        numerator_list.append(list1_tf[i] * list2_tf[i])
    print(numerator_list)
    numerator = sum(numerator_list)
    print(numerator)
    denominator = math.sqrt(sum(map(lambda x: x*x, list1_tf))) * math.sqrt(sum(map(lambda x: x*x, list2_tf)))
    print(denominator)
    cosin = numerator/denominator
    print(cosin)
    f.write(item[1]+","+str(cosin)+"\n")
f.close()
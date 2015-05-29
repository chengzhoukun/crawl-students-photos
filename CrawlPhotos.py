import requests
import threading
import queue
import os
from multiprocessing import Pool

MIN_SIZE = 2000  # 最小的图片大小，防止写入无效数据


def getStuPic(stuNum):
    url = "你要爬取的教务系统的地址"
    tmp = '%d' % stuNum
    while(len(tmp) < 4):
        tmp = "0" + tmp
    url = url + tmp + ".jpg"
    print(url)
    try:
        opener = requests.get(url)
        data = opener.content
        if len(data) < MIN_SIZE:
            return
        path = 'F:\\' + 'pic2\\' + '%s.jpg' % tmp  # 替换成你要存储的本放目录
        print(path)
        with open(path, "wb") as jpg:
            jpg.write(data)
        opener.close()
    except:
        print(url + " not exist")


def main():
    p = Pool(300)
    for year in range(10, 15):  # 循环替换成你要爬取的学号规则
        for college in range(1, 16):
            for subject in range(1, 8):
                for classes in range(1, 8):
                    for student in range(1, 60):
                        number = int('%.2d' % year + '%.3d' % college + '%d' %
                                     subject + '%.2d' % classes + '%.2d' % student)
                        p.apply_async(getStuPic, args=(number,))

                        # getStuPic(number)
    p.close()
    p.join()


if __name__ == '__main__':
    main()

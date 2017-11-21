from urllib.request import urlopen, urlretrieve

import requests
from bs4 import BeautifulSoup
import os


# 导入所需要的模块
class mzitu():
    def all_url(self, url):
        html = urlopen(url)
        bsObj = BeautifulSoup(html, "lxml")
        name = bsObj.h2.get_text()
        avatar = bsObj.find("div", {"class": "cover"}).find("img").attrs['src']
        path = self.mkdir(name)
        urlretrieve("http://www.biqukan.com/" + avatar, path + '\\1.jpg')

    def mkdir(self, path):  ##创建文件夹
        path = path.strip()
        dir = "D:\\test\\photos\\"
        isExists = os.path.exists(os.path.join(dir, path))
        if not isExists:
            print('建了一个名字叫做', path, '的文件夹！')
            os.makedirs(os.path.join(dir, path))
            os.chdir(os.path.join(dir, path))  ##切换到目录
            return dir + path
        else:
            print(path, '文件夹已经存在了！')
            return False

    def request(self, url):  ##这个函数获取网页的response 然后返回
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
            'referer': 'http://www.baidu.com',  # 伪造一个访问来源 "http://www.mzitu.com/100260/2"
        }
        content = requests.get(url, headers=headers)
        return content


# 设置启动函数
def main():
    Mzitu = mzitu()  ##实例化
    Mzitu.all_url('http://www.biqukan.com/0_790')  ##给函数all_url传入参数


main()

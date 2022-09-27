import requests
import os

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}



def getDemoFilePath():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    return current_directory + os.sep


def makeDir(file_path):
    dirs = getDemoFilePath() + os.sep + file_path
    if not os.path.exists(dirs):
        os.mkdir(dirs)
    return file_path


def downloadFile(file_path, url):
    res = requests.get(url, headers=headers)
    if not os.path.exists(file_path):
        with open(file_path, "wb") as code:
            code.write(res.content)


def fileOperate(url_path, file_path, file_type, file_name):
    if (file_type == "directory"):
        url = url_path + "/" + file_name
        path = makeDir(file_path + os.sep + file_name)
        getText(url, path)
    elif (file_type == "file"):
        down_path = file_path + os.sep + file_name
        url = "http://doc.canglaoshi.org/" + file_path.replace("\\", "/") + "/" + file_name
        downloadFile(getDemoFilePath() + down_path, url)

def getText(url_path, file_path):
    try:
        res = requests.get(f"http://doc.canglaoshi.org/{url_path}/?j", headers=headers).json()
    except:
        print(res)
    file_path = makeDir(file_path)
    for i in range(0, len(res)):
        # print(res[i])
        file_type = res[i]["type"]
        file_name = res[i]["name"]
        fileOperate(url_path, file_path, file_type, file_name)
    return

if __name__ =="__main__":
    print("正在下载文件。。。。。")
    url_path = "jsd"
    getText(url_path, url_path)

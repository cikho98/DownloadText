import requests


def go():
    for i in range(0,10000000):
        name="刘德华"
        name= name+str(i)
        url = f"http://176.114.16.176:8080/regUser?username={name}&password=&nickname=cikho&age=24"
        par ={
            "username": name,
            "password": 123456,
            "nickname": name,
            "age": 24
        }
        re = requests.get(url,data=par)
        print(re)

go()
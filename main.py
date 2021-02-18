
from multiprocessing import Process
import webview
import os
import time
def runManage():
    os.system('python manage.py runserver')
def runApp():

    webview.create_window('To Do','http://127.0.0.1:8000/')
    webview.start()


if __name__ == '__main__':

    p1 = Process(target=runManage)
    p2 = Process(target=runApp)

    p1.start()
    p2.start()
    time.sleep(500)
    p1.join()
    p2.join()

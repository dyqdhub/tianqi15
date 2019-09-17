import time
from multiprocessing import Process
from api import app
from getter import Getter
from tester import Tester
from db import RedisClient
from settings import *

## 调度器，调用各个模块多进程运行。

class Scheduler():
    def schedule_tester(self, cycle=TESTER_CYCLE):
        """
        定时测试代理
        while循环运行测试器模块，运行一次之后间隔一段时间，间隔时间参数为TESTER_CYCLE配置。
        """
        tester = Tester()
        while True:
            print('测试器开始运行')
            tester.run()
            time.sleep(cycle)

    def schedule_getter(self, cycle=GETTER_CYCLE):
        """
        定时获取代理
        while循环运行获取器模块，运行一次之后间隔一段时间，间隔时间参数为GETTER_CYCLE配置。
        """
        getter = Getter()
        while True:
            print('开始抓取代理')
            getter.run()
            time.sleep(cycle)

    def schedule_api(self):
        """
        开启API
        """
        app.run(API_HOST, API_PORT)

    def run(self):
        print('代理池开始运行')
        if GETTER_ENABLED:
            getter_process = Process(target=self.schedule_getter)
            getter_process.start()

        if TESTER_ENABLED:
            tester_process = Process(target=self.schedule_tester)
            tester_process.start()

        if API_ENABLED:
            api_process = Process(target=self.schedule_api)
            api_process.start()

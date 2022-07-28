from select import select
from time import sleep
import util.screen as screen
import util.util as util


# 捉鬼
#
# 分遍率使用配置1
# 仅保留一个窗口在桌面
# mumu界面分辩率 1720 x 968         脚本监测窗口对应大小为 1720 x 1057

class ZhuoGui():
    count = 1
    max = 8

    def __init__(self):
        # screen.set(1)
        # util.sleep(5)
        self.run()

    def run(self):
        if self.checkHasTask():
            util.sleep(200)
            self.loop()
            return
        print('当前无捉鬼任务，即将开始...')
        self.checkHasCancel()
        print('捉鬼：running....', self.count, '轮')
        self.start()

    def start(self):
        if util.stop : 
            print('按下空格键  任务结束')
            return 

        # 超出最多轮数停止
        if self.count > self.max:
            return

        # 世界地图
        if util.clickChangan() == False:
            return

        util.sleep(3)
        # npc map
        if util.clickEnd('img/common/screen1/map-changan-2.png') == False:
            return
        print('点击Npc地图')

        # 钟魁
        if util.clickEnd('img/common/screen1/npc-zhongkui.png', 8, 8, 8) == False:
            return

         # 捉鬼任务
        if util.clickEnd('img/task-zhuogui/task.png', 5, 5, 3) == False:
            return
         # 任务栏-捉鬼任务文本
        if util.doubleClickEnd('img/task-zhuogui/task-text.png') == False:
            return
        self.count = self.count + 1
        util.sleep(600)
        self.loop()

    def checkHasTask(self):
        return util.doubleClickEnd('img/task-zhuogui/task-text.png')
    def checkHasConfirm(self):
        return util.click('img/task-zhuogui/confirm.png')
    def checkHasCancel(self):
        return util.click('img/task-zhuogui/cancel.png')

    def loop(self):
        print('启动循环任务...')
        if self.checkHasCancel():
            util.sleep(4)
            self.start()
            return
        else:
            util.sleep(6)
            self.loop()

util.start_listen()
ZhuoGui()

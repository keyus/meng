from select import select
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
        screen.set(1)
        self.run()

    # 检测任务栏-是否已有捉鬼任务文本
    def checkHasTask(self):
        return util.doubleClickEnd('img/task-zhuogui/task-text.png')
    # 检测是否有-确认按钮

    def checkHasConfirm(self):
        return util.click('img/task-zhuogui/confirm.png')
    # 检测是否有-取消按钮

    def checkHasCancel(self):
        return util.click('img/task-zhuogui/cancel.png')

    def run(self):
        if self.checkHasTask():
            util.sleep(200)
            self.loop()
            return
        print('当前无捉鬼任务，即将开始...')
        self.checkHasCancel()
        self.start()

    def start(self):
        print('捉鬼：running....', self.count, '轮')

        # 超出最多轮数停止
        if self.count > self.max: 
            return 
        
        # 世界地图
        if util.clickMap() == False:
            return 

        # 长安城NPC地图
        res = util.clickEnd('img/common/screen1/map-changancheng-2.png')
        if res == False:
            return

        # 钟魁
        res = util.clickEnd('img/common/screen1/npc-zhongkui.png', 8, 8, 8)
        if res == False:
            return
         # 捉鬼任务
        res = util.clickEnd('img/task-zhuogui/task.png', 5, 5, 3)
        if res == False:
            return
         # 任务栏-捉鬼任务文本
        res = util.doubleClickEnd('img/task-zhuogui/task-text.png')
        if res == False:
            return

        self.count = self.count + 1
        util.sleep(600)
        self.loop()

    # 循环任务-检测取消按钮
    def loop(self):
        print('启动循环任务...')
        if self.checkHasCancel():
            util.sleep(4)
            # 点击取消  从头开始接取任务
            self.start()
            return
        else:
            util.sleep(6)
            self.loop()


ZhuoGui()

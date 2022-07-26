import util.screen as screen
import util.util as util
import time

# 运镖
# 分辩率使用配置5 
# 即在屏幕平铺5个游戏号窗口,支持同时压镖5个账号
class YunBiao():
    count = 0
    def __init__(self):
        self.run()
        # self.loop()

    def run(self):
        print('运镖：running....')
        
        if util.clickNpc('biao') == False:
            return 

        print('正在跑步向前，寻找郑镖头...预计16秒')
        time.sleep(16)
        print('16秒结束...')

        # 弹出任务
        if util.clickSelectAll():
            print('开始领取任务')

        time.sleep(8)
        # 确认压镖
        res = util.clickCenterAll('images/yb/confirm.png')
        if res == False:
            print('运镖已结束')
            return

        print('领取任务成功')

        time.sleep(20)
        self.count = self.count + res
        # 启动循环任务
        self.loop()

    # 循环任务
    def loop(self):

        if util.stop : 
            print('按下空格键  任务结束')
            return 


        if self.count >= 15 :
            print('运镖任务END')
            return 

        # 弹出任务 点击
        if util.clickSelectAll():
            print('运镖任务')
            time.sleep(2)
        
        box = util.clickCenterAll('images/yb/confirm.png')
        if box:
            self.count = self.count + box
            print('确认运镖')
            print('count', self.count)

        time.sleep(3)
        print('loop...')
        return self.loop()

util.start_listen()
YunBiao()
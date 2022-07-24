from itertools import count
import util.screen as screen
import util.util as util
import time

# 运镖
# 分辩率使用配置5 
# 即在屏幕平铺5个游戏号窗口,支持同时压镖5个账号
class YunBiao():
    count = 0
    def __init__(self):
        # screen.set(5)
        # time.sleep(3)
        self.run()

    def run(self):
        print('运镖：running....')
         # 世界地图
        if util.clickMapAll() == False:
            return 

         # 长安城NPC地图
        res = util.clickEndAll('img/common/screen5/map-changan-2.png')
        if res == False:
            return
        # NPC
        res = util.clickEndAll('img/common/screen5/npc-biao.png',10,3)
        if res == False:
            return
        
        print('正在跑步向前，寻找郑镖头...预计20秒')
        time.sleep(20)
        print('20秒结束...')

        # 弹出任务
        res = util.clickEndAll('img/task-yunbiao/task.png')
        if res == False:
            return
        print('开始领取任务')

        time.sleep(8)
        # 确认压镖
        res = util.clickEndAll('img/task-yunbiao/confirm.png')
        if res == False:
            print('运镖已结束')
            return

        print('领取任务成功')

        time.sleep(20)

        self.count = self.count + 5
        # 启动循环任务
        self.loop()

    # 循环任务
    def loop(self):

        print('loop 监听...')

        if self.count >= 15 :
            print('运镖任务END')
            return 

        # 弹出任务 点击
        if util.clickEndAll('img/task-yunbiao/task.png'):
            print('运镖任务')
            time.sleep(5)
            self.loop()
            return 
        
        res = util.clickEndAll('img/task-yunbiao/confirm.png',5,5,1,True)
        if res:
            self.count = self.count + res
            print('确认运镖')
            print('count', self.count)
            time.sleep(5)
            self.loop()
            return 

        self.loop()


YunBiao()
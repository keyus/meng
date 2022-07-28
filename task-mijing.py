from itertools import count
import util.screen as screen
import util.util as util
import time

# 秘境
# 分辩率使用配置5 
# 即在屏幕平铺5个游戏号窗口
class MiJing():
    count = 1
    leave = 0
    def __init__(self):
        screen.set(5)
        time.sleep(3)
        self.run()

    def run(self):
        print('秘境：running....')

        #到达东海湾
        if util.clickDonghaiAll() == False:
            return 

        # NPC 坐标点
        if util.clickEndAll('img/common/screen5/map-donghai-2.png') == False:
            return 

        # 云乐游 
        if util.clickEndAll('img/common/screen5/npc-yunleyou.png') == False:
            return

        print('正在跑步向前，寻找云乐游...预计6秒')
        time.sleep(6)
        print('6秒结束...')

        # # 弹出任务
        if util.clickEndAll('img/task-mijing/task.png') == False:
            return
        print('开始领取任务')

        time.sleep(3)
        # 点击第一关
        if util.clickAll('img/task-mijing/first.png',40,-30) == False:
            return

        time.sleep(3)

        # 进入第一关
        if util.clickEndAll('img/task-mijing/button.png',0,7) == False:
            return
        
        # 点击任务栏 第一关文字
        if util.clickAll('img/task-mijing/text.png',0,15) == False:
            return

        # 启动循环任务
        self.loop()

    # 循环任务
    def loop(self):
        print('listen...')

        if self.leave >= 5:
            print('秘境到达25关，已自动离开', self.leave)
            return 

        # 点击战斗
        if util.clickAll('img/task-mijing/task-zhandou.png',0, -8) :
            print('点击战斗')
            util.sleep(3)
            self.loop()
            return 

        if util.has('img/task-mijing/text-last.png'):
            util.click('img/task-mijing/text-last.png',100, 40)
            util.sleep(3)
            self.leave = self.leave + 1
            self.loop()
            return 

        util.sleep(5)
        self.loop()


MiJing()
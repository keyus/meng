import util.screen as screen
import util.util as util
import time


# 帮派任务
# 分辩率使用配置5 即在屏幕平铺5个游戏号窗口
# 每个账号需要点击使用一次宝图,不要点使用,等待脚本接管



class BangPai():
    count = 0
    faild = 0

    def __init__(self):
        # screen.set(5)
        # time.sleep(2)
        # self.run()
        self.loop()

    def run(self):
        print('帮派任务....')

        if util.clickCenterAll('img/common/screen5/huodong.png'):
            print('点击活动')
            util.sleep(2)

        if util.clickEndAll('img/task-bangpai/bangpai.png', 5, 0):
            print('参加帮派活动')
            util.sleep(4)

        if util.clickCenterAll('img/task-bangpai/take.png'):
            print('领取帮派任务')
            util.sleep(4)

    def loop(self):
        if util.stop : 
            print('按下空格键  任务结束')
            return 


        if util.clickEndAll('img/task-bangpai/task-button.png'):
            print('点击了,帮派任务按钮')

        if util.clickAll('img/task-bangpai/use.png', 10, 6):
            print('点击了,使用')

        # 购买任务组
        util.clickBuy()

        if util.clickAll('img/task-bangpai/select.png',30,45):
            print('点击了,请选择')
        

        if util.clickEndAll('img/task-bangpai/give.png'):
            print('点击了,上交')

        if util.clickEndAll('img/common/screen5/task.png', 0, -22):
            print('点击了,任务栏文字')


        print('loop + 1')
        self.loop()


util.start_listen()
BangPai()



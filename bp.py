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

        if util.clickCenterAll('images/common/huodong.png'):
            print('点击活动')
            util.sleep(2)

        if util.clickEndAll('images/bangpai/canjia.png'):
            print('参加帮派活动')
            util.sleep(4)

        # 请选择
        if util.clickSelect():
            return self.loop()

    def loop(self):
        if util.stop : 
            print('按下空格键  任务结束')
            return 

          # 请选择
        if util.clickSelect():
            return self.loop()

        # 购买任务组
        util.clickBuy()

        # 使用-上交
        util.clickUse()

        # 任务栏第一个任务
        util.clickTaskFirst()

        print('loop...')
        return self.loop()


util.start_listen()
BangPai()



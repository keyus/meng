import util.screen as screen
import util.util as util
import time


# 师门
# 分辩率使用配置5 即在屏幕平铺5个游戏号窗口,支持同时压镖5个账号

class ShiMen():
    closeCount= 0
    def __init__(self):
        # screen.set(5)
        # time.sleep(2)
        self.loop()

    def loop(self):
        print('师门：running....')

        if self.closeCount >= 5:
            print('师门任务结束')
            return 
        util.clickEndAll('img/task-shimen/task-button1.png')
        print('按钮-师门任务')

        util.clickAll('img/task-shimen/task-button2.png',10,6)
        print('按钮-使用')

        res = util.clickAll('img/task-shimen/task-button3.png',30,45)
        print('请选择')

        util.clickEndAll('img/task-shimen/task-button4.png')
        print('按钮-购买')

        util.clickEndAll('img/task-shimen/task-button5.png')
        print('按钮-上交')

        util.clickEndAll('img/task-shimen/task-button6.png')
        print('按钮-等等')

        util.clickEndAll('img/task-shimen/text-shimen.png')
        print('师门文字')

        close = util.clickAll('img/task-shimen/close.png')
        if close:
            self.closeCount = self.closeCount + close
            print('已完成个数', self.closeCount)
        self.loop()


ShiMen()

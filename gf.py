import util.screen as screen
import util.util as util
import time


# 工坊任务
# 分辩率使用配置1 
# 每个账号需要点击使用一次宝图,不要点使用,等待脚本接管
class GongFang():
    count = 0
    faild = 0

    def __init__(self):
        # screen.set(1)
        # time.sleep(2)
        # self.run()
        self.loop()


    def loop(self):
        if util.stop : 
            print('按下空格键  任务结束')
            return 

        if util.clickAnyway():
            return self.loop()

        if util.has('images/gf/gf-select.png'):
            util.click('images/gf/gf-select.png', 33,13)
            print('点击了工坊选择答案')
            return self.loop()


        # 请选择
        if util.clickSelectAll():
            return self.loop()

        # 使用-上交
        util.clickUse()

        # 购买任务组
        util.clickBuy()
        

        # 任务栏第二个任务
        util.clickTaskTwo()
      
        print('loop...')
        return self.loop()


util.start_listen()
GongFang()



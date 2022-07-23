import util.screen as screen
import util.util as util
import time


# 打图
# 分辩率使用配置5 即在屏幕平铺5个游戏号窗口,支持同时压镖5个账号
# 每个账号需要点击使用一次宝图,不要点使用,等待脚本接管

class Datu():
    count = 0
    faild = 0
    def __init__(self):
        screen.set(5)
        time.sleep(2)
        self.run()

    def run(self):
        print('打图：running....', self.count)

        if self.count > 100 : 
            print('打图END')
            return 

        if self.faild > 150 :
            print('打图时间结束,超出失败尝试次数')
            return 

        res = util.clickEndAll('img/task-tu/tu.png',10,8)
        # 记录未点击找到次数
        if res == False: 
            self.faild = self.faild + 1

        util.sleep(5)
        self.count = self.count + 1
        self.run()

Datu()
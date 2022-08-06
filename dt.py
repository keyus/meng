import util.util as util


# 打图
# 分辩率使用配置5 即在屏幕平铺5个游戏号窗口,支持同时压镖5个账号
# 每个账号需要点击使用一次宝图,不要点使用,等待脚本接管

class Datu():
    count = 0
    faild = 0
    def __init__(self):
        self.run()
        print('打图：running....', self.count)


    def run(self):
        if util.stop : 
            print('按下空格键  任务结束')
            return 

        if self.faild > 300 :
            print('打图时间结束,超出失败尝试次数')
            return 

        box = util.clickCenterAll('images/tu/use.png')
        if box : 
            self.count = self.count + box
            print('点击',self.count,'张图')
        else:
            self.faild = self.faild + 1

        util.sleep(3)
        self.count = self.count + 1
        return self.run()

util.start_listen()
Datu()
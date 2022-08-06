import util.util as util

# 秘境
# 分辩率使用配置5
# 即在屏幕平铺5个游戏号窗口


class MiJing():
    def __init__(self):
        self.run()

    def run(self):
        print('秘境：running....')

        # 启动循环任务
        self.loop()

    # 循环任务
    def loop(self):

        if util.stop:
            print('按下空格键  任务结束')
            return

        # 秘境任务
        if util.clickAll('images/mj/mj-map.png', 0, -30,1,0.8):
            print('点击了，任务')
            util.sleep(3)
            return self.loop()
            
          # 请选择
        if util.clickSelectAll():
            return self.loop()

        util.sleep(5)

        print('loop...')
        return self.loop()


util.start_listen()

MiJing()

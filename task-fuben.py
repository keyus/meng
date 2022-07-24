from select import select
import util.screen as screen
import util.util as util


# 副本

# 分遍率使用配置1
# 仅保留一个窗口在桌面
# mumu界面分辩率 1720 x 968         脚本监测窗口对应大小为 1720 x 1057

class Fuben():
    erchongyingFinish = False
    liulisuiFinish = False
    erchongyingIng = False
    liulisuiIng = False

    def __init__(self):
        # screen.set(1)
        self.run()

    def run(self):
        self.start()

    def start(self):
        print('副本：running....')

        # 世界地图
        if util.clickMap() == False:
            return 

        # 长安城NPC地图
        res = util.clickEnd('img/common/screen1/map-changancheng-2.png')
        if res == False:
            return

        # 百晓仙子
        res = util.clickEnd('img/common/screen1/npc-baixiao.png', 8, 8, 5)
        if res == False:
            return

         # 选择副本
        res = util.clickEnd('img/task-fb/select.png', 5, 5, 3)
        if res == False:
            return

        # 存在琉璃副本且未完成
        if util.has('img/task-fb/select-liulisui.png') and util.has('img/task-fb/finish-liulisui.png') == None:
            return self.selectLiulisui()

        # 存在二重影副本且未完成
        if util.has('img/task-fb/select-erchongyin.png') and util.has('img/task-fb/finish-erchongyin.png') == None:
            return self.selectErchongyin()

         # 存在绿烟副本且未完成
        if util.has('img/task-fb/select-lvyan.png') :
            return self.selectLvyan()

        print('今日50级普通副本已完成，没有可以领取的副本')

    # 选择琉璃碎
    def selectLiulisui (self):
        res = util.clickEnd('img/task-fb/select-liulisui.png', 5, 5, 4)
        if res == False:
            return
        self.liulisuiIng = True
        print('琉璃副本开始...')
        self.loop()
        return True

    # 选择二重影
    def selectErchongyin (self):
        res = util.clickEnd('img/task-fb/select-erchongyin.png', 5, 5, 4)
        if res == False:
            return
        self.erchongyingIng = True
        print('二重影副本开始...')
        self.loop()
        return True

     # 选择绿烟如梦
    def selectLvyan (self):
        res = util.clickEnd('img/task-fb/select-lvyan.png', 5, 5, 4)
        if res == False:
            return
        self.erchongyingIng = True
        print('绿烟如梦副本开始...')
        self.loop()
        return True


    # 循环任务
    # 1.检测跳过剧情
    def loop(self):
        if util.isZhandou():
            util.sleep(5)
            print('战斗中...')
            self.loop()
            return
        
        # 跳过剧情
        if util.click('img/task-fb/text-tiaoguojuqing.png', 5, 5, 4):
            print('跳过剧情...')
            self.loop()
            return

        # 任意地方继续
        if util.click('img/task-fb/text-jixu.png', 5, 5, 4):
            print('任意地方继续...')
            self.loop()
            return

        # 交互按钮
        if util.click('img/task-fb/button.png', 5, 5, 4):
            print('交互按钮...')
            self.loop()
            return

        # 已完成
        if util.click('img/task-fb/finish.png', 5, 5, 4):
            if self.liulisuiIng :
                print('琉璃副本已完成')
            if self.erchongyingIng :
                print('二重影副本已完成')
            self.liulisuiFinish = True

            self.run()
            return

        # 副本-绿烟
        if util.click('img/task-fb/text-lvyan.png', 5, 5, 4):
            print('点击 副本-绿烟如梦...')
            self.loop()
            return

        # 副本-普通
        if util.click('img/task-fb/text-putong.png', 5, 5, 4):
            print('点击 副本-普通...')
            self.loop()
            return

        util.sleep(8)
        self.loop()

Fuben()

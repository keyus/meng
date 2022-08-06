import util.util as util
import os

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
        self.run()

    def run(self):
        self.start()
        # self.loop()

    def start(self):
        print('副本：running....')

        if util.clickNpc('ben') == False:
            return
        util.sleep(3)
        if util.clickSelect() == False:
            return
        util.sleep(2)

        # 存在琉璃副本且未完成
        if util.has('images/fb/fb-lls.png') and util.has('images/fb/lls-success.png') == None:
            if util.clickEnd('images/fb/fb-lls.png',0,0):
                return self.loop()

        # 存在二重影副本且未完成
        if util.has('images/fb/fb-ecy.png') and util.has('images/fb/ecy-success.png') == None:
            if util.clickEnd('images/fb/fb-ecy.png',0,0):
                return self.loop()


        # 存在绿烟副本且未完成
        # if util.has('images/fb/fb-lls.png') :
        #     return self.selectLvyan()

        print('今日50级普通副本已完成，没有可以领取的副本')

        util.clickCenter('images/fb/close.png')
        util.sleep(2)
        
        #捉鬼
        os.system('python zg.py')


    # 循环任务
    def loop(self):
        print('loop...')
        if util.stop:
            print('按下空格键  任务结束')
            return

        if util.isFire():
            util.sleep(5)
            print('战斗中...')
            return self.loop()

        # 已完成
        if util.clickCenter('images/fb/finish-tag2.png',1,0.8):
            return self.run()


        # 跳过剧情
        if util.clickCenter('images/fb/jump.png', 1, 0.8):
            print('跳过剧情...')
            return self.loop()

        if util.clickAnyway():
            return self.loop()

        if util.clickSelect():
            return self.loop()

        # 副本
        if util.click('images/common/time.png',-100,20):
            print('点击 副本任务栏...')
            return self.loop()
        
        # 完成标志
        if util.clickCenter('images/fb/finish-tag1'):
            return self.loop()

        util.sleep(3)
        return self.loop()


util.start_listen()
Fuben()

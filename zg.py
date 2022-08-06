import util.util as util
import pyautogui as gui



# 捉鬼
#
# 分遍率使用配置1
# 仅保留一个窗口在桌面
# mumu界面分辩率 1720 x 968         脚本监测窗口对应大小为 1720 x 1057

class ZhuoGui():

    def __init__(self):
        self.run()

    def run(self):

        task = util.has('images/zg/zg.png',0.8)
        if task:
            gui.click(task.left, task.top)
            print('检测到已经有捉鬼任务...listen.')
            util.sleep(100)
            return self.loop()


        print('捉鬼任务，即将开始...')
        self.start()

    def start(self):

        # 世界地图
        if util.clickChangan() == False:
            return
        
        util.sleep(3)

         # 长安城NPC地图
        if util.click('images/common/pool.png',15,20) == False:
            return
        util.sleep(4)

        # npc map
        if util.clickCenter('images/zg/npc.png',1,0.8) == False:
            return
        print('点击钟馗')

        util.sleep(8)
        if util.clickSelect() == False:
            return 
        print('请选择...')

        util.sleep(2)
        self.loop()


    def loop(self):
        if util.stop : 
            print('按下空格键  任务结束')
            return 
        print('loop...')

        if util.isFire():
            print('战斗中...')
            util.sleep(8)
            return self.loop()
             

        go = util.has('images/zg/jixu.png',0.8)
        if go:
            gui.click(go.left + 35, go.top + 45)

        util.clickSelect()
        util.sleep(3)
        util.doubleClick('images/zg/zg.png',10,8,1,0.8)
        util.sleep(3)
        return self.loop()

util.start_listen()
ZhuoGui()

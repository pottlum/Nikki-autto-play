from airtest.core.api import *
import uiautomator2 as u2
import time
import datetime
import sys

auto_setup(__file__)

from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()

class NikkiAtuo():
    def __init__(self,device_id = "340755949200AUK"):
        self.device_id = device_id

    def connect_device(self):
        self.device = u2.connect(self.device_id)
    
    def start_game(self,app_name):
        self.device.app_start(app_name)
        notice = self.icon_check(Template(r"pic/notice.png", record_pos=(0.002, -0.419), resolution=(1080, 2400)))
        if notice :
            time.sleep(0.5)
            self.device.click(0.493, 0.748)
    
    def head_icon_check(self,icon_path = r"pic/nickname.png"):
        try:
            self.head_icon = wait(Template(icon_path, record_pos=(-0.419, -0.931), resolution=(1080, 2400)),timeout=10)
        except:
            self.head_icon = False
        return self.head_icon

    def back_to_homepage(self):
        head_icon = self.head_icon_check()
        if head_icon :
            return True
        else:
            sys.exit(0)
    
    def icon_check(self,icon_path):
        icon = exists(icon_path)
        if icon :
            return True
        else:
            return False

    def close_notice(self):
        head_icon = self.head_icon_check()
        if head_icon:
            #今日不在提示
            self.device.click(0.742,0.756)
            time.sleep(1)
            for i in range(1,20):
                self.device.click(0.54,0.81)
                time.sleep(0.5)
            time.sleep(1)
        else:
            print("没有找到头像")

    def paly_with_partner(self):
        # 开始旅程
        self.device.click(0.5,0.9)
        time.sleep(2)
        #结伴
        self.device.click(0.68,0.935)
        time.sleep(1)
        #时光钟表铺
        self.device.click(0.374, 0.34)
        time.sleep(1)
        #选择难度4
        self.device.click(0.828, 0.597)
        time.sleep(0.5)
        # 快速组队
        self.device.click(0.826, 0.836)
        time.sleep(5)
        #选择奖励

        #关闭奖励界面
        self.device.click(0.49, 0.849)
        time.sleep(1)
        # 返回
        self.device.press("back")
        time.sleep(0.5)
        # 不落的帷幕
        self.device.click(0.578, 0.455)
        time.sleep(0.5)
        today = datetime.datetime.now().weekday() + 1
        if today == 1 or today == 6:
            #音乐厅
            self.device.click(0.458, 0.207)
        elif today == 2 or today == 7:
            #星舞台
            self.device.click(0.462, 0.322)
        elif today == 3:
            self.device.click(0.506, 0.459)
        elif today == 4:
            self.device.click(0.488, 0.588)
        else:
            self.device.click(0.482, 0.717)
        time.sleep(1)
        #选择高难度
        self.device.click(0.62, 0.558)
        time.sleep(0.5)
        #选择第八幕
        self.device.click(0.838, 0.599)
        time.sleep(0.5)
        # 快速组队
        self.device.click(0.826, 0.836)
        time.sleep(5)
        #选择奖励

        #关闭奖励界面
        self.device.click(0.49, 0.849)
        time.sleep(1)
        self.device.press("back")
        time.sleep(0.5)
        self.device.press("back")
        time.sleep(0.5)
        # 印象航旅
        self.device.click(0.564, 0.601)
        time.sleep(0.5)
        # 高难度
        self.device.click(0.626, 0.561)
        time.sleep(0.5)
        # 虚渊 险
        self.device.click(0.828, 0.604)
        time.sleep(0.5)
        # 快速组队
        self.device.click(0.826, 0.836)
        time.sleep(5)
        #选择奖励

        # 关闭奖励界面
        self.device.click(0.49, 0.849)
        time.sleep(1)
        # 返回
        self.device.press("back")
        time.sleep(0.5)
        # 返回
        self.device.press("back")
        time.sleep(0.5)
        # 返回到主界面
        self.device.press("back")
        time.sleep(5)

    def friend(self):
        # 好友
        self.device.click(0.92, 0.169)
        time.sleep(10)
        #领取体力
        self.device.click(0.418, 0.939)
        # 一键领取
        self.device.click(0.5, 0.724)
        time.sleep(1)
        # 关闭领取界面
        self.device.click(0.28, 0.861)
        time.sleep(0.5)
        # 一键送心
        self.device.click(0.15, 0.944)
        time.sleep(1)
        #返回到主界面
        self.device.press("back")
        time.sleep(5)

    def union(self):
        # 联盟
        self.device.click(0.924, 0.415)
        time.sleep(4)
        # 机密任务
        self.device.click(0.54, 0.644)
        time.sleep(4)
        # 关闭奖励界面
        self.device.click(0.474, 0.934)
        time.sleep(0.5)
        # 前往当前目标
        self.device.click(0.382, 0.85)
        time.sleep(1)
        #执行五次
        self.device.click(0.382, 0.85)
        # 关闭奖励界面
        self.device.click(0.474, 0.934)
        time.sleep(0.5)
        #返回
        self.device.press("back")
        time.sleep(1)
        #联盟捐献
        self.device.click(0.82, 0.644)
        for i in range(1,6):
            #免费+金币
            self.device.click(0.222, 0.629)
            time.sleep(0.5)
            self.device.click(0.52, 0.9)
            time.sleep(0.5)
        time.sleep(1)
        # 联盟福利
        self.device.click(0.096, 0.846)
        time.sleep(1)
        # 一键领取
        self.device.click(0.51, 0.721)
        time.sleep(0.5)
        self.device.click(0.474, 0.934)
        time.sleep(0.5)
        self.device.click(0.474, 0.934)
        time.sleep(0.5)
        #返回到主界面
        self.device.press("back")
        time.sleep(5)
    
    def home(self):
        # 回家
        self.device.click(0.912, 0.838)
        time.sleep(8)
        # 收起日程表
        # self.device.click(0.498, 0.684)
        # time.sleep(0.5)
        # 日常采购
        self.device.click(0.888, 0.817)
        time.sleep(0.5)
        # 选择电影票
        self.device.click(0.208, 0.531)
        time.sleep(0.5)
        # 购买
        self.device.click(0.732, 0.728)
        time.sleep(0.5)
        # 关闭活力不足提示
        self.device.click(0.34, 0.553)
        time.sleep(0.5)
        # 购买
        self.device.click(0.732, 0.728)
        time.sleep(0.5)
        # 选择雨伞
        self.device.click(0.492, 0.649)
        time.sleep(0.5)
        # 购买
        self.device.click(0.732, 0.728)
        time.sleep(0.5)
        # 购买
        self.device.click(0.732, 0.728)
        time.sleep(0.5)
        # 选择调色板
        self.device.click(0.792, 0.529)
        # 购买
        self.device.click(0.732, 0.728)
        time.sleep(0.5)
        # 购买
        self.device.click(0.732, 0.728)
        time.sleep(0.5)
        # 零食
        self.device.click(0.596, 0.295)
        time.sleep(1)
        # 选择薯片
        self.device.click(0.216, 0.523)
        time.sleep(0.5)
        # 购买
        self.device.click(0.732, 0.728)
        time.sleep(0.5)
        # 购买
        self.device.click(0.732, 0.728)
        time.sleep(0.5)
        # 购买
        self.device.click(0.732, 0.728)
        time.sleep(0.5)
        # 关闭采购界面
        self.device.click(0.502, 0.821)
        time.sleep(1)
        # 返回到主界面
        self.device.click(0.046, 0.83)
        # self.device.press("back")
        time.sleep(6)

    def door_of_heart(self):
        # 心之门
        self.device.click(0.74, 0.918)
        time.sleep(4)
        # 切换到迷之海
        self.device.swipe_ext("right", 0.6)
        time.sleep(1)
        # 免费感应
        self.device.click(0.2, 0.863)
        time.sleep(6)
        for i in range(1,6):
            # 分享
            self.device.click(0.918, 0.927)
            time.sleep(1)
            # 微信
            self.device.click(0.068, 0.929)
            time.sleep(2)
            # 取消
            self.device.press("back")
            time.sleep(0.5)
            # 不保留
            self.device(resourceId="com.tencent.mm:id/gui").click()
            time.sleep(2)
            # 关闭奖励界面
            self.device.click(0.474, 0.794)
            time.sleep(0.5)
        # 关闭抽奖结果
        self.device.click(0.474, 0.794)
        time.sleep(0.5)
        # 幻之海
        self.device.swipe_ext("right", 0.6)
        time.sleep(1.5)
        self.device.swipe_ext("right", 0.6)
        time.sleep(1.5)
        # 判断时间是否免费
        if (time.time() - 1660487617) > 7 * 3600:
            # 幻之海感应一次
            self.device.click(0.274,0.866)
            time.sleep(4)
            self.device.click(0.474, 0.794)
            time.sleep(0.5)
        # 返回主界面
        self.device.press("back")
        time

    def pvp_game(self):
         # 开始旅程
        self.device.click(0.5,0.9)
        time.sleep(2)
        #独自
        self.device.click(0.335,0.926)
        time.sleep(1)
        #钻石竞技场
        self.device.click(0.65,0.53)
        time.sleep(1)
        # 循环5次
        for i in range(1,6):
            # 选择挑战者
            self.device.click(0.84,0.73)
            time.sleep(0.5)
            #关闭结算界面
            self.device.click(0.534,0.162)
            time.sleep(0.5)
            # 关闭奖励界面
            self.device.click(0.534,0.162)
            time.sleep(0.5)
        self.device.press("back")

    def time_to_cloister(self):
         # 开始旅程
        self.device.click(0.5,0.9)
        time.sleep(2)
        #独自
        self.device.click(0.335,0.926)
        time.sleep(1)
        # 时空回廊
        self.device.click(0.542,0.667)
        time.sleep(1)
        # 切换期数
    
    def manicure_work(self):
        # 设计中心
        # 美甲工作间
        # 我的店铺
        # 
        # 判断是否周一
        # 此刻投稿
        # 我的投稿
        # 





if __name__ == "__main__":
    autogame = NikkiAtuo("340755949200AUK")
    autogame.connect_device()
    # autogame.start_game("com.papegames.nn4.cn") 
    # time.sleep(20)
    # server = exists(Template(r"pic/serverlist.png", record_pos=(-0.015, 0.461), resolution=(1080, 2400)))
    # if server:
    #     autogame.device.click(0.496, 0.771)
    #     time.sleep(30)
    # else:
    #     wait(Template(r"pic/serverlist.png", record_pos=(-0.015, 0.461), resolution=(1080, 2400)),20)
    #     print("没有找到服务器列表")
    #     sys.exit(0)
    # autogame.close_notice()
    # autogame.friend()
    # autogame.back_to_homepage()
    # autogame.union()
    # autogame.back_to_homepage()
    # autogame.home()
    # autogame.back_to_homepage()
    # autogame.door_of_heart()
    # autogame.paly_with_partner()
    # autogame.back_to_homepage()
    autogame.pvp_game()
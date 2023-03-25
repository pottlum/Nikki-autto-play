# -*- encoding=utf8 -*-
__author__ = "pottlum"

from airtest.core.api import *
import uiautomator2 as u2
import time
import datetime

auto_setup(__file__)


from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()

#连接设备，启动游戏
dev = u2.connect("340755949200AUK")
# dev = u2.connect()
dev.app_start("com.papegames.nn4.cn")
# time.sleep(30)

server = exists(Template(r"pic/serverlist.png", record_pos=(-0.015, 0.461), resolution=(1080, 2400)))
notice = exists(Template(r"pic/notice.png", record_pos=(0.002, -0.419), resolution=(1080, 2400)))
if server:
    dev.click(0.496, 0.771)
    time.sleep(30)
else:
    # wait(Template(r"pic/serverlist.png", record_pos=(-0.015, 0.461), resolution=(1080, 2400)),20,intervalfunc=)
    print("没有找到服务器列表")
# #########################################################################
# head_icon = exists(Template(r"pic/headicon.png", record_pos=(-0.419, -0.931), resolution=(1080, 2400)))
# if head_icon:
#     #今日不在提示
#     dev.click(0.742,0.756)
#     time.sleep(1)
#     for i in range(1,15):
#         dev.click(0.54,0.81)
#         time.sleep(0.5)
# else:
#     print("没有找到头像")
############################################################################
# 开始旅程
# dev.click(0.5,0.9)
# time.sleep(2)
# #结伴
# dev.click(0.68,0.935)
# time.sleep(1)
# #时光钟表铺
# dev.click(0.374, 0.34)
# time.sleep(1)
# #选择难度4
# dev.click(0.828, 0.597)
# time.sleep(1)
# #组队登场
# dev.click(0.696, 0.819)
# time.sleep(1)
# #代理评选
# dev.click(0.486, 0.506)
# time.sleep(1)
# #登场准备
# dev.click(0.492, 0.445)
# #准备好了
# pass
# time.sleep(20)
# #关闭奖励界面
# dev.click(0.49, 0.849)
# time.sleep(1)
# #关闭结算界面
# dev.click(0.49, 0.849)
# time.sleep(2)
# dev.press("back")
# time.sleep(0.5)
# dev.press("back")
# time.sleep(0.5)
############################
# 不落的帷幕
# dev.click(0.578, 0.455)
# time.sleep(0.5)
# today = datetime.datetime.now().weekday() + 1
# if today == 1 or today == 6:
#     #音乐厅
#     dev.click(0.458, 0.207)
# elif today == 2 or today == 7:
#     #星舞台
#     dev.click(0.462, 0.322)
# elif today == 3:
#     dev.click(0.506, 0.459)
# elif today == 4:
#     dev.click(0.488, 0.588)
# else:
#     dev.click(0.482, 0.717)
# time.sleep(1)
# #选择高难度
# dev.click(0.62, 0.558)
# time.sleep(0.5)
# #选择第八幕
# dev.click(0.838, 0.599)
# time.sleep(0.5)
# #组队登场
# dev.click(0.706, 0.826)
# time.sleep(1)
# # 代理评选
# dev.click(0.486, 0.506)
# time.sleep(1)
# #登场准备
# dev.click(0.492, 0.445)
# time.sleep(20)
# #关闭奖励界面
# dev.click(0.49, 0.849)
# #关闭结算界面
# dev.click(0.49, 0.849)
# time.sleep(2)
# dev.press("back")
# time.sleep(0.5)
# dev.press("back")
# time.sleep(0.5)
# dev.press("back")
# time.sleep(0.5)
######################################################
# #印象航旅
# dev.click(0.564, 0.601)
# time.sleep(0.5)
# # 高难度
# dev.click(0.626, 0.561)
# time.sleep(0.5)
# # 虚渊 险
# dev.click(0.828, 0.604)
# time.sleep(0.5)
# # 组队登场
# dev.click(0.712, 0.823)
# time.sleep(1)
# # 代理评选
# dev.click(0.486, 0.506)
# time.sleep(1)
# # 登场准备
# dev.click(0.492, 0.445)
# time.sleep(15)
# #准备好了
# redy = exists(Template(r"pic/redy.png", record_pos=(-0.419, -0.931), resolution=(1080, 2400)))
# #游戏时间
# time.sleep(40)
# # 关闭奖励界面
# dev.click(0.49, 0.849)
# #关闭结算界面
# dev.click(0.49, 0.849)
# time.sleep(2)
# dev.press("back")
# time.sleep(0.5)
# dev.press("back")
# time.sleep(0.5)
# # 返回到主界面
# dev.press("back")
# time.sleep(3)
# head_icon = exists(Template(r"pic/headicon.png", record_pos=(-0.419, -0.931), resolution=(1080, 2400)))
#头像存在继续，不存在等待
#############################################################################################
# 好友
dev.click(0.92, 0.169)
time.sleep(7)
#领取体力
dev.click(0.418, 0.939)
# 一键领取
dev.click(0.5, 0.724)
time.sleep(1)
# 关闭领取界面
dev.click(0.28, 0.861)
time.sleep(0.5)
# 一键送心
dev.click(0.15, 0.944)
time.sleep(1)
#返回到主界面
dev.press("back")
time.sleep(5)
#头像判断
###############################################################################################
# 联盟
dev.click(0.924, 0.415)
time.sleep(3)
# 机密任务
dev.click(0.568, 0.512)
time.sleep(3)
# 关闭奖励界面
dev.click(0.474, 0.934)
time.sleep(0.5)
# 前往当前目标
dev.click(0.382, 0.85)
time.sleep(1)
#执行五次
dev.click(0.382, 0.85)
# 关闭奖励界面
dev.click(0.474, 0.934)
time.sleep(0.5)
#返回
dev.press("back")
time.sleep(1)
#联盟捐献
dev.click(0.826, 0.511)
for i in range(1,6):
    #免费+金币
    dev.click(0.222, 0.629)
    time.sleep(0.5)
    dev.click(0.474, 0.934)
    time.sleep(0.5)
time.sleep(1)
# 联盟福利
dev.click(0.096, 0.846)
time.sleep(1)
# 一键领取
dev.click(0.51, 0.721)
time.sleep(0.5)
dev.click(0.474, 0.934)
time.sleep(0.5)
dev.click(0.474, 0.934)
time.sleep(0.5)
#返回到主界面
dev.press("back")
time.sleep(3)
#头像检测
#########################################################################################################
# 回家
dev.click(0.912, 0.838)
time.sleep(7)
# 收起日程表
dev.click(0.498, 0.684)
time.sleep(0.5)
# 日常采购
dev.click(0.882, 0.917)
time.sleep(0.5)
# 选择电影票
dev.click(0.208, 0.531)
time.sleep(0.5)
# 购买
dev.click(0.732, 0.728)
time.sleep(0.5)
# 关闭活力不足提示
dev.click(0.34, 0.553)
time.sleep(0.5)
# 购买
dev.click(0.732, 0.728)
time.sleep(0.5)
# 选择雨伞
dev.click(0.492, 0.649)
time.sleep(0.5)
# 购买
dev.click(0.732, 0.728)
time.sleep(0.5)
# 购买
dev.click(0.732, 0.728)
time.sleep(0.5)
# 选择调色板
dev.click(0.792, 0.529)
# 购买
dev.click(0.732, 0.728)
time.sleep(0.5)
# 购买
dev.click(0.732, 0.728)
time.sleep(0.5)
# 零食
dev.click(0.596, 0.295)
time.sleep(1)
# 选择薯片
dev.click(0.216, 0.523)
time.sleep(0.5)
# 购买
dev.click(0.732, 0.728)
time.sleep(0.5)
# 购买
dev.click(0.732, 0.728)
time.sleep(0.5)
# 购买
dev.click(0.732, 0.728)
time.sleep(0.5)
# 关闭采购界面
dev.click(0.502, 0.821)
time.sleep(0.5)
# 返回到主界面
dev.press("back")
time.sleep(6)
# 头像检测
#########################################################################################################
# 心之门
dev.click(0.734, 0.918)
time.sleep(3)
# 切换到迷之海
dev.swipe_ext("left", 0.6)
time.sleep(1)
# 免费感应
dev.click(0.2, 0.863)
time.sleep(6)
for i in range(1,6):
    # 分享
    dev.click(0.918, 0.927)
    time.sleep(1)
    # 微信
    dev.click(0.068, 0.929)
    time.sleep(2)
    # 取消
    dev.press("back")
    time.sleep(0.5)
    # 不保留
    dev(resourceId="com.tencent.mm:id/gui").click()
    time.sleep(1)
    # 关闭奖励界面
    dev.click(0.474, 0.794)
    time.sleep(0.5)
# 关闭抽奖结果
dev.click(0.474, 0.794)
time.sleep(0.5)
# 幻之海
dev.swipe_ext("left", 0.6)
time.sleep(0.5)
# 判断时间是否免费
if (time.time() - 1660487617) > 7 * 3600:
    # 幻之海感应一次
    dev.click(0.274,0.866)
    time.sleep(4)
    dev.click(0.474, 0.794)
    time.sleep(0.5)
# 返回主界面
dev.press("back")
time.sleep(6)
# 头像检测
#########################################################################################################
#########################################################################################################
#########################################################################################################
#废弃
# # 组队登场
        # self.device.click(0.696, 0.819)
        # time.sleep(1)
        # #代理评选
        # self.device.click(0.486, 0.506)
        # time.sleep(1)
        #登场准备
        # self.device.click(0.492, 0.445)
        # time.sleep(2)
        # #准备好了
        # redy = self.iocn_check(Template(r"pic/redy.png", record_pos=(-0.419, -0.931), resolution=(1080, 2400)))
        # if redy:
        #    touch(Template(r"pic/redy.png", record_pos=(-0.419, -0.931), resolution=(1080, 2400)))
        # time.sleep(15)
        # #关闭奖励界面
        # self.device.click(0.49, 0.849)
        # time.sleep(1)
        # #关闭结算界面
        # self.device.click(0.49, 0.849)

        #   #组队登场
        # self.device.click(0.706, 0.826)
        # time.sleep(1)
        # # 代理评选
        # self.device.click(0.486, 0.506)
        # time.sleep(1)
        # #登场准备
        # self.device.click(0.492, 0.445)
        # redy = self.iocn_check(Template(r"pic/redy.png", record_pos=(-0.419, -0.931), resolution=(1080, 2400)))
        # if redy:
        #    touch(Template(r"pic/redy.png", record_pos=(-0.419, -0.931), resolution=(1080, 2400)))
        # time.sleep(15)
        # #关闭奖励界面
        # self.device.click(0.49, 0.849)
        # #关闭结算界面
         # 组队登场
        # self.device.click(0.712, 0.823)
        # time.sleep(1)
        # # 代理评选
        # self.device.click(0.486, 0.506)
        # time.sleep(1)
        # # 登场准备
        # self.device.click(0.492, 0.445)
        # time.sleep(1)
        # #准备好了
        # redy = self.iocn_check(Template(r"pic/redy.png", record_pos=(-0.419, -0.931), resolution=(1080, 2400)))
        # if redy:
        #    touch(Template(r"pic/redy.png", record_pos=(-0.419, -0.931), resolution=(1080, 2400)))
        # time.sleep(60)
        # # 关闭奖励界面
        # self.device.click(0.49, 0.849)
        # #关闭结算界面
        # self.device.click(0.49, 0.849)
        # time.sleep(2)
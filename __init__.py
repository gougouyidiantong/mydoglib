"""狗狗第三方库 mydoglib v1.20.3.55"""
__version__ = "1.20.3.55"
__author__ = "刘雨晨"
__all__ = ["狗狗类", "环境类", "道具类", "info"]


class 狗狗类:
    def __init__(self, name: str):
        self.name = name
        self.睡觉中 = False   # v1.20.3.46新增睡眠状态
        self.饱腹 = 50        # v1.20.3.46饱腹值0‑100
        self.开心度 = 50      # v1.20.3.46开心度0‑100

    # 叫声基础
    def ww(self, sound="汪汪汪"):
        if self.睡觉中:
            print(f"{self.name}正在呼呼大睡，叫不出来💤")
            return
        print(f"{self.name}：{sound}")

    def ku(self, cry_sound="呜呜呜"):
        if self.睡觉中:
            print(f"{self.name}睡得很沉，没有发出声音💤")
            return
        print(f"{self.name}委屈地哭了：{cry_sound}")

    # 情绪表情
    def xiao(self, msg="哈哈哈哈"):
        if self.睡觉中:
            print(f"{self.name}睡得安安稳稳💤")
            return
        print(f"{self.name}开心大笑：{msg} 😆")

    def shengqi(self, msg="气死我了"):
        if self.睡觉中:
            print(f"{self.name}睡得安安稳稳💤")
            return
        print(f"{self.name}气鼓鼓：{msg} 😠")

    def haixiu(self, msg="好害羞"):
        if self.睡觉中:
            print(f"{self.name}睡得安安稳稳💤")
            return
        print(f"{self.name}耳朵红了：{msg} 😳")

    def jingya(self, msg="吓一跳！"):
        if self.睡觉中:
            print(f"{self.name}睡得安安稳稳💤")
            return
        print(f"{self.name}瞪大双眼：{msg} 😲")

    def gaoxing(self, msg="太开心啦"):
        if self.睡觉中:
            print(f"{self.name}睡得安安稳稳💤")
            return
        print(f"{self.name}摇尾巴：{msg} 🥰")

    def shui(self, msg="呼呼呼"):
        """原有睡觉打印，不修改睡眠开关"""
        print(f"{self.name}趴着睡觉：{msg} 😴")

    # 身体动作
    def yao_weiba(self, msg="疯狂摇尾巴"):
        if self.睡觉中:
            print(f"{self.name}睡着了，尾巴一动不动💤")
            return
        print(f"{self.name} {msg} 🐕")
        self.开心度 += 8

    def xiu_qiwei(self, msg="低头嗅地面气味"):
        if self.睡觉中:
            print(f"{self.name}睡得很沉，鼻子不动💤")
            return
        print(f"{self.name} {msg} 👃")

    def tianmao(self, msg="低头舔自己的毛毛"):
        if self.睡觉中:
            print(f"{self.name}睡得很沉💤")
            return
        print(f"{self.name} {msg} 🧼")

    def batu(self, msg="爪子疯狂扒土挖洞"):
        if self.睡觉中:
            print(f"{self.name}睡得很沉💤")
            return
        print(f"{self.name} {msg} 🕳️")

    def tiaoyuan(self, msg="后腿发力奋力跳远"):
        if self.睡觉中:
            print(f"{self.name}睡得起不来💤")
            return
        print(f"{self.name} {msg} 🦘")

    def dapenti(self, sound="阿嚏！"):
        if self.睡觉中:
            print(f"{self.name}睡得很沉💤")
            return
        print(f"{self.name}猛地打喷嚏：{sound}")

    def dahaqian(self, msg="张大嘴巴打哈欠"):
        if self.睡觉中:
            print(f"{self.name}睡梦中迷迷糊糊打哈欠 🥱💤")
            return
        print(f"{self.name} {msg} 🥱")

    def cengceng(self, target="主人腿边"):
        if self.睡觉中:
            print(f"{self.name}睡得很沉💤")
            return
        print(f"{self.name}蹭了蹭{target} 🤍")

    def diaodongxi(self, thing="小球"):
        if self.睡觉中:
            print(f"{self.name}睡得很沉💤")
            return
        print(f"{self.name}叼起了{thing}跑远 🎾")

    def benpao(self, msg="撒开腿全力奔跑"):
        if self.睡觉中:
            print(f"{self.name}睡得起不来💤")
            return
        print(f"{self.name} {msg} 💨")
        self.开心度 += 12
        self.饱腹 -= 5

    def fadou(self, msg="害怕得浑身发抖"):
        if self.睡觉中:
            print(f"{self.name}睡得很沉💤")
            return
        print(f"{self.name} {msg} 🥶")

    def zuomeng(self, msg="正在做甜甜的美梦"):
        if not self.睡觉中:
            print(f"{self.name}清醒着，没有做梦")
            return
        print(f"{self.name}蜷缩在地，{msg} 💤")

    def yao_tou(self, msg="脑袋左右摇晃"):
        if self.睡觉中:
            print(f"{self.name}睡得很沉💤")
            return
        print(f"{self.name} {msg} 🤯")

    def paoxiaobu(self, msg="慢悠悠小跑散步"):
        if self.睡觉中:
            print(f"{self.name}睡得起不来💤")
            return
        print(f"{self.name} {msg} 🐾")

    def yao_guai(self, msg="调皮捣蛋，到处乱撞"):
        if self.睡觉中:
            print(f"{self.name}睡得很沉💤")
            return
        print(f"{self.name} {msg} 🤪")

    def wan(self, partner="小伙伴"):
        if self.睡觉中:
            print(f"{self.name}正在睡觉，不想玩耍💤")
            return
        print(f"{self.name} 和{partner}追逐打闹玩耍 🎉")

    # v1.20.3.46
    def sleep(self):
        if self.睡觉中:
            self.睡觉中 = False
            print(f"{self.name}睡醒了，打了个哈欠！")
        else:
            self.睡觉中 = True
            print(f"{self.name}趴下，呼呼睡着了💤")

    def 摇尾巴(self):
        if self.睡觉中:
            print(f"{self.name}睡得安安稳稳，尾巴一动不动💤")
            return
        print(f"{self.name}开心地使劲摇晃尾巴！摇来摇去～")

    def 抬脚(self):
        if self.睡觉中:
            print(f"{self.name}睡得很沉，不肯抬起爪子💤")
            return
        print(f"{self.name}抬起一只小爪子，举到半空中🖐")

    def 趴下(self):
        if self.睡觉中:
            print(f"{self.name}已经趴在地上睡觉啦💤")
            return
        print(f"{self.name}前爪往前伸，整个身子趴到地板上。")

    def 坐下(self):
        if self.睡觉中:
            print(f"{self.name}正在睡觉，不想坐💤")
            return
        print(f"{self.name}后腿弯曲，屁股重重坐到地上。")

    def 打滚(self):
        if self.睡觉中:
            print(f"{self.name}睡得一动不动💤")
            return
        print(f"{self.name}四脚朝天，躺在地上打滚，露出软软肚皮！")
        self.开心度 += 10

    def 舔手(self):
        if self.睡觉中:
            print(f"{self.name}闭着眼睡觉💤")
            return
        print(f"{self.name}伸出小舌头，轻轻舔来舔去👅")

    def 啃骨头(self):
        if self.睡觉中:
            print(f"{self.name}睡着了，不啃骨头💤")
            return
        print(f"{self.name}叼起骨头，咯吱咯吱使劲啃🦴")
        self.饱腹 += 15

    def 喝水(self):
        if self.睡觉中:
            print(f"{self.name}睡着，不喝水💤")
            return
        print(f"{self.name}吧嗒吧嗒低头舔水喝。")

    def 甩身子(self):
        if self.睡觉中:
            print(f"{self.name}睡得安安稳稳💤")
            return
        print(f"{self.name}浑身用力左右甩动，水珠四处飞溅！")

    def 扒腿(self):
        if self.睡觉中:
            print(f"{self.name}正在睡觉💤")
            return
        print(f"{self.name}站起来，两只前爪扒住你的腿。")

    def 叫名字(self):
        if self.睡觉中:
            print(f"{self.name}睡得香香的，听见呼唤动了动耳朵💤")
            return
        print(f"{self.name}耳朵唰地竖起来：汪汪！我在这里🐶")

    def 摇耳朵(self):
        if self.睡觉中:
            print(f"{self.name}睡得香香的，耳朵微微动了一下，没有醒过来")
            return
        print(f"{self.name}耳朵哗啦哗啦来回摇动✨")
        self.开心度 += 1

    def 吃狗粮(self):
        if self.睡觉中:
            print(f"{self.name}正在睡觉，不想吃东西😴")
            return
        if self.饱腹 >= 100:
            print(f"{self.name}肚子饱饱的，不想再吃狗粮了")
            return
        print(f"{self.name}咔哧咔哧大口吃狗粮🍚")
        self.饱腹 += 25
        self.开心度 += 2
        if self.饱腹 > 100:
            self.饱腹 = 100

    # v1.20.3.54 游戏功能，自动区分现实/梦境，使用 self.睡觉中
    def da_youxi(self):
        if self.睡觉中:
            print(f"【{self.name}】熟睡中✨梦里爪子胡乱挥舞，正在梦境世界打游戏🎮💤")
        else:
            print(f"【{self.name}】现实里扒住游戏机，噼里啪啦按按键🎮")

    def sheng_li(self):
        if self.睡觉中:
            print(f"【{self.name}】梦里游戏胜利！四条腿开心乱蹬，睡梦中偷偷摇尾巴🎉💤")
        else:
            print(f"【{self.name}】现实游戏赢啦！蹦蹦跳跳疯狂摇尾巴🎉")

    def shu_le(self):
        if self.睡觉中:
            print(f"【{self.name}】梦里游戏输了，睡觉小声呜呜哼唧，耳朵耷拉😔💤")
        else:
            print(f"【{self.name}】现实游戏输了，垂头丧气趴在地上😔")

    def wan_youxi_zhua_qiu(self):
        if self.睡觉中:
            print(f"【{self.name}】梦里奔跑追逐小球，四肢来回蹬动⚽💤")
        else:
            print(f"【{self.name}】现实跑来跑去追逐玩具小球⚽")


# 环境场景类
class 环境类:
    @staticmethod
    def taiyang():
        print("【场景】阳光明媚，满地金光 ☀️")

    @staticmethod
    def feng(word="微风轻轻吹过草地"):
        print(f"【场景】{word} 🌬️")

    @staticmethod
    def xiaoyu():
        print("【场景】下起绵绵小雨，地面湿润 💧")

    @staticmethod
    def wanxia():
        print("【场景】天边铺满橘红色晚霞 🌇")

    @staticmethod
    def caodi():
        print("【场景】大片软软的青草地 🌱")

    @staticmethod
    def xiaoxi():
        print("【场景】清澈小溪缓缓流淌 🌊")

    @staticmethod
    def yewan():
        print("【场景】夜晚满天星星，十分安静 🌌")

    @staticmethod
    def daxue():
        print("【场景】漫天飘起鹅毛大雪，大地白茫茫 ❄️")


# 游戏道具类
class 道具类:
    def __init__(self, item_name: str):
        self.name = item_name

    def chuxian(self):
        print(f"【道具】{self.name}掉落在草地上")

    def beidiaozou(self, dog_name):
        print(f"【道具】{dog_name}一口叼走了{self.name}")

    def gun_yi_xia(self):
        print(f"【道具】{self.name}在地上滚了一圈")


def info():
        print("===== mydoglib 狗狗第三方库 v1.20.3.54 =====")
        print(f"版本：{__version__}")
        print(f"作者：{__author__}")
        print("内置类：")
        print("  1. 狗狗类 —— 控制小狗所有动作、情绪")
        print("  2. 环境类 —— 生成户外场景天气")
        print("  3. 道具类 —— 皮球、骨头、飞盘等玩具")
        print("\n【狗狗类基础叫声方法】")
        print("  .ww()     汪汪叫")
        print("  .ku()     委屈哭泣")
        print("\n【狗狗情绪表情方法】")
        print("  .xiao()   大笑")
        print("  .shengqi()生气")
        print("  .haixiu() 害羞")
        print("  .jingya() 惊讶")
        print("  .gaoxing()高兴")
        print("  .shui()   睡觉文字输出")
        print("\n【v1.2.0新增动作】")
        print("  .zuomeng() 做梦")
        print("  .yao_tou() 摇头")
        print("  .paoxiaobu()小跑")
        print("  .yao_guai()调皮捣蛋")
        print("\n【v1.3.0新增动作】")
        print("  .wan() 互相追逐打闹玩耍")
        print("\n【v1.20.3.49新增动作】")
        print("  .sleep()   切换睡觉/唤醒状态")
        print("  .摇尾巴()   开心摇晃尾巴")
        print("  .抬脚()    抬起爪子握手")
        print("  .坐下()    原地坐下")
        print("  .趴下()    趴在地上")
        print("  .打滚()    四脚朝天打滚")
        print("  .舔手()    舔爪子舔手")
        print("  .啃骨头()  啃骨头磨牙")
        print("  .喝水()    低头喝水")
        print("  .甩身子()  抖动身上毛发")
        print("  .扒腿()    爪子扒住人的腿")
        print("  .叫名字()  呼唤小狗，小狗回应")
        print("  .摇耳朵()  摇动耳朵")
        print("  .吃狗粮()  吃狗粮，提升饱腹、开心度")
        print("\n【v1.20.3.54新增 · 游戏（现实/梦境自动切换）】")
        print("  .da_youxi()      打游戏")
        print("  .sheng_li()     游戏胜利")
        print("  .shu_le()       游戏输掉")
        print("  .wan_youxi_zhua_qiu() 抓球小游戏")

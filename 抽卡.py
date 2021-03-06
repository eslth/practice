import random
import copy
#warning
# 下方出现大量拼音和小学英语

class kachi:  #这些是池子间共享资源
    six = ["棘刺", "铃兰", "早露", "温蒂", "傀影", "风笛",
           "刻俄柏", "阿", "煌", "莫斯提马", "麦哲伦", "赫拉格",
           "黑", "陈", "斯卡蒂", "银灰", "塞雷娅", "星熊", "夜莺",
           "闪灵", "安洁莉娜", "艾雅法拉","伊芙利特", "推进之王",
            "能天使", "森蚺", "史尔特尔", "瑕光","泥岩","山","空弦"]
    five = ["安哲拉", "贾维", "蜜蜡", "断崖", "莱恩哈特","月禾", "石棉", "极境", "巫恋", "慑砂","惊蛰", "吽", "灰喉", "布洛卡", "苇草", "槐琥","送葬人", "星极",
            "格劳克斯", "诗怀雅","夜魔", "食铁兽", "狮蝎", "空", "真理", "初雪","崖心", "守林人", "普罗旺斯", "可颂", "雷蛇", "红","临光", "华法琳", "赫默",
            "梅尔", "天火", "陨星", "白金","蓝毒", "幽灵鲨", "拉普兰德", "芙兰卡", "德克萨斯","凛冬", "白面鸮","燧石", "四月", "奥斯塔","絮雨","卡夫卡","爱丽丝"]
    four = ["孑", "卡达", "波登可", "刻刀", "宴", "安比尔","梅", "红云", "桃金娘", "苏苏洛", "格雷伊", "猎蜂","阿消", "地灵", "深海色", "古米", "蛇屠箱",
            "角峰", "调香师", "嘉维尔","末药", "暗索", "砾", "慕斯", "霜叶", "缠丸", "杜宾", "红豆","清道夫", "讯使", "白雪", "流星", "杰西卡", "远山",
            "夜烟", "酸糖", "芳汀","泡泡","杰克","松果","豆苗" ]
    three = ["斑点", "泡普卡", "月见夜", "空爆", "梓兰", "史都华德","安塞尔", "芙蓉", "炎熔", "安德切尔","克洛斯", "米格鲁", "卡缇", "梅兰莎", "翎羽", "香草", "芬"]
    yiyongyou = {}
    _baodi = 0
    _yu = 0

    def __init__(self, theupsix=None, theupfive=None, theupfour=None):  #这是每个池子的资源
        if theupfour is None:
            theupfour = []
        if theupfive is None:
            theupfive = []
        if theupsix is None:
            theupsix = []
        self.liuxingshu=0
        self.wuxingshu=0
        self.lianxusanxing=0
        self.yichoushu=0
        self.upsix =[]
        self.upfive=[]
        self.upfour=[]
        self.upsix=self.upchuli(theupsix,self.six,self.upsix)
        self.upfive=self.upchuli(theupfive, self.five, self.upfive)
        self.upfour=self.upchuli(theupfour, self.four, self.upfour)

    def upchuli(self,thelist,mainlist,uplist): #处理up的列表
        if len(thelist):
            for i in thelist:
                if i in mainlist:
                    mainlist.remove(i)
                uplist.append(i)
        else:
            uplist=copy.copy(mainlist)
        return uplist

    @property
    def yu(self):
        return self._yu

    @property
    def baodi(self):
        return self._baodi

    @property
    def yichoudaodeka(self):
        return self.yiyongyou

    def chulvtongji(self):
        print('五星出了%d' % (self.wuxingshu ))
        print('六星出了%d' % (self.liuxingshu ))
        print('五星出率为%f' % (self.wuxingshu /self.yichoushu))
        print('六星出率为%f' % (self.liuxingshu /self.yichoushu))

    def cunhuo(self,shitou,hechengyu):
        print("请依次输入您目前拥有的石头和合成玉")
        self._yu+=(hechengyu+shitou*180)
        print('合计为%d玉'%(self._yu))

    def zhubei(self,choushu):
        a=self._yu//600
        if choushu <0:
            a = a
        elif a>= choushu:
            a = choushu
        else:
            a=a
            print('请充钱')
        self._yu -= a * 600
        print('正在进行%d次抽卡，还有%d玉' % (a, self._yu))
        return a

    def gailv(self,a):
        star=0
        while a > 0:
            self._baodi += 1
            self.yichoushu+=1
            if self._baodi > 50:
                i = (self._baodi - 50) / 50
            else:
                i = 0
            thestar = random.random()
            if thestar>=0 and thestar<=0.02+i:
                star =6
            elif thestar>0.02+i and thestar<=0.1+i*(4/49):
                star =5
            elif thestar>0.1+i*(4/49) and thestar<=0.6+i*(29/49):
                star =4
            elif thestar>0.6+i*(29/49) and thestar<=1:
                star =3
            self.chouka(star)
            a -= 1

    def choukafuzhu(self,form):
        str=random.choice(form)
        if str in self.yiyongyou.keys():
            self.yiyongyou[str]+=1
        else:
            self.yiyongyou[str]=1

    def chuleliuxing(self):
        self.lianxusanxing = 0
        p=random.random() #概率p控制up出率
        if p<=0.5:
            self.choukafuzhu(self.six)
        else:
            self.choukafuzhu(self.upsix)
        # print('恭喜寻访到六星干员！')
        self.liuxingshu += 1
        self._baodi = 0

    def chulewuxing(self):
        self.lianxusanxing = 0
        p = random.random()  # 概率p控制up出率
        if p <= 0.5:
            self.choukafuzhu(self.five)
        else:
            self.choukafuzhu(self.upfive)
        self.wuxingshu += 1

    def chulesixing(self):
        self.lianxusanxing = 0
        p = random.random()  # 概率p控制up出率
        if p >= 0.2:
            self.choukafuzhu(self.four)
        else:
            self.choukafuzhu(self.upfour)

    def chulesanxing(self):
        self.choukafuzhu(self.three)

    def chouka(self,star):
        if star == 3:
            self.lianxusanxing += 1
            if self.wuxingshu + self.liuxingshu == 0 and self._baodi == 10:
                print("首次十连保底了")
                self.chulewuxing()
            elif self.lianxusanxing==10:
                self.chulesixing()
            else:
                self.chulesanxing()


        elif star == 4:
            if self.wuxingshu + self.liuxingshu != 0 or self._baodi != 10:
               self.chulesixing()
            else:
                print("首次十连保底了")
                self.chulewuxing()

        elif star == 5:
            self.chulewuxing()

        elif star == 6:
           self.chuleliuxing()
        else:
            print("出错了")

    def zhuchengxu(self,choushu=-1):
        self.gailv(self.zhubei(choushu))

if __name__=='__main__':
    a=kachi(theupsix=[],theupfive=[],theupfour=[])
    a.cunhuo(100000000,0)
    #b=int(input("您想抽多少抽"))
    a.zhuchengxu(30)
    a.chulvtongji()
    print(sorted(a.yiyongyou.items(), key = lambda kv:(kv[1], kv[0])))


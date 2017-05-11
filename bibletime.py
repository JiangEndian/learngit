#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import tkinter as tk
from tkinter import *

#canvas的长和宽设定
global cx
cx = 7000
global cy
cy = 700

#Y轴的步子
global sy
sy = 30

#开始位置及时间AA,BC的设定
global bx
bx = 0
global by
by = sy
global bAA
bAA = 1
global bBC
bBC = 3969

#画面X轴和Y轴的缩放系数
global kx
kx = 1
global ky
ky = 1

#canvase开始画画,没有明确纪年的，推算的时间的。如族长时代们～
def cr(cvst, who, whenson, age, color, other='空白'):
    global cy
    global bx
    global by
    global bAA
    global bBC
    global kx
    global ky
    def bAD(after=0):#通过BC计算AD
        global bBC
        return 1-(bBC-after)
    if bAA == 1:#刚开始时画标尺
        cvst.create_line(1,(sy/2)*ky,cx*kx,(sy/2)*ky,fill='black')#上线
        cvst.create_line(1,(cy-sy/2)*ky,cx*kx,(cy-sy/2)*ky,fill='black')#下线
        for ix in [i*100 for i in range(int(cx/100))]:
            cvst.create_line(ix*kx,(sy/2)*ky,ix*kx,sy*ky,fill='black')#上线标尺
            cvst.create_text(ix*kx,sy*ky,text='AA' + str(ix),fill='black')
            if ix<3970:
                cvst.create_text(ix*kx,sy*ky+sy/4,text='BC'+str(3970-ix),fill='black')
            elif ix>3970:
                cvst.create_text(ix*kx,sy*ky+sy/4,text='AD'+str(ix-3969),fill='black')
            cvst.create_line(ix*kx,(cy-sy/2)*ky,ix*kx,(cy-sy)*ky,fill='black')#下线标尺
            cvst.create_text(ix*kx,(cy-sy)*ky,text='AA' + str(ix),fill='black')
            if ix<3970:
                cvst.create_text(ix*kx,(cy-sy)*ky+sy/4,text='BC'+str(3970-ix),fill='black')
            elif ix>3970:
                cvst.create_text(ix*kx,(cy-sy)*ky+sy/4,text='AD'+str(ix-3969),fill='black')
        by = by/2 + by#画完标尺，下移图画
    if by > 600:#如果y轴画过600了，重新回到sy*1.5开始画
        by = sy * 1.5

    #AD1年为AA3970年，那么，BC1年，为AA3969年（AA:AfterAdam)
    if whenson == 0:
        msgt1 = 'AA%d-AA%d年  事件:%s  持续:%d年' % (bAA,bAA+age, who, age)
    else:
        msgt1 = 'AA%d-AA%d年  事件:%s  交任:%d年  持续:%d年' % (bAA,bAA+age, who, whenson, age)
    if bBC > bAD() and (bBC-age) > bAD(age):#生死都在公元前
        if len(other) < 6:
            msgt2 = 'BC%d-BC%d年  大事记:%s' % (bBC,bBC-age, other)
        else:
            msgt2 = 'BC%d-BC%d年  大事记:\n%s' % (bBC,bBC-age, other)
    elif bBC < bAD():#生于公元后
        if len(other) < 6:
            msgt2 = 'AD%d-AD%d年  大事记:%s' % (bAD(),bAD(age), other)
        else:
            msgt2 = 'AD%d-AD%d年  大事记:\n%s' % (bAD(),bAD(age), other)
    else:#生于公元前，但死于公元后
        if len(other) < 6:
            msgt2 = 'BC%d-AD%d年  大事记:%s' % (bBC,bAD(age), other)
        else:
            msgt2 = 'BC%d-AD%d年  大事记:\n%s' % (bBC,bAD(age), other)
    msgt = msgt1 + '  ' + msgt2
    #计算新的高度nsy
    #if msgt.count('\n') == 1:
     #   msgt = msgt.strip()
    nsy = (msgt.count('\n')+1) * sy / 2 
    #画矩形，开始位置，长宽，填充,然后在末处画一条纵线
    cvst.create_rectangle(bx*kx, by*ky, (bx+age)*kx, (by+nsy)*ky, fill=color)
    cvst.pack()
    cvst.create_line((bx+age)*kx, 0, (bx+age)*kx, cy, fill=color)
    #显示这些信息
    cvst.create_text((bx+age/2)*kx, (by+nsy/2)*ky, text=msgt, fill='black')

    #开始位置和时间前进喽
    bx += whenson
    by += nsy
    bAA += whenson
    bBC -= whenson

bibletime = tk.Tk()
bibletime.title('BibleTime...')
#一个Y轴滚动条
scrollbary = Scrollbar(bibletime)
scrollbary.set(0.5,1)
scrollbary.pack(side=RIGHT)
#一个X轴滚动条
scrollbarx = Scrollbar(bibletime, orient=HORIZONTAL)
scrollbarx.set(0.5,1)
scrollbarx.pack()
#把这个东西设置好同时绑定到滚动条上
#cvs = tk.Canvas(bibletime, width=cx, height=cy, bg='white', xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)#加上set后，win不好使
cvs = tk.Canvas(bibletime, width=cx, height=cy, bg='white', xscrollcommand=scrollbarx, yscrollcommand=scrollbary)#不加set,mint好使...
cvs.pack()
#对滚动条进行配置，滚动时触发什么
scrollbarx.config(command=cvs.xview)
scrollbary.config(command=cvs.yview)

color1 = 'pink'
color2 = 'yellow'
color3 = '#00FF00'#闪绿色
color4 = '#00FFFF'#青色

#cr(cvs, '事件', 交任, 持续, 'color', '大事记')

cr(cvs, '''亚当入世''' ,  130, 930,  color1, '''创造，光/空气/植物/光体/飞鸟和鱼/陆地生物和人/安息，亚当，伊甸，起名，夏娃
蛇诱，堕落，星爆，惩罚，救恩，救恩，被逐，人类史开始，该隐和亚伯，生塞特，相似''')
cr(cvs, '''塞特''' ,  105,  912,  color2, '''生以挪士''')
cr(cvs, '''以挪士''' ,  90,  905,  color1, '''生该南''')
cr(cvs, '''该南''' ,  70,  910,  color2, '''生玛勒列''')
cr(cvs, '''玛勒列''' ,  65, 895,   color1, '''生雅列''')
cr(cvs, '''雅列''' ,  162, 962,   color2, '''生以诺''')
cr(cvs, '''以诺''' ,  65, 365,   color1, '''与神同行300年，神将他取走，生玛土撒拉''')
cr(cvs, '''玛土撒拉''' ,  187, 969,   color2, '''人类史最长寿的男人，生拉麦''')
cr(cvs, '''拉麦''' ,  182, 777,   color1, '''给儿子起名挪亚时很感慨''')
cr(cvs, '''挪亚''' ,  480, 950,   color2, '''500岁生闪，含，雅弗，世界败坏，挪亚蒙恩，指示方舟''')
cr(cvs, '''方舟''', 119, 119, color1, '''300×50×30（肘^3），三层，同时传道''')
cr(cvs, '''洪水''', 2, 1, color2, '''挪亚600.2.17开始,洪水审判，601.2.27地干.新规，彩虹之约\n农夫挪亚，闪、雅弗、含、迦南，宁录，巴别之变''')
cr(cvs, '''百岁闪''' , 0, 500,   color1, '''创11：10,洪水后两年闪100,此时挪亚602\n即挪亚502岁生了闪，不明所以。。。生亚法撒''')
cr(cvs, '''亚法撒''' ,  35,  438,  color2, '''生沙拉''')
cr(cvs, '''沙拉''' ,  30,  433,  color1, '''生希伯''')
cr(cvs, '''希伯''' ,  34,  464,  color2, '''生法勒''')
cr(cvs, '''法勒''' ,  30,  239,  color1, '''生拉吴''')
cr(cvs, '''拉吴''' ,  32,  239,  color2, '''生西鹿''')
cr(cvs, '''西鹿''' ,  30,  230,  color1, '''生拿鹤''')
cr(cvs, '''拿鹤''' , 29,  148,   color2, '''生他拉''')
cr(cvs, '''他拉''' ,  130, 205,   color1, '''创11：26节，和挪亚500岁生3个儿子一样的描述，不明所以。。。生亚伯兰\n亚伯兰娶妹子撒莱，拿鹤娶侄女密迦，三拉一得出吾珥至哈兰，他拉死''')
cr(cvs, '''亚伯兰''' ,  85, 175,  color2, '''75岁，蒙召，到迦南，饥荒,下埃及，法老，怒送，南地，罗得分，四王KO五王，救罗得\n麦基洗德，所多玛王，立约，夏甲插曲，85岁，86岁得以实玛利，100岁得以撒''')
cr(cvs, '''立约到立法''', 14, 430, color1, '''加3：17,立约与立法的时间距为430年''')
cr(cvs, '''亚伯兰99''', 1, 1, color2, '''撒拉90，亚伯拉罕，割礼，应许以撒，灭所多玛，罗得家，摩押，押扪
基拉耳王亚比米勒，百岁生以撒''')
cr(cvs, '''以撒''', 60, 180, color1, '''以撒生，摆筵席，逐夏甲与巴兰旷野，亚亚约，甘心被献，拿鹤消息，撒拉127去世，买坟地，4年
以撒40，利百加，60双子（父娶基土拉，分财散子，175死）雅各以扫红豆汤，基拉耳，非利士王亚比米勒，昌盛，挖井，以亚约''')#127-91=36,36-》40，4年，迎来利百加
cr(cvs, '''雅各''', 91, 147, color2, '''40以扫娶妻，利百加之计，77至拉班，以扫再娶，伯特利异梦，饮羊，20年打工娶妻生娃生约瑟挣家业
被召回，偷走*，追搜怒斥，雅拉约，见以扫，瘸腿以色列，迎以扫，示剑*，底拿，西利屠城，伯特利
以法他（伯利恒），便雅悯，以得台，流便，至以撒，以扫分''')#过14年，91岁生约瑟，至拉班时，91-14=77，84娶妻。。。
cr(cvs, '''约瑟''', 39, 110, color1, '''被偏爱，打报告，彩衣，17做梦，看望，被卖，波提乏（犹大，书亚，他玛，法勒斯）蒙恩
诱惑与不从，被冤下监，蒙恩，28解梦，信好，好坏，被忘，双七梦，30见法老，解梦出策，治理埃及，31丰年，得妻生子，38饥荒
38见哥哥们，要见便雅悯，通事传话，哭，银包，父亲之痛，犹大担保，见便雅闵，哭，银杯，犹大护弟，哭，相认
原谅，哭，约瑟之意法老之令，39见雅各，130雅各全家70人在埃及歌珊，奉养，五一分，玛以以玛，领受双分，祝福''')
cr(cvs, '''以色列在埃及''', 145, 225, color2, '''雅各死，葬于那坟地，哥哥们求饶恕，哭，我岂能代替神呢。神的意思是好的。亲爱话安慰
让以色列人起誓，约瑟死，BC1560，含逐闪，18代新王兴，摩西''')
cr(cvs, '''摩西''', 80, 120, color1, '''雅各繁盛，新王苦待，收生婆，雅各强盛，丢男孩，摩西生，三月弃，被收养，40岁摩西发热心
至米甸，娶妻生子，雅各哀声，40年放羊，何烈山异象，神之名Yahweh，被迫领导''')
cr(cvs, '''立法到建殿''', 0, 480, color2, '''王上6：1,出埃及后480年，所罗门王4年2月，建殿''')
cr(cvs, '''出埃及与旷野''', 40, 40, color1, '''十灾，逾越节，红海，西奈山，律法，会幕，利未人和祭司长，五祭七节，人口调查
加底斯巴尼亚，12探子，徘徊死亡，摩押，摩西，重申律法''')
cr(cvs, '''约书亚到撒母耳''', 356, 356, color2, '''新生代，摩西死，约书亚，进迦南，探耶利哥，分约旦河，城墙倒塌，艾城事件\n26年征服(徒13：20），分地定居png，约书亚死，懂事长老死，埋约瑟骸骨，以利亚撒死，恶性循环，最后士师撒母耳''')#约书亚到分裂共476年，以色列得地450年
cr(cvs, '''扫罗''', 40, 40, color1, '''越权，牧童大卫，歌利亚，大卫被膏，追杀，求鬼，战死''')
cr(cvs, '''大卫''', 40, 40, color2, '''乌利亚的妻子，被儿子追杀''')
cr(cvs, '''所罗门''', 40, 40, color1, '''智慧，繁荣，建殿，箴言，传道，娶妻，偏离，BC931分裂''')
cr(cvs, '''北国以色列''', 0, 209, color2, '''耶罗波安，19, 0，BC722，亚述，以色列''')
cr(cvs, '''南国犹大''', 31, 345, color1, '''20，8，巴比伦，犹大''')

cr(cvs, '''亚述''', 288, 288, color4, '''灭了北国以色列的国家''')
cr(cvs, '''巴比伦''', -5, 76, color4, '''灭了南国犹大的国家''')

cr(cvs, '''约雅敬''', 19, 11, color1, '''BC605，约雅敬，但以理，贵族王族''')
cr(cvs, '''约雅斤''', 1, 1, color2, '''BC597，约雅斤，以西结，首领和技工''')
cr(cvs, '''西底家''', 11, 11, color1, '''BC586，西底家，南国灭''')
cr(cvs, '''被掳70年''', 50, 70, color2, '''但以理在巴比伦''')

cr(cvs, '''波斯''', 20, 204, color4, '''归回，BC515大利乌一世，马拉松战败，圣殿完工，亚哈随鲁（薛西斯一世）以斯帖王后\n波斯：古烈，大利乌一世，亚哈随鲁，亚达薛西一世，大利乌二世，亚达薛西二世，大利乌三世''')

cr(cvs, '''所罗巴伯''', 58, 1, color2, '''BC538-BC515,古烈，49897人，第二圣殿，所罗巴伯，哈该，撒迦利亚''')
cr(cvs, '''以斯拉''', 14, 1, color1, '''BC457，亚达薛西一世，1754人，复兴信仰''')
cr(cvs, '''尼希米''', 112, 19, color2, '''BC444-BC425,亚达薛西，贵族家庭，尼希米，42360人，城墙，52日重修耶路撒冷''')

cr(cvs, '''希腊''', 31, 165, color4, '''BC404-BC331波斯被亚历山大攻陷，亚历山大和大利乌三世几乎同时上位\n马拉松战，亚历山大胜，BC333年，亚历山大33岁，死于蚊子，希腊语''')

cr(cvs, '''托勒密王朝''', 103, 100, color4, '''BC301-BC201=托勒密王朝，被安条克三世占领，BC250，70士译本''')
cr(cvs, '''塞硫西王朝''', 31, 31, color4, '''BC198-BC167=塞硫西王朝，安条克把埃及军队赶出去，安条克四世污秽圣殿''')
cr(cvs, '''马喀比革命''', 3, 3, color2, '''BC167马加比革命，BC164洁净圣殿，修殿节，玛他提亚（祭司长）\n自称撒都该人（贵族），把圣殿中的希腊人都杀人，建立哈斯摩尼王朝''')
cr(cvs, '''哈斯摩尼王朝''', 100, 100, color1, '''BC167-BC64=以色列，自由''')

cr(cvs, '''罗马''', 27, 193, color4, '''BC64，罗马占领巴勒斯坦，罗马庞贝将军占领耶路撒冷，希律家族支配犹大''')

cr(cvs, '''以东人希律''', 33, 40, color4, '''BC37-AD4=以东人希律统治犹大，21城，第三圣殿，BC4，耶稣降生''')

cr(cvs, '''耶稣''', 7, 34, color3, '''BC4-AD31=耶稣在世做工''')

cr(cvs, '''分封王&巡抚''', 40, 35, color4, '''AD4-AD39=分封王&敏感地带巡抚''')
cr(cvs, '''巡抚''', 26, 26, color4, '''AD44=巡抚''')
cr(cvs, '''耶路撒冷沦陷''', 65, 65, color4, '''AD70，罗马提多将军攻陷耶路撒冷,AD130年，驱逐犹太人''')
cr(cvs, '''动乱与镇压''', 2, 2, color4, '''AD135动乱，AD137镇压，禁止犹太人入耶路撒冷''')
cr(cvs, '''全球分散''', 1811, 1811, color2, '''犹太人分散在全世界，直至1948年复国''')
cr(cvs, '''以色列复国''', 69, 69, color1, '''以色列复国，等待弥赛亚''')

#插入不影响：插入的交付为0，例如：
#cr(cvs, '插入不影响', 0, *, color...
#或者上条记录交付=新交付+插入交付，例如：cr(cvs, '''上条''', 40, *, color...
#cr(cvs, '上条', 19/20/21, *, color...
#cr(cvs, '插入', 21/20/19, *, color...
#总原则就是：交付总数不能变，原来总多少，后来也总多少。。。

bibletime.mainloop()

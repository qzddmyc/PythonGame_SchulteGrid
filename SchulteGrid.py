# 这是舒尔特方格训练程序
# 开始创作于2024年2月3日；结稿于2024年2月21日。于大一上寒假。
# 作者：轻舟独钓猫倚窗（Methry_qzddmyc）

import pygame
import sys
import time
import random

"""
列表介绍：
Locat_list：二维列表，包含玩家应当点击的数字及其顺序，其中数字为int型，顺序
final为一维列表，包含int型乱序数字
fin_whole一维乱序，但数字为str型
origin为一维列表，包含str型顺序数字

颜色介绍：
(163,154,123)为按钮的灰底色
(189,202,218)为偏蓝背景色
(144,243,215)为青色字体色
(255,255,255)为白tips色
WRONG为表示错误的暗橙色
"""

GRAY = (163, 154, 123)
BLUE = (189, 202, 218)
CYAN = (144, 243, 215)
WHITE = (255, 255, 255)
WRONG = (225, 143, 48)
REGREEN = (34, 135, 0)
ALBESCENT = (242, 242, 242)

# 游戏内方块占位数据：40 60 30 60 30 60 30 60 30 60 40
Len = 60  # 每个方块长度
Mar = 40
Ave = 30

FPS = 30


# 绘制初始状态下的数字块（列表对应模式，即0对应数字一）
def add_num_up(nuum):
    pygame.draw.rect(screen, GRAY, (Locat_list[nuum][1], Locat_list[nuum][2], Len, Len))
    text_num = ycfont_num.render("{0}".format(origin[nuum]), True, CYAN)
    textRect_num = text_num.get_rect()
    textRect_num = (Locat_list[nuum][1] + 3, Locat_list[nuum][2] + 2)
    screen.blit(text_num, textRect_num)


# 绘制被按下的数字块（列）
def add_num_down(nuum):
    pygame.draw.rect(screen, CYAN, (Locat_list[nuum][1], Locat_list[nuum][2], Len, Len))
    text_num = ycfont_num.render("{0}".format(origin[nuum]), True, GRAY)
    textRect_num = text_num.get_rect()
    textRect_num = (Locat_list[nuum][1] + 3, Locat_list[nuum][2] + 2)
    screen.blit(text_num, textRect_num)


# 绘制已被正确按过的数字块（列）
def add_num_done(nuum):
    pygame.draw.rect(screen, BLUE, (Locat_list[nuum][1], Locat_list[nuum][2], Len, Len))
    text_num = ycfont_num.render("{0}".format(origin[nuum]), True, GRAY)
    textRect_num = text_num.get_rect()
    textRect_num = (Locat_list[nuum][1] + 3, Locat_list[nuum][2] + 2)
    screen.blit(text_num, textRect_num)


# 绘制被错误按下的数字块（列）
def add_num_wrong(nuum):
    pygame.draw.rect(screen, WRONG, (Locat_list[nuum][1], Locat_list[nuum][2], Len, Len))
    text_num = ycfont_num.render("{0}".format(origin[nuum]), True, CYAN)
    textRect_num = text_num.get_rect()
    textRect_num = (Locat_list[nuum][1] + 3, Locat_list[nuum][2] + 2)
    screen.blit(text_num, textRect_num)


# 在“正确选择后方块不变色”模式下，对已经正确点过的方块再点击时，绘制绿色方块
def add_num_again(nuum):
    pygame.draw.rect(screen, REGREEN, (Locat_list[nuum][1], Locat_list[nuum][2], Len, Len))
    text_num = ycfont_num.render("{0}".format(origin[nuum]), True, CYAN)
    textRect_num = text_num.get_rect()
    textRect_num = (Locat_list[nuum][1] + 3, Locat_list[nuum][2] + 2)
    screen.blit(text_num, textRect_num)


# 判断某位置是否在某数字对应区域内（给定：应该点击的数字；被点击出的x,y坐标）（准确对应模式，1对应数字1）
def is_site_in(nuum, px, py):
    tempx, tempy = Locat_list[nuum - 1][1], Locat_list[nuum - 1][2]
    if px >= tempx and px <= tempx + Len and py >= tempy and py <= tempy + Len:
        return True
    return False


##分隔（作弊代码）

# 生成作弊空格按下时显示的提示方块（列）
def cheat_on(nuum):
    pygame.draw.rect(screen, (255, 255, 70), (Locat_list[nuum][1], Locat_list[nuum][2], Len, Len), 2)
    text_num = ycfont_num.render("{0}".format(origin[nuum]), True, CYAN)
    textRect_num = text_num.get_rect()
    textRect_num = (Locat_list[nuum][1] + 3, Locat_list[nuum][2] + 2)
    screen.blit(text_num, textRect_num)


# 作弊空格松开，恢复（与add_num_up相同）
def cheat_off(nuum):
    pygame.draw.rect(screen, GRAY, (Locat_list[nuum][1], Locat_list[nuum][2], Len, Len))
    text_num = ycfont_num.render("{0}".format(origin[nuum]), True, CYAN)
    textRect_num = text_num.get_rect()
    textRect_num = (Locat_list[nuum][1] + 3, Locat_list[nuum][2] + 2)
    screen.blit(text_num, textRect_num)


##分隔(163,154,123)(181,172,141)(193,184,153)由深至浅

# 生成模式一中，挑战失败后下一个方块的浅灰底(同最后几个方块的颜色)深色框；以及最后一个被点击的方块增加深色底绿框（列）
def update_next(nuum):
    pygame.draw.rect(screen, (193, 184, 153), (Locat_list[nuum][1], Locat_list[nuum][2], Len, Len))  # 下一个应该点击方块的浅色
    pygame.draw.rect(screen, (158, 149, 118), (Locat_list[nuum][1], Locat_list[nuum][2], Len, Len),
                     2)  # 下一个应该点击方块的深灰色边框
    text_num = ycfont_num.render("{0}".format(origin[nuum]), True, CYAN)
    textRect_num = text_num.get_rect()
    textRect_num = (Locat_list[nuum][1] + 3, Locat_list[nuum][2] + 2)
    screen.blit(text_num, textRect_num)  # 数字
    if nuum != 0:
        nuum -= 1
        if click_to_hide == False:
            pygame.draw.rect(screen, (158, 149, 118),
                             (Locat_list[nuum][1], Locat_list[nuum][2], Len, Len))  # 被点过最后一个方块的深灰色
            text_num = ycfont_num.render("{0}".format(origin[nuum]), True, CYAN)
            textRect_num = text_num.get_rect()
            textRect_num = (Locat_list[nuum][1] + 3, Locat_list[nuum][2] + 2)
            screen.blit(text_num, textRect_num)  # 其上数字
            pygame.draw.rect(screen, REGREEN, (Locat_list[nuum][1], Locat_list[nuum][2], Len, Len), 2)  # 被点过最后一个方块的绿边框
        else:
            pygame.draw.rect(screen, (84, 185, 50), (Locat_list[nuum][1], Locat_list[nuum][2], Len, Len), 2)  # 被点过最后一个方块的绿边框


# 生成模式一中，挑战失败后除最后几个方块的浅灰色（列）
def update_left(nuum):
    pygame.draw.rect(screen, (193, 184, 153), (Locat_list[nuum][1], Locat_list[nuum][2], Len, Len))
    text_num = ycfont_num.render("{0}".format(origin[nuum]), True, CYAN)
    textRect_num = text_num.get_rect()
    textRect_num = (Locat_list[nuum][1] + 3, Locat_list[nuum][2] + 2)
    screen.blit(text_num, textRect_num)


##分隔

# 判断被点击区域是否为有数字块的区域，并返回点击位置数字值（准）
def is_in_num_area(px, py):
    for i in range(25):
        if is_site_in(i + 1, px, py):
            return i + 1
    return 0


# 生成模式一中所有时间选择块的初始情况
def show_origin_choice():
    for i in range(8):
        pygame.draw.rect(screen, GRAY, (text_site[i][0] - 2, text_site[i][1] - 1, 40, 40))  # 每个小方块的边长为40
        text = ycfont.render(text_con[i], True, CYAN)
        textRect = text.get_rect()
        textRect = (text_site[i][0], text_site[i][1])
        screen.blit(text, textRect)


# 生成模式一中数字n被按下时的方块
def show_sig_pushed(n):
    n = (n - 20) // 5
    pygame.draw.rect(screen, CYAN, (text_site[n][0] - 2, text_site[n][1] - 1, 40, 40))
    text = ycfont.render(text_con[n], True, GRAY)
    textRect = text.get_rect()
    textRect = (text_site[n][0], text_site[n][1])
    screen.blit(text, textRect)


# 生成模式一中数字n对应的初始方块
def show_sig_ori(n):
    n = (n - 20) // 5
    pygame.draw.rect(screen, GRAY, (text_site[n][0] - 2, text_site[n][1] - 1, 40, 40))
    text = ycfont.render(text_con[n], True, CYAN)
    textRect = text.get_rect()
    textRect = (text_site[n][0], text_site[n][1])
    screen.blit(text, textRect)


# 生成模式一中数字n已被选择的方块
def show_sig_done(n):
    n = (n - 20) // 5
    pygame.draw.rect(screen, CYAN, (text_site[n][0] - 2, text_site[n][1] - 1, 40, 40))
    pygame.draw.rect(screen, GRAY, (text_site[n][0] - 2, text_site[n][1] - 1, 40, 40), 2)
    text = ycfont.render(text_con[n], True, GRAY)
    textRect = text.get_rect()
    textRect = (text_site[n][0], text_site[n][1])
    screen.blit(text, textRect)


# 对于模式一选择中的时间块，给定坐标值，返回该坐标值对应的数字
def check_pos_choice(pox, poy):
    for po in text_site:
        if pox > po[0] and pox < po[0] + 40 and poy > po[1] and poy < po[1] + 40:
            return ((po[0] - 220) // 68 * 5 + 20) + ((po[1] - 125) // 50 * 20)  # 通过位置的运算返回该坐标下的数字值
            # 20至55对应的左上角坐标值分别为：[220, 125] [288, 125] [356, 125] [424, 125] [220, 175] [288, 175] [356, 175] [424, 175]
    return 0


##分隔

# 生成末页的“再次挑战”的初始按钮
def zctz_ori():
    pygame.draw.rect(screen, GRAY, (orix, oriy, length, height))
    text_bot1 = ycfont_startbot.render("再次挑战", True, CYAN)
    textRect_bot1 = text_bot1.get_rect()
    textRect_bot1 = (orix + 9, oriy + 12)
    screen.blit(text_bot1, textRect_bot1)


# 末页的“再次挑战”按下的按钮
def zctz_pressed():
    pygame.draw.rect(screen, CYAN, (orix, oriy, length, height))
    text_bot1 = ycfont_startbot.render("再次挑战", True, GRAY)
    textRect_bot1 = text_bot1.get_rect()
    textRect_bot1 = (orix + 9, oriy + 12)
    screen.blit(text_bot1, textRect_bot1)


# 生成末页的“退出游戏”的初始按钮
def tcyx_ori():
    pygame.draw.rect(screen, GRAY, (orix + gap, oriy, length, height))
    text_bot1 = ycfont_startbot.render("退出游戏", True, CYAN)
    textRect_bot1 = text_bot1.get_rect()
    textRect_bot1 = (orix + gap + 9, oriy + 12)
    screen.blit(text_bot1, textRect_bot1)


# 末页的“退出游戏”按下的按钮
def tcyx_pressed():
    pygame.draw.rect(screen, CYAN, (orix + gap, oriy, length, height))
    text_bot1 = ycfont_startbot.render("退出游戏", True, GRAY)
    textRect_bot1 = text_bot1.get_rect()
    textRect_bot1 = (orix + gap + 9, oriy + 12)
    screen.blit(text_bot1, textRect_bot1)


# 初始化
pygame.init()
screen = pygame.display.set_mode(size=(500, 500))
# pygame.mouse.set_visible(False)
# pygame.event.set_grab(True)

# 图标及标题设定
pygame.display.set_caption("Focus Training from qzddmyc", "yc")
icon = pygame.image.load("yc_extrafile\game_icon.jpg")
pygame.display.set_icon(icon)

# 字体设置
ycfont = pygame.font.Font("yc_extrafile\HYWenHei_85W.ttf", 30)
ycfont_startbot = pygame.font.Font("yc_extrafile\HYWenHei_85W.ttf", 35)
ycfont_surebot = pygame.font.Font("yc_extrafile\HYWenHei_85W.ttf", 40)
ycfont_num = pygame.font.Font("yc_extrafile\HYWenHei_85W.ttf", 45)
ycfont_tip = pygame.font.Font("yc_extrafile\HYWenHei_85W.ttf", 17)
ycfont_big_num = pygame.font.Font("yc_extrafile\HYWenHei_85W.ttf", 60)
ycfont_sma_num = pygame.font.Font("yc_extrafile\HYWenHei_85W.ttf", 25)
ycfont_choice = pygame.font.Font("yc_extrafile\HYWenHei_85W.ttf", 22)
ycfont_sta = pygame.font.Font("yc_extrafile\HYWenHei_85W.ttf", 10)

# 时间对象
clock = pygame.time.Clock()

REpeat = True
while REpeat:

    # 生成随机数
    final = random.sample(range(1, 26), 25)

    # 数字都改为str型两位数
    fin_whole = []
    for temp in final:
        if temp < 10:
            fin_whole.append('0' + str(temp))
        else:
            fin_whole.append(temp)

    # 保存一个规则的01至25列表
    origin = list(range(1, 26))
    for temp in origin:
        if temp < 10:
            origin[temp - 1] = '0' + str(temp)

    # 画布染色
    screen.fill(BLUE)
    pygame.display.flip()

    # 初始文字展示
    introduction = ["这是一个基于舒尔特方格训练法", "制作的程序，有两种模式可选择", "", "模式一：限定时间，时间可自选",
                    "模式二：不限时，但会为你计时", "", "请在下方选择模式："]
    sitex = 40
    sitey = 40
    for yc in range(7):
        text = ycfont.render(introduction[yc], True, (255, 255, 255), None)
        textRect = text.get_rect()
        textRect = (sitex, sitey)
        screen.blit(text, textRect)
        sitey += 35

    text = ycfont_tip.render("*具体玩法：在5×5随机打乱的表格中依次点击01至25即可", True, (245, 245, 245))
    textRect = text.get_rect()
    textRect = (30, 440)
    screen.blit(text, textRect)

    # 按钮一
    bot1x, bot1y, bot1l, bot1h = 60, 340, 130, 65
    pygame.draw.rect(screen, (163, 154, 123), (bot1x, bot1y, bot1l, bot1h))
    text_bot1 = ycfont_startbot.render("模式一", True, (144, 243, 215))
    textRect_bot1 = text_bot1.get_rect()
    textRect_bot1 = (72, 352)
    screen.blit(text_bot1, textRect_bot1)

    # 按钮二
    bot2x, bot2y, bot2l, bot2h = 280, 340, 130, 65
    pygame.draw.rect(screen, (163, 154, 123), (bot2x, bot2y, bot2l, bot2h))
    text_bot2 = ycfont_startbot.render("模式二", True, (144, 243, 215))
    textRect_bot2 = text_bot2.get_rect()
    textRect_bot2 = (292, 352)
    screen.blit(text_bot2, textRect_bot2)

    pygame.display.update()

    '''模式选择（界面一选择模式部分）'''
    Judge = True
    mode = 0
    check1down = check2down = check1up = check2up = False  # 判断按下鼠标与松开鼠标在同一键上
    while Judge:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                posx, posy = event.pos
                if posx >= bot1x and posx <= bot1x + bot1l and posy >= bot1y and posy <= bot1y + bot1h:
                    pygame.draw.rect(screen, (144, 243, 215), (bot1x, bot1y, bot1l, bot1h))
                    text_bot1 = ycfont_startbot.render("模式一", True, (163, 154, 123))
                    textRect_bot1 = text_bot1.get_rect()
                    textRect_bot1 = (72, 352)
                    screen.blit(text_bot1, textRect_bot1)
                    check1down = True

                if posx >= bot2x and posx <= bot2x + bot2l and posy >= bot2y and posy <= bot2y + bot2h:
                    pygame.draw.rect(screen, (144, 243, 215), (bot2x, bot2y, bot2l, bot2h))
                    text_bot2 = ycfont_startbot.render("模式二", True, (163, 154, 123))
                    textRect_bot2 = text_bot1.get_rect()
                    textRect_bot2 = (292, 352)
                    screen.blit(text_bot2, textRect_bot2)
                    check2down = True

            if event.type == pygame.MOUSEBUTTONUP:
                pygame.draw.rect(screen, (163, 154, 123), (bot1x, bot1y, bot1l, bot1h))
                text_bot1 = ycfont_startbot.render("模式一", True, (144, 243, 215))
                textRect_bot1 = text_bot1.get_rect()
                textRect_bot1 = (72, 352)
                screen.blit(text_bot1, textRect_bot1)
                pygame.draw.rect(screen, (163, 154, 123), (bot2x, bot2y, bot2l, bot2h))
                text_bot2 = ycfont_startbot.render("模式二", True, (144, 243, 215))
                textRect_bot2 = text_bot1.get_rect()
                textRect_bot2 = (292, 352)
                screen.blit(text_bot2, textRect_bot2)

                posx, posy = event.pos
                if posx >= bot1x and posx <= bot1x + bot1l and posy >= bot1y and posy <= bot1y + bot1h and check1down == True:
                    check1up = True
                if (posx >= bot1x and posx <= bot1x + bot1l and posy >= bot1y and posy <= bot1y + bot1h) == False and check1down == True:
                    check1down = False
                if posx >= bot2x and posx <= bot2x + bot2l and posy >= bot2y and posy <= bot2y + bot2h and check2down == True:
                    check2up = True
                if (posx >= bot2x and posx <= bot2x + bot2l and posy >= bot2y and posy <= bot2y + bot2h) == False and check2down == True:
                    check2down = False

            if check1down and check1up:
                mode = 1
                Judge = False
            if check2down and check2up:
                mode = 2
                Judge = False

            pygame.display.update()
        clock.tick(FPS)

    # 画布清除并准备刷新
    screen.fill(BLUE)
    pygame.display.flip()

    Locat_list = []

    '''模式一的界面二布置'''  # 55,50,45,40,35,30,25,20
    if mode == 1:
        # 确认界面
        text_temp = ["当前为模式一，", "请选择时间后点击确定以开始"]
        for i in range(2):
            text = ycfont.render(text_temp[i], True, (255, 255, 255))
            textRect = text.get_rect()
            textRect = (40, 20 + 37 * i)
            screen.blit(text, textRect)

        text_con = ["20", "25", "30", "35", "40", "45", "50", "55"]
        stax, stay = 220, 125  # 最左上角的坐标值
        avex, avey = 68, 50  # 两个trigger之间的间隔
        text_site = [[stax, stay], [stax + avex, stay], [stax + avex * 2, stay], [stax + avex * 3, stay],
                     [stax, stay + avey], [stax + avex, stay + avey], [stax + avex * 2, stay + avey],
                     [stax + avex * 3, stay + avey]]
        show_origin_choice()

        text = ycfont_tip.render("单位：秒", True, (245, 245, 245))
        textRect = text.get_rect()
        textRect = (300, 97)
        screen.blit(text, textRect)

    # '''模式二的界面二布置'''
    elif mode == 2:
        # 确认界面
        text = ycfont.render("当前为模式二，点击确定后开始", True, (255, 255, 255))
        textRect = text.get_rect()
        textRect = (40, 40)
        screen.blit(text, textRect)

    '''界面二共用部分布置'''
    text = ycfont_surebot.render("确定", True, (163, 154, 123))
    textRect = text.get_rect()
    textRect = (100, 120)
    screen.blit(text, textRect)

    ##额外选项部分
    click_to_hide = False  # 正确点击后是否隐藏，默认不隐藏(False)
    show_next_num = False
    show_time = False

    text = ycfont_sma_num.render("*以下为可供选择的额外选项：", True, (250, 250, 200))
    textRect = text.get_rect()
    textRect = (55, 250)
    screen.blit(text, textRect)

    # 位置信息
    locx, locy = 78, 300
    gaap = 40

    # 隐藏被正确点击过的数字块
    pygame.draw.rect(screen, WHITE, (locx, locy, 20, 20), 2)
    text = ycfont_choice.render("隐藏被正确点击过的数字块", True, ALBESCENT)
    textRect = text.get_rect()
    textRect = (locx + 33, locy - 3)
    screen.blit(text, textRect)

    # 显示下一个数字的值
    pygame.draw.rect(screen, WHITE, (locx, locy + gaap, 20, 20), 2)
    text = ycfont_choice.render("显示下一个数字的值", True, ALBESCENT)
    textRect = text.get_rect()
    textRect = (locx + 33, locy - 3 + gaap)
    screen.blit(text, textRect)

    # 显示已用/剩余时间
    pygame.draw.rect(screen, WHITE, (locx, locy + gaap * 2, 20, 20), 2)
    if mode == 1:
        text = ycfont_choice.render("显示剩余时间", True, ALBESCENT)
    else:
        text = ycfont_choice.render("显示已用时间", True, ALBESCENT)
    textRect = text.get_rect()
    textRect = (locx + 33, locy - 3 + gaap * 2)
    screen.blit(text, textRect)

    # 末尾关于可作弊的tip
    text = ycfont_tip.render("tips：挑战中，按下空格键可获得下一个数字的位置提示", True, (247, 247, 247))
    textRect = text.get_rect()
    textRect = (45, 440)
    screen.blit(text, textRect)

    pygame.display.update()

    '''界面二的用户选择部分'''
    Judge = True
    check3down = check3up = False  # 用于确定按钮
    if mode == 1:
        set_time = 0  # 存储玩家选择的目标时间
        check6down = check6up = 0  # 用于选择目标时间的按钮
        check7 = False  # 存储是否显示“时间未选择文字”

    while Judge:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                posx, posy = event.pos
                if posx >= 100 and posx <= 180 and posy >= 120 and posy <= 160:
                    pygame.draw.rect(screen, BLUE, (98, 120, 84, 44))  # 确定键处的屏幕覆盖
                    text = ycfont_surebot.render("确定", True, (144, 243, 215))
                    textRect = text.get_rect()
                    textRect = (100, 120)
                    screen.blit(text, textRect)
                    check3down = True

                if mode == 1:
                    teemp = check_pos_choice(posx, posy)
                    if teemp and teemp != set_time:
                        check6down = check_pos_choice(posx, posy)
                        show_sig_pushed(check6down)

                # 额外选项的改变；locx=78；x1=375,x2=310,x3=243
                if posx >= locx and posx <= locx + 297 and posy >= locy and posy <= locy + 20:
                    if click_to_hide == False:
                        click_to_hide = True
                        pygame.draw.rect(screen, CYAN, (locx + 4, locy + 4, 12, 12))
                        text = ycfont_choice.render("隐藏被正确点击过的数字块", True, WHITE, BLUE)
                        textRect = text.get_rect()
                        textRect = (locx + 33, locy - 3)
                        screen.blit(text, textRect)
                    elif click_to_hide == True:
                        click_to_hide = False
                        pygame.draw.rect(screen, BLUE, (locx, locy, 20, 20))
                        pygame.draw.rect(screen, WHITE, (locx, locy, 20, 20), 2)
                        text = ycfont_choice.render("隐藏被正确点击过的数字块", True, ALBESCENT, BLUE)
                        textRect = text.get_rect()
                        textRect = (locx + 33, locy - 3)
                        screen.blit(text, textRect)
                if posx >= locx and posx <= locx + 232 and posy >= locy + gaap and posy <= locy + gaap + 20:
                    if show_next_num == False:
                        show_next_num = True
                        pygame.draw.rect(screen, CYAN, (locx + 4, locy + gaap + 4, 12, 12))
                        text = ycfont_choice.render("显示下一个数字的值", True, WHITE, BLUE)
                        textRect = text.get_rect()
                        textRect = (locx + 33, locy - 3 + gaap)
                        screen.blit(text, textRect)
                    elif show_next_num == True:
                        show_next_num = False
                        pygame.draw.rect(screen, BLUE, (locx, locy + gaap, 20, 20))
                        pygame.draw.rect(screen, WHITE, (locx, locy + gaap, 20, 20), 2)
                        text = ycfont_choice.render("显示下一个数字的值", True, ALBESCENT, BLUE)
                        textRect = text.get_rect()
                        textRect = (locx + 33, locy - 3 + gaap)
                        screen.blit(text, textRect)
                if posx >= locx and posx <= locx + 165 and posy >= locy + gaap * 2 and posy <= locy + gaap * 2 + 20:
                    if show_time == False:
                        show_time = True
                        pygame.draw.rect(screen, CYAN, (locx + 4, locy + gaap * 2 + 4, 12, 12))
                        if mode == 1:
                            text = ycfont_choice.render("显示剩余时间", True, WHITE, BLUE)
                        else:
                            text = ycfont_choice.render("显示已用时间", True, WHITE, BLUE)
                        textRect = text.get_rect()
                        textRect = (locx + 33, locy - 3 + gaap * 2)
                        screen.blit(text, textRect)
                    elif show_time == True:
                        show_time = False
                        pygame.draw.rect(screen, BLUE, (locx, locy + gaap * 2, 20, 20))
                        pygame.draw.rect(screen, WHITE, (locx, locy + gaap * 2, 20, 20), 2)
                        if mode == 1:
                            text = ycfont_choice.render("显示剩余时间", True, ALBESCENT, BLUE)
                        else:
                            text = ycfont_choice.render("显示已用时间", True, ALBESCENT, BLUE)
                        textRect = text.get_rect()
                        textRect = (locx + 33, locy - 3 + gaap * 2)
                        screen.blit(text, textRect)

            if event.type == pygame.MOUSEBUTTONUP:
                posx, posy = event.pos
                if posx >= 100 and posx <= 180 and posy >= 120 and posy <= 160 and check3down:
                    check3up = True
                    pygame.draw.rect(screen, BLUE, (98, 120, 84, 44))  # 确定键处的屏幕覆盖
                    text = ycfont_surebot.render("确定", True, (163, 154, 123))
                    textRect = text.get_rect()
                    textRect = (100, 120)
                    screen.blit(text, textRect)
                if (posx >= 100 and posx <= 180 and posy >= 120 and posy <= 160) == False and check3down:
                    check3down = False
                    pygame.draw.rect(screen, BLUE, (98, 120, 84, 44))  # 确定键处的屏幕覆盖
                    text = ycfont_surebot.render("确定", True, (163, 154, 123))
                    textRect = text.get_rect()
                    textRect = (100, 120)
                    screen.blit(text, textRect)

                if mode == 1:
                    temp_check_pos = check_pos_choice(posx, posy)
                    if temp_check_pos == check6down and check6down != 0 and check6down != set_time:
                        check6up = temp_check_pos
                    if (temp_check_pos == 0 or temp_check_pos != check6down) and check6down and check6down != set_time:
                        show_sig_ori(check6down)
                        check6down = 0

            if check3down and check3up:  # 确定键被按下
                if mode == 2:
                    Judge = False
                if mode == 1:
                    if set_time == 0 and check7 == False:  # 当前未选择时间
                        text = ycfont_tip.render("请先选择目标时间", True, (245, 245, 245))
                        textRect = text.get_rect()
                        textRect = (60, 175)
                        screen.blit(text, textRect)
                        check7 = True
                    if set_time != 0:
                        if check7 == True:
                            pygame.draw.rect(screen, BLUE, (57, 172, 141, 22))  # 未选时间提示处的屏幕覆盖
                            check7 = False
                        Judge = False
                check3down = check3up = False

            if mode == 1:  # 时间选择键被不重复地按下
                if check6up == check6down and check6up and check6down and check6down != set_time:
                    if set_time != 0:
                        show_origin_choice()
                    set_time = check6down
                    show_sig_done(check6down)
                    if check7:
                        pygame.draw.rect(screen, BLUE, (57, 172, 141, 22))  # 未选时间提示处的屏幕覆盖
                        check7 = False

            pygame.display.update()
        clock.tick(FPS)

    """
    ##########标记，可删。此处可直接修改用户设定的时间(set_time)
    """
    
    # 画布清除并开始游戏
    screen.fill(BLUE)
    pygame.display.flip()

    # 放置所需的25个方块
    for num in range(25):
        # 保存数字信息，位置暂定为(0,0)
        temp2 = [final[num], 0, 0]
        tem_fin_whole = fin_whole[num]

        locatey = Mar + (num // 5) * (Len + Ave)
        num += 1
        num %= 5
        if num == 0:
            num = 5
        locatex = Mar + (num - 1) * (Len + Ave)
        pygame.draw.rect(screen, (163, 154, 123), (locatex, locatey, Len, Len))

        # 保存位置信息 [数字，x轴起点，y轴起点]
        temp2[1], temp2[2] = locatex, locatey
        Locat_list.append(temp2)

        # 方块上的数字显示
        text_num = ycfont_num.render("{0}".format(tem_fin_whole), True, (144, 243, 215))
        textRect_num = text_num.get_rect()
        textRect_num = (locatex + 3, locatey + 2)
        screen.blit(text_num, textRect_num)

    pygame.display.update()

    # 对Locat_list进行排序操作，按数字位由小到大
    for i in range(25):
        for j in range(25 - i - 1):
            if Locat_list[j][0] > Locat_list[j + 1][0]:
                temp3 = Locat_list[j + 1]
                Locat_list[j + 1] = Locat_list[j]
                Locat_list[j] = temp3

    pygame.display.update()

    ##游戏核心部分

    counter = 0
    
    """
    ##########可修改counter为25（该值应该为0），直接测试结算画面
    """
    
    check4down = check4up = False  # 用于正确块检查
    check5 = 0  # 用于错误块的检查
    check8 = 0  # 用于不改变颜色中，已按下的块的检查

    cheat = False  # 检查作弊状态是否开启（空格是否按下）

    '''正式游戏部分的程序'''
    # 对于模式一，程序分为正常结束（规定时间内完成），以及异常结束（规定时间未完成）；该变量为True时，正常结束；为False时，异常结束。
    norm_ter = True

    time_start = time.time()  # 计时
    while counter != 25 and norm_ter:
        # 显示下一个数字
        if show_next_num == True:
            text = ycfont_tip.render("下一个待点击数字为：{}".format(origin[counter]), True, (245, 245, 245), BLUE)
            textRect = text.get_rect()
            textRect = (5, 5)
            screen.blit(text, textRect)
            pygame.display.update()

        # 显示已用/剩余时间
        if show_time == True:
            time_show = time.time()
            time_show = round(time_show - time_start)
            if mode == 1:
                time_show = set_time - time_show
                if time_show <= 9:
                    if time_show < 0:
                        time_show = 0
                    time_show = "0" + str(time_show)
                text = ycfont_tip.render("时间剩余：{}秒".format(time_show), True, (245, 245, 245), BLUE)
                textRect = text.get_rect()
                textRect = (360, 5)
                screen.blit(text, textRect)
            if mode == 2:
                if time_show <= 9:
                    if time_show < 0:
                        time_show = 0
                    time_show = "0" + str(time_show)
                text = ycfont_tip.render("时间已用：{}秒".format(time_show), True, (245, 245, 245), BLUE)
                textRect = text.get_rect()
                textRect = (360, 5)
                screen.blit(text, textRect)

            pygame.display.update()

        # 模式一到时间截止语句
        if mode == 1:
            time_now = time.time()
            time_now = round(time_now - time_start, 4)
            if time_now >= set_time:
                norm_ter = False

        if norm_ter:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    # 空格（作弊）按下
                    if event.key == pygame.K_SPACE and cheat == False and check4down == False:
                        cheat = True
                        cheat_on(counter)

                if event.type == pygame.KEYUP:
                    # Esc键
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    # 空格松开
                    if event.key == pygame.K_SPACE and cheat == True and check4down == False:
                        cheat = False
                        cheat_off(counter)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    posx, posy = event.pos
                    clicknum = is_in_num_area(posx, posy)
                    if is_site_in(counter + 1, posx, posy):  # 按下位置正确
                        add_num_down(counter)
                        check4down = True
                    elif clicknum > counter + 1:  # 点击错误情况
                        add_num_wrong(clicknum - 1)
                        check5 = clicknum
                    if click_to_hide == False:  # 再次点击已经点击过的方块
                        if clicknum <= counter and clicknum > 0:
                            add_num_again(clicknum - 1)
                            check8 = clicknum

                if event.type == pygame.MOUSEBUTTONUP:
                    posx, posy = event.pos
                    if is_site_in(counter + 1, posx, posy) and check4down:  # 松手位置正确
                        check4up = True
                    if is_site_in(counter + 1, posx, posy) == False and check4down:  # 松手位置错误
                        check4down = False
                        add_num_up(counter)
                    if check5:  # 错误情况对方块复原
                        add_num_up(check5 - 1)
                        check5 = 0
                    if check8:  # 按到已经按下的情况对方块复原
                        add_num_up(check8 - 1)
                        check8 = 0

                if check4down and check4up:  # 按下与松开均正确，判True
                    if click_to_hide:
                        add_num_done(counter)
                    else:  # 选择了按对之后不改变颜色
                        add_num_up(counter)
                    check4down = check4up = False
                    if cheat == True:
                        cheat = False
                    counter += 1

                pygame.display.update()

        # 额外选项在时间结束或成功后的显示
        if show_next_num == True and counter == 25:
            pygame.draw.rect(screen, BLUE, (3, 3, 200, 23))
        if show_time == True:
            if norm_ter == False:
                pygame.draw.rect(screen, BLUE, (355, 3, 140, 23))
                text = ycfont_tip.render("倒计时结束", True, (245, 245, 245), BLUE)
                textRect = text.get_rect()
                textRect = (360, 5)
                screen.blit(text, textRect)
            elif counter == 25:
                pygame.draw.rect(screen, BLUE, (355, 3, 140, 23))
                text = ycfont_tip.render("挑战已完成", True, (245, 245, 245), BLUE)
                textRect = text.get_rect()
                textRect = (360, 5)
                screen.blit(text, textRect)

        pygame.display.update()

        clock.tick(FPS)
    time_end = time.time()

    time_all = round(time_end - time_start, 2)
    
    """
    ##########可以在此修改time_all的值（用户完成挑战花费的总时间）
    """
    
    # 说明：time_all为XX.XX的str型字符，time_all_int为int型数字
    
    revamp_a = revamp_b = revamp_c = False  # a表示小数点之前只有一位；b小数点之后只有一位；c只有整数部分
    if time_all < 10 and time_all > 0:
        revamp_a = True
    if round(time_all * 100) % 10 == 0:
        revamp_b = True
    if round(time_all * 100) % 100 == 0:
        revamp_c = True
        time_all = int(time_all)

    # 为后文备份数据
    time_all_int = time_all

    # 时间显示修改为固定XX.XX形式
    if revamp_a:
        time_all = '0' + str(time_all)
    if revamp_b and revamp_c == False:
        time_all = str(time_all) + '0'
    if revamp_c:
        time_all = str(time_all) + '.00'

    # if后为正常结束时跳转到最后一页的设定；else后为非正常结束的提示（该if-else到清屏前即可，不需更新屏幕）
    if norm_ter:
        text = ycfont_tip.render("挑战已完成，再次点击屏幕任意处以查看成绩", True, (245, 245, 245))
        textRect = text.get_rect()
        textRect = (35, 467)
        screen.blit(text, textRect)
        pygame.display.update()

        # 判断是否点击屏幕，点击后进行结算
        Judge = True
        while Judge:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                if event.type == pygame.MOUSEBUTTONUP:
                    Judge = False
            clock.tick(FPS)

    else:
        update_next(counter)
        if counter != 24:
            for i in range(counter + 1, 25):
                update_left(i)
        pygame.display.update()

        pt = 4  # pausetime，暂停的时间。倒计时结束后pauset值为pt+1
        time_pause_start = time.time()  # 暂停pt秒无法点击的开始时间
        pauset = 1
        check_onetime = True  # pt秒过后的提示只更新一遍
        Judge = True
        while Judge:
            # 底部文字显示及可否点击的判断
            if pauset < pt + 1:
                time_pause_now = time.time()
                time_pause_now = round(time_pause_now - time_pause_start, 4)
                text = ycfont_tip.render(f"时间到，挑战失败，请于{pt + 1 - pauset}秒后点击屏幕进行结算", True, (245, 245, 245), BLUE)
                if time_pause_now >= pauset:
                    pauset += 1
                textRect = text.get_rect()
                textRect = (35, 467)
                screen.blit(text, textRect)
            elif pauset == pt + 1 and check_onetime:
                text = ycfont_tip.render("时间到，挑战失败，请点击屏幕任意处以进行结算", True, (245, 245, 245), BLUE)
                textRect = text.get_rect()
                textRect = (35, 467)
                screen.blit(text, textRect)
                check_onetime = False

            pygame.display.update()

            # 判断鼠标操作
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                if pauset == pt + 1:
                    if event.type == pygame.MOUSEBUTTONUP:
                        Judge = False

            clock.tick(FPS)

    # 清屏，之后加载结算页面
    screen.fill(BLUE)
    pygame.display.flip()

    # 结算画面
    endwidth = 0  # 结束语的y坐标
    if mode == 2:
        if time_all_int < 100 and time_all_int > 0:
            endwidth = 100

            text = ycfont.render("此次成绩为：", True, WHITE)
            textRect = text.get_rect()
            textRect = (100, 100)
            screen.blit(text, textRect)

            text = ycfont_big_num.render("{}".format(time_all), True, WHITE)
            textRect = text.get_rect()
            textRect = (120, 150)
            screen.blit(text, textRect)

            text = ycfont.render("秒", True, WHITE)
            textRect = text.get_rect()
            textRect = (300, 180)
            screen.blit(text, textRect)
        else:
            endwidth = 25

            textline = ["嗯？训练期间请不要走神", "时间已大于100秒", "屏幕都要被撑爆了，不再进行展示"]
            if time_all_int <= 0:
                textline = ["喂！请不要在训练期间使用虫洞", "系统时间都被修改了", "快去重新挑战"]
            for i in range(3):
                text = ycfont.render(textline[i], True, WHITE)
                textRect = text.get_rect()
                textRect = (25, 100 + 40 * i)
                screen.blit(text, textRect)

    elif mode == 1 and norm_ter:
        endwidth = 50

        text = ycfont.render("祝贺你在{0}秒内完成了挑战，".format(set_time), True, WHITE)
        textRect = text.get_rect()
        textRect = (50, 60)
        screen.blit(text, textRect)

        text = ycfont.render("此次实际用时为：", True, WHITE)
        textRect = text.get_rect()
        textRect = (50, 100)
        screen.blit(text, textRect)

        text = ycfont_big_num.render("{}".format(time_all), True, WHITE)
        textRect = text.get_rect()
        textRect = (120, 150)
        screen.blit(text, textRect)

        text = ycfont.render("秒", True, WHITE)
        textRect = text.get_rect()
        textRect = (300, 180)
        screen.blit(text, textRect)

    else:
        endwidth = 70

        if counter == 0:
            temp_num = "00"
        else:
            temp_num = origin[counter - 1]
        textline = ["很遗憾，挑战失败。", "此次挑战目标用时为：{}秒".format(set_time), "实际找至数字：{}".format(temp_num)]
        for i in range(3):
            text = ycfont.render(textline[i], True, WHITE)
            textRect = text.get_rect()
            textRect = (70, 100 + 40 * i)
            screen.blit(text, textRect)

    # 重新开始以及关闭程序按钮
    text = ycfont.render("现在，你可以选择：", True, WHITE)
    textRect = text.get_rect()
    textRect = (endwidth, 240)
    screen.blit(text, textRect)

    # 按钮基本位置信息
    orix, oriy, length, height = 65, 320, 160, 68
    gap = 215

    pygame.draw.rect(screen, (163, 154, 123), (orix, oriy, length, height))
    pygame.draw.rect(screen, (163, 154, 123), (orix + gap, oriy, length, height))

    text_bot1 = ycfont_startbot.render("再次挑战", True, (144, 243, 215))
    textRect_bot1 = text_bot1.get_rect()
    textRect_bot1 = (orix + 9, oriy + 12)
    screen.blit(text_bot1, textRect_bot1)

    text_bot1 = ycfont_startbot.render("退出游戏", True, (144, 243, 215))
    textRect_bot1 = text_bot1.get_rect()
    textRect_bot1 = (orix + gap + 9, oriy + 12)
    screen.blit(text_bot1, textRect_bot1)

    '''
    text = ycfont_sta.render("Edited by Methry_qzddmyc", True, WHITE)
    textRect = text.get_rect()
    textRect = (404,485)
    screen.blit(text,textRect)
    '''
    pygame.display.update()

    '''界面四（用户选择再次挑战或者退出游戏）'''
    check9down = check9up = check10down = check10up = False
    Judge = True
    while Judge:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                posx, posy = event.pos
                if posx >= orix and posx <= orix + length and posy >= oriy and posy <= oriy + height:
                    zctz_pressed()
                    check9down = True
                if posx >= orix + gap and posx <= orix + length + gap and posy >= oriy and posy <= oriy + height:
                    tcyx_pressed()
                    check10down = True

            if event.type == pygame.MOUSEBUTTONUP:
                posx, posy = event.pos
                if posx >= orix and posx <= orix + length and posy >= oriy and posy <= oriy + height and check9down:
                    zctz_ori()
                    check9up = True
                if (posx >= orix and posx <= orix + length and posy >= oriy and posy <= oriy + height) == False and check9down:
                    zctz_ori()
                    check9down = False

                if posx >= orix + gap and posx <= orix + length + gap and posy >= oriy and posy <= oriy + height and check10down:
                    tcyx_ori()
                    pygame.display.update()
                    check10up = True
                if (posx >= orix + gap and posx <= orix + length + gap and posy >= oriy and posy <= oriy + height and check10down) == False and check10down:
                    tcyx_ori()
                    check10down = False

            if check9down and check9up:
                Judge = False
            if check10down and check10up:
                Judge = False
                REpeat = False
                pygame.quit()
                sys.exit()

            pygame.display.update()
        clock.tick(FPS)

    screen.fill(BLUE)
    pygame.display.flip()

    # 重置画面
    text_update = ycfont_num.render("重置中...", True, WHITE)
    textRect_update = text_update.get_rect()
    textRect_update = (115, 90)
    screen.blit(text_update, textRect_update)

    time_update_a = time.time()
    time_update_a = round(time_update_a, 4)

    for i in range(12):
        pygame.draw.rect(screen, (240, 240, 240), (60 + i * 33, 185, 20, 40), 3)

    n = 1
    while n != 14:
        time_update_b = time.time()
        time_update_b = round(time_update_b - time_update_a, 4)

        if time_update_b > n * 0.15:
            n += 1

        if n != 1 and n != 14:
            pygame.draw.rect(screen, (240, 240, 240), (60 + (n - 2) * 33, 185, 20, 40))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        clock.tick(FPS)

# end

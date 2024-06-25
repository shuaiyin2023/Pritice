import pygame
from pygame.locals import *

# 使用pygame前需要进行初始化
pygame.init()

# 创建游戏窗口
width, height = 600, 500
screen = pygame.display.set_mode(size=(width, height), flags=pygame.RESIZABLE)
pygame.display.set_caption("The First Pygame")

# 创建一个字体对象 None:使用默认字体，60为字体大小
my_font = pygame.font.Font(None, 60)
white = (255, 255, 255)
blue = (0, 0, 255)
pink = (255, 192, 203)

# 加载图片
image_2 = pygame.image.load("./images/zombie.png")
image_2 = pygame.transform.scale(image_2, (50, 50))  # 缩放图片


position_x = position_y = x = y = 0


""" 执行鼠标和键盘事件的逻辑 """
clicked = False
# 圆的移动速度
speed = 2
# 创建一个子弹列表
bullets = []
speeds = []


def bullet_update():
    global bullets, speed, width
    for i, bullet in enumerate(bullets):
        bullet[0] += speeds[i]  # 假设子弹向右移动
        # 检查子弹是否超出屏幕边界
        if bullet[0] < 0 or bullet[0] > width:
            # 子弹触碰到左右边界时，反转水平速度方向
            bullet[0] = max(0, min(bullet[0], width))  # 限制子弹在屏幕范围内
            speeds[i] = -speeds[i]  # 反向移动
            # bullets.remove(bullet)  # 子弹触碰到边框则消失
            # speeds.remove(speeds[i])


def bullet_draw():
    global bullets
    for bullet in bullets:
        pygame.draw.circle(screen, pink, (int(bullet[0]), int(bullet[1])), 10)


def event_func(event_ele):
    global position_x, position_y, x, y, clicked
    ''' 鼠标事件 '''
    if event_ele.type == pygame.MOUSEBUTTONDOWN:
        if event_ele.button == 1:
            clicked = True
            position_x, position_y = event_ele.pos
            bullets.append([position_x, position_y])
            speeds.append(speed)

            # screen_ele.blit(image_2_ele, (int(position_x), int(position_y)))
            # pygame.display.update()

    ''' 键盘事件 '''
    if event_ele.type == KEYDOWN:

        if event_ele.key == K_DOWN:
            y = 1
            x = 0
        elif event_ele.key == K_UP:
            y = -1
            x = 0
        elif event_ele.key == K_LEFT:
            x = -1
            y = 0
        elif event_ele.key == K_RIGHT:
            x = 1
            y = 0

    elif event_ele.type == KEYUP:
        x = 0
        y = 0

    return x, y


""" 游戏主循环 用于循环监听游戏的所有事件，这是所有pygame程序必不可少的一部分 """
# 游戏循环
clock = pygame.time.Clock()

# 只是初始化不做任何设定的话，屏幕窗口只会短暂的一闪而过
while True:  # 通过while循环让窗口一直显示
    # 还需要对用户的操作进行事件处理，例如：当用户点击屏幕的×，会关闭窗口
    # 读取事件
    for event in pygame.event.get():
        # 如果按下右上角的叉，关闭窗口
        if event.type == QUIT:
            exit()  # 程序退出

        x, y = event_func(event)

    # key_board_events = pygame.key.get_pressed()  # 获取所有键盘按下的情况
    # mouse_events = pygame.mouse.get_pressed()  # 获取所有鼠标按下的情况
    # print("mouse_events:", mouse_events)
    # print("用户按下的所有事件: ", key_board_events)
    # if key_board_events[K_LEFT]:
    #     print("yesssssssssss")
    # position_x += x
    # position_y += y
    # 清除屏幕内容(这里实际上是将窗口填充成了黑色，所以看不见图片的运行轨迹，实现了类似于清除运行轨迹的效果)
    # screen.fill((0, 0, 0))
    # screen.blit(image_2, (int(position_x), int(position_y)))
    if clicked:
        screen.fill((0, 0, 0))
        bullet_update()
        bullet_draw()
        # check_bullet_boundary()

    """ update()和flip()的区别在于update可以根据选定区域更新部分内容，flip是更新整个待显示的内容，如果update没有传递区域参数，则效果和flip一样 """
    # 刷新页面显示(实时更新游戏页面显示内容)
    # pygame.display.update()
    # 刷新页面显示(实时更新游戏页面显示内容)
    pygame.display.flip()
    clock.tick(60)

import pygame
import sys
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SRCALPHA)
window_size = screen.get_size()
pygame.display.set_caption("植物大战僵尸")

# 游戏背景
background = pygame.image.load("./images/grassland.png").convert()
# 缩放背景图片以适应窗口大小
scaled_background = pygame.transform.scale(background, window_size)

# 设置线条透明度
alpha_value = 50  # 0为完全透明，255为完全不透明
# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)


class GridCell:
    """ 格子类 """

    def __init__(self):
        self.plant = None
        self.position = None


# 格子大小
cell_size = HEIGHT // 5

# 创建格子的行列数
grid_row_count = HEIGHT // cell_size
grid_column_count = 10
grid = [[GridCell() for _ in range(grid_row_count)] for _ in range(grid_column_count)]


class Plants(pygame.sprite.Sprite):
    """ 植物类 """

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        # self.image.fill((0, 255, 0))  # 绿色
        self.rect = self.image.get_rect(center=pos)
        self.last_shot = pygame.time.get_ticks()
        self.shoot_delay = 1500  # 子弹发射间隔（毫秒）
        # self.base_damage = 20  # 初始伤害
        self.damage = self.get_damage()

    def get_damage(self):
        if isinstance(self, SunFlowers):
            return 20
        else:
            return 100

    def update(self):
        """
        循环发射子弹
        :return:
        """
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet(self.rect.center, self.damage)
            all_plants_sprites.add(bullet)  # 将循环生成的子弹添加到植物精灵组中是为了将与植物相关的子弹循环生成，实现循环发射的效果
            bullets.add(bullet)  # 这里将子弹加入子弹精灵组中是为了在子弹精灵组中专门处理子弹的移动、碰撞等逻辑

        ''' 因为在Plants的循环发射子弹中，每新增一颗子弹，都会在植物精灵组中也添加一个子弹精灵，
                如果数据过大占用过多内存影响性能，所以当子弹超出边界，将其从精灵组中删除 '''
        for _sprite in all_plants_sprites:
            if _sprite.rect.right >= WIDTH:
                _sprite.kill()

        self._be_devoured()

    def _be_devoured(self):
        """
        植物是否被僵尸吃掉
        :return:
        """
        for _sprite in all_plants_sprites:
            for _zombie in all_zombie_sprites:
                if pygame.sprite.collide_rect(_sprite, _zombie):
                    _sprite.kill()

                    # 获取被僵尸吃掉的当前植物的位置
                    pos_x, pos_y = _sprite.rect[0] // cell_size, _sprite.rect[1] // cell_size
                    self.replant_plant(pos_x, pos_y)
                    # _zombie._take_damage(_sprite.damage)

    @staticmethod  # 将此方法定义为staticmethod静态方法，因为此方法中并不需要使用类变量和实例变量，
    def replant_plant(pos_x, pos_y):
        """ 当格子中的植物被僵尸吃掉时，允许重新种植 """
        grid[pos_x][pos_y].plant = None


class SunFlowers(Plants):
    """ 向日葵类 """

    def __init__(self, pos):
        super().__init__(pos)
        self.image = pygame.image.load('./images/sunflower.png').convert_alpha()
        # 切分长图像成单独的帧
        self.frames = []
        # 定义每个小图的宽度和高度
        self.frame_width = 82
        self.frame_height = 77
        # 动态效果参数
        self.image_timer = 0  # 控制时间的初始值
        self.image_delay = 10  # 图像切换延迟
        self.current_frame = 0  # 当前图片
        self.base_damage = 20  # 初始伤害

    # 图片的切割处理
    def deal_image(self):
        for image_width in range(0, self.image.get_width(), self.frame_width):
            for image_height in range(0, self.image.get_height(), self.frame_height):
                if self.image.get_width() - image_width < self.frame_width:  # 这个if语句用于判断原图的最后一个位置是否满足切割大小
                    break
                sub = self.image.subsurface(pygame.Rect(image_width, image_height, self.frame_width, self.frame_height))
                self.frames.append(sub)

    # 轮播图片
    def dynamic_effect(self):
        # 设置动态效果的时间频率
        self.image_timer += 1
        if self.image_timer >= self.image_delay:
            self.current_frame = (self.current_frame + 1) % len(self.frames)  # 无限轮播(如果第一遍轮播到最后一张图片，则继续从第一张开始轮播)
            self.image_timer = 0

        # 获取当前帧的小图
        self.image = self.frames[self.current_frame]

        # 在屏幕上绘制当前帧的小图
        screen.blit(self.image, self.rect)

    def update(self):
        # 这个for循环用于展示向日葵的动态效果
        for sprite in all_plants_sprites:
            if isinstance(sprite, SunFlowers):
                sprite.dynamic_effect()


class Peashooter(Plants):
    """ 豌豆射手类 """

    def __init__(self, pos):
        super().__init__(pos)
        self.image = pygame.image.load('./images/Peashooter.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.base_damage = 100  # 初始伤害


class Bullet(pygame.sprite.Sprite):
    """ 子弹类 """

    def __init__(self, pos, damage):
        super().__init__()
        # self.image = pygame.Surface((20, 20), pygame.SRCALPHA)  # 创建带有Alpha通道的表面对象
        # pygame.draw.circle(self.image, (255, 123, 0), (10, 10), 10)  # 绘制红色圆形子弹
        self.image = pygame.image.load("./images/peabullet.png").convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.speed = 1
        self.bullet_damage = damage

    # 子弹移动及是否超出范围
    def update(self):
        self.rect.x += self.speed
        if self.rect.right < 0:
            self.kill()


class Zombies(pygame.sprite.Sprite):
    """ 僵尸类 """

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('./images/zombie.png').convert_alpha()  # 僵尸
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(center=pos)
        self.speed = 1
        self.blood_volume = 100

    # 僵尸移动
    def update(self):
        self.rect.x -= self.speed
        if self.rect.left < 0:
            self.kill()

        self.is_attack()

    # 检测僵尸是否被攻击
    def is_attack(self):
        for _bullet in bullets:
            for _zombie in all_zombie_sprites:
                if pygame.sprite.collide_rect(_bullet, _zombie):
                    _bullet.kill()
                    # 因为在主循环中点击鼠标时，初始化了plant对象，属于全局可见，所以可以直接访问此属性plant.base_damage
                    self._take_damage(_bullet.bullet_damage)

    # 根据血量进行处理
    def _take_damage(self, damage):
        self.blood_volume -= damage
        if self.blood_volume <= 0:
            self.kill()


def draw_lines():
    """ 此函数用于给所有方格之间加上分割线 """
    for grid_x in range(0, WIDTH, cell_size):
        pygame.draw.line(screen, GREEN, (grid_x, 0), (grid_x, HEIGHT))  # 绘制垂直分割线
    for grid_y in range(0, HEIGHT, cell_size):
        pygame.draw.line(screen, GREEN, (0, grid_y), (WIDTH, grid_y))  # 绘制水平分割线


def call_all_sprites_update_method():
    """ 此函数用于调用所有精灵组的update方法 """
    all_plants_sprites.update()  # 将精灵组中的所有精灵对象的状态和属性及时更新
    all_zombie_sprites.update()  # 将精灵组中的所有精灵对象的状态和属性及时更新
    bullets.update()  # 将精灵组中的所有精灵对象的状态和属性及时更新


def call_all_sprites_draw_method():
    """ 此函数用于调用所有精灵组的draw方法 """
    all_plants_sprites.draw(screen)  # 将所有精灵组中的精灵对象绘制到屏幕上
    all_zombie_sprites.draw(screen)  # 将所有精灵组中的精灵对象绘制到屏幕上
    bullets.draw(screen)


all_plants_sprites = pygame.sprite.Group()  # 所有植物类精灵
all_zombie_sprites = pygame.sprite.Group()  # 所有僵尸类精灵
bullets = pygame.sprite.Group()  # 所有植物类子弹精灵

clock = pygame.time.Clock()
running = True


while running:
    clock.tick(60)
    # break
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN:
            x, y = event.pos
            cell_x = x // cell_size
            cell_y = y // cell_size
            if event.button == 1:
                if 0 <= cell_x < grid_column_count and 0 <= cell_y < grid_row_count:
                    if grid[cell_x][cell_y].plant is None:  # 检查格子是否为空
                        # 计算植物位置为当前格子的中心位置
                        plant_pos = ((cell_x * cell_size) + cell_size // 2, (cell_y * cell_size) + cell_size // 2)
                        new_plant = SunFlowers(plant_pos)
                        grid[cell_x][cell_y].plant = new_plant
                        all_plants_sprites.add(new_plant)
                        new_plant.deal_image()
                        new_plant.dynamic_effect()
            elif event.button == 3:
                if 0 <= cell_x < grid_column_count and 0 <= cell_y < grid_row_count:
                    if grid[cell_x][cell_y].plant is None:  # 检查格子是否为空
                        # 植物是否种植在格子中心
                        plant_pos = ((cell_x * cell_size) + cell_size // 2, (cell_y * cell_size) + cell_size // 2)
                        new_plant = Peashooter(plant_pos)
                        grid[cell_x][cell_y].plant = new_plant
                        all_plants_sprites.add(new_plant)
            else:
                zombie = Zombies(event.pos)
                all_zombie_sprites.add(zombie)

    screen.fill(BLACK)

    # 绘制分割线
    draw_lines()

    # 调用所有精灵组的update方法进行更新
    call_all_sprites_update_method()
    # 调用所有精灵组的draw方法
    call_all_sprites_draw_method()

    # screen.blit(scaled_background, (0, 0))

    pygame.display.flip()

pygame.quit()
sys.exit()

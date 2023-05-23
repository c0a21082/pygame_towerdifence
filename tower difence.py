import random
import sys
import time
import math

import pygame as pg
from pygame.sprite import AbstractGroup

WIDTH = 1600  # ゲームウィンドウの幅
HEIGHT = 900  # ゲームウィンドウの高さ




class PlTower(pg.sprite.Sprite):
    """
    左のタワー　に関するクラス
    """

    def __init__(self, xy: tuple[int, int]):
        """
        タワー画像Surfaceを生成する
        引数 xy：タワー画像の位置座標タプル
        """
        super().__init__()
        img0 = pg.transform.rotozoom(pg.image.load(f"ex05/fig/tower.png"), 0, 0.5)  # 左向き，2倍
        img1 = pg.transform.flip(img0, True, False)  # 右向き，2倍
        self.image = img1   # デフォルトで右      
        self.rect = self.image.get_rect()
        self.rect.center = xy

    def update(self,screen:pg.Surface):
        screen.blit(self.image, self.rect)

class EnemyTower(pg.sprite.Sprite):
    """
    右のタワー　に関するクラス
    """

    def __init__(self):
        """
        タワー画像Surfaceを生成する
        引数 xy：タワー画像の位置座標タプル
        """
        super().__init__()
        img0 = pg.transform.rotozoom(pg.image.load(f"ex05/fig/shiro.png"), 0, 0.5)  # 左向き，2倍
        self.image = img0      
        self.rect = self.image.get_rect()
        self.rect.center = (1500,400)

    def update(self,screen:pg.Surface):
        screen.blit(self.image, self.rect)

class Unit0(pg.sprite.Sprite):
    """
    タワーから償還する基礎ユニットのクラス
    """
    def __init__(self, tower:PlTower):
        """
        ユニット画像を生成する
        """
        super().__init__()
        self.image = pg.transform.rotozoom(pg.image.load(f"ex05/fig/alien1.png"), 0, 0.5) 
        self.rect = self.image.get_rect()
        self.rect.centery = tower.rect.centery
        self.rect.centerx = tower.rect.centerx
        self.vx = 1
        self.vy = 0
        self.speed = 1

    def update(self):
        """
        unitを速度ベクトルself._vx, self._vyに基づき移動させる
        """
        self.rect.move_ip(+self.speed*self.vx, +self.speed*self.vy)

class UnitEnemy(pg.sprite.Sprite):
    """
    タワーから償還する基礎ユニットのクラス
    """
    def __init__(self, tower:EnemyTower):
        """
        ユニット画像を生成する
        """
        super().__init__()
        self.image = pg.transform.rotozoom(pg.image.load(f"ex05/fig/alien2.png"), 0, 0.5) 
        self.rect = self.image.get_rect()
        self.rect.centery = tower.rect.centery
        self.rect.centerx = tower.rect.centerx
        self.vx = -1
        self.vy = 0
        self.speed = 1

    def update(self):
        """
        unitを速度ベクトルself._vx, self._vyに基づき移動させる
        """
        self.rect.move_ip(+self.speed*self.vx, +self.speed*self.vy)

class Explosion(pg.sprite.Sprite):
    """
    爆発に関するクラス
    """
    def __init__(self, obj: "EnemyTower|UnitEnemy", life: int):
        """
        爆弾が爆発するエフェクトを生成する
        引数1 obj：爆発するBombまたは敵機インスタンス
        引数2 life：爆発時間
        """
        super().__init__()
        img = pg.image.load("ex04/fig/explosion.gif")
        self.imgs = [img, pg.transform.flip(img, 1, 1)]
        self.image = self.imgs[0]
        self.rect = self.image.get_rect(center=obj.rect.center)
        self.life = life

    def update(self):
        """
        爆発時間を1減算した爆発経過時間_lifeに応じて爆発画像を切り替えることで
        爆発エフェクトを表現する
        """
        self.life -= 1
        self.image = self.imgs[self.life//10%2]
        if self.life < 0:
            self.kill()


def main():
    pg.display.set_caption("towerdifence")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex05/fig/pg_bg.jpg")
    font = pg.font.Font("ex05/fig/JKG-L_3.ttf", 300)

    pl_tower = PlTower((100, 400))
    emy_tower = EnemyTower()
    tmr = 0
    units = pg.sprite.Group()
    unitsemys = pg.sprite.Group()
    gbb = pg.sprite.Group()
    exps = pg.sprite.Group()
    emy_towerHP = 20


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                units.add(Unit0(pl_tower))
            
            if tmr%20 == 0:  # 200フレームに1回，敵機を出現させる
                unitsemys.add(UnitEnemy(emy_tower))
        
        if len(pg.sprite.spritecollide(emy_tower, units, True)) != 0:
            exps.add(Explosion(emy_tower,50))
            emy_towerHP-=1
            if emy_towerHP == 0:
                screen.blit(font.render("君の勝ち！", True, (255,0,0)),[400,400])
                pg.display.update()
                time.sleep(3)
                return

        for unitsemy in pg.sprite.groupcollide(unitsemys, units, True, True).keys():
            exps.add(Explosion(unitsemy,10))
           
        

        screen.blit(bg_img, [0, 0])
        tmr += 1
        gbb.update(pl_tower)
        gbb.draw(screen)
        pl_tower.update(screen)
        emy_tower.update(screen)
        units.update()
        units.draw(screen)
        unitsemys.update()
        unitsemys.draw(screen)
        exps.update()
        exps.draw(screen)
        pg.display.update()
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()

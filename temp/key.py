#*_*coding:utf-8*_*
import pygame as py
from pygame.locals import *
from sys import exit


class key(object):
    def __init__(self):
        pass
    def init(self):
        info = []
        py.init() #加载硬件
        py.display.list_modes()
        se = py.display.set_mode((640,480),0,32)#设置窗口分辨率
        py.display.set_caption('这是一个window')#窗口标题
        im =py.image.load('sushiplate.jpg').convert() #加载背景图像
        se.blit(im,(0,0)) #将背景图像画到屏幕上
        py.display.update() #更新屏幕


if __name__=='__main__':
    while True:
        se =key().init()
        for event in py.event.get():
                if event.type == QUIT:
                    exit()


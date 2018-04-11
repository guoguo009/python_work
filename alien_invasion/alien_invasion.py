
import sys
import pygame
from alien_settings import Settings 
from ship import Ship
import game_functions as gf

def run_game():
	#初始化游戏并创建一个屏幕对象
	#初始化pygame、设置和屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	#screen = pygame.display.set_mode((1200, 600))
	pygame.display.set_caption("Alien Invasion")
	#注意这里颜色用的是[]
	bg_color = [230, 230, 230]
	#ship = Ship(screen)
	ship = Ship(ai_settings, screen)
	#开始游戏的主循环
	while True:
		
		#监视键盘和鼠标事件
		gf.check_events(ship)
		ship.update()
		gf.update_screen(ai_settings, screen, ship)
		#for event in pygame.event.get():
			#if event.type == pygame.QUIT:
				#sys.exit()
		#每次循环都重绘屏幕
		#必须把设置颜色的放在循环内部
		#screen.fill(ai_settings.bg_color)
		#screen.fill([230, 230, 230])
		#ship.blitme()
		#让最近绘制的屏幕可见
	pygame.display.flip()
run_game()

import pygame
import sys
import random
import pygame_menu
import time
pygame.init()

def main():
	# Цвета (R, G, B)
	BLACK = (0, 0, 0)
	WHITE = (255, 255, 255)
	RED = (255, 0, 0)
	GREEN = (0, 255, 0)
	BLUE = (0, 0, 255)

	SIZE_BLOCK = 20
	FRAME_COLOR = (60, 179, 113)  
	WHITE = (255, 255, 255)
	GREEN = (143, 188, 143)
	HEADER_COLOR = (46, 139, 87)
	SNAKE_COLOR = (255, 69, 0)
	COUNT_BLOCKS = 30
	HEADER_MARGIN = 70
	MARGIN = 1
	size = [SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCKS,
			SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCKS + HEADER_MARGIN]
	

	font = pygame.font.SysFont('courier', 36, True)

	timer = pygame.time.Clock()

	screen = pygame.display.set_mode(size)
	pygame.display.set_caption('Snake')

	# bg_image = pygame.image.load("img_2.png")
	
	class SnakeBlock:
		def __init__(self, x, y):
			self.x = x
			self.y = y

		def is_inside(self):
			return 0 <= self.x < COUNT_BLOCKS and 0 <= self.y < COUNT_BLOCKS

		# сравнение экземпляров класса
		def __eq__(self, other):
			return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y 


	def draw_block(color, raw, column):
		pygame.draw.rect(screen, color, [SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column + 1),
										 HEADER_MARGIN + SIZE_BLOCK + raw * SIZE_BLOCK + MARGIN * (raw + 1),
										 SIZE_BLOCK,
										 SIZE_BLOCK])


	def start_the_game():
		snake_blocks = [SnakeBlock(6,8), SnakeBlock(6,9)] # создаются объекты класса SnakeBlock и помещаются в кортеж
		apple = SnakeBlock(random.randint(0, COUNT_BLOCKS-1), random.randint(0, COUNT_BLOCKS-1))
		d_col = buf_col = 1
		d_raw = buf_raw = 0
		score = 0
		speed = 1

		while True:
			# получаем все события
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP and d_col!=0:
						buf_raw = -1
						buf_col = 0
					elif event.key == pygame.K_DOWN and d_col!=0:
						buf_raw = 1
						buf_col = 0
					elif event.key == pygame.K_LEFT and d_raw!=0:
						buf_raw = 0
						buf_col = -1
					elif event.key == pygame.K_RIGHT and d_raw!=0:
						buf_raw = 0
						buf_col = 1


			screen.fill(FRAME_COLOR)

			pygame.draw.rect(screen, HEADER_COLOR, [0, 0, size[0], HEADER_MARGIN])

			text_score = font.render(f"Your score: {score}", 2, WHITE)
			text_speed = font.render(f"Speed: {speed}", 2, WHITE)

			screen.blit(text_score, (SIZE_BLOCK, SIZE_BLOCK))
			screen.blit(text_speed, (SIZE_BLOCK + 400, SIZE_BLOCK))

			for raw in range(COUNT_BLOCKS):
				for column in range(COUNT_BLOCKS):
					if (raw + column) % 2 == 0:
						color = GREEN
					else:
						color = WHITE
					
					draw_block(color, raw, column)
			
			
			head = snake_blocks[-1]

			if not head.is_inside():
				break

			draw_block(RED, apple.x, apple.y)

			for block in snake_blocks:
				draw_block(BLUE, block.x, block.y)

			pygame.display.flip()  # применение всех изменений в графике

			if apple == head:
				snake_blocks.insert(0, apple)
				apple = SnakeBlock(random.randint(0, COUNT_BLOCKS-1), random.randint(0, COUNT_BLOCKS-1))
				score += 1
				speed = score // 5 + 1 
				
			d_col = buf_col
			d_raw = buf_raw
			head_2 = SnakeBlock(head.x + d_raw, head.y + d_col)

			if head_2 in snake_blocks:
				break

			snake_blocks.append(head_2)
			snake_blocks.pop(0)

			timer.tick(3 + speed)

	menu = pygame_menu.Menu(300, 500, 'Добро пожаловать!',
                       theme=pygame_menu.themes.THEME_BLUE)

	menu.add_text_input('Имя :', default='Игрок')
	menu.add_button('Играть', start_the_game)
	menu.add_button('Выйти', pygame_menu.events.EXIT)

	while True:

		# screen.blit(bg_image, (0, 0))

		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				exit()

		if menu.is_enabled():
			menu.update(events)
			menu.draw(screen)

		pygame.display.update()
		
if __name__ == '__main__':
	main()



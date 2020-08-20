import pygame
import sys
import random
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

	font = pygame.font.SysFont('courier', 36)

	
	class SnakeBlock:
		def __init__(self, x, y):
			self.x = x
			self.y = y

		def is_inside(self):
			return 0 <= self.x < COUNT_BLOCKS and 0 <= self.y < COUNT_BLOCKS

		# сравнение экземпляров класса
		def __eq__(self, other):
			return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y 

	screen = pygame.display.set_mode(size)
	pygame.display.set_caption('Snake')

	timer = pygame.time.Clock()

	def draw_block(color, raw, column):
		pygame.draw.rect(screen, color, [SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column + 1),
										 HEADER_MARGIN + SIZE_BLOCK + raw * SIZE_BLOCK + MARGIN * (raw + 1),
										 SIZE_BLOCK,
										 SIZE_BLOCK])
	
	snake_blocks = [SnakeBlock(10,10)] # создаются объекты класса SnakeBlock и помещаются в кортеж
	apple = SnakeBlock(random.randint(0, COUNT_BLOCKS-1), random.randint(0, COUNT_BLOCKS-1))
	d_col = 1
	d_raw = 0
	score = 0
	speed = 1

	while True:
		# получаем все события
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP and d_col!=0:
					d_raw = -1
					d_col = 0
				elif event.key == pygame.K_DOWN and d_col!=0:
					d_raw = 1
					d_col = 0
				elif event.key == pygame.K_LEFT and d_raw!=0:
					d_raw = 0
					d_col = -1
				elif event.key == pygame.K_RIGHT and d_raw!=0:
					d_raw = 0
					d_col = 1


		screen.fill(FRAME_COLOR)

		pygame.draw.rect(screen, HEADER_COLOR, [0, 0, size[0], HEADER_MARGIN])

		text_score = font.render(f"Your score: {score}", 0, WHITE)
		text_speed = font.render(f"Speed: {speed}", 0, WHITE)

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
			sys.exit()

		draw_block(RED, apple.x, apple.y)

		for block in snake_blocks:
			draw_block(BLUE, block.x, block.y)

		if apple == head:
			snake_blocks.insert(0, apple)
			apple = SnakeBlock(random.randint(0, COUNT_BLOCKS-1), random.randint(0, COUNT_BLOCKS-1))
			score += 1
			speed = score // 5 + 1 
			
			
		head_2 = SnakeBlock(head.x + d_raw, head.y + d_col)
		snake_blocks.append(head_2)
		snake_blocks.pop(0)

		
		pygame.display.flip()  # применение всех изменений в графике
		timer.tick(3 + speed)


if __name__ == '__main__':
	main()



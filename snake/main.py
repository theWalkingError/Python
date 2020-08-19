import pygame
import sys

def main():
	SIZE_BLOCK = 20
	FRAME_COLOR = (60, 179, 113)  # цвет заливки поля
	WHITE = (255, 255, 255)
	GREEN = (143, 188, 143)
	HEADER_COLOR = (46, 139, 87)
	SNAKE_COLOR = (205, 92, 92)
	COUNT_BLOCKS = 30
	HEADER_MARGIN = 70
	MARGIN = 1
	size = [SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCKS,
			SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCKS + HEADER_MARGIN]

	
	class SnakeBlock:
		def __init__(self, x, y):
			self.x = x
			self.y = y

		def is_inside(self):
			return 0 <= self.x < COUNT_BLOCKS and 0 <= self.y < COUNT_BLOCKS

	snake_blocks = [SnakeBlock(10,10), SnakeBlock(10, 11)] # создаются объекты класса SnakeBlock и помещаются в кортеж


	screen = pygame.display.set_mode(size)
	pygame.display.set_caption('Snake')

	timer = pygame.time.Clock()

	def draw_block(color, raw, column):
		pygame.draw.rect(screen, color, [SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column + 1),
										 HEADER_MARGIN + SIZE_BLOCK + raw * SIZE_BLOCK + MARGIN * (raw + 1),
										 SIZE_BLOCK,
										 SIZE_BLOCK])

	d_col = 1
	d_raw = 0

	while True:
		# получаем все события
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					d_raw = -1
					d_col = 0
				elif event.key == pygame.K_DOWN:
					d_raw = 1
					d_col = 0
				elif event.key == pygame.K_LEFT:
					d_raw = 0
					d_col = -1
				elif event.key == pygame.K_RIGHT:
					d_raw = 0
					d_col = 1


		screen.fill(FRAME_COLOR)
		pygame.draw.rect(screen, HEADER_COLOR, [0, 0, size[0], HEADER_MARGIN])

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

		for block in snake_blocks:
			draw_block(SNAKE_COLOR, block.x, block.y)
			
		head_2 = SnakeBlock(head.x + d_raw, head.y + d_col)
		snake_blocks.append(head_2)
		snake_blocks.pop(0)


		pygame.display.flip()  # применение всех изменений в графике
		timer.tick(8)


if __name__ == '__main__':
	main()



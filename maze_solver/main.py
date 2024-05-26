# with open('./input.txt', 'r') as f:
#   input = f.read()

# print(input)

from operator import methodcaller, truth
from enum import Enum

class i2():
	MOVE_DIAGONAL_COST	= 14
	MOVE_STRAIGHT_COST	= 10
	__slots__			= ('x', 'y')
	
	def __init__(self, x: int, y: int) -> None:
		self.x = x
		self.y = y
	
	def distance_from(self, other: 'i2') -> int:
		x_distance = abs(self.x - other.x)
		y_distance = abs(self.y - other.y)
		remaining = abs(x_distance - y_distance)

		return self.MOVE_DIAGONAL_COST * min(x_distance, y_distance) + self.MOVE_STRAIGHT_COST * remaining

	def __hash__(self) -> int:
		return hash((self.x, self.y))
	
	def __repr__(self) -> str:
		return f'({self.x}, {self.y})'
	
	def __eq__(self, value: object) -> bool:
		return hash(self) == hash(value)
	
	def __add__(self, other: 'i2') -> 'i2':
		return i2(self.x + other.x, self.y + other.y)

class Direction(Enum):
	LEFT		= i2(-1,  0)
	DOWN		= i2( 0,  1)
	UP			= i2( 0, -1)
	RIGHT		= i2( 1,  0)

class TileType(Enum):
	START		= 'S'
	GOAL		= 'G'
	PATH		= '.'
	OBSTACKLE	= '#'

class MazeTile():
	__slots__ = (
		'type',
		'position',
		'maze',
		'traversable',
		'g_cost',
	)

	def __init__(self, type: TileType, position: i2, maze: 'Maze') -> None:
		self.type			= type
		self.position		= position
		self.maze			= maze
		self.traversable	= type != TileType.OBSTACKLE
		self.g_cost			= 0
	
	@property
	def h_cost(self) -> int:
		return self.position.distance_from(self.maze.end.position)

	@property
	def f_cost(self) -> int:
		return self.g_cost + self.h_cost
	

	def get_neighbors(self) -> list[tuple[Direction, 'MazeTile']]:
		neighbors: list[tuple[Direction, 'MazeTile']] = []

		for direction in Direction:
			try:
				neighbors.append((direction, self.maze[self.position + direction.value]))
			except IndexError: continue
		
		return neighbors

class Maze():
	__slots__ = ('tiles', 'start', 'end')

	def __init__(self, raw_data: list[str]) -> None:
		self.tiles = [[self._register_tile(TileType(cell), i2(x,y)) for x, cell in enumerate(row)] for y, row in enumerate(raw_data)]
	
	def solve_a_star(self) -> list[Direction]:
		search_queue = [self.start]
		searched: set[MazeTile] = set()
		connections: dict[MazeTile, tuple[Direction, MazeTile]] = dict()

		path: list[Direction] = []

		while search_queue:
			current = search_queue[0]
			
			for tile in search_queue:
				if tile.f_cost < current.f_cost or tile.f_cost == current.f_cost and tile.h_cost < current.h_cost:
					current = tile
			
			if current == self.end:
				tile = self.end

				while tile != self.start:
					direction, tile = connections[tile]
					path.append(direction)
				
				break

			search_queue.remove(current)
			searched.add(current)

			for direction, neighbor in filter(lambda x: x[1].traversable and not x[1] in searched, current.get_neighbors()):
				qeued_for_search = neighbor in search_queue
				cost_to_neighbor = neighbor.g_cost + current.position.distance_from(neighbor.position)

				if not qeued_for_search or cost_to_neighbor < neighbor.g_cost:
					neighbor.g_cost = cost_to_neighbor
					connections[neighbor] = (direction, current)

					if not qeued_for_search:
						# neighbor.h_cost = neighbor.position.distance_from(end.position)
						search_queue.append(neighbor)
		
		path.reverse()
		return path
	
	def _register_tile(self, type: TileType, position: i2) -> MazeTile:
		tile = MazeTile(type, position, self)

		match type:
			case TileType.GOAL:
				self.end = tile
			case TileType.START:
				self.start = tile

		return tile

	def __getitem__(self, idx: i2) -> MazeTile:
		return self.tiles[idx.y][idx.x]
	
	def __str__(self) -> str:
		return '\n'.join(' '.join(tile.type.value for tile in row) for row in self.tiles)
	


def main() -> None:
	raw_maps: dict[str, list[str]] = dict()
	current_map = ''

	with open('input.txt', 'r', encoding='utf8') as file:

		for line in filter(truth, map(methodcaller('replace', ' ', ''), map(str.strip, file))):
			if len(line) == 1:
				raw_maps[line] = []
				current_map = line
				continue

			raw_maps[current_map].append(line)

	maps = dict((k, Maze(v)) for k,v in raw_maps.items())

	for k,v in maps.items():
		# print(k, v, sep='\n')
		print(k, f'S {" ".join(direction.name[0] for direction in v.solve_a_star())} G', sep='\n', end='\n\n')

if __name__ == '__main__':
	main()
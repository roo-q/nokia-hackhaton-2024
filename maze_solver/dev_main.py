from operator import methodcaller, truth
from functools import singledispatchmethod
from typing import Optional, Self
from tkinter import Tk, ttk, Frame, NSEW, Button, Label
from enum import Enum

MOVE_STRAIGHT_COST = 10
MOVE_DIAGONAL_COST = 14

class i2():
	__slots__ = ('x', 'y')

	def __init__(self, x: int, y: int) -> None:
		self.x = x
		self.y = y
	
	def __hash__(self) -> int:
		return hash((self.x, self.y))
	
	def __repr__(self) -> str:
		return f'({self.x}, {self.y})'
	
	def __add__(self, other: Self | tuple[int, int]) -> 'i2':
		try:
			return i2(self.x + other.x, self.y + other.y)
		except AttributeError:
			return i2(self.x + other[0], self.y + other[1])
		
	def __sub__(self, other: Self | tuple[int, int]) -> 'i2':
		try:
			return i2(self.x - other.x, self.y - other.y)
		except AttributeError:
			return i2(self.x - other[0], self.y - other[1])
	
	def __eq__(self, other: object) -> bool:
		return hash(self) == hash(other)
	
	def distance_from(self, other: Self) -> int:
		x_distance = abs(self.x - other.x)
		y_distance = abs(self.y - other.y)
		remaining = abs(x_distance - y_distance)

		return MOVE_DIAGONAL_COST * min(x_distance, y_distance) + MOVE_STRAIGHT_COST * remaining

class Direction(Enum):
	LEFT	=i2(-1, 0)
	DOWN	=i2( 0,-1)
	UP		=i2( 0, 1)
	RIGHT	=i2( 1, 0)

class TileType(Enum):
	OBSTACLE = 0
	PATH = 1
	START = 2
	GOAL = 3

class GridTile():
	def __init__(self, position: i2, cell: str) -> None:
		self.position = position
		self.traversable = cell != '#'
		self.g_cost = 0 # distance from start
		self.h_cost = 0 # distance from end

		match cell:
			case '#': self.type = TileType.OBSTACLE
			case '.': self.type = TileType.PATH
			case 'S': self.type = TileType.START
			case goal: self.type = TileType.GOAL
		
	def __repr__(self) -> str:
		return str(self.position)
	
	@property
	def f_cost(self) -> int:
		return self.g_cost + self.h_cost

def index_2d_on_1d[T](list: list[T], idx: i2, width: int) -> Optional[T]:
	try:
		return list[idx.x + idx.y * width]
	except IndexError: return None

def flatten_2d[T](list: list[list[T]]) -> list[T]:
	return [cell for row in list for cell in row]

def a_star(tiles: list[list[GridTile]], start: GridTile, end: GridTile):
	for tile in flatten_2d(tiles):
		tile.h_cost = tile.position.distance_from(end.position)

	search_queue = [start]
	searched: set[GridTile] = set()

	connections: dict[GridTile, tuple[Direction, GridTile]] = dict()

	while search_queue:
		current = search_queue[0]

		for tile in search_queue:
			if tile.f_cost < current.f_cost or tile.f_cost == current.f_cost and tile.h_cost < current.h_cost:
				current = tile
		
		if current == end:
			tile = end
			ret = []

			while tile != start:
				# ret.append(tile)
				dir, tile = connections[tile]
				ret.append(dir)
			return ret
			# current_direction, current_tile = connections[end]
			# path: list[Direction] = []

			# while current_tile != start:
			# 	path.append(current_direction)
			# 	current_direction, current_tile = connections[current_tile]
			
			# return path
		
		search_queue.remove(current)
		searched.add(current)

		for direction in Direction:
			position = direction.value + current.position

			try:
				neighbor = tiles[position.y][position.x]

				if neighbor in searched:
					continue

				if not neighbor.traversable:
					continue

				qeued_for_search = neighbor in search_queue
				cost_to_neighbor = neighbor.g_cost + current.position.distance_from(neighbor.position)

				if not qeued_for_search or cost_to_neighbor < neighbor.g_cost:
					neighbor.g_cost = cost_to_neighbor
					connections[neighbor] = (direction, current)

					if not qeued_for_search:
						neighbor.h_cost = neighbor.position.distance_from(end.position)
						search_queue.append(neighbor)
			except IndexError:
				continue

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

	for k,v in raw_maps.items():
		print(k, *v, sep='\n')
		break
	
	raw_map = raw_maps['A']
	# map_data = [GridTile(i2(x,y), cell) for y, row in enumerate(raw_map) for x, cell in enumerate(row)]
	# start = next(tile for tile in map_data if tile.type == TileType.START)
	# end = next(tile for tile in map_data if tile.type == TileType.GOAL)
	map_data = [[GridTile(i2(x,y), cell) for x, cell in enumerate(row)] for y, row in enumerate(raw_map)]
	start = next(cell for row in map_data for cell in row if cell.type == TileType.START)
	end = next(cell for row in map_data for cell in row if cell.type == TileType.GOAL)
	path: reversed[GridTile] = reversed(a_star(map_data, start, end))

	path = [Direction.UP if dir == Direction.DOWN else Direction.DOWN if dir == Direction.UP else dir for dir in path]

	print(f'S {" ".join([dir.name[0] for dir in path])} G')
	# previous_position = start.position
	# for tile in path:
	# 	print(previous_position)
	# 	# previous_position += tile.position
	# 	print(f'{tile.position}-{previous_position} = {tile.position-previous_position}')
	# 	previous_position = tile.position - previous_position


#A
# # # # # # #
# S . . . . #
# # . # # . #
# . . # . . #
# . . . # # #
# . # G . . #
# # # # # # #

#S R D D D R D G

#######
#S....#
##.##.#
#..#..#
#...###
#.#G..#
#######

if __name__ == '__main__':
	main()
# with open('./input.txt', 'r') as f:
#   input = f.read()

# print(input)

HEADERS = {
	'matrices',
	'operations'
}

class Matrix():
	def __init__(self, data: list[list[int]]) -> None:
		self.rows = data
		self.columns = [[row[cell] for row in data] for cell in range(len(data[0]))]
		self.size = (len(self.rows), len(self.columns))
	
	def __add__(self, other: 'Matrix') -> 'Matrix':
		assert self.size == other.size, 'incompatible matrix sizes'

		return Matrix([
			[
				self.rows[ridx][cidx] + other.rows[ridx][cidx]
				for cidx in range(self.size[1])
			]
			for ridx in range(self.size[0])
		])
	
	def __mul__(self, other: 'Matrix') -> 'Matrix':
		assert self.size[1] == other.size[0], 'incompatible matrix sizes'
		
		return Matrix([
			[
				sum(x*y for x,y in zip(row, column))
				for column in other.columns
			]
			for row in self.rows
		])
	
	def __str__(self) -> str:
		return '\n'.join([' '.join(map(str, row)) for row in self.rows])

def main() -> None:
	current_header = ''
	current_matrix = ''
	matrices_raw: dict[str, list[list[int]]] = dict()
	operations: list[str] = []

	with open('input.txt', 'r', encoding='utf8') as file:
		for line in map(str.strip, file):
			if line in HEADERS:
				current_header = line
				continue

			if not line:
				continue

			if len(line) == 1: # start of a matrix
				current_matrix = line
				matrices_raw[current_matrix] = []
				continue

			if current_header == 'matrices':
				matrices_raw[current_matrix].append(list(map(int, filter(lambda x: x != '', line.split(' ')))))
			
			if current_header == 'operations':
				operations.append(line)
	
	matrices: dict[str, Matrix] = dict([(k, Matrix(v)) for k,v in matrices_raw.items()])

	for operation in operations:
		print(operation)
		print(eval(operation, matrices))
		print('') # could've just used end='\n\n'


if __name__ == '__main__':
	main()
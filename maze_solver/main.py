# with open('./input.txt', 'r') as f:
#   input = f.read()

# print(input)

from operator import methodcaller, truth

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

if __name__ == '__main__':
	main()
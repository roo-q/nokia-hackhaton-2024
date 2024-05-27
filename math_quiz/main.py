# print('1.:')

def main() -> None:
	print(*[f'{i}.: {ans}' for i, ans in enumerate([100, 512, 12.5, 12, 2, 8, 10, 1849, 9], 1)], sep='\n')
# 	print("""
# 1.: 100
# 2.: 512
# 3.: 12.5
# 4.: 12
# 5.: 2
# 6.: 8
# 7.: 10
# 8.: 1849
# 9.: 9
# """)


if __name__ == '__main__':
	main()
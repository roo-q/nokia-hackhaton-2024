
# with open('./input.txt', 'r') as f:
#   input = f.read()

# print(input)

# char_filter = {ord(c) for c in 'abcdefghijklmnopqrstuvwxyz0123456789'}
char_filter = set('abcdefghijklmnopqrstuvwxyz0123456789')

def process_word(word: str) -> tuple[bool, int]:
    word_as_char_list: list[str] = [c for c in word.lower() if c in char_filter]
    unique_chars = set(word_as_char_list)

    # slightly faster than return word_as_char_list == word_as_char_list[::-1], len(unique_chars)
    word_len = len(word_as_char_list)
    seg_len = word_len//2
    start = word_as_char_list[:seg_len]
    # (word_len ^ 1) == (word_len + 1) slowest
    # word_len & 1 consistently fast
    # word_len % 2 inconsistent
    end = word_as_char_list[seg_len + (1 if word_len & 1 else 0):]
    end.reverse()
    return start == end, len(unique_chars)

def main():
    with open('input.txt', 'r', encoding='utf8') as file:
        print(*[process_word(line) for line in file], sep='\n')

if __name__ == '__main__':
    main()
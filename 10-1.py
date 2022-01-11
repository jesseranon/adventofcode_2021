file = open("day10input.txt")

inp = file.read()
file.close()
inp = inp.split('\n')

test = "[({(<(())[]>[[{[]{<()<>>\n[(()[<>])]({[<{<<[]>>(\n{([(<{}[<>[]}>{[]{[(<()>\n(((({<>}<{<{<>}{[]{[]{}\n[[<[([]))<([[{}[[()]]]\n[{[{({}]{}}([{[{{{}}([]\n{<[[]]>}<{[{[{[]{()[[[]\n[<(<(<(<{}))><([]([]()\n<{([([[(<>()){}]>(<<{{\n<{([{{}}[<[[[<>{}]]]>[]]"
test = test.split('\n')

# test
# [({(<(())[]>[[{[]{<()<>>
# [(()[<>])]({[<{<<[]>>(
# {([(<{}[<>[]}>{[]{[(<()> - Expected ], but found } instead.
# (((({<>}<{<{<>}{[]{[]{}
# [[<[([]))<([[{}[[()]]] - Expected ], but found ) instead.
# [{[{({}]{}}([{[{{{}}([] - Expected ), but found ] instead.
# {<[[]]>}<{[{[{[]{()[[[]
# [<(<(<(<{}))><([]([]() - Expected >, but found ) instead.
# <{([([[(<>()){}]>(<<{{ - Expected ], but found > instead. <{([([>(<<{{
# <{([{{}}[<[[[<>{}]]]>[]] 

chunk_chars = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

# process input

def process_syntax(s): #s is single line of text
    global chunk_chars
    for i in reversed(range(len(s))):
        if s[i] in chunk_chars and i + 1 <= len(s) - 1 and s[i+1] in chunk_chars.values():
            if s[i+1] == chunk_chars[s[i]]:
                s = s[:i] + s[i+2:]
            else:
                return s[i+1]


def solve(list_of_text):
    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    res = 0
    for t in list_of_text:
        try:
            res += points[process_syntax(t)]
        except:
            pass
    return res

print(solve(inp))

# test 26397 - correct
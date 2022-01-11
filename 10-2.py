file = open("day10input.txt")

inp = file.read()
file.close()
inp = inp.split('\n')

test = "[({(<(())[]>[[{[]{<()<>>\n[(()[<>])]({[<{<<[]>>(\n{([(<{}[<>[]}>{[]{[(<()>\n(((({<>}<{<{<>}{[]{[]{}\n[[<[([]))<([[{}[[()]]]\n[{[{({}]{}}([{[{{{}}([]\n{<[[]]>}<{[{[{[]{()[[[]\n[<(<(<(<{}))><([]([]()\n<{([([[(<>()){}]>(<<{{\n<{([{{}}[<[[[<>{}]]]>[]]"
test = test.split('\n')

chunk_chars = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

def process_syntax(syntax): #s is single line of text
    global chunk_chars
    s = syntax
    for i in reversed(range(len(s))):
        if s[i] in chunk_chars and i + 1 <= len(s) - 1 and s[i+1] in chunk_chars.values():
            if s[i+1] == chunk_chars[s[i]]:
                s = s[:i] + s[i+2:]
            else:
                return False
    return s

def solve(list_of_text):
    global chunk_chars
    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    res = []
    for t in list_of_text:
        if process_syntax(t):
            remaining = ''.join(chunk_chars[c] for c in process_syntax(t)[::-1])
            score = 0
            for r in remaining:
                score *= 5
                score += points[r]
            res.append(score)
    res.sort()
    # print(res)
    return res[int((len(res)-1)/2)]

print(solve(inp))

# test 288957 - correct
input_file = 'input.txt'


def main():
    with open(input_file) as f:
        lines = f.readlines()

        prev = int(lines[0])
        inc = 0
        for i in range(1, len(lines)):
            if int(lines[i]) > prev:
                inc = inc + 1

            prev = int(lines[i])

        print(inc)

main()

def main2():
    with open(input_file) as f:
        lines = f.readlines()

        prev = int(lines[0]) + int(lines[1]) + int(lines[2])
        inc = 0
        for i in range(1, len(lines)-2):
            if int(lines[i]) + int(lines[i+1]) + int(lines[i+2]) > prev:
                inc = inc + 1

            prev = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])

        print(inc)

main2()
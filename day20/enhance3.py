import itertools
import numpy as np

enhancer = '#..##..#.#.#.###.#..##.####..##..##.##.#.###.......##..#..#.#.#.#..#...##....#.#.##.###....###.#.##.##..##.#...##.##...#...##......##.#...#.......##.#.#..####.##..#.#.#.....##.....#....#.#.#.##..##..##.##.....###...#.#..###.#######.#.....###....#......#.###.#...#.#####.#.#.###..#...##.##.#..#...######.###.#.##...####..####.###...####........##...##.##.####...##.#.#...##.#####.#....#.....##..#......###..###.#.#..###..#.####......#.....#.#.#.###..#.#..#..#...##..##..#.##....#....#.##..###..#....##.##..#.###..'
image = np.empty([300, 300], dtype=np.dtype('str'))
image.fill('.')

lines = [[char for char in line] for line in [line.rstrip('\n') for line in open("input.txt", "r").readlines()]]

image[100:200, 100:200] = lines


def enhance_image(image):
    old = np.copy(image)
    replace = '.' if image[0, 0] == '#' else '#'
    image[::, 0] = replace
    image[::, -1] = replace
    image[0, ::] = replace
    image[-1, ::] = replace
    to_check = list(itertools.product([-1, 0, 1], [-1, 0, 1]))
    for i in range(1, len(image) - 1):
        for j in range(1, len(image) - 1):
            bin_string = ''
            for check in to_check:
                token = old[i + check[0]][j + check[1]]
                # print(token)
                bin_string += '1' if token == '#' else '0'
            ind = int(bin_string, 2)
            image[i][j] = enhancer[ind]


for i in range(50):
    print(i)
    enhance_image(image)
# print('x')
# enhance_image(image)

total = 0
for i in range(len(image)):
    for j in range(len(image)):
        if image[i, j] == '#':
            total += 1

print(total)
# print(image)
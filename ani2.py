# txt = "numbers.txt"
# output_asu = "ani_20193061_numbers.asu"
txt = "number31.txt"
output_asu = "ani_20193061_number31.asu"

# Read numbers from the input file
num = []
result_lines = []

with open(txt, "r") as file:
    for line in file:
        num.append(int(line.strip()))

cnt = 0

positions = [
    (800, 50), (400, 100), (1200, 100), (250, 150), (650, 150), (1050, 150), (1450, 150),
    (150, 200), (350, 200), (550, 200), (750, 200), (950, 200), (1150, 200), (1350, 200), (1550, 200),
    (100, 300), (200, 300), (300, 300), (400, 300), (500, 300), (600, 300), (700, 300), (800, 300), 
    (900, 300), (1000, 300), (1100, 300), (1200, 300), (1300, 300), (1400, 300), (1500, 300), (1600, 300)
]

def add_line():
    graph = f'graph "Tree" size {len(num)} nodeFontColor black directed nodes {{'
    edges = 'edges {'
    for i, value in enumerate(num):            
        if i < len(positions):
            x, y = positions[i]
            graph += f' "{value}" ({x}, {y}),'
            if cnt == i and cnt != 0:
                draw_circle(x, y)
        if 2 * i + 1 < len(num):
            edges += f' ({i}, {2 * i + 1}),'
        if 2 * i + 2 < len(num):
            edges += f' ({i}, {2 * i + 2}),'
        

    graph = graph.rstrip(',') + '}'
    edges = edges.rstrip(',') + '}'

    result = f'{graph} {edges}\n'
    print(result)
    result_lines.append(result)


def draw_circle(x, y):
    line = f'move "c1" to ({x-12}, {y-12})\n'
    result_lines.append(line)
#루트를 제외한 왼쪽 오른쪽 서브트리는 모드 히프
#현재 시점으로 노드 최대 레벨 순서 번호는 
add_line()
result_lines.append('circle "c1" (810, 60) radius 22 color red\n')
node = 0
for i in range(4):
    v = num[node]
    left = (node * 2) + 1
    right = (node * 2) + 2
    
    if num[left] > num[right] and num[left] > num[node]:
        num[left], num[node] = num[node], num[left]
        node = left
        cnt = left
    elif num[left] < num[right] and num[node] < num[right]:
        num[right], num[node] = num[node], num[right]
        node = right
        cnt = right

    add_line()
    
with open(output_asu, "w") as file:
    file.writelines(result_lines)

print(f"Graph definition written to {output_asu}")

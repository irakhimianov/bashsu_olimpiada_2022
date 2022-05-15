"""
Студент скачал черно-белую картинку размера n x m пикселей. С
тудент хочет изменить цвета картинки как можно меньшего количества пикселей так, чтобы получился QR-код.

Картинка является QR-кодом если выполняются следующие условия:
    - в каждом столбце все пиксели одного цвета;
    - ширина каждой одноцветной вертикальной полосы не менее x и не более y пикселей.

Формат ввода
В первой строке записаны четыре целых числа через пробел
Далее идет n строк, описывающих исходную картинку. В каждой из этих строк содержится ровно m символов.
Символ «.» обозначает белый пиксель, а «#» — черный.
Никаких других символов кроме «.» и «#» в описании картинки не содержится.

Формат вывода
В первой строке выведите наименьшее количество пикселей, которое нужно перекрасить. Гарантируется, что ответ существует.

Пример

Ввод	            Вывод

6 5 1 2             11
##.#.
.###.
###..
#...#
.##.#
###..
"""
n, m, x, y = list(map(int, input().split()))
pic_bitmap = [input() for _ in range(n)]

pic_bitmap = [i.replace("#", "1") for i in pic_bitmap]
pic_bitmap = [i.replace(".", "0") for i in pic_bitmap]
black_pixels = [sum(list(map(int, i))) for i in list(zip(*pic_bitmap))]
black_pixels.insert(0, 0)
for i in range(1, m + 1):
    black_pixels[i] += black_pixels[i - 1]
change_color = [[1e4] * (m + 1), [1e4] * (m + 1)]
change_color[0][0] = 0
change_color[1][0] = 0

for i in range(m):
    for j in range(x, y + 1):
        if (i + j) > m:
            break
        change_color[0][i + j] = min(change_color[0][i + j], change_color[1][i] + black_pixels[i + j] - black_pixels[i])
        change_color[1][i + j] = min(change_color[1][i + j], change_color[0][i] + n * j - (black_pixels[i + j] - black_pixels[i]))

print(min(change_color[0][m], change_color[1][m]))


from PIL import Image, ImageDraw

image = Image.new("RGBA", (500, 500), (255, 255, 255))

draw = ImageDraw.Draw(image)

points = [(100, 300), (200, 100), (300, 300), (300, 400)]
for i in range(0, len(points)-1):
    draw.line([points[i], points[i + 1]], fill=(0,0,255), width=5)
draw.line([points[0], points[-1]], fill=(0,0,255), width=5)
# draw.line([points[1], points[2]], fill=outline_color, width=5)
# draw.line([points[0], points[2]], fill=outline_color, width=5)
#
# # Рисуем многогранник только с контуром
# draw.polygon(points, fill=(0, 0, 0, 0), outline=outline_color)

# Сохраняем изображение
image.save("polygon_outline.png")

# Показываем изображение
image.show()

# file = open("input.txt", 'r')
# n = int(file.readline())
# for i in range(0, n):
#     mas = file.readline().strip().split("\\s+")
#     if len(mas) != 2:
#         print("Ошибка в данных файла.")
#     for number in mas:
#         if number.__contains__('/'):
#             num, den = map(int, number.split('/'))
#             if den == 0:
#                 print("Ошибка: деление на ноль.")
#         elif number.__contains__('.'):
#             numbers = map(int, number.split('.'))
#             length = len(map[1])
#             num = map[0] * 10 ** length + map[1]
#             den = 10 ** length
#         else:
#             num, den = number, 1

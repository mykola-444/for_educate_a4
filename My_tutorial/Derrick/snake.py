from tkinter import *  # Замовлення  бібліотеки tkinter

root = Tk()  # Створити вікно
root.title("PythonicWay Snake")  # Встановити назву вікна

WIDTH = 750  # Ширина екрану
HEIGHT = 550  # Висота екрану
SEG_SIZE = 20  # Розмір сегмента змійки
IN_GAME = True  # Cтан гри

c = Canvas(root, width=WIDTH, height=HEIGHT, bg="#003300")
c.grid()
c.focus_set()

class Segment(object):
    def __init__(self, x, y):
        self.instance = c.create_rectangle(x, y, x + SEG_SIZE, y + SEG_SIZE, fill="white")


class Snake(object):
    def __init__(self, segments):
        self.segments = segments

        # список доступних напрямків руху змійки
        self.mapping = {"Down": (0, 1), "Up": (0, -1), "Left": (-1, 0), "Right": (1, 0)}

        # спочатку змійка рухається вправо
        self.vector = self.mapping["Right"]

    def move(self):  # Рух змійки в заданому напрямку
    # перебираємо всі сегменти крім першого
        for index in range(len(self.segments) - 1):
            segment = self.segments[index].instance
            x1, y1, x2, y2 = c.coords(self.segments[index + 1].instance)
            # задаємо кожному сегменту позицію сегмента стоїть після нього
            c.coords(segment, x1, y1, x2, y2)

            # отримуємо координати сегмента перед "головою"
            x1, y1, x2, y2 = c.coords(self.segments[-2].instance)

            # поміщаємо "голову" в напрямку вказаному в векторі руху
            c.coords(self.segments[-1].instance,
                     x1 + self.vector[0] * SEG_SIZE,
                     y1 + self.vector[1] * SEG_SIZE,
                     x2 + self.vector[0] * SEG_SIZE,
                     y2 + self.vector[1] * SEG_SIZE)

    def change_direction(self, event):  # Зміна напрямку руху змійки

        # event передає символ натиснутої клавіші
        # якщо ця клавіша в доступних напрямках, змінюємо напрямок
        if event.keysym in self.mapping:
            self.vector = self.mapping[event.keysym]

    def add_segment(self):  # Додати сегмент змійці

        # визначити останній сегмент
        last_seg = c.coords(self.segments[0].instance)

        # визначаємо координати куди поставити наступний сегмент
        x = last_seg[2] - SEG_SIZE
        y = last_seg[3] - SEG_SIZE

        # додаємо змійці ще один сегмент в заданих координатах
        self.segments.insert(0, Segment(x, y))


# створити набір 3 сегментів
segments = [Segment(SEG_SIZE, SEG_SIZE),
            Segment(SEG_SIZE * 2, SEG_SIZE),
            Segment(SEG_SIZE * 3, SEG_SIZE)]




s = Snake(segments)  # компонувати змійку


root.mainloop()  # Запуск вікна

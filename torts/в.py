import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference

# Создание DataFrame с данными о работе ивентов
data = {'Название': ['Ивент 1', 'Ивент 2', 'Ивент 3'],
        'Срок прохождения (в днях)': [10, 20, 30]}

df = pd.DataFrame(data)

# Создание Excel файла и запись данных
wb = Workbook()
ws = wb.active

for r in dataframe_to_rows(df, index=False, header=True):
    ws.append(r)

# Создание столбчатой диаграммы
chart = BarChart()
chart.type = "col"
chart.style = 10
chart.title = "График работы ивентов"
chart.y_axis.title = "Срок прохождения (в днях)"

data = Reference(ws, min_col=2, min_row=1, max_col=2, max_row=4)
labels = Reference(ws, min_col=1, min_row=2, max_row=4)
chart.add_data(data, titles_from_data=True)
chart.set_categories(labels)

ws.add_chart(chart, "E2")

# Сохранение Excel файла
wb.save("ивенты.xlsx")

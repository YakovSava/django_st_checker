from docx import Document

# Загружаем документ
doc = Document("example.docx")

# Вводим имя пользователя
name = input("Введите имя: ")

# Итерируем по всем параграфам
for paragraph in doc.paragraphs:
    # Заменяем {name} в тексте параграфа
    paragraph.text = paragraph.text.format(name=name)

# Итерируем по всем таблицам
for table in doc.tables:
    # Итерируем по всем ячейкам в таблице
    for row in table.rows:
        for cell in row.cells:
            # Заменяем {name} в тексте ячейки
            cell.text = cell.text.format(name=name)

# Сохраняем изменения
doc.save("example2.docx")

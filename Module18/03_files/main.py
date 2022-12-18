# spec_sym = list('@№$%^&*()')
#extensions = ('.txt', '.docx')
file_name = input('Название файла: ').lower()

# if file_name[0] in spec_sym:
#     print('Ошибка: название начинается на один из специальных символов')
if file_name.startswith(("@", "№", "$", "%", "^", "&", "*", "(", ")")):
    print('Ошибка: название начинается на один из специальных символов')
elif not file_name.endswith(('.txt', 'docx')):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
else:
    print('Файл назван верно.')

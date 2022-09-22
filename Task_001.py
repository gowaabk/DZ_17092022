""" Напишите программу, удаляющую из текста все слова, содержащие ""абв"". """


"""
def del_words(my_text: str, words: str):
    my_text = list(filter(lambda x: words not in x, my_text.split()))
    return ' '.join(my_text)

my_text = 'Какой то текст абв гдеабв удаабвлен текст, абвсодержащий\
    абв все абв слова, содерабващие содержащие "абв"'
words = 'абв'
my_text = del_words(my_text, words)
print(my_text)

 """
my_str = 'Какой то текст абв гдеабв удаабвлен текст, абвсодержащий\
    абв все абв слова, содерабващие содержащие "абв"'.split()
print(' '.join([word for word in my_str if 'абв' not in word]))

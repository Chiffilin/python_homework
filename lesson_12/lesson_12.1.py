import codecs
import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    # Видаляємо всі HTML-теги за допомогою регулярного виразу
    clean_text = re.sub(r'<[^>]+>', '', html)

    # Розділяємо текст на рядки, видаляємо порожні рядки
    cleaned_lines = [line for line in clean_text.splitlines() if line.strip()]
    clean_text_no_empty_lines = '\n'.join(cleaned_lines)

    # Записуємо очищений текст у новий файл
    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(clean_text_no_empty_lines)

    print(f"HTML-теги та пусті рядки видалено. Текст збережено в '{result_file}'.")


delete_html_tags("draft.html")
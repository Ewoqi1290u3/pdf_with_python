# Напомним, что PyMuPDF импортируется как fitz
import fitz

input_file = "source/Computer-Vision-Resources.pdf"
output_file = "dist/extra-page.pdf"

# Определите страницы для сохранения - 2, 3 и 5
file_handle = fitz.open(input_file)
pages_list = [1,2,4]

# Выберите страницы и сохраните вывод
file_handle.select(pages_list)
file_handle.save(output_file)

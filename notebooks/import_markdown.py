from IPython.display import display, HTML, Code, Markdown, Javascript

def import_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        markdown_content = file.read()
    display(Markdown(markdown_content))

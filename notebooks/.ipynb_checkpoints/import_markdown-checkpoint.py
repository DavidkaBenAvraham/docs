def import_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    markdown_cell = markdown_content
    jupyter_code = f'%%markdown\n{markdown_cell}'
    
    print(jupyter_code) 

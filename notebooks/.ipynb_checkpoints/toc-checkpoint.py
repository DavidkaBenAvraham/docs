from IPython.display import display, HTML, Javascript

def toc(page: str = None) -> None:
    """!
    @brief HTML TOC

    Parameters : 
        @param page : str = None => current page
    Returns : 
        @return None => [description]

    """

    """!  'путь_к_блокноту' на фактический путь к блокноту, куда хотите поставить ссылку"""
    notebook_path_supplier = 'supplier.ipynb'
    notebook_path_product = 'product.ipynb'
    notebook_path_scenario = 'scenario.ipynb'
    notebook_path_driver = 'driver.ipynb'
    notebook_path_driver_firefox = 'webdriver_firefox.ipynb'
    
    """!  'Текст для ссылки' на текст, который вы хотите использовать в качестве текста ссылки"""
    link_supplier = f'<a href="{notebook_path_supplier}" target="_blank"><b>Поставщик (Supplier)</b> - <i><font size="small">supplier.ipnb</font></i></a>'
    link_product = f'<a href="{notebook_path_product}" target="_blank"><i><b>Товар (Product)</b></i></a>'
    link_scenario = f'<a href="{notebook_path_scenario}" target="_blank"><i><b>Сценарий (scenario)</b></i>/<a>'
    link_driver = f'<a href="{notebook_path_driver}" target="_blank"><i><b>Драйвер (Driver)</b></i></a>'
    link_driver_firefox = f'<a href="{notebook_path_driver_firefox}" target="_blank"><i><b>Драйвер Firefox (Firefox)</b></i></a>'
    link_profile_firefox = '<a href="{notebook_path_driver_firefox}" target="_blank"><i><b>Профиль пользователя Firefox (Profile)</b></a>'
    link_driver_suffix = '</ul>'
    
    """! Генерируем HTML-код с ссылкой"""
    link_supplier = f'<a href="{notebook_path_supplier}" target="_blank">{link_supplier}</a>'
    link_product = f'<a href="{notebook_path_product}" target="_blank">{link_product}</a>'
    link_scenario = f'<a href="{notebook_path_scenario}" target="_blank">{link_scenario}</a>'
    link_driver = f'<a href="{notebook_path_driver}" target="_blank">{link_driver}</a>'
    link_driver_firefox = f'<a href="{notebook_path_driver_firefox}" target="_blank">{link_driver_firefox}{link_profile_firefox}{link_driver_suffix}</a>'
    

    """! Отображаем ссылку"""
    display(HTML(link_driver))
    display(HTML(link_supplier))
    display(HTML(link_product))
    display(HTML(link_scenario))
    if not page == 'intro':
        display(HTML(link_driver_firefox))
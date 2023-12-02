# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'hypotez'
copyright = '2023, davidka'
author = 'davidka'
release = '0.1.0'

import os
import sys

#sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))
#sys.path.insert(0, os.path.abspath('..'))
#sys.path.insert(0, os.path.abspath('../..'))

# -- Глубина рекурсии --------------------------------------------------------
sys.setrecursionlimit(1500)

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


"""
sphinx.ext.autodoc:
-------------------
Описание: Позволяет автоматически генерировать документацию на основе docstrings из исходного кода. 
Оно автоматически извлекает документацию для функций, классов, методов, переменных и т.д. из исходного кода.
Использование: Включается в conf.py с помощью extensions = ['sphinx.ext.autodoc']. 
Затем вы можете использовать директивы .. autoclass::, .. autofunction::, .. automodule::, и другие для автоматической генерации документации.


sphinx.ext.viewcode:
-------------------
Описание: Создает ссылки на исходный код, чтобы пользователи могли легко перейти к нему, чтобы увидеть реализацию.
Использование: Включается в conf.py с помощью extensions = ['sphinx.ext.viewcode']. 
Автоматически добавляет ссылки на исходный код к сгенерированным страницам документации.

sphinx.ext.napoleon:
-------------------
Описание: Позволяет использовать расширенные docstrings в стиле NumPy/Google. 
Это позволяет вам писать более понятную и информативную документацию для ваших функций и методов.
Использование: Включается в conf.py с помощью extensions = ['sphinx.ext.napoleon'].

sphinx.ext.autosummary:
-----------------------
Описание: Генерирует автоматические краткие описания для модулей на основе docstrings. 
Это позволяет вам создавать краткие описания для всех функций, классов и переменных в модуле с минимальными усилиями.
Использование: Включается в conf.py с помощью extensions = ['sphinx.ext.autosummary']. 
Затем можно использовать директиву .. autosummary:: в .rst файлах.

sphinx_autopackagesummary:
--------------------------
Описание: Это стороннее расширение, которое расширяет функциональность sphinx.ext.autosummary
и автоматически создает документацию для пакетов.
Использование: Требует установки пакета. Подробные инструкции можно найти в репозитории проекта: 
https://github.com/morefigs/sphinx-autopackagesummary
"""

# extensions = [
#     'sphinx.ext.autodoc',
#     'sphinx.ext.viewcode',
#     'sphinx.ext.napoleon',
#     'sphinx.ext.autosummary', 
#     'sphinx_autopackagesummary'
    
# ]
extensions = [
    'sphinx_autopackagesummary',
    'sphinx.ext.autosummary', 
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode', 
    'sphinx.ext.napoleon',
   
]

autosummary_generate = True
autosummary_mock_imports = ['src',
                            'webservers',
                            'notebooks',
                            'log',
                            'launchers',
                            'google',
                            'draw.io',
                            'BEERYAKOV',]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']





# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
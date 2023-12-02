"""! @brief Модуль запуска скрипта. 


@russian {
@details Определяет порядок запуска поставщиков (потоки/очередь), интерфейс (GUI, JUPYTER, CMD), 
            параметры запуска поставщиков (см. `start_script()`). 
            
@todo Расписать GUI, JUPYTER интерфейсы

--------

@note УРА!!!

--------

@warning Enabling multithreading puts a load on the CPU
        Запуск многопоточности нагружает цпу

--------


@code
> python main.py
@endcode

-------


### Flowchart

            
@image html diagrams-main.png

@}


@section libs imports:
- src.launchers (local)
- src.suppliers (local)
- src.project_settings (local)
- threading
- typing
- sys
- os
"""
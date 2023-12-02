# #Установить политику выполнения для текущего пользователя, разрешив выполнение всех скриптов:
# Set-ExecutionPolicy Unrestricted -Scope CurrentUser

# # Получение пути к директории исполняюого файла
# $scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Definition

# # Собираю пути
# # $doxygenPath = Join-Path $scriptDirectory "\bin\doxygen\doxygen.exe"
# # $enDoxyfilePath = Join-Path $scriptDirectory "\docs\doxygen\en.doxy"
# # $ruDoxyfilePath = Join-Path $scriptDirectory "\docs\doxygen\ru.doxy"

# $doxygenPath = Join-Path $scriptDirectory "\bin\doxygen\doxygen.exe"
# $enDoxyfilePath = Join-Path $scriptDirectory "\docs\doxygen\en.doxy"
# $ruDoxyfilePath = Join-Path $scriptDirectory "\docs\doxygen\ru.doxy"

# # Переходим в рабочий каталог скрипта
# Set-Location -Path $scriptDirectory

# # Запускаю EN doxygen
# Start-Process -FilePath $doxygenPath -ArgumentList $enDoxyfilePath -Wait

# # Запускаю RU doxygen
# Start-Process -FilePath $doxygenPath -ArgumentList $ruDoxyfilePath -Wait

Start-Process -FilePath ../../bin/doxygen/doxygen.exe -ArgumentList ru.doxy -Wait
Start-Process -FilePath ../../bin/doxygen/doxygen.exe -ArgumentList en.doxy -Wait
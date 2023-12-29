
# Путь к HTML-документу
$htmlFilePath = "_build\ru\html\index.html"

# Проверка существования файла
if (Test-Path $htmlFilePath -PathType Leaf) {
    # Открываем HTML-документ в браузере по умолчанию
    Start-Process $htmlFilePath
} else {
    Write-Host "_build\\ru\\html\\index.html не найден"
}

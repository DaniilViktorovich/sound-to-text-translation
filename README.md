# Преобразование аудио-файлов в текст

Для работы нам понадобиться установить модуль SpeechRecognition

### Установка модуля SpeechRecognition
```pip install SpeechRecognition```

### Cписок аудио форматов, с которыми работает модуль SpeechRecognition
* WAV
* AIFF
* AIFF-C
* FLAC

### Порядок выполнения кода:
* импортируем модуль SpeechRecognition
* присваиваем переменной "распознающее устройство"
* создадим объект класса AudioFile из библиотеки speech_recognition, передав в него аудиофайл
* выполняем преобразование аудио в текст с применением Google Cloud Speech API



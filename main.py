import speech_recognition as speech_recog


def text_recognition_from_audio(path_to_audio: str) -> None:
    '''Функция для преобразования аудио в текст'''

    # присваиваем переменной распознающее устройство
    recognition_device = speech_recog.Recognizer()

    # создадим объект класса AudioFile из библиотеки speech_recognition, передав в него аудиофайл
    audio_file = speech_recog.AudioFile(path_to_audio)

    # преобразовываем звук в текст
    with audio_file as source:
        recognition_device.adjust_for_ambient_noise(source)
        audio = recognition_device.record(source)
        result = recognition_device.recognize_google(audio, language='ru')
        print(result)

    # записываем распознанный текст в файл
    with open('audio_to_text.txt', 'w', encoding='utf-8') as result_txt:
        result_txt.write(result)


def main():
    path = input('введите путь к аудио-файлу: ')
    text_recognition_from_audio(path)


if __name__ == '__main__':
    main()

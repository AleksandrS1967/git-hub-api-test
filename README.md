# git-hub-api-test
Автоматический тест для проверки работы с GitHub API на языке Python.  
Тест умеет создавать, проверять наличие и удалять репозиторий если такой уже имеется.  
Легко воспроизводимо на любом компьютере.
___
Для работы c API GitHub была выбрана библиотека PyGitHub:  
![scrin](https://sun9-21.userapi.com/impg/_X4K6xV2grNpCvpHadUaAkyo-ezaBZYdHXTaXg/aZ99wz8qm0A.jpg?size=405x326&quality=96&sign=c97cffc253958714dc25d70b8c386c00&type=album)   
___
⚙️ Рекомендации по запуску:

- Клонируйте проект "https://github.com/AleksandrS1967/git-hub-api-test"  
- Установите виртуальное окружение в проект  
- Установите библиотеки из requirements.txt  
  ![scrin](https://sun9-30.userapi.com/impg/SIONKv_swvX7g4dIn43KUATZuXvjQKUFtb16iQ/d6lio7lbMHg.jpg?size=210x81&quality=96&sign=83926d5f63b43aaca5261ebe6ebcef6b&type=album)   
- Получите токен в настройках личного кабинета вашего аккаунта  
на gitHub и добавьте его в переменные окружения вашего ПК под именем GIT_TOKEN  
- Данные о токене, имени нового репозитория и все основные импорты находятся в "init" файле пакета "src"  
  ![scrin](https://sun9-37.userapi.com/impg/Rg0TlxY71WJmok-ZCb73rzFi5BLnQHv2rksMJw/UeHkK6VcCPs.jpg?size=728x373&quality=96&sign=7b4346b2ecc3ee32f75c6ea586425391&type=album)  
- Запустите файл сценария "main.py"  
___
💭 В планах:
- Установить библиотеку PyTest и покрыть проект тестами...
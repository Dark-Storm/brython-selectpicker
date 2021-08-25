# brython-selectpicker
## 

Установка
0. Скачиваем brython, или добавляем из CDN, в общем необходимо подключить Brython к своей странице (желательно в <head>) - <script src="/brython.js"></script>
1. Добавляем на свою страницу статику
    <script src="/brython_modules.js"></script>
    <link rel="stylesheet" href="/listbox.css">
2. Для того чтобы код на brython заработал необходимо добавить для тега body событие onload="brython()" (<body onload="brython()">)
3. Далее для тега <select> добавляем class="brython_select", а также сам код с selectpicker <script type="text/python" src="/custom_select.py"></script>
  
Это очень черновой вариант. Буду благодарен за любую помощь в развитии.

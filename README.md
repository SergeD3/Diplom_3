# Diplom_3
# Дипломный проект для курса обучения автоматизации тестирования веб-приложения на Python, PyTest и Selenium

## Описание
**Этот проект содержит автоматизированные тесты для тестового сайта StellarBurgers.
Тесты написаны с использованием фреймворков Selenium и Pytest, отчеты - с использованием Allure.
Для генерации тестовых данных исплоьзовалась библиотека Faker.
В проекте используется паттерн Page Object Model для организации структуры тестового фреймворка.**

## Список тестов

### 1. Восстановление пароля:
- **Переход на страницу восстановления пароля по кнопке «Восстановить пароль»**
- **Ввод почты и клик по кнопке «Восстановить»**
- **Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его**

### 2. Личный кабинет:
- **Переход по клику на «Личный кабинет»**
- **Переход в раздел «История заказов»**
- **Выход из аккаунта**

### 3. Проверка основного функционала:
- **Переход по клику на «Конструктор»**
- **Переход по клику на «Лента заказов»** 
- **При клике на ингредиент появляется всплывающее окно с деталями** 
- **Всплывающее окно закрывается кликом по крестику** 
- **При добавлении ингредиента в заказ увеличивается каунтер данного ингредиента** 
- **Залогиненный пользователь может оформить заказ** 

### 4. Раздел «Лента заказов»:
- **При клике на заказ открывается всплывающее окно с деталями**
- **Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»**
- **При создании нового заказа счётчик «Выполнено за всё время» увеличивается**
- **При создании нового заказа счётчик «Выполнено за сегодня» увеличивается**
- **После оформления заказа его номер появляется в разделе «В работе»**

### Зависимости:
- **Зависимости для проекта описаны в `requirements.txt`.**
- Команда для установки зависимостей: `pip install -r requirements.txt`
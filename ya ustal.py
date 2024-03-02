import requests
import re
class БазаДанных:
    def __init__(self):
        self.сайты = {}
    def добавить_сайт(self, сайт):
        if сайт in self.сайты:
            self.сайты[сайт] += 1
        else:
            self.сайты[сайт] = 1
    def очистить_бд(self):
        self.сайты.clear()
    def получить_результаты(self):
        # Сортировка сайтов по частоте
        отсортированные_сайты = sorted(self.сайты.items(), key=lambda x: x[1], reverse=True)
        return отсортированные_сайты
class Парсер:
    def __init__(self):
        pass
    def парсить_сайт(self, сайт):
        try:
            response = requests.get(сайт)
            # Используем регулярное выражение для поиска ссылок на странице
            найденные_ссылки = re.findall(r'href="\'(?=["\'])', response.text)
            for ссылка in найденные_ссылки:
                self.добавить_сайт(ссылка)
        except Exception as e:
            print(f"Ошибка при парсинге сайта {сайт}: {e}")
    def добавить_сайт(self, сайт):
        pass
class Интерфейс:
    def __init__(self):
        self.база_данных = БазаДанных()
        self.парсер = Парсер()

    def добавить_сайт(self, сайт):
        self.база_данных.добавить_сайт(сайт)

    def очистить_бд(self):
        self.база_данных.очистить_бд()

    def показать_результаты(self):
        результаты = self.база_данных.получить_результаты()
        for сайт, частота in результаты:
            print(f"{сайт}: {частота} раз")

def run():
    интерфейс = Интерфейс()
    while True:
        print("\nВыберите действие:")
        print("1. Добавить сайт")
        print("2. Очистить базу данных")
        print("3. Показать результаты")
        print("4. Выйти")
        выбор = input("Введите номер действия: ")
        if выбор == "1":
            сайт = input("Введите ссылку на сайт: ")
            интерфейс.добавить_сайт(сайт)
            print(f"Сайт {сайт} добавлен в базу данных.")
        elif выбор == "2":
            интерфейс.очистить_бд()
            print("База данных очищена.")
        elif выбор == "3":
            интерфейс.показать_результаты()
        elif выбор == "4":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
if __name__ == "__main__":
    run()

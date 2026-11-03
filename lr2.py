import sys
import platform
from datetime import datetime


def main():
    print("=" * 40)
    print(" 🚀 ПРОВЕРКА ОКРУЖЕНИЯ GITHUB CODESPACES ")
    print("=" * 40)

    # Информация о версии Python и ОС
    print(f"Версия Python: {sys.version.split()[0]}")
    print(f"Операционная система: {platform.system()} {platform.release()}")
    print(f"Архитектура: {platform.machine()}")

    # Текущая дата и время
    current_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    print(f"Текущее системное время: {current_time}")

    print("-" * 40)
    print("Все системы работают исправно. Окружение готово к работе!")
    print("=" * 40)


if __name__ == "__main__":
    main()
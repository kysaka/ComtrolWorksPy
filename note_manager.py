import csv
import os
from datetime import datetime

# Путь к файлу для хранения заметок
FILE_PATH = "notes.csv"

def save_notes(notes):
    with open(FILE_PATH, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(["ID", "Заголовок", "Тело", "Дата/Время"])
        for note in notes:
            writer.writerow(note)

def load_notes():
    if not os.path.exists(FILE_PATH):
        return []
    
    with open(FILE_PATH, "r") as file:
        reader = csv.reader(file, delimiter=";")
        next(reader)  # Пропускаем заголовок
        notes = [row for row in reader]
    return notes

def print_notes(notes):
    for note in notes:
        print(f"ID: {note[0]}")
        print(f"Заголовок: {note[1]}")
        print(f"Тело: {note[2]}")
        print(f"Дата/Время: {note[3]}")
        print("=" * 30)

def main():
    notes = load_notes()
    
    while True:
        print("Введите команду:")
        print("1 - Вывести список заметок")
        print("2 - Показать заметку по ID")
        print("3 - Добавить заметку")
        print("4 - Редактировать заметку")
        print("5 - Удалить заметку")
        print("0 - Выход")
        
        command = input()
        
        if command == "1":
            print_notes(notes)
        elif command == "2":
            note_id = input("Введите ID заметки: ")
            for note in notes:
                if note[0] == note_id:
                    print("Найденная заметка:")
                    print(f"ID: {note[0]}")
                    print(f"Заголовок: {note[1]}")
                    print(f"Тело: {note[2]}")
                    print(f"Дата/Время: {note[3]}")
                    break
            else:
                print("Заметка не найдена.")
        elif command == "3":
            title = input("Введите заголовок заметки: ")
            body = input("Введите тело заметки: ")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_note = [str(len(notes) + 1), title, body, timestamp]
            notes.append(new_note)
            save_notes(notes)
            print("Заметка успешно добавлена.")
        elif command == "4":
            note_id = input("Введите ID заметки для редактирования: ")
            for note in notes:
                if note[0] == note_id:
                    new_title = input("Введите новый заголовок заметки: ")
                    new_body = input("Введите новое тело заметки: ")
                    note[1] = new_title
                    note[2] = new_body
                    note[3] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    save_notes(notes)
                    print("Заметка успешно отредактирована.")
                    break
            else:
                print("Заметка не найдена.")
        elif command == "5":
            note_id = input("Введите ID заметки для удаления: ")
            for note in notes:
                if note[0] == note_id:
                    notes.remove(note)
                    save_notes(notes)
                    print("Заметка успешно удалена.")
                    break
            else:
                print("Заметка не найдена.")
        elif command == "0":
            break
        else:
            print("Неверная команда. Попробуйте снова.")

if __name__ == "__main__":
    main()

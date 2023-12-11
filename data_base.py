import psycopg2


data_base = psycopg2.connect(dbname="library", user="postgres", password="123456")
cursor = data_base.cursor()

def print_table():
    cursor.execute("SELECT * FROM Книги")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def edit_table():
    book_id = int(input("Введите номер записи для редактирования: "))
    author = input("Введите нового автора(ов): ")
    title = input("Введите новое название книги: ")
    year = int(input("Введите новый год издания: "))
    copies = int(input("Введите новое количество экземпляров: "))
    
    cursor.execute("UPDATE Книги SET \"Автор(ы)\" = %s, Название = %s, \"Год издания\" = %s, \"Кол-во экземпляров\" = %s WHERE \"Код книги\" = %s", (author, title, year, copies, book_id))
    cursor.connection.commit()

def create_row():
    kod_book = int(input("Введите код книги: "))
    author = input("Введите автора(ов): ")
    title = input("Введите название книги: ")
    year = int(input("Введите год издания: "))
    copies = int(input("Введите количество экземпляров: "))
    book = (kod_book, author, title, year, copies)
    
    
    
    cursor.connection.commit()

def delete_row():
    book_id = int(input("Введите номер записи для удаления: "))
    
    cursor.execute("DELETE FROM Книги WHERE \"Код книги\" = %s", (book_id,))
    cursor.connection.commit()

def main():
    print("Добро пожаловать!!!")
    print("1, Вывести базу данных на экран")
    print("2, Редактировать элементы")
    print("3, удалить элементы")
    print("4, Добавить элементы")
    print("5, Закончить работу")
    while True:
        alghoritm = {
            1: lambda: print_table(),
            2: lambda: edit_table(),
            3: lambda: delete_row(),
            4: lambda: create_row()
        }
        user_input = int(input("Выберете действие "))
        if isinstance(user_input, int):
            if user_input == 5:
                print("Всего наилучшего!")
                break  
            else:
                alghoritm[user_input]()
        else:
            print("Ошибка")

main()
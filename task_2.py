# Визначення класу Teacher
class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        # Перетворення списку предметів у множину для зручності операцій
        self.can_teach_subjects = set(can_teach_subjects)
        # Список предметів, які викладач фактично отримує для проведення занять
        self.assigned_subjects = []

def create_schedule(subjects, teachers):
    """
    Створює розклад занять за допомогою жадібного алгоритму для задачі покриття множини.
    На кожному кроці алгоритм обирає викладача, який може покрити найбільшу кількість
    непокритих предметів. При рівності – вибирається наймолодший викладач.
    
    Параметри:
        subjects  - множина предметів, які потрібно покрити
        teachers  - список об’єктів Teacher
        
    Повертає:
        Список викладачів, яким призначено певні предмети, або None, якщо неможливо покрити всі предмети.
    """
    uncovered_subjects = set(subjects)
    schedule = []
    remaining_teachers = teachers.copy()

    while uncovered_subjects:
        best_teacher = None
        best_new_subjects = set()
        best_count = 0

        for teacher in remaining_teachers:
            # Обчислюємо, які предмети з непокритих може викласти цей викладач
            new_subjects = teacher.can_teach_subjects.intersection(uncovered_subjects)
            count = len(new_subjects)
            # Обираємо викладача, який покриває найбільшу кількість нових предметів.
            # При рівності – вибираємо наймолодшого.
            if count > best_count:
                best_teacher = teacher
                best_new_subjects = new_subjects
                best_count = count
            elif count == best_count and count > 0 and best_teacher is not None:
                if teacher.age < best_teacher.age:
                    best_teacher = teacher
                    best_new_subjects = new_subjects

        # Якщо жоден викладач не може покрити жодного з непокритих предметів, розклад неможливо скласти
        if best_teacher is None or best_count == 0:
            return None

        # Призначаємо викладачу ті предмети, які він може покрити з-поміж непокритих
        best_teacher.assigned_subjects = list(best_new_subjects)
        schedule.append(best_teacher)
        remaining_teachers.remove(best_teacher)
        # Видаляємо покриті предмети з множини непокритих
        uncovered_subjects -= best_new_subjects

    return schedule

if __name__ == '__main__':
    # Множина предметів
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}

    # Створення списку викладачів
    teachers = [
        Teacher("Олександр", "Іваненко", 45, "o.ivanenko@example.com", {'Математика', 'Фізика'}),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {'Хімія'}),
        Teacher("Сергій", "Коваленко", 50, "s.kovalenko@example.com", {'Інформатика', 'Математика'}),
        Teacher("Наталія", "Шевченко", 29, "n.shevchenko@example.com", {'Біологія', 'Хімія'}),
        Teacher("Дмитро", "Бондаренко", 35, "d.bondarenko@example.com", {'Фізика', 'Інформатика'}),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", {'Біологія'})
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            # Сортуємо предмети для зручності виведення
            print(f"   Викладає предмети: {', '.join(sorted(teacher.assigned_subjects))}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
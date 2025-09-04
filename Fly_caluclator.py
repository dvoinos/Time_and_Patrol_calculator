from datetime import timedelta


def print_menu():
    print("=" * 40)
    print("   🚀 Time & Patrol Calculator 🚀")
    print("=" * 40)
    print("1️⃣  Розрахувати різницю між двома годинами")
    print("2️⃣  Додати два значення часу")
    print("3️⃣  Розрахунок палива для літака")
    print("4️⃣  Сума багатьох введених часів")
    print("0️⃣  Вихід")
    print("=" * 40)
    print("         created by Wadoz")
    print("=" * 40)


def diff_hours_minutes(time1, time2):
    t1 = timedelta(hours=time1[0], minutes=time1[1])
    t2 = timedelta(hours=time2[0], minutes=time2[1])
    delta = abs(t1 - t2)
    total_seconds = int(delta.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    return hours, minutes


def sum_hours_minutes(time_list):
    total_duration = timedelta()
    for hours, minutes in time_list:
        total_duration += timedelta(hours=hours, minutes=minutes)
    total_seconds = int(total_duration.total_seconds())
    total_hours = total_seconds // 3600
    total_minutes = (total_seconds % 3600) // 60
    return total_hours, total_minutes


def patrol_calculator():
    print('Введіть поокремо години та хвилини ')
    hours = input('Скільки годин тривав політ ?: ')
    minutes = input('Скільки хвилин ?: ')

    const_first_start_hours_ml = 1400
    const_last_hours_ml = 500
    const_hours_to_minutes = 60
    const_last_hours_ml_to_minutes = 8.3334

    int_hours_value = int(hours) - 1
    int_minutes_value = int(minutes)

    all_hours_to_minutes = (int_hours_value * const_hours_to_minutes) + int_minutes_value

    calculate_patrol_values = const_first_start_hours_ml + (
            const_last_hours_ml / const_hours_to_minutes * all_hours_to_minutes)

    calculate_last_hours = round(all_hours_to_minutes * const_last_hours_ml_to_minutes, 2)

    print(f'Політ тривав: {hours} годин та {minutes} хвилин')
    print(f'Загальна розрахована кількість палива на політ: {round(calculate_patrol_values, 2)} мл.')
    print('------------------')
    print(
        f'Загальна формула : За першу годину польоту -> 1400 мл. + решта часу : {int_hours_value} годин -> {calculate_last_hours} мл. ')


def sum_hours_minutes(time_list):
    total_duration = timedelta()
    for hours, minutes in time_list:
        total_duration += timedelta(hours=hours, minutes=minutes)
    total_seconds = int(total_duration.total_seconds())
    total_hours = total_seconds // 3600
    total_minutes = (total_seconds % 3600) // 60
    return total_hours, total_minutes


def patrol_calculator():
    print('Введіть поокремо години та хвилини ')
    hours = input('Скільки годин тривав політ ?: ')
    minutes = input('Скільки хвилин ?: ')

    const_first_start_hours_ml = 1400
    const_last_hours_ml = 500
    const_hours_to_minutes = 60
    const_last_hours_ml_to_minutes = 8.3334

    int_hours_value = int(hours) - 1
    int_minutes_value = int(minutes)

    all_hours_to_minutes = (int_hours_value * const_hours_to_minutes) + int_minutes_value

    calculate_patrol_values = const_first_start_hours_ml + (
            const_last_hours_ml / const_hours_to_minutes * all_hours_to_minutes)

    calculate_last_hours = round(all_hours_to_minutes * const_last_hours_ml_to_minutes, 2)

    print(f'Політ тривав: {hours} годин та {minutes} хвилин')
    print(f'Загальна розрахована кількість палива на політ: {round(calculate_patrol_values, 2)} мл.')
    print('------------------')
    print(
        f'Загальна формула : За першу годину польоту -> 1400 мл. + решта часу : {int_hours_value} годин -> {calculate_last_hours} мл. ')


def main():
    while True:
        print_menu()
        choice = input("Ваш вибір : ")

        if choice == "0":
            print("✅ Програма завершена користувачем.")
            break

        elif choice == "1":
            first_input = input('Введіть першу годину у форматі (15:30): ')
            if first_input == "0":
                break
            second_input = input('Введіть другу годину у форматі (8:15): ')
            if second_input == "0":
                break
            first_time = tuple(map(int, first_input.split(':')))
            second_time = tuple(map(int, second_input.split(':')))
            delta_h, delta_m = diff_hours_minutes(first_time, second_time)
            print(f"Різниця часу: {delta_h} годин та {delta_m} хвилин")

        elif choice == "2":
            first_input = input('Введіть першу годину у форматі (16:30): ')
            if first_input == "0":
                break
            second_input = input('Введіть другу годину у форматі (26:15): ')
            if second_input == "0":
                break
            first_time = tuple(map(int, first_input.split(':')))
            second_time = tuple(map(int, second_input.split(':')))
            total_h, total_m = sum_hours_minutes([first_time, second_time])
            print(f"Загальний час: {total_h} годин та {total_m} хвилин")

        elif choice == "3":
            patrol_calculator()

        elif choice == "4":
            time_list = []
            while True:
                if time_list:
                    print("Введені часи:", ", ".join([f"{h:02d}:{m:02d}" for h, m in time_list]))
                data_input = input("Введіть час у форматі ГГ:ХХ (наприклад 01:30). "
                                   "Введіть '=' щоб підрахувати суму, '-' щоб видалити останній, "
                                   "'q' щоб вийти у меню, або '0' для завершення: ")

                if data_input == "0":
                    print("✅ Програма завершена користувачем.")
                    return

                if data_input == "=":
                    total_h, total_m = sum_hours_minutes(time_list)
                    print("Введені часи:", ", ".join([f"{h:02d}:{m:02d}" for h, m in time_list]))
                    print(f"Загальний час: {total_h} годин та {total_m} хвилин")
                    break

                elif data_input == "-":
                    if time_list:
                        removed = time_list.pop()
                        print(f"❌ Видалено останній час: {removed[0]:02d}:{removed[1]:02d}")
                    else:
                        print("⚠️ Список порожній.")

                elif data_input.lower() == "q":
                    print("↩️ Повернення у меню.")
                    break

                else:
                    try:
                        hours, minutes = map(int, data_input.split(":"))
                        time_list.append((hours, minutes))
                    except ValueError:
                        print("❌ Невірний формат! Введіть у вигляді ГГ:ХХ")


if __name__ == "__main__":
    main()

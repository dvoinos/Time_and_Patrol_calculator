from datetime import timedelta


def print_menu():
    print("=" * 40)
    print("   🚀 Time & Patrol Calculator 🚀")
    print("=" * 40)
    print("1️⃣  Розрахувати різницю між двома годинами")
    print("2️⃣  Додати два значення часу")
    print("3️⃣  Розрахунок палива для літака")
    print("4️⃣  Сума багатьох введених часів")
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

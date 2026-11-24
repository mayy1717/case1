import datetime

SEPARATOR = "=" * 80

FONT = {
    '0': (" *** ",
          "*   *",
          "*   *",
          "*   *",
          " *** "),
    '1': ("  *  ",
          " **  ",
          "  *  ",
          "  *  ",
          " *** "),
    '2': (" *** ",
          "*   *",
          "   * ",
          "  *  ",
          "*****"),
    '3': ("*****",
          "   * ",
          "  ** ",
          "   * ",
          "*****"),
    '4': ("*   *",
          "*   *",
          "*****",
          "    *",
          "    *"),
    '5': ("*****",
          "*    ",
          "**** ",
          "    *",
          "**** "),
    '6': (" *** ",
          "*    ",
          "**** ",
          "*   *",
          " *** "),
    '7': ("*****",
          "   * ",
          "  *  ",
          " *   ",
          "*    "),
    '8': (" *** ",
          "*   *",
          " *** ",
          "*   *",
          " *** "),
    '9': (" *** ",
          "*   *",
          " ****",
          "    *",
          " *** "),
    '.': ("     ",
          "     ",
          "     ",
          "     ",
          "  *  "),
    ' ': ("     ",
          "     ",
          "     ",
          "     ",
          "     "),
}

ROW_COUNT = 5
CHAR_GAP = "  "


def read_int(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Это не число. Попробуйте ещё раз.")


def input_date():
    while True:
        day = read_int("День рождения (1-31): ")
        month = read_int("Месяц рождения (1-12): ")
        year = read_int("Год рождения: ")
        try:
            return datetime.date(year, month, day)
        except ValueError:
            print("Такой даты не существует. Введите данные заново.\n")


def get_weekday(birth_date):
    names = (
        "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье",
    )
    return names[birth_date.weekday()]


def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


def get_age(birth_date):
    today = datetime.date.today()
    try:
        anniversary = birth_date.replace(year=today.year)
    except ValueError:
        anniversary = datetime.date(today.year, 3, 1)
    if anniversary > today:
        return today.year - birth_date.year - 1
    return today.year - birth_date.year


def render_line(text, row):
    parts = []
    for ch in text:
        if ch not in FONT:
            ch = ' '
        parts.append(FONT[ch][row])
    return CHAR_GAP.join(parts)


def print_date_stars(birth_date):
    text = birth_date.strftime("%d %m %Y")
    print("\nДата рождения на табло:\n")
    for row in range(ROW_COUNT):
        print(render_line(text, row))
    print()


def print_report(birth_date):
    print(SEPARATOR)
    print(f"Дата рождения: {birth_date.strftime('%d.%m.%Y')}")
    print(f"День недели: {get_weekday(birth_date)}")
    print(f"Високосный год: {'Да' if is_leap_year(birth_date.year) else 'Нет'}")
    print(f"Возраст: {get_age(birth_date)} лет")
    print(SEPARATOR)


def main():
    print(SEPARATOR)
    birth_date = input_date()
    print()
    print_report(birth_date)
    print_date_stars(birth_date)


if __name__ == "__main__":
    main()
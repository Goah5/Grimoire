import os
from sys import argv


def get_page_number_list() -> list[int]:
    l = list(map((lambda x: x.split()[0]), os.listdir()))
    ll = []
    for i in l:
        if not i.isdigit():
            i = i[:i.find('.')]
        if i.isdigit():
            ll.append(int(i))
    return ll


def get_next_page_number() -> int:
    return max(get_page_number_list()+[0,]) + 1


def create_next_page(flag: bool = False) -> None:
    temp = get_next_page_number()

    if flag:
        os.mkdir(f"{temp}")
        print(f"Gen dir {temp}")
    else:
        with open(f"{temp}.py", "w") as f:
            f.write("")
        print(f"Gen py {temp}.py")


def display_commands_list(comands_list) -> None:
    for i in comands_list.keys():
        print(f'{i}: {comands_list[i][1]}')


def f1() -> None:
    create_next_page(False)


def f2() -> None:
    create_next_page(True)


def main():
    global comands_list
    display_commands_list(comands_list)

    while 1:
        is_correct = False
        while not is_correct:
            inp = input("Введите Команду> ").split()
            if inp != []:
                is_correct = inp[0] in comands_list

        if inp[0] == "1":
            display_commands_list(comands_list)
            continue

        comands_list[inp.pop(0)][0](*inp)


os.chdir(os.path.dirname(os.path.abspath(__file__)))
comands_list = {"0": [quit, "Выход"],
                "1": [display_commands_list, 'Help'],
                "2": [f1, 'Добавить Файл'],
                "3": [f2, 'Добавить Папку']}


if len(argv) > 1:
    for i in argv[1:]:
        comands_list[i][0]()
    quit()

if __name__ == "__main__":
    main()

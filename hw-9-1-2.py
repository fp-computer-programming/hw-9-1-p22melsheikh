# MEE 1/18/22


def on(list):
    for i, v in enumerate(list):
        try:
            if i % 2 != 0:
                print(int(v))
        except:
            if v == str or bool:
                print("only input integers please")

on([1, "two", 3, 4, 5, 6])
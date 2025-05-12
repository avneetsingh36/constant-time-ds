from constant_ds import ConstantDS

def main() -> None:

    test = ConstantDS()

    for x in (5, 3, 10, 20):
        test.insert(x)

    test.show()
    print(f'Random pick from list: {test.get_random()}')

    test.remove(5)
    test.show()

if __name__ == "__main__":
    main()

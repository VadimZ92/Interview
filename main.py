class Stack():

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        if len(self.stack) == 0:
            print("True")
            return True
        else:
            print("False")
            return False

    def push(self):
        elem = input("Введите элемент стека:\n")
        self.stack.append(elem)
        return self.stack

    def pop(self):
        elem = self.stack.pop(-1)
        return elem

    def peek(self):
        elem = self.stack[-1]
        print(f" Последний элемент стека: {elem}")
        return elem

    def size(self):
        size = len(self.stack)
        print(f"Длина стека: {size}")
        return size

    def main(self):
        """
                a - команда, которая вводит новый элемент стека;
                p – команда, которая выводит последний элемент стека;
                d – команда, которая удаляет последний элемент стека;
                s – команда, которая выводит длину стека;
                e - команда, которая проверяет стек на пустоту;
                q - (quit) - команда, которая завершает выполнение программы
        """
        while True:
            command = input("Введите команду:\n")
            if command == "a":
                st.push()
            elif command == "p":
                st.peek()
            elif command == "s":
                st.size()
            elif command == "d":
                st.pop()
            elif command == "e":
                st.isEmpty()
            elif command == "q":
                print("Выход")
                break


if __name__ == '__main__':
    st = Stack()
    st.main()

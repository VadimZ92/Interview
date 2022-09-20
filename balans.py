str_stack = "[([])((([[[]]])))]{()}"
stack = []


class Stack():

    def __init__(self):
        self.stack = []
        # self.str_stack = str_stack

    def isEmpty(self, stack):
        if len(stack) == 0:
            print("Строка сбалансирована")
            return True
        else:
            return False

    def pop(self, stack):
        elem = stack.pop(-1)
        return elem

    def size(self, str_stack):
        size = len(str_stack)
        return size

    def balans(self, str_stack):
        var = None
        if st.size(str_stack) % 2 != 0:
            print("Строка несбалансирована")
            return False
        for item in str_stack:
            if item == "(" or item == "[" or item == "{":
                stack.append(item)
            if st.isEmpty(stack) == True:
                break
            if item == ")":
                var = st.pop(stack)
                if var == "{" or var == "[":
                    print("Строка несбалансирована")
                    return False
                    break
            elif item == "}":
                var = st.pop(stack)
                if var == "(" or var == "[":
                    print("Строка несбалансирована")
                    return False
                    break
            elif item == "]":
                var = st.pop(stack)
                if var == "(" or var == "{":
                    print("Строка несбалансирована")
                    return False
                    break

        return st.isEmpty(stack)


# if __name__ == '__main__':
st = Stack()
st.balans(str_stack)

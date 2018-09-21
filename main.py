from Stack import Stack


def main():
    st = Stack()
    print('''
    0 - Exit
    1 - Print
    2 - Push
    3 - Top
    4 - Pop
    5 - Copy''')
    while True:
        try:
            k = int(input("-> "))
        except ValueError:
            k = "error"
        if k == 0:
            break
        elif k == 1:
            print(str(st))
        elif k == 2:
            elem = input("New element: ")
            st.push(elem)
        elif k == 3:
            print("Top: " + str(st.top()))
        elif k == 4:
            st.pop()
            print("Popped")
        elif k == 5:
            cpy = Stack(original=st)
            print("Copy: " + str(cpy))
        else:
            print("Incorrect input")


main()

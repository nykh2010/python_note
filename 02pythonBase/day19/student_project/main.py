


from menu import show_menu
from student_info import *


def main():
    docs = []  # 用来保存学生信息的列表
    while True:
        show_menu()
        s = input("请选择: ")
        if s == 'q':
            return
        elif s == '1':
            docs += input_student()
        elif s == '2':
            output_student(docs)
        elif s == '5':
            print_score_by_desc(docs)
        elif s == '9':
            save_to_file(docs, "si.txt")
        elif s == '10':
            docs = read_from_file("si.txt")
            


if __name__ == '__main__':
    main()

    
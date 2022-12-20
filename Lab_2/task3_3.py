def header_footer(fn):  # TODO написать декоратор
    def start_end():
        print("========")
        fn()
        print("========")
    return start_end


@header_footer
def my_func():
    print("Hello World")


if __name__ == "__main__":
    my_func()

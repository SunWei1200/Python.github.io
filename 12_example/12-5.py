#当直接执行此python程序时， __name__ == “__main__“ 的结果为True
#当执行其他python程序并调用此python程序时，
# __name__ == “__main__“ 的结果为False

class MyClass:
    i=12345
    def f(self):
        return 'hello world'
if __name__ =="__main__":
    myc=MyClass()
    print(myc.i)
    print(myc.f())
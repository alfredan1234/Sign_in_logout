# 1.用户自定义异常类型
class TooLongExceptin(Exception):
    "this is user's Exception for check the length of name "

    def __init__(self, leng):
        self.leng = leng

    def __str__(self):
        print("姓名长度是" + str(self.leng) + "，超过长度了")


# 2.手动抛出用户自定义类型异常
def name_Test():
    name = input("enter your naem:")
    if len(name) > 4:
        raise TooLongExceptin(len(name))  # 抛出异常很简单，使用raise即可,但是没有处理，即捕捉
    else:
        print(name)


# 调用函数，执行
name_Test()
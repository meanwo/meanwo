# def decorator(func):
#     def decorated(input_text):
#         print('함수 시작!')
#         func(input_text)
#         print('함수 끝!')
#
#     return decorated
#
#
# @decorator
# def hello_world(input_text):
#     print(input_text)
#
#
# hello_world('Hello world!')
#
# def check_integer(func):
#     def decorated(user, width, height):
#         if width>=0 and height>=0:
#             return func(user, width, height)
#         else:
#             raise ValueError('Input must be positive value')
#         return
#
# def login_required(func):
#     def decorated(user, width, height):
#         if user.is_authenticated:
#             return func(user, width,height)
# @check_integer
# @login_required
# def rect_area(width, height):
#     return width * height
#
# @check_integer
# @login_required
# def tri_area(width, height):
#     return (width * height) *0.5
#
#
# r_area = rect_area(-10, 10)
#
#
# class User:
#     def __init__(self, auth):
#         self.is_authenticated = auth
#
# user = User(auth=False)
#
# r_area = rect_area(user, 10, 10)
# print(r_area)
#
# r_area = rect_area(user, 10, 10)
# print(r_area)
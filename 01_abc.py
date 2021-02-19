# # 如果 a+b+c=1000，且 a^2+b^2=c^2（a,b,c 为自然数），如何求出所有a、b、c可能的组合?
# # 不靠数学公式，一个一个去试（枚举法）
# import time
#
# start_time = time.time()
#
# # 注意是三重循环
# # for a in range(0, 1001):
# #     for b in range(0, 1001):
# #         for c in range(0, 1001):
# #             if a**2 + b**2 == c**2 and a+b+c == 1000:
# #                 print("a, b, c: %d, %d, %d" % (a, b, c))
# # T= 1000 * 1000 * 1000 * 2
# # T= N * N * N * 2
# # T(n) = n^3 * 2
# for a in range(0, 1001):
#     for b in range(0, 1001):
#         c = 1000 - a - b
#         if a ** 2 + b ** 2 == c ** 2:
#             print("a, b, c: %d, %d, %d" % (a, b, c))
# # T= 1000 * 1000
# end_time = time.time()
# print("elapsed: %f" % (end_time - start_time))
# print("complete!")
from timeit import timeit

timeit(number=1000)
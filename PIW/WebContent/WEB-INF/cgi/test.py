#! /Library/Frameworks/Python.framework/Versions/3.8/bin/python3

import cgi  # python을 cgi로 사용
import request  # 결과 post 
import numpy as np
import matplotlib.pyplot as plt

# print("content-type:text/html; charset=UTF-8\n")

# 원적합 확인을 위한 원 만드는 함수 
"""
def make_circle(c, r):
    theta = np.linspace(0, 2 * np.pi, 256)
    x = r * np.cos(theta)
    y = r * np.sin(theta)    
    return np.vstack((x, y)).T + c
"""

# data from client
form = cgi.FieldStorage()
latlng = form["latlng"].value
# print("test : {}".format(latlng))

# 임의의 좌표 추가, ndarray 형식 변환
# data = [[1,1], [3, -1], [0, 4], [5, 6]]
# A = np.array(data)

# ones = np.ones((A.shape[0], 1))
# A = np.concatenate((ones, A), axis = 1)
# b = A[:,1] ** 2 + A[:,2] ** 2

# c = np.linalg.inv(A.T.dot(A)).dot(A.T).dot(b)
# # or you can do this just by using 
# # np.linalg.lstsq(A, b, rcond=None)[0]

# def return_circle(c):
#     x_c = c[1] / 2
#     y_c = c[2] / 2
#     r = c[0] + x_c ** 2 + y_c ** 2
    
#     return x_c, y_c, np.sqrt(r)

# x_c, y_c, r_c = return_circle(c)
# print(x_c, y_c, r_c)

# result = {
#     'lat' : x_c,
#     'lng' : y_c,
#     'rad' : r_c
# }

# result = []
# result.append(x_c)
# result.append(y_c)
# result.append(r_c)

# url = "http://localhost:12345/MLS/testResult.jsp"
# response = request.post(url, data=result)

print("Location: test.jsp")
print()

# 원적합 확인 
"""
fitted_circle = make_circle(np.array([x_c, y_c]), r_c)

plt.figure(figsize = (4,4))

plt.subplot(132)
plt.plot(fitted_circle[:,0], fitted_circle[:, 1], 'y-', label = 'fitted_circle')
plt.scatter(x = A[:,1], y = A[:, 2], color = 'r', label = 'sampled point')
plt.grid()
plt.xlim(0,20)
plt.ylim(0,20)

plt.show()
"""
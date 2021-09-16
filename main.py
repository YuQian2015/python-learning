course = "Python's Course for Beginners"  # 显示单引号
course2 = 'Python for "Beginners"'  # 显示双引号
course3 = 'Python\'s Course for Beginners'  # 显示单引号

print(course)
print(course2)
print(course3)
print(course[0])  # 获取第一个字符
print(course[-1])  # 获取倒数第一个字符
print(course[0:3])  # 获取第一个到第三个的字符，不包含course[3]
print(course[1:])  # 获取从第二个到最后一个的字符串
print(course[0:5])  # 获取前五个字符
print(course[:])  # 相当于复制一个字符串

name = 'Jennifer'
print(name[1:-1])

# 显示多行文本
email = '''
Hi John,

Here is out first email to you.

Thank you,
The support team

'''
print(email)
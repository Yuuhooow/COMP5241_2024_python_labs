# 创建一个空字典
fruit_dict = {}

# 向字典中添加键值对
fruit_dict['apple'] = 3
fruit_dict['banana'] = 5
fruit_dict['cherry'] = 7

# 访问字典中的值
print(fruit_dict['apple'])  # 输出: 3

# 遍历字典
for fruit, quantity in fruit_dict.items():
    print(f"{fruit}: {quantity}")

# 检查键是否存在于字典中
if 'apple' in fruit_dict:
    print("Apple is in the dictionary")

# 删除字典中的键值对
del fruit_dict['banana']
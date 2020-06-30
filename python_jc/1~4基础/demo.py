# 用户输入一个数字，打印这个数字出现的每一位数字的次数

def find_num_counts():
    nums = input()
    dic = {}
    for i in range(len(nums)):
        if nums[i] not in dic:
            dic[nums[i]] = 1
        else:
            dic[nums[i]] += 1

    for k in dic.keys():
        print(f"{k} 出现 {dic[k]} 次")

# 将列表[1,3,2,5,4,1,2,3,6,8,4,2]中的重复元素去掉并排好序（分别打印正序和倒叙）

def deal_list():
    list_=[1,3,2,5,4,1,2,3,6,8,4,2]
    l1 = list(set(list_))
    print('正序：',l1)
    print('倒叙：',l1[::-1])

# ### 存在一个列表
# list = [{'id' : 1,'name' : 'zhangsan','age' : '1'},
# {'id' : 2,'name' : 'lisi','age' : '2'}],
# 请设计实现：用户输入姓名，返回对应年龄,如果姓名不在内，则输出Not Found。

def find_user():
    name = input()
    list = [{'id' : 1,'name' : 'zhangsan','age' : '1'},{'id' : 2,'name' : 'lisi','age' : '2'}]
    is_exist = False
    for i in range(len(list)):
        if list[i]['name']==name:
            is_exist=True
            print(f'{name} 的年龄为 {list[i]["age"]}')
    if not is_exist:
        print("Not Found")

# print(ord('我'),' ',ord('喜'),' ',ord('欢'),' ',ord('你'))
# # 25105   21916   27426   20320
# print(chr(25105),chr(21916),chr(27426),chr(20320))
# # 我 喜 欢 你

# nums = [10,5,6,9,1,2,8,7,66]
# nums1 = sorted(nums)
# print(nums)
# print(nums1)
#
# # 正序
# nums.sort()
# print(nums)
# # 倒序
# nums.sort(reverse=True)
# print(nums)

list = [1,22,333]
yz = tuple(list)
print(yz)# (1, 22, 333)
a,b,c= yz
print(a,b,c) # 1 22 333


#需求:给定一个已排序的整数列表，要求输入一个数，
#并根据列表原有的排序规律将其插入到正确的位置上。
nums = [1, 3, 5, 7, 9]
b=0
a=int(input("请输入"))
for i in nums:               #还可以这样，更好
    b+=1                    #for i in range(len(nums)):    #这样可以判断下标而不是b+=1,i是下表，而不是其中的数字
    if a <=i:               #   if nums[i]>=a:
        nums.insert(b-1,a)  #      nums.insert(i,a) 
        break         
else:                        #      break
    nums.append(a)
print(nums)                 #print(nums)

#for else语句
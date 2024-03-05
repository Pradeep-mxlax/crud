# def sum_to():
#     nums = [3,2,4]
#     target = 6
#     dic = {}
#     for i,j in enumerate(nums):
#         if target - j not in dic:
#             dic.update({j:i})
#         else:
#             return  [dic[target-j],i]
        
# print(sum_to())

# x = 121
# y = 0
# z = x
# while 0<x:
#     a = x%10
#     y = y*10+a
#     x = x//10

# print(y) 



# def romanToInt(s):
#     dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
#     num=0
#     if len(s)>1:
#         for i,j in enumerate(s):
#             import pdb;pdb.set_trace()
#             if i+1==len(s) or dic[s[i]] > dic[s[i+1]] or dic[s[i]] == dic[s[i+1]]:
#                 num+=dic[s[i]]
#             else:
#                 num-=dic[s[i]]
#     else:
#         return dic[s]
        
#     return num 
# print(romanToInt('III'))












# def longestCommonPrefix(strs):
#     """
#     :type strs: List[str]
#     :rtype: str
#     """
#     lenth = len(min(strs,key=lambda x:len(x)))
#     for i in range(len(strs)):
#         import pdb;pdb.set_trace()
#         while lenth>0 and strs[0][0:lenth] !=strs[i][0:lenth]:
#             lenth-=1
#             if lenth == 0:
#                 return ""
#         pass
#     return strs[0][0:lenth]
# print(longestCommonPrefix(["flower","flow","flight"]))



# def removeElement( nums, val):
#     i = 0
#     import pdb;pdb.set_trace()
#     for x in nums:
#         if x != val:
#             nums[i] = x
#             i += 1
#     return i

# print(removeElement([3,2,2,3],3))


#Solution with TLE
# class Solution:
#     def dailyTemperatures(self, temp: List[int]) -> List[int]:
#         arr=[]
#         for i in range(len(temp)):
#             j=i+1
#             count=0
#             while j<len(temp):
#                 if temp[j]>temp[i]:
#                     count+=1
#                     break
#                 j+=1
#                 count+=1
#             if temp[i+count]>temp[i]:
#                 arr.append(count)
#             else:
#                 arr.append(0)
#         return arr

#True solution
class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        resu = [0]*len(temp)
        arr=[]
        for i,t in enumerate(temp):
            while arr and arr[-1][0]<t:
                tt,ii = arr.pop()
                resu[ii]=i-ii
            arr.append([t,i])
        return resu


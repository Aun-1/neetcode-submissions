class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            count[num] = count.get(num,0)+1
        print(count)

        arr=[]
        for num,cnt in count.items():
            arr.append([cnt,num]) #if you do .append((num,cnt)) then it will be a tuple instead of a list
        arr.sort()
        print(arr)

        res=[]
        while len(res)<k:
            res.append(arr.pop()[1])# [1] pops second elemt of each lsit
        return(res)
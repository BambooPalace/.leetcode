 def threeSum(nums, target): 
        # from xiaohao, 792ms, top 49%, O(N)
        n=len(nums)
        res=[]
        if(not nums or n<3):
            return []
        # nums.sort()
        res=[]
        for i in range(n):
            if(nums[i]>target):
                return res
            # 4Sum bug, modify 0 as target
            if(i>0 and nums[i]==nums[i-1]):
                continue
            L=i+1
            R=n-1
            while(L<R):
                if(nums[i]+nums[L]+nums[R]==target):
                    res.append([nums[i],nums[L],nums[R]])
                    while(L<R and nums[L]==nums[L+1]):
                        L=L+1
                    while(L<R and nums[R]==nums[R-1]):
                        R=R-1
                    L=L+1
                    R=R-1
                elif(nums[i]+nums[L]+nums[R]>target):
                    R=R-1
                else:
                    L=L+1
        return res

nums = [0,-1,0,-2,2]
target = -1
print(threeSum(nums, target))

class Solution(object):
    def threeSum(self, nums):
        ans,num_list = [], nums
        while len(num_list) > 2:
            n = num_list.pop(0)
            target = -n
            l = self.twoSum(num_list, target)
            if l is not None:
                for ll in l:
                    ll.append(n)
                for ll in l:
                    ll.sort()
                    if ll not in ans:
                        ans.append(ll)
        return ans
    def twoSum(self, num_list, target):
        num_dict, ans = {}, []
        for i, num in enumerate(num_list):
            diff = target - num
            if diff in num_dict:
                ans.append([diff, num])
            num_dict[num] = i
        return ans

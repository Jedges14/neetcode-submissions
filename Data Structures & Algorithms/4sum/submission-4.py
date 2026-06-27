class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res= []

        # a = 0
        # b = len(nums)-1

        # while a<b:
        #     c = a+1
        #     d = b-1

        #     while c < d:
        #         val = nums[a] + nums[b] + nums[c] + nums[d]
        #         if val > target:
        #             d -= 1

        #         elif val < target:
        #             c+=1

        #         else:
        #             found = [nums[a], nums[b], nums[c], nums[d]]
        #             res.add(found)
        #             c+=1
        #             d-=1
        #     a+=1
        #     b-=1
        # return list(res)



        for a in range(len(nums)):
            if a>0 and nums[a] == nums[a-1]:
                continue
            for b in range(a+1, len(nums)):
                if b>a+1 and nums[b] == nums[b-1]:
                    continue

                c = b+1
                d = len(nums)-1

                while c<d:
                    val = nums[a] + nums[b] + nums[c] + nums[d]

                    if val > target:
                        d -= 1

                    elif val < target:
                        c+=1

                    else:
                        found = [nums[a], nums[b], nums[c], nums[d]]
                        res.append(found)
                        c+=1
                        d-=1
                        while c<d and nums[c] == nums[c-1]:
                            c+=1

                        while c<d and nums[d] == nums[d+1]:
                            d-=1
        return res

        # seen = set()
        # unique = []
        # for sub in res:
        #     un = tuple(sorted(sub))
        #     if un not in seen:
        #         seen.add(un)
        #         unique.append(sub)
        #     else:
        #         seen.add(un)

        # return unique
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        carr = [0] * (max(people)+1)

        for p in people:
            carr[p] += 1

        idx = 0
        for n in range(len(carr)):
            while carr[n] > 0:
                people[idx] = n
                idx+=1
                carr[n] -= 1

        res = 0
        r = len(people) - 1
        l = 0

        while l<=r:
            if people[l] + people[r] <= limit:
                l+=1

            r-=1
            res+=1

        return res


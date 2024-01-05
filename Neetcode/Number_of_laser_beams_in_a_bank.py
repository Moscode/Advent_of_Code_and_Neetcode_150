class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = []
        for floor in bank:
            count = 0
            for one in floor:
                if one == "1":
                    count = count + 1
            if count > 0:
                ans.append(count)
        sums = 0
        prev = 0
        for i in ans:
            if prev == 0:
                prev = i
            else:
                sums += prev * i
                prev = i
        return sums
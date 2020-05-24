"""
    There are 8 prison cells in a row, and each cell is either occupied or vacant.
    Each day, whether the cell is occupied or vacant changes according to the following rules:
    If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
    Otherwise, it becomes vacant.

    (Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)
    We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, 
    else cells[i] == 0.

    Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)
"""

from collections import deque

class Solution():
    def prisionAfterNday(self, cells, k):
        res = cells
        seen = set()
        t = 0
        period = {}
        while k > 0:
            res = self.prisonAfterOneDay(res)
            res_tup = tuple(res)
            if res_tup in seen:
                k -= 1
                break
            else:
                seen.add(res_tup)
                period[t] = res
            k -= 1
            t += 1

        if k > 0:
            return period[k % len(period)]
        return res

    def prisonAfterOneDay(self, cells):
        return [int(i > 0 and i < 7 and cells[i - 1] == cells[i + 1]) for i in range(8)]


tc1, tc1_n = [0,1,0,1,1,0,0,1], 7

#constructing matrix and iterating through everyrow is not optimal solution
#for 10^9 iterations
tc2, tc2_n = [1,0,0,1,0,0,1,0], 1000000000

print(Solution().prisionAfterNday(tc1, tc1_n))
print(Solution().prisionAfterNday(tc2, tc2_n))

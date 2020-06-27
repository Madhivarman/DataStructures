"""
    Problem Statement:
    Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

    If the fractional part is repeating, enclose the repeating part in parentheses.
"""

class Solution():
    def fractionToDecimal(self, numerator, denominator):
        if denominator == 0: raise Exception('division by zero')

        def positiveDecimal(numerator: int, denominator: int) -> str:
            (q, r) = divmod(numerator, denominator)
            start = str(q)

            if r:
                #print(r)
                cur = ''
                seen = {}
                while True:
                    #print("current:{}, Seen:{}".format(cur, seen))
                    r *= 10
                    (q, r) = divmod(r, denominator)
                    cur += str(q)

                    if r == 0: 
                        return start + '.' + cur # non-recurring

                    if (q, r) in seen: # recurring case
                        i = seen[(q, r)]
                        return start + '.' + cur[:i] + '(' + cur[i:len(cur)-1] + ')'
                    else: 
                        seen[(q, r)] = len(cur) - 1

            else: return start
        
        #pass params numerator and denominator as absolute
        fraction = positiveDecimal(abs(numerator), abs(denominator))

        if numerator * denominator >= 0:
            return fraction
        else:
            '-'+fraction


tc1 = (1, 2)
tc2 = (2, 1)
tc3 = (2, 3)
tc4 = (95, 890)
tc5 = (999, 888888)

print(Solution().fractionToDecimal(tc1[0], tc1[1]))
print(Solution().fractionToDecimal(tc2[0], tc2[1]))
print(Solution().fractionToDecimal(tc3[0], tc3[1]))
print(Solution().fractionToDecimal(tc4[0], tc4[1]))
print(Solution().fractionToDecimal(tc5[0], tc5[1]))

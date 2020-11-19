class Solution():
    def decodeStrings(self, s):
        stack = [["", 1]]
        nums = [str(x) for x in range(10)]
        num = ""

        for char in s:
            #just append till you have formed the 
            #whole number
            if char in nums:
                num += char
            
            elif char == '[':
                stack.append(["", int(num)])
                num = "" #clear the integer number

            elif char == ']':
                string_, k = stack.pop()
                #append to the previous string
                stack[-1][0] += string_ * k

            else:
                stack[-1][0] += char
            
        return stack[-1][0]

tc1 = "3[a]2[bc]"
tc2 = "3[a2[bc]]"

print(Solution().decodeStrings(tc1))
print(Solution().decodeStrings(tc2))
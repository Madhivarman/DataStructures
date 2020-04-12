class Solution():

    def minimumEditRequired(self, str1, str2):
        src_length = len(str1)
        des_length = len(str2)
        #create a grid
        dp = [[0]*(src_length+1) for _ in range(des_length+1)]

        src_word = '0'+str1
        des_word = '0'+str2

        #initialize first row and column with range values
        for row in range(des_length+1):
            dp[row][0] = row

        for col in range(src_length+1):
            dp[0][col] = col

        #iterate through the table 
        for row in range(1, des_length+1):
            for col in range(1, src_length+1):
                #if the char matches just get the diagonal value
                if des_word[row] == src_word[col]:
                    dp[row][col] = dp[row-1][col-1]
                else:
                    dp[row][col] = 1 + min(dp[row][col-1], dp[row-1][col-1], dp[row-1][col])

        return dp[-1][-1]

        
tc1s='horse'
tc1d='ros'

tc2s='intention'
tc2d='execution'

tc3s='abcdef'
tc3d='azced'

print(Solution().minimumEditRequired(tc1s, tc1d))
print(Solution().minimumEditRequired(tc2s, tc2d))
print(Solution().minimumEditRequired(tc3s, tc3d))
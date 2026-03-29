# DP - LCS (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9251

import sys
sys.setrecursionlimit(10**6)

text1 = input()
text2 = input()

dp = [[-1] * (len(text2)+1) for _ in range(len(text1)+1)]

def longest_common_subsequence(text1_pos, text2_pos): 
    # base case
    if text1_pos < 0 or text2_pos < 0: 
        return 0 
    
    if dp[text1_pos+1][text2_pos+1] != -1:
        return dp[text1_pos+1][text2_pos+1]

    # case 1: 만약에 마지막 character가 같을때 
    if text1[text1_pos] == text2[text2_pos]: 
        dp[text1_pos+1][text2_pos+1] = longest_common_subsequence(text1_pos-1, text2_pos-1) + 1       
    else:
        # case 2: 만약에 현재 위치에 있는 각 text의 character가 다를 때 
        dp[text1_pos+1][text2_pos+1] = max(longest_common_subsequence(text1_pos-1, text2_pos), longest_common_subsequence(text1_pos, text2_pos-1))

    return dp[text1_pos+1][text2_pos+1]

print(longest_common_subsequence(len(text1)-1, len(text2)-1))
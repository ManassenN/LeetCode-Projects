# Given a string s, find the length of the longest substring without repeating characters.
#
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
#
# Constraints:
#
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

#Solution 1
# The Time Complexity Of This Solution Is O(n²)
def lengthOfLongestSubstring(s):
    visited = []
    counter = 0
    max = 0
    for i in range(0,len(s)):
        if s[i] in visited:
            if counter>max :
                max = counter
                counter = 0
                if s[i] == visited[i-1]:
                    visited.append(s[i])
                continue
        counter += 1
        visited.append(s[i])
    if counter > max:
        max = counter
    return max
print(lengthOfLongestSubstring('pwwkew'))
print(lengthOfLongestSubstring('bbbbb'))
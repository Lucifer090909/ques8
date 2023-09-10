# Function to find the longest common subsequence of consonants
def longest_common_subsequence_consonants(str1, str2):
    # Remove vowels from both strings
    consonants1 = ''.join(char for char in str1 if char not in 'aeiouAEIOU')
    consonants2 = ''.join(char for char in str2 if char not in 'aeiouAEIOU')

    # Length of the two strings
    m = len(consonants1)
    n = len(consonants2)

    # Initialize a table to store the length of the LCS
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if consonants1[i - 1] == consonants2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the longest common subsequence
    i, j = m, n
    lcs_consonants = []
    while i > 0 and j > 0:
        if consonants1[i - 1] == consonants2[j - 1]:
            lcs_consonants.append(consonants1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # Reverse the lcs_consonants list to get the correct order
    lcs_consonants.reverse()

    return ''.join(lcs_consonants)

# Input a string
input_string = input("Enter a string: ")

# Find the longest common subsequence of consonants
lcs_consonants = longest_common_subsequence_consonants(input_string, input_string[::-1])

# Display the result
print("Longest Common Subsequence of Consonants:", lcs_consonants)

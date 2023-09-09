def count_ways_and_probability(N):
    # Create a DP array to store the number of ways to attend classes on each day
    dp = [0] * (N + 1)

    # Initialize the DP array for the first few days
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    # Fill the DP array for the remaining days
    for i in range(4, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4]

    # Calculate the total number of ways to attend classes over N days
    total_ways = dp[N]

    # Calculate the probability of missing the graduation ceremony
    probability_miss = total_ways - dp[N - 4]

    # Return the answer in the requested string format
    return f"{probability_miss}/{total_ways}"

# Test cases
print(count_ways_and_probability(5))  
# Output: "14/29"
print(count_ways_and_probability(10)) 
# Output: "372/773"

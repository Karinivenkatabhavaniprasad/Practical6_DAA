def matrix_chain_order(p):
    n = len(p) - 1
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]
    for L in range(2, n + 1):
        for i in range(1, n - L + 2):
            j = i + L - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j]
                
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    s[i][j] = k
    return dp[1][n], s
def get_optimal_parenthesis(s, i, j):
    """
    Returns the formatted string of the optimal parenthesization.
    """
    if i == j:
        return f"A{i}"
    k = s[i][j]
    left = get_optimal_parenthesis(s, i, k)
    right = get_optimal_parenthesis(s, k + 1, j)
    return f"({left} x {right})"
if __name__ == "__main__":
    matrix_dimensions = [10, 20, 30, 40, 30] 
    min_cost, split_table = matrix_chain_order(matrix_dimensions)
    total_matrices = len(matrix_dimensions) - 1
    
    print(f"Minimum Scalar Multiplications: {min_cost}")
    print(f"Optimal Order: {get_optimal_parenthesis(split_table, 1, total_matrices)}")

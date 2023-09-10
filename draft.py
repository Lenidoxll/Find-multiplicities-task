def FindMultiplicitiesRecurive(Zs, Zi_values):
    ans = set()
    n = len(Zi_values)
    def recoursion(i, curS, ni):
        while Zi_values[i] * ni[i] + curS <= Zs:
            if Zi_values[i] * ni[i] + curS == Zs:
                ans.add(tuple(ni))
            if i < n - 1:
                recoursion(i + 1, curS + Zi_values[i] * ni[i], ni[:])
            ni[i] += 1

    recoursion(0, 0, [0] * n)
    return ans

def calculate_multiplicity(Zs, Zi_values):
    return [Zs // Zi for Zi in Zi_values]

def generate_effective_Zi_values(Zi_values, multiplicity):
    Zi = []
    for i in range(len(Zi_values)):
        Zi += [Zi_values[i]] * multiplicity[i]
    return Zi

def dynamic_programming(Zs, Zi_values):
    n = len(Zi_values)

    dp = [[False for _ in range(Zs + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for z in range(1, Zs + 1):
            if Zi_values[i - 1] <= z:
                dp[i][z] = dp[i - 1][z] or dp[i - 1][z - Zi_values[i - 1]]
            else:
                dp[i][z] = dp[i - 1][z]

    return dp

def backtrack(dp, Zi_values, Zs):
    ni_values = [0] * len(Zi_values)
    i, z = len(Zi_values), Zs
    while i > 0 and z > 0:
        if dp[i][z] and not dp[i - 1][z]:
            ni_values[i - 1] = 1
            z -= Zi_values[i - 1]
        i -= 1

    if z == 0:
        return ni_values
    else:
        return None


def backtrack_all(dp, Zi_values, Zs):
    n = len(Zi_values)
    valid_sets = []

    def backtrack_helper(i, z, ni_values):
        if i == 0:
            if z == 0:
                valid_sets.append(ni_values[:])  # Found a valid set, make a copy
            return

        # Include the current position and continue
        if i > 0 and z > 0 and dp[i][z]:
            ni_values[i - 1] = 1
            backtrack_helper(i - 1, z - Zi_values[i - 1], ni_values)
            ni_values[i - 1] = 0  # Backtrack

        # Exclude the current position and continue
        if i > 0:
            backtrack_helper(i - 1, z, ni_values)

    backtrack_helper(n, Zs, [0] * n)

    return valid_sets

# Main function to find valid ni values
def find_valid_ni(Zs, Zi_values):
    multiplicity = calculate_multiplicity(Zs, Zi_values)
    Zi_values = generate_effective_Zi_values(Zi_values, multiplicity)
    dp = dynamic_programming(Zs, Zi_values)
    valid_ni_values = backtrack_all(dp, Zi_values, Zs)
    return valid_ni_values
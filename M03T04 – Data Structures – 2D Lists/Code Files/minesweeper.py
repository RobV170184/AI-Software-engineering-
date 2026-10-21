# M03T04: 2D Lists - Minesweeper grid calculator

def minesweeper(grid):
    """
    Replace each dash with the count of adjacent mines.

    Parameters:
        grid (list): 2D list with # (mines) and - (safe spots).

    Returns:
        list: 2D list with numbers indicating adjacent mine counts.
    """
    rows = len(grid)
    cols = len(grid[0])
    result = []

    for row in range(rows):
        result_row = []
        for col in range(cols):
            if grid[row][col] == "#":
                result_row.append("#")
            else:
                # Count adjacent mines
                count = 0
                # Check all 8 adjacent positions
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        new_row = row + dr
                        new_col = col + dc
                        # Check if position is within bounds
                        if 0 <= new_row < rows and 0 <= new_col < cols:
                            if grid[new_row][new_col] == "#":
                                count += 1
                result_row.append(count)
        result.append(result_row)

    return result


# Example usage
grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

result = minesweeper(grid)

# Print result
for row in result:
    print(row)

import heapq

def min_path_sum(matrix):
    """
    Find the minimum path sum from top-left to bottom-right in a matrix
    Allowed moves: up, down, left, right
    """
    rows, cols = len(matrix), len(matrix[0])
    
    # Distance grid to track minimum cost to each cell
    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[0][0] = matrix[0][0]
    
    # Priority queue for efficient path exploration
    # Format: (current_total_cost, row, col)
    pq = [(matrix[0][0], 0, 0)]
    
    # Possible move directions: right, down, left, up
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    
    # Track visited cells to prevent redundant processing
    visited = set()
    
    while pq:
        current_cost, row, col = heapq.heappop(pq)
        
        # Optimization: Skip if we've found a better path to this cell
        if (row, col) in visited:
            continue
        
        # Mark as visited
        visited.add((row, col))
        
        # If we've reached bottom-right, return total cost
        if row == rows-1 and col == cols-1:
            return current_cost
        
        # Explore all four directions
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            
            # Check if new position is valid
            if (0 <= new_row < rows and 
                0 <= new_col < cols and 
                (new_row, new_col) not in visited):
                
                # Calculate new total cost
                new_cost = current_cost + matrix[new_row][new_col]
                
                # If we've found a cheaper path to this cell
                if new_cost < distances[new_row][new_col]:
                    distances[new_row][new_col] = new_cost
                    heapq.heappush(pq, (new_cost, new_row, new_col))
    
    return -1  # No path found

# Example usage
matrix = [
    [131,673,234,103,18],
    [201,96,342,965,150],
    [630,803,746,4422,111],
    [537,699,497,121,956],
    [805,732,524,37,331]
]

result = min_path_sum(matrix)
print(result)

m = open("0083_matrix.txt")
matrix = []
for line in m:
    l = line.strip()
    newline = [int(a) for a in l.split(",")]
    matrix.append(newline)

result = min_path_sum(matrix)
print(result)
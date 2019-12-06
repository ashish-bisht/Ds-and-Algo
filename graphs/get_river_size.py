def river_size(matrix):
    sizes = []
    visited = [[False for ele in row] for row in matrix]
    # print(visited)
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            # check if the node is vited or not
            if visited[row][col]:
                continue
            traverse_node(row, col, matrix, visited, sizes)
    return sizes


def traverse_node(row, col, matrix, visited, sizes):
    current_river_size = 0
    # will use dfs , hence using stack
    nodes_to_be_expored = [[row, col]]
    while len(nodes_to_be_expored):
        current_node = nodes_to_be_expored.pop()
        row = current_node[0]
        col = current_node[1]

        if visited[row][col]:
            continue
        visited[row][col] = True
        if matrix[row][col] == 0:
            continue

        # if no above condition then we know that river is there hence incrementing size.
        current_river_size += 1

        # now check for neighbours
        unvisited_neighbours = get_unvisited_neighbours(
            row, col, matrix, visited)

        # now add neighbours which qualify
        for neighbour in unvisited_neighbours:
            nodes_to_be_expored.append(neighbour)

        # now add the river size to the array
    if current_river_size > 0:
        sizes.append(current_river_size)


def get_unvisited_neighbours(row, col, matrix, visited):
    unvisited_neighbours = []
    # now checking for various conditions as if (i or col) == 0 will have less neighbours
    if row > 0 and not visited[row-1][col]:
        unvisited_neighbours.append([row-1, col])
    if row < len(matrix)-1 and not visited[row+1][col]:
        unvisited_neighbours.append([row+1, col])
    if col > 0 and not visited[row][col-1]:
        unvisited_neighbours.append([row, col-1])
    if col < len(matrix[0])-1 and not visited[row][col+1]:
        unvisited_neighbours.append([row, col+1])
    return unvisited_neighbours


if __name__ == "__main__":
    matrix = [
        [1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0],
    ]
    print(river_size(matrix))

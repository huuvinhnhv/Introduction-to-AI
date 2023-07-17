def thong_tin_sinh_vien():
    print('----------------------------')
    print("\tLab 1 - Basic search")
    print("\tMSSV: 21880159")
    print("\tTen: Nguyen Huu Vinh")
    print('----------------------------')


def graph_data(n):
    graph1 = [[1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0],
              [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
              [0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]]
    lable1 = ['s', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'p', 'q', 'r']
    graph2 = [[1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
              [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
              [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1]]
    lable2 = ['s', 'a', 'b', 'c', 'd', 'e', 'f',
              'g', 'h', 'k', 'm', 'n', 'p', 'q', 'r', 't']

    priority = [[8, -1, 6, -1],  # [phải, dưới, trái, trên],
                [2, 3, -1, -1],
                [-1, 4, 1, -1],
                [-1, 9, -1, 1],
                [5, 10, -1, 2],
                [-1, 11, 4, -1],
                [0, 2, -1, -1],
                [-1, -1, 15, 10],
                [9, -1, 0, -1],
                [-1, -1, 8, 3],
                [11, 7, -1, 4],
                [-1, -1, 10, 5],
                [13, -1, -1, 6],
                [14, -1, 12, -1],
                [15, -1, 13, -1],
                [7, -1, 14, -1]]
    graph3 = [[1, 1, 1, 0, 0, 0, 0],
              [1, 1, 1, 1, 0, 0, 0],
              [1, 1, 1, 1, 0, 0, 0],
              [0, 1, 1, 1, 1, 1, 1],
              [0, 0, 0, 1, 1, 0, 1],
              [0, 0, 0, 1, 0, 1, 1],
              [0, 0, 0, 0, 1, 1, 1]]
    label3 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    if n == 1:
        return graph1, lable1
    if n == 2:
        return graph2, lable2, priority
    if n == 3:
        return graph3, label3


def uniform_cost_search(matrix1, source, des):
    MAX_VALUE = 9999
    n = len(matrix1)
    matrix = matrix1.copy()
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][j] = MAX_VALUE

    parent = [-1] * n
    visited = [False] * n
    visited[source] = True
    distances = [MAX_VALUE] * n
    distances[source] = 0
    priority_queue = [(source, 0)]
    while priority_queue:
        cur_vertex = get_min_vertex(priority_queue)
        if cur_vertex == des:
            break
        visited[cur_vertex] = True
        for des in range(n):
            if des not in visited:
                if matrix[cur_vertex][des] != MAX_VALUE:
                    if distances[des] > matrix[cur_vertex][des] + distances[cur_vertex]:
                        distances[des] = matrix[cur_vertex][des] + \
                            distances[cur_vertex]
                        parent[des] = cur_vertex
                    data_vertex = (des, distances[des])
                    if data_vertex in priority_queue:
                        priority_queue.remove(data_vertex)
                    priority_queue.append(data_vertex)
    result_dis = distances[des]
    print(f"Distance from {source} to {des}: ", result_dis)
    print_path(parent, source, des)


def get_min_vertex(pq):
    pq.sort(reverse=True)
    v = pq.pop()
    return v[0]


def depth_first_search(matrix, label, source, des):
    n = len(matrix)
    parent = [-1] * n
    visited = [False] * n
    visited[source] = True
    stack = [source]
    while stack:
        v = stack.pop()
        if v == des:
            break
        i = 0
        while i < n:
            if matrix[v][i] == 1 and visited[i] is False:
                stack.append(v)
                visited[i] = True
                parent[i] = v
                if v == des:
                    break
                v = i
                i = -1
            i += 1
    print_path(parent, source, des, label)


def depth_first_search_with_priority(matrix, label, priority, source, des):
    n = len(matrix)
    parent = [-1] * n
    visited = [False] * n
    visited[source] = True
    stack = [source]
    while stack:
        v = stack.pop()
        if v == des:
            break
        i = 0
        while i < n:
            if matrix[v][i] == 1 and visited[i] is False:
                if get_priority(priority[v], visited) == i:
                    stack.append(v)
                    visited[i] = True
                    parent[i] = v
                    if v == des:
                        break
                    v = i
                    i = -1
            i += 1
    print_path(parent, source, des, label)


def get_priority(priority, visited):
    if priority[0] != -1 and not visited[priority[0]]:
        return priority[0]
    if priority[1] != -1 and not visited[priority[1]]:
        return priority[1]
    if priority[2] != -1 and not visited[priority[2]]:
        return priority[2]
    if priority[3] != -1 and not visited[priority[3]]:
        return priority[3]


def breadth_first_search(matrix, label, source, des):
    n = len(matrix)
    parent = [-1] * n
    visited = [False] * n
    visited[source] = True
    queue = [source]
    while queue:
        v = queue.pop(0)
        if v == des:
            break
        for i in range(n):
            if matrix[v][i] == 1 and visited[i] is False:
                queue.append(i)
                visited[i] = True
                parent[i] = v
    print_path(parent, source, des, label)


def print_path(path, source, des, label):
    cur = des
    while cur != source:
        print(label[cur] + " <- ", end="")
        cur = path[cur]
    print(label[cur], "")


if __name__ == '__main__':
    # adjacent_matrix = [[0, 0, 1, 0, 0, 0, 0, 0],
    #                    [1, 0, 0, 0, 0, 0, 0, 0],
    #                    [0, 1, 0, 1, 0, 0, 0, 0],
    #                    [0, 0, 0, 0, 1, 1, 1, 0],
    #                    [0, 0, 0, 0, 0, 1, 0, 0],
    #                    [0, 0, 0, 0, 0, 0, 0, 0],
    #                    [0, 0, 0, 0, 0, 0, 0, 0],
    #                    [1, 0, 0, 0, 0, 0, 1, 0]]
    # adjacent_matrix1 = [[0, 5, 0, 3, 0, 0, 0],
    #                     [0, 0, 1, 0, 0, 0, 0],
    #                     [0, 0, 0, 0, 6, 0, 8],
    #                     [0, 0, 0, 0, 2, 2, 0],
    #                     [0, 4, 0, 0, 0, 0, 0],
    #                     [0, 0, 0, 0, 0, 0, 3],
    #                     [0, 0, 0, 0, 4, 0, 0]]
    # matrix = np.array(adjacent_matrix)
    adjacent_matrix1, label1 = graph_data(1)
    adjacent_matrix2, label2, priority3 = graph_data(2)
    adjacent_matrix3, label3 = graph_data(3)
    thong_tin_sinh_vien()
    print('Cau 2.1: Thuat toan dung BFS tim duong di tu s -> g hoac tu A -> G cho 3 hinh:')
    print("Hinh 1: ")
    breadth_first_search(adjacent_matrix1, label1, 0, 7)
    print("Hinh 2: ")
    breadth_first_search(adjacent_matrix2, label2, 0, 7)
    print("Hinh 3: ")
    breadth_first_search(adjacent_matrix3, label3, 0, 6)
    print('Cau 2.2: Thuat toan dung DFS tim duong di tu s -> g hoac tu A -> G cho 3 hinh:')
    print("Hinh 1: ")
    depth_first_search(adjacent_matrix1, label1, 0, 7)
    print("Hinh 2: ")
    depth_first_search_with_priority(adjacent_matrix2, label2, priority3, 0, 7)
    print("Hinh 3: ")
    depth_first_search(adjacent_matrix3, label3, 0, 6)
    # breadth_first_search(adjacent_matrix, 0, 5)
    # uniform_cost_search(adjacent_matrix1, 0, 6)

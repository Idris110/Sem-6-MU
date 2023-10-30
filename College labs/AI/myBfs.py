graph  = {
    '5' : ['3', '7'],
    '3' : ['2', '4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}
visited =[]
queue = []
path = []

def bfs(initial, goal, visited) :
    # visited.append(initial)
    queue.append(initial)

    while queue :
        print(queue)
        node = queue.pop(0)
        
        # print("vis :" ,visited)

        if node not in visited :
            visited.append(node)
            path.append(node)
            # print("gra ",graph[str(node)])

            for child in graph[str(node)] :
                print(child)
                if child == goal :
                    for i in path:
                        print(i," -> ", end="")
                    print(goal)
                    return True
                queue.append(child)



    return False

print(bfs('5','8',visited))

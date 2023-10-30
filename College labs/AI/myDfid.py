graph  = {
    '5' : ['3', '7'],
    '3' : ['2', '4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}

def dfs(init, goal, lim) :
    visited =[]
    stack = []
    # path = []

    stack.append(init)
    iter = 1

    while stack and iter <= lim :
        print(iter, "th iter, Stack :", stack)
        iter += 1
        node = stack.pop(0)

        if node not in visited :
            visited.append(node)

            for child in reversed(graph[node]) :
                if child == goal :
                    print("found goal node "+ goal)
                    return True
                
                stack.insert(0, child)
    return False


def dfid(init, goal, lim):
    
    for i in range(lim):
        print("\nLimit :", (i+1), "  ======================")
        if dfs(init, goal, i+1) == True :
            return True


dfid('5', '8', 5)
    
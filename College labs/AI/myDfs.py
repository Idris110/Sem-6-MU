graph  = {
    '5' : ['3', '7'],
    '3' : ['2', '4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}
visited =[]
stack = []
path = []

# def dfs(cur, final, visited) :
#     # print(cur, " - ", final)
#     if(cur == final):
#         return True
    
#     for child in graph[cur]:
#         print(child)
#         if cur not in visited :
#             if dfs(child, final, visited) == True :
#                 return True
#     return False
def dfs(init, goal, visited) :
    # print(cur, " - ", final)
    stack.append(init)

    while stack :
        print(stack)
        node = stack.pop(0)
        print("cur : ",node )

        if node not in visited :
            visited.append(node)

            for child in reversed(graph[node]):
                print(child)
                if child == goal :
                    return True

                stack.insert(0, child)

    return False


print(dfs('5', '8', visited))
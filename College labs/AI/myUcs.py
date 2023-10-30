        
graph= [
    # 0   1  2   3    4    5    6    7
    [100, 1, 4, 100, 100, 100, 100, 100],
    [100, 100, 100, 3, 2, 100, 100, 100],
    [100, 100, 100, 100, 100, 100, 100, 5],
    [100, 100, 100, 100, 100, 5, 100, 100],
    [100, 100, 100, 100, 100, 100, 4, 3],
    [100, 100, 100, 100, 100, 100, 100, 7],
    [100, 100, 100, 100, 100, 100, 100, 100],
    [100, 100, 100, 100, 100, 100, 100, 100]
]
cnt=0
path = []

def ucs(graph,initial,goal):
    open = {}
    closed = []
    open[initial] = 0
    curr = initial

    while True:
        if(curr == goal):
            print('Goal Reached')
            break
        else:

            for i in graph[curr]:
                if(i!=100):
                    open[(graph[curr].index(i))]= i

            closed.append(curr)
            # open.remove(curr)
            del open[curr]
            print('Open:',open)
            print('Closed:',closed)
            # curr = graph[curr].index(min(graph[curr]))
            # print('min open:',min(open, key=open.get) , 'open.get',min(open))
            curr = min(open, key=open.get)
            print('NEW curr:',curr)
            path.append(curr)
    print('Path:',path)

goal = 7
initial = 0
ucs(graph,initial,goal)

print(initial,'->',end='')
for i in path:
    if(i==goal):
        print(i)
    else:
        print(i,'->',end='')

# replace number with alphabet
print(chr(initial+65),'->',end='')
for i in path:
    print(chr(i+65),'->',end='')    

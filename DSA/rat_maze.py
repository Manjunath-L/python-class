def findPath(i,j,maze,n,path,res,tracker):
    if i == (n-1) and j == (n-1):
        res.append(path)
        return
        
    #Downwards
    if(i+1 < n and tracker[i+1][j] == 0 and maze[i+1][j] == 1):
        path += "D"
        tracker[i+1][j] = 1 #visited
        findPath(i+1,j,maze,n,path,res,tracker)
        tracker[i+1][j] = 0 # not visited
        
    #Left
    if(j-1 >= 0 and tracker[i][j-1] == 0 and maze[i][j-1] == 1):
        path += "L"
        tracker[i][j-1] = 1 #visited
        findPath(i,j-1,maze,n,path,res,tracker)
        tracker[i][j-1] = 0 # not visited
        
    #Right
    if(j + 1 < n and tracker[i][j+1] == 0 and maze[i][j+1] == 1):
        path += "R"
        tracker[i][j+1] = 1 #visited
        findPath(i,j+1,maze,n,path,res,tracker)
        tracker[i][j+1] = 0 # not visited
    #UP
    if(i-1 >= 0 and tracker[i-1][j] == 0 and maze[i-1][j] == 1):
        path += "U"
        tracker[i-1][j] = 1 #visited
        findPath(i-1,j,maze,n,path,res,tracker)
        tracker[i-1][j] = 0 # not visited

def ratInMaze(maze):
    res = []
    n = len(maze)
    tracker = []
    for i in range(0,n):
        cols = []
        for j in range(0,n):
            cols.append(0)
        tracker.append(cols)   
        
    if maze[0][0] == 1:
        tracker[0][0] == 1
        findPath(0,0,maze,n,"",res,tracker)
    return res

maze = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
res = ratInMaze(maze)
print(res)
import copy
class Node:
    def __init__(self, state, parent=None): #parent is to  be note the previous node
        # Store the node state and parent state
            self.state=state
            self.parent=parent
    
    def __str__(self):
        # Implement a method to print the state of the node
        s=""
        for i in range(len(self.state)):
            for j in range(len(self.state[0])):
                s+=f"{self.state[i][j]} "
            s+="\n"
        return s

class PuzzleSolver:
    def __init__(self, start, goal):
        # Initialize the puzzle with start and goal state
        self.start=start
        self.goal=goal
    
    def is_solvable (self, state):
        # Check if the puzzle state is solvable
        
        copy_state = []
        for row in state.state:
            for col in row:
                if col != " ":
                    copy_state.append(col)

        #print(copy_state)
        inv_count=0
        for k in  range(len(copy_state)):
            for l in range(k+1,len(copy_state)):
                if (copy_state[k]> copy_state[l]):
                    inv_count+=1
        print(inv_count)
        return (inv_count%2==0)  
            

    def find_space(self, state):
        # Implement the method to find the position (x, y) of the empty space (' ')
        for i in range(len(state)):
            for j in range(len(state[0])):
                if (state[i][j]==" "):
                    return (i, j)

    def find_moves(self, pos):
        # Implement the method to generate valid moves for the empty space
        x, y = pos
        return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

    def is_valid(self, move , state):
        # Implement the method to check if a move is within bounds of the puzzle
        x,y= move
        return 0 <= x < len(state) and 0 <= y < len(state[0]) #column

    def play_move(self, state, move, space):
        # Implement the method to generate a new state after making the move
        x_space, y_space = space
        x_move, y_move = move
        copy_state = copy.deepcopy(state)
        for i in range(len(state)): 
             for j in range(len(state[0])):
                copy_state[i][j] =state[i][j]
        #print(copy_state)
        copy_state[x_space][y_space], copy_state[x_move][y_move] = copy_state[x_move][y_move], copy_state[x_space][y_space] # swapping the values of the space and the move
        return copy_state

    def generate_children(self, state):
        # Implement the method to generate all valid children from a state
        children = []
        space = self.find_space(state)
        moves = self.find_moves(space)

        for move in moves:
             if self.is_valid(move,state):
                child = self.play_move(state,move,space)
                children.append(child)
        return children
        

    def solve_puzzle_dfs(self): # using stack LIFO for this
        # Implement the search strategy for simple depth-first-search
        open_list = [self.start]
        closed_list = []
        while open_list:
            node = open_list.pop()  
            if self.is_goal(node.state):
                print("Goal state reached!")
                #self.disp_solution(node)
                return node
            elif node.state not in closed_list:
                closed_list.append(node.state)
                childs = self.generate_children(node.state)
                for child in childs:
                        if child not in closed_list:
                            open_list.append(Node(child,node))
        print("No solution found!")
        
    
    def solve_puzzle_bfs(self):
        # Implement the search strategy for breadth-first-search
        open_list = [self.start] 
        #print(open_list)
        closed_list = [] # using for visited
         
        while open_list:
            node = open_list.pop(0)  

            if self.is_goal(node.state):
                print("Goal state reached!")
                #self.disp_solution(node)
                return node
                

            elif node.state not in closed_list:
                closed_list.append(node.state)  
                childs = self.generate_children(node.state)
                for child in childs :
                    if child not in closed_list:
                        open_list.append(Node(child, node))   

        print("No solution found!")
        return None



        
    
    def solve_puzzle_dfid(self):
    # Implement the search strategy for depth-first-search with iterative deepening
        def dls(node, depth):
            if node.state == self.goal.state:
                #self.disp_solution(node)
                return node
        
            if depth == 0:
                return None
        
            for child_state in self.generate_children(node.state):
                child = Node(child_state, node)
                res = dls(child, depth - 1)  
                if res:  
                    return res
        
            return None 

    # Call dls function iteratively and search
        depth = 0
        while True:
            res = dls(self.start, depth)
            if res: 
                return res
                
            depth += 1 
                

    def disp_solution(self, final_state):
        # Implement the method to display the solution path
        
        path = []
        while final_state:
            path.insert(0, final_state)
            final_state = final_state.parent
        print("\nSolution Path:")
        i=1
        for step in path:
            print(f"step {i}")
            print(step)
            i+=1
        
    def is_goal(self, current_state):
      return current_state == self.goal.state 

#Run this Test-Case

def main ():
    start = Node([[4, 7, 8], [3, 6, 5], [1, 2, ' ']])
    goal = Node([[' ',7,8],[4,3,6],[1,2,5]])
    #print(start)
    solver = PuzzleSolver(start,goal)
    
    #print(solver.is_goal(goal))
    """ print(solver.is_solvable(start.state))
    s= solver.find_space(start.state)
    print(s)
    print(solver.find_moves(s)) """
    #print(solver.generate_children(start.state))
    #==========================================================================
    if solver.is_solvable(start):
        print(solver.solve_puzzle_dfs())
        #print(solver.solve_puzzle_bfs())
        #print(solver.solve_puzzle_dfid())
        #print(solver.solve_puzzle_backtracking())
    else: 
      print("Puzzle is not solveable")
      
main()
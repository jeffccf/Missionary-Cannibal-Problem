class solution:
    def __init__(self): # Initialize the three counts and number of solutions
        self.ill_count = 0
        self.visited_count=0
        self.total_count=0
        
    def dfs(self, mis, can, side, res, visited, path, goal_state):
        cur_state = [mis,can,side] # Current state
        if mis<0 or mis>3 or can<0 or can>3: # invalid states
            return
        if cur_state==goal_state: # If this is the goal state
            self.total_count += 1 # Add total state count here
            res.append(path + [goal_state]) # Add the path to the result list
            return
        if cur_state in visited: #This checks for repeated states
            self.visited_count += 1 # If current state is visited, count++
            return
        if mis!=0 and mis<can: # Cannibals on the left bank eat the missionaries
            self.ill_count += 1
            return # death state
        if 3>mis and mis>can: # Cannibals on the right bank eat the missionaries
            self.ill_count += 1
            return # death state 
        self.total_count += 1 # Add total state count here
        if side=="L": # If the boat is on the left bank, search the 5 possible next state (regardless its visited or invalid)
            self.dfs(mis-2, can, "R", res, visited+[cur_state], path+[cur_state], goal_state) # MMR
            self.dfs(mis-1, can, "R", res, visited+[cur_state], path+[cur_state], goal_state) # MR
            self.dfs(mis-1, can-1, "R", res, visited+[cur_state], path+[cur_state], goal_state) #MCR
            self.dfs(mis, can-1, "R", res, visited+[cur_state], path+[cur_state], goal_state) # CR
            self.dfs(mis, can-2, "R", res, visited+[cur_state], path+[cur_state], goal_state) # CCR
        if side=="R": # If the boat is on the right bank, search the 5 possible next state (regardless its visited or invalid)
            self.dfs(mis+2, can, "L", res, visited+[cur_state], path+[cur_state], goal_state) # MML
            self.dfs(mis+1, can, "L", res, visited+[cur_state], path+[cur_state], goal_state) # ML
            self.dfs(mis+1, can+1, "L", res, visited+[cur_state], path+[cur_state], goal_state) # MCL
            self.dfs(mis, can+1, "L", res, visited+[cur_state], path+[cur_state], goal_state) # CL
            self.dfs(mis, can+2, "L", res, visited+[cur_state], path+[cur_state], goal_state) # CCL
        return
    
if __name__ == '__main__':
    
    # Initialize inputs
    res = [] # A list of solutions
    visited = [] # A list of visited states
    path = [] # This stores the current path
    goal_state = [0,0,'R']
    
    agent = solution() # Initialize the solution class
    missionary = 3
    carnnibals = 3
    agent.dfs(missionary, carnnibals, 'L', res, visited, path, goal_state) # Run the depth first search
    
    for i in range(len(res)): # Lastly, print all the results
        print("Solution:")
        for state in res[i]:
            print(tuple(state))
    print("total states:", agent.total_count) # Print the counts
    print("illegal states:",agent.ill_count)
    print("repeat states:",agent.visited_count)

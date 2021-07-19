#!/usr/bin/env python
# coding: utf-8

# # Assignment: Handling Data
# 
# This problem set aims to solidify your understanding of the first half of Module 4 (intermediate data types).  
# 
# Please follow all instructions precisely.

# ## Problem 1: Social Media Relationships (9 points) 
# 
# Let us pretend that you are building a new app. Your app supports social media functionality, which means that users can have _relationships_ with other users.  
# 
# There are two guidelines for describing relationships on this social media app:  
# 1. Any user can _follow_ any other user.  
# 2. If two users follow each other, they are considered _friends_.  
# 
# Data about your users and their followers is stored in a dictionary that adheres to this structure:  

# In[2]:


# NON-INTERACTIVE CODE CELL. YOU MAY RUN THIS CELL, BUT DO NOT EDIT IT.
# FOR DEMONSTRATION PURPOSES ONLY. DO NOT EDIT.

social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}


# **Write a function called `relationship_status` that takes three positional arguments: (str) `from_member`, (str) `to_member`, and (dict) `social_graph`. The function should determine the _relationship status_ of the first member to the second member based on the data stored in the social graph. The function should _return_ one of these values depending on what is appropriate:**  
# - "follower", if `from_member` follows `to_member`
# - "followed by", if `from_member` is followed by `to_member`
# - "friends", if `from_member` and `to_member` follow each other
# - None if none of the above scenarios are applicable  
# 
# Specifications:  
# 1. `from_member` and `to_member` are user IDs (e.g. "@jobenilagan").
# 2. `social_graph` is a dictionary that adheres to the specification demonstrated in the demo cell.

# In[19]:


# CODE CELL
# PROBLEM 1

def relationship_status(from_member,to_member,social_graph):
    if to_member in social_graph.keys() and from_member in social_graph.keys():
        if to_member in social_graph[from_member]["following"] and from_member in social_graph[to_member]["following"]: 
            return "friends"
        elif to_member in social_graph[from_member]["following"]:
            return "follower"
        elif from_member in social_graph[to_member]["following"]:
            return "followed by"
        else:
            return None
        
    elif from_member in social_graph.keys() and to_member not in social_graph.keys():
        if to_member in social_graph[from_member]["following"]:
            return "follower"
        else:
            return None
        
    elif to_member in social_graph.keys() and from_member not in social_graph.keys():
        if from_member in social_graph[to_member]["following"]:
            return "followed by"
        else:
            pass
        
    elif from_member not in social_graph.keys() and from_member not in social_graph.keys():
        return None
    
relationship_status("@joaquin","@chums",social_graph)


# ## Problem 2: Tic Tac Toe (10 points)  
# 
# Tic Tac Toe is a common paper-and-pencil game. Players must attempt to successfully draw a straight line of their symbol across a grid. The player that does this first is considered the winner.  
# 
# Here are several possible board configurations:

# In[9]:


# NON-INTERACTIVE CODE CELL. YOU MAY RUN THIS CELL, BUT DO NOT EDIT IT.
# FOR DEMONSTRATION PURPOSES ONLY. DO NOT EDIT.

board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]


# **Write a function called `tic_tac_toe` that takes one positional argument (list) `board`. The function should _return_ the winner of the board if there is one, and it should return `None` if there is no winner on the board.**  
# 
# Specifications:
# 1. Each player is represented by their symbol. Example: if the player using 'X' won the board, then simply return the string 'X'.
# 2. The board may be 3x3, 4x4, 5x5, or 6x6.
# 3. The game will only ever be player X vs player O. No other symbols will be used.
# 4. There may be no winner, and there may be 1 winner, but there will never be a situation where there is more than 1 winner.

# In[18]:


# CODE CELL
# PROBLEM 2

def tic_tac_toe(board):
    for h in board:
        if len(set(h)) == 1:
            return h[0]
        
    for v in [v for v in zip(*board)]:
        if len(set(v)) == 1:
            return v[0]
        
    if all([ud == "X" for ud in [board[i][i] for i,v in enumerate(board)]]):
        return "X"
    elif all([ud == "O" for ud in [board[i][i] for i,v in enumerate(board)]]):
        return "O"
    
    if all([du == "X" for du in [board[2-i][i] for i,v in enumerate(board)]]):
        return "X"
    elif all([du == "O" for du in [board[2-i][i] for i,v in enumerate(board)]]):
        return "O"
    
    else:
        return None
    
tic_tac_toe(board5)


# ## Problem 3: Routing (9 points)
# 
# During the pandemic, a shuttle van service is tasked to travel along a predefined circular route as follows:
# 
# - UP Diliman -> Ateneo de Manila (Estimated Time: 10 mins)
# - Ateneo de Manila -> De La Salle Taft (Estimated Time: 35 mins)
# - De La Salle Taft -> UP Diliman (Estimated Time: 55 mins)
# 
# The route is one-way only. So, the van cannot go back directly to UP Diliman from Ateneo de Manila; rather, it will have to drop by De La Salle Taft first before going to UP Diliman.
# 
# 

# In[11]:


# NON-INTERACTIVE CODE CELL. YOU MAY RUN THIS CELL, BUT DO NOT EDIT IT.
# FOR DEMONSTRATION PURPOSES ONLY. DO NOT EDIT.

legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}


# **Write a function called `eta` that takes three positional arguments: (dict) `legs`, (str) `source`, and (str) `destination`. The function should _return_ the estimated number of minutes it will take to reach the destination from the source based on the data stored in the `legs` dictionary.**  
# 
# Specifications:
# 1. The `legs` dictionary adheres to the schema followed in the demo cell.  
# 2. There may be more legs than shown in the demo cell.
# 3. Any destination can be reached from any source.

# In[22]:


# CODE CELL
# PROBLEM 3

def eta(legs,source,destination):
    if (source,destination) in legs.keys():
        return legs[(source,destination)]["travel_time_mins"]
    
    elif (source,destination) not in legs.keys():
        if source == destination:
            return 0
        elif source == "upd":
            return legs[("upd","admu")]["travel_time_mins"] + legs[("admu","dlsu")]["travel_time_mins"]
        elif source == "admu":
            return legs[("admu","dlsu")]["travel_time_mins"] + legs[("dlsu","upd")]["travel_time_mins"]
        elif source == "dlsu":
            return legs[("dlsu","upd")]["travel_time_mins"] + legs[("upd","admu")]["travel_time_mins"]
        
eta(legs,"upd","dlsu")


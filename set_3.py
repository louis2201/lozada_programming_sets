'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    from_follows_to = to_member in social_graph.get(from_member, {}).get("following", [])
    to_follows_from = from_member in social_graph.get(to_member, {}).get("following", [])
    
    if from_follows_to and to_follows_from:
        return "friends"
    elif from_follows_to:
        return "follower"
    elif to_follows_from:
        return "followed by"
    else:
        return "no relationship"

#Sample social graph data
social_graph = {
    "@bongolpoc": {"first_name": "Joselito", "last_name": "Olpoc", "following": []},
    "@joaquin": {"first_name": "Joaquin", "last_name": "Gonzales", "following": ["@chums", "@jobenilagan"]},
    "@chums": {"first_name": "Matthew", "last_name": "Uy", "following": ["@bongolpoc", "@miketan", "@rudyang", "@joeilagan"]},
    "@jobenilagan": {"first_name": "Joben", "last_name": "Ilagan", "following": ["@eeebeee", "@joeilagan", "@chums", "@joaquin"]},
    "@joeilagan": {"first_name": "Joe", "last_name": "Ilagan", "following": ["@eeebeee", "@jobenilagan", "@chums"]},
    "@eeebeee": {"first_name": "Elizabeth", "last_name": "Ilagan", "following": ["@jobenilagan", "@joeilagan"]},
}

# Examples testing functions
print(relationship_status("@joaquin", "@chums", social_graph))
print(relationship_status("@bongolpoc", "@chums", social_graph))  
print(relationship_status("@eeebeee", "@joeilagan", social_graph))     
print(relationship_status("@bongolpoc", "@joaquin", social_graph))


def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    size = len(board)

    for i in range(size):
        if all(cell == board[i][0] and cell != '' for cell in board[i]):
            return board[i][0] 
        if all(board[j][i] == board[0][i] and board[j][i] != '' for j in range(size)):
            return board[0][i]  
    
    if all(board[i][i] == board[0][0] and board[i][i] != '' for i in range(size)):
        return board[0][0]  
    if all(board[i][size-1-i] == board[0][size-1] and board[i][size-1-i] != '' for i in range(size)):
        return board[0][size-1]  
    
    return "NO WINNER"

#Sample boards
board1 = [['X','X','O'], ['O','X','O'], ['O','','X']]
board2 = [['X','X','O'], ['O','X','O'], ['','O','X']]
board3 = [['O','X','O'], ['','O','X'], ['X','X','O']]
board4 = [['X','X','X'], ['O','X','O'], ['O','','O']]
board5 = [['X','X','O'], ['O','X','O'], ['X','','O']]
board6 = [['X','X','O'], ['O','X','O'], ['X','','']]
board7 = [['X','X','O',''], ['O','X','O','O'], ['X','','','O'], ['O','X','','']]

#Examples testing functions
print(tic_tac_toe(board1))  
print(tic_tac_toe(board2))  
print(tic_tac_toe(board3))  
print(tic_tac_toe(board4))  
print(tic_tac_toe(board5))  
print(tic_tac_toe(board6))  
print(tic_tac_toe(board7))

def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    total_time = 0
    current_stop = first_stop
    
    while current_stop != second_stop:
        for (start, end), data in route_map.items():
            if start == current_stop:
                total_time += data["travel_time_mins"]
                current_stop = end
                break
    
    return total_time

#Sample routes
legs1 = {
    ("upd","admu"): {"travel_time_mins": 10},
    ("admu","dlsu"): {"travel_time_mins": 35},
    ("dlsu","upd"): {"travel_time_mins": 55}
}

legs2 = {
    ('a1', 'a2'): {"travel_time_mins": 10},
    ('a2', 'b1'): {"travel_time_mins": 10230},
    ('b1', 'a1'): {"travel_time_mins": 1}
}

#Examples testing functions
print(eta("upd", "dlsu", legs1)) 
print(eta("admu", "upd", legs1))
print(eta("a1", "b1", legs2))  
print(eta("a2", "a1", legs2))

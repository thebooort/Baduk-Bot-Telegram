#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 20:15:55 2018

@author: thebooort & espectro123
"""


def locate_group(board, group, x_coordinate, y_coordinate):

    """
    This function locate a whole group and place it in a vector

    Making a circle around our stone to search for other stones that are near
    it, all of them are stored in a vector.

    Parameters
    ----------
    board : array
        Array that contains the situations of our board
        
    group : vector
        Vector that contains all the stones that are in our group.
        If called for the first time, use a void vector
        
    x_coordinate : int
        X axes Position of the stone we are considerating in first place
        
    y_coordinate : int
       Y axes Position of the stone we are considerating in first place

    Returns
    -------
    group: vector
        Vector with all the stones in our group

    """
    color = board[x_coordinate, y_coordinate].color

    group.append([x_coordinate, y_coordinate])

    # TODO: we need something to check if we are in our limits, if not then
    # skip the step

    if board[x_coordinate+1, y_coordinate] == color and \
       [x_coordinate+1, y_coordinate] not in group:
        group.append([x_coordinate+1, y_coordinate])
        locate_group(board, group, x_coordinate+1, y_coordinate)

    if board[x_coordinate, y_coordinate+1] == color and \
       [x_coordinate, y_coordinate+1] not in group:
        group.append([x_coordinate, y_coordinate+1])
        locate_group(board, group, x_coordinate, y_coordinate+1)

    if board[x_coordinate-1, y_coordinate] == color and \
       [x_coordinate-1, y_coordinate] not in group:
        group.append([x_coordinate-1, y_coordinate])
        locate_group(board, group, x_coordinate-1, y_coordinate)  

    if board[x_coordinate, y_coordinate-1] == color and \
       [x_coordinate, y_coordinate-1] not in group:
        group.append([x_coordinate, y_coordinate-1])
        locate_group(board, group, x_coordinate, y_coordinate-1)    
    
    return group
    
    
def stone_surround(board, x_coordinate, y_coordinate):

    """
    This function tell us the surroundings of one stone. It counts liberties 
    of one stone, if there's one or more, the state is true.

    Parameters
    ----------
    board : array
        Array that contains the situations of our board
        
    x_coordinate : int
        X axes Position of the stone we are considerating in first place
        
    y_coordinate : int
       Y axes Position of the stone we are considerating in first place
        
    Returns
    -------
    state: boolean
        boolean, True: if there is any liberties, False: if not

    """  
    
    state = False
    count = 0
    
    if board[x_coordinate+1, y_coordinate].color == void:
        count += 1
    if board[x_coordinate-1, y_coordinate].color == void:
        count += 1
    if board[x_coordinate, y_coordinate+1].color == void:
        count += 1
    if board[x_coordinate, y_coordinate-1].color == void:
        count += 1
  
    if count >= 1:
        state = True

    return state



def is_this_group_alive(board, group):
    
    """
    This function tell us if our group is alive, it follow all the 
    elements in a vector and store in a vector if stone has liberties or not.
    Then it check if there is any liberty (that means, if there is any True), 
    if so, it returns True. If not the group is dead and it returns False.

    Parameters
    ----------
    board : array
        Array that contains the situations of our board
        
    group : vector
        Vector that contains all the stones that are in our group.
        If called for the first time, use a void vector
        
    Returns
    -------
    final_state: boolean
        boolean, True: if our group is alive, False: if our group is dead

    """    

    states = []
    final_state = False
    
    for stone in group:
        states.append(stone_surround(board, stone[1], stone[2]))
    if True in states:
        final_state = True

    return final_state
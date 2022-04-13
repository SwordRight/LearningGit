from turtle import st




def plant_recommendation(state):
    if state == 'low':
        print('first')
    elif state == 'medium':
        print('second')
    elif state == 'high':
        print('third')


plant_recommendation('low') # output -> first
plant_recommendation('medium') # output -> second
plant_recommendation('high') # output -> third
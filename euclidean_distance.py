#Some dummy data
critics={'Lisa Rose':{'Lady in the Water':2.5, 'Snakes on a Plane':3.5, 'Just My Luck': 3.0, 'Superman Returns':3.5,'You, Me and Dupree':2.5, 'The Night Listener':3.0},
        'Gene Seymour':{'Lady in the Water':3.0, 'Snakes on a Plane':3.5, 'Just My Luck':1.5, 'Superman Returns':5.0, 'The Night Listener':3.0, 'You, Me and Dupree':3.5},
        'Michael Phillips':{'Lady in the Water':2.5, 'Snakes on a Plane':3.0, 'Superman Returns':3.5, 'The Night Listener':3.0, 'You, Me and Dupree':4.0},
        'Claudia Puig':{'Snakes on a Plane':3.5, 'Just My Luck':3.0, 'Superman Returns':4.0, 'The Night Listener':3.0, 'You, Me and Dupree':2.5},
        'Mick LaSalle':{'Lady in the Water':3.0, 'Snakes on a Plane':4.0, 'Just My Luck':2.0, 'Superman Returns':3.0, 'The Night Listener':3.0, 'You, Me and Dupree':2.0},
        'Jack Matthews':{'Lady in the Water':3.0, 'Snakes on a Plane':4.0, 'The Night Listener':3.0, 'Superman Returns':5.0,'You, Me and Dupree':3.5},
        'Jack Matthews2':{'Lady in the Water':3.0, 'Snakes on a Plane':4.0, 'The Night Listener':3.0, 'Superman Returns':5.0,'You, Me and Dupree':3.5},         
        'Toby':{'Snakes on a Plane':4.5, 'Superman Returns':4.0, 'You, Me and Dupree':1.0}
        }


#This method uses the Euclidean distance method to calcuate the similarity between two people in a dataset
#The function takes three inputs:
#1. dataset in the schema presented above
#2. the two people that the similarity distance is of interest

#EUCLIDEAN DISTANCE METHOD
from math import sqrt

#returns a distance-based similarity score for person1 and person2

def sim_distance(prefs,person1,person2):
    # Get the list of shared_items
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1
    # if they have no ratings in common, return 0
    if len(si)==0: return 0
    
    #add up the squares of all of the differences
    sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2)
                       for item in si])
    return 1/(1+sqrt(sum_of_squares))
# In python and other programming languages developers (Like Phil and Jaleh) use other people's code to accomplish what they wish.
# When a developer wants to let other people use their code they create a package for their code called a module then they let others download that module on to their computer.
# When a module is downloaded onto a computer, that computer then has access to it and can use the whatever the module was created for. 
# In Python we import modules so that our project can use the code inside. 
import os
import glob
import pandas as pd
import time

# Variables are used to store information that we wish to reference throughout our project.
# For example, let's say I was creating a PacMan application and everytime PacMan ate food I wanted the words 'Nom Nom Nom' to appear.
# Then I would create a 'Variable' that contained the string 'Nom Nom Nom' and reference the variable name whenever I wanted those words to appear. 
pacman_says = 'Nom Nom Nom'
print('When I see food I {} it all down\n'.format(pacman_says))
time.sleep(5)

# This creates a variables of all the files we have in the `games` folder that end in `.EVE`
# A variable can be a raw/base type which are simple in nature, or an object which are complicated and created from mulitple simple types. 
game_files = glob.glob(os.path.join(os.getcwd(), 'games', '*.EVE'))

# ETL - Extract, Transform, Load
# This is one of the primary jobs of a Developer. 
# It is here that the incoming user data is massaged and readied for our systems consumption. 
# You may be curious to why we need to look and fix our clients code.. This is because in software development we can't trust anyone.
# This seems a little mean I know, but it's not because we don't trust everyone, it's because anyone could want to try and harm your system. 
# This way we treat everyone equally and assure that what they are giving us is what we expect. 
game_files.sort()
print('These are 5 of the files we found: {}\n'.format(game_files[:5]))
time.sleep(5)

# Variables live as long as they are in scope and a scope in python is defined by an indent (spaces before a line of text). 
# For example;
#             Scope1{
#                 Variable1 life begins
#                 Scope2{
#                      Variable2 life begins
#                      Variable2 life ends
#                 }
#                 Variable1 life ends
#             }
game_frames = []

# When we are working on a list of values we can cycle through them one at a time and isolate the value in the list we wish to work on.
for game_file in game_files:
    game_frame = pd.read_csv(game_file, names=['type', 'multi2', 'multi3', 'multi5', 'multi6', 'event'])
    # Each loop through our game_files list we extract and read another file and add its contents to our main scope 'games' variable
    game_frames.append(game_frame)
#-# QUESTION TIME #-# Based on the above code which variable will live past the for loop and which won't?
    #-----------#

# Now that the games_frames variable is full of all the data that was in the `games/` folder files we are ready to concatenate (join all the data together) it into a large variable called a `Dataframe`
games = pd.concat(game_frames)

# With the whole Dataframe now available to us it's time to clean up the values within.
# Let's look in our Dataframe at the column 'multi5' and lock our Dataframe to show us only entries with '??' as their value.
# This is an example of Extraction in ETL because we've limited what we are seeing to a specific view of the data. 
games.loc[games['multi5'] == '??', 'multi5'] == ''
print('These are the 5 top values from our `games` Dataframe:\n{}'.format(games[:5]))
time.sleep(5)

# Awesome work so far!
# Next let's seperate and rename the multi2 column in our games Dataframe so we can see the game_id's and the year they played.
identifiers = games['multi2'].str.extract(r'(.LS(\d{4})\d{5})')
identifiers = identifiers.fillna(method='ffill')
print('\nLook at the column names before we change them: \n{}'.format(identifiers[:5]))

# And rename the columns here
identifiers.columns = ['game_id', 'year']
print('\nNow look at the column names after: \n{}'.format(identifiers[:5]))

# This is some final clean up for my computer. It will free up a bit of space on our computers.
games = pd.concat([games, identifiers], axis=1, sort=False)
games = games.fillna(' ')
pd.Categorical(games['type'].iloc[:])

print('\nAnd finally we have a working Dataframe that contains meaningful and insightful data!\n{}'.format(games[:25]))


# Data means nothing unless it is telling a story. 

## Instructor Notes: 

Notes from Ryan: 
- solidify the narrative structure
    - in the beginning, we hypothesized A and worked on cleaning/etc...
    - in the middle, we discovered B
    - in the end, our takeaway is C
- simplify the executive summary slide
- recommend end w/ a slide of the team w/ portraits and links
- Typos and formatting, in need of some proof reading
- Features for modeling, perhaps they should have more human reading friendly names?

Biggest takeaway from instructor feedback:
1. Draw the line in the stand for messing with code
2. Need to create the story from the piles of discovery that we have
3. Make slides beautiful
4. Rename features


## Structure for or story Filled in
Goal (opening spiel):
We are the Racket Science team and our goal is to take data from the last 20 years of professional men's tennis and explore it to identify drivers of win. Using modern machine learning algorithms, we aim to predict the outcome of future matches. We are also delving into the career stats of Roger Federer whom some consider to be the best to ever play the game. We are discovering his drivers of greatness and comparing those drivers to his top rivals to see if he is truly unmatched or if he has been dethroned. We are also exploring the first 50 games of Federer and his rivals to determine if their rise to tennis fame could have been predicted early on. 

- Beginning. In the beginning, we hypothesized A
In the beginning, only one of use had domain knowledge of professional men’s tennis, but there are certain players that are so famous, even non-tennis heads are aware of them. Roger Federer is that kind of player. We hypothesized that he would be the best player to look at to determine what drives greatness. 
- and worked on cleaning/etc...
Before we could get into the project we had to clean and prep the data. We ran into a few issues: 
    - The dataset was extremely vast so we chose to only work with the last 20 years of ATP (Association of Tennis Professionals) men’s matches starting from 1999 and ending in 2019 since a lot of player’s rankings got messed up during COVID when they couldn’t play matches. 
    - Each row had a winner and loser instead of a player1 player2 and a column that listed who won. To amend this we randomized winner & loser as player1 and player2 alphabetically and set our target to player_1_wins (True or False) for binary classification.
    - There was noise in are target column due to walkovers, best of 1 matches,  and players retiring early in the match. We removed these matches from the dataset. 
    - We also filtered out players that played less than 50 matches. 
    - We filled missing match time lengths with average match length time for respective tournaments and dropped rows in other columns like height that contained nulls. 
 	-   There were no aggregated stats, just the stats from each match. We aggregated these stats together to find player averages. 
	-   The stats from each match can be used for exploration but not modeling, because we can’t model on future knowledge that we won’t have pre-match. For feature selection for modeling we had to narrow the scope to variables we would have access to pre-match like height, age, surface, and rank points, as well as engineer a few more custom features. 

 - Middle. in the middle, we discovered B

1. What drives win? 
Since our ultimate goal is modeling, our exploration starts with looking at the variables we would have access to pre-match like height, age, surface, and rank points, and identify which of these drive winning a match. 

To do this, separate the groups by wins / losses and then see if there is a significant difference between variables in that group. For example: I'll take all of the matches that player1 wins and get the mean rank points for player1 for that group then do the same for all of the matches where player1 loses. If there is a significant difference then height is likely a driver of winning and I can move forward with stats and visuals to confirm this theory. 

Variables we can know pre-match: Height, Age, Rank, Rank Points, Hand, Surface, Rounds, Levels. 
We discovered that height, age, rounds, and levels weren’t dependent on win. 
player_1_rank, player_1_rank_points, player_1_hand_R, player_1_hand_L, surface_Clay are all dependent on win. 

2. Roger Federer. Drivers of greatness. Show him compared to the average player. Driver of greatness could be a stat over a certain threshold. 

3. Roger Federer. Compare him against his rivals. Is he really the greatest current player? 

4. When they were young. Can greatness of the greatest be predicted? Look at Federer and his rivals when they were young and see if they had those drivers of greatness then. 

 - End. in the end, our takeaway is C


## Slide Ideas and structure: 

Cover slide:

Slide of the team (photos):

Data Science pipeline slide:

Acquire and prepare slide: 

Explore slides (idea of layout): 

    - What drives win? 

    - Roger Federer. Drivers of greatness. Show him compared to the average player. Driver of greatness could be a stat over a certain threshold. 

    - Roger Federer. Compare him against his rivals. Is he really the greatest current player? 

    - When they were young. Can greatness of the greatest be predicted? Look at Federer and his rivals when they were young and see if they had those drivers of greatness then. 

Model Slide:

Conclusion Slide:

Next Steps Slide:

Links Slide: 



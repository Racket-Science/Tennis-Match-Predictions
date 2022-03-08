
# Data means nothing unless it tells a story. 

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


## Structure for our story Filled in
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

5. Modeling

 - End. in the end, our takeaway is C


## Slide Ideas and structure: 

Slide Presentastion Break-down: 


Alejandro - Intro: 
    - Introduce the team 
    - Game Plan of project
    - Executive Summary
    - Explain the game of tennis

Mason - Acuisition & Preparation
    - steps to acquire
    - steps to prepare
    - problems and resolutions

Daniel - Exploration 
    - What drives win? 
    - Roger Federer. Drivers of greatness. Show him compared to the average player. Driver of greatness could be a stat over a certain threshold. 
    - Roger Federer. Compare him against his rivals. Is he really the greatest current player? 
    - when they were young. Can greatness of the greatest be predicted? Look at Federer and his rivals when they were young and see if they had those drivers of greatness then. 

Chloe - Modeling
    - prepare
    - models
        - baseline
        - no_upset model 
        - best model accuracy (train & validate)
    - explain how best model works
    - best model on test data

Alejandro - Conclusion 
    - What did we learn from all this? 
    - What else can this be applied to? 

## Script: 

Alejandro - Intro

#########################################################

Mason - Acuisition & Preparation

#########################################################

Daniel - Exploration 

    SLIDE 1:
        - We first asked, what attributes can correctly predict a match outcome? Using exploration and statistical testing we focused on these key features.  We found that there is no significant difference on either height or age in predicting an outcome and within court surface type of carpet, clay, grass, and hard – only clay showed to be an indicator.

    SLIDE 2:
        - Beyond, looking at the features to predict a match outcome, we wanted to also explore what are the Drivers of Greatness for a player to succeed in their career.  Aggregating the stats of the 13 players that reached Rank 1, compared to the other 269 other players, we discovered:

        Aces & Breakpoint per match along with First Serve Win % were the primary attributes.
        While Second Serve Win %, Grass & Hard Surface Performance, and low double fault % served as secondary features

        As we put weight on these features, we concluded that Roger Federer is the greatest tennis player within this time. This discovery was attributed to being in the top 3 of all player attributes.

    SLIDE 3:
        - We explored Federer’s career over the past two decades and it has been nothing but spectacular, highlighting a 74%-win rate on players ranked 30 or higher and winning a total of 20 grand slams

    SLIDE 4:
                (viz - 5 seconds or delete it)

    SLIDE 5: 
        -He has had many rivalries over the years which has produced the finest tennis matches of all time.

        As you can see many players have a higher record then him, including Rafael Nadal who has him beat 9-3 on Clay which is preferable surface for defensive players.

        Still though his performance in the key metrics of greatness, makes him the best player within this twenty-year time span

    SLIDE 6:

        Looking at Federer and his rivals, we asked can greatness be predicted at an early age? Is it natural talent or an evolution through one’s career?

        Aggregating all players first 50 matches, we concluded that it is extremely difficult to predetermine future champions.  We found trends in predicting top 30 players but within Federer and his 4 rivalries only one of which stood out beyond the mean.  Federer, performed within the average in aces and breakpoints, while performing very low in first serve win%, a high loss rate against ranked opponents, and high double fault percentage.

    SLIDE 7:

        In Conclusion:

    - We discovered that height and age play no significant difference in match predictions 
    - Drivers of Greatness are based on Aces, Breakpoints, & First Serve Win %
    - Only Clay surface type is significant for prediction – also as expressed in Feder’s Rivals
    - We believe that greatness comes with experience rather than talent – Age is not a factor

    Next, we have Chloe to talk about our modeling

#########################################################

Chloe - Modeling

    Thanks Daniel. 

    Model Outline

    Our modeling process to predict match winners is as follows: 
    - We prepared the data for modeling
    - Created the Baseline to compare our models against
    - Created a model based on no upsets
    - Created several classification models evaluating on train and validate before choosing the best one
    - And finally evaluated on the test dataset


    Prepare

    - The first step is to prepare. 
    - We separated the data into X and Y where the X represents the features that drive player1 to win, and the y represents the target variable that we are trying to predict which is player_1_wins. This reduces the 91 columns in our dataset down to 7.

    Baseline

    - Before creating our classification models, we created a baseline to compare them to based on assuming player 2 will win, since player 2 wins most often in this dataset. 
    - The baseline accuracy is 51%. 

    No Upset Model

    - To improve on the baseline we created a model based on the assumption that there will be no upsets, and that the highest ranked player will win the match. 
    - This might seem like a simple model, however it will actually be tough to beat since it is based off a player’s rank they got through winning tournaments and racking up rank points. The best indication we have that a player will win in the future is that they’ve done so consistently in the past. 
    - The accuracy for this model is 64%. 

    Features Model 

    - To try to improve on this model, we built several decision tree, random forest and logistic regression models with varying parameters using the features we identified as drivers of win.
    - The model that preformed the best was the random forest model with an accuracy of 66% on train and 64% on validate.

    Random Forest Model 

    - I’ll now explain how our model works. 
    - A  random forest model is made up of many decision trees. In classification modeling, the objective is to determine which class an observations fits into. To do this, a decision tree chooses the features that effect the target the most, and asks true false questions until a conclusion is reached. 
    - Many decision trees that use random features and samples make up the random forest model. After each tree has come to its conclusion, the model selects the most common outcome amongst all of the tress as the final decision for the random forest. 

    Feature Importance

    - The features that our Model found to be most important in predicting player 1 winning were: 
        - player1_rank_diff
        - player1_rankpoints
        - Clay
        - h2h_1
        - h2h_2

    Evaluate on Test

    - Finally, to test our best model on unseen data, we evaluated the random forest on the test dataset. 
    - Our model predicts the winner accurately 64% of the time.
    - This is the same accuracy as our upset model but beats our baseline by 25%. 

    Alejandro will now wrap up the presentation with our conclusion. 

    (2 mins, 30 secs)

#########################################################

Alejandro - Conclusion 

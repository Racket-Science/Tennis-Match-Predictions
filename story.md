## Script: 

Alejandro - Intro

Like most of the world, Team Racket Science loves sports, both watching and predicting the outcome. As data scientists we believe that we can leverage machine learning techniques to help predict the victor. We have used 20 years of pre pandemic Association of Tennis Professionals data to predict the outcome of a tennis match between two tennis players.

--------------

Now let me introduce you to team Racket Science
My names is Alejandro Velasquez,
Mason Sherbondy
Daniel Northcutt
And Chloe Whitaker 

-------------

For today's agenda, I will give you an executive summary, a quick intro to the game of tennis,
and tell you about our gameplan

After me, Mason will tell you about the work that went in to acquiring and preparing our data

Daniel will talk about the exploratory work the team did

And the Chloe will let you know how we defined our baseline and created our predictive model

At the end, I will discuss our conclusions with you 


----------------

Our team stabilized 2 main goals:

Predict the outcome of a match and 
discover what makes a player great. 
To accomplish our second goal, we focused on Roger Federer,one of the modern greats of tennis.

To do so we We asked ourselves 
What drives the success of a player
And Is Roger Federer one of the best of the last 20 years?

In our journey we found that 

Top players will win a lot of break points

Will ace their opnets a lot 

and win their first serve points 
 

-----------------

For our project we followed the 6 steps of the data science pipeline.

We planned using Trello 

We acquired our data using python and Github

To prepare our data we used Jupyter Notebooks, pandas and Numpy 

To learn about our data we leveraged jupyter notebooks with seaborn and matplotlib

For modeling we used scikit learn 

And deliver this presentation using google slides and slidesgo

----------------------------

Tennis is played between two players who stand on opposite ends of the court

 One serves and the other receives

The serving player will stand behind the baseline and attempt to serve the ball from the “deuce” half of the court to the opponent’s deuce half. 

The ball should hit the service box in the opponent’s court, for the point to play out.

When a service is returned, the ball most land in the highlighted area for the game to go on. 

If the player who is returning the ball lets the ball bounce two times before returning it, the opposite player wins the point.

A tennis match is made up of Sets. Sets are made up of Games and Games are made up from points. The goal of a tennis match is to win more sets than your opponent in a best of 3 sets or a best of 5 sets escenario. 


Up next Mason will share with you how we acquired and prepared over 100,000 rows of data 


#########################################################

Mason - Acuisition & Preparation

Thank you Alejandro.

#Acquire Slide

- To begin our wrangle, we simply cloned Jeff Sackmann's repository for the men's tennis tour on Github, a code hosting platform for version control and collaboration.

- After we cloned the repository, we were ready to prepare the data in our Jupyter Notebooks

#Prepare Slide

-First, we combined all of our .csv files in one dataframe.

- The data was largely in the format we needed, which is all of the match statistics as well as biographical information for both players, except the players were designated as winner and loser

-Since our goal was to develop a model to predict the winner of tennis matches, we renamed the winner and loser columns as player 1 and player 2, and we balanced the dataset by randomizing the order of winners so that player 1 and player 2 had a similar chance of being the winner. We then created a boolean mask that declared whether or not player 1 won the match. This was our target variable

- Because the pandemic has curbed top player participation, and because we wanted our data to represent the heart of men's tennis, we limited our data to the years 1999 - 2019, and we dropped all records that involved players who played less than 50 matches. Our data now represented the heart of the game.

-To clean the data, we renamed columns, filled missing values and encoded categorical features for modeling

- Now that our data was clean, the biggest problem we faced in preparing the data was most of our features were post-match accounts. We cannot base a pre-match prediction for a matchup based on features that are generated during the match. 

-So, since we were really looking for drivers of winning, we decided to navigate our major feature problem through feature engineering, and we decided to explore drivers of greatness as well.

- We set our feature focus on aggregated statistics. A feature we created for the problem was head 2 head stats, which is a rolling aggregate record of wins for each player matchup.

-And in order to explore drivers of greatness, we created a player dataset based on aggregated career stats for any players in our data who achieved a rank of 100 or higher, and we focused on Roger Federer and his top rivals.

- This sums up our wrangling process. I will now hand you over to Daniel, who will go over our findings in this project.

#########################################################

Daniel - Exploration 

SLIDE 1:
 - We first asked, what attributes can correctly predict a match outcome? Using exploration and statistical testing we focused on these key features.  We found that there is no significant difference on either height or age in predicting an outcome and within court surface type of carpet, clay, grass, and hard – only clay showed to be an indicator.

SLIDE 2:
- Beyond, looking at the features to predict a match outcome, we wanted to also explore what are the Drivers of Greatness for a player to succeed in their career.  Aggregating the stats of the 13 players that reached Rank 1, compared to the other 269 other players, we discovered:

Aces & Breakpoint per match along with First Serve Win % were the primary attributes.
While Second Serve Win %, Grass & Hard Surface Performance, and low double fault % served as secondary features

SLIDE 3: 
As we put weight on these features, we concluded that Roger Federer is the greatest tennis player within this time. This discovery was attributed to being in the top 3 of all player attributes.

SLIDE 4:
- We explored Federer’s career over the past two decades and it has been nothing but spectacular, highlighting a 74%-win rate on players ranked 30 or higher and winning a total of 20 grand slams
    
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

Thank you Chloe,

In conclusion

Higher rank players will beat their opponents about 64% of the time. Meaning greatness is thought to beat, even for ML 

Roger is has a winning record of 82% 

And greatness comes from experience, in reality age is not a factor 

With more time we would:

Engineering aggregate features-by-date to improve prediction

-------------------

Thank you for your attention, I hope our time with you was insightful. 


--------------------

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


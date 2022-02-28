
# Tennis Match Prediction

##  About the Project

### Project Goals

    Our goal is to make a tennis match predictor that will take in two players and return the predicted winner. 

### Project Description 

 Throughout the history of tennis, there have been matches and players who have captivated fans.  Using data from the last 20 years and modern machine learning algorithms, our team aims to predict the outcome of matches based on the players’ statistics and data of their professional matches.

### Initial Questions

    I. Does a difference in career average break points saved impact victory?

    II. Does a difference in career average break points won impact victory?

    III. Does a difference in career percent-of-break-points-won impact victory?

    A. What are the drivers that determine a change in the dynamic between two players? Is there anything in our data set to suggest a change in dynamic?

    B. How do key rivalries play out in best of 3 matches vs best of 5? Do rivalries take a different story at Grand Slam events?

    C. How do key rivalries play out on clay? On grass? On hard court?

### Data Dictionary
    A list of the variables in the dataframe and their meaning. 

| -------------- | --------- |------------------------ |
| Variable       | Datatype| Description               |
| -------------- | --------- |------------------------ |
|player_1_wins   |           | Target variable. Indicates if person  classified as player one has won the game|
| PlayerID    |int64|Unique player identification| 
|Player Name|object|Represents the players name| 
|Age|float64|                         | 
|Height|float64|Represents the height of the player| 
|MaxRank|float64|Maximum rank achieved by player in the length of our database| 
|Hand|object|Represents dominant hand of player R = right, L = left| 
|Country|object|Country of descendants of the player| 
|win_count|float64|Number of wins for the for the period of time of our database|
|lose_count|float64|Number of losses for the period of time of our database| 
|match_count|float64|Total matches just played for the period of time of our database| 
|win%|float64|Total wins divided by the sum of losses and wins| 
|aces_in_match_lost|float64|Times rival answers first serve| 
|aces_in_match_won|float64|Times player serving the ball gets a point without the contest of rival| 
|ace_count|float64|Total count of aces for the period of time of our database| 
|aces_per_game|float64|Count of aces in a game| 
|first_serve_percentage_match_lost|float64|                         | 
|first_serve_percentage_match_won|float64|                         | 
|first_serve_won_percentage_match_lost|float64|                         | 
|first_serve_won_percentage_match_won|float64|                         | 
|breakpoints_won_match_lost|float64|                         | 
|breakpoints_won_match_won|float64|                         | 
|breakpoint_count|float64|Total count of all breakpoints for the period of time of our database| 
|breakpoints_per_game|float64|Total count of brakpoints in a game| 
|win_count_30|float64|| 
|loss_count_30|float64|                         | 
|win_count_100|float64|                         | 
|loss_count_100|float64|                         | 
|total_top30_matches|float64|                         | 
|total_top100_matches|float64|                         | 
|top_30_win%|float64|                         | 
|top_100_win%|float64|                         | 
|tourney_level|uint8|                         | 
|best_of|int64|                         | 
|player_1|string|Name of player one| 
|player_2|sring|Name of player two| 
|player_ioc|object|                         | 
|player_rank|float64|Rank of player at the time of match| 
|player_1_wins|bool|                         | 
|round|object|                         | 
|surface|object|Represents the type of material the floor of the court is made of| 
|ht_diff|float64|Hight difference between players| 
|age_diff|float64|Age difference at the time of match| 
|rank_diff|float64|Rank difference at the time of match| 
|rank_points_diff|float64|Rank points difference at the time of match| 
|winner_rank|float64|Rank of winner| 
|loser_rank|float64|Rank of looser

  

### Steps to Reproduce 

        1. Clone this repo containing the Final_Report as well as the helper files.
        2. Create a .gitignore with .csv listed to prevent pushing any large CSVs to github. 
        3. That should be all you need to do run the Final_Report!

### The Plan 
        - Planning
            - Create a Trello board
            - Creare chats on slack and discord for team engagement
            - Gain domain knowledge
        - Wrangle (Acquire and Prepare)
            - Create wrangle.py with functions for aquiring and prepping the data
        - Explore
            - ask initial questions of the data
            - answer questions with visuals and statistics 
        - Model
            - for mvp (features: )
            - target : outcome (win/loss)
            - 3 best models
            - on best model provide visuals of how it preformed on the test sample

        - Refine (Report)
            - state what states and counties the homes are located in (fips)
            - project overview, goals, initial questions conclusion (did reach goal?, key findings, recommendations, and next steps)
            - Make sure markdown is clear on it's own.
            - Make sure all code is commented out. 

        - Deliver
            - README.md
            - Wrangle.py
            - working notebook(s)
            - report notebook
            - presentaion of report notebook

## Conclusion:


## With more time...

# License Information

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Dataset" property="dct:title" rel="dct:type">Tennis databases, files, and algorithms</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="http://www.tennisabstract.com/" property="cc:attributionName" rel="cc:attributionURL">Jeff Sackmann / Tennis Abstract</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.<br />Based on a work at <a xmlns:dct="http://purl.org/dc/terms/" href="https://github.com/JeffSackmann" rel="dct:source">https://github.com/JeffSackmann</a>.

In other words: Attribution is required. Non-commercial use only.

[1] http://www.tennisabstract.com/charting/meta.html

[2] http://www.tennisabstract.com/charting/meta.html#contributors
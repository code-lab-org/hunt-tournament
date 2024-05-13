# CoDe Lab 2021 Hunting Tournament

## Introduction

In 1979, Robert Axelrod organized a computational tournament to study strategies for the Prisoner's Dilemma game [1]. He solicited 14 entrants plus a random strategy and conducted a round-robin (all-plays-all) tournament with 200 iterations per pair. Surprisingly, one of the simplest strategies, called "TIT FOR TAT," submitted by Anatol Rapaport was victorious. In 1980, Axelrod organized a second tournament, soliciting participation from 62 entrants with full knowledge of the first tournament results [2]. It was conducted in a similar manner but with a 0.00346 probability of ending on any given iteration (i.e., the expected median is 200 iterations). Again, "TIT FOR TAT" was the winning strategy.

Discussion over the past 40 years has explored and extended Axelrod's tournaments, creating a new area of research on computational models of evolutionary behavior under social dilemmas. However, I was unable to find an exact analog for Stag Hunt games which I believe to capture a key strategic dynamic in engineering systems problems [3]. Furthermore, research developed in the Collective Design Lab proposes a more detailed bi-level game with both upper-level strategic decisions and lower-level design decisions, mirroring the types of decisions facing engineering systems [4]. How might computational strategies of 2020 fare in this extended Stag Hunt game?

## Technical Details

Review the [source code repository](https://github.com/code-lab-org/hunt-tournament) for more information on the Python API.

## Quick Start

 I have prepared a [Python code repository](https://github.com/code-lab-org/hunt-tournament) to help conduct the tournament. For a quick start, run the `main-example.ipynb` file which conducts a tournament with two games and three players. The two games include:
 * Single-level game with payoffs: 2 (00), 3 (01), 0 (10), and 4 (11) for strategies (ij) selected by players i and j.
 * Bi-level game with four designs and payoffs for strategies (ij) selected by the two players:
   - 0 (00), 0 (01), 0 (10), and 4 (11)
   - 1 (00), 1 (01), 1.5 (10), and 3.5 (11)
   - 1 (00), 1 (01), 0 (10), and 2 (11)
   - 2 (00), 3 (01), 0 (10), and 0 (11)

The three players include:
 * `Player`: always chooses strategy 0 and design 0. This is the default player defined in the `hunt/game.py` file.
 * `RandomPlayer`: chooses strategies and designs randomly. This is an extended player defined in the `hunt/player.py` file.
 * `MirrorPlayer`: always chooses the opponent's prior strategy/design decisions. This is an extended player with internal state defined in the `hunt/player.py` file.

The `main-example.ipynb` script conducts a round-robin (all-plays-all) tournament with six matches, each with the two games, and each game repeated 200 iterations. The results report the average score per game for each player. More detailed results stored within the tournament record the average score for each matchup, each game, and each replication.

## References
1.	Robert Axelrod (1980). "Effective Choice in the Prisoner's Dilemma," The Journal of Conflict Resolution, vol. 24, no. 1, pp. 3-25. URL: http://www.jstor.org/stable/173932
2.	Robert Axelrod (1980). "More Effective Choice in the Prisoner's Dilemma," The Journal of Conflict Resolution, vol. 24, no. 3, pp. 379-403. DOI: 10.1177/002200278002400301
3.	Paul T. Grogan and Ambrosio Valencia-Romero (2019). "Strategic Risk Dominance in Collective Systems Design," Design Science, vol. 5, no. e24. DOI: 10.1017/dsj.2019.23
4.	Ambrosio Valencia-Romero and Paul T. Grogan (2020). " Structured to Succeed? Strategy Dynamics in Engineering Systems Design and Their Effect on Collective Performance," Journal of Mechanical Design, vol. 142, no. 12, p. 121404. DOI: 10.1115/1.4048115
5. David Schmidt, Robert Schupp, James M. Walker, and Elinor Ostrom (2003). "Playing safe in coordination games: the roles of risk dominance, payoff dominance, and history of play," Games and Economic Behavior, vol. 42, pp. 281-299. DOI: 10.1016/S0899-8256(02)00552-3

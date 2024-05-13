#!/usr/bin/env python

import numpy as np
import scipy.stats as stats

from hunt.game import Player, Decision

class RiskDominancePlayer(Player):
    def __init__(self, game):
        super().__init__(game, "selten")

    def get_decision(self):
        with np.errstate(invalid='ignore'):
            independent_value = [
                self.game.get_payoff(
                    Decision(0, design),
                    Decision(0)
                ) for design in range(len(self.game.designs))
            ]
            independent_design = np.nanargmax(independent_value)
            risk_dominance = np.array([
                np.log(
                    (
                        self.game.get_payoff(
                            Decision(0, independent_design),
                            Decision(0)
                        ) - self.game.get_payoff(
                            Decision(1, design),
                            Decision(0)
                        )
                    ) / (
                        self.game.get_payoff(
                            Decision(1, design),
                            Decision(1)
                        ) - self.game.get_payoff(
                            Decision(0, independent_design),
                            Decision(1)
                        )
                    )
                ) for design in range(len(self.game.designs))
            ])
            collaborative_value = [
                self.game.get_payoff(
                    Decision(1, design),
                    Decision(1)
                ) for design in range(len(self.game.designs))
            ]
            collaborative_design = np.argmax(collaborative_value*(risk_dominance<0))
            if np.nanmin(risk_dominance) < 0:
                return Decision(1, collaborative_design)
            else:
                return Decision(0, independent_design)

class ExpectedValuePlayer(Player):
    def __init__(self, game, prior_collab=1, prior_no_collab=1):
        super().__init__(game, "economic")
        self.strategy_prior = np.array([prior_no_collab, prior_collab])

    def report_result(self, result):
        self.strategy_prior[result.their_decision.strategy] += 1

    def get_decision(self):
        p_collab = stats.beta(
                self.strategy_prior[1], 
                self.strategy_prior[0]
            ).mean()
        
        independent_expected_value = np.array([
                self.game.get_payoff(
                    Decision(0, design),
                    Decision(1)
                ) * p_collab + self.game.get_payoff(
                    Decision(0, design),
                    Decision(0)
                ) * (1-p_collab)
                for design in range(len(self.game.designs))
            ])
        independent_design = np.nanargmax(independent_expected_value)
        
        collab_expected_value = np.array([
                self.game.get_payoff(
                    Decision(1, design),
                    Decision(1)
                ) * p_collab + self.game.get_payoff(
                    Decision(1, design),
                    Decision(0)
                ) * (1-p_collab)
                for design in range(len(self.game.designs))
            ])
        collaborative_design = np.argmax(collab_expected_value)
        
        if np.all(collab_expected_value < independent_expected_value[independent_design]):
            return Decision(0, independent_design)
        else:
           return Decision(1, collaborative_design)

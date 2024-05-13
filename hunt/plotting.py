import matplotlib.pyplot as plt
import numpy as np

def plot_strategy_profile(ax, tournament, game, player_1, player_2):
    ax.step([i for i in range(tournament.num_reps)], 
             [
                 rep.get('player_1').get('strategy') 
                 for rep in tournament.rep_results
                 if rep.get('game') == game 
                     and ( (rep.get('player_1').get('name') == player_1
                            and rep.get('player_2').get('name') == player_2)
                          or (rep.get('player_2').get('name') == player_1
                              and rep.get('player_1').get('name') == player_2) )
             ], label=player_1, where='post', lw=0.5
         )
    ax.step([i for i in range(tournament.num_reps)], 
             [
                 rep.get('player_2').get('strategy') 
                 for rep in tournament.rep_results
                 if rep.get('game') == game 
                     and ( (rep.get('player_1').get('name') == player_1
                            and rep.get('player_2').get('name') == player_2)
                          or (rep.get('player_2').get('name') == player_1
                              and rep.get('player_1').get('name') == player_2) )
             ], label=player_2, where='post', lw=0.5
         )
    ax.set_xlabel('Replication')
    ax.set_ylabel('Strategy')
    ax.set_yticks([0,1])
    ax.legend(loc='best')
    
def plot_design_profile(ax, tournament, game, player_1, player_2):
    ax.step([i for i in range(tournament.num_reps)], 
             [
                 rep.get('player_1').get('design') 
                 for rep in tournament.rep_results
                 if rep.get('game') == game 
                     and ( (rep.get('player_1').get('name') == player_1
                            and rep.get('player_2').get('name') == player_2)
                          or (rep.get('player_2').get('name') == player_1
                              and rep.get('player_1').get('name') == player_2) )
             ], label=player_1, where='post', lw=0.5
         )
    ax.step([i for i in range(tournament.num_reps)], 
             [
                 rep.get('player_2').get('design') 
                 for rep in tournament.rep_results
                 if rep.get('game') == game 
                     and ( (rep.get('player_1').get('name') == player_1
                            and rep.get('player_2').get('name') == player_2)
                          or (rep.get('player_2').get('name') == player_1
                              and rep.get('player_1').get('name') == player_2) )
             ], label=player_2, where='post', lw=0.5
         )
    ax.set_xlabel('Replication')
    ax.set_ylabel('Design')
    ax.set_yticks(range(len(tournament.games[game].designs)))
    ax.legend(loc='best')
    
def plot_payoff_profile(ax, tournament, game, player_1, player_2):
    ax.step([i for i in range(tournament.num_reps)], 
             [
                 rep.get('player_1').get('payoff') 
                 for rep in tournament.rep_results
                 if rep.get('game') == game 
                     and ( (rep.get('player_1').get('name') == player_1
                            and rep.get('player_2').get('name') == player_2)
                          or (rep.get('player_2').get('name') == player_1
                              and rep.get('player_1').get('name') == player_2) )
             ], label=player_1, where='post', lw=0.5
         )
    ax.step([i for i in range(tournament.num_reps)], 
             [
                 rep.get('player_2').get('payoff') 
                 for rep in tournament.rep_results
                 if rep.get('game') == game 
                     and ( (rep.get('player_1').get('name') == player_1
                            and rep.get('player_2').get('name') == player_2)
                          or (rep.get('player_2').get('name') == player_1
                              and rep.get('player_1').get('name') == player_2) )
             ], label=player_2, where='post', lw=0.5
         )
    ax.set_xlabel('Replication')
    ax.set_ylabel('Payoff')
    ax.legend(loc='best')

def plot_panel(tournament, player_1, player_2):
    match = [ m for m in tournament.match_results 
             if (m.get('players')[0].get('name') == player_1 
                 and m.get('players')[1].get('name') == player_2)
             or (m.get('players')[0].get('name') == player_2 
                 and m.get('players')[1].get('name') == player_1) ][0]
    score_1 = match.get('players')[0].get('score') if match.get('players')[0].get('name') == player_1 else match.get('players')[1].get('score')
    score_2 = match.get('players')[0].get('score') if match.get('players')[0].get('name') == player_2 else match.get('players')[1].get('score')
    fig, axs = plt.subplots(3, len(tournament.games), sharex=True, figsize=(3*len(tournament.games),7))
    fig.suptitle('{:s} ({:.2f}) vs. {:s} ({:.2f})'.format(player_1, score_1, player_2, score_2))
    for game in range(len(tournament.games)):
        ax0 = axs[0,game] if len(tournament.games) > 1 else axs[0]
        ax1 = axs[1,game] if len(tournament.games) > 1 else axs[1]
        ax2 = axs[2,game] if len(tournament.games) > 1 else axs[2]
        ax0.set_title('Game {:d}'.format(game+1))
        plot_strategy_profile(ax0, tournament, game, player_1, player_2)
        ax0.set_xlabel(None)
        if game > 0: ax0.set_ylabel(None)
        plot_design_profile(ax1, tournament, game, player_1, player_2)
        ax1.set_xlabel(None)
        if game > 0: ax1.set_ylabel(None)
        plot_payoff_profile(ax2, tournament, game, player_1, player_2)
        if game > 0: ax2.set_ylabel(None)

def plot_strategy_pie(ax, tournament, game, player_1, player_2):
    values = np.array([np.sum(np.array([
                rep.get('player_1').get('strategy') 
                if rep.get('player_1').get('name') == player_1 
                else rep.get('player_2').get('strategy') 
                for rep in tournament.rep_results
                if rep.get('game') == game 
                    and ( (rep.get('player_1').get('name') == player_1
                           and rep.get('player_2').get('name') == player_2)
                         or (rep.get('player_2').get('name') == player_1
                             and rep.get('player_1').get('name') == player_2) )
            ]) == i)/tournament.num_reps for i in range(2)])
    labels = np.array(['$s_{:d}$'.format(i) for i in range(2)])
    ax.pie(values, labels=labels, autopct='%1.0f%%')
    ax.set_ylabel(player_1)

def plot_design_pie(ax, tournament, game, player_1, player_2):
    values = np.array([np.sum(np.array([
                rep.get('player_1').get('design') 
                if rep.get('player_1').get('name') == player_1 
                else rep.get('player_2').get('design') 
                for rep in tournament.rep_results
                if rep.get('game') == game 
                    and ( (rep.get('player_1').get('name') == player_1
                           and rep.get('player_2').get('name') == player_2)
                         or (rep.get('player_2').get('name') == player_1
                             and rep.get('player_1').get('name') == player_2) )
            ]) == i)/tournament.num_reps for i in range(len(tournament.games[game].designs))])
    labels = np.array(['$d_{:d}$'.format(i) for i in range(len(tournament.games[game].designs))])
    ax.pie(values, labels=labels, autopct='%1.0f%%')
    ax.set_ylabel(player_1)

def plot_pie_panel(tournament, player_1, player_2):
    match = [ m for m in tournament.match_results 
             if (m.get('players')[0].get('name') == player_1 
                 and m.get('players')[1].get('name') == player_2)
             or (m.get('players')[0].get('name') == player_2 
                 and m.get('players')[1].get('name') == player_1) ][0]
    score_1 = match.get('players')[0].get('score') if match.get('players')[0].get('name') == player_1 else match.get('players')[1].get('score')
    score_2 = match.get('players')[0].get('score') if match.get('players')[0].get('name') == player_2 else match.get('players')[1].get('score')
    fig, axs = plt.subplots(4, len(tournament.games), sharex=True, figsize=(3*len(tournament.games),12))
    fig.suptitle('{:s} ({:.2f}) vs. {:s} ({:.2f})'.format(player_1, score_1, player_2, score_2))
    for game in range(len(tournament.games)):
        ax0 = axs[0,game] if len(tournament.games) > 1 else axs[0]
        ax1 = axs[1,game] if len(tournament.games) > 1 else axs[1]
        ax2 = axs[2,game] if len(tournament.games) > 1 else axs[2]
        ax3 = axs[3,game] if len(tournament.games) > 1 else axs[3]
        ax0.set_title('Game {:d}'.format(game+1))
        plot_strategy_pie(ax0, tournament, game, player_1, player_2)
        if game > 0: ax0.set_ylabel(None)
        plot_strategy_pie(ax1, tournament, game, player_2, player_1)
        if game > 0: ax1.set_ylabel(None)
        plot_design_pie(ax2, tournament, game, player_1, player_2)
        if game > 0: ax2.set_ylabel(None)
        plot_design_pie(ax3, tournament, game, player_2, player_1)
        if game > 0: ax3.set_ylabel(None)
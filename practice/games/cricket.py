import sys
import random
import re


def get_valid_name(prompt):
    pattern = re.compile(r'^[A-Za-z0-9 ]+$')
    while True:
        name = input(prompt).strip()
        if name and pattern.match(name):
            return name
        print("Name is not valid")


def main():
   
    # team names
    team_names = [get_valid_name(f"Name of Team {i+1}: ") for i in range(2)]
    
    # number of players per team
    while True:
        try:
            players_per_team = int(input("Players per team: "))
            if 3 <= players_per_team <= 11:
                break
            else:
                print("Please enter a number of players between 3 and 11 (inclusive).")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # scorcards and totals for both teams
    scorecards = []
    totals = []

    for i in range(2):
        # target is only for 2nd innings
        target = totals[0] if i == 1 else None

        # getting all results after team has played their innings
        scorecard, total, chased = play_innings(team_names[i], players_per_team, target)
        
        # appending current team's scorecard and total to scorecards and totals (for match summary)
        scorecards.append(scorecard)
        totals.append(total)
        
        # writing scorcard in a txt file (<team-name>_scorecard.txt)
        write_scorecard(f"{team_names[i]}_scorecard.txt", team_names[i], scorecard, total)
        if chased:
            print(f"{team_names[i]} has chased down the target!")
            break

    # Checking the result
    winner = team_names[totals.index(max(totals))] if totals[0] != totals[1] else "Tie"
    
    # Writing the match summary
    with open("match_summary.txt", 'w') as f:
        f.write(f"{team_names[0]}: {totals[0]}\n")
        f.write(f"{team_names[1]}: {totals[1]}\n")
        f.write(f"Winner: {winner}\n")
    print(f"\nMatch summary is written to match_summary.txt")
    print(f"WINNER: {winner}")


def play_innings(team_name, players_per_team, target=None):
    boundry_shots = ["sweep", "slog sweep", "pull", "cover drive", "helicopter", "lofted drive", "scoop"]
    wicket_balls = ["googly", "carrom", "off-cutter", "leg-cutter", "top-spin", "leg-spin", "reverse-swing", "knuckle", "slower-one"]
    run_balls = ["front-foot punch", "backfoot punch", "late cut", "upper-cut"]
    dot_balls = ["front-foot defence", "beaten", "back-foot defence"]
    print(f"\n{team_name} is batting!")
    scorecard = []
    total_runs = 0
    chased = False

    # play innings for each player
    for player_num in range(players_per_team):
        player = get_valid_name(f"Enter name for Player {player_num+1} of {team_name}: ")
        runs = 0
        balls = 0
        shots = []

        # Player's innings
        while True:
            result = random.choice([-1, 0, 1, 2, 3, 4, 5, 6])
            balls += 1

            # if he is out
            if result == -1:
                wicket_ball = random.choice(wicket_balls)
                print(f"{player} is OUT after {balls} balls, scored {runs} runs. (Ball: {wicket_ball})")
                shots.append(f"OUT ({wicket_ball})")
                break

            # if he scored runs
            else:
                runs += result
                if result == 4 or result == 6:
                    shot = random.choice(boundry_shots)
                    shots.append(f"{result} ({shot})")
                elif result in [1, 2, 3]:
                    shot = random.choice(run_balls)
                    shots.append(f"{result} ({shot})")
                elif result == 0:
                    shot = random.choice(dot_balls)
                    shots.append(f"0 ({shot})")

            # check if team chased the target
            if target is not None and (total_runs + runs) > target:
                chased = True
                break
        scorecard.append({'name': player, 'runs': runs, 'balls': balls, 'shots': shots})
        total_runs += runs

        # Display all balls played and shots offered for this player
        for ball_no, shot in enumerate(shots, 1):
            print(f"  Ball {ball_no}: {shot}")
        print()

        # game over if chase was successful
        if chased:
            break
    print(f"Total runs for {team_name}: {total_runs}\n")
    return scorecard, total_runs, chased

# Writing team scorecard
def write_scorecard(filename, team_name, scorecard, total_runs):
    with open(filename, 'w') as f:
        f.write(f"Scorecard for {team_name}\n")
        f.write("Player\tRuns\tBalls\tShots\n")
        for entry in scorecard:
            shots_str = ', '.join(entry['shots'])
            f.write(f"{entry['name']}\t{entry['runs']}\t{entry['balls']}\t{shots_str}\n")
        f.write(f"Total: {total_runs}\n")


if __name__ == "__main__":
    main()
import json


def fileReader(filename: str):
    with open(filename) as file:
        data = file.read()
    return json.loads(data)


class PlayersApp:
    def __init__(self):
        pass

    def help(self):
        print('''
commands:
0 quit
1 search for player
2 teams
3 countries
4 players in team
5 players from country
6 most points
7 most goals''')

    @classmethod
    def print_player(cls, player: dict):
        return f"{player['name']:21}{player['team']:>3}{player['goals']:>4} + {player['assists']:>2} = {(player['goals'] + player['assists']):>3}"

    @classmethod
    def get_points(cls, player: dict):
        return (player['goals'] + player['assists'])

    def get_player(self):
        name = input('name: ')
        print()
        for player in self.players:
            if player['name'] == name:
                print(self.print_player(player))

    def get_teams(self):
        teams = sorted(set([player['team'] for player in self.players]))
        for team in teams:
            print(team)

    def get_countries(self):
        countries = sorted(set([player['nationality']
                           for player in self.players]))
        for country in countries:
            print(country)

    def get_players(self, team_or_country: str):
        if team_or_country == 't':
            user_prompt = 'team'
        elif team_or_country == 'c':
            user_prompt = 'nationality'

        search_term = input(f"{user_prompt}: ")
        print()
        players = list(
            filter(lambda x: x[user_prompt] == search_term, self.players))

        players = sorted(players, key=self.get_points, reverse=True)
        for player in players:
            print(self.print_player(player))

    def get_most_points(self, points_or_goals: str):
        user_prompt = input('how many: ')
        print()
        if points_or_goals == 'p':
            players = sorted(
                self.players, key=lambda i: (self.get_points(i), i['goals']), reverse=True)
        elif points_or_goals == 'g':
            players = sorted(
                self.players, key=lambda i: (i['goals'], -i['games']), reverse=True)

        for p in range(0, int(user_prompt)):
            print(self.print_player(players[p]))

    def execute(self):
        file_name = input('file name: ')
        self.players = fileReader(file_name)
        print(f"read the data of {len(self.players)} players")
        self.help()
        while True:
            command = input('\ncommand: ')
            if command == '0':
                break
            elif command == '1':
                self.get_player()
            elif command == '2':
                self.get_teams()
            elif command == '3':
                self.get_countries()
            elif command == '4':
                self.get_players('t')
            elif command == '5':
                self.get_players('c')
            elif command == '6':
                self.get_most_points('p')
            elif command == '7':
                self.get_most_points('g')


test = PlayersApp()
test.execute()

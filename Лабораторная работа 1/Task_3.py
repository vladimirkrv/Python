list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

count_players = len(list_players)  # TODO кол-во игроков
count_team = count_players // 2  # TODO число участников одной команды
team1 = list_players[:count_team]  # TODO имя с индексом 0 и имена с четными индексами
team2 = list_players[count_team:]  # TODO имена с нечетными индексами
print(team1)
print(team2)

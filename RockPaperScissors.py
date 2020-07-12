from random import random, randint, randrange

game_pos = ["камень", "ножницы", "бумага"]
player_win_sit = [["ножницы", "бумага"], ["бумага", "камень"], ["камень", "ножницы"]]
player_lose_sit = [["бумага", "ножницы"], ["ножницы", "камень"], ["камень", "бумага"]]
player_draw_sit = [["бумага", "бумага"], ["ножницы", "ножницы"], ["камень", "камень"]]

test = []
test1 = []


class Player:

    score = 0

    def pTurn(self, player_pos):
        if player_pos == game_pos[0]:
            return game_pos[0]
        if player_pos == game_pos[1]:
            return game_pos[1]
        if player_pos == game_pos[2]:
            return game_pos[2]


class AI:

    score = 0

    def aTurn(self):
        return game_pos[randint(0, 2)]


if __name__ == "__main__":

    lim = randrange(3, 8, 2)
    print("---" * 10)
    print("Приветствую!\nИгра ведется до {} очков.\n".format(lim))

    player = Player()
    opponent = AI()

    def turn():
        print("---" * 10)
        print("Ход игрока.\n\nВыберите позицию:")
        player_pos = str(input()).lower()
        player.pTurn(player_pos)
        test.append(player_pos)

        print("---" * 5)
        op_pos = opponent.aTurn()
        print("Ход компьютера.\n\nКомпьютер выбирает:\n{}\n".format(op_pos))
        test.append(op_pos)

        for i in range(len(player_win_sit)):
            if test == player_win_sit[i]:
                player.score += 1
                print("-- Победа игрока --\n")
            if test == player_lose_sit[i]:
                opponent.score += 1
                print("-- Победа компьютера --\n")
            if test == player_draw_sit[i]:
                print("-- Ничья --\n")

        test.clear()

    for i in range(lim):
        turn()
    print("---" * 10)

    if player.score > opponent.score:
        print("Победил игрок c {} очками, компьютер - {}".format(player.score, opponent.score))
    if player.score < opponent.score:
        print("Победил компьютер c {} очками, игрок - {}".format(opponent.score, player.score))
    if player.score == opponent.score:
        print("Ничья, у обоих по {}".format(player.score))

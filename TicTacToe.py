#Assignment: CSE 210-01, W02, Tic Tac Toe
#Author: Samuel Gallew
def main():
    width = 3
    height = 3
    index = 0
    
    end = ""
    while end != "exit":
        end = input("Shall we play a game?\n").lower()
        if end == "yes" or end == "y":
            game = {1:[1, 2, 3], 2:[4, 5, 6], 3:[7, 8, 9]}
        pass
    pass


def play(game_struct):
    show_game(game_struct)
    turn = "x"
    win = False
    while not win:
        select = input(f"{turn}'s turn to choos a space (e.g. 9): ")
        valid = False
        for i in game_struct:
            if select in game_struct[i]:
                change = list(game_struct[i]).index(select)
                list(game_struct[i]).insert(select, turn)
                list(game_struct[i]).remove(change)
                valid = True
                break
        if valid:
            win = check_state(game_struct, turn)
            if not win:
                if turn == "x":
                    turn = "o"
                else:
                    turn = "x"
            else:
                print(f"Good game! {turn}'s Won!")

        else:
            print("Sorry, that's not currently a valid move, try something else.")
        show_game(game_struct)


def show_game(game_struct):
    say = []
    for i in game_struct:
        save = ""
        lines = ""
        for j in i:
            save += f"{j}|"
            lines += "-+"
        save.removesuffix("|")
        lines.removesuffix("+")
        say.append(save)
        say.append(lines)
    say.pop()
    pint = ""
    for i in say:
        pint += i
    print(pint)


def check_state(game_struct, turn):
    win = False
    y = []
    for i in game_struct:
        x = []
        if turn in game_struct:
            count = 0
            for j in game_struct[i]:
                count += 1
                if j == turn:
                    x.append(count)
        y.append(x)
        index = -1
    for i in y:
        index += 1
        for j in x:
            if j + 1 in x and j + 2 in x:
                win = True
            if j in y[index + 1] and j in y[index + 2]:
                win = True
            if j + 1 in y[index + 1] and j + 2 in y[index + 2]:
                win = True
            if j - 1 in y[index + 1] and j - 2 in y[index + 2]:
                win = True
    return win
            
            


if __name__ == "__main__":
    main()
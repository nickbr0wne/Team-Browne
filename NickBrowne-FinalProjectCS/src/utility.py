from src.constant import WIDTH, WHITE
import pygame


def display_message(content, win, BACK_IMAGE, END_FONT):
    pygame.time.delay(500)
    win.blit(BACK_IMAGE, (0, 0))
    end_text = END_FONT.render(content, 1, WHITE)
    win.blit(end_text, ((WIDTH - end_text.get_width()) // 2, (WIDTH - end_text.get_height()) // 2))
    pygame.display.update()
    pygame.time.delay(3000)


# Checking if someone has won
def has_won(game_array, win, BACK_IMAGE, END_FONT):
    # Checking rows
    for row in range(len(game_array)):
        if (game_array[row][0][2] == game_array[row][1][2] == game_array[row][2][2]) and game_array[row][0][2] != "":
            display_message(game_array[row][0][2].upper() + " WINS!", win, BACK_IMAGE, END_FONT)
            return True

    # Checking columns
    for col in range(len(game_array)):
        if (game_array[0][col][2] == game_array[1][col][2] == game_array[2][col][2]) and game_array[0][col][2] != "":
            display_message(game_array[0][col][2].upper() + " WINS!", win, BACK_IMAGE, END_FONT)
            return True

    # Checking main diagonal
    if (game_array[0][0][2] == game_array[1][1][2] == game_array[2][2][2]) and game_array[0][0][2] != "":
        display_message(game_array[0][0][2].upper() + " WINS!", win, BACK_IMAGE, END_FONT)
        return True

    # Checking reverse diagonal
    if (game_array[0][2][2] == game_array[1][1][2] == game_array[2][0][2]) and game_array[0][2][2] != "":
        display_message(game_array[0][2][2].upper() + " WINS!", win, BACK_IMAGE, END_FONT)
        return True

    return False


def has_drawn(game_array, win, BACK_IMAGE, END_FONT):
    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            if game_array[i][j][2] == "":
                return False

    display_message("TIE!", win, BACK_IMAGE, END_FONT)
    return True
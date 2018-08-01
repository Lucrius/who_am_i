#include <stdio.h>
#include <stdbool.h>

#define BOARDSIZE 3
int board[BOARDSIZE][BOARDSIZE];

void display_board()
{
	int i, j;
	printf("\nBoard \n");
	for(i=0; i<BOARDSIZE; i++) {
		for (j=0; j<BOARDSIZE; j++) {
			printf("%d\t", board[i][j]);
		}
		printf("\n");
	}
}

bool check_for_end(int player)
{
	int i, j;
	
	/* Row wise check */
	for (i=0; i<BOARDSIZE; i++) {
		for (j=0; j<BOARDSIZE -1; j++) {
			if (board[i][j] != board[i][j+1])
				break;
		}
		if (j==BOARDSIZE -1 && board[i][j-1] == board[i][j] && board[i][j] == player) {
			return true;
		}
	}
	
	/* Column wise check */
	for (j=0; j<BOARDSIZE; j++) {
		for (i=0; i<BOARDSIZE -1; i++) {
			if (board[i][j] != board[i+1][j])
				break;
		}
		if (i==BOARDSIZE -1 && board[i-1][j] == board[i][j] && board[i][j] == player) {
			return true;
		}
	}
	
	/* Right diagonal wise check */
	for (i=0, j=0; i<BOARDSIZE -1, j<BOARDSIZE -1; i++, j++) {
		if (board[i][j] != board[i+1][j+1])
			break;
	}
	if (j==BOARDSIZE -1 && board[i-1][j-1] == board[i][j] && board[i][j] == player)
		return true;
	
	/* Left diagonal wise check */
	for (i=0, j=BOARDSIZE -1; i<BOARDSIZE -1, j>0; i++, j--) {
		if (board[i][j] != board[i+1][j-1])
			break;
	}
	if (j==0 && board[i][j] == board[i-1][j+1] && board[i][j] == player)
		return true;

	return false;
}

int main()
{
	bool game_not_over = true;
	bool player = true;
	int x,y, game_count=0;

	printf("Let's begin the GAME!!\n");
	display_board();

	while (game_not_over) {
get_input:
		printf("Player %d : (x,y) - ", player? 1:2);
		scanf("%d %d", &x, &y);
		if (x > BOARDSIZE || x <0 && y > BOARDSIZE || y <0) {
			printf("Enter the correct co-ordinates\n");
			goto get_input;
		}
		if (board[x][y] != 0) {
			printf("Already value is there in those co-ordinates, please enter other co-ordinates\n");
			goto get_input;
		}

		if (player)
			board[x][y] = 1;
		else
			board[x][y] = 2;
		
		display_board();
		if (check_for_end(player? 1:2)) {
			printf("Congratulations.. Player %d Wins!!\n", player? 1:2);
			break;
		}

		player = !player;
		game_count++;
		if (game_count == BOARDSIZE*BOARDSIZE) {
			printf("Game Tie!! Thanks for playing\n");
			break;
		}
	}
	return 0;
}

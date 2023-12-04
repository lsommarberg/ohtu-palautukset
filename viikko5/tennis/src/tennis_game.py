class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.match_score_player1 = 0
        self.match_score_player2 = 0
        self.score = ''
        self.scores = {
            0: 'Love',
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.match_score_player1 = self.match_score_player1 + 1
        if player_name == self.player2_name:
            self.match_score_player2 = self.match_score_player2 + 1


    def points_won_when_even(self):
        deuce = 3
        if self.match_score_player1 >= deuce:
            self.score = "Deuce"
        else:
            self.score = self.scores[self.match_score_player1]+"-All"
            

    def points_won(self):
        player1 = self.player1_name, self.match_score_player1
        player2 = self.player2_name, self.match_score_player2
        players = [player1, player2]

        for player in players:
            if player[1] not in self.scores.keys():
                self.game_over()
                break
            if player[0] == self.player1_name:
                self.score = self.score + self.scores[player[1]]
            if player[0] == self.player2_name:
                self.score = self.score + "-" 
                self.score = self.score + self.scores[player[1]]


    def game_over(self):
        difference_of_scores = self.match_score_player1 - self.match_score_player2
        player1_advantage = 1
        player2_advantage = -1
        player1_win = 2
        player2_win = -2

        if difference_of_scores >= player1_advantage:
            if difference_of_scores >= player1_win:
                self.score = "Win for player1"
            else:
                self.score = "Advantage player1"

        if difference_of_scores <= player2_advantage:
            if difference_of_scores <= player2_win:
                self.score = "Win for player2"
            else:
                self.score = "Advantage player2"
        
            

    def get_score(self):

        if self.match_score_player1 == self.match_score_player2:
            self.points_won_when_even()

        if self.match_score_player1 != self.match_score_player2:
            self.points_won()
                    

        return self.score

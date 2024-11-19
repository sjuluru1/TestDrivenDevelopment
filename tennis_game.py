class TennisGame:
    def __init__(self, player_one_name, player_two_name):
        self.player_one_name = player_one_name
        self.player_two_name = player_two_name
        self.player_one_score = 0
        self.player_two_score = 0

    def get_score(self):
        if self.has_winner():
            return f"{self.player_with_highest_score()} wins"
        if self.has_advantage():
            return f"Advantage {self.player_with_highest_score()}"
        if self.is_deuce():
            return "Deuce"
        if self.player_one_score == self.player_two_score:
            return f"{self.translate_score(self.player_one_score)} all"
        return f"{self.translate_score(self.player_one_score)},{self.translate_score(self.player_two_score)}"

    def player_with_highest_score(self):
        if self.player_one_score > self.player_two_score:
            return self.player_one_name
        else:
            return self.player_two_name

    def has_winner(self):
        if self.player_two_score >= 4 and self.player_two_score >= self.player_one_score + 2:
            return True
        if self.player_one_score >= 4 and self.player_one_score >= self.player_two_score + 2:
            return True
        return False

    def has_advantage(self):
        if self.player_two_score >= 4 and self.player_two_score == self.player_one_score + 1:
            return True
        if self.player_one_score >= 4 and self.player_one_score == self.player_two_score + 1:
            return True
        return False

    def is_deuce(self):
        return self.player_one_score >= 3 and self.player_one_score == self.player_two_score

    def player_one_scores(self):
        self.player_one_score += 1

    def player_two_scores(self):
        self.player_two_score += 1

    def translate_score(self, score):
        translations = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
        return translations.get(score, "Invalid Score")

class ScoreBoard:
    def __init__(self, scores):
        self.scores = scores

    def __add__(self, other):
        if isinstance(other, ScoreBoard):
            return ScoreBoard(self.scores + other.scores)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, ScoreBoard):
            return sum(self.scores) > sum(other.scores)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, ScoreBoard):
            return sum(self.scores) < sum(other.scores)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, ScoreBoard):
            return sum(self.scores) == sum(other.scores)
        return NotImplemented

    def __contains__(self, score):
        return score in self.scores

    def __len__(self):
        return len(self.scores)

    def __str__(self):
        return f"ScoreBoard({self.scores})"


score1 = ScoreBoard([30, 40, 50])
score2 = ScoreBoard([10, 20, 90])
score3 = ScoreBoard([30, 40, 50])
final = score1 + score2
print(final)

print(score1 > score2)
print(score1 < score2)
print(score1 == score3)

print(len(final))

print(40 in final)
print(100 in score1)

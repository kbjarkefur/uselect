from District import District

class State:

    def __init__(self,state,state_data):
        self.state = state
        self.data = state_data
        self.winners = {}
        self.partyvotes = {}

        self.dist_list = []
        for dist in self.data.D_ID.unique():
            self.add_dist(dist)

    def add_dist(self,dist):
        distObj = District(dist,self.data[self.data.D_ID == dist])
        self.dist_list.append(distObj)
        self.add_dist_winner(distObj.winner)
        self.add_dist_votes(distObj.partyvotes)

    def add_dist_winner(self, winner):
        if winner in self.winners:
            self.winners[winner] = self.winners[winner] + 1
        else:
            self.winners[winner] = 1

    def add_dist_votes(self, new_votes):
        for party in new_votes.keys():
            if party in self.partyvotes:
                self.partyvotes[party] = self.partyvotes[party] + new_votes[party]
            else:
                self.partyvotes[party] = new_votes[party]

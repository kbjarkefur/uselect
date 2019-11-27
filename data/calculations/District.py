class District:

    def __init__(self, d_id,d_data):
        self.id = d_id
        self.data = d_data

        self.partyvotes = {}
        for party in self.data.PARTY_VALID.unique():
            self.partyvotes[party] = int( self.data.loc[self.data['PARTY_VALID'] == party, 'VOTES'].values[0])

        self.winner = max(self.partyvotes, key=self.partyvotes.get)

    # def addPartyVote(self,partyabb:str, votes: int):
    #     self.partyvotes[partyabb] = votes
    #
    #     if votes > self.maxvotes:
    #         self.winner = partyabb
    #         self.maxvotes = votes

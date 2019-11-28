from Election import Election

class District:

    def __init__(self, d_id,d_data):
        self.id = d_id
        self.data = d_data

        #populate dict with Party abb as key and number votes in district as value
        self.votes = {}
        for party in self.data.PARTY_VALID.unique():
            self.votes[party] = int(self.data.loc[self.data['PARTY_VALID']==party, 'VOTES'].values[0])

        #winner in district is party with the most voter
        self.election = Election(self.votes,{})

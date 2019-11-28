class Election:

    def __init__(self,votes,mandates):

        self.mandates_in = mandates
        self.votes = votes
        self.mandates_out = {}

        #Calculate uddatals
        self.uddatals = {}
        for party in self.votes.keys():
            #If no mandates already, default to 0
            self.mandates_in[party]  = self.mandates_in.get(party, 0)
            self.mandates_out[party] = self.mandates_in[party]
            #Calculate current uddatal
            self.uddatals[party] =  self.votes[party] / (1+2*self.mandates_in[party])

        #Calculate winner
        self.this_mandate = max(self.uddatals, key=self.uddatals.get)
        self.mandates_out[self.this_mandate] += 1

        #Calculate Aggregates
        self.total_votes = 0
        self.total_mandates = 0
        for party in self.votes.keys():
            self.total_votes    += self.votes[party]
            self.total_mandates += self.mandates_out[party]

        #Populate self.pcnts with percent values
        self.pcnts = {}
        for party in self.votes.keys():

            pcnt_of_votes    = self.votes[party] / self.total_votes
            pcnt_of_mandates = self.mandates_out[party] / self.total_mandates

            self.pcnts[party] = {}
            self.pcnts[party]["pcnt_of_votes"]    = format(pcnt_of_votes,'.2%')
            self.pcnts[party]["pcnt_of_mandates"] = format(pcnt_of_mandates,'.2%')
            self.pcnts[party]["pcnt_diff"] = "{0:.1f}".format(100*(pcnt_of_votes - pcnt_of_mandates)) + " pp"

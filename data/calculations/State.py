from jinja2 import Template

from District import District
from Election import Election

class State:

    def __init__(self,state,state_data):
        self.state = state
        self.data = state_data
        self.mandates = {}
        self.total_mandates = 0
        self.votes = {}
        self.total_votes = 0

        self.dist_list = []
        for dist in self.data.D_ID.unique():
            self.add_dist(dist)

        #Populate self.pcnts with percent values
        self.pcnts = {}
        for party in self.votes.keys():

            pcnt_of_votes    = self.votes[party] / self.total_votes
            pcnt_of_mandates = self.mandates[party] / self.total_mandates

            self.pcnts[party] = {}
            self.pcnts[party]["pcnt_of_votes"]    = format(pcnt_of_votes,'.2%')
            self.pcnts[party]["pcnt_of_mandates"] = format(pcnt_of_mandates,'.2%')
            self.pcnts[party]["pcnt_diff"] = "{0:.1f}".format(100*(pcnt_of_votes - pcnt_of_mandates)) + " pp"

        self.adj_elct1 = Election(self.votes,self.mandates)
        self.adj_elct2 = Election(self.votes,self.adj_elct1.mandates_out)
        self.adj_elct3 = Election(self.votes,self.adj_elct2.mandates_out)

#######################################

    def add_dist(self,dist):
        distObj = District(dist,self.data[self.data.D_ID == dist])
        self.dist_list.append(distObj)
        self.add_mandates(distObj.election.mandates_out)
        self.add_votes(distObj.votes)

    def add_mandates(self, mandates):
        #Get number of winners for party and add 1, initialize to 0 first if party has no previous winners
        for party in mandates.keys():
            self.mandates[party] = self.mandates.get(party, 0) + mandates[party]
            self.total_mandates += mandates[party]

    def add_votes(self, new_votes):
        #Loop over all parties. Get number of votes for party and add number of new votes, initialize to 0 first if needed
        for party in new_votes.keys():
            self.votes[party] = self.votes.get(party, 0) + new_votes[party]
            self.total_votes += new_votes[party]

    def write_report(self,test=False):
        with open('state_report_template.md', 'r') as file:
            templateFromFile = Template(file.read(),trim_blocks=True)

        if test:
            output_filename = "state_report_output.md"
        else:
            output_filename = "../../reports/state_report_" + self.state + ".md"

        output_file = open(output_filename, "w")
        output_file.write(templateFromFile.render(state=self))
        output_file.close()

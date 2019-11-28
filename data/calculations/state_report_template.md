# State report - {{state.state}}

## Total results in the state

One mandate is awarded per district to the party that received the most number of votes in that district. The table below show the number of votes and mandates aggregated from district level. It also shows the percentage of  all votes and percentage of mandates each party received relative to the total number of votes and mandates in the state.

The last column shows the percentage point (pp) difference in percentage of votes and percentage or mandates. The more negative number the more a party benefits from gerrymandering, wasted votes and the current system of all mandates only being assigned one per district to the party that received most votes in that district. The higher positive number the more you are disadvantaged of the same things.

| Party | Mandates | Votes | % of Votes |  % of mandates | Diff % of votes minus % of mandates |
|---|--:|--:|--:|--:|--:|
{% for party in state.votes.keys() %}
|{{party}}|{{state.mandates[party]}}|{{'{:,}'.format(state.votes[party])}}|{{state.pcnts[party]["pcnt_of_votes"]}}|{{state.pcnts[party]["pcnt_of_mandates"]}}|{{state.pcnts[party]["pcnt_diff"]}}|
{% endfor %}

## Adjustment mandates

### Adjustment mandates 1

Adjustment mandate 1 would have gone to party **{{state.adj_elct1.this_mandate}}**.

| Party | Mandates | Votes | % of Votes |  % of mandates | Diff % of votes minus % of mandates |
|---|--:|--:|--:|--:|--:|
{% for party in state.votes.keys() %}
|{{party}}|{{state.adj_elct1.mandates_out[party]}}|{{'{:,}'.format(state.votes[party])}}|{{state.adj_elct1.pcnts[party]["pcnt_of_votes"]}}|{{state.adj_elct1.pcnts[party]["pcnt_of_mandates"]}}|{{state.adj_elct1.pcnts[party]["pcnt_diff"]}}|
{% endfor %}

### Adjustment mandates 2

Adjustment mandate 2 would have gone to party **{{state.adj_elct2.this_mandate}}**.

| Party | Mandates | Votes | % of Votes |  % of mandates | Diff % of votes minus % of mandates |
|---|--:|--:|--:|--:|--:|
{% for party in state.votes.keys() %}
|{{party}}|{{state.adj_elct2.mandates_out[party]}}|{{'{:,}'.format(state.votes[party])}}|{{state.adj_elct2.pcnts[party]["pcnt_of_votes"]}}|{{state.adj_elct2.pcnts[party]["pcnt_of_mandates"]}}|{{state.adj_elct2.pcnts[party]["pcnt_diff"]}}|
{% endfor %}

### Adjustment mandates 3

Adjustment mandate 3 would have gone to party **{{state.adj_elct3.this_mandate}}**.

| Party | Mandates | Votes | % of Votes |  % of mandates | Diff % of votes minus % of mandates |
|---|--:|--:|--:|--:|--:|
{% for party in state.votes.keys() %}
|{{party}}|{{state.adj_elct3.mandates_out[party]}}|{{'{:,}'.format(state.votes[party])}}|{{state.adj_elct3.pcnts[party]["pcnt_of_votes"]}}|{{state.adj_elct3.pcnts[party]["pcnt_of_mandates"]}}|{{state.adj_elct3.pcnts[party]["pcnt_diff"]}}|
{% endfor %}


## Districts

{% for dist in state.dist_list %}

### District {{dist.id}}
Winner of mandate in {{dist.id}} is **{{dist.election.this_mandate}}**

| Party | Votes | Mandate |
|---|---|---|
{% for party in dist.votes.keys() %}
|{{party}}|{{dist.votes[party]}}|{{dist.election.mandates_out[party]}}
{% endfor %}
{% endfor %}

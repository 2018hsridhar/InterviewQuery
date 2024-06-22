'''
URL := https://www.interviewquery.com/questions/ticket-agent-analysis
Analyze ticket data -> better response time
Track ticket progress

3 seperate aggregates to count
those assigned and not assigned to an agent : should equal count ( null in agent id field )

Log :
(A) isnull() NaN testing of rows
(B) ~ versus ! for NOT operator in df row subset selections
'''
import pandas as pd

def tickets_analysis(tickets: pd.DataFrame):
    numTickets = tickets.shape[0]
    agentTickets = tickets[~tickets['agent_id'].isnull()]
    numAgentTickets = agentTickets.shape[0]
    notAgentTickets = tickets[tickets['agent_id'].isnull()]
    numNotAgentTickets =  notAgentTickets.shape[0]
    # a simple list
    aggrStats = [numTickets, numAgentTickets, numNotAgentTickets]
    # create series form a list
    # pdSeries = pd.Series(aggrStats)
    # df = pd.DataFrame(columns=('col1', 'col2', 'col3'))
    df = pd.DataFrame(columns=('total_tickets','tickets_with_agent','tickets_without_agent'))
    df.loc[0] = aggrStats
    return df
    
    

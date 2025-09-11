from property_agency_director import PropertyAgencyDirector
from property import Property
from property_agent import PropertyAgent
directorx = PropertyAgencyDirector("D123", "ABC Realty", 2010, 0.05, 0.75)

# print(directorx.get_registration_number())
# print(directorx.get_company())
# print(directorx.get_commission_sharing_rate())
# print(directorx.get_director_commission_rate())



directory = PropertyAgencyDirector("D123", "ABC Realty", 2010, 0.06, 0.95)
print(directory.get_director_commission_rate())
# print(directory.get_commission_sharing_rate())




# directorx = PropertyAgencyDirector("D123", "ABC Realty", 2010, 0.05, 0.75)
# agenta = PropertyAgent("X123", "ABC Realty", 2015)
# agentb = PropertyAgent("Y456", "XYZ Realty", 2018)
# agentc = PropertyAgent("Z789", "LMN Realty", 2020)

# directorx.add_agent(agenta)
# directorx.add_agent(agentb)
# directorx.add_agent(agentc)


# for agent in directorx.get_agents():
#     print (f"registration num: {agent.agent_registration_number}")
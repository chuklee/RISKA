import pandas as pd
from get_data import *
from agent import *
import random
import warnings
warnings.filterwarnings('ignore')

# Get the data
df = get_data()
df = df.drop(columns = ["Open time", "Close time"])
df = add_simple_indicators(df)
df = change_to_num_simple(df)
df = add_complicated_indicators(df)
normal_df = df.copy(deep=True)
df = normalise_data(df)
#Delete the column ignore
df = df.drop(columns = ["Ignore"])
normalise_df = new_normalise_df(df)
#Cut the data in 8 parts and store them in a list
parts = []

"""PARAMETERS BEGIN"""
cut = 12
cash = 1000
agents = []
nb_agents = 500 # Number of agents
generation_nb = 10
"""PARAMETERS END"""

# Create the agents
for i in range(cut):
    parts.append(normalise_df.iloc[int(len(normalise_df) / cut) * i : int(len(normalise_df) / cut) * (i + 1)])
normal_df_parts = []
for i in range(cut):
    normal_df_parts.append(normal_df.iloc[int(len(normal_df) / cut) * i : int(len(normal_df) / cut) * (i + 1)])


for i in range(nb_agents):
    parameters = []
    for j in range(len(normalise_df.columns)):
        parameters.append(random.uniform(-1, 1))
    # Take a random number in the list of parts
    part_number = random.randint(0, len(parts) - 1)
    new_agent = agent(parts[part_number], parameters, cash, i, normal_df_parts[part_number])
    agents.append(new_agent)
for i in range(nb_agents):
    agents[i].trade()
    agents[i].test(parts, normal_df_parts)
# Sort the agents by their profit
agents.sort(key=lambda x: x.total_test, reverse=True)
nb_agents_toadd = int(nb_agents / 2)

"""TRAINING"""
for i in range(generation_nb):
    print("Generation: " + str(i))
    for j in range(nb_agents_toadd):
        agents = agents[:nb_agents_toadd]
        for k in range(nb_agents_toadd):
            part_number = random.randint(0, len(parts) - 1)
            new_agent = agent(parts[part_number], agents[k].parameters, cash, i, normal_df_parts[part_number])
            for l in range(len(new_agent.parameters)):
                new_agent.parameters[l] += random.uniform(-0.01, 0.01)
            agents.append(new_agent)
    for j in range(nb_agents):
        agents[j].indice = 0
        agents[j].buying = 0
        agents[j].trade()
        agents[j].test(parts, normal_df_parts)
    agents.sort(key=lambda x: x.total_test, reverse=True)

# Save the parameters of the best agent
param = agents[0].parameters
with open('parameters.json', 'w') as outfile:
    json.dump(param, outfile)
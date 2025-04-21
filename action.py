from pprint import pprint
from CybORG import CybORG
from CybORG.Simulator.Scenarios import EnterpriseScenarioGenerator
from CybORG.Agents import SleepAgent
from CybORG.Simulator.Actions.AbstractActions import PrivilegeEscalate

steps = 200
sg = EnterpriseScenarioGenerator(blue_agent_class=SleepAgent, 
                                green_agent_class=SleepAgent, 
                                red_agent_class=SleepAgent,
                                steps=steps)
cyborg = CybORG(scenario_generator=sg, seed=1234)

reset = cyborg.reset(agent='red_agent_0')
first_session_host = list(reset.observation.keys())[1]
initial_obs = reset.observation

print("\nRed Agent 0: Initial Observation \n")
pprint(initial_obs)


first_action = PrivilegeEscalate(hostname=first_session_host, session=0, agent='red_agent_0')
results = cyborg.step(agent='red_agent_0', action=first_action)
first_action_obs = results.observation

print("\nRed Agent 0: Observation #1 \n")
pprint(first_action_obs)

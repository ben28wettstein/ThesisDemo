from pprint import pprint
from CybORG import CybORG
from CybORG.Simulator.Scenarios import EnterpriseScenarioGenerator
from CybORG.Agents import SleepAgent, FiniteStateRedAgent, RandomSelectRedAgent
### Human On the Loop! ##############
from CybORG.Simulator.Actions import Sleep
#"""
# Initialise environment
steps = 1000
sg = EnterpriseScenarioGenerator(blue_agent_class=SleepAgent,
                                green_agent_class=SleepAgent,
                                red_agent_class=FiniteStateRedAgent,
                                steps=steps)
cyborg = CybORG(scenario_generator=sg, seed=1234)

# Record actions of red_agent_0
red_agent_0_actions = []
consent = True
cyborg.step()
step_actions = cyborg.environment_controller.action
red_agent_0_actions.append(step_actions['red_agent_0'])

for i in range(10):
    print("The last action taken by your Red Agent was:")
    print(red_agent_0_actions[-1])
    consent = input("Would you like the agent to proceed? Type Y to continue  ")
    if consent == "Y":
        cyborg.step()
    else:
        cyborg.step(agent='red_agent_0', action = Sleep())
    step_actions = cyborg.environment_controller.action
    #print(step_actions)
    red_agent_0_actions.append(step_actions['red_agent_0'])
# Print red_agent_0's actions
#pprint(red_agent_0_actions)
#"""

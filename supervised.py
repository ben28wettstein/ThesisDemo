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
for i in range(10):
    
    cyborg.step()
    step_actions = cyborg.environment_controller.action
    if consent:
        red_agent_0_actions.append(step_actions['red_agent_0'])
    else:
        red_agent_0_actions.append(Sleep())
    print("The last action taken by your Red Agent was:")
    print(red_agent_0_actions[-1])
    consent = input("Would you like the agent to proceed? type 1 to continue")
    if consent == "1":
        consent = True
    else:
        consent = False

# Print red_agent_0's actions
#pprint(red_agent_0_actions)
#"""

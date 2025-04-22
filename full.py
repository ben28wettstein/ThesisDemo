from pprint import pprint
from CybORG import CybORG
from CybORG.Simulator.Scenarios import EnterpriseScenarioGenerator
from CybORG.Agents import SleepAgent, FiniteStateRedAgent, RandomSelectRedAgent

### Human Out Of the Loop! ####
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
for i in range(20):
    cyborg.step()
    step_actions = cyborg.environment_controller.action
    red_agent_0_actions.append(step_actions['red_agent_0'])

# Print red_agent_0's actions
#pprint(red_agent_0_actions)
#"""

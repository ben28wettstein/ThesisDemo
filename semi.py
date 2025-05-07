from pprint import pprint
from CybORG import CybORG
from CybORG.Simulator.Scenarios import EnterpriseScenarioGenerator
from CybORG.Agents import SleepAgent, FiniteStateRedAgent, RandomSelectRedAgent

############# Human in the Loop ################
from CybORG.Agents.SimpleAgents.LinearAgent import LinearAgent
from ipaddress import IPv4Network,IPv4Address
from CybORG.Simulator.Actions import DiscoverRemoteSystems, AggressiveServiceDiscovery, StealthServiceDiscovery, Sleep, DiscoverDeception, PrivilegeEscalate, DegradeServices, Impact, Withdraw, ExploitRemoteService
#from CybORG.Simulator.Actions.ScenarioActions.EnterpriseActions import ExploitRemoteService_cc4
#"""
# Initialize environment
steps = 1000
sg = EnterpriseScenarioGenerator(blue_agent_class=SleepAgent,
                                 green_agent_class=SleepAgent,
                                 red_agent_class=LinearAgent,  # Will override manually
                                 steps=steps)
cyborg = CybORG(scenario_generator=sg, seed=1234)

# Get red agent's name and its action space
red_agent_name = 'red_agent_0'
#red_interface = cyborg.get_agent_interface(red_agent_name)

# Record actions taken
red_agent_0_actions = []

for i in range(9):
    print(f"\n--- Step {i + 1} ---")

    # Get available actions for red_agent_0
    action_space = cyborg.get_action_space(red_agent_name)
    actions = (action_space['action']) #list this 
    
    #remove actions which are False
    #actions = {key: value for key, value in actions.items() if value}
    
    #print(actions)
    actions = list(actions)
    # Print options
    print("Available actions:")
    for idx, action in enumerate(actions):
        print(f"{idx}: {action}")

    # Let user pick an action
    choice = int(input("Select action number:  "))

    def param_pick(param):
        param_dict = action_space[param]
        param_dict = {key: value for key, value in param_dict.items() if value}
        for idx, p in enumerate(param_dict):
            print(f"{idx}: {p}")
        return list(param_dict)[int(input("select " + param+ "  "))]
    
    if choice == 0: #Discover Remote
        subnet0 = param_pick('subnet')
        session0 = param_pick('session')
        action = DiscoverRemoteSystems(subnet=IPv4Network(subnet0), session=session0, agent=red_agent_name)
    
    elif choice == 1: #aggresive discovery
        session0 = param_pick('session')
        ip_address0 = param_pick('ip_address')
        action = AggressiveServiceDiscovery(session=session0, agent=red_agent_name, ip_address=IPv4Address(ip_address0))
    elif choice == 2: #stealth discovery
        session0 = param_pick('session')
        ip_address0 = param_pick('ip_address')
        action = StealthServiceDiscovery(session=session0, agent=red_agent_name, ip_address=IPv4Address(ip_address0))  
    elif choice == 3: #exploit remote
        session0 = param_pick('session')
        ip_address0 = param_pick('ip_address')
        action = ExploitRemoteService(ip_address=IPv4Address(ip_address0), session=session0, agent=red_agent_name)
    elif choice == 4: #privlege escalate
        hostname0 = param_pick('hostname')
        session0 = param_pick('session')
        action = PrivilegeEscalate(hostname=hostname0, session=session0, agent=red_agent_name)
    elif choice == 5: #degrade
        hostname0 = param_pick('hostname')
        session0 = param_pick('session')
        action = DegradeServices(hostname=hostname0, session=session0, agent=red_agent_name)
    elif choice == 6: #discover deception
        session0 = param_pick('session')
        ip_address0 = param_pick('ip_address')
        action =DiscoverDeception(session=session0, agent=red_agent_name, ip_address=IPv4Address(ip_address0))
    elif choice == 7: #impact
        hostname0 = param_pick('hostname')
        session0 = param_pick('session')
        action = Impact(hostname=hostname0, session=session0, agent=red_agent_name)
    elif choice == 8: #widthraw
        session0 = param_pick('session')
        ip_address0 = param_pick('ip_address')
        hostname0 = param_pick('hostname')
        action = Withdraw(session=session0, agent=red_agent_name, ip_address=IPv4Address(ip_address0),hostname=hostname0)
    else: #Sleep
        action = Sleep()
    chosen_action = action
    # Manually inject selected action ^^^   
    # Step the environment
    x = cyborg.step(action = chosen_action, agent = red_agent_name)
    
    # Extract action taken (should be just a list of one action
    action_taken = x.action[0] if isinstance(x.action, list) else x.action

    # Extract success (defaulting to 'UNKNOWN' if not present)
    success = x.observation.get('success', 'UNKNOWN')
    # Print formatted output
    print(f"** Turn {i+1} for {red_agent_name} **")
    print(f"Action: {action_taken}")
    print(f"Action Success: {str(success).upper()}")

# Optionally print the list of actions taken
#pprint(red_agent_0_actions)

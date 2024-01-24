from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import matplotlib.pyplot as plt
import networkx as nx


model = BayesianNetwork([
    ('Weather', 'TrafficCongestion'),
    ('TimeOfDay', 'TrafficCongestion'),
    ('DayOfWeek', 'TrafficCongestion'),
    ('SpecialEvent', 'TrafficCongestion')
])

cpd_weather = TabularCPD(variable='Weather', variable_card=3,
                         values=[[0.5], [0.3], [0.2]],
                         state_names={'Weather': ['Sunny', 'Rainy', 'Snowy']})

cpd_time_of_day = TabularCPD(variable='TimeOfDay', variable_card=3,
                             values=[[0.4], [0.4], [0.2]],
                             state_names={'TimeOfDay': ['Morning', 'Afternoon', 'Evening']})

cpd_day_of_week = TabularCPD(variable='DayOfWeek', variable_card=2,
                             values=[[0.7], [0.3]],
                             state_names={'DayOfWeek': ['Weekday', 'Weekend']})

cpd_special_event = TabularCPD(variable='SpecialEvent', variable_card=2,
                               values=[[0.9], [0.1]],
                               state_names={'SpecialEvent': ['No', 'Yes']})

cpd_traffic_congestion = TabularCPD(variable='TrafficCongestion', variable_card=3,
                                    values=[
                                        [0.1] * 36,  
                                        [0.2] * 36,  
                                        [0.7] * 36   
                                    ],
                                    evidence=['Weather', 'TimeOfDay', 'DayOfWeek', 'SpecialEvent'],
                                    evidence_card=[3, 3, 2, 2],
                                    state_names={
                                        'TrafficCongestion': ['High', 'Medium', 'Low'],
                                        'Weather': ['Sunny', 'Rainy', 'Snowy'],
                                        'TimeOfDay': ['Morning', 'Afternoon', 'Evening'],
                                        'DayOfWeek': ['Weekday', 'Weekend'],
                                        'SpecialEvent': ['No', 'Yes']
                                    })


model.add_cpds(cpd_weather, cpd_time_of_day, cpd_day_of_week, cpd_special_event, cpd_traffic_congestion)
assert model.check_model()


# Drawing the Bayesian Network
G = nx.DiGraph()
G.add_edges_from(model.edges())
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=12)
plt.title("Bayesian Network Graph")
plt.show()

inference = VariableElimination(model)
result = inference.query(variables=['TrafficCongestion'],
                         evidence={
                             'Weather': 'Rainy',
                             'TimeOfDay': 'Morning',
                             'DayOfWeek': 'Weekday',
                             'SpecialEvent': 'Yes'
                         })

print(result)

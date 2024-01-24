from sympy import symbols
from sympy.logic.boolalg import And, Not, Implies
from sympy.logic.inference import satisfiable

Tweety, Polly, Donald, Sylvester, Sunny = symbols('Tweety Polly Donald Sylvester Sunny')

Bird_Tweety, Bird_Polly, Bird_Donald, CanFly_Tweety, CanFly_Polly, CanFly_Donald, CanFly_Sylvester, \
CanFly_Sunny, Bird_Sunny = symbols(
    'Bird_Tweety Bird_Polly Bird_Donald CanFly_Tweety CanFly_Polly CanFly_Donald CanFly_Sylvester '
    'CanFly_Sunny Bird_Sunny'
)
Canary_Tweety, Canary_Sunny, Parrot_Polly, Penguin_Donald, Cat_Sylvester = symbols(
    'Canary_Tweety Canary_Sunny Parrot_Polly Penguin_Donald Cat_Sylvester'
)
knowledge_base = And(
    Canary_Tweety, Bird_Tweety, CanFly_Tweety,  
    Canary_Sunny, Bird_Sunny, CanFly_Sunny,     
    Bird_Donald, Not(CanFly_Donald),            
    Cat_Sylvester, Not(CanFly_Sylvester)       
)
rules = And(
    Implies(Canary_Tweety, CanFly_Tweety),
    Implies(Canary_Sunny, CanFly_Sunny),       
    Implies(Parrot_Polly, CanFly_Polly),
    Implies(Penguin_Donald, Not(CanFly_Donald)),
    Implies(Cat_Sylvester, Not(CanFly_Sylvester))
)

full_knowledge = And(knowledge_base, rules)

print("Can all canaries (Tweety and Sunny) fly? ", satisfiable(And(CanFly_Tweety, CanFly_Sunny, full_knowledge)) != False)
print("Can some birds (Polly) fly? ", satisfiable(And(CanFly_Polly, full_knowledge)) != False)
print("Can cats (Sylvester) fly? ",  satisfiable(And(CanFly_Sylvester, full_knowledge)))

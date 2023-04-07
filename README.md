# **virus_evo**

### *Current Representations :*

```
INITIALIZATION

Virus:
% initial structure of the virus and vaccine

Var : [ [0,0,0,0,0,0,0,0]x8 , [Lethal Point : index] , [Properties] ]
Vac : [ 0,0,0,0,0,0,0,0 ]

Lethal Points:
% initialize the lethal points of the virus

Choose x = randInt ( 1 , 3 )
Choose x randInt ( 0 , 7 ) to be index non repeating
Append indexes to Var : Lethal Point Array

Threatened:
% indicates whether or not a virus is threatened by vaccine
Append 0 to Var : Properties Array

```

```
VIRUS
% get virus threat binary
def get_virus_threat (virus):
    return value of virus threat parameter

% set virus threat binary
def set_virus_threat (virus, value):
    set the virus threat parameter to value

% get virus lp as an array
def get_virus_lp (virus):
    for each value in lp array:
        return array associated with lp index

% threaten a virus
def virus_threaten (virus, vaccine):
    for each lethal point in a virus:
        check if any match the VACCINE

    if lp match vaccine:
        if the virus was already threated:
            kill the virus
        otherwise threaten the virus
    otherwise remove / reset threat


```

```
VACCINE
% determine ways to threaten a virus

% method 1: avg of all LP array columns
for each column in a virus LP array:
    for each LP array in LP arrays:
        determine the most common value in a column
        append to avg array
    return average
```

```
MUTATION
*implementation*

```

```
SELECTION

Parent Selection
*implementation*
```

```
FUNCTIONS

set LP:
    change the set of LP of a virus
get LP:
    return set of LP (their binary stings)
```

### *Functions TODO :*
The following are functions that are to be done:
```
Virus:
- [] Translate Tree <-> Translate String
- [] Initialize Virus String
- [] Alter Lethal Points of Tree / String
- [] Alter Genetic Code of Virus Nodes
- [] Virus Threatened Property
- [] Virus Mutate Lethal Points
- []

Vaccine:
- [] Initialize String
- [] Alter Vaccine Genetic Code
- [] Vaccine Fitness  
- [] Collect all Lethal Nodes
```
## Timeline

```
Tasks:
Lavi    : init vacine (x) / threat / avg LP string (x)
Cyril   : mutation / set + get helper for LP
Priyank : init parent selection
```

### Mar 23 Virus Rep, Lethal Points
### Mar 24
### Mar 25
### Mar 26
### Mar 27
### Mar 28
### Mar 29
### Mar 30
### Mar 31

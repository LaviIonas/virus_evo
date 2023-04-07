# **virus_evo**

### *Current Representations :*

```
INITIALIZATION

Virus:
% initial structure of the virus and vaccine

Var : [ [00000000]x8 , [Lethal Point : index] , [Properties] ]
Vac : [ 00000000 ]

Lethal Points:
% initialize the lethal points of the virus

Choose x = randInt ( 1 , 3 )
Choose x randInt ( 0 , 7 ) to be index non repeating
Append indexes to Var : Lethal Point Array

Threatened:
% indicates whether or not a virus is threatened by vaccine

Append 0 to Var : Properties Array

VACCINE
init
```

```
VIRUS
    set / get virus threat status
```

```
VACCINE
    compute LP avg
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
Lavi    : init vacine / threat / avg LP string
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

# **virus_evo**

### *Current Representations :*

```
INITIALIZATION

Virus :
% initial structure of the virus and vaccine


Vir : [ [0,0,0,0,0,0,0,0]x8 , [Lethal Point : index] , [Properties] , [Mut_Val] ]
Vac : [ 0,0,0,0,0,0,0,0 ] (global var.vaccine)

    Lethal Points :
    % initialize the lethal points of the virus

        Choose x = randint ( 1 , 3 )
        Choose x randint ( 0 , 7 ) to be index non repeating
        Append indexes to Var : Lethal Point Array

    Properties :
    % store virus related information
        index 0:
            Threatened:
            % indicates whether or not a virus is threatened by vaccine
            Append 0 to Var : Properties Array

        index 1:
            Fitness Value:
            % store and update the fitness of a virus with each generation
            Append 0 to Var : Properties Array

        index 2:
            Virality Value:
            % store and update the virality of a virus based on mutations
            Append 0 to Var : Properties Array
        index 3:
            Virus Name:
            % Root Virus' are named Rn
            Upon Change, alter name of new virus (child/clone)

    Mutation Value :
    % store virus mutation values
        % stores the value of a mutation so that it can be reversed
        index 0->(virus length * virus node length)

        initialize array of 0's size => (virus length * virus node length)

```

```
VIRUS FUNCTIONS

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
def virus_threat_check (virus):
    for each lethal point in a virus:
        check if any match the VACCINE

    if lp match vaccine:
        if the virus was already threatened:
            kill the virus
        otherwise threaten the virus
    otherwise remove / reset threat

% kill a virus
def virus_null(virus):
    virus = []

% clean a virus_pop of all empty sets
def virus_pop_clean (virus_pop):
    TODO

% print a virus for human readability
def print_virus_readable(virus_pop):
    print virus names and stats

% update virus virality number after successful mutation
def update_virus_virality(virus):
    sum all the values of mut array
    return sum

% return avg virality of a virus pop in a generation
def get_generation_virality_avg(virus_pop):
    rturn avg virality / pop size

```

```
VACCINE
% determine ways to threaten a virus

% set vaccine value
def set_vaccine (vaccine) :
    set the global var vaccine to be the new vaccine

% method 1: avg of all LP array columns
def avg_lp_virus_string (lethal points)
    for each column in a virus LP array:
        for each LP array in LP arrays:
            determine the most common value in a column
            append to avg array
        return average

```

```
MUTATION

NATURAL SELECTION IMPLEMENTATION
% this is the mutation function when applied to the natural selection method
Considering that virus do not have DNA proofing, they are capable of rapid and
random mutations that can negatively, neutrally, or positively impact their
ability to exist in nature.

def natural_selection_mutation(virus):
    if random more than mutation rate:
        % select a random index in all the nodes
        r1 = random.randint(0,var.virus_length-1)
        r2 = random.randint(0,var.virus_length-1)

        flip the value of that index from 0->1 or 1->0

        mut_index = r1*var.virus_length + r2

        if the value is 0
            % mutation has be reversed
            set mut array value at mut index to 0
        if the value is 1
            % new mutation, add new random mutation value from -1 to 1
            new mut array value at mut index is random value

def natural_selection_virus_lp_mutation(virus):
    TODO
```

```
SELECTION

BIOLOGICAL REPRESENTATION
NATURAL SELECTION
Considering that virus' in biology do not have parents nor children,
It can be considered that virus' clone themselves using hosts.

In this method, a virus duplicates itself if its virality value is above 0.
That is, if the sum of all mutation values is above 0.
A negative virality value would indicate that a virus is not capable of spreading

In this instance, a clone is generated that can be identical or possibly mutated.
A Virus with a negative virality value cannot clone itself and can only mutate in
the attempt to improve its virality value.

%----------------

init virus and vaccine
gen = 0
gen_max = n

GENERATIONAL LOOP for n
    def natural_selection():
        call generate_virus_clones(virus_pop, gen)
            for each virus, if the virality value is above 0: make a clone
                rename the clone as a child of virus
        % natural_selection_virus_mutation function
        mutate the set of clones and append to virus population
        mutate the entire virus population

        TODO : implement vaccine interaction and evolution
        TODO : determine goal of system (termination)


Parent Selection
*implementation*
    TODO
```

```
FUNCTIONS


```
## Varying Methods for Virus / Vaccine EA

### Natural Selection (natural_selection.py)

```
NATURAL SELECTION IMPLEMENTATION
TODO : Define the entire Alg

```

### Parent Selection

```
PARENT SELECTION IMPLEMENTATION
TODO : Define the entire Alg
```

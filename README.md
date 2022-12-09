# Find-S Algorithm
The problem specification is as following:

Given:
  - **Instances X**: Possible days, each described by the attributes
    1. *Sky* (with possible values `Sunny`, `Cloudy`, and `Rainy`),
    2. *AirTemp* (with values `Warm` and `Cold`),
    3. *Humidity* (with values `Normal` and `High`),
    4. *Wind* (with values `Strong` and `Weak`),
    5. *Water* (with values `Warm` and `Cool`), and
    6. *Forecast* (with values `Same` and `Change`).
  - **Hypotheses H**: Each hypothesis is described by a conjunction of constraints on the attributes *Sky, AirTemp, Humidity, Wind, Water, and Forecast*. The constraints may be `?`
(any value is acceptable), `''` (no value is acceptable), or a specific value.
  - **Target concept c**: *EnjoySport* which maps each x in X to a member of {`Yes`,`No`}
  - **Training examples D**: Positive and negative examples of the target function.
  
Determine:
  - A hypothesis h in H such that h(x)=c(x) for all x in X.

## The Algorithm Flow
1. Initialize h to the most specific hypothesis in H which is `['','','','','','']` in this case.
2. For each positive training instance x
  - For each attribute constraint a_i in h
    - If the constraint a_i is satisfied by x, then do nothing
    -  Else replace a_i in h by the next more general constraint that is satisfied by x
3. Output hypothesis h
  

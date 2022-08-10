# Intro

This document serves 2 purposes: to list our assumptions (most of modelling is
assumption), and to help people _navigate_ the 3 kinds of variables (soon to be
4) in the model. We will start with the variables, and then move onto the assumptions
and the explicit rationale (we cannot talk about one without the other).

# Variables

## Endogenous / Exogenous

Variables come on the form of stocks, flows, and indicators. However, it is common
in the literature to divide each of those into two sub-types: exogenous variables and
endogenous variables. Exogenous just means native-to-the-outside and endogenous means
native-to-the-inside -- you can also think of them as inputs and not-inputs.

So what separates endogenous and exogenous variables? Simply, the endogenous variable's
value is **always** deterministically derived/computed from the internal system state,
while the exogenous variable utilizes _external state_. Which naturally leads us to ask:
what exactly **is** _external state_? In practice (or at least in this model) the external
state can be broken down into 2 types: **random values** (provided by the programming environment)
and **assumed values** (provided by the programmer). There is a third hybrid type: **randomly
chosen values from an assumed distribution**.

## Decisions, Scenarios

Variables can be alternatively categorized as decision-variables and scenario-variables.
A decision-variable is any variable that **we/Interlock** have direct control over -- either
at the start of the simulation (i.e. a parameter) or throughout (i.e. as a policy-or-update-function, used in A/B-testing),
while a scenario-variable is any variable that could be used to represent one of many
imagined scenarios (user-exodus, market-bubble, bubble-burst, heuristic-innovation-exhaustion,
high/low/zero-profit, etc). **This implies that both decision and scenario variables are exogenous**.

Obviously, these two kinds of variables affect each other -- we want to choose the decisions/strategies
that will work best in the majority of scenarios weighted by likelihood.

### Decision Variables

The variables that we have _direct_ control over are:

    * mint-rate
    * reward-rate
    * max-total-stake-per-entity
    * stake-yield
    * airlock-lookup-price
    * heuristic-innovation
    * token-mint-supply-rate
    * token-mint-reward-rate

You will notice that we can only control flow-rates and indicators (controlling stocks
would imply that we can create/destroy matter at will). While all of our values
are _numbers_, we can narrow the search-space by using fuzzy-values (which are _also_
just numbers internally, but they represent higher-level ideas instead of quantities).
For example, we can consider 4 possible fuzzy values for `airlock-lookup-price`: at-cost,
above-cost, below-cost, zero-cost. These four have implications for things like interlock-revenue,
airlock-adotpion-rate, and so on.

This brings us to variables that we have _indirect_ control over. These are variables that we
**do not** control, but we can influence them by modifying/initializing the above _direct-control_
variables.

    * interlock-hype
    * heuristic-contradictions
    * staking-opportunities
    * token-hold-rate
    * token-stake-rate
    * token-unstake-rate
    * token-reward-to-supply-rate
    * token-reward-to-held-rate
    * intr-invest-rate
    * intr-divest-rate
    * airlock-adoption-rate
    * airlock-abandonment-rate
    * airlock-lookup-rate
    * resolution-rate
    * airlock-share-rate
    * scam-page-success-rate
    * scam-upkeep-rate

### Scenario Variables

And finally we have variables that we have zero control over.

    * data-value
    * token-price
    * money-mint-rate
    * money-reclaim-rate
    * crypto-invest-rate
    * crypto-divest-rate
    * grey-area-entity-rate
    * airlock-revenue-rate
    * scam-page-visit-rate
    * scam-profits-per-page
    * scam-profit-rate
    * scammer-innovation
    * staking-enthusiasm

These variables are effectively **scenario-variables**. What happens if scammer-innovation
is consistently ahead of our own heuristic-innovation? What if nobody wants to stake? What if
(for reasons outside of our control) scam-page-success-rate drops to zero, _while_ the money-mint-rate
sky-rockets (effectively destroying our value prop, and causing crypto-investments to crater)?

### Morphological Analysis

These scenario and decision variables will need to be tested against each other. However given that there are
around 70 variables, and given that they can have almost any numerical value (except where they are bounded),
there are infinitely many combinations. To reduce the search-space, we will discretify the decision and
scenario variables, into discrete fuzzy values (as demonstrated with the airlock-lookup-price), and use the
cross-consistenć-matrices to declare any contradictory pairings. All non-contradictory pairings can then
be encoded as parameters, lending the model to aggresive and systematic parameter sweeping.

Ref:  https://www.swemorph.com/pdf/it-webart.pdf, https://www.swemorph.com/amg/pdf/amg-4-2-2015.pdf

The Python-level work for this still needs to be done, but it should be relatively easy. Even without it,
doing a limited manual analysis on just a few of the most important direct-control values is useful.

### Optimization and Goals and Assumptions

Overall, modelling is a planning and optimization exercise. In order to plan and optimize, we need
goals that we _assume_ are _good_ for _us_. We then evaluate the feasibility of those goals
and the durability of the decisions and strategies that are supposed to help us achieve those goals.

Interlock has one goal: to protect as many people in the web2 and web3 space as possible. Everything
else is in service of that goal. We **assume** a few things: that giving people tokens will encourage them
to install and use our extension, that doing _that_ will let us collect valuable (anonymized) data that will help us
improve our heuristics and that we can turn into profits, which will in turn let us buy our own token and drive the price
up, resulting in more adoption. We also assume that people will want to help us improve the heuristics in more active
ways (i.e. staking) in return for a yield, and for status (i.e. via a unique achievement-type NFT, among other things).

If one of those assumptions is false, we might be in trouble. If two of them are false, we might not have
a business. That said, we are pretty convinced (based on numerous affirming web2 and web3 examples, that
our assumptions are correct).


	  



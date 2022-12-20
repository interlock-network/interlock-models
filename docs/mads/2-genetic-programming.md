# MAD-2: Genetic Programming

## Changes Since MAD-1

In the previous MAD (MAD-1) we took a look at how reward-rate was
correlated with adoption-rate. Since that time, we have made changes
to how adoption is handled, so that it is more realistic. Specifically,
our adoption is modelled via a growth-rate between 1% and 20% per week
(Facebook, at its peak, grew at 25% per week). The growth rate is chosen
at random for each week, but can be boosted by 5% if we issue more rewards
this week than the previous week. We have also suppressed the abandoment-rate
for testing purposes, but will change that soon.

This of course changed a lot about the model and what strategies work. A few
bugs also made their way into the model, as a result of this change. Realising
that it took a long time to run the fully parameterized model, and then to inspect
the change of each state-variable over sim-time, we needed to think of a way to
change, test, and inspect the relevant decision-parameters, in way that was more
effective per labor-hour.

The answer -- it turned out -- was in Genetic Programming. Specifically, we wanted
to treat a subset of the model-parameters as a genome, and we wanted to treat a
state-variable as a fitness-value. This immediately disqualified python-libraries like
`deap`, since they are centered on complex evolution around a simple fitness function.
We, on the other hand, want to use the cadCAD simulation _itself_ as a complex fitness
function, and we want our evolution to be _simple_. Where most systems want to evolve
tree-like and stack-like _programs_ -- it is, after all, part of the field of
_program synthesis_ -- we want to evolve an optimal set of signed, floating-point
integers, and let the model do the rest.

Other changes include how we model heuristic-contradictions. We model heuristics and anti-heuristics,
where contradictions are `anti-heuristics/heuristics` (anti-heuristics are basically counter-measures),
and this represents our false-positive-rate, which directly correlates to grey-area-entity rate.

## Quasi-UMAD

Having a tiny, flat, space-efficient, and order-free (parameters are keys to dictionary values)
genome makes evolution and mutation very simple and easy. In fact, instead of doing
complex cross-over procedures, we use mutation exclusively, and control the addition-rate
and deletion-rate using function-arguments. We use a method nearly identical to UMAD
(Uniform Mutation through Addition and Deletion) -- called Quasi-Umad -- which differs
in that it has no order-sensitive addition (we cannot insert before or after a gene, because
our genome is order-free -- we instead choose to increment or decrement the gene-value to
a non-zero number (because zero is analogous to deletion of a gene)).

## Using Genetic Parameters

We express our decision-matrix as 2 sets of state-variables: stimuli and actions. Each
stimulus transmits a signal to each action. If you have S stimuli and A actions, you
have SxA cross-connections (or update arrows). The genetic parameters encode a sensitivity
from each S to each A, between -1 and 1. The granularity is set ahead of time
(currently set to three values, -1, 0, and 1 -- but will make it more granular, as we need to).

In other words, we are not evolving decision or computation, as much as we are evolving sensitivities,
while encoding the actual computations in the model itself.

In our current model, we have 3 stimuli:

  * token-price-delta
  * user-goal-prograss
  * anti-user-goal-progress

The token-price-delta is the change in token-price since the previous turn.
User-goal-progress is how _close_ we are to our goal of 100M users.
Anti-user-goal-progress is how _far_ we are to our goal of 100M users.

We could have wrapped the two user goals into 1 signed variable, but that would
have resulted in awkward stimulus of 0 at 50% users.

We have 6 actions:

  * change-max-stake
  * change-stake-yield
  * change-lookup-fee
  * change-user-fee
  * change-buyback-amount
  * change-reward-amount

This means there is a total of 18 stimulus-action pairs. We keep a population of
20 individuals, and evolve for 100 generations, selecting the fittest 20% of
each generation. We have an addition-rate and deletion-rate of 10%. Our fitness-value
is -- mostly out of curiosity -- `1/token-price`, where 0 represents perfect fitness.

We previously had a fitness value based around `scam-page-successes` -- and sure enough,
the model evolved a decision-matrix that issued only enough rewards to get to 100M users
(we cap at 100M, making growth a logistic curve instead of an exponential curce), and then
saving them up thereafter.

Here is a list of the top organisms from the latest token-price-maximizing run. We ran
this evolutionary loop on the `worst-case-greedy` parameter, where traders seek to sell tokens
for meager profits, and where our investors waste no time in unloading their tokens.

```
[({'anti-user-goal-progress-change-max-stake': 0,
   'user-goal-progress-change-max-stake': 0,
   'token-price-delta-change-max-stake': 1,
   'anti-user-goal-progress-change-stake-yield': 1,
   'user-goal-progress-change-stake-yield': 0,
   'token-price-delta-change-stake-yield': -1,
   'anti-user-goal-progress-change-lookup-fee': -1,
   'user-goal-progress-change-lookup-fee': 0,
   'token-price-delta-change-lookup-fee': -1,
   'anti-user-goal-progress-change-user-fee': 0,
   'user-goal-progress-change-user-fee': 1,
   'token-price-delta-change-user-fee': 0,
   'anti-user-goal-progress-change-buyback-amount': -1,
   'user-goal-progress-change-buyback-amount': 1,
   'token-price-delta-change-buyback-amount': 0,
   'anti-user-goal-progress-change-reward-amount': 0,
   'user-goal-progress-change-reward-amount': -1,
   'token-price-delta-change-reward-amount': 0},
  0.4484322400265658),
 ({'anti-user-goal-progress-change-max-stake': 0,
   'user-goal-progress-change-max-stake': 1,
   'token-price-delta-change-max-stake': 1,
   'anti-user-goal-progress-change-stake-yield': 1,
   'user-goal-progress-change-stake-yield': 1,
   'token-price-delta-change-stake-yield': -1,
   'anti-user-goal-progress-change-lookup-fee': -1,
   'user-goal-progress-change-lookup-fee': 1,
   'token-price-delta-change-lookup-fee': -1,
   'anti-user-goal-progress-change-user-fee': 1,
   'user-goal-progress-change-user-fee': 1,
   'token-price-delta-change-user-fee': 0,
   'anti-user-goal-progress-change-buyback-amount': -1,
   'user-goal-progress-change-buyback-amount': 1,
   'token-price-delta-change-buyback-amount': 1,
   'anti-user-goal-progress-change-reward-amount': 0,
   'user-goal-progress-change-reward-amount': -1,
   'token-price-delta-change-reward-amount': 0},
  0.44924678262870793),
 ({'anti-user-goal-progress-change-max-stake': 0,
   'user-goal-progress-change-max-stake': 0,
   'token-price-delta-change-max-stake': 1,
   'anti-user-goal-progress-change-stake-yield': 0,
   'user-goal-progress-change-stake-yield': 0,
   'token-price-delta-change-stake-yield': 0,
   'anti-user-goal-progress-change-lookup-fee': 0,
   'user-goal-progress-change-lookup-fee': 0,
   'token-price-delta-change-lookup-fee': 0,
   'anti-user-goal-progress-change-user-fee': 0,
   'user-goal-progress-change-user-fee': 0,
   'token-price-delta-change-user-fee': 0,
   'anti-user-goal-progress-change-buyback-amount': 0,
   'user-goal-progress-change-buyback-amount': 0,
   'token-price-delta-change-buyback-amount': 0,
   'anti-user-goal-progress-change-reward-amount': 0,
   'user-goal-progress-change-reward-amount': 0,
   'token-price-delta-change-reward-amount': 1},
  0.4606627634310311),
 ({'anti-user-goal-progress-change-max-stake': 0,
   'user-goal-progress-change-max-stake': 0,
   'token-price-delta-change-max-stake': 0,
   'anti-user-goal-progress-change-stake-yield': 0,
   'user-goal-progress-change-stake-yield': 0,
   'token-price-delta-change-stake-yield': 0,
   'anti-user-goal-progress-change-lookup-fee': 0,
   'user-goal-progress-change-lookup-fee': 0,
   'token-price-delta-change-lookup-fee': 0,
   'anti-user-goal-progress-change-user-fee': 0,
   'user-goal-progress-change-user-fee': 0,
   'token-price-delta-change-user-fee': 0,
   'anti-user-goal-progress-change-buyback-amount': 0,
   'user-goal-progress-change-buyback-amount': 0,
   'token-price-delta-change-buyback-amount': 0,
   'anti-user-goal-progress-change-reward-amount': 0,
   'user-goal-progress-change-reward-amount': -1,
   'token-price-delta-change-reward-amount': 0},
  0.47341600246214255)]
```

We can see that the top 2 strategies are sensitive to different things, yet produce a similar
fitness-value. This suggests that the algorithm is not getting stuck in evolutionary
blind-alleys, but instead can find alternative paths to the same destination.

If you look at the last organism, you will find that it manages to get into the top 4
by simply giving fewer rewards, the more users we get (which is another way of saying, that
it gives more rewards the fewer users it has, which supports our previous conclusion from
MAD-1).

One key thing to note, is that it takes 3 time-steps for a stimulus to result in an effect
on the state: state changes stimulus, stimulus changes actions, actions change state.
All actions end up with a value between -100 and 100, which it they then use to arbitrarily
act on the world (we have to code this manually, because the _intensity_ of action still
has to get translated into _meaning_ or _effect_).


## Genetic Fuzzing

Because we are no longer manually parameterizing the decision-variables with values that
make sense -- and are instead making it possible for the model to autonomously set those
values at an arbitrary granularity -- we are discovering bugs or "loopholes" in the model
itself.

One thing that we found astonishing is that even with 3 very simple stimuli, the algorithm
was able to come up with very specific strategies for maximizing its fitness. The token-price-delta
is oblivious to any changes older than a week, so you would expect it to be less informative
than it actually is. The user-goal-progress parameters do a lot of the heavy lifting it seems.

Some of the loopholes that we found include:

  * a bug in how we calculate stake-yield, resulting in the yield-percent getting withdrawn instead of stake along with its yield
  * deliberately stopped rewarding users when we hit 100M users
  * would oscillate the reward-amount by tiny fractions of a token maximize growth-rate
  * after fixing stake-yield bug, it figured out that -- since stake-yield is payed out from the rewards-pool stock, it can drain the stock, and pay effectively 0% yield, even though another part of the model presents the yield as 0.01%+, enticing users to stake their tokens instead of selling them

All of these methods worked, and the token price was at 2.8$, after 200 weeks -- the highest it has ever been under the worst-case
scenario-parameterization.

These results are encouraging, since it identifies (in around 10 minutes) where our model is flawed, and what
we can do to fix it. More interestingly, we can probably use this method on other existing models to find
flaws in them -- if there are any.

**TODO: Add plots of these loopholes**
**TODO: Add new model diagram**

## Other Interesting Results

Aside from the various model-bugs the algorithm has uncovered and exploited, it has also presented two
extreme scenarios as far as our heuristics are concerned: either the heuristics get neutralized by the scammers,
resulting in high false-negative-rate and false-positive-rates (which causes an absolute staking bonanza), or
the scammers never manage to catch up, causing the equivalent of a bankruptcy. While the model does not deal
with this directly, the last scenario would involve scammers moving from _mimicry_ to outright _deception_
(i.e. websites that look original, high-quality, and legitimate, but are in fact phishing-scams). Both of these
scenarios will create _more_ demand for threat-intelligence instead of less, which in turn will create more
demand for the security-staking.

## Future Work

Aside from fixing the loopholes, we want to add more stimuli, and have a granularity greater than
`[-1,0,1]`. Also, maybe -- if time allows -- test it against models of popular systems like Uniswap, to see
if it will find bugs in it.

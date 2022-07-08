This is the cadCAD model. It has 71 variables (one of: stock, flow, indicator).
It is meant to represent the the important aspects of the interlock network.
Right now it is slightly broken, but will be fixed soon.

This model is tested by copying the python file in this directory
and pasting it into Jupyter, and then you execute the simulation
and analyze the data with Pandas.

We tried to pick sensible initial values. Some were just completely random
guesses (i.e. page-visits, money-supply, browser-users), while others were
more informed (i.e. we choose a money-supply-multiplier from an actual data
set [in the form of a frequency distribution] of weekly deltas of circulating
supply of USD, from the time period of 2005 to 2022. Turns out, expansions and
contractions in the circulating supply are a very good proxy for things like
interest-rates and taxes. (This data was retrieved from Mathematica -- we will
commit that notebook to this repo real soon -- and pasted into the python
code, hence the complete lack of formatting).

The time-step in the simulation corresponds to 1 week of time. We wanted to
do a _day_ initially, but calculating day-to-day deltas of the money supply was
problematic (i.e. most deltas evaluated to 1.0 because floating-point is not
precise enough for such small deltas).

The coding style is such that the code is _isomorphic_ to the graph
found in the `graphs` directory. This means that the graph is a _map
to the code_. Each arrow in the graph corresponds to a function.
Each function acts as a (metaphorical) channel that sends (metaphorical)
tagged messages to an indicator or a flow (which is the caller of the channel-function).
This lets us delete and rearrange arrows in an order-free fashion. These function have the form
X_updates_Y. The callers of the channel-function are named update_Y. Stocks can only be updated
by flow-functions (which usually have the form update_X_rate). The stocks are updated in 3 phases:
flow-adjustment (which helps prioritize sinks, and conserve-mass), stock-reduction, and
stock-aggregation. These functions have the form adjust_X, reduce_X, aggregate_X. Each
of these phases executes in its own partial-state-update-block, because they cannot execute
simultaneously (many operations are not commutative or associative).

To facilitate this flexibility, we use a list-based arithmetic (i.e. mul_ls, sum_ls, etc)
which act on a flat list of numbers. The div_ls function rewrites every non-leading zero
into 0.0000001, because you cannot divide by zero, and we _usually_ want to capture
growth or decay via division, so zero -- as a practical matter -- represents a tiny
number, instead of _zero_.

There are other plans for the code in the model, that we never got to implement:
service-orders, and delays. Service-orders have to do with the reduction of a
source-stock into sink-stocks -- which sink stocks get prioritized? Currently
they get prioritized at random, to emulate an opaque first-come-first-serve
service order at the time-step-granularity. We plan to add other orders:
largest-demand-first, lowest-demand-first, most-abundant-first, least-abundant-first,
and fair-share (i.e. the source-stock is distributed equally to each sink-stock, regardless
of any demand or abundance).

As for delays, there are a few kinds of those: no-delay (always-latest-value),
blink-delay (sometimes-latest-value), transmission-delay (always-old-value),
blinky-transmission-delay (sometimes-old-value). This would require that the
channel functions implement a queue (somewhere) and control the tempo at
which flows and indicators receive their messages.

The current model has delays in the graph, but the code does not. These 2 things
-- service-orders and delays -- are cool, but not essential for a first-draft
of the model.

Also, every variable (i.e. stock, flow, indicator) is a _tuple_ containing
a current_value and a previous_value: this makes it easy for us to measure
step-to-step deltas.
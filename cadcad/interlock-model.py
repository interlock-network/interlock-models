import numpy as np
import pandas as pd
import plotly
import plotly.express as px
import random
from cadCAD.configuration.utils import bound_norm_random, config_sim, time_step, env_trigger
from cadCAD.configuration import Experiment
from cadCAD.engine import ExecutionMode, ExecutionContext
from cadCAD.engine import Executor
def expectation_updates_staking_enthusiasm (ctx, s):
    if ctx.get ("expectation-multiplier") == None:
        ctx ["expectation-multiplier"] = []
    
    expectation_multiplier = ctx.get ("expectation-multiplier")
    new_val = [4] if lt_eq_ls (get_new_value (s, "expectation") + [0]) [0] else [1]
    append_each (expectation_multiplier, new_val)

def expectation_updates_token_price (ctx, s):
    if ctx.get ("expectation-multiplier") == None:
        ctx ["expectation-multiplier"] = []
    
    expectation_multiplier = ctx.get ("expectation-multiplier")
    new_val = [1] if eq_ls (get_new_value (s, "expectation") + [0]) [0] else diff_ls ([1] + div_ls ([random.randrange (1, 10)] + [100])) if eq_ls (get_new_value (s, "expectation") + [-1]) [0] else diff_ls ([1] + div_ls ([random.randrange (11, 20)] + [100])) if eq_ls (get_new_value (s, "expectation") + [-2]) [0] else sum_ls ([1] + div_ls ([random.randrange (1, 10)] + [100])) if eq_ls (get_new_value (s, "expectation") + [1]) [0] else sum_ls ([1] + div_ls ([random.randrange (11, 20)] + [100])) if eq_ls (get_new_value (s, "expectation") + [2]) [0] else [-100]
    append_each (expectation_multiplier, new_val)

def crypto_hype_updates_interlock_hype (ctx, s):
    if ctx.get ("crypto-hype-growth") == None:
        ctx ["crypto-hype-growth"] = []
    
    crypto_hype_growth = ctx.get ("crypto-hype-growth")
    new_val = div_ls (get_new_value (s, "crypto-hype") + get_old_value (s, "crypto-hype"))
    append_each (crypto_hype_growth, new_val)

def crypto_hype_updates_crypto_invest_rate (ctx, s):
    if ctx.get ("crypto-hype-growth") == None:
        ctx ["crypto-hype-growth"] = []
    
    crypto_hype_growth = ctx.get ("crypto-hype-growth")
    new_val = div_ls (get_new_value (s, "crypto-hype") + get_old_value (s, "crypto-hype"))
    append_each (crypto_hype_growth, new_val)

def crypto_hype_updates_crypto_divest_rate (ctx, s):
    if ctx.get ("crypto-hype-growth") == None:
        ctx ["crypto-hype-growth"] = []
    
    crypto_hype_growth = ctx.get ("crypto-hype-growth")
    new_val = div_ls (get_old_value (s, "crypto-hype") + get_new_value (s, "crypto-hype"))
    append_each (crypto_hype_growth, new_val)

def interlock_hype_updates_intr_invest_rate (ctx, s):
    if ctx.get ("crypto-hype-growth") == None:
        ctx ["crypto-hype-growth"] = []
    
    crypto_hype_growth = ctx.get ("crypto-hype-growth")
    new_val = div_ls (get_new_value (s, "interlock-hype") + get_old_value (s, "interlock-hype"))
    append_each (crypto_hype_growth, new_val)

def interlock_hype_updates_intr_divest_rate (ctx, s):
    if ctx.get ("crypto-hype-growth") == None:
        ctx ["crypto-hype-growth"] = []
    
    crypto_hype_growth = ctx.get ("crypto-hype-growth")
    new_val = div_ls (get_old_value (s, "interlock-hype") + get_new_value (s, "interlock-hype"))
    append_each (crypto_hype_growth, new_val)

def interlock_hype_updates_airlock_adoption_rate (ctx, s):
    if ctx.get ("crypto-hype-growth") == None:
        ctx ["crypto-hype-growth"] = []
    
    crypto_hype_growth = ctx.get ("crypto-hype-growth")
    new_val = div_ls (get_new_value (s, "interlock-hype") + get_old_value (s, "interlock-hype"))
    append_each (crypto_hype_growth, new_val)

def money_growth_rate_updates_money_mint_rate (ctx, s):
    if ctx.get ("growth") == None:
        ctx ["growth"] = []
    
    growth = ctx.get ("growth")
    new_val = get_new_value (s, "money-growth-rate")
    append_each (growth, new_val)

def money_growth_rate_updates_money_reclaim_rate (ctx, s):
    if ctx.get ("growth") == None:
        ctx ["growth"] = []
    
    growth = ctx.get ("growth")
    new_val = get_new_value (s, "money-growth-rate")
    append_each (growth, new_val)

def adjust_token_mint_outflow (s, flow_adjustments):
    flow_list = ["token-mint-reward-rate", "token-mint-supply-rate"]
    random.shuffle (flow_list)
    inventory = get_new_value (s, "token-mint") [0]
    for f in flow_list:
        flow_val = get_new_value (s, f) [0]
        if inventory >= flow_val:
            inventory = (inventory - flow_val)
        elif inventory == flow_val:
            inventory = 0
        else:
            flow_val = inventory
            inventory = 0
        
        flow_adjustments [f] = flow_val


def reduce_token_mint (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "token-mint-reward-rate") + get_new_value (s, "token-mint-supply-rate"))
    return "token-mint", update_state (s, "token-mint", diff_ls (get_new_value (s, "token-mint") + red))

def adjust_token_supply_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "token-hold-rate") [0]
    inventory = get_new_value (s, "token-supply") [0]
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["token-hold-rate"] = flow_val

def aggregate_token_supply (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "token-reward-to-supply-rate") + get_new_value (s, "token-unhold-rate") + get_new_value (s, "token-mint-supply-rate"))
    return "token-supply", update_state (s, "token-supply", sum_ls (get_new_value (s, "token-supply") + agg))

def reduce_token_supply (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "token-hold-rate"))
    return "token-supply", update_state (s, "token-supply", diff_ls (get_new_value (s, "token-supply") + red))

def adjust_token_rewards_pool_outflow (s, flow_adjustments):
    flow_list = ["token-reward-to-held-rate", "token-reward-to-supply-rate"]
    random.shuffle (flow_list)
    inventory = get_new_value (s, "token-rewards-pool") [0]
    for f in flow_list:
        flow_val = get_new_value (s, f) [0]
        if inventory >= flow_val:
            inventory = (inventory - flow_val)
        elif inventory == flow_val:
            inventory = 0
        else:
            flow_val = inventory
            inventory = 0
        
        flow_adjustments [f] = flow_val


def aggregate_token_rewards_pool (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "token-mint-reward-rate"))
    return "token-rewards-pool", update_state (s, "token-rewards-pool", sum_ls (get_new_value (s, "token-rewards-pool") + agg))

def reduce_token_rewards_pool (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "token-reward-to-held-rate") + get_new_value (s, "token-reward-to-supply-rate"))
    return "token-rewards-pool", update_state (s, "token-rewards-pool", diff_ls (get_new_value (s, "token-rewards-pool") + red))

def adjust_token_supply_staked_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "token-unstake-rate") [0]
    inventory = get_new_value (s, "token-supply-staked") [0]
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["token-unstake-rate"] = flow_val

def aggregate_token_supply_staked (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "token-stake-rate"))
    return "token-supply-staked", update_state (s, "token-supply-staked", sum_ls (get_new_value (s, "token-supply-staked") + agg))

def reduce_token_supply_staked (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "token-unstake-rate"))
    return "token-supply-staked", update_state (s, "token-supply-staked", diff_ls (get_new_value (s, "token-supply-staked") + red))

def adjust_token_supply_held_outflow (s, flow_adjustments):
    flow_list = ["token-stake-rate", "token-unhold-rate"]
    random.shuffle (flow_list)
    inventory = get_new_value (s, "token-supply-held") [0]
    for f in flow_list:
        flow_val = get_new_value (s, f) [0]
        if inventory >= flow_val:
            inventory = (inventory - flow_val)
        elif inventory == flow_val:
            inventory = 0
        else:
            flow_val = inventory
            inventory = 0
        
        flow_adjustments [f] = flow_val


def aggregate_token_supply_held (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "token-reward-to-held-rate") + get_new_value (s, "token-unstake-rate") + get_new_value (s, "token-hold-rate"))
    return "token-supply-held", update_state (s, "token-supply-held", sum_ls (get_new_value (s, "token-supply-held") + agg))

def reduce_token_supply_held (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "token-stake-rate") + get_new_value (s, "token-unhold-rate"))
    return "token-supply-held", update_state (s, "token-supply-held", diff_ls (get_new_value (s, "token-supply-held") + red))

def commit_token_mint_supply_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "token-mint-supply-rate", update_state (s, "token-mint-supply-rate", [adjusted_flows ["token-mint-supply-rate"]])

def commit_token_mint_reward_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "token-mint-reward-rate", update_state (s, "token-mint-reward-rate", [adjusted_flows ["token-mint-reward-rate"]])

def commit_token_hold_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "token-hold-rate", update_state (s, "token-hold-rate", [adjusted_flows ["token-hold-rate"]])

def commit_token_unhold_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "token-unhold-rate", update_state (s, "token-unhold-rate", [adjusted_flows ["token-unhold-rate"]])

def commit_token_stake_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "token-stake-rate", update_state (s, "token-stake-rate", [adjusted_flows ["token-stake-rate"]])

def staking_enthusiasm_updates_token_stake_rate (ctx, s):
    if ctx.get ("enthusiasm") == None:
        ctx ["enthusiasm"] = []
    
    enthusiasm = ctx.get ("enthusiasm")
    new_val = get_new_value (s, "staking-enthusiasm")
    append_each (enthusiasm, new_val)

def commit_token_unstake_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "token-unstake-rate", update_state (s, "token-unstake-rate", [adjusted_flows ["token-unstake-rate"]])

def data_value_updates_airlock_revenue_rate (ctx, s):
    if ctx.get ("data-value") == None:
        ctx ["data-value"] = []
    
    data_value = ctx.get ("data-value")
    new_val = get_new_value (s, "data-value")
    append_each (data_value, new_val)

def data_value_updates_token_reward_to_supply_rate (ctx, s):
    if ctx.get ("data-value") == None:
        ctx ["data-value"] = []
    
    data_value = ctx.get ("data-value")
    new_val = get_new_value (s, "data-value")
    append_each (data_value, new_val)

def data_value_updates_token_reward_to_held_rate (ctx, s):
    if ctx.get ("data-value") == None:
        ctx ["data-value"] = []
    
    data_value = ctx.get ("data-value")
    new_val = get_new_value (s, "data-value")
    append_each (data_value, new_val)

def token_reward_to_supply_rate_updates_airlock_adoption_rate (ctx, s):
    if ctx.get ("rewards-supply") == None:
        ctx ["rewards-supply"] = []
    
    rewards_supply = ctx.get ("rewards-supply")
    new_val = div_ls (get_new_value (s, "token-reward-to-supply-rate") + get_new_value (s, "airlock-users"))
    append_each (rewards_supply, new_val)

def token_reward_to_held_rate_updates_airlock_adoption_rate (ctx, s):
    if ctx.get ("rewards-held") == None:
        ctx ["rewards-held"] = []
    
    rewards_held = ctx.get ("rewards-held")
    new_val = div_ls (get_new_value (s, "token-reward-to-held-rate") + get_new_value (s, "airlock-users"))
    append_each (rewards_held, new_val)

def token_reward_to_supply_rate_updates_airlock_abandonment_rate (ctx, s):
    if ctx.get ("rewards-supply") == None:
        ctx ["rewards-supply"] = []
    
    rewards_supply = ctx.get ("rewards-supply")
    new_val = div_ls (get_old_value (s, "token-reward-to-supply-rate") + get_new_value (s, "token-reward-to-supply-rate"))
    append_each (rewards_supply, new_val)

def token_reward_to_held_rate_updates_airlock_abandonment_rate (ctx, s):
    if ctx.get ("rewards-held") == None:
        ctx ["rewards-held"] = []
    
    rewards_held = ctx.get ("rewards-held")
    new_val = div_ls (get_old_value (s, "token-reward-to-held-rate") + get_new_value (s, "token-reward-to-held-rate"))
    append_each (rewards_held, new_val)

def commit_token_reward_to_supply_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "token-reward-to-supply-rate", update_state (s, "token-reward-to-supply-rate", [adjusted_flows ["token-reward-to-supply-rate"]])

def commit_token_reward_to_held_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "token-reward-to-held-rate", update_state (s, "token-reward-to-held-rate", [adjusted_flows ["token-reward-to-held-rate"]])

def adjust_money_mint_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "money-mint-rate") [0]
    inventory = get_new_value (s, "money-mint") [0]
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["money-mint-rate"] = flow_val

def reduce_money_mint (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "money-mint-rate"))
    return "money-mint", update_state (s, "money-mint", diff_ls (get_new_value (s, "money-mint") + red))

def adjust_money_supply_outflow (s, flow_adjustments):
    flow_list = ["crypto-invest-rate", "money-reclaim-rate"]
    random.shuffle (flow_list)
    inventory = get_new_value (s, "money-supply") [0]
    for f in flow_list:
        flow_val = get_new_value (s, f) [0]
        if inventory >= flow_val:
            inventory = (inventory - flow_val)
        elif inventory == flow_val:
            inventory = 0
        else:
            flow_val = inventory
            inventory = 0
        
        flow_adjustments [f] = flow_val


def aggregate_money_supply (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "crypto-divest-rate") + get_new_value (s, "money-mint-rate"))
    return "money-supply", update_state (s, "money-supply", sum_ls (get_new_value (s, "money-supply") + agg))

def reduce_money_supply (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "crypto-invest-rate") + get_new_value (s, "money-reclaim-rate"))
    return "money-supply", update_state (s, "money-supply", diff_ls (get_new_value (s, "money-supply") + red))

def aggregate_money_reclaimed (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "money-reclaim-rate"))
    return "money-reclaimed", update_state (s, "money-reclaimed", sum_ls (get_new_value (s, "money-reclaimed") + agg))

def adjust_crypto_investments_outflow (s, flow_adjustments):
    flow_list = ["crypto-divest-rate", "intr-invest-rate"]
    random.shuffle (flow_list)
    inventory = get_new_value (s, "crypto-investments") [0]
    for f in flow_list:
        flow_val = get_new_value (s, f) [0]
        if inventory >= flow_val:
            inventory = (inventory - flow_val)
        elif inventory == flow_val:
            inventory = 0
        else:
            flow_val = inventory
            inventory = 0
        
        flow_adjustments [f] = flow_val


def aggregate_crypto_investments (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "intr-divest-rate") + get_new_value (s, "crypto-invest-rate"))
    return "crypto-investments", update_state (s, "crypto-investments", sum_ls (get_new_value (s, "crypto-investments") + agg))

def reduce_crypto_investments (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "crypto-divest-rate") + get_new_value (s, "intr-invest-rate"))
    return "crypto-investments", update_state (s, "crypto-investments", diff_ls (get_new_value (s, "crypto-investments") + red))

def adjust_intr_investments_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "intr-divest-rate") [0]
    inventory = get_new_value (s, "intr-investments") [0]
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["intr-divest-rate"] = flow_val

def aggregate_intr_investments (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "intr-invest-rate"))
    return "intr-investments", update_state (s, "intr-investments", sum_ls (get_new_value (s, "intr-investments") + agg))

def reduce_intr_investments (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "intr-divest-rate"))
    return "intr-investments", update_state (s, "intr-investments", diff_ls (get_new_value (s, "intr-investments") + red))

def commit_money_reclaim_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "money-reclaim-rate", update_state (s, "money-reclaim-rate", [adjusted_flows ["money-reclaim-rate"]])

def commit_money_mint_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "money-mint-rate", update_state (s, "money-mint-rate", [adjusted_flows ["money-mint-rate"]])

def commit_crypto_invest_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "crypto-invest-rate", update_state (s, "crypto-invest-rate", [adjusted_flows ["crypto-invest-rate"]])

def commit_intr_invest_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "intr-invest-rate", update_state (s, "intr-invest-rate", [adjusted_flows ["intr-invest-rate"]])

def commit_crypto_divest_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "crypto-divest-rate", update_state (s, "crypto-divest-rate", [adjusted_flows ["crypto-divest-rate"]])

def commit_intr_divest_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "intr-divest-rate", update_state (s, "intr-divest-rate", [adjusted_flows ["intr-divest-rate"]])

def intr_investments_updates_token_hold_rate (ctx, s):
    if ctx.get ("invested") == None:
        ctx ["invested"] = []
    
    invested = ctx.get ("invested")
    new_val = max_ls (diff_ls (get_new_value (s, "intr-investments") + get_old_value (s, "intr-investments")) + [0])
    append_each (invested, new_val)

def intr_investments_updates_token_unhold_rate (ctx, s):
    if ctx.get ("uninvested") == None:
        ctx ["uninvested"] = []
    
    uninvested = ctx.get ("uninvested")
    new_val = max_ls (diff_ls (get_old_value (s, "intr-investments") + get_new_value (s, "intr-investments")) + [0])
    append_each (uninvested, new_val)

def money_supply_updates_crypto_hype (ctx, s):
    if ctx.get ("extra-cash-growth") == None:
        ctx ["extra-cash-growth"] = []
    
    extra_cash_growth = ctx.get ("extra-cash-growth")
    new_val = div_ls (get_new_value (s, "money-supply") + get_old_value (s, "money-supply"))
    append_each (extra_cash_growth, new_val)

def money_supply_updates_token_price (ctx, s):
    if ctx.get ("extra-cash-growth") == None:
        ctx ["extra-cash-growth"] = []
    
    extra_cash_growth = ctx.get ("extra-cash-growth")
    new_val = div_ls (get_new_value (s, "money-supply") + get_old_value (s, "money-supply"))
    append_each (extra_cash_growth, new_val)

def token_supply_updates_token_price (ctx, s):
    if ctx.get ("supply-price-growth") == None:
        ctx ["supply-price-growth"] = []
    
    supply_price_growth = ctx.get ("supply-price-growth")
    new_val = div_ls (get_old_value (s, "token-supply") + get_new_value (s, "token-supply"))
    append_each (supply_price_growth, new_val)

def intr_investments_updates_token_price (ctx, s):
    if ctx.get ("invest-price-growth") == None:
        ctx ["invest-price-growth"] = []
    
    invest_price_growth = ctx.get ("invest-price-growth")
    new_val = div_ls (get_new_value (s, "intr-investments") + get_old_value (s, "intr-investments"))
    append_each (invest_price_growth, new_val)

def token_price_updates_token_profit (ctx, s):
    if ctx.get ("price-delta-pct") == None:
        ctx ["price-delta-pct"] = []
    
    price_delta_pct = ctx.get ("price-delta-pct")
    new_val = div_ls (get_new_value (s, "token-price") + get_old_value (s, "token-price"))
    append_each (price_delta_pct, new_val)

def token_price_updates_airlock_lookup_price (ctx, s):
    if ctx.get ("price-delta-pct") == None:
        ctx ["price-delta-pct"] = []
    
    price_delta_pct = ctx.get ("price-delta-pct")
    new_val = div_ls (get_new_value (s, "token-price") + get_old_value (s, "token-price"))
    append_each (price_delta_pct, new_val)

def airlock_lookup_price_updates_intr_invest_rate (ctx, s):
    if ctx.get ("lookup-price") == None:
        ctx ["lookup-price"] = []
    
    lookup_price = ctx.get ("lookup-price")
    new_val = get_new_value (s, "airlock-lookup-price")
    append_each (lookup_price, new_val)

def token_price_updates_intr_invest_rate (ctx, s):
    if ctx.get ("price-delta-pct") == None:
        ctx ["price-delta-pct"] = []
    
    price_delta_pct = ctx.get ("price-delta-pct")
    new_val = div_ls (get_old_value (s, "token-price") + get_new_value (s, "token-price"))
    append_each (price_delta_pct, new_val)

def token_price_updates_token_reward_to_supply_rate (ctx, s):
    if ctx.get ("price-delta-pct") == None:
        ctx ["price-delta-pct"] = []
    
    price_delta_pct = ctx.get ("price-delta-pct")
    new_val = div_ls (get_new_value (s, "token-price") + get_old_value (s, "token-price"))
    append_each (price_delta_pct, new_val)

def token_price_updates_token_reward_to_held_rate (ctx, s):
    if ctx.get ("price-delta-pct") == None:
        ctx ["price-delta-pct"] = []
    
    price_delta_pct = ctx.get ("price-delta-pct")
    new_val = div_ls (get_new_value (s, "token-price") + get_old_value (s, "token-price"))
    append_each (price_delta_pct, new_val)

def token_price_updates_airlock_adoption_rate (ctx, s):
    if ctx.get ("price") == None:
        ctx ["price"] = []
    
    price = ctx.get ("price")
    new_val = get_new_value (s, "token-price")
    append_each (price, new_val)

def token_price_updates_airlock_abandonment_rate (ctx, s):
    if ctx.get ("price") == None:
        ctx ["price"] = []
    
    price = ctx.get ("price")
    new_val = get_new_value (s, "token-price")
    append_each (price, new_val)

def token_profit_updates_intr_divest_rate (ctx, s):
    if ctx.get ("profit-delta-pct") == None:
        ctx ["profit-delta-pct"] = []
    
    profit_delta_pct = ctx.get ("profit-delta-pct")
    new_val = div_ls (get_new_value (s, "token-profit") + get_old_value (s, "token-profit"))
    append_each (profit_delta_pct, new_val)

def stake_yield_updates_token_reward_to_held_rate (ctx, s):
    if ctx.get ("stake-yield") == None:
        ctx ["stake-yield"] = []
    
    stake_yield = ctx.get ("stake-yield")
    new_val = mul_ls (get_new_value (s, "token-unstake-rate") + get_new_value (s, "stake-yield"))
    append_each (stake_yield, new_val)

def adjust_page_visits_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "scam-page-visit-rate") [0]
    inventory = get_new_value (s, "page-visits") [0]
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["scam-page-visit-rate"] = flow_val

def reduce_page_visits (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "scam-page-visit-rate"))
    return "page-visits", update_state (s, "page-visits", diff_ls (get_new_value (s, "page-visits") + red))

def adjust_airlock_lookups_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "grey-area-entity-rate") [0]
    inventory = get_new_value (s, "airlock-lookups") [0]
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["grey-area-entity-rate"] = flow_val

def aggregate_airlock_lookups (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "airlock-lookup-rate"))
    return "airlock-lookups", update_state (s, "airlock-lookups", sum_ls (get_new_value (s, "airlock-lookups") + agg))

def reduce_airlock_lookups (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "grey-area-entity-rate"))
    return "airlock-lookups", update_state (s, "airlock-lookups", diff_ls (get_new_value (s, "airlock-lookups") + red))

def adjust_potential_airlock_lookups_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "airlock-lookup-rate") [0]
    inventory = get_new_value (s, "potential-airlock-lookups") [0]
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["airlock-lookup-rate"] = flow_val

def reduce_potential_airlock_lookups (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "airlock-lookup-rate"))
    return "potential-airlock-lookups", update_state (s, "potential-airlock-lookups", diff_ls (get_new_value (s, "potential-airlock-lookups") + red))

def adjust_browsing_data_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "airlock-share-rate") [0]
    inventory = get_new_value (s, "browsing-data") [0]
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["airlock-share-rate"] = flow_val

def reduce_browsing_data (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "airlock-share-rate"))
    return "browsing-data", update_state (s, "browsing-data", diff_ls (get_new_value (s, "browsing-data") + red))

def aggregate_airlock_data_shared (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "airlock-share-rate"))
    return "airlock-data-shared", update_state (s, "airlock-data-shared", sum_ls (get_new_value (s, "airlock-data-shared") + agg))

def aggregate_airlock_revenue (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "airlock-revenue-rate"))
    return "airlock-revenue", update_state (s, "airlock-revenue", sum_ls (get_new_value (s, "airlock-revenue") + agg))

def adjust_data_buyer_money_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "airlock-revenue-rate") [0]
    inventory = get_new_value (s, "data-buyer-money") [0]
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["airlock-revenue-rate"] = flow_val

def reduce_data_buyer_money (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "airlock-revenue-rate"))
    return "data-buyer-money", update_state (s, "data-buyer-money", diff_ls (get_new_value (s, "data-buyer-money") + red))

def adjust_browser_users_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "airlock-adoption-rate") [0]
    inventory = get_new_value (s, "browser-users") [0]
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["airlock-adoption-rate"] = flow_val

def aggregate_browser_users (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "airlock-abandonment-rate"))
    return "browser-users", update_state (s, "browser-users", sum_ls (get_new_value (s, "browser-users") + agg))

def reduce_browser_users (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "airlock-adoption-rate"))
    return "browser-users", update_state (s, "browser-users", diff_ls (get_new_value (s, "browser-users") + red))

def adjust_airlock_users_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "airlock-abandonment-rate") [0]
    inventory = get_new_value (s, "airlock-users") [0]
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["airlock-abandonment-rate"] = flow_val

def aggregate_airlock_users (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "airlock-adoption-rate"))
    return "airlock-users", update_state (s, "airlock-users", sum_ls (get_new_value (s, "airlock-users") + agg))

def reduce_airlock_users (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "airlock-abandonment-rate"))
    return "airlock-users", update_state (s, "airlock-users", diff_ls (get_new_value (s, "airlock-users") + red))

def adjust_grey_area_entities_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "resolution-rate") [0]
    inventory = get_new_value (s, "grey-area-entities") [0]
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["resolution-rate"] = flow_val

def aggregate_grey_area_entities (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "grey-area-entity-rate"))
    return "grey-area-entities", update_state (s, "grey-area-entities", sum_ls (get_new_value (s, "grey-area-entities") + agg))

def reduce_grey_area_entities (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "resolution-rate"))
    return "grey-area-entities", update_state (s, "grey-area-entities", diff_ls (get_new_value (s, "grey-area-entities") + red))

def aggregate_resolved_entities (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "resolution-rate"))
    return "resolved-entities", update_state (s, "resolved-entities", sum_ls (get_new_value (s, "resolved-entities") + agg))

def adjust_scam_page_visits_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "scam-page-success-rate") [0]
    inventory = get_new_value (s, "scam-page-visits") [0]
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["scam-page-success-rate"] = flow_val

def aggregate_scam_page_visits (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "scam-page-visit-rate"))
    return "scam-page-visits", update_state (s, "scam-page-visits", sum_ls (get_new_value (s, "scam-page-visits") + agg))

def reduce_scam_page_visits (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "scam-page-success-rate"))
    return "scam-page-visits", update_state (s, "scam-page-visits", diff_ls (get_new_value (s, "scam-page-visits") + red))

def aggregate_scam_page_successes (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "scam-page-success-rate"))
    return "scam-page-successes", update_state (s, "scam-page-successes", sum_ls (get_new_value (s, "scam-page-successes") + agg))

def adjust_potential_scam_profits_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "scam-profit-rate") [0]
    inventory = get_new_value (s, "potential-scam-profits") [0]
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["scam-profit-rate"] = flow_val

def reduce_potential_scam_profits (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "scam-profit-rate"))
    return "potential-scam-profits", update_state (s, "potential-scam-profits", diff_ls (get_new_value (s, "potential-scam-profits") + red))

def adjust_scam_profits_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "scam-upkeep-rate") [0]
    inventory = get_new_value (s, "scam-profits") [0]
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["scam-upkeep-rate"] = flow_val

def aggregate_scam_profits (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "scam-profit-rate"))
    return "scam-profits", update_state (s, "scam-profits", sum_ls (get_new_value (s, "scam-profits") + agg))

def reduce_scam_profits (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "scam-upkeep-rate"))
    return "scam-profits", update_state (s, "scam-profits", diff_ls (get_new_value (s, "scam-profits") + red))

def aggregate_scam_upkeep (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "scam-upkeep-rate"))
    return "scam-upkeep", update_state (s, "scam-upkeep", sum_ls (get_new_value (s, "scam-upkeep") + agg))

def commit_airlock_adoption_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "airlock-adoption-rate", update_state (s, "airlock-adoption-rate", [adjusted_flows ["airlock-adoption-rate"]])

def commit_airlock_abandonment_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "airlock-abandonment-rate", update_state (s, "airlock-abandonment-rate", [adjusted_flows ["airlock-abandonment-rate"]])

def commit_airlock_lookup_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "airlock-lookup-rate", update_state (s, "airlock-lookup-rate", [adjusted_flows ["airlock-lookup-rate"]])

def commit_grey_area_entity_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "grey-area-entity-rate", update_state (s, "grey-area-entity-rate", [adjusted_flows ["grey-area-entity-rate"]])

def commit_resolution_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "resolution-rate", update_state (s, "resolution-rate", [adjusted_flows ["resolution-rate"]])

def resolved_entities_updates_token_unstake_rate (ctx, s):
    if ctx.get ("resolutions") == None:
        ctx ["resolutions"] = []
    
    resolutions = ctx.get ("resolutions")
    new_val = diff_ls (get_new_value (s, "resolved-entities") + get_old_value (s, "resolved-entities"))
    append_each (resolutions, new_val)

def commit_airlock_share_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "airlock-share-rate", update_state (s, "airlock-share-rate", [adjusted_flows ["airlock-share-rate"]])

def commit_airlock_revenue_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "airlock-revenue-rate", update_state (s, "airlock-revenue-rate", [adjusted_flows ["airlock-revenue-rate"]])

def commit_scam_page_visit_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "scam-page-visit-rate", update_state (s, "scam-page-visit-rate", [adjusted_flows ["scam-page-visit-rate"]])

def commit_scam_page_success_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "scam-page-success-rate", update_state (s, "scam-page-success-rate", [adjusted_flows ["scam-page-success-rate"]])

def scam_page_successes_updates_scam_profit_rate (ctx, s):
    if ctx.get ("total-pages") == None:
        ctx ["total-pages"] = []
    
    total_pages = ctx.get ("total-pages")
    new_val = diff_ls (get_new_value (s, "scam-page-successes") + get_old_value (s, "scam-page-successes"))
    append_each (total_pages, new_val)

def scam_profits_per_page_updates_scam_profit_rate (ctx, s):
    if ctx.get ("cash-per-page") == None:
        ctx ["cash-per-page"] = []
    
    cash_per_page = ctx.get ("cash-per-page")
    new_val = get_new_value (s, "scam-profits-per-page")
    append_each (cash_per_page, new_val)

def commit_scam_profit_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "scam-profit-rate", update_state (s, "scam-profit-rate", [adjusted_flows ["scam-profit-rate"]])

def commit_scam_upkeep_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "scam-upkeep-rate", update_state (s, "scam-upkeep-rate", [adjusted_flows ["scam-upkeep-rate"]])

def airlock_users_updates_scam_page_success_rate (ctx, s):
    if ctx.get ("user-share") == None:
        ctx ["user-share"] = []
    
    user_share = ctx.get ("user-share")
    new_val = div_ls (get_new_value (s, "airlock-users") + get_new_value (s, "browser-users"))
    append_each (user_share, new_val)

def airlock_users_updates_airlock_lookup_rate (ctx, s):
    if ctx.get ("user-share") == None:
        ctx ["user-share"] = []
    
    user_share = ctx.get ("user-share")
    new_val = div_ls (get_new_value (s, "airlock-users") + get_new_value (s, "browser-users"))
    append_each (user_share, new_val)

def airlock_data_shared_updates_token_reward_to_supply_rate (ctx, s):
    if ctx.get ("shared") == None:
        ctx ["shared"] = []
    
    shared = ctx.get ("shared")
    new_val = diff_ls (get_new_value (s, "airlock-data-shared") + get_old_value (s, "airlock-data-shared"))
    append_each (shared, new_val)

def airlock_data_shared_updates_token_reward_to_held_rate (ctx, s):
    if ctx.get ("shared") == None:
        ctx ["shared"] = []
    
    shared = ctx.get ("shared")
    new_val = diff_ls (get_new_value (s, "airlock-data-shared") + get_old_value (s, "airlock-data-shared"))
    append_each (shared, new_val)

def airlock_lookup_rate_updates_intr_invest_rate (ctx, s):
    if ctx.get ("lookups") == None:
        ctx ["lookups"] = []
    
    lookups = ctx.get ("lookups")
    new_val = get_new_value (s, "airlock-lookup-rate")
    append_each (lookups, new_val)

def airlock_users_updates_airlock_share_rate (ctx, s):
    if ctx.get ("user-share") == None:
        ctx ["user-share"] = []
    
    user_share = ctx.get ("user-share")
    new_val = div_ls (get_new_value (s, "airlock-users") + get_new_value (s, "browser-users"))
    append_each (user_share, new_val)

def airlock_revenue_updates_token_hold_rate (ctx, s):
    if ctx.get ("revenue-buys") == None:
        ctx ["revenue-buys"] = []
    
    revenue_buys = ctx.get ("revenue-buys")
    new_val = div_ls (diff_ls (get_new_value (s, "airlock-revenue") + get_old_value (s, "airlock-revenue")) + get_new_value (s, "token-price"))
    append_each (revenue_buys, new_val)

def scam_page_success_rate_updates_scammer_innovation (ctx, s):
    if ctx.get ("urgency") == None:
        ctx ["urgency"] = []
    
    urgency = ctx.get ("urgency")
    new_val = div_ls (get_old_value (s, "scam-page-success-rate") + get_new_value (s, "scam-page-success-rate"))
    append_each (urgency, new_val)

def scammer_innovation_updates_scam_upkeep_rate (ctx, s):
    if ctx.get ("profit-diverted-to-innovate") == None:
        ctx ["profit-diverted-to-innovate"] = []
    
    profit_diverted_to_innovate = ctx.get ("profit-diverted-to-innovate")
    new_val = mul_ls (get_new_value (s, "scammer-innovation"))
    append_each (profit_diverted_to_innovate, new_val)

def scammer_innovation_updates_heuristic_contradictions (ctx, s):
    if ctx.get ("innovation") == None:
        ctx ["innovation"] = []
    
    innovation = ctx.get ("innovation")
    new_val = sum_ls (get_new_value (s, "heuristic-contradictions") + mul_ls (div_ls ([random.randrange (1, 50)] + [100]) + get_new_value (s, "heuristic-contradictions") + get_new_value (s, "scammer-innovation")))
    append_each (innovation, new_val)

def heuristic_contradictions_updates_scam_page_success_rate (ctx, s):
    if ctx.get ("pass-through") == None:
        ctx ["pass-through"] = []
    
    pass_through = ctx.get ("pass-through")
    new_val = diff_ls ([1] + div_ls (get_new_value (s, "heuristic-contradictions") + [100]))
    append_each (pass_through, new_val)

def heuristic_contradictions_updates_airlock_abandonment_rate (ctx, s):
    if ctx.get ("contradiction-delta") == None:
        ctx ["contradiction-delta"] = []
    
    contradiction_delta = ctx.get ("contradiction-delta")
    new_val = div_ls (get_new_value (s, "heuristic-contradictions") + get_old_value (s, "heuristic-contradictions"))
    append_each (contradiction_delta, new_val)

def heuristic_contradictions_updates_grey_area_entity_rate (ctx, s):
    if ctx.get ("contradictions") == None:
        ctx ["contradictions"] = []
    
    contradictions = ctx.get ("contradictions")
    new_val = div_ls (get_new_value (s, "heuristic-contradictions") + [100])
    append_each (contradictions, new_val)

def grey_area_entities_updates_staking_opportunities (ctx, s):
    if ctx.get ("grey-stake") == None:
        ctx ["grey-stake"] = []
    
    grey_stake = ctx.get ("grey-stake")
    new_val = mul_ls ([0.5] + get_new_value (s, "grey-area-entities"))
    append_each (grey_stake, new_val)

def staking_opportunities_updates_token_stake_rate (ctx, s):
    if ctx.get ("staking-ops") == None:
        ctx ["staking-ops"] = []
    
    staking_ops = ctx.get ("staking-ops")
    new_val = get_new_value (s, "staking-opportunities")
    append_each (staking_ops, new_val)

def max_total_stake_per_entity_updates_token_stake_rate (ctx, s):
    if ctx.get ("max-per-entity") == None:
        ctx ["max-per-entity"] = []
    
    max_per_entity = ctx.get ("max-per-entity")
    new_val = get_new_value (s, "max-total-stake-per-entity")
    append_each (max_per_entity, new_val)

def heuristic_contradictions_updates_heuristic_innovation (ctx, s):
    if ctx.get ("urgency") == None:
        ctx ["urgency"] = []
    
    urgency = ctx.get ("urgency")
    new_val = get_new_value (s, "heuristic-contradictions")
    append_each (urgency, new_val)

def heuristic_innovation_updates_heuristic_contradictions (ctx, s):
    if ctx.get ("innovation") == None:
        ctx ["innovation"] = []
    
    innovation = ctx.get ("innovation")
    new_val = diff_ls (get_new_value (s, "heuristic-contradictions") + mul_ls (div_ls ([random.randrange (1, 50)] + [100]) + get_new_value (s, "heuristic-contradictions") + get_new_value (s, "heuristic-innovation")))
    append_each (innovation, new_val)

def max_ls (ls):
    if len (ls) == 0:
        return []
    
    ret_val = ls [0]
    for n in ls:
        ret_val = max (ret_val, n)

    return [ret_val]


def min_ls (ls):
    if len (ls) == 0:
        return []
    
    ret_val = ls [0]
    for n in ls:
        ret_val = min (ret_val, n)

    return [ret_val]


def diff_ls (ls):
    if len (ls) == 0:
        return []
    
    ret_val = (2 * ls [0])
    for n in ls:
        ret_val = (ret_val - n)

    return [ret_val]


def sum_ls (ls):
    if len (ls) == 0:
        return []
    
    ret_val = 0
    for n in ls:
        ret_val = (ret_val + n)

    return [ret_val]


def div_ls (ls):
    if len (ls) == 0:
        return []
    elif len (ls) == 1:
        return ls
    
    ret_val = 0
    first = 1
    for n in ls:
        if first == 1:
            ret_val = n
            first = 0
        elif first == 0:
            if n == 0:
                ret_val = (ret_val / 0.000000001)
            else:
                ret_val = (ret_val / n)
            
        

    return [ret_val]


def mul_ls (ls):
    if len (ls) == 0:
        return []
    elif len (ls) == 1:
        return ls
    
    ret_val = 1
    first = 1
    for n in ls:
        if first == 1:
            ret_val = n
            first = 0
        elif first == 0:
            if n == 0:
                return [0]
            else:
                ret_val = (ret_val * n)
            
        

    return [ret_val]


def eq_ls (ls):
    if len (ls) == 0:
        return []
    elif len (ls) == 1:
        return [0]
    
    ret_val = 1
    first = 1
    prev_val = 0
    for n in ls:
        if first == 1:
            prev_val = n
            first = 0
        elif first == 0:
            ret_val = prev_val == n
            if ret_val == 0:
                return [ret_val]
            
            prev_val = n
        

    return [ret_val]


def lt_ls (ls):
    if len (ls) == 0:
        return []
    elif len (ls) == 1:
        return [0]
    
    ret_val = 1
    first = 1
    prev_val = 0
    for n in ls:
        if first == 1:
            prev_val = n
            first = 0
        elif first == 0:
            ret_val = prev_val < n
            if ret_val == 0:
                return [ret_val]
            
            prev_val = n
        

    return [ret_val]


def lt_eq_ls (ls):
    if len (ls) == 0:
        return []
    elif len (ls) == 1:
        return [0]
    
    ret_val = 1
    first = 1
    prev_val = 0
    for n in ls:
        if first == 1:
            prev_val = n
            first = 0
        elif first == 0:
            ret_val = prev_val <= n
            if ret_val == 0:
                return [ret_val]
            
            prev_val = n
        

    return [ret_val]


def gt_ls (ls):
    if len (ls) == 0:
        return []
    elif len (ls) == 1:
        return [0]
    
    ret_val = 1
    first = 1
    prev_val = 0
    for n in ls:
        if first == 1:
            prev_val = n
            first = 0
        elif first == 0:
            ret_val = prev_val > n
            if ret_val == 0:
                return [ret_val]
            
            prev_val = n
        

    return [ret_val]


def gt_eq_ls (ls):
    if len (ls) == 0:
        return []
    elif len (ls) == 1:
        return [0]
    
    ret_val = 1
    first = 1
    prev_val = 0
    for n in ls:
        if first == 1:
            prev_val = n
            first = 0
        elif first == 0:
            ret_val = prev_val >= n
            if ret_val == 0:
                return [ret_val]
            
            prev_val = n
        

    return [ret_val]


def choose_distro (distro):
    summage = 0
    i = 0
    for tup in distro:
        summage = (summage + tup [0])

    choice = random.randrange (1, summage)
    for tup in distro:
        i = (i + tup [0])
        if i >= choice:
            return [tup [1]]
        



def append_each (target, values):
    for v in values:
        target.append (v)



def get_new_value (s, name):
    return s.get (name) [0]


def get_old_value (s, name):
    return s.get (name) [1]


def initialize_state (val):
    if isinstance (val, list):
        return val, val
    elif isinstance (val, float):
        return [val], [val]
    elif isinstance (val, int):
        return [val], [val]
    


def update_state (s, name, val):
    return val, s.get (name) [0]


def tuple_to_value (x):
    if isinstance (x, tuple):
        if isinstance (x [0], list):
            return x [0] [0]
        
    
    return x


def show_columns ():
    ret = list (sim_res.columns)
    ret.sort ()
    return ret


def plot_lines (data, x_vars, y_vars):
    fig = px.line (data, x=x_vars, y=y_vars, facet_row='simulation', facet_col='run', height=800, template='seaborn')
    fig.update_layout (margin=dict(l=20, r=20, t=20, b=20),)
    return fig


def plot_log_lines (data, x_vars, y_vars):
    fig = px.line (data, x=x_vars, y=y_vars, log_y=True, facet_row='simulation', facet_col='run', height=800, template='seaborn')
    fig.update_layout (margin=dict(l=20, r=20, t=20, b=20),)
    return fig


def adjust_all_flows (_params, substep, sH, s, _input, **kwargs):
    flow_adjustments = {}
    adjust_scam_profits_outflow (s, flow_adjustments)
    adjust_potential_scam_profits_outflow (s, flow_adjustments)
    adjust_scam_page_visits_outflow (s, flow_adjustments)
    adjust_page_visits_outflow (s, flow_adjustments)
    adjust_data_buyer_money_outflow (s, flow_adjustments)
    adjust_browsing_data_outflow (s, flow_adjustments)
    adjust_grey_area_entities_outflow (s, flow_adjustments)
    adjust_airlock_lookups_outflow (s, flow_adjustments)
    adjust_potential_airlock_lookups_outflow (s, flow_adjustments)
    adjust_airlock_users_outflow (s, flow_adjustments)
    adjust_browser_users_outflow (s, flow_adjustments)
    adjust_intr_investments_outflow (s, flow_adjustments)
    adjust_crypto_investments_outflow (s, flow_adjustments)
    adjust_money_mint_outflow (s, flow_adjustments)
    adjust_money_supply_outflow (s, flow_adjustments)
    adjust_token_rewards_pool_outflow (s, flow_adjustments)
    adjust_token_supply_staked_outflow (s, flow_adjustments)
    adjust_token_supply_held_outflow (s, flow_adjustments)
    adjust_token_supply_outflow (s, flow_adjustments)
    adjust_token_mint_outflow (s, flow_adjustments)
    return "flow-adjustments", flow_adjustments


def update_heuristic_innovation (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    heuristic_contradictions_updates_heuristic_innovation (ctx, s)
    heuristic_innovation = ctx.get ("urgency")
    return "heuristic-innovation", update_state (s, "heuristic-innovation", heuristic_innovation)


def update_scammer_innovation (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    scam_page_success_rate_updates_scammer_innovation (ctx, s)
    scammer_innovation = ctx.get ("urgency")
    return "scammer-innovation", update_state (s, "scammer-innovation", scammer_innovation)


def update_scam_profits_per_page (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    scam_profits_per_page = min_ls ([100] + max_ls ([1] + [random.randrange (1, 100)]))
    return "scam-profits-per-page", update_state (s, "scam-profits-per-page", scam_profits_per_page)


def update_stake_yield (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    stake_yield = min_ls ([0.02] + max_ls ([0.01] + choose_distro ([(1, 0.01), (1, 0.02)])))
    return "stake-yield", update_state (s, "stake-yield", stake_yield)


def update_max_total_stake_per_entity (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    max_total_stake_per_entity = min_ls ([500] + max_ls ([100] + [random.randrange (100, 500)]))
    return "max-total-stake-per-entity", update_state (s, "max-total-stake-per-entity", max_total_stake_per_entity)


def update_staking_opportunities (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    grey_area_entities_updates_staking_opportunities (ctx, s)
    staking_opportunities = min_ls ([3000000000000] + max_ls ([0] + ctx.get ("grey-stake")))
    return "staking-opportunities", update_state (s, "staking-opportunities", staking_opportunities)


def update_heuristic_contradictions (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    heuristic_innovation_updates_heuristic_contradictions (ctx, s)
    scammer_innovation_updates_heuristic_contradictions (ctx, s)
    heuristic_contradictions = min_ls ([100] + max_ls ([0] + max_ls ([random.randrange (5, 15)] + sum_ls (ctx.get ("innovation")))))
    return "heuristic-contradictions", update_state (s, "heuristic-contradictions", heuristic_contradictions)


def update_data_value (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    data_value = min_ls (div_ls ([600] + [1000]) + max_ls (div_ls ([100] + [1000]) + div_ls ([random.randrange (100, 600)] + [1000])))
    return "data-value", update_state (s, "data-value", data_value)


def update_staking_enthusiasm (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    expectation_updates_staking_enthusiasm (ctx, s)
    staking_enthusiasm = min_ls ([100] + max_ls ([0] + mul_ls (ctx.get ("expectation-multiplier") + div_ls ([random.randrange (5, 25)] + [100]))))
    return "staking-enthusiasm", update_state (s, "staking-enthusiasm", staking_enthusiasm)


def update_money_growth_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    money_growth_rate = min_ls (div_ls ([1017] + [1000]) + max_ls (div_ls ([988] + [1000]) + choose_distro ([(1, 0.988), (2, 0.991), (2, 0.992), (5, 0.993), (7, 0.994), (10, 0.995), (38, 0.997), (80, 0.998), (124, 0.999), (145, 1.0), (127, 1.001), (105, 1.002), (68, 1.003), (35, 1.004), (27, 1.005), (29, 1.006), (12, 1.007), (4, 1.008), (2, 1.009), (3, 1.01), (1, 1.017)])))
    return "money-growth-rate", update_state (s, "money-growth-rate", money_growth_rate)


def update_crypto_hype (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    money_supply_updates_crypto_hype (ctx, s)
    crypto_hype = min_ls ([100] + max_ls ([1] + mul_ls (get_new_value (s, "crypto-hype") + ctx.get ("extra-cash-growth"))))
    return "crypto-hype", update_state (s, "crypto-hype", crypto_hype)


def update_interlock_hype (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    crypto_hype_updates_interlock_hype (ctx, s)
    interlock_hype = min_ls ([100] + max_ls ([1] + mul_ls (get_new_value (s, "interlock-hype") + ctx.get ("crypto-hype-growth"))))
    return "interlock-hype", update_state (s, "interlock-hype", interlock_hype)


def update_token_profit (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    token_price_updates_token_profit (ctx, s)
    token_profit = ctx.get ("price-delta-pct")
    return "token-profit", update_state (s, "token-profit", token_profit)


def update_airlock_lookup_price (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    token_price_updates_airlock_lookup_price (ctx, s)
    airlock_lookup_price = min_ls ([50] + max_ls ([1] + div_ls (get_new_value (s, "airlock-lookup-price") + ctx.get ("price-delta-pct"))))
    return "airlock-lookup-price", update_state (s, "airlock-lookup-price", airlock_lookup_price)


def update_token_price (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    token_supply_updates_token_price (ctx, s)
    intr_investments_updates_token_price (ctx, s)
    money_supply_updates_token_price (ctx, s)
    expectation_updates_token_price (ctx, s)
    token_price = min_ls ([60] + max_ls ([0.01] + div_ls (sum_ls (mul_ls (get_new_value (s, "token-price") + ctx.get ("expectation-multiplier") + [4]) + mul_ls (get_new_value (s, "token-price") + ctx.get ("invest-price-growth")) + mul_ls (get_new_value (s, "token-price") + ctx.get ("supply-price-growth"))) + [6])))
    return "token-price", update_state (s, "token-price", token_price)


def update_expectation (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    expectation = min_ls ([2] + max_ls ([-2] + choose_distro ([(1, 2), (1, -1), (6, 1)]) if eq_ls (get_new_value (s, "expectation") + [-2]) [0] else choose_distro ([(1, 2), (6, -2), (7, -1), (10, 1)]) if eq_ls (get_new_value (s, "expectation") + [-1]) [0] else choose_distro ([(1, 2), (1, 0), (3, -1)]) if eq_ls (get_new_value (s, "expectation") + [0]) [0] else choose_distro ([(2, -2), (3, 0), (5, 2), (9, -1), (11, 1)]) if eq_ls (get_new_value (s, "expectation") + [1]) [0] else choose_distro ([(1, 0), (4, 1), (4, -1), (5, 2)]) if eq_ls (get_new_value (s, "expectation") + [2]) [0] else [-100]))
    return "expectation", update_state (s, "expectation", expectation)


def update_scam_upkeep_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    scammer_innovation_updates_scam_upkeep_rate (ctx, s)
    scam_upkeep_rate = mul_ls (get_new_value (s, "scam-profits") + [1.01] + ctx.get ("profit-diverted-to-innovate"))
    return "scam-upkeep-rate", update_state (s, "scam-upkeep-rate", scam_upkeep_rate)


def update_scam_profit_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    scam_profits_per_page_updates_scam_profit_rate (ctx, s)
    scam_page_successes_updates_scam_profit_rate (ctx, s)
    scam_profit_rate = mul_ls (ctx.get ("total-pages") + ctx.get ("cash-per-page"))
    return "scam-profit-rate", update_state (s, "scam-profit-rate", scam_profit_rate)


def update_scam_page_success_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    airlock_users_updates_scam_page_success_rate (ctx, s)
    heuristic_contradictions_updates_scam_page_success_rate (ctx, s)
    scam_page_success_rate = diff_ls (mul_ls ([0.4] + get_new_value (s, "scam-page-visits")) + mul_ls ([0.4] + get_new_value (s, "scam-page-visits") + mul_ls (ctx.get ("pass-through") + ctx.get ("user-share"))))
    return "scam-page-success-rate", update_state (s, "scam-page-success-rate", scam_page_success_rate)


def update_scam_page_visit_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    scam_page_visit_rate = mul_ls ([1] + [1000000])
    return "scam-page-visit-rate", update_state (s, "scam-page-visit-rate", scam_page_visit_rate)


def update_airlock_revenue_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    data_value_updates_airlock_revenue_rate (ctx, s)
    airlock_revenue_rate = mul_ls (ctx.get ("data-value") + diff_ls (get_new_value (s, "airlock-data-shared") + get_old_value (s, "airlock-data-shared")))
    return "airlock-revenue-rate", update_state (s, "airlock-revenue-rate", airlock_revenue_rate)


def update_airlock_share_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    airlock_users_updates_airlock_share_rate (ctx, s)
    airlock_share_rate = mul_ls (ctx.get ("user-share") + get_new_value (s, "browsing-data"))
    return "airlock-share-rate", update_state (s, "airlock-share-rate", airlock_share_rate)


def update_resolution_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    resolution_rate = get_old_value (s, "grey-area-entity-rate")
    return "resolution-rate", update_state (s, "resolution-rate", resolution_rate)


def update_grey_area_entity_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    heuristic_contradictions_updates_grey_area_entity_rate (ctx, s)
    grey_area_entity_rate = mul_ls (get_new_value (s, "airlock-lookups") + ctx.get ("contradictions"))
    return "grey-area-entity-rate", update_state (s, "grey-area-entity-rate", grey_area_entity_rate)


def update_airlock_lookup_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    airlock_users_updates_airlock_lookup_rate (ctx, s)
    airlock_lookup_rate = mul_ls (get_new_value (s, "page-visits") + ctx.get ("user-share") + [2])
    return "airlock-lookup-rate", update_state (s, "airlock-lookup-rate", airlock_lookup_rate)


def update_airlock_abandonment_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    token_reward_to_held_rate_updates_airlock_abandonment_rate (ctx, s)
    token_reward_to_supply_rate_updates_airlock_abandonment_rate (ctx, s)
    heuristic_contradictions_updates_airlock_abandonment_rate (ctx, s)
    token_price_updates_airlock_abandonment_rate (ctx, s)
    airlock_abandonment_rate = mul_ls (ctx.get ("contradiction-delta") + max_ls ([1] + get_new_value (s, "airlock-abandonment-rate")) + mul_ls (ctx.get ("price") + div_ls (sum_ls (ctx.get ("rewards-supply") + ctx.get ("rewards-held")) + [2])))
    return "airlock-abandonment-rate", update_state (s, "airlock-abandonment-rate", airlock_abandonment_rate)


def update_airlock_adoption_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    token_price_updates_airlock_adoption_rate (ctx, s)
    token_reward_to_held_rate_updates_airlock_adoption_rate (ctx, s)
    token_reward_to_supply_rate_updates_airlock_adoption_rate (ctx, s)
    interlock_hype_updates_airlock_adoption_rate (ctx, s)
    airlock_adoption_rate = mul_ls (ctx.get ("crypto-hype-growth") + max_ls ([20] + get_new_value (s, "airlock-adoption-rate")) + mul_ls (ctx.get ("price") + div_ls (sum_ls (ctx.get ("rewards-supply") + ctx.get ("rewards-held")) + [2])))
    return "airlock-adoption-rate", update_state (s, "airlock-adoption-rate", airlock_adoption_rate)


def update_intr_divest_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    interlock_hype_updates_intr_divest_rate (ctx, s)
    token_profit_updates_intr_divest_rate (ctx, s)
    intr_divest_rate = mul_ls (ctx.get ("profit-delta-pct") + max_ls ([1] + get_new_value (s, "intr-divest-rate")))
    return "intr-divest-rate", update_state (s, "intr-divest-rate", intr_divest_rate)


def update_crypto_divest_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    crypto_hype_updates_crypto_divest_rate (ctx, s)
    crypto_divest_rate = mul_ls (ctx.get ("crypto-hype-growth") + max_ls ([1] + get_new_value (s, "crypto-divest-rate")))
    return "crypto-divest-rate", update_state (s, "crypto-divest-rate", crypto_divest_rate)


def update_intr_invest_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    token_price_updates_intr_invest_rate (ctx, s)
    airlock_lookup_rate_updates_intr_invest_rate (ctx, s)
    airlock_lookup_price_updates_intr_invest_rate (ctx, s)
    interlock_hype_updates_intr_invest_rate (ctx, s)
    intr_invest_rate = min_ls (mul_ls ([0.001] + get_new_value (s, "crypto-investments")) + sum_ls (mul_ls (ctx.get ("price-delta-pct") + get_new_value (s, "intr-invest-rate") + ctx.get ("crypto-hype-growth")) + mul_ls (ctx.get ("lookups") + ctx.get ("lookup-price"))))
    return "intr-invest-rate", update_state (s, "intr-invest-rate", intr_invest_rate)


def update_crypto_invest_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    crypto_hype_updates_crypto_invest_rate (ctx, s)
    crypto_invest_rate = mul_ls (ctx.get ("crypto-hype-growth") + max_ls ([1] + get_new_value (s, "crypto-invest-rate")))
    return "crypto-invest-rate", update_state (s, "crypto-invest-rate", crypto_invest_rate)


def update_money_mint_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    money_growth_rate_updates_money_mint_rate (ctx, s)
    money_mint_rate = diff_ls (mul_ls (get_new_value (s, "money-supply") + ctx.get ("growth")) + get_new_value (s, "money-supply")) if gt_ls (ctx.get ("growth") + [1]) [0] else [0]
    return "money-mint-rate", update_state (s, "money-mint-rate", money_mint_rate)


def update_money_reclaim_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    money_growth_rate_updates_money_reclaim_rate (ctx, s)
    money_reclaim_rate = diff_ls (get_new_value (s, "money-supply") + mul_ls (get_new_value (s, "money-supply") + ctx.get ("growth"))) if lt_ls (ctx.get ("growth") + [1]) [0] else [0]
    return "money-reclaim-rate", update_state (s, "money-reclaim-rate", money_reclaim_rate)


def update_token_reward_to_held_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    token_price_updates_token_reward_to_held_rate (ctx, s)
    airlock_data_shared_updates_token_reward_to_held_rate (ctx, s)
    stake_yield_updates_token_reward_to_held_rate (ctx, s)
    data_value_updates_token_reward_to_held_rate (ctx, s)
    token_reward_to_held_rate = sum_ls (div_ls (get_new_value (s, "token-rewards-pool") + [2]) + ctx.get ("stake-yield"))
    return "token-reward-to-held-rate", update_state (s, "token-reward-to-held-rate", token_reward_to_held_rate)


def update_token_reward_to_supply_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    token_price_updates_token_reward_to_supply_rate (ctx, s)
    airlock_data_shared_updates_token_reward_to_supply_rate (ctx, s)
    data_value_updates_token_reward_to_supply_rate (ctx, s)
    token_reward_to_supply_rate = div_ls (get_new_value (s, "token-rewards-pool") + [2])
    return "token-reward-to-supply-rate", update_state (s, "token-reward-to-supply-rate", token_reward_to_supply_rate)


def update_token_unstake_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    resolved_entities_updates_token_unstake_rate (ctx, s)
    token_unstake_rate = ctx.get ("resolutions")
    return "token-unstake-rate", update_state (s, "token-unstake-rate", token_unstake_rate)


def update_token_stake_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    max_total_stake_per_entity_updates_token_stake_rate (ctx, s)
    staking_opportunities_updates_token_stake_rate (ctx, s)
    staking_enthusiasm_updates_token_stake_rate (ctx, s)
    token_stake_rate = mul_ls (ctx.get ("enthusiasm") + ctx.get ("staking-ops") + ctx.get ("max-per-entity"))
    return "token-stake-rate", update_state (s, "token-stake-rate", token_stake_rate)


def update_token_unhold_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    intr_investments_updates_token_unhold_rate (ctx, s)
    token_unhold_rate = sum_ls (div_ls (ctx.get ("uninvested") + get_new_value (s, "token-price")))
    return "token-unhold-rate", update_state (s, "token-unhold-rate", token_unhold_rate)


def update_token_hold_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    airlock_revenue_updates_token_hold_rate (ctx, s)
    intr_investments_updates_token_hold_rate (ctx, s)
    token_hold_rate = sum_ls (div_ls (ctx.get ("invested") + get_new_value (s, "token-price")) + ctx.get ("revenue-buys"))
    return "token-hold-rate", update_state (s, "token-hold-rate", token_hold_rate)


def update_token_mint_reward_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    token_mint_reward_rate = mul_ls ([0.489] + div_ls ([27000000] + [4]))
    return "token-mint-reward-rate", update_state (s, "token-mint-reward-rate", token_mint_reward_rate)


def update_token_mint_supply_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    token_mint_supply_rate = mul_ls ([0.511] + div_ls ([27000000] + [4]))
    return "token-mint-supply-rate", update_state (s, "token-mint-supply-rate", token_mint_supply_rate)


cfg = config_sim ({ "N": 10, "T": range (100) })
init_state = {}
init_state ["flow-adjustments"] = {}
init_state ["heuristic-innovation"] = initialize_state ([random.randrange (0, 100)])
init_state ["scammer-innovation"] = initialize_state ([random.randrange (0, 100)])
init_state ["scam-profits-per-page"] = initialize_state ([random.randrange (1, 100)])
init_state ["stake-yield"] = initialize_state (choose_distro ([(1, 0.01), (1, 0.02)]))
init_state ["max-total-stake-per-entity"] = initialize_state ([random.randrange (100, 500)])
init_state ["staking-opportunities"] = initialize_state (1)
init_state ["heuristic-contradictions"] = initialize_state ([random.randrange (1, 10)])
init_state ["data-value"] = initialize_state (div_ls ([100] + [1000]))
init_state ["staking-enthusiasm"] = initialize_state (div_ls ([random.randrange (0, 25)] + [100]))
init_state ["money-growth-rate"] = initialize_state (1.0)
init_state ["crypto-hype"] = initialize_state (25)
init_state ["interlock-hype"] = initialize_state (1)
init_state ["token-profit"] = initialize_state ([random.randrange (0, 100)])
init_state ["airlock-lookup-price"] = initialize_state ([random.randrange (1, 50)])
init_state ["token-price"] = initialize_state (1.2)
init_state ["expectation"] = initialize_state ([random.randrange (-2, 2)])
init_state ["scam-upkeep"] = initialize_state (0)
init_state ["scam-profits"] = initialize_state (0)
init_state ["potential-scam-profits"] = initialize_state (20000000000)
init_state ["scam-page-successes"] = initialize_state (0)
init_state ["scam-page-visits"] = initialize_state (0)
init_state ["resolved-entities"] = initialize_state (0)
init_state ["grey-area-entities"] = initialize_state (0)
init_state ["airlock-users"] = initialize_state (100)
init_state ["browser-users"] = initialize_state (3000000000)
init_state ["data-buyer-money"] = initialize_state (300000000000)
init_state ["airlock-revenue"] = initialize_state (0)
init_state ["airlock-data-shared"] = initialize_state (0)
init_state ["browsing-data"] = initialize_state (3000000000)
init_state ["potential-airlock-lookups"] = initialize_state (3000000000000)
init_state ["airlock-lookups"] = initialize_state (0)
init_state ["page-visits"] = initialize_state (3000000000000)
init_state ["intr-investments"] = initialize_state (0)
init_state ["crypto-investments"] = initialize_state (18000000000)
init_state ["money-reclaimed"] = initialize_state (0)
init_state ["money-supply"] = initialize_state (10000000000)
init_state ["money-mint"] = initialize_state (10000000000)
init_state ["token-supply-held"] = initialize_state (0)
init_state ["token-supply-staked"] = initialize_state (0)
init_state ["token-rewards-pool"] = initialize_state (0)
init_state ["token-supply"] = initialize_state (0)
init_state ["token-mint"] = initialize_state (1000000000)
init_state ["scam-upkeep-rate"] = initialize_state (0)
init_state ["scam-profit-rate"] = initialize_state (0)
init_state ["scam-page-success-rate"] = initialize_state (0)
init_state ["scam-page-visit-rate"] = initialize_state (0)
init_state ["airlock-revenue-rate"] = initialize_state (0)
init_state ["airlock-share-rate"] = initialize_state (0)
init_state ["resolution-rate"] = initialize_state (0)
init_state ["grey-area-entity-rate"] = initialize_state (0)
init_state ["airlock-lookup-rate"] = initialize_state (0)
init_state ["airlock-abandonment-rate"] = initialize_state (0)
init_state ["airlock-adoption-rate"] = initialize_state (0)
init_state ["intr-divest-rate"] = initialize_state (0)
init_state ["crypto-divest-rate"] = initialize_state (0)
init_state ["intr-invest-rate"] = initialize_state (0)
init_state ["crypto-invest-rate"] = initialize_state (0)
init_state ["money-mint-rate"] = initialize_state (0)
init_state ["money-reclaim-rate"] = initialize_state (0)
init_state ["token-reward-to-held-rate"] = initialize_state (0)
init_state ["token-reward-to-supply-rate"] = initialize_state (0)
init_state ["token-unstake-rate"] = initialize_state (0)
init_state ["token-stake-rate"] = initialize_state (0)
init_state ["token-unhold-rate"] = initialize_state (0)
init_state ["token-hold-rate"] = initialize_state (0)
init_state ["token-mint-reward-rate"] = initialize_state (0)
init_state ["token-mint-supply-rate"] = initialize_state (0)
indicators_and_flows = {}
indicators_and_flows ["heuristic-innovation"] = update_heuristic_innovation
indicators_and_flows ["scammer-innovation"] = update_scammer_innovation
indicators_and_flows ["scam-profits-per-page"] = update_scam_profits_per_page
indicators_and_flows ["stake-yield"] = update_stake_yield
indicators_and_flows ["max-total-stake-per-entity"] = update_max_total_stake_per_entity
indicators_and_flows ["staking-opportunities"] = update_staking_opportunities
indicators_and_flows ["heuristic-contradictions"] = update_heuristic_contradictions
indicators_and_flows ["data-value"] = update_data_value
indicators_and_flows ["staking-enthusiasm"] = update_staking_enthusiasm
indicators_and_flows ["money-growth-rate"] = update_money_growth_rate
indicators_and_flows ["crypto-hype"] = update_crypto_hype
indicators_and_flows ["interlock-hype"] = update_interlock_hype
indicators_and_flows ["token-profit"] = update_token_profit
indicators_and_flows ["airlock-lookup-price"] = update_airlock_lookup_price
indicators_and_flows ["token-price"] = update_token_price
indicators_and_flows ["expectation"] = update_expectation
indicators_and_flows ["scam-upkeep-rate"] = update_scam_upkeep_rate
indicators_and_flows ["scam-profit-rate"] = update_scam_profit_rate
indicators_and_flows ["scam-page-success-rate"] = update_scam_page_success_rate
indicators_and_flows ["scam-page-visit-rate"] = update_scam_page_visit_rate
indicators_and_flows ["airlock-revenue-rate"] = update_airlock_revenue_rate
indicators_and_flows ["airlock-share-rate"] = update_airlock_share_rate
indicators_and_flows ["resolution-rate"] = update_resolution_rate
indicators_and_flows ["grey-area-entity-rate"] = update_grey_area_entity_rate
indicators_and_flows ["airlock-lookup-rate"] = update_airlock_lookup_rate
indicators_and_flows ["airlock-abandonment-rate"] = update_airlock_abandonment_rate
indicators_and_flows ["airlock-adoption-rate"] = update_airlock_adoption_rate
indicators_and_flows ["intr-divest-rate"] = update_intr_divest_rate
indicators_and_flows ["crypto-divest-rate"] = update_crypto_divest_rate
indicators_and_flows ["intr-invest-rate"] = update_intr_invest_rate
indicators_and_flows ["crypto-invest-rate"] = update_crypto_invest_rate
indicators_and_flows ["money-mint-rate"] = update_money_mint_rate
indicators_and_flows ["money-reclaim-rate"] = update_money_reclaim_rate
indicators_and_flows ["token-reward-to-held-rate"] = update_token_reward_to_held_rate
indicators_and_flows ["token-reward-to-supply-rate"] = update_token_reward_to_supply_rate
indicators_and_flows ["token-unstake-rate"] = update_token_unstake_rate
indicators_and_flows ["token-stake-rate"] = update_token_stake_rate
indicators_and_flows ["token-unhold-rate"] = update_token_unhold_rate
indicators_and_flows ["token-hold-rate"] = update_token_hold_rate
indicators_and_flows ["token-mint-reward-rate"] = update_token_mint_reward_rate
indicators_and_flows ["token-mint-supply-rate"] = update_token_mint_supply_rate
stock_driven_flow_adjust = {}
stock_driven_flow_adjust ["flow-adjustments"] = adjust_all_flows
flow_commit = {}
flow_commit ["scam-upkeep-rate"] = commit_scam_upkeep_rate
flow_commit ["scam-profit-rate"] = commit_scam_profit_rate
flow_commit ["scam-page-success-rate"] = commit_scam_page_success_rate
flow_commit ["scam-page-visit-rate"] = commit_scam_page_visit_rate
flow_commit ["airlock-revenue-rate"] = commit_airlock_revenue_rate
flow_commit ["airlock-share-rate"] = commit_airlock_share_rate
flow_commit ["resolution-rate"] = commit_resolution_rate
flow_commit ["grey-area-entity-rate"] = commit_grey_area_entity_rate
flow_commit ["airlock-lookup-rate"] = commit_airlock_lookup_rate
flow_commit ["airlock-abandonment-rate"] = commit_airlock_abandonment_rate
flow_commit ["airlock-adoption-rate"] = commit_airlock_adoption_rate
flow_commit ["intr-divest-rate"] = commit_intr_divest_rate
flow_commit ["crypto-divest-rate"] = commit_crypto_divest_rate
flow_commit ["intr-invest-rate"] = commit_intr_invest_rate
flow_commit ["crypto-invest-rate"] = commit_crypto_invest_rate
flow_commit ["money-mint-rate"] = commit_money_mint_rate
flow_commit ["money-reclaim-rate"] = commit_money_reclaim_rate
flow_commit ["token-reward-to-held-rate"] = commit_token_reward_to_held_rate
flow_commit ["token-reward-to-supply-rate"] = commit_token_reward_to_supply_rate
flow_commit ["token-unstake-rate"] = commit_token_unstake_rate
flow_commit ["token-stake-rate"] = commit_token_stake_rate
flow_commit ["token-unhold-rate"] = commit_token_unhold_rate
flow_commit ["token-hold-rate"] = commit_token_hold_rate
flow_commit ["token-mint-reward-rate"] = commit_token_mint_reward_rate
flow_commit ["token-mint-supply-rate"] = commit_token_mint_supply_rate
stock_reduction = {}
stock_reduction ["scam-profits"] = reduce_scam_profits
stock_reduction ["potential-scam-profits"] = reduce_potential_scam_profits
stock_reduction ["scam-page-visits"] = reduce_scam_page_visits
stock_reduction ["page-visits"] = reduce_page_visits
stock_reduction ["data-buyer-money"] = reduce_data_buyer_money
stock_reduction ["browsing-data"] = reduce_browsing_data
stock_reduction ["grey-area-entities"] = reduce_grey_area_entities
stock_reduction ["airlock-lookups"] = reduce_airlock_lookups
stock_reduction ["potential-airlock-lookups"] = reduce_potential_airlock_lookups
stock_reduction ["airlock-users"] = reduce_airlock_users
stock_reduction ["browser-users"] = reduce_browser_users
stock_reduction ["intr-investments"] = reduce_intr_investments
stock_reduction ["crypto-investments"] = reduce_crypto_investments
stock_reduction ["money-mint"] = reduce_money_mint
stock_reduction ["money-supply"] = reduce_money_supply
stock_reduction ["token-rewards-pool"] = reduce_token_rewards_pool
stock_reduction ["token-supply-staked"] = reduce_token_supply_staked
stock_reduction ["token-supply-held"] = reduce_token_supply_held
stock_reduction ["token-supply"] = reduce_token_supply
stock_reduction ["token-mint"] = reduce_token_mint
stock_aggregation = {}
stock_aggregation ["scam-upkeep"] = aggregate_scam_upkeep
stock_aggregation ["scam-profits"] = aggregate_scam_profits
stock_aggregation ["scam-page-successes"] = aggregate_scam_page_successes
stock_aggregation ["scam-page-visits"] = aggregate_scam_page_visits
stock_aggregation ["airlock-revenue"] = aggregate_airlock_revenue
stock_aggregation ["airlock-data-shared"] = aggregate_airlock_data_shared
stock_aggregation ["resolved-entities"] = aggregate_resolved_entities
stock_aggregation ["grey-area-entities"] = aggregate_grey_area_entities
stock_aggregation ["airlock-lookups"] = aggregate_airlock_lookups
stock_aggregation ["browser-users"] = aggregate_browser_users
stock_aggregation ["airlock-users"] = aggregate_airlock_users
stock_aggregation ["intr-investments"] = aggregate_intr_investments
stock_aggregation ["crypto-investments"] = aggregate_crypto_investments
stock_aggregation ["money-supply"] = aggregate_money_supply
stock_aggregation ["money-reclaimed"] = aggregate_money_reclaimed
stock_aggregation ["token-supply-staked"] = aggregate_token_supply_staked
stock_aggregation ["token-supply-held"] = aggregate_token_supply_held
stock_aggregation ["token-rewards-pool"] = aggregate_token_rewards_pool
stock_aggregation ["token-supply"] = aggregate_token_supply
psubs = [{ "policies": {}, "variables": indicators_and_flows }, { "policies": {}, "variables": stock_driven_flow_adjust }, { "policies": {}, "variables": flow_commit }, { "policies": {}, "variables": stock_reduction }, { "policies": {}, "variables": stock_aggregation }]
exp = Experiment ()
exp.append_model (initial_state=init_state, model_id='interlock-1', sim_configs=cfg, partial_state_update_blocks=psubs)
exec_mode = ExecutionMode ()
local_mode_ctx = ExecutionContext (context=exec_mode.local_mode)
simulation = Executor (exec_context=local_mode_ctx, configs=exp.configs)
exec_res = simulation.execute ()
sim_events = exec_res [0]
sim_res = pd.DataFrame (sim_events)
sim_res = sim_res.applymap (tuple_to_value)

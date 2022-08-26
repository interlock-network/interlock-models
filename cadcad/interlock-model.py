import numpy as np
import copy as copy
import pandas as pd
import constraint as lim
import plotly
import plotly.express as px
import random
import math
from cadCAD.configuration.utils import bound_norm_random, config_sim, time_step, env_trigger
from cadCAD.configuration import Experiment
from cadCAD.engine import ExecutionMode, ExecutionContext
from cadCAD.engine import Executor
def s_expectation_updates_staking_enthusiasm (ctx, s):
    if ctx.get ("expectation-multiplier") == None:
        ctx ["expectation-multiplier"] = []
    
    expectation_multiplier = ctx.get ("expectation-multiplier")
    new_val = [4] if lt_eq_ls (get_new_value (s, "expectation") + [0]) [0] else [1]
    append_each (expectation_multiplier, new_val)

def s_expectation_updates_token_price (ctx, s):
    if ctx.get ("expectation-multiplier") == None:
        ctx ["expectation-multiplier"] = []
    
    expectation_multiplier = ctx.get ("expectation-multiplier")
    new_val = [1] if eq_ls (get_new_value (s, "expectation") + [const_stag]) [0] else diff_ls ([1] + div_ls ([sim_random (1, 10)] + [100])) if eq_ls (get_new_value (s, "expectation") + [const_bigup]) [0] else diff_ls ([1] + div_ls ([sim_random (11, 20)] + [100])) if eq_ls (get_new_value (s, "expectation") + [const_bigdip]) [0] else sum_ls ([1] + div_ls ([sim_random (1, 10)] + [100])) if eq_ls (get_new_value (s, "expectation") + [const_up]) [0] else sum_ls ([1] + div_ls ([sim_random (11, 20)] + [100])) if eq_ls (get_new_value (s, "expectation") + [const_bigup]) [0] else [-100]
    append_each (expectation_multiplier, new_val)

def s_crypto_hype_updates_interlock_hype (ctx, s):
    if ctx.get ("crypto-hype-growth") == None:
        ctx ["crypto-hype-growth"] = []
    
    crypto_hype_growth = ctx.get ("crypto-hype-growth")
    new_val = div_ls (get_new_value (s, "crypto-hype") + get_old_value (s, "crypto-hype"))
    append_each (crypto_hype_growth, new_val)

def s_crypto_hype_updates_crypto_invest_rate (ctx, s):
    if ctx.get ("crypto-hype-growth") == None:
        ctx ["crypto-hype-growth"] = []
    
    crypto_hype_growth = ctx.get ("crypto-hype-growth")
    new_val = div_ls (get_new_value (s, "crypto-hype") + get_old_value (s, "crypto-hype"))
    append_each (crypto_hype_growth, new_val)

def s_crypto_hype_updates_crypto_divest_rate (ctx, s):
    if ctx.get ("crypto-hype-growth") == None:
        ctx ["crypto-hype-growth"] = []
    
    crypto_hype_growth = ctx.get ("crypto-hype-growth")
    new_val = div_ls (get_old_value (s, "crypto-hype") + get_new_value (s, "crypto-hype"))
    append_each (crypto_hype_growth, new_val)

def s_interlock_hype_updates_intr_invest_rate (ctx, s):
    if ctx.get ("crypto-hype-growth") == None:
        ctx ["crypto-hype-growth"] = []
    
    crypto_hype_growth = ctx.get ("crypto-hype-growth")
    new_val = div_ls (get_new_value (s, "interlock-hype") + get_old_value (s, "interlock-hype"))
    append_each (crypto_hype_growth, new_val)

def s_interlock_hype_updates_intr_divest_rate (ctx, s):
    if ctx.get ("crypto-hype-growth") == None:
        ctx ["crypto-hype-growth"] = []
    
    crypto_hype_growth = ctx.get ("crypto-hype-growth")
    new_val = div_ls (get_old_value (s, "interlock-hype") + get_new_value (s, "interlock-hype"))
    append_each (crypto_hype_growth, new_val)

def s_interlock_hype_updates_airlock_adoption_rate (ctx, s):
    if ctx.get ("crypto-hype-growth") == None:
        ctx ["crypto-hype-growth"] = []
    
    crypto_hype_growth = ctx.get ("crypto-hype-growth")
    new_val = div_ls (get_new_value (s, "interlock-hype") + get_old_value (s, "interlock-hype"))
    append_each (crypto_hype_growth, new_val)

def s_money_growth_rate_updates_money_mint_rate (ctx, s):
    if ctx.get ("growth") == None:
        ctx ["growth"] = []
    
    growth = ctx.get ("growth")
    new_val = get_new_value (s, "money-growth-rate")
    append_each (growth, new_val)

def s_money_growth_rate_updates_money_reclaim_rate (ctx, s):
    if ctx.get ("growth") == None:
        ctx ["growth"] = []
    
    growth = ctx.get ("growth")
    new_val = get_new_value (s, "money-growth-rate")
    append_each (growth, new_val)

def s_adjust_token_mint_outflow (s, flow_adjustments):
    flow_list = ["token-mint-reward-rate", "token-mint-hold-rate", "token-mint-supply-rate"]
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


def s_reduce_token_mint (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "token-mint-reward-rate") + get_new_value (s, "token-mint-hold-rate") + get_new_value (s, "token-mint-supply-rate"))
    return "token-mint", update_state (s, "token-mint", diff_ls (get_new_value (s, "token-mint") + red))

def s_adjust_token_sell_pool_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "token-hold-rate") [0]
    inventory = get_new_value (s, "token-sell-pool") [0]
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["token-hold-rate"] = flow_val

def s_aggregate_token_sell_pool (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "token-reward-to-sell-rate") + get_new_value (s, "token-unhold-rate") + get_new_value (s, "token-mint-supply-rate"))
    return "token-sell-pool", update_state (s, "token-sell-pool", sum_ls (get_new_value (s, "token-sell-pool") + agg))

def s_reduce_token_sell_pool (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "token-hold-rate"))
    return "token-sell-pool", update_state (s, "token-sell-pool", diff_ls (get_new_value (s, "token-sell-pool") + red))

def s_adjust_token_rewards_pool_outflow (s, flow_adjustments):
    flow_list = ["token-reward-to-held-rate", "token-reward-to-sell-rate"]
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


def s_aggregate_token_rewards_pool (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "token-mint-reward-rate"))
    return "token-rewards-pool", update_state (s, "token-rewards-pool", sum_ls (get_new_value (s, "token-rewards-pool") + agg))

def s_reduce_token_rewards_pool (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "token-reward-to-held-rate") + get_new_value (s, "token-reward-to-sell-rate"))
    return "token-rewards-pool", update_state (s, "token-rewards-pool", diff_ls (get_new_value (s, "token-rewards-pool") + red))

def s_adjust_token_stake_pool_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "token-unstake-rate") [0]
    inventory = get_new_value (s, "token-stake-pool") [0]
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["token-unstake-rate"] = flow_val

def s_aggregate_token_stake_pool (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "token-stake-rate"))
    return "token-stake-pool", update_state (s, "token-stake-pool", sum_ls (get_new_value (s, "token-stake-pool") + agg))

def s_reduce_token_stake_pool (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "token-unstake-rate"))
    return "token-stake-pool", update_state (s, "token-stake-pool", diff_ls (get_new_value (s, "token-stake-pool") + red))

def s_adjust_token_hold_pool_outflow (s, flow_adjustments):
    flow_list = ["token-stake-rate", "token-unhold-rate"]
    random.shuffle (flow_list)
    inventory = get_new_value (s, "token-hold-pool") [0]
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


def s_aggregate_token_hold_pool (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "token-reward-to-held-rate") + get_new_value (s, "token-unstake-rate") + get_new_value (s, "token-hold-rate") + get_new_value (s, "token-mint-hold-rate"))
    return "token-hold-pool", update_state (s, "token-hold-pool", sum_ls (get_new_value (s, "token-hold-pool") + agg))

def s_reduce_token_hold_pool (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "token-stake-rate") + get_new_value (s, "token-unhold-rate"))
    return "token-hold-pool", update_state (s, "token-hold-pool", diff_ls (get_new_value (s, "token-hold-pool") + red))

def s_commit_token_mint_supply_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "token-mint-supply-rate", update_state (s, "token-mint-supply-rate", [adjusted_flows ["token-mint-supply-rate"]])

def s_commit_token_mint_hold_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "token-mint-hold-rate", update_state (s, "token-mint-hold-rate", [adjusted_flows ["token-mint-hold-rate"]])

def s_commit_token_mint_reward_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "token-mint-reward-rate", update_state (s, "token-mint-reward-rate", [adjusted_flows ["token-mint-reward-rate"]])

def s_commit_token_hold_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "token-hold-rate", update_state (s, "token-hold-rate", [adjusted_flows ["token-hold-rate"]])

def s_commit_token_unhold_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "token-unhold-rate", update_state (s, "token-unhold-rate", [adjusted_flows ["token-unhold-rate"]])

def s_commit_token_stake_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "token-stake-rate", update_state (s, "token-stake-rate", [adjusted_flows ["token-stake-rate"]])

def s_staking_enthusiasm_updates_token_stake_rate (ctx, s):
    if ctx.get ("enthusiasm") == None:
        ctx ["enthusiasm"] = []
    
    enthusiasm = ctx.get ("enthusiasm")
    new_val = get_new_value (s, "staking-enthusiasm")
    append_each (enthusiasm, new_val)

def s_commit_token_unstake_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "token-unstake-rate", update_state (s, "token-unstake-rate", [adjusted_flows ["token-unstake-rate"]])

def s_data_value_updates_airlock_revenue_rate (ctx, s):
    if ctx.get ("data-value") == None:
        ctx ["data-value"] = []
    
    data_value = ctx.get ("data-value")
    new_val = get_new_value (s, "data-value")
    append_each (data_value, new_val)

def s_data_value_updates_token_reward_to_sell_rate (ctx, s):
    if ctx.get ("data-value") == None:
        ctx ["data-value"] = []
    
    data_value = ctx.get ("data-value")
    new_val = get_new_value (s, "data-value")
    append_each (data_value, new_val)

def s_data_value_updates_token_reward_to_held_rate (ctx, s):
    if ctx.get ("data-value") == None:
        ctx ["data-value"] = []
    
    data_value = ctx.get ("data-value")
    new_val = get_new_value (s, "data-value")
    append_each (data_value, new_val)

def s_token_reward_to_sell_rate_updates_airlock_adoption_rate (ctx, s):
    if ctx.get ("rewards-sold") == None:
        ctx ["rewards-sold"] = []
    
    rewards_sold = ctx.get ("rewards-sold")
    new_val = div_ls_safe (get_new_value (s, "token-reward-to-sell-rate") + get_new_value (s, "airlock-users"))
    append_each (rewards_sold, new_val)

def s_token_reward_to_held_rate_updates_airlock_adoption_rate (ctx, s):
    if ctx.get ("rewards-held") == None:
        ctx ["rewards-held"] = []
    
    rewards_held = ctx.get ("rewards-held")
    new_val = div_ls_safe (get_new_value (s, "token-reward-to-held-rate") + get_new_value (s, "airlock-users"))
    append_each (rewards_held, new_val)

def s_token_reward_to_sell_rate_updates_airlock_abandonment_rate (ctx, s):
    if ctx.get ("rewards-sold") == None:
        ctx ["rewards-sold"] = []
    
    rewards_sold = ctx.get ("rewards-sold")
    new_val = div_ls_safe (get_old_value (s, "token-reward-to-sell-rate") + get_new_value (s, "token-reward-to-sell-rate"))
    append_each (rewards_sold, new_val)

def s_token_reward_to_held_rate_updates_airlock_abandonment_rate (ctx, s):
    if ctx.get ("rewards-held") == None:
        ctx ["rewards-held"] = []
    
    rewards_held = ctx.get ("rewards-held")
    new_val = div_ls_safe (get_old_value (s, "token-reward-to-held-rate") + get_new_value (s, "token-reward-to-held-rate"))
    append_each (rewards_held, new_val)

def s_commit_token_reward_to_sell_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "token-reward-to-sell-rate", update_state (s, "token-reward-to-sell-rate", [adjusted_flows ["token-reward-to-sell-rate"]])

def s_commit_token_reward_to_held_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "token-reward-to-held-rate", update_state (s, "token-reward-to-held-rate", [adjusted_flows ["token-reward-to-held-rate"]])

def s_adjust_money_mint_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "money-mint-rate") [0]
    inventory = get_new_value (s, "money-mint") [0]
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["money-mint-rate"] = flow_val

def s_reduce_money_mint (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "money-mint-rate"))
    return "money-mint", update_state (s, "money-mint", diff_ls (get_new_value (s, "money-mint") + red))

def s_adjust_money_supply_outflow (s, flow_adjustments):
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


def s_aggregate_money_supply (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "crypto-divest-rate") + get_new_value (s, "money-mint-rate"))
    return "money-supply", update_state (s, "money-supply", sum_ls (get_new_value (s, "money-supply") + agg))

def s_reduce_money_supply (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "crypto-invest-rate") + get_new_value (s, "money-reclaim-rate"))
    return "money-supply", update_state (s, "money-supply", diff_ls (get_new_value (s, "money-supply") + red))

def s_aggregate_money_reclaimed (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "money-reclaim-rate"))
    return "money-reclaimed", update_state (s, "money-reclaimed", sum_ls (get_new_value (s, "money-reclaimed") + agg))

def s_adjust_crypto_investments_outflow (s, flow_adjustments):
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


def s_aggregate_crypto_investments (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "intr-divest-rate") + get_new_value (s, "crypto-invest-rate"))
    return "crypto-investments", update_state (s, "crypto-investments", sum_ls (get_new_value (s, "crypto-investments") + agg))

def s_reduce_crypto_investments (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "crypto-divest-rate") + get_new_value (s, "intr-invest-rate"))
    return "crypto-investments", update_state (s, "crypto-investments", diff_ls (get_new_value (s, "crypto-investments") + red))

def s_adjust_intr_investments_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "intr-divest-rate") [0]
    inventory = get_new_value (s, "intr-investments") [0]
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["intr-divest-rate"] = flow_val

def s_aggregate_intr_investments (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "intr-invest-rate"))
    return "intr-investments", update_state (s, "intr-investments", sum_ls (get_new_value (s, "intr-investments") + agg))

def s_reduce_intr_investments (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "intr-divest-rate"))
    return "intr-investments", update_state (s, "intr-investments", diff_ls (get_new_value (s, "intr-investments") + red))

def s_commit_money_reclaim_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "money-reclaim-rate", update_state (s, "money-reclaim-rate", [adjusted_flows ["money-reclaim-rate"]])

def s_commit_money_mint_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "money-mint-rate", update_state (s, "money-mint-rate", [adjusted_flows ["money-mint-rate"]])

def s_commit_crypto_invest_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "crypto-invest-rate", update_state (s, "crypto-invest-rate", [adjusted_flows ["crypto-invest-rate"]])

def s_commit_intr_invest_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "intr-invest-rate", update_state (s, "intr-invest-rate", [adjusted_flows ["intr-invest-rate"]])

def s_commit_crypto_divest_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "crypto-divest-rate", update_state (s, "crypto-divest-rate", [adjusted_flows ["crypto-divest-rate"]])

def s_commit_intr_divest_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "intr-divest-rate", update_state (s, "intr-divest-rate", [adjusted_flows ["intr-divest-rate"]])

def s_intr_investments_updates_token_hold_rate (ctx, s):
    if ctx.get ("invested") == None:
        ctx ["invested"] = []
    
    invested = ctx.get ("invested")
    new_val = max_ls (diff_ls (get_new_value (s, "intr-investments") + get_old_value (s, "intr-investments")) + [0])
    append_each (invested, new_val)

def s_intr_investments_updates_token_unhold_rate (ctx, s):
    if ctx.get ("uninvested") == None:
        ctx ["uninvested"] = []
    
    uninvested = ctx.get ("uninvested")
    new_val = max_ls (diff_ls (get_old_value (s, "intr-investments") + get_new_value (s, "intr-investments")) + [0])
    append_each (uninvested, new_val)

def s_money_supply_updates_crypto_hype (ctx, s):
    if ctx.get ("extra-cash-growth") == None:
        ctx ["extra-cash-growth"] = []
    
    extra_cash_growth = ctx.get ("extra-cash-growth")
    new_val = div_ls (get_new_value (s, "money-supply") + get_old_value (s, "money-supply"))
    append_each (extra_cash_growth, new_val)

def s_token_hold_pool_updates_avg_token_value (ctx, s):
    if ctx.get ("held") == None:
        ctx ["held"] = []
    
    held = ctx.get ("held")
    new_val = get_new_value (s, "token-hold-pool")
    append_each (held, new_val)

def s_intr_investments_updates_avg_token_value (ctx, s):
    if ctx.get ("invested") == None:
        ctx ["invested"] = []
    
    invested = ctx.get ("invested")
    new_val = get_new_value (s, "intr-investments")
    append_each (invested, new_val)

def s_token_sell_pool_updates_token_price (ctx, s):
    if ctx.get ("sell-pool-growth") == None:
        ctx ["sell-pool-growth"] = []
    
    sell_pool_growth = ctx.get ("sell-pool-growth")
    new_val = [0] if any_in_range (div_ls_safe (get_new_value (s, "token-sell-pool") + get_old_value (s, "token-sell-pool")) + [0.96] + [1.04]) [0] else [1] if gt_ls (div_ls_safe (get_new_value (s, "token-sell-pool") + get_old_value (s, "token-sell-pool")) + [1]) [0] else [-1]
    append_each (sell_pool_growth, new_val)

def s_intr_investments_updates_token_price (ctx, s):
    if ctx.get ("investment-pool-growth") == None:
        ctx ["investment-pool-growth"] = []
    
    investment_pool_growth = ctx.get ("investment-pool-growth")
    new_val = [0] if any_in_range (div_ls_safe (get_new_value (s, "intr-investments") + get_old_value (s, "intr-investments")) + [0.96] + [1.04]) [0] else [1] if gt_ls (div_ls_safe (get_new_value (s, "intr-investments") + get_old_value (s, "intr-investments")) + [1]) [0] else [-1]
    append_each (investment_pool_growth, new_val)

def s_token_price_updates_token_profit (ctx, s):
    if ctx.get ("price-delta-pct") == None:
        ctx ["price-delta-pct"] = []
    
    price_delta_pct = ctx.get ("price-delta-pct")
    new_val = div_ls_safe (get_new_value (s, "token-price") + get_old_value (s, "token-price"))
    append_each (price_delta_pct, new_val)

def s_token_price_updates_airlock_lookup_price (ctx, s):
    if ctx.get ("price-delta-pct") == None:
        ctx ["price-delta-pct"] = []
    
    price_delta_pct = ctx.get ("price-delta-pct")
    new_val = div_ls_safe (get_new_value (s, "token-price") + get_old_value (s, "token-price"))
    append_each (price_delta_pct, new_val)

def s_airlock_lookup_price_updates_intr_invest_rate (ctx, s):
    if ctx.get ("lookup-price") == None:
        ctx ["lookup-price"] = []
    
    lookup_price = ctx.get ("lookup-price")
    new_val = get_new_value (s, "airlock-lookup-price")
    append_each (lookup_price, new_val)

def s_token_price_updates_intr_invest_rate (ctx, s):
    if ctx.get ("price-delta-pct") == None:
        ctx ["price-delta-pct"] = []
    
    price_delta_pct = ctx.get ("price-delta-pct")
    new_val = div_ls_safe (get_old_value (s, "token-price") + get_new_value (s, "token-price"))
    append_each (price_delta_pct, new_val)

def s_token_price_updates_token_reward_to_sell_rate (ctx, s):
    if ctx.get ("price-delta-pct") == None:
        ctx ["price-delta-pct"] = []
    
    price_delta_pct = ctx.get ("price-delta-pct")
    new_val = div_ls_safe (get_new_value (s, "token-price") + get_old_value (s, "token-price"))
    append_each (price_delta_pct, new_val)

def s_token_price_updates_token_reward_to_held_rate (ctx, s):
    if ctx.get ("price-delta-pct") == None:
        ctx ["price-delta-pct"] = []
    
    price_delta_pct = ctx.get ("price-delta-pct")
    new_val = div_ls_safe (get_new_value (s, "token-price") + get_old_value (s, "token-price"))
    append_each (price_delta_pct, new_val)

def s_token_price_updates_airlock_adoption_rate (ctx, s):
    if ctx.get ("price") == None:
        ctx ["price"] = []
    
    price = ctx.get ("price")
    new_val = get_new_value (s, "token-price")
    append_each (price, new_val)

def s_token_price_updates_airlock_abandonment_rate (ctx, s):
    if ctx.get ("price") == None:
        ctx ["price"] = []
    
    price = ctx.get ("price")
    new_val = get_new_value (s, "token-price")
    append_each (price, new_val)

def s_token_profit_updates_intr_divest_rate (ctx, s):
    if ctx.get ("profit-delta-pct") == None:
        ctx ["profit-delta-pct"] = []
    
    profit_delta_pct = ctx.get ("profit-delta-pct")
    new_val = div_ls_safe (get_new_value (s, "token-profit") + get_old_value (s, "token-profit"))
    append_each (profit_delta_pct, new_val)

def s_stake_yield_updates_token_reward_to_held_rate (ctx, s):
    if ctx.get ("stake-yield") == None:
        ctx ["stake-yield"] = []
    
    stake_yield = ctx.get ("stake-yield")
    new_val = mul_ls (get_new_value (s, "token-unstake-rate") + get_new_value (s, "stake-yield"))
    append_each (stake_yield, new_val)

def s_adjust_potential_page_visits_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "page-visit-rate") [0]
    inventory = get_new_value (s, "potential-page-visits") [0]
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["page-visit-rate"] = flow_val

def s_reduce_potential_page_visits (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "page-visit-rate"))
    return "potential-page-visits", update_state (s, "potential-page-visits", diff_ls (get_new_value (s, "potential-page-visits") + red))

def s_adjust_page_visits_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "scam-page-visit-rate") [0]
    inventory = get_new_value (s, "page-visits") [0]
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["scam-page-visit-rate"] = flow_val

def s_aggregate_page_visits (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "page-visit-rate"))
    return "page-visits", update_state (s, "page-visits", sum_ls (get_new_value (s, "page-visits") + agg))

def s_reduce_page_visits (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "scam-page-visit-rate"))
    return "page-visits", update_state (s, "page-visits", diff_ls (get_new_value (s, "page-visits") + red))

def s_adjust_airlock_lookups_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "grey-area-entity-rate") [0]
    inventory = get_new_value (s, "airlock-lookups") [0]
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["grey-area-entity-rate"] = flow_val

def s_aggregate_airlock_lookups (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "airlock-lookup-rate"))
    return "airlock-lookups", update_state (s, "airlock-lookups", sum_ls (get_new_value (s, "airlock-lookups") + agg))

def s_reduce_airlock_lookups (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "grey-area-entity-rate"))
    return "airlock-lookups", update_state (s, "airlock-lookups", diff_ls (get_new_value (s, "airlock-lookups") + red))

def s_adjust_potential_airlock_lookups_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "airlock-lookup-rate") [0]
    inventory = get_new_value (s, "potential-airlock-lookups") [0]
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["airlock-lookup-rate"] = flow_val

def s_reduce_potential_airlock_lookups (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "airlock-lookup-rate"))
    return "potential-airlock-lookups", update_state (s, "potential-airlock-lookups", diff_ls (get_new_value (s, "potential-airlock-lookups") + red))

def s_adjust_browsing_data_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "airlock-share-rate") [0]
    inventory = get_new_value (s, "browsing-data") [0]
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["airlock-share-rate"] = flow_val

def s_reduce_browsing_data (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "airlock-share-rate"))
    return "browsing-data", update_state (s, "browsing-data", diff_ls (get_new_value (s, "browsing-data") + red))

def s_aggregate_airlock_data_shared (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "airlock-share-rate"))
    return "airlock-data-shared", update_state (s, "airlock-data-shared", sum_ls (get_new_value (s, "airlock-data-shared") + agg))

def s_aggregate_airlock_revenue (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "airlock-revenue-rate"))
    return "airlock-revenue", update_state (s, "airlock-revenue", sum_ls (get_new_value (s, "airlock-revenue") + agg))

def s_adjust_data_buyer_money_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "airlock-revenue-rate") [0]
    inventory = get_new_value (s, "data-buyer-money") [0]
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["airlock-revenue-rate"] = flow_val

def s_reduce_data_buyer_money (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "airlock-revenue-rate"))
    return "data-buyer-money", update_state (s, "data-buyer-money", diff_ls (get_new_value (s, "data-buyer-money") + red))

def s_adjust_browser_users_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "airlock-adoption-rate") [0]
    inventory = get_new_value (s, "browser-users") [0]
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["airlock-adoption-rate"] = flow_val

def s_aggregate_browser_users (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "airlock-abandonment-rate"))
    return "browser-users", update_state (s, "browser-users", sum_ls (get_new_value (s, "browser-users") + agg))

def s_reduce_browser_users (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "airlock-adoption-rate"))
    return "browser-users", update_state (s, "browser-users", diff_ls (get_new_value (s, "browser-users") + red))

def s_adjust_airlock_users_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "airlock-abandonment-rate") [0]
    inventory = get_new_value (s, "airlock-users") [0]
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["airlock-abandonment-rate"] = flow_val

def s_aggregate_airlock_users (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "airlock-adoption-rate"))
    return "airlock-users", update_state (s, "airlock-users", sum_ls (get_new_value (s, "airlock-users") + agg))

def s_reduce_airlock_users (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "airlock-abandonment-rate"))
    return "airlock-users", update_state (s, "airlock-users", diff_ls (get_new_value (s, "airlock-users") + red))

def s_adjust_grey_area_entities_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "resolution-rate") [0]
    inventory = get_new_value (s, "grey-area-entities") [0]
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["resolution-rate"] = flow_val

def s_aggregate_grey_area_entities (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "grey-area-entity-rate"))
    return "grey-area-entities", update_state (s, "grey-area-entities", sum_ls (get_new_value (s, "grey-area-entities") + agg))

def s_reduce_grey_area_entities (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "resolution-rate"))
    return "grey-area-entities", update_state (s, "grey-area-entities", diff_ls (get_new_value (s, "grey-area-entities") + red))

def s_aggregate_resolved_entities (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "resolution-rate"))
    return "resolved-entities", update_state (s, "resolved-entities", sum_ls (get_new_value (s, "resolved-entities") + agg))

def s_adjust_scam_page_visits_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "scam-page-success-rate") [0]
    inventory = get_new_value (s, "scam-page-visits") [0]
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["scam-page-success-rate"] = flow_val

def s_aggregate_scam_page_visits (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "scam-page-visit-rate"))
    return "scam-page-visits", update_state (s, "scam-page-visits", sum_ls (get_new_value (s, "scam-page-visits") + agg))

def s_reduce_scam_page_visits (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "scam-page-success-rate"))
    return "scam-page-visits", update_state (s, "scam-page-visits", diff_ls (get_new_value (s, "scam-page-visits") + red))

def s_aggregate_scam_page_successes (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "scam-page-success-rate"))
    return "scam-page-successes", update_state (s, "scam-page-successes", sum_ls (get_new_value (s, "scam-page-successes") + agg))

def s_adjust_potential_scam_profits_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "scam-profit-rate") [0]
    inventory = get_new_value (s, "potential-scam-profits") [0]
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["scam-profit-rate"] = flow_val

def s_reduce_potential_scam_profits (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "scam-profit-rate"))
    return "potential-scam-profits", update_state (s, "potential-scam-profits", diff_ls (get_new_value (s, "potential-scam-profits") + red))

def s_adjust_scam_profits_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "scam-upkeep-rate") [0]
    inventory = get_new_value (s, "scam-profits") [0]
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["scam-upkeep-rate"] = flow_val

def s_aggregate_scam_profits (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "scam-profit-rate"))
    return "scam-profits", update_state (s, "scam-profits", sum_ls (get_new_value (s, "scam-profits") + agg))

def s_reduce_scam_profits (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "scam-upkeep-rate"))
    return "scam-profits", update_state (s, "scam-profits", diff_ls (get_new_value (s, "scam-profits") + red))

def s_aggregate_scam_upkeep (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "scam-upkeep-rate"))
    return "scam-upkeep", update_state (s, "scam-upkeep", sum_ls (get_new_value (s, "scam-upkeep") + agg))

def s_commit_airlock_adoption_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "airlock-adoption-rate", update_state (s, "airlock-adoption-rate", [adjusted_flows ["airlock-adoption-rate"]])

def s_commit_airlock_abandonment_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "airlock-abandonment-rate", update_state (s, "airlock-abandonment-rate", [adjusted_flows ["airlock-abandonment-rate"]])

def s_commit_airlock_lookup_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "airlock-lookup-rate", update_state (s, "airlock-lookup-rate", [adjusted_flows ["airlock-lookup-rate"]])

def s_commit_grey_area_entity_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "grey-area-entity-rate", update_state (s, "grey-area-entity-rate", [adjusted_flows ["grey-area-entity-rate"]])

def s_commit_resolution_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "resolution-rate", update_state (s, "resolution-rate", [adjusted_flows ["resolution-rate"]])

def s_resolved_entities_updates_token_unstake_rate (ctx, s):
    if ctx.get ("resolutions") == None:
        ctx ["resolutions"] = []
    
    resolutions = ctx.get ("resolutions")
    new_val = diff_ls (get_new_value (s, "resolved-entities") + get_old_value (s, "resolved-entities"))
    append_each (resolutions, new_val)

def s_commit_airlock_share_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "airlock-share-rate", update_state (s, "airlock-share-rate", [adjusted_flows ["airlock-share-rate"]])

def s_commit_airlock_revenue_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "airlock-revenue-rate", update_state (s, "airlock-revenue-rate", [adjusted_flows ["airlock-revenue-rate"]])

def s_commit_page_visit_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "page-visit-rate", update_state (s, "page-visit-rate", [adjusted_flows ["page-visit-rate"]])

def s_commit_scam_page_visit_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "scam-page-visit-rate", update_state (s, "scam-page-visit-rate", [adjusted_flows ["scam-page-visit-rate"]])

def s_commit_scam_page_success_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "scam-page-success-rate", update_state (s, "scam-page-success-rate", [adjusted_flows ["scam-page-success-rate"]])

def s_scam_page_successes_updates_scam_profit_rate (ctx, s):
    if ctx.get ("total-pages") == None:
        ctx ["total-pages"] = []
    
    total_pages = ctx.get ("total-pages")
    new_val = diff_ls (get_new_value (s, "scam-page-successes") + get_old_value (s, "scam-page-successes"))
    append_each (total_pages, new_val)

def s_scam_profits_per_page_updates_scam_profit_rate (ctx, s):
    if ctx.get ("cash-per-page") == None:
        ctx ["cash-per-page"] = []
    
    cash_per_page = ctx.get ("cash-per-page")
    new_val = get_new_value (s, "scam-profits-per-page")
    append_each (cash_per_page, new_val)

def s_commit_scam_profit_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "scam-profit-rate", update_state (s, "scam-profit-rate", [adjusted_flows ["scam-profit-rate"]])

def s_commit_scam_upkeep_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "scam-upkeep-rate", update_state (s, "scam-upkeep-rate", [adjusted_flows ["scam-upkeep-rate"]])

def s_airlock_users_updates_scam_page_success_rate (ctx, s):
    if ctx.get ("user-share") == None:
        ctx ["user-share"] = []
    
    user_share = ctx.get ("user-share")
    new_val = div_ls (get_new_value (s, "airlock-users") + get_new_value (s, "browser-users"))
    append_each (user_share, new_val)

def s_page_visit_rate_updates_airlock_lookup_rate (ctx, s):
    if ctx.get ("pages-visited") == None:
        ctx ["pages-visited"] = []
    
    pages_visited = ctx.get ("pages-visited")
    new_val = get_new_value (s, "page-visit-rate")
    append_each (pages_visited, new_val)

def s_airlock_users_updates_airlock_lookup_rate (ctx, s):
    if ctx.get ("user-share") == None:
        ctx ["user-share"] = []
    
    user_share = ctx.get ("user-share")
    new_val = div_ls (get_new_value (s, "airlock-users") + get_new_value (s, "browser-users"))
    append_each (user_share, new_val)

def s_airlock_data_shared_updates_token_reward_to_supply_rate (ctx, s):
    if ctx.get ("shared") == None:
        ctx ["shared"] = []
    
    shared = ctx.get ("shared")
    new_val = diff_ls (get_new_value (s, "airlock-data-shared") + get_old_value (s, "airlock-data-shared"))
    append_each (shared, new_val)

def s_airlock_data_shared_updates_token_reward_to_held_rate (ctx, s):
    if ctx.get ("shared") == None:
        ctx ["shared"] = []
    
    shared = ctx.get ("shared")
    new_val = diff_ls (get_new_value (s, "airlock-data-shared") + get_old_value (s, "airlock-data-shared"))
    append_each (shared, new_val)

def s_airlock_lookup_rate_updates_intr_invest_rate (ctx, s):
    if ctx.get ("lookups") == None:
        ctx ["lookups"] = []
    
    lookups = ctx.get ("lookups")
    new_val = get_new_value (s, "airlock-lookup-rate")
    append_each (lookups, new_val)

def s_airlock_users_updates_airlock_share_rate (ctx, s):
    if ctx.get ("user-share") == None:
        ctx ["user-share"] = []
    
    user_share = ctx.get ("user-share")
    new_val = div_ls (get_new_value (s, "airlock-users") + get_new_value (s, "browser-users"))
    append_each (user_share, new_val)

def s_airlock_revenue_updates_token_hold_rate (ctx, s):
    if ctx.get ("revenue-buys") == None:
        ctx ["revenue-buys"] = []
    
    revenue_buys = ctx.get ("revenue-buys")
    new_val = div_ls (diff_ls (get_new_value (s, "airlock-revenue") + get_old_value (s, "airlock-revenue")) + get_new_value (s, "token-price"))
    append_each (revenue_buys, new_val)

def s_scam_page_success_rate_updates_scammer_innovation (ctx, s):
    if ctx.get ("urgency") == None:
        ctx ["urgency"] = []
    
    urgency = ctx.get ("urgency")
    new_val = div_ls (get_old_value (s, "scam-page-success-rate") + max_ls ([1] + get_new_value (s, "scam-page-success-rate")))
    append_each (urgency, new_val)

def s_scammer_innovation_updates_scam_upkeep_rate (ctx, s):
    if ctx.get ("profit-diverted-to-innovate") == None:
        ctx ["profit-diverted-to-innovate"] = []
    
    profit_diverted_to_innovate = ctx.get ("profit-diverted-to-innovate")
    new_val = mul_ls (get_new_value (s, "scammer-innovation"))
    append_each (profit_diverted_to_innovate, new_val)

def s_scammer_innovation_updates_heuristic_contradictions (ctx, s):
    if ctx.get ("innovation") == None:
        ctx ["innovation"] = []
    
    innovation = ctx.get ("innovation")
    new_val = sum_ls (get_new_value (s, "heuristic-contradictions") + mul_ls (div_ls ([sim_random (1, 50)] + [100]) + get_new_value (s, "heuristic-contradictions") + get_new_value (s, "scammer-innovation")))
    append_each (innovation, new_val)

def s_heuristic_contradictions_updates_scam_page_success_rate (ctx, s):
    if ctx.get ("pass-through") == None:
        ctx ["pass-through"] = []
    
    pass_through = ctx.get ("pass-through")
    new_val = diff_ls ([1] + div_ls (get_new_value (s, "heuristic-contradictions") + [100]))
    append_each (pass_through, new_val)

def s_heuristic_contradictions_updates_airlock_abandonment_rate (ctx, s):
    if ctx.get ("contradiction-delta") == None:
        ctx ["contradiction-delta"] = []
    
    contradiction_delta = ctx.get ("contradiction-delta")
    new_val = div_ls_safe (get_new_value (s, "heuristic-contradictions") + get_old_value (s, "heuristic-contradictions"))
    append_each (contradiction_delta, new_val)

def s_heuristic_contradictions_updates_grey_area_entity_rate (ctx, s):
    if ctx.get ("contradictions") == None:
        ctx ["contradictions"] = []
    
    contradictions = ctx.get ("contradictions")
    new_val = div_ls (get_new_value (s, "heuristic-contradictions") + [100])
    append_each (contradictions, new_val)

def s_grey_area_entities_updates_staking_opportunities (ctx, s):
    if ctx.get ("grey-stake") == None:
        ctx ["grey-stake"] = []
    
    grey_stake = ctx.get ("grey-stake")
    new_val = mul_ls ([0.5] + get_new_value (s, "grey-area-entities"))
    append_each (grey_stake, new_val)

def s_staking_opportunities_updates_token_stake_rate (ctx, s):
    if ctx.get ("staking-ops") == None:
        ctx ["staking-ops"] = []
    
    staking_ops = ctx.get ("staking-ops")
    new_val = get_new_value (s, "staking-opportunities")
    append_each (staking_ops, new_val)

def s_max_total_stake_per_entity_updates_token_stake_rate (ctx, s):
    if ctx.get ("max-per-entity") == None:
        ctx ["max-per-entity"] = []
    
    max_per_entity = ctx.get ("max-per-entity")
    new_val = get_new_value (s, "max-total-stake-per-entity")
    append_each (max_per_entity, new_val)

def s_heuristic_contradictions_updates_heuristic_innovation (ctx, s):
    if ctx.get ("urgency") == None:
        ctx ["urgency"] = []
    
    urgency = ctx.get ("urgency")
    new_val = get_new_value (s, "heuristic-contradictions")
    append_each (urgency, new_val)

def s_heuristic_innovation_updates_heuristic_contradictions (ctx, s):
    if ctx.get ("innovation") == None:
        ctx ["innovation"] = []
    
    innovation = ctx.get ("innovation")
    new_val = diff_ls (get_new_value (s, "heuristic-contradictions") + mul_ls (div_ls ([sim_random (1, 50)] + [100]) + get_new_value (s, "heuristic-contradictions") + get_new_value (s, "heuristic-innovation")))
    append_each (innovation, new_val)

morph = lim.Problem ()
sim_rng = np.random.RandomState (12421)
def tuple_list_to_agg (ls):
    ret = {}
    if len (ls) == 0:
        return ret
    


class Aggregation:
    agg_stats = {}
    def __init__ (self, schema, agg, base=0, min_mag=0, max_mag=0, step=0):
        self.schema = schema
        self.agg = agg
        self.root = {}
        self.base = base
        self.min_mag = min_mag
        self.max_mag = max_mag
        self.step = step


    def agg_dict_walk (self, hasht, func, depth, tup):
        for k in hasht:
            val = hasht [k]
            if isinstance (val, dict):
                self.agg_dict_walk (val, func, depth, (tup + (k,)))
            else:
                func ((tup + (k, val)))
            





def what_if_contradicts_max_total_stake_policy (what_if, max_total_stake_policy):
    return all_true ([not (what_if == const_base_what_if and max_total_stake_policy == const_halving), not (what_if == const_base_what_if and max_total_stake_policy == const_doubling)])


def what_if_contradicts_token_reward_policy (what_if, token_reward_policy):
    return all_true ([not (what_if == const_base_what_if and token_reward_policy == const_trickle), not (what_if == const_base_what_if and token_reward_policy == const_halted)])


def what_if_contradicts_token_reward_price_normalization (what_if, token_reward_price_normalization):
    return all_true ([not (what_if == const_base_what_if and token_reward_price_normalization == const_yes)])


def what_if_contradicts_heuristic_innovation_scenario (what_if, heuristic_innovation_scenario):
    return all_true ([not (what_if == const_base_what_if and heuristic_innovation_scenario == const_industrialized), not (what_if == const_base_what_if and heuristic_innovation_scenario == const_leading), not (what_if == const_base_what_if and heuristic_innovation_scenario == const_lagging), not (what_if == const_base_what_if and heuristic_innovation_scenario == const_terminal)])


def what_if_contradicts_airlock_lookup_policy (what_if, airlock_lookup_policy):
    return all_true ([not (what_if == const_base_what_if and airlock_lookup_policy == const_above_cost), not (what_if == const_base_what_if and airlock_lookup_policy == const_below_cost)])


def what_if_contradicts_stake_yield_policy (what_if, stake_yield_policy):
    return all_true ([not (what_if == const_base_what_if and stake_yield_policy == const_at_market), not (what_if == const_base_what_if and stake_yield_policy == const_above_market)])


def choose_agg_ls (agg, keep):
    summage = 0
    i = 0
    last = 0
    for tup in agg:
        last = (len (tup) - 1)
        summage = (summage + tup [last])

    choice = sim_random (0, (summage - 1))
    for tup in agg:
        last = (len (tup) - 1)
        i = (i + tup [last])
        if i >= choice:
            ret = []
            for k in keep:
                ret.append (tup [k])

            return ret
        



def agg_to_tuple_list (agg):
    ret = []
    max_depth = len (agg.schema)
    def add_tuple (tuple):
        ret.append (tuple)


    agg.agg_dict_walk (agg.root, add_tuple, max_depth, ())
    return ret


def agg_choose (agg_or_ls, keep):
    if isinstance (agg_or_ls, list):
        agg = agg_or_ls [0]
    elif isinstance (agg_or_ls, Aggregation):
        agg = agg_or_ls
    
    return choose_agg_ls (agg_to_tuple_list (agg), keep)


def agg_load (agg, path):
    ret = agg.root
    for k_or_ls in path:
        if isinstance (k_or_ls, list):
            k = k_or_ls [0]
        else:
            k = k_or_ls
        
        ret = ret.get (k)

    return ret


def agg_store (agg, path, val):
    hasht_prev = None
    k_prev = None
    hasht = agg.root
    pl = len (path)
    if isinstance (val, list):
        val = val [0]
    
    pi = 1
    for ki in path:
        if isinstance (ki, list):
            k = ki [0]
        else:
            k = ki
        
        k_prev = k
        hasht_prev = hasht
        hasht = hasht.get (k)
        if (hasht == None and not pi == pl):
            hasht = {}
            hasht_prev [k] = hasht
        elif pi == pl:
            hasht_prev [k] = val
        
        pi = (pi + 1)



def agg_cols (cols, agg_or_ls):
    if isinstance (agg_or_ls, list):
        agg = agg_or_ls [0]
    else:
        agg = agg_or_ls
    
    tuple_list = agg_to_tuple_list (agg)
    ret = Aggregation (agg.schema, agg.agg, agg.base, agg.min_mag, agg.max_mag, agg.step)
    depth = 0
    path_len = (len (cols) - 1)
    for e in tuple_list:
        new = ()
        for c_or_ls in cols:
            if isinstance (c_or_ls, list):
                c = c_or_ls [0]
            else:
                c = c_or_ls
            
            new = (new + (e [c],))

        found = agg_load (ret, new [:path_len])
        if found == None:
            agg_store (ret, new [:path_len], new [path_len])
        else:
            agg_store (ret, new [:path_len], (found + new [path_len]))
        

    return ret


def agg_rows (matches, agg_or_ls):
    if isinstance (agg_or_ls, list):
        agg = agg_or_ls [0]
    else:
        agg = agg_or_ls
    
    ret = Aggregation (agg.schema, agg.agg, agg.base, agg.min_mag, agg.max_mag, agg.step)
    for k in matches:
        found = agg_load (agg, k)
        if not found == None:
            agg_store (ret, k, found)
        

    return ret


def agg_store_records (agg, records):
    for rec in records:
        ln = len (rec)
        pn = (ln - 1)
        path = rec [:pn]
        agg_store (agg, path, rec [pn])

    return agg


def aggregate (agg_orig, keys):
    agg = copy.deepcopy (agg_orig)
    if agg.agg == "count":
        found = agg_load (agg, keys)
        if found == None:
            agg_store (agg, keys, 1)
        else:
            agg_store (agg, keys, (found + 1))
        
    elif agg.agg == "sum":
        kl = len (keys)
        pl = (kl - 1)
        path = keys [:pl]
        to_agg = keys [pl]
        found = agg_load (agg, path)
        if found == None:
            agg_store (agg, path, sum_ls (to_agg) [0])
        else:
            agg_store (agg, path, (found + sum_ls (to_agg) [0]))
        
    


def all_true (ls):
    test = True
    for b in ls:
        if b == False:
            return False
        

    return True


def any_in_range (ls):
    if len (ls) < 3:
        return [0]
    
    ultimate = (len (ls) - 1)
    penultimate = (len (ls) - 2)
    r1 = ls [ultimate]
    r2 = ls [penultimate]
    vals = ls [:penultimate]
    for val in vals:
        if (val >= min (r1, r2) and val <= max (r1, r2)):
            return [1]
        

    return [0]


def any_true (ls):
    test = False
    for b in ls:
        if b == True:
            return True
        

    return False


def generate_params ():
    morph.addVariable ("stake-yield-policy", [const_at_market, const_above_market, const_below_market])
    morph.addVariable ("airlock-lookup-policy", [const_at_cost, const_above_cost, const_below_cost])
    morph.addVariable ("heuristic-innovation-scenario", [const_industrialized, const_leading, const_holding, const_lagging, const_terminal])
    morph.addVariable ("what-if", [const_base_what_if])
    morph.addVariable ("token-valuation", [const_half_value])
    morph.addVariable ("token-reward-price-normalization", [const_no])
    morph.addVariable ("token-reward-policy", [const_firehose, const_trickle, const_halted])
    morph.addVariable ("supply-perception", [const_supply_expansion, const_supply_filling])
    morph.addVariable ("max-total-stake-policy", [const_egalitarian, const_halving, const_doubling])
    morph.addVariable ("expectation-chain", [const_observed_expectation_chain_id])
    morph.addVariable ("money-growth", [const_observed_money_growth_id])
    morph.addConstraint (what_if_contradicts_max_total_stake_policy, ("what-if", "max-total-stake-policy"))
    morph.addConstraint (what_if_contradicts_token_reward_policy, ("what-if", "token-reward-policy"))
    morph.addConstraint (what_if_contradicts_token_reward_price_normalization, ("what-if", "token-reward-price-normalization"))
    morph.addConstraint (what_if_contradicts_heuristic_innovation_scenario, ("what-if", "heuristic-innovation-scenario"))
    morph.addConstraint (what_if_contradicts_airlock_lookup_policy, ("what-if", "airlock-lookup-policy"))
    morph.addConstraint (what_if_contradicts_stake_yield_policy, ("what-if", "stake-yield-policy"))
    sol = morph.getSolutions ()
    ret = {}
    for ht in sol:
        for param in ht:
            val = ht [param]
            ret_ls = ret.get (param)
            if ret_ls == None:
                ret [param] = []
                ret_ls = ret.get (param)
            
            ret_ls.append (val)


    return ret


def floor_ls (ls):
    if len (ls) == 0:
        return []
    
    ret_ls = []
    for n in ls:
        ret_ls.append (math.floor (n))

    return ret_ls


def ceil_ls (ls):
    if len (ls) == 0:
        return []
    
    ret_ls = []
    for n in ls:
        ret_ls.append (math.ceil (n))

    return ret_ls


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
            if n == 0:
                return [0]
            
        elif first == 0:
            ret_val = (ret_val / n)
        

    return [ret_val]


def div_ls_safe (ls):
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
            if n == 0:
                return [0]
            
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


def sim_random (a, b):
    return math.floor (bound_norm_random (sim_rng, a, b))


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
    elif isinstance (val, Aggregation):
        return val, val
    


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
    fig = px.line (data, x=x_vars, y=y_vars, facet_col='run', facet_col_wrap=3, height=8000, facet_row_spacing=0.006, template='seaborn')
    fig.update_layout (margin=dict(l=20, r=20, t=20, b=20),)
    return fig


def plot_log_lines (data, x_vars, y_vars):
    fig = px.line (data, x=x_vars, y=y_vars, log_y=True, facet_col='run', facet_col_wrap=3, height=8000, facet_row_spacing=0.006, template='seaborn')
    fig.update_layout (margin=dict(l=20, r=20, t=20, b=20),)
    return fig


def adjust_all_flows (_params, substep, sH, s, _input, **kwargs):
    flow_adjustments = {}
    s_adjust_scam_profits_outflow (s, flow_adjustments)
    s_adjust_potential_scam_profits_outflow (s, flow_adjustments)
    s_adjust_scam_page_visits_outflow (s, flow_adjustments)
    s_adjust_page_visits_outflow (s, flow_adjustments)
    s_adjust_potential_page_visits_outflow (s, flow_adjustments)
    s_adjust_data_buyer_money_outflow (s, flow_adjustments)
    s_adjust_browsing_data_outflow (s, flow_adjustments)
    s_adjust_grey_area_entities_outflow (s, flow_adjustments)
    s_adjust_airlock_lookups_outflow (s, flow_adjustments)
    s_adjust_potential_airlock_lookups_outflow (s, flow_adjustments)
    s_adjust_airlock_users_outflow (s, flow_adjustments)
    s_adjust_browser_users_outflow (s, flow_adjustments)
    s_adjust_intr_investments_outflow (s, flow_adjustments)
    s_adjust_crypto_investments_outflow (s, flow_adjustments)
    s_adjust_money_mint_outflow (s, flow_adjustments)
    s_adjust_money_supply_outflow (s, flow_adjustments)
    s_adjust_token_rewards_pool_outflow (s, flow_adjustments)
    s_adjust_token_stake_pool_outflow (s, flow_adjustments)
    s_adjust_token_hold_pool_outflow (s, flow_adjustments)
    s_adjust_token_sell_pool_outflow (s, flow_adjustments)
    s_adjust_token_mint_outflow (s, flow_adjustments)
    return "flow-adjustments", flow_adjustments


const_base_what_if = 0
const_industrialized = 2
const_leading = 1
const_holding = 0
const_lagging = -1
const_terminal = -2
const_no = 0
const_yes = 1
const_half_value = 0.5
const_firehose = 2
const_trickle = 1
const_halted = 0
const_supply_expansion = 1
const_supply_filling = 0
const_halving = -1
const_egalitarian = 0
const_doubling = 1
const_bigdip = -2
const_dip = -1
const_stag = 0
const_up = 1
const_bigup = 2
const_at_market = 0
const_below_market = -1
const_above_market = 1
const_at_cost = 0
const_below_cost = -1
const_above_cost = 1
const_price_movement = agg_store_records (Aggregation (["sell", "buy", "mul", "count"], "count"), [[1, -1, 0.8, 1], [0, -1, 0.9, 1], [1, 0, 0.9, 1], [1, 1, 1.0, 1], [-1, -1, 1.0, 1], [0, 0, 1.0, 1], [0, 1, 1.1, 1], [-1, 0, 1.1, 1], [-1, 1, 1.2, 1]])
const_observed_money_growth = agg_store_records (Aggregation (["mult"], "count"), [[0.988, 1], [0.991, 2], [0.992, 2], [0.993, 5], [0.994, 7], [0.995, 10], [0.997, 38], [0.998, 80], [0.999, 124], [1.0, 145], [1.001, 127], [1.002, 105], [1.003, 68], [1.004, 35], [1.005, 27], [1.006, 29], [1.007, 12], [1.008, 4], [1.009, 2], [1.01, 3], [1.017, 1]])
const_observed_expectation_chain_id = 0
const_observed_money_growth_id = 0
const_observed_expectation_chain = agg_store_records (Aggregation (["in", "out"], "count"), [[[const_bigdip], [const_bigup], 1], [[const_bigdip], [const_dip], 1], [[const_bigdip], [const_up], 6], [[const_dip], [const_bigup], 1], [[const_dip], [const_bigdip], 6], [[const_dip], [const_dip], 7], [[const_dip], [const_up], 10], [[const_stag], [const_bigup], 1], [[const_stag], [const_stag], 1], [[const_stag], [const_dip], 3], [[const_up], [const_bigdip], 2], [[const_up], [const_stag], 3], [[const_up], [const_bigup], 5], [[const_up], [const_dip], 9], [[const_up], [const_up], 11], [[const_bigup], [const_stag], 1], [[const_bigup], [const_up], 4], [[const_bigup], [const_dip], 4], [[const_bigup], [const_bigup], 5]])
const_buy = 0
const_sell = 1
def s_update_heuristic_innovation (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_heuristic_contradictions_updates_heuristic_innovation (ctx, s)
    heuristic_innovation = ctx.get ("urgency")
    return "heuristic-innovation", update_state (s, "heuristic-innovation", heuristic_innovation)


def s_update_scammer_innovation (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_scam_page_success_rate_updates_scammer_innovation (ctx, s)
    scammer_innovation = ctx.get ("urgency")
    return "scammer-innovation", update_state (s, "scammer-innovation", scammer_innovation)


def s_update_scam_profits_per_page (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    scam_profits_per_page = min_ls ([100] + max_ls ([1] + [sim_random (1, 100)]))
    return "scam-profits-per-page", update_state (s, "scam-profits-per-page", scam_profits_per_page)


def s_update_stake_yield (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    stake_yield = min_ls ([0.02] + max_ls ([0.01] + agg_choose (agg_store_records (Aggregation (["yield"], "count"), [[0.01, 1], [0.02, 1]]), [0])))
    return "stake-yield", update_state (s, "stake-yield", stake_yield)


def s_update_max_total_stake_per_entity (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    max_total_stake_per_entity = min_ls ([500] + max_ls ([100] + [sim_random (100, 500)]))
    return "max-total-stake-per-entity", update_state (s, "max-total-stake-per-entity", max_total_stake_per_entity)


def s_update_staking_opportunities (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_grey_area_entities_updates_staking_opportunities (ctx, s)
    staking_opportunities = min_ls ([3000000000000] + max_ls ([0] + ctx.get ("grey-stake")))
    return "staking-opportunities", update_state (s, "staking-opportunities", staking_opportunities)


def s_update_heuristic_contradictions (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_heuristic_innovation_updates_heuristic_contradictions (ctx, s)
    s_scammer_innovation_updates_heuristic_contradictions (ctx, s)
    heuristic_contradictions = min_ls ([100] + max_ls ([0] + max_ls ([sim_random (5, 15)] + sum_ls (ctx.get ("innovation")))))
    return "heuristic-contradictions", update_state (s, "heuristic-contradictions", heuristic_contradictions)


def s_update_data_value (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    data_value = min_ls (div_ls ([600] + [1000]) + max_ls (div_ls ([100] + [1000]) + div_ls ([sim_random (100, 600)] + [1000])))
    return "data-value", update_state (s, "data-value", data_value)


def s_update_staking_enthusiasm (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_expectation_updates_staking_enthusiasm (ctx, s)
    staking_enthusiasm = min_ls ([100] + max_ls ([0] + mul_ls (ctx.get ("expectation-multiplier") + div_ls ([sim_random (5, 25)] + [100]))))
    return "staking-enthusiasm", update_state (s, "staking-enthusiasm", staking_enthusiasm)


def s_update_money_growth_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    money_growth_rate = min_ls (div_ls ([1017] + [1000]) + max_ls (div_ls ([988] + [1000]) + agg_choose ([const_observed_money_growth] if eq_ls ([_params ["money-growth"]] + [const_observed_money_growth_id]) [0] else [-999], [0])))
    return "money-growth-rate", update_state (s, "money-growth-rate", money_growth_rate)


def s_update_crypto_hype (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_money_supply_updates_crypto_hype (ctx, s)
    crypto_hype = min_ls ([100] + max_ls ([1] + mul_ls (get_new_value (s, "crypto-hype") + ctx.get ("extra-cash-growth"))))
    return "crypto-hype", update_state (s, "crypto-hype", crypto_hype)


def s_update_interlock_hype (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_crypto_hype_updates_interlock_hype (ctx, s)
    interlock_hype = min_ls ([100] + max_ls ([1] + mul_ls (get_new_value (s, "interlock-hype") + ctx.get ("crypto-hype-growth"))))
    return "interlock-hype", update_state (s, "interlock-hype", interlock_hype)


def s_update_token_profit (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_token_price_updates_token_profit (ctx, s)
    token_profit = ctx.get ("price-delta-pct")
    return "token-profit", update_state (s, "token-profit", token_profit)


def s_update_airlock_lookup_price (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_token_price_updates_airlock_lookup_price (ctx, s)
    airlock_lookup_price = min_ls ([50] + max_ls ([1] + div_ls (get_new_value (s, "airlock-lookup-price") + ctx.get ("price-delta-pct"))))
    return "airlock-lookup-price", update_state (s, "airlock-lookup-price", airlock_lookup_price)


def s_update_airlock_expenses (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    airlock_expenses = min_ls ([1000000] + max_ls ([1] + get_new_value (s, "airlock-expenses")))
    return "airlock-expenses", update_state (s, "airlock-expenses", airlock_expenses)


def s_update_token_price (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_token_sell_pool_updates_token_price (ctx, s)
    s_intr_investments_updates_token_price (ctx, s)
    s_expectation_updates_token_price (ctx, s)
    token_price = min_ls ([60] + max_ls ([0.01] + mul_ls (get_new_value (s, "token-price") + agg_choose (agg_cols ([[2], [3]], agg_rows ([[ctx.get ("sell-pool-growth"), ctx.get ("investment-pool-growth")]], [const_price_movement])), [0]))))
    return "token-price", update_state (s, "token-price", token_price)


def s_update_avg_token_value (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_token_hold_pool_updates_avg_token_value (ctx, s)
    s_intr_investments_updates_avg_token_value (ctx, s)
    avg_token_value = min_ls ([500000] + max_ls ([1] + div_ls_safe (ctx.get ("invested") + ctx.get ("held"))))
    return "avg-token-value", update_state (s, "avg-token-value", avg_token_value)


def s_update_expectation (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    expectation = min_ls ([2] + max_ls ([-2] + agg_choose (agg_cols ([[1], [2]], agg_rows ([[get_new_value (s, "expectation")]], [const_observed_expectation_chain] if eq_ls ([_params ["expectation-chain"]] + [const_observed_expectation_chain_id]) [0] else [-999])), [0])))
    return "expectation", update_state (s, "expectation", expectation)


def s_update_scam_upkeep_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_scammer_innovation_updates_scam_upkeep_rate (ctx, s)
    scam_upkeep_rate = mul_ls (get_new_value (s, "scam-profits") + [1.01] + ctx.get ("profit-diverted-to-innovate"))
    return "scam-upkeep-rate", update_state (s, "scam-upkeep-rate", scam_upkeep_rate)


def s_update_scam_profit_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_scam_profits_per_page_updates_scam_profit_rate (ctx, s)
    s_scam_page_successes_updates_scam_profit_rate (ctx, s)
    scam_profit_rate = mul_ls (ctx.get ("total-pages") + ctx.get ("cash-per-page"))
    return "scam-profit-rate", update_state (s, "scam-profit-rate", scam_profit_rate)


def s_update_scam_page_success_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_airlock_users_updates_scam_page_success_rate (ctx, s)
    s_heuristic_contradictions_updates_scam_page_success_rate (ctx, s)
    scam_page_success_rate = diff_ls (mul_ls ([0.4] + get_new_value (s, "scam-page-visits")) + mul_ls ([0.4] + get_new_value (s, "scam-page-visits") + mul_ls (ctx.get ("pass-through") + ctx.get ("user-share"))))
    return "scam-page-success-rate", update_state (s, "scam-page-success-rate", scam_page_success_rate)


def s_update_scam_page_visit_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    scam_page_visit_rate = mul_ls ([1] + [1000000])
    return "scam-page-visit-rate", update_state (s, "scam-page-visit-rate", scam_page_visit_rate)


def s_update_page_visit_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    page_visit_rate = mul_ls ([100] + [1000000])
    return "page-visit-rate", update_state (s, "page-visit-rate", page_visit_rate)


def s_update_airlock_revenue_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_data_value_updates_airlock_revenue_rate (ctx, s)
    airlock_revenue_rate = mul_ls (ctx.get ("data-value") + diff_ls (get_new_value (s, "airlock-data-shared") + get_old_value (s, "airlock-data-shared")))
    return "airlock-revenue-rate", update_state (s, "airlock-revenue-rate", airlock_revenue_rate)


def s_update_airlock_share_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_airlock_users_updates_airlock_share_rate (ctx, s)
    airlock_share_rate = mul_ls (ctx.get ("user-share") + get_new_value (s, "browsing-data"))
    return "airlock-share-rate", update_state (s, "airlock-share-rate", airlock_share_rate)


def s_update_resolution_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    resolution_rate = get_old_value (s, "grey-area-entity-rate")
    return "resolution-rate", update_state (s, "resolution-rate", resolution_rate)


def s_update_grey_area_entity_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_heuristic_contradictions_updates_grey_area_entity_rate (ctx, s)
    grey_area_entity_rate = mul_ls (get_new_value (s, "airlock-lookups") + ctx.get ("contradictions"))
    return "grey-area-entity-rate", update_state (s, "grey-area-entity-rate", grey_area_entity_rate)


def s_update_airlock_lookup_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_airlock_users_updates_airlock_lookup_rate (ctx, s)
    s_page_visit_rate_updates_airlock_lookup_rate (ctx, s)
    airlock_lookup_rate = mul_ls (ctx.get ("pages-visited") + ctx.get ("user-share") + [2])
    return "airlock-lookup-rate", update_state (s, "airlock-lookup-rate", airlock_lookup_rate)


def s_update_airlock_abandonment_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_token_reward_to_held_rate_updates_airlock_abandonment_rate (ctx, s)
    s_token_reward_to_sell_rate_updates_airlock_abandonment_rate (ctx, s)
    s_heuristic_contradictions_updates_airlock_abandonment_rate (ctx, s)
    s_token_price_updates_airlock_abandonment_rate (ctx, s)
    airlock_abandonment_rate = mul_ls (ctx.get ("contradiction-delta") + max_ls ([1] + get_new_value (s, "airlock-abandonment-rate")) + mul_ls (ctx.get ("price") + div_ls (sum_ls (ctx.get ("rewards-sold") + ctx.get ("rewards-held")) + [2])))
    return "airlock-abandonment-rate", update_state (s, "airlock-abandonment-rate", airlock_abandonment_rate)


def s_update_airlock_adoption_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_token_price_updates_airlock_adoption_rate (ctx, s)
    s_token_reward_to_held_rate_updates_airlock_adoption_rate (ctx, s)
    s_token_reward_to_sell_rate_updates_airlock_adoption_rate (ctx, s)
    s_interlock_hype_updates_airlock_adoption_rate (ctx, s)
    airlock_adoption_rate = mul_ls (ctx.get ("crypto-hype-growth") + max_ls ([20] + get_new_value (s, "airlock-adoption-rate")) + mul_ls (ctx.get ("price") + div_ls (sum_ls (ctx.get ("rewards-sold") + ctx.get ("rewards-held")) + [2])))
    return "airlock-adoption-rate", update_state (s, "airlock-adoption-rate", airlock_adoption_rate)


def s_update_intr_divest_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_interlock_hype_updates_intr_divest_rate (ctx, s)
    s_token_profit_updates_intr_divest_rate (ctx, s)
    intr_divest_rate = mul_ls (ctx.get ("profit-delta-pct") + max_ls ([1] + get_new_value (s, "intr-divest-rate")))
    return "intr-divest-rate", update_state (s, "intr-divest-rate", intr_divest_rate)


def s_update_crypto_divest_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_crypto_hype_updates_crypto_divest_rate (ctx, s)
    crypto_divest_rate = mul_ls (ctx.get ("crypto-hype-growth") + max_ls ([1] + get_new_value (s, "crypto-divest-rate")))
    return "crypto-divest-rate", update_state (s, "crypto-divest-rate", crypto_divest_rate)


def s_update_intr_invest_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_token_price_updates_intr_invest_rate (ctx, s)
    s_airlock_lookup_rate_updates_intr_invest_rate (ctx, s)
    s_airlock_lookup_price_updates_intr_invest_rate (ctx, s)
    s_interlock_hype_updates_intr_invest_rate (ctx, s)
    intr_invest_rate = min_ls (mul_ls ([0.001] + get_new_value (s, "crypto-investments")) + sum_ls (mul_ls (ctx.get ("price-delta-pct") + get_new_value (s, "intr-invest-rate") + ctx.get ("crypto-hype-growth")) + mul_ls (ctx.get ("lookups") + ctx.get ("lookup-price"))))
    return "intr-invest-rate", update_state (s, "intr-invest-rate", intr_invest_rate)


def s_update_crypto_invest_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_crypto_hype_updates_crypto_invest_rate (ctx, s)
    crypto_invest_rate = mul_ls (ctx.get ("crypto-hype-growth") + max_ls ([1] + get_new_value (s, "crypto-invest-rate")))
    return "crypto-invest-rate", update_state (s, "crypto-invest-rate", crypto_invest_rate)


def s_update_money_mint_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_money_growth_rate_updates_money_mint_rate (ctx, s)
    money_mint_rate = diff_ls (mul_ls (get_new_value (s, "money-supply") + ctx.get ("growth")) + get_new_value (s, "money-supply")) if gt_ls (ctx.get ("growth") + [1]) [0] else [0]
    return "money-mint-rate", update_state (s, "money-mint-rate", money_mint_rate)


def s_update_money_reclaim_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_money_growth_rate_updates_money_reclaim_rate (ctx, s)
    money_reclaim_rate = diff_ls (get_new_value (s, "money-supply") + mul_ls (get_new_value (s, "money-supply") + ctx.get ("growth"))) if lt_ls (ctx.get ("growth") + [1]) [0] else [0]
    return "money-reclaim-rate", update_state (s, "money-reclaim-rate", money_reclaim_rate)


def s_update_token_reward_to_held_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_token_price_updates_token_reward_to_held_rate (ctx, s)
    s_airlock_data_shared_updates_token_reward_to_held_rate (ctx, s)
    s_stake_yield_updates_token_reward_to_held_rate (ctx, s)
    s_data_value_updates_token_reward_to_held_rate (ctx, s)
    token_reward_to_held_rate = sum_ls (div_ls (get_new_value (s, "token-rewards-pool") + [2]) + ctx.get ("stake-yield"))
    return "token-reward-to-held-rate", update_state (s, "token-reward-to-held-rate", token_reward_to_held_rate)


def s_update_token_reward_to_sell_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_token_price_updates_token_reward_to_sell_rate (ctx, s)
    s_data_value_updates_token_reward_to_sell_rate (ctx, s)
    token_reward_to_sell_rate = div_ls (get_new_value (s, "token-rewards-pool") + [2])
    return "token-reward-to-sell-rate", update_state (s, "token-reward-to-sell-rate", token_reward_to_sell_rate)


def s_update_token_unstake_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_resolved_entities_updates_token_unstake_rate (ctx, s)
    token_unstake_rate = ctx.get ("resolutions")
    return "token-unstake-rate", update_state (s, "token-unstake-rate", token_unstake_rate)


def s_update_token_stake_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_max_total_stake_per_entity_updates_token_stake_rate (ctx, s)
    s_staking_opportunities_updates_token_stake_rate (ctx, s)
    s_staking_enthusiasm_updates_token_stake_rate (ctx, s)
    token_stake_rate = mul_ls (ctx.get ("enthusiasm") + ctx.get ("staking-ops") + ctx.get ("max-per-entity"))
    return "token-stake-rate", update_state (s, "token-stake-rate", token_stake_rate)


def s_update_token_unhold_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_intr_investments_updates_token_unhold_rate (ctx, s)
    token_unhold_rate = sum_ls (div_ls (ctx.get ("uninvested") + get_new_value (s, "token-price")))
    return "token-unhold-rate", update_state (s, "token-unhold-rate", token_unhold_rate)


def s_update_token_hold_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_airlock_revenue_updates_token_hold_rate (ctx, s)
    s_intr_investments_updates_token_hold_rate (ctx, s)
    token_hold_rate = sum_ls (div_ls (ctx.get ("invested") + get_new_value (s, "token-price")) + ctx.get ("revenue-buys"))
    return "token-hold-rate", update_state (s, "token-hold-rate", token_hold_rate)


def s_update_token_mint_reward_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    token_mint_reward_rate = mul_ls ([0.489] + div_ls ([27000000] + [4]))
    return "token-mint-reward-rate", update_state (s, "token-mint-reward-rate", token_mint_reward_rate)


def s_update_token_mint_hold_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    token_mint_hold_rate = mul_ls ([0.511] + div_ls ([27000000] + [4])) if eq_ls ([_params ["supply-perception"]] + [const_supply_filling]) [0] else [1]
    return "token-mint-hold-rate", update_state (s, "token-mint-hold-rate", token_mint_hold_rate)


def s_update_token_mint_supply_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    token_mint_supply_rate = mul_ls ([0.511] + div_ls ([27000000] + [4])) if eq_ls ([_params ["supply-perception"]] + [const_supply_expansion]) [0] else [1]
    return "token-mint-supply-rate", update_state (s, "token-mint-supply-rate", token_mint_supply_rate)


cfg = config_sim ({ "N": 1, "T": range (100), "M": generate_params () })
init_state = {}
init_state ["flow-adjustments"] = {}
init_state ["heuristic-innovation"] = initialize_state ([sim_random (0, 100)])
init_state ["scammer-innovation"] = initialize_state ([sim_random (0, 100)])
init_state ["scam-profits-per-page"] = initialize_state ([sim_random (1, 100)])
init_state ["stake-yield"] = initialize_state (agg_choose (agg_store_records (Aggregation (["yield"], "count"), [[0.01, 1], [0.02, 1]]), [0]))
init_state ["max-total-stake-per-entity"] = initialize_state ([sim_random (100, 500)])
init_state ["staking-opportunities"] = initialize_state (1)
init_state ["heuristic-contradictions"] = initialize_state ([sim_random (1, 10)])
init_state ["data-value"] = initialize_state (div_ls ([100] + [1000]))
init_state ["staking-enthusiasm"] = initialize_state (div_ls ([sim_random (0, 25)] + [100]))
init_state ["money-growth-rate"] = initialize_state (1.0)
init_state ["crypto-hype"] = initialize_state (25)
init_state ["interlock-hype"] = initialize_state (1)
init_state ["token-profit"] = initialize_state ([sim_random (0, 100)])
init_state ["airlock-lookup-price"] = initialize_state ([sim_random (1, 50)])
init_state ["airlock-expenses"] = initialize_state (40229)
init_state ["token-price"] = initialize_state (1.2)
init_state ["avg-token-value"] = initialize_state (1)
init_state ["expectation"] = initialize_state ([sim_random (-2, 2)])
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
init_state ["page-visits"] = initialize_state (mul_ls ([100] + [1000000]))
init_state ["potential-page-visits"] = initialize_state (3000000000000)
init_state ["intr-investments"] = initialize_state (0)
init_state ["crypto-investments"] = initialize_state (18000000000)
init_state ["money-reclaimed"] = initialize_state (0)
init_state ["money-supply"] = initialize_state (10000000000)
init_state ["money-mint"] = initialize_state (10000000000)
init_state ["token-hold-pool"] = initialize_state (0)
init_state ["token-stake-pool"] = initialize_state (0)
init_state ["token-rewards-pool"] = initialize_state (0)
init_state ["token-sell-pool"] = initialize_state (0)
init_state ["token-mint"] = initialize_state (1000000000)
init_state ["scam-upkeep-rate"] = initialize_state (0)
init_state ["scam-profit-rate"] = initialize_state (0)
init_state ["scam-page-success-rate"] = initialize_state (0)
init_state ["scam-page-visit-rate"] = initialize_state (0)
init_state ["page-visit-rate"] = initialize_state (0)
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
init_state ["token-reward-to-sell-rate"] = initialize_state (0)
init_state ["token-unstake-rate"] = initialize_state (0)
init_state ["token-stake-rate"] = initialize_state (0)
init_state ["token-unhold-rate"] = initialize_state (0)
init_state ["token-hold-rate"] = initialize_state (0)
init_state ["token-mint-reward-rate"] = initialize_state (0)
init_state ["token-mint-hold-rate"] = initialize_state (0)
init_state ["token-mint-supply-rate"] = initialize_state (0)
indicators_and_flows = {}
indicators_and_flows ["heuristic-innovation"] = s_update_heuristic_innovation
indicators_and_flows ["scammer-innovation"] = s_update_scammer_innovation
indicators_and_flows ["scam-profits-per-page"] = s_update_scam_profits_per_page
indicators_and_flows ["stake-yield"] = s_update_stake_yield
indicators_and_flows ["max-total-stake-per-entity"] = s_update_max_total_stake_per_entity
indicators_and_flows ["staking-opportunities"] = s_update_staking_opportunities
indicators_and_flows ["heuristic-contradictions"] = s_update_heuristic_contradictions
indicators_and_flows ["data-value"] = s_update_data_value
indicators_and_flows ["staking-enthusiasm"] = s_update_staking_enthusiasm
indicators_and_flows ["money-growth-rate"] = s_update_money_growth_rate
indicators_and_flows ["crypto-hype"] = s_update_crypto_hype
indicators_and_flows ["interlock-hype"] = s_update_interlock_hype
indicators_and_flows ["token-profit"] = s_update_token_profit
indicators_and_flows ["airlock-lookup-price"] = s_update_airlock_lookup_price
indicators_and_flows ["airlock-expenses"] = s_update_airlock_expenses
indicators_and_flows ["token-price"] = s_update_token_price
indicators_and_flows ["avg-token-value"] = s_update_avg_token_value
indicators_and_flows ["expectation"] = s_update_expectation
indicators_and_flows ["scam-upkeep-rate"] = s_update_scam_upkeep_rate
indicators_and_flows ["scam-profit-rate"] = s_update_scam_profit_rate
indicators_and_flows ["scam-page-success-rate"] = s_update_scam_page_success_rate
indicators_and_flows ["scam-page-visit-rate"] = s_update_scam_page_visit_rate
indicators_and_flows ["page-visit-rate"] = s_update_page_visit_rate
indicators_and_flows ["airlock-revenue-rate"] = s_update_airlock_revenue_rate
indicators_and_flows ["airlock-share-rate"] = s_update_airlock_share_rate
indicators_and_flows ["resolution-rate"] = s_update_resolution_rate
indicators_and_flows ["grey-area-entity-rate"] = s_update_grey_area_entity_rate
indicators_and_flows ["airlock-lookup-rate"] = s_update_airlock_lookup_rate
indicators_and_flows ["airlock-abandonment-rate"] = s_update_airlock_abandonment_rate
indicators_and_flows ["airlock-adoption-rate"] = s_update_airlock_adoption_rate
indicators_and_flows ["intr-divest-rate"] = s_update_intr_divest_rate
indicators_and_flows ["crypto-divest-rate"] = s_update_crypto_divest_rate
indicators_and_flows ["intr-invest-rate"] = s_update_intr_invest_rate
indicators_and_flows ["crypto-invest-rate"] = s_update_crypto_invest_rate
indicators_and_flows ["money-mint-rate"] = s_update_money_mint_rate
indicators_and_flows ["money-reclaim-rate"] = s_update_money_reclaim_rate
indicators_and_flows ["token-reward-to-held-rate"] = s_update_token_reward_to_held_rate
indicators_and_flows ["token-reward-to-sell-rate"] = s_update_token_reward_to_sell_rate
indicators_and_flows ["token-unstake-rate"] = s_update_token_unstake_rate
indicators_and_flows ["token-stake-rate"] = s_update_token_stake_rate
indicators_and_flows ["token-unhold-rate"] = s_update_token_unhold_rate
indicators_and_flows ["token-hold-rate"] = s_update_token_hold_rate
indicators_and_flows ["token-mint-reward-rate"] = s_update_token_mint_reward_rate
indicators_and_flows ["token-mint-hold-rate"] = s_update_token_mint_hold_rate
indicators_and_flows ["token-mint-supply-rate"] = s_update_token_mint_supply_rate
stock_driven_flow_adjust = {}
stock_driven_flow_adjust ["flow-adjustments"] = adjust_all_flows
flow_commit = {}
flow_commit ["scam-upkeep-rate"] = s_commit_scam_upkeep_rate
flow_commit ["scam-profit-rate"] = s_commit_scam_profit_rate
flow_commit ["scam-page-success-rate"] = s_commit_scam_page_success_rate
flow_commit ["scam-page-visit-rate"] = s_commit_scam_page_visit_rate
flow_commit ["page-visit-rate"] = s_commit_page_visit_rate
flow_commit ["airlock-revenue-rate"] = s_commit_airlock_revenue_rate
flow_commit ["airlock-share-rate"] = s_commit_airlock_share_rate
flow_commit ["resolution-rate"] = s_commit_resolution_rate
flow_commit ["grey-area-entity-rate"] = s_commit_grey_area_entity_rate
flow_commit ["airlock-lookup-rate"] = s_commit_airlock_lookup_rate
flow_commit ["airlock-abandonment-rate"] = s_commit_airlock_abandonment_rate
flow_commit ["airlock-adoption-rate"] = s_commit_airlock_adoption_rate
flow_commit ["intr-divest-rate"] = s_commit_intr_divest_rate
flow_commit ["crypto-divest-rate"] = s_commit_crypto_divest_rate
flow_commit ["intr-invest-rate"] = s_commit_intr_invest_rate
flow_commit ["crypto-invest-rate"] = s_commit_crypto_invest_rate
flow_commit ["money-mint-rate"] = s_commit_money_mint_rate
flow_commit ["money-reclaim-rate"] = s_commit_money_reclaim_rate
flow_commit ["token-reward-to-held-rate"] = s_commit_token_reward_to_held_rate
flow_commit ["token-reward-to-sell-rate"] = s_commit_token_reward_to_sell_rate
flow_commit ["token-unstake-rate"] = s_commit_token_unstake_rate
flow_commit ["token-stake-rate"] = s_commit_token_stake_rate
flow_commit ["token-unhold-rate"] = s_commit_token_unhold_rate
flow_commit ["token-hold-rate"] = s_commit_token_hold_rate
flow_commit ["token-mint-reward-rate"] = s_commit_token_mint_reward_rate
flow_commit ["token-mint-hold-rate"] = s_commit_token_mint_hold_rate
flow_commit ["token-mint-supply-rate"] = s_commit_token_mint_supply_rate
stock_reduction = {}
stock_reduction ["scam-profits"] = s_reduce_scam_profits
stock_reduction ["potential-scam-profits"] = s_reduce_potential_scam_profits
stock_reduction ["scam-page-visits"] = s_reduce_scam_page_visits
stock_reduction ["page-visits"] = s_reduce_page_visits
stock_reduction ["potential-page-visits"] = s_reduce_potential_page_visits
stock_reduction ["data-buyer-money"] = s_reduce_data_buyer_money
stock_reduction ["browsing-data"] = s_reduce_browsing_data
stock_reduction ["grey-area-entities"] = s_reduce_grey_area_entities
stock_reduction ["airlock-lookups"] = s_reduce_airlock_lookups
stock_reduction ["potential-airlock-lookups"] = s_reduce_potential_airlock_lookups
stock_reduction ["airlock-users"] = s_reduce_airlock_users
stock_reduction ["browser-users"] = s_reduce_browser_users
stock_reduction ["intr-investments"] = s_reduce_intr_investments
stock_reduction ["crypto-investments"] = s_reduce_crypto_investments
stock_reduction ["money-mint"] = s_reduce_money_mint
stock_reduction ["money-supply"] = s_reduce_money_supply
stock_reduction ["token-rewards-pool"] = s_reduce_token_rewards_pool
stock_reduction ["token-stake-pool"] = s_reduce_token_stake_pool
stock_reduction ["token-hold-pool"] = s_reduce_token_hold_pool
stock_reduction ["token-sell-pool"] = s_reduce_token_sell_pool
stock_reduction ["token-mint"] = s_reduce_token_mint
stock_aggregation = {}
stock_aggregation ["scam-upkeep"] = s_aggregate_scam_upkeep
stock_aggregation ["scam-profits"] = s_aggregate_scam_profits
stock_aggregation ["scam-page-successes"] = s_aggregate_scam_page_successes
stock_aggregation ["scam-page-visits"] = s_aggregate_scam_page_visits
stock_aggregation ["page-visits"] = s_aggregate_page_visits
stock_aggregation ["airlock-revenue"] = s_aggregate_airlock_revenue
stock_aggregation ["airlock-data-shared"] = s_aggregate_airlock_data_shared
stock_aggregation ["resolved-entities"] = s_aggregate_resolved_entities
stock_aggregation ["grey-area-entities"] = s_aggregate_grey_area_entities
stock_aggregation ["airlock-lookups"] = s_aggregate_airlock_lookups
stock_aggregation ["browser-users"] = s_aggregate_browser_users
stock_aggregation ["airlock-users"] = s_aggregate_airlock_users
stock_aggregation ["intr-investments"] = s_aggregate_intr_investments
stock_aggregation ["crypto-investments"] = s_aggregate_crypto_investments
stock_aggregation ["money-supply"] = s_aggregate_money_supply
stock_aggregation ["money-reclaimed"] = s_aggregate_money_reclaimed
stock_aggregation ["token-stake-pool"] = s_aggregate_token_stake_pool
stock_aggregation ["token-rewards-pool"] = s_aggregate_token_rewards_pool
stock_aggregation ["token-hold-pool"] = s_aggregate_token_hold_pool
stock_aggregation ["token-sell-pool"] = s_aggregate_token_sell_pool
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


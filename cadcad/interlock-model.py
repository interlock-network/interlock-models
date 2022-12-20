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
from IPython.utils import io
def s_token_price_delta_updates_change_max_stake (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = mul_ls ([100] + get_new_value (s, "token-price-delta") + [_params ["token-price-delta-change-max-stake"]])
    append_each (points, new_val)

def s_token_price_delta_updates_change_stake_yield (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = mul_ls ([100] + get_new_value (s, "token-price-delta") + [_params ["token-price-delta-change-stake-yield"]])
    append_each (points, new_val)

def s_token_price_delta_updates_change_lookup_fee (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = mul_ls ([100] + get_new_value (s, "token-price-delta") + [_params ["token-price-delta-change-lookup-fee"]])
    append_each (points, new_val)

def s_token_price_delta_updates_change_user_fee (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = mul_ls ([100] + get_new_value (s, "token-price-delta") + [_params ["token-price-delta-change-user-fee"]])
    append_each (points, new_val)

def s_token_price_delta_updates_change_buyback_amount (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = mul_ls ([100] + get_new_value (s, "token-price-delta") + [_params ["token-price-delta-change-buyback-amount"]])
    append_each (points, new_val)

def s_token_price_delta_updates_change_reward_amount (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = mul_ls ([100] + get_new_value (s, "token-price-delta") + [_params ["token-price-delta-change-reward-amount"]])
    append_each (points, new_val)

def s_user_goal_progress_updates_change_max_stake (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = mul_ls ([100] + get_new_value (s, "user-goal-progress") + [_params ["user-goal-progress-change-max-stake"]])
    append_each (points, new_val)

def s_user_goal_progress_updates_change_stake_yield (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = mul_ls ([100] + get_new_value (s, "user-goal-progress") + [_params ["user-goal-progress-change-stake-yield"]])
    append_each (points, new_val)

def s_user_goal_progress_updates_change_lookup_fee (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = mul_ls ([100] + get_new_value (s, "user-goal-progress") + [_params ["user-goal-progress-change-lookup-fee"]])
    append_each (points, new_val)

def s_user_goal_progress_updates_change_user_fee (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = mul_ls ([100] + get_new_value (s, "user-goal-progress") + [_params ["user-goal-progress-change-user-fee"]])
    append_each (points, new_val)

def s_user_goal_progress_updates_change_buyback_amount (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = mul_ls ([100] + get_new_value (s, "user-goal-progress") + [_params ["user-goal-progress-change-buyback-amount"]])
    append_each (points, new_val)

def s_user_goal_progress_updates_change_reward_amount (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = mul_ls ([100] + get_new_value (s, "user-goal-progress") + [_params ["user-goal-progress-change-reward-amount"]])
    append_each (points, new_val)

def s_anti_user_goal_progress_updates_change_max_stake (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = mul_ls ([100] + get_new_value (s, "anti-user-goal-progress") + [_params ["anti-user-goal-progress-change-max-stake"]])
    append_each (points, new_val)

def s_anti_user_goal_progress_updates_change_stake_yield (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = mul_ls ([100] + get_new_value (s, "anti-user-goal-progress") + [_params ["anti-user-goal-progress-change-stake-yield"]])
    append_each (points, new_val)

def s_anti_user_goal_progress_updates_change_lookup_fee (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = mul_ls ([100] + get_new_value (s, "anti-user-goal-progress") + [_params ["anti-user-goal-progress-change-lookup-fee"]])
    append_each (points, new_val)

def s_anti_user_goal_progress_updates_change_user_fee (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = mul_ls ([100] + get_new_value (s, "anti-user-goal-progress") + [_params ["anti-user-goal-progress-change-user-fee"]])
    append_each (points, new_val)

def s_anti_user_goal_progress_updates_change_buyback_amount (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = mul_ls ([100] + get_new_value (s, "anti-user-goal-progress") + [_params ["anti-user-goal-progress-change-buyback-amount"]])
    append_each (points, new_val)

def s_anti_user_goal_progress_updates_change_reward_amount (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = mul_ls ([100] + get_new_value (s, "anti-user-goal-progress") + [_params ["anti-user-goal-progress-change-reward-amount"]])
    append_each (points, new_val)

def s_token_price_updates_swing_order_book (ctx, s, _params):
    if ctx.get ("buy-price") == None:
        ctx ["buy-price"] = []
    
    buy_price = ctx.get ("buy-price")
    new_val = get_new_value (s, "token-price")
    append_each (buy_price, new_val)

def s_token_price_updates_position_order_book (ctx, s, _params):
    if ctx.get ("buy-price") == None:
        ctx ["buy-price"] = []
    
    buy_price = ctx.get ("buy-price")
    new_val = get_new_value (s, "token-price")
    append_each (buy_price, new_val)

def s_token_price_updates_investor_order_book (ctx, s, _params):
    if ctx.get ("buy-price") == None:
        ctx ["buy-price"] = []
    
    buy_price = ctx.get ("buy-price")
    new_val = get_new_value (s, "token-price")
    append_each (buy_price, new_val)

def s_token_price_updates_hodler_order_book (ctx, s, _params):
    if ctx.get ("buy-price") == None:
        ctx ["buy-price"] = []
    
    buy_price = ctx.get ("buy-price")
    new_val = get_new_value (s, "token-price")
    append_each (buy_price, new_val)

def s_clock_updates_swing_order_book (ctx, s, _params):
    if ctx.get ("sell-time") == None:
        ctx ["sell-time"] = []
    
    sell_time = ctx.get ("sell-time")
    new_val = sum_ls ([1] + get_new_value (s, "clock"))
    append_each (sell_time, new_val)

def s_clock_updates_position_order_book (ctx, s, _params):
    if ctx.get ("sell-time") == None:
        ctx ["sell-time"] = []
    
    sell_time = ctx.get ("sell-time")
    new_val = sum_ls ([2] + get_new_value (s, "clock"))
    append_each (sell_time, new_val)

def s_clock_updates_investor_order_book (ctx, s, _params):
    if ctx.get ("sell-time") == None:
        ctx ["sell-time"] = []
    
    sell_time = ctx.get ("sell-time")
    new_val = sum_ls ([4] + get_new_value (s, "clock"))
    append_each (sell_time, new_val)

def s_clock_updates_hodler_order_book (ctx, s, _params):
    if ctx.get ("sell-time") == None:
        ctx ["sell-time"] = []
    
    sell_time = ctx.get ("sell-time")
    new_val = sum_ls ([200] + get_new_value (s, "clock"))
    append_each (sell_time, new_val)

def s_token_hold_rate_updates_swing_order_book (ctx, s, _params):
    if ctx.get ("quantity") == None:
        ctx ["quantity"] = []
    
    quantity = ctx.get ("quantity")
    new_val = mul_ls ([_params ["swing-traders"]] + get_new_value (s, "token-hold-rate"))
    append_each (quantity, new_val)

def s_token_hold_rate_updates_position_order_book (ctx, s, _params):
    if ctx.get ("quantity") == None:
        ctx ["quantity"] = []
    
    quantity = ctx.get ("quantity")
    new_val = mul_ls ([_params ["position-traders"]] + get_new_value (s, "token-hold-rate"))
    append_each (quantity, new_val)

def s_token_hold_rate_updates_investor_order_book (ctx, s, _params):
    if ctx.get ("quantity") == None:
        ctx ["quantity"] = []
    
    quantity = ctx.get ("quantity")
    new_val = mul_ls ([_params ["investors"]] + get_new_value (s, "token-hold-rate"))
    append_each (quantity, new_val)

def s_token_hold_rate_updates_hodler_order_book (ctx, s, _params):
    if ctx.get ("quantity") == None:
        ctx ["quantity"] = []
    
    quantity = ctx.get ("quantity")
    new_val = mul_ls ([_params ["hodlers"]] + get_new_value (s, "token-hold-rate"))
    append_each (quantity, new_val)

def s_swing_order_book_updates_swing_order_book (ctx, s, _params):
    if ctx.get ("removable") == None:
        ctx ["removable"] = []
    
    removable = ctx.get ("removable")
    new_val = agg_rows_range ([[LessThanEq (mul_ls (get_new_value (s, "token-price") + diff_ls ([1] + [_params ["minimum-trade-profit"]]))), LessThanEq (get_new_value (s, "clock"))]], get_new_value (s, "swing-order-book"))
    append_each (removable, new_val)

def s_position_order_book_updates_position_order_book (ctx, s, _params):
    if ctx.get ("removable") == None:
        ctx ["removable"] = []
    
    removable = ctx.get ("removable")
    new_val = agg_rows_range ([[LessThanEq (mul_ls (get_new_value (s, "token-price") + diff_ls ([1] + [_params ["minimum-trade-profit"]]))), LessThanEq (get_new_value (s, "clock"))]], get_new_value (s, "position-order-book"))
    append_each (removable, new_val)

def s_investor_order_book_updates_investor_order_book (ctx, s, _params):
    if ctx.get ("removable") == None:
        ctx ["removable"] = []
    
    removable = ctx.get ("removable")
    new_val = agg_rows_range ([[LessThanEq (mul_ls (get_new_value (s, "token-price") + diff_ls ([1] + [_params ["minimum-trade-profit"]]))), LessThanEq (get_new_value (s, "clock"))]], get_new_value (s, "investor-order-book"))
    append_each (removable, new_val)

def s_swing_order_book_updates_token_unhold_rate (ctx, s, _params):
    if ctx.get ("quantity") == None:
        ctx ["quantity"] = []
    
    quantity = ctx.get ("quantity")
    new_val = sum_ls (agg_to_list (agg_col_to_list (2, agg_rows_range ([[LessThanEq (mul_ls (get_new_value (s, "token-price") + diff_ls ([1] + [_params ["minimum-trade-profit"]]))), LessThanEq (get_new_value (s, "clock"))]], get_new_value (s, "swing-order-book")))))
    append_each (quantity, new_val)

def s_position_order_book_updates_token_unhold_rate (ctx, s, _params):
    if ctx.get ("quantity") == None:
        ctx ["quantity"] = []
    
    quantity = ctx.get ("quantity")
    new_val = sum_ls (agg_to_list (agg_col_to_list (2, agg_rows_range ([[LessThanEq (mul_ls (get_new_value (s, "token-price") + diff_ls ([1] + [_params ["minimum-trade-profit"]]))), LessThanEq (get_new_value (s, "clock"))]], get_new_value (s, "position-order-book")))))
    append_each (quantity, new_val)

def s_investor_order_book_updates_token_unhold_rate (ctx, s, _params):
    if ctx.get ("quantity") == None:
        ctx ["quantity"] = []
    
    quantity = ctx.get ("quantity")
    new_val = sum_ls (agg_to_list (agg_col_to_list (2, agg_rows_range ([[LessThanEq (mul_ls (get_new_value (s, "token-price") + diff_ls ([1] + [_params ["minimum-trade-profit"]]))), LessThanEq (get_new_value (s, "clock"))]], get_new_value (s, "investor-order-book")))))
    append_each (quantity, new_val)

def s_crypto_hype_updates_staking_enthusiasm (ctx, s, _params):
    if ctx.get ("expectation-multiplier") == None:
        ctx ["expectation-multiplier"] = []
    
    expectation_multiplier = ctx.get ("expectation-multiplier")
    new_val = [4] if lt_eq_ls (get_new_value (s, "crypto-hype") + [0]) [0] else [1]
    append_each (expectation_multiplier, new_val)

def s_crypto_hype_updates_interlock_hype (ctx, s, _params):
    if ctx.get ("crypto-hype") == None:
        ctx ["crypto-hype"] = []
    
    crypto_hype = ctx.get ("crypto-hype")
    new_val = get_new_value (s, "crypto-hype")
    append_each (crypto_hype, new_val)

def s_crypto_hype_updates_crypto_invest_rate (ctx, s, _params):
    if ctx.get ("crypto-hype") == None:
        ctx ["crypto-hype"] = []
    
    crypto_hype = ctx.get ("crypto-hype")
    new_val = get_new_value (s, "crypto-hype")
    append_each (crypto_hype, new_val)

def s_crypto_hype_updates_crypto_divest_rate (ctx, s, _params):
    if ctx.get ("crypto-hype") == None:
        ctx ["crypto-hype"] = []
    
    crypto_hype = ctx.get ("crypto-hype")
    new_val = get_new_value (s, "crypto-hype")
    append_each (crypto_hype, new_val)

def s_crypto_hype_updates_intr_invest_rate (ctx, s, _params):
    if ctx.get ("crypto-hype") == None:
        ctx ["crypto-hype"] = []
    
    crypto_hype = ctx.get ("crypto-hype")
    new_val = get_new_value (s, "crypto-hype")
    append_each (crypto_hype, new_val)

def s_crypto_hype_updates_intr_divest_rate (ctx, s, _params):
    if ctx.get ("crypto-hype") == None:
        ctx ["crypto-hype"] = []
    
    crypto_hype = ctx.get ("crypto-hype")
    new_val = get_new_value (s, "crypto-hype")
    append_each (crypto_hype, new_val)

def s_interlock_hype_updates_airlock_adoption_rate (ctx, s, _params):
    if ctx.get ("crypto-hype") == None:
        ctx ["crypto-hype"] = []
    
    crypto_hype = ctx.get ("crypto-hype")
    new_val = get_new_value (s, "interlock-hype")
    append_each (crypto_hype, new_val)

def s_money_growth_rate_updates_money_mint_rate (ctx, s, _params):
    if ctx.get ("growth") == None:
        ctx ["growth"] = []
    
    growth = ctx.get ("growth")
    new_val = get_new_value (s, "money-growth-rate")
    append_each (growth, new_val)

def s_money_growth_rate_updates_money_reclaim_rate (ctx, s, _params):
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

def s_cumulate_token_sell_pool (_params, substep, sH, s, _input, **kwargs):
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


def s_cumulate_token_rewards_pool (_params, substep, sH, s, _input, **kwargs):
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

def s_cumulate_token_stake_pool (_params, substep, sH, s, _input, **kwargs):
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


def s_cumulate_token_hold_pool (_params, substep, sH, s, _input, **kwargs):
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

def s_staking_enthusiasm_updates_token_stake_rate (ctx, s, _params):
    if ctx.get ("enthusiasm") == None:
        ctx ["enthusiasm"] = []
    
    enthusiasm = ctx.get ("enthusiasm")
    new_val = get_new_value (s, "staking-enthusiasm")
    append_each (enthusiasm, new_val)

def s_commit_token_unstake_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "token-unstake-rate", update_state (s, "token-unstake-rate", [adjusted_flows ["token-unstake-rate"]])

def s_token_reward_to_sell_rate_updates_reward_rate (ctx, s, _params):
    if ctx.get ("rewards-sold") == None:
        ctx ["rewards-sold"] = []
    
    rewards_sold = ctx.get ("rewards-sold")
    new_val = div_ls (get_new_value (s, "token-reward-to-sell-rate") + max_ls ([1] + get_new_value (s, "airlock-users")))
    append_each (rewards_sold, new_val)

def s_token_reward_to_held_rate_updates_reward_rate (ctx, s, _params):
    if ctx.get ("rewards-held") == None:
        ctx ["rewards-held"] = []
    
    rewards_held = ctx.get ("rewards-held")
    new_val = div_ls (get_new_value (s, "token-reward-to-held-rate") + max_ls ([1] + get_new_value (s, "airlock-users")))
    append_each (rewards_held, new_val)

def s_token_reward_to_sell_rate_updates_airlock_abandonment_rate (ctx, s, _params):
    if ctx.get ("rewards-sold") == None:
        ctx ["rewards-sold"] = []
    
    rewards_sold = ctx.get ("rewards-sold")
    new_val = div_ls (get_old_value (s, "token-reward-to-sell-rate") + max_ls ([1] + get_new_value (s, "token-reward-to-sell-rate")))
    append_each (rewards_sold, new_val)

def s_token_reward_to_held_rate_updates_airlock_abandonment_rate (ctx, s, _params):
    if ctx.get ("rewards-held") == None:
        ctx ["rewards-held"] = []
    
    rewards_held = ctx.get ("rewards-held")
    new_val = div_ls (get_old_value (s, "token-reward-to-held-rate") + max_ls ([1] + get_new_value (s, "token-reward-to-held-rate")))
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


def s_cumulate_money_supply (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "crypto-divest-rate") + get_new_value (s, "money-mint-rate"))
    return "money-supply", update_state (s, "money-supply", sum_ls (get_new_value (s, "money-supply") + agg))

def s_reduce_money_supply (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "crypto-invest-rate") + get_new_value (s, "money-reclaim-rate"))
    return "money-supply", update_state (s, "money-supply", diff_ls (get_new_value (s, "money-supply") + red))

def s_cumulate_money_reclaimed (_params, substep, sH, s, _input, **kwargs):
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


def s_cumulate_crypto_investments (_params, substep, sH, s, _input, **kwargs):
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

def s_cumulate_intr_investments (_params, substep, sH, s, _input, **kwargs):
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

def s_intr_investments_updates_token_hold_rate (ctx, s, _params):
    if ctx.get ("invested") == None:
        ctx ["invested"] = []
    
    invested = ctx.get ("invested")
    new_val = max_ls (diff_ls (get_new_value (s, "intr-investments") + get_old_value (s, "intr-investments")) + [0])
    append_each (invested, new_val)

def s_money_supply_updates_crypto_hype (ctx, s, _params):
    if ctx.get ("extra-cash-growth") == None:
        ctx ["extra-cash-growth"] = []
    
    extra_cash_growth = ctx.get ("extra-cash-growth")
    new_val = div_ls (get_new_value (s, "money-supply") + get_old_value (s, "money-supply"))
    append_each (extra_cash_growth, new_val)

def s_token_hold_pool_updates_avg_token_value (ctx, s, _params):
    if ctx.get ("held") == None:
        ctx ["held"] = []
    
    held = ctx.get ("held")
    new_val = get_new_value (s, "token-hold-pool")
    append_each (held, new_val)

def s_intr_investments_updates_avg_token_value (ctx, s, _params):
    if ctx.get ("invested") == None:
        ctx ["invested"] = []
    
    invested = ctx.get ("invested")
    new_val = get_new_value (s, "intr-investments")
    append_each (invested, new_val)

def s_token_sell_pool_updates_token_price (ctx, s, _params):
    if ctx.get ("sell-pool") == None:
        ctx ["sell-pool"] = []
    
    sell_pool = ctx.get ("sell-pool")
    new_val = get_new_value (s, "token-sell-pool")
    append_each (sell_pool, new_val)

def s_intr_investments_updates_token_price (ctx, s, _params):
    if ctx.get ("invest-pool") == None:
        ctx ["invest-pool"] = []
    
    invest_pool = ctx.get ("invest-pool")
    new_val = get_new_value (s, "intr-investments")
    append_each (invest_pool, new_val)

def s_token_price_updates_token_profit (ctx, s, _params):
    if ctx.get ("price-delta-pct") == None:
        ctx ["price-delta-pct"] = []
    
    price_delta_pct = ctx.get ("price-delta-pct")
    new_val = div_ls (get_new_value (s, "token-price") + get_old_value (s, "token-price"))
    append_each (price_delta_pct, new_val)

def s_token_price_updates_airlock_lookup_price (ctx, s, _params):
    if ctx.get ("price-delta-pct") == None:
        ctx ["price-delta-pct"] = []
    
    price_delta_pct = ctx.get ("price-delta-pct")
    new_val = div_ls (get_new_value (s, "token-price") + get_old_value (s, "token-price"))
    append_each (price_delta_pct, new_val)

def s_airlock_expenses_updates_airlock_lookup_price (ctx, s, _params):
    if ctx.get ("expenses") == None:
        ctx ["expenses"] = []
    
    expenses = ctx.get ("expenses")
    new_val = get_new_value (s, "airlock-expenses")
    append_each (expenses, new_val)

def s_airlock_expenses_updates_airlock_upkeep_rate (ctx, s, _params):
    if ctx.get ("expenses") == None:
        ctx ["expenses"] = []
    
    expenses = ctx.get ("expenses")
    new_val = get_new_value (s, "airlock-expenses")
    append_each (expenses, new_val)

def s_airlock_lookup_price_updates_airlock_share_rate (ctx, s, _params):
    if ctx.get ("lookup-price") == None:
        ctx ["lookup-price"] = []
    
    lookup_price = ctx.get ("lookup-price")
    new_val = get_new_value (s, "airlock-lookup-price")
    append_each (lookup_price, new_val)

def s_airlock_lookup_price_updates_intr_invest_rate (ctx, s, _params):
    if ctx.get ("lookup-price") == None:
        ctx ["lookup-price"] = []
    
    lookup_price = ctx.get ("lookup-price")
    new_val = get_new_value (s, "airlock-lookup-price")
    append_each (lookup_price, new_val)

def s_token_price_updates_intr_invest_rate (ctx, s, _params):
    if ctx.get ("price-delta-pct") == None:
        ctx ["price-delta-pct"] = []
    
    price_delta_pct = ctx.get ("price-delta-pct")
    new_val = div_ls (get_old_value (s, "token-price") + get_new_value (s, "token-price"))
    append_each (price_delta_pct, new_val)

def s_token_price_updates_reward_rate (ctx, s, _params):
    if ctx.get ("price") == None:
        ctx ["price"] = []
    
    price = ctx.get ("price")
    new_val = get_new_value (s, "token-price")
    append_each (price, new_val)

def s_token_profit_updates_intr_divest_rate (ctx, s, _params):
    if ctx.get ("profit-delta-pct") == None:
        ctx ["profit-delta-pct"] = []
    
    profit_delta_pct = ctx.get ("profit-delta-pct")
    new_val = div_ls (get_new_value (s, "token-profit") + get_old_value (s, "token-profit"))
    append_each (profit_delta_pct, new_val)

def s_heuristics_updates_heuristic_contradictions (ctx, s, _params):
    if ctx.get ("heur") == None:
        ctx ["heur"] = []
    
    heur = ctx.get ("heur")
    new_val = get_new_value (s, "heuristics")
    append_each (heur, new_val)

def s_anti_heuristics_updates_heuristic_contradictions (ctx, s, _params):
    if ctx.get ("anti") == None:
        ctx ["anti"] = []
    
    anti = ctx.get ("anti")
    new_val = get_new_value (s, "anti-heuristics")
    append_each (anti, new_val)

def s_stake_yield_updates_token_reward_to_held_rate (ctx, s, _params):
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

def s_cumulate_page_visits (_params, substep, sH, s, _input, **kwargs):
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

def s_cumulate_airlock_lookups (_params, substep, sH, s, _input, **kwargs):
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

def s_cumulate_airlock_data_shared (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "airlock-share-rate"))
    return "airlock-data-shared", update_state (s, "airlock-data-shared", sum_ls (get_new_value (s, "airlock-data-shared") + agg))

def s_adjust_airlock_revenue_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "airlock-upkeep-rate") [0]
    inventory = get_new_value (s, "airlock-revenue") [0]
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["airlock-upkeep-rate"] = flow_val

def s_cumulate_airlock_revenue (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "airlock-revenue-rate"))
    return "airlock-revenue", update_state (s, "airlock-revenue", sum_ls (get_new_value (s, "airlock-revenue") + agg))

def s_reduce_airlock_revenue (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "airlock-upkeep-rate"))
    return "airlock-revenue", update_state (s, "airlock-revenue", diff_ls (get_new_value (s, "airlock-revenue") + red))

def s_cumulate_airlock_upkeep (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "airlock-upkeep-rate"))
    return "airlock-upkeep", update_state (s, "airlock-upkeep", sum_ls (get_new_value (s, "airlock-upkeep") + agg))

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

def s_cumulate_browser_users (_params, substep, sH, s, _input, **kwargs):
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

def s_cumulate_airlock_users (_params, substep, sH, s, _input, **kwargs):
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

def s_cumulate_grey_area_entities (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "grey-area-entity-rate"))
    return "grey-area-entities", update_state (s, "grey-area-entities", sum_ls (get_new_value (s, "grey-area-entities") + agg))

def s_reduce_grey_area_entities (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "resolution-rate"))
    return "grey-area-entities", update_state (s, "grey-area-entities", diff_ls (get_new_value (s, "grey-area-entities") + red))

def s_cumulate_resolved_entities (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "resolution-rate"))
    return "resolved-entities", update_state (s, "resolved-entities", sum_ls (get_new_value (s, "resolved-entities") + agg))

def s_adjust_scam_page_visits_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "scam-page-success-rate") [0]
    inventory = get_new_value (s, "scam-page-visits") [0]
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["scam-page-success-rate"] = flow_val

def s_cumulate_scam_page_visits (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "scam-page-visit-rate"))
    return "scam-page-visits", update_state (s, "scam-page-visits", sum_ls (get_new_value (s, "scam-page-visits") + agg))

def s_reduce_scam_page_visits (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "scam-page-success-rate"))
    return "scam-page-visits", update_state (s, "scam-page-visits", diff_ls (get_new_value (s, "scam-page-visits") + red))

def s_cumulate_scam_page_successes (_params, substep, sH, s, _input, **kwargs):
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

def s_cumulate_scam_profits (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "scam-profit-rate"))
    return "scam-profits", update_state (s, "scam-profits", sum_ls (get_new_value (s, "scam-profits") + agg))

def s_reduce_scam_profits (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "scam-upkeep-rate"))
    return "scam-profits", update_state (s, "scam-profits", diff_ls (get_new_value (s, "scam-profits") + red))

def s_cumulate_scam_upkeep (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "scam-upkeep-rate"))
    return "scam-upkeep", update_state (s, "scam-upkeep", sum_ls (get_new_value (s, "scam-upkeep") + agg))

def s_token_price_updates_token_price_delta (ctx, s, _params):
    if ctx.get ("stim") == None:
        ctx ["stim"] = []
    
    stim = ctx.get ("stim")
    new_val = div_ls (get_new_value (s, "token-price") + get_old_value (s, "token-price"))
    append_each (stim, new_val)

def s_airlock_users_updates_user_goal_progress (ctx, s, _params):
    if ctx.get ("stim") == None:
        ctx ["stim"] = []
    
    stim = ctx.get ("stim")
    new_val = div_ls (get_new_value (s, "airlock-users") + [100000000])
    append_each (stim, new_val)

def s_airlock_users_updates_anti_user_goal_progress (ctx, s, _params):
    if ctx.get ("stim") == None:
        ctx ["stim"] = []
    
    stim = ctx.get ("stim")
    new_val = div_ls (diff_ls ([100000000] + get_new_value (s, "airlock-users")) + [100000000])
    append_each (stim, new_val)

def s_change_max_stake_updates_max_stake (ctx, s, _params):
    if ctx.get ("mul-max-stake") == None:
        ctx ["mul-max-stake"] = []
    
    mul_max_stake = ctx.get ("mul-max-stake")
    new_val = mul_ls (get_new_value (s, "change-max-stake") + [5]) if gt_ls (get_new_value (s, "change-max-stake") + [0]) [0] else [0]
    append_each (mul_max_stake, new_val)

def s_change_stake_yield_updates_stake_yield (ctx, s, _params):
    if ctx.get ("mul-stake-yield") == None:
        ctx ["mul-stake-yield"] = []
    
    mul_stake_yield = ctx.get ("mul-stake-yield")
    new_val = sum_ls ([1] + div_ls (get_new_value (s, "change-stake-yield") + [100])) if gt_ls (get_new_value (s, "change-stake-yield") + [0]) [0] else [0]
    append_each (mul_stake_yield, new_val)

def s_change_lookup_fee_updates_airlock_lookup_price (ctx, s, _params):
    if ctx.get ("mul-lookup-fee") == None:
        ctx ["mul-lookup-fee"] = []
    
    mul_lookup_fee = ctx.get ("mul-lookup-fee")
    new_val = div_ls (mul_ls (get_new_value (s, "change-lookup-fee") + [3]) + [1000000]) if gt_ls (get_new_value (s, "change-lookup-fee") + [0]) [0] else [0]
    append_each (mul_lookup_fee, new_val)

def s_change_user_fee_updates_airlock_lookup_price (ctx, s, _params):
    if ctx.get ("mul-user-fee") == None:
        ctx ["mul-user-fee"] = []
    
    mul_user_fee = ctx.get ("mul-user-fee")
    new_val = div_ls (mul_ls (get_new_value (s, "change-user-fee") + [3]) + [100]) if gt_ls (get_new_value (s, "change-user-fee") + [0]) [0] else [0]
    append_each (mul_user_fee, new_val)

def s_change_buyback_amount_updates_token_hold_rate (ctx, s, _params):
    if ctx.get ("mul-buyback-amount") == None:
        ctx ["mul-buyback-amount"] = []
    
    mul_buyback_amount = ctx.get ("mul-buyback-amount")
    new_val = div_ls (get_new_value (s, "change-buyback-amount") + [100]) if gt_ls (get_new_value (s, "change-buyback-amount") + [0]) [0] else [0]
    append_each (mul_buyback_amount, new_val)

def s_change_reward_amount_updates_token_reward_to_sell_rate (ctx, s, _params):
    if ctx.get ("mul-reward-rate") == None:
        ctx ["mul-reward-rate"] = []
    
    mul_reward_rate = ctx.get ("mul-reward-rate")
    new_val = div_ls (get_new_value (s, "change-reward-amount") + [100]) if gt_ls (get_new_value (s, "change-reward-amount") + [0]) [0] else [0]
    append_each (mul_reward_rate, new_val)

def s_change_reward_amount_updates_token_reward_to_held_rate (ctx, s, _params):
    if ctx.get ("mul-reward-rate") == None:
        ctx ["mul-reward-rate"] = []
    
    mul_reward_rate = ctx.get ("mul-reward-rate")
    new_val = div_ls (get_new_value (s, "change-reward-amount") + [100]) if gt_ls (get_new_value (s, "change-reward-amount") + [0]) [0] else [0]
    append_each (mul_reward_rate, new_val)

def s_reward_rate_updates_growth_level (ctx, s, _params):
    if ctx.get ("reward-rate-delta") == None:
        ctx ["reward-rate-delta"] = []
    
    reward_rate_delta = ctx.get ("reward-rate-delta")
    new_val = diff_ls (get_new_value (s, "reward-rate") + get_old_value (s, "reward-rate"))
    append_each (reward_rate_delta, new_val)

def s_growth_level_updates_airlock_adoption_rate (ctx, s, _params):
    if ctx.get ("growth") == None:
        ctx ["growth"] = []
    
    growth = ctx.get ("growth")
    new_val = get_new_value (s, "growth-level")
    append_each (growth, new_val)

def s_airlock_users_updates_airlock_adoption_rate (ctx, s, _params):
    if ctx.get ("users") == None:
        ctx ["users"] = []
    
    users = ctx.get ("users")
    new_val = get_new_value (s, "airlock-users")
    append_each (users, new_val)

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

def s_staking_enthusiasm_updates_token_unstake_rate (ctx, s, _params):
    if ctx.get ("enthusiasm") == None:
        ctx ["enthusiasm"] = []
    
    enthusiasm = ctx.get ("enthusiasm")
    new_val = get_old_value (s, "staking-enthusiasm")
    append_each (enthusiasm, new_val)

def s_staking_opportunities_updates_token_unstake_rate (ctx, s, _params):
    if ctx.get ("staking-ops") == None:
        ctx ["staking-ops"] = []
    
    staking_ops = ctx.get ("staking-ops")
    new_val = get_old_value (s, "staking-opportunities")
    append_each (staking_ops, new_val)

def s_commit_airlock_share_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "airlock-share-rate", update_state (s, "airlock-share-rate", [adjusted_flows ["airlock-share-rate"]])

def s_commit_airlock_revenue_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "airlock-revenue-rate", update_state (s, "airlock-revenue-rate", [adjusted_flows ["airlock-revenue-rate"]])

def s_commit_airlock_upkeep_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "airlock-upkeep-rate", update_state (s, "airlock-upkeep-rate", [adjusted_flows ["airlock-upkeep-rate"]])

def s_commit_page_visit_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "page-visit-rate", update_state (s, "page-visit-rate", [adjusted_flows ["page-visit-rate"]])

def s_commit_scam_page_visit_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "scam-page-visit-rate", update_state (s, "scam-page-visit-rate", [adjusted_flows ["scam-page-visit-rate"]])

def s_commit_scam_page_success_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "scam-page-success-rate", update_state (s, "scam-page-success-rate", [adjusted_flows ["scam-page-success-rate"]])

def s_scam_page_successes_updates_fitness (ctx, s, _params):
    if ctx.get ("scams") == None:
        ctx ["scams"] = []
    
    scams = ctx.get ("scams")
    new_val = get_new_value (s, "scam-page-successes")
    append_each (scams, new_val)

def s_token_price_updates_fitness (ctx, s, _params):
    if ctx.get ("price") == None:
        ctx ["price"] = []
    
    price = ctx.get ("price")
    new_val = get_new_value (s, "token-price")
    append_each (price, new_val)

def s_scam_page_successes_updates_scam_profit_rate (ctx, s, _params):
    if ctx.get ("total-pages") == None:
        ctx ["total-pages"] = []
    
    total_pages = ctx.get ("total-pages")
    new_val = diff_ls (get_new_value (s, "scam-page-successes") + get_old_value (s, "scam-page-successes"))
    append_each (total_pages, new_val)

def s_scam_profits_per_page_updates_scam_profit_rate (ctx, s, _params):
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

def s_airlock_users_updates_scam_page_success_rate (ctx, s, _params):
    if ctx.get ("user-share") == None:
        ctx ["user-share"] = []
    
    user_share = ctx.get ("user-share")
    new_val = div_ls (get_new_value (s, "airlock-users") + get_new_value (s, "browser-users"))
    append_each (user_share, new_val)

def s_airlock_users_updates_airlock_lookup_price (ctx, s, _params):
    if ctx.get ("users") == None:
        ctx ["users"] = []
    
    users = ctx.get ("users")
    new_val = get_new_value (s, "airlock-users")
    append_each (users, new_val)

def s_page_visit_rate_updates_airlock_lookup_rate (ctx, s, _params):
    if ctx.get ("pages-visited") == None:
        ctx ["pages-visited"] = []
    
    pages_visited = ctx.get ("pages-visited")
    new_val = get_new_value (s, "page-visit-rate")
    append_each (pages_visited, new_val)

def s_airlock_users_updates_airlock_lookup_rate (ctx, s, _params):
    if ctx.get ("user-share") == None:
        ctx ["user-share"] = []
    
    user_share = ctx.get ("user-share")
    new_val = div_ls (get_new_value (s, "airlock-users") + get_new_value (s, "browser-users"))
    append_each (user_share, new_val)

def s_airlock_data_shared_updates_token_reward_to_sell_rate (ctx, s, _params):
    if ctx.get ("shared") == None:
        ctx ["shared"] = []
    
    shared = ctx.get ("shared")
    new_val = diff_ls (get_new_value (s, "airlock-data-shared") + get_old_value (s, "airlock-data-shared"))
    append_each (shared, new_val)

def s_airlock_data_shared_updates_token_reward_to_held_rate (ctx, s, _params):
    if ctx.get ("shared") == None:
        ctx ["shared"] = []
    
    shared = ctx.get ("shared")
    new_val = diff_ls (get_new_value (s, "airlock-data-shared") + get_old_value (s, "airlock-data-shared"))
    append_each (shared, new_val)

def s_airlock_lookup_rate_updates_airlock_lookup_price (ctx, s, _params):
    if ctx.get ("lookups") == None:
        ctx ["lookups"] = []
    
    lookups = ctx.get ("lookups")
    new_val = get_new_value (s, "airlock-lookup-rate")
    append_each (lookups, new_val)

def s_airlock_users_updates_airlock_share_rate (ctx, s, _params):
    if ctx.get ("user-share") == None:
        ctx ["user-share"] = []
    
    user_share = ctx.get ("user-share")
    new_val = div_ls (get_new_value (s, "airlock-users") + get_new_value (s, "browser-users"))
    append_each (user_share, new_val)

def s_airlock_revenue_updates_token_hold_rate (ctx, s, _params):
    if ctx.get ("revenue-buys") == None:
        ctx ["revenue-buys"] = []
    
    revenue_buys = ctx.get ("revenue-buys")
    new_val = div_ls (diff_ls (get_new_value (s, "airlock-revenue") + get_old_value (s, "airlock-revenue")) + get_new_value (s, "token-price"))
    append_each (revenue_buys, new_val)

def s_scam_page_success_rate_updates_scammer_innovation (ctx, s, _params):
    if ctx.get ("urgency") == None:
        ctx ["urgency"] = []
    
    urgency = ctx.get ("urgency")
    new_val = [1] if lt_ls (div_ls (get_new_value (s, "scam-page-success-rate") + get_old_value (s, "scam-page-success-rate")) + [0.9]) [0] else [0]
    append_each (urgency, new_val)

def s_scammer_innovation_updates_scam_upkeep_rate (ctx, s, _params):
    if ctx.get ("profit-diverted-to-innovate") == None:
        ctx ["profit-diverted-to-innovate"] = []
    
    profit_diverted_to_innovate = ctx.get ("profit-diverted-to-innovate")
    new_val = mul_ls (get_new_value (s, "scammer-innovation") + [_params ["base-heuristic-cost"]])
    append_each (profit_diverted_to_innovate, new_val)

def s_scammer_innovation_updates_anti_heuristics (ctx, s, _params):
    if ctx.get ("innovation") == None:
        ctx ["innovation"] = []
    
    innovation = ctx.get ("innovation")
    new_val = get_new_value (s, "scammer-innovation")
    append_each (innovation, new_val)

def s_heuristic_contradictions_updates_scam_page_success_rate (ctx, s, _params):
    if ctx.get ("pass-through") == None:
        ctx ["pass-through"] = []
    
    pass_through = ctx.get ("pass-through")
    new_val = diff_ls ([1] + get_new_value (s, "heuristic-contradictions"))
    append_each (pass_through, new_val)

def s_heuristic_contradictions_updates_airlock_abandonment_rate (ctx, s, _params):
    if ctx.get ("contradiction-delta") == None:
        ctx ["contradiction-delta"] = []
    
    contradiction_delta = ctx.get ("contradiction-delta")
    new_val = get_new_value (s, "heuristic-contradictions")
    append_each (contradiction_delta, new_val)

def s_heuristic_contradictions_updates_grey_area_entity_rate (ctx, s, _params):
    if ctx.get ("contradictions") == None:
        ctx ["contradictions"] = []
    
    contradictions = ctx.get ("contradictions")
    new_val = div_ls (get_new_value (s, "heuristic-contradictions") + [100])
    append_each (contradictions, new_val)

def s_grey_area_entities_updates_staking_opportunities (ctx, s, _params):
    if ctx.get ("grey-stake") == None:
        ctx ["grey-stake"] = []
    
    grey_stake = ctx.get ("grey-stake")
    new_val = mul_ls ([0.5] + get_new_value (s, "grey-area-entities"))
    append_each (grey_stake, new_val)

def s_staking_opportunities_updates_token_stake_rate (ctx, s, _params):
    if ctx.get ("staking-ops") == None:
        ctx ["staking-ops"] = []
    
    staking_ops = ctx.get ("staking-ops")
    new_val = get_new_value (s, "staking-opportunities")
    append_each (staking_ops, new_val)

def s_max_stake_updates_token_stake_rate (ctx, s, _params):
    if ctx.get ("max-per-entity") == None:
        ctx ["max-per-entity"] = []
    
    max_per_entity = ctx.get ("max-per-entity")
    new_val = get_new_value (s, "max-stake")
    append_each (max_per_entity, new_val)

def s_max_stake_updates_token_unstake_rate (ctx, s, _params):
    if ctx.get ("max-per-entity") == None:
        ctx ["max-per-entity"] = []
    
    max_per_entity = ctx.get ("max-per-entity")
    new_val = get_old_value (s, "max-stake")
    append_each (max_per_entity, new_val)

def s_heuristic_contradictions_updates_heuristic_innovation (ctx, s, _params):
    if ctx.get ("urgency") == None:
        ctx ["urgency"] = []
    
    urgency = ctx.get ("urgency")
    new_val = [1] if gt_ls (get_new_value (s, "heuristic-contradictions") + get_old_value (s, "heuristic-contradictions")) [0] else [0]
    append_each (urgency, new_val)

def s_heuristic_innovation_updates_airlock_expenses (ctx, s, _params):
    if ctx.get ("profit-diverted-to-innovate") == None:
        ctx ["profit-diverted-to-innovate"] = []
    
    profit_diverted_to_innovate = ctx.get ("profit-diverted-to-innovate")
    new_val = mul_ls (get_new_value (s, "heuristic-innovation") + [_params ["base-heuristic-cost"]])
    append_each (profit_diverted_to_innovate, new_val)

def s_heuristic_innovation_updates_heuristics (ctx, s, _params):
    if ctx.get ("innovation") == None:
        ctx ["innovation"] = []
    
    innovation = ctx.get ("innovation")
    new_val = get_new_value (s, "heuristic-innovation")
    append_each (innovation, new_val)

morph = lim.Problem ()
sim_rng = None
def tuple_list_to_agg (ls):
    ret = {}
    if len (ls) == 0:
        return ret
    


class Eq:
    def __init__ (self, val):
        self.val = val


    def match (self, cval):
        if isinstance (self.val, list):
            return self.val [0] == cval
        else:
            return self.val == cval
        




class NotEq:
    def __init__ (self, val):
        self.val = val


    def match (self, cval):
        if isinstance (self.val, list):
            return not self.val [0] == cval
        else:
            return not self.val == cval
        




class Any:
    def __init__ (self, val):
        self.val = val


    def match (self, cval):
        return True




class LessThanEq:
    def __init__ (self, val):
        self.val = val


    def match (self, cval):
        if isinstance (self.val, list):
            return self.val [0] <= cval
        else:
            return self.val <= cval
        




class GreaterThanEq:
    def __init__ (self, val):
        self.val = val


    def match (self, cval):
        if isinstance (self.val, list):
            return self.val [0] >= cval
        else:
            return self.val >= cval
        




class LessThan:
    def __init__ (self, val):
        self.val = val


    def match (self, cval):
        if isinstance (self.val, list):
            return self.val [0] < cval
        else:
            return self.val < cval
        




class GreaterThan:
    def __init__ (self, val):
        self.val = val


    def match (self, cval):
        if isinstance (self.val, list):
            return self.val [0] > cval
        else:
            return self.val > cval
        




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
            





def what_if_contradicts_security_users (what_if, security_users):
    return all_true ([not (what_if == const_base_what_if and security_users == 0.1), not (what_if == const_base_what_if and security_users == 0.2), not (what_if == const_base_what_if and security_users == 0.8), not (what_if == const_base_what_if and security_users == 0.9), not (what_if == const_best_case_greedy and not security_users == 0.9), not (what_if == const_worst_case_greedy and not security_users == 0.1), not (what_if == const_best_case_generous and not security_users == 0.1), not (what_if == const_best_case_x and not security_users == 0.1)])


def what_if_contradicts_free_loaders (what_if, free_loaders):
    return all_true ([not (what_if == const_base_what_if and free_loaders == 0.1), not (what_if == const_base_what_if and free_loaders == 0.2), not (what_if == const_base_what_if and free_loaders == 0.8), not (what_if == const_base_what_if and free_loaders == 0.9), not (what_if == const_best_case_greedy and not free_loaders == 0.1), not (what_if == const_worst_case_greedy and not free_loaders == 0.9), not (what_if == const_best_case_generous and not free_loaders == 0.1), not (what_if == const_best_case_x and not free_loaders == 0.1)])


def what_if_contradicts_minimum_trade_profit (what_if, minimum_trade_profit):
    return all_true ([not (what_if == const_base_what_if and minimum_trade_profit == 0.1), not (what_if == const_base_what_if and minimum_trade_profit == 0.2), not (what_if == const_base_what_if and minimum_trade_profit == 0.15), not (what_if == const_best_case_greedy and not minimum_trade_profit == 0.2), not (what_if == const_worst_case_greedy and not minimum_trade_profit == 0.01), not (what_if == const_best_case_generous and not minimum_trade_profit == 0.2), not (what_if == const_best_case_x and not minimum_trade_profit == 0.2)])


def what_if_contradicts_supply_perception (what_if, supply_perception):
    return all_true ([not (what_if == const_best_case_greedy and not supply_perception == const_supply_filling), not (what_if == const_best_case_generous and not supply_perception == const_supply_filling), not (what_if == const_best_case_x and not supply_perception == const_supply_filling), not (what_if == const_worst_case_greedy and not supply_perception == const_supply_expanding), not (what_if == const_worst_case_generous and not supply_perception == const_supply_expanding)])


def what_if_contradicts_token_valuation (what_if, token_valuation):
    return all_true ([not (what_if == const_base_what_if and token_valuation == const_half_value), not (what_if == const_best_case_greedy and not token_valuation == const_half_value), not (what_if == const_worst_case_greedy and not token_valuation == const_tenth_value), not (what_if == const_best_case_x and not token_valuation == const_half_value)])


def what_if_contradicts_heuristic_innovation_scenario (what_if, heuristic_innovation_scenario):
    return all_true ([not (what_if == const_base_what_if and not heuristic_innovation_scenario == const_holding), not (what_if == const_best_case_greedy and not heuristic_innovation_scenario == const_industrialized), not (what_if == const_worst_case_greedy and not heuristic_innovation_scenario == const_industrialized), not (what_if == const_best_case_generous and not heuristic_innovation_scenario == const_industrialized), not (what_if == const_best_case_x and not heuristic_innovation_scenario == const_industrialized)])


def anchor_contradicts_what_if (anchor, what_if):
    return all_true ([not (anchor == const_anchor and not what_if == const_best_case_greedy), not (anchor == const_anchor and what_if == const_best_case_x), not (anchor == const_anchor and what_if == const_worst_case_generous), not (anchor == const_anchor and what_if == const_best_case_generous), not (anchor == const_anchor and what_if == const_base_what_if)])


def what_if_contradicts_max_growth (what_if, max_growth):
    return all_true ([not (what_if == const_best_case_greedy and not max_growth == 1.2), not (what_if == const_worst_case_greedy and not max_growth == 1.2)])


def what_if_contradicts_token_reward_sellers (what_if, token_reward_sellers):
    return all_true ([not (what_if == const_base_what_if and token_reward_sellers == 0.1), not (what_if == const_base_what_if and token_reward_sellers == 0.9), not (what_if == const_best_case_greedy and not token_reward_sellers == 0.1), not (what_if == const_worst_case_greedy and not token_reward_sellers == 0.9), not (what_if == const_best_case_generous and not token_reward_sellers == 0.1), not (what_if == const_best_case_x and not token_reward_sellers == 0.1)])


def what_if_contradicts_vesting_ratio (what_if, vesting_ratio):
    return all_true ([not (what_if == const_base_what_if and vesting_ratio == 0.1), not (what_if == const_base_what_if and vesting_ratio == 0.5), not (what_if == const_best_case_greedy and not vesting_ratio == 0.1), not (what_if == const_worst_case_greedy and not vesting_ratio == 0.5), not (what_if == const_best_case_generous and not vesting_ratio == 0.1), not (what_if == const_best_case_x and not vesting_ratio == 0.1)])


def what_if_contradicts_data_value (what_if, data_value):
    return all_true ([not (what_if == const_base_what_if and data_value == 0.6), not (what_if == const_best_case_greedy and not data_value == 0.6), not (what_if == const_worst_case_greedy and not data_value == 0.1), not (what_if == const_best_case_generous and not data_value == 0.6), not (what_if == const_best_case_x and not data_value == 0.6)])


def what_if_contradicts_max_users (what_if, max_users):
    return all_true ([not (what_if == const_best_case_greedy and not max_users == 100000000), not (what_if == const_worst_case_greedy and not max_users == 100000000)])


def choose_agg_ls (agg, keep, run, default):
    if len (agg) == 0:
        return default
    
    summage = 0
    i = 0
    last = 0
    for tup in agg:
        last = (len (tup) - 1)
        summage = (summage + tup [last])

    choice = sim_random (0, (summage - 1), run)
    for tup in agg:
        last = (len (tup) - 1)
        i = (i + tup [last])
        if i >= choice:
            ret = []
            for k in keep:
                ret.append (tup [k])

            return ret
        



def agg_to_list (agg):
    if isinstance (agg, list):
        return agg
    
    tuples = agg_to_tuple_list (agg)
    ret = []
    for e in tuples:
        for e2 in e:
            ret.append (e2)


    return ret


def list_to_agg (ls, agg_type):
    tuples = agg_to_tuple_list (agg)
    ret = []


def agg_to_tuple_list (agg):
    ret = []
    max_depth = len (agg.schema)
    def add_tuple (tuple):
        ret.append (tuple)


    agg.agg_dict_walk (agg.root, add_tuple, max_depth, ())
    return ret


def agg_choose (agg_or_ls, keep, run, default):
    if isinstance (agg_or_ls, list):
        agg = agg_or_ls [0]
    elif isinstance (agg_or_ls, Aggregation):
        agg = agg_or_ls
    
    return choose_agg_ls (agg_to_tuple_list (agg), keep, run, default)


def agg_load (agg, path):
    ret = agg.root
    for k_or_ls in path:
        if isinstance (k_or_ls, list):
            k = k_or_ls [0]
        else:
            k = k_or_ls
        
        if ret == None:
            return ret
        else:
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



def agg_col_to_list (col, agg_or_ls):
    if isinstance (agg_or_ls, list):
        agg = agg_or_ls [0]
    else:
        agg = agg_or_ls
    
    tuple_list = agg_to_tuple_list (agg)
    ret = []
    depth = 0
    path_len = 1
    for e in tuple_list:
        new = e [col]
        ret.append (new)

    return ret


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
            if path_len >= 2:
                agg_store (ret, new [:path_len], new [path_len])
            else:
                agg_store (ret, new [:path_len], 1)
            
        else:
            if path_len >= 2:
                agg_store (ret, new [:path_len], (found + new [path_len]))
            else:
                agg_store (ret, new [:path_len], (found + 1))
            
        

    return ret


def agg_rows_range (tuple_matches, agg_or_ls):
    if isinstance (agg_or_ls, list):
        agg = agg_or_ls [0]
    else:
        agg = agg_or_ls
    
    tuple_list = agg_to_tuple_list (agg)
    ret = Aggregation (agg.schema, agg.agg, agg.base, agg.min_mag, agg.max_mag, agg.step)
    for e in tuple_list:
        tlen = len (e)
        plen = (tlen - 1)
        for matches in tuple_matches:
            all_match = True
            col = 0
            for m in matches:
                col_match = m.match (e [col])
                all_match = (all_match and col_match)
                col = (col + 1)

            if all_match == True:
                agg_store (ret, e [:plen], e [plen])
                break
            


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
        
    
    return agg


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
    morph.addVariable ("trader-demographics", [const_power_of_2_trader_distribution_id])
    morph.addVariable ("swing-traders", [const_pow_2_swing_trader])
    morph.addVariable ("position-traders", [const_pow_2_position_trader])
    morph.addVariable ("investors", [const_pow_2_investor])
    morph.addVariable ("hodlers", [const_pow_2_hodler])
    morph.addVariable ("base-heuristic-cost", [4000])
    morph.addVariable ("max-users", [1000000, 100000000])
    morph.addVariable ("data-value", [0.1, 0.6])
    morph.addVariable ("vesting-ratio", [0.1, 0.2, 0.5])
    morph.addVariable ("token-reward-sellers", [0.5, 0.1, 0.9])
    morph.addVariable ("max-growth", [1.05, 1.1, 1.15, 1.2])
    morph.addVariable ("base-yield", [1.01])
    morph.addVariable ("heuristic-innovation-scenario", [const_industrialized, const_leading, const_holding, const_lagging, const_terminal])
    morph.addVariable ("anchor", [const_anchor])
    morph.addVariable ("what-if", [const_base_what_if, const_best_case_greedy, const_best_case_generous, const_best_case_x, const_worst_case_greedy, const_worst_case_generous])
    morph.addVariable ("token-valuation", [const_tenth_value, const_half_value])
    morph.addVariable ("supply-perception", [const_supply_expanding, const_supply_filling])
    morph.addVariable ("expectation-chain", [const_observed_expectation_chain_id])
    morph.addVariable ("money-growth", [const_observed_money_growth_id])
    morph.addVariable ("minimum-trade-profit", [0.01, 0.05, 0.1, 0.15, 0.2])
    morph.addVariable ("free-loaders", [0.1, 0.2, 0.5, 0.8, 0.9])
    morph.addVariable ("security-users", [0.1, 0.2, 0.5, 0.8, 0.9])
    morph.addVariable ("token-price-delta-change-reward-amount", [0])
    morph.addVariable ("user-goal-progress-change-reward-amount", [0])
    morph.addVariable ("anti-user-goal-progress-change-reward-amount", [0])
    morph.addVariable ("token-price-delta-change-buyback-amount", [0])
    morph.addVariable ("user-goal-progress-change-buyback-amount", [0])
    morph.addVariable ("anti-user-goal-progress-change-buyback-amount", [0])
    morph.addVariable ("token-price-delta-change-user-fee", [0])
    morph.addVariable ("user-goal-progress-change-user-fee", [0])
    morph.addVariable ("anti-user-goal-progress-change-user-fee", [0])
    morph.addVariable ("token-price-delta-change-lookup-fee", [0])
    morph.addVariable ("user-goal-progress-change-lookup-fee", [0])
    morph.addVariable ("anti-user-goal-progress-change-lookup-fee", [0])
    morph.addVariable ("token-price-delta-change-stake-yield", [0])
    morph.addVariable ("user-goal-progress-change-stake-yield", [0])
    morph.addVariable ("anti-user-goal-progress-change-stake-yield", [0])
    morph.addVariable ("token-price-delta-change-max-stake", [0])
    morph.addVariable ("user-goal-progress-change-max-stake", [0])
    morph.addVariable ("anti-user-goal-progress-change-max-stake", [0])
    morph.addConstraint (what_if_contradicts_security_users, ("what-if", "security-users"))
    morph.addConstraint (what_if_contradicts_free_loaders, ("what-if", "free-loaders"))
    morph.addConstraint (what_if_contradicts_minimum_trade_profit, ("what-if", "minimum-trade-profit"))
    morph.addConstraint (what_if_contradicts_supply_perception, ("what-if", "supply-perception"))
    morph.addConstraint (what_if_contradicts_token_valuation, ("what-if", "token-valuation"))
    morph.addConstraint (what_if_contradicts_heuristic_innovation_scenario, ("what-if", "heuristic-innovation-scenario"))
    morph.addConstraint (anchor_contradicts_what_if, ("anchor", "what-if"))
    morph.addConstraint (what_if_contradicts_max_growth, ("what-if", "max-growth"))
    morph.addConstraint (what_if_contradicts_token_reward_sellers, ("what-if", "token-reward-sellers"))
    morph.addConstraint (what_if_contradicts_vesting_ratio, ("what-if", "vesting-ratio"))
    morph.addConstraint (what_if_contradicts_data_value, ("what-if", "data-value"))
    morph.addConstraint (what_if_contradicts_max_users, ("what-if", "max-users"))
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


def neg_ls (ls):
    if len (ls) == 0:
        return []
    
    ret_ls = []
    for n in ls:
        ret_ls.append (-n)

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


def agg_zeroize (agg_or_ls):
    if isinstance (agg_or_ls, list):
        agg = agg_or_ls [0]
    else:
        agg = agg_or_ls
    
    ret = Aggregation (agg.schema, agg.agg, agg.base, agg.min_mag, agg.max_mag, agg.step)
    return ret


def set_diff_agg (agg_or_ls, agg2_or_ls):
    if isinstance (agg_or_ls, list):
        agg = agg_or_ls [0]
    else:
        agg = agg_or_ls
    
    if isinstance (agg2_or_ls, list):
        agg2 = agg2_or_ls [0]
    else:
        agg2 = agg2_or_ls
    
    ret = Aggregation (agg.schema, agg.agg, agg.base, agg.min_mag, agg.max_mag, agg.step)
    max_depth = len (agg.schema)
    def insert_if_unique (tup):
        tlen = len (tup)
        plen = (tlen - 1)
        found = agg_load (agg2, tup [:plen])
        if found == None:
            agg_store (ret, tup [:plen], tup [plen])
        


    agg.agg_dict_walk (agg.root, insert_if_unique, max_depth, ())
    return ret


def set_diff_agg_eq (agg_or_ls, agg2_or_ls):
    if isinstance (agg_or_ls, list):
        agg = agg_or_ls [0]
    else:
        agg = agg_or_ls
    
    if isinstance (agg2_or_ls, list):
        agg2 = agg2_or_ls [0]
    else:
        agg2 = agg2_or_ls
    
    ret = Aggregation (agg.schema, agg.agg, agg.base, agg.min_mag, agg.max_mag, agg.step)
    max_depth = len (agg.schema)
    def insert_if_unique (tuple):
        tlen = len (tuple)
        plen = (tlen - 1)
        found = agg_load (agg2, tup [:plen])
        if found == None:
            agg_store (ret, tup [:plen], tup [plen])
        elif found == tup [plen]:
            agg_store (ret, tup [:plen], tup [plen])
        


    agg.agg_dict_walk (agg.root, insert_if_unique, max_depth, ())
    return ret


def arith_diff_agg (agg_or_ls, agg2_or_ls):
    if isinstance (agg_or_ls, list):
        agg = agg_or_ls [0]
    else:
        agg = agg_or_ls
    
    if isinstance (agg2_or_ls, list):
        agg2 = agg2_or_ls [0]
    else:
        agg2 = agg2_or_ls
    
    ret = Aggregation (agg.schema, agg.agg, agg.base, agg.min_mag, agg.max_mag, agg.step)
    return ret


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
                ret_val = (ret_val / 0.999)
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


def exp_ls (ls):
    if len (ls) == 0:
        return []
    elif len (ls) == 1:
        return ls
    
    ret_val = 1
    first = 1
    for n in ls:
        if first == 1:
            if n == 0:
                return [0]
            elif n == 1:
                return [1]
            else:
                first = 0
                ret_val = n
            
        elif first == 0:
            if n == 0:
                return [1]
            else:
                ret_val = (ret_val ** n)
            
        

    return [ret_val]


def abs_ls (ls):
    if len (ls) == 0:
        return []
    
    ret_val = 1
    first = 1
    ret_ls = []
    for n in ls:
        ret_ls.append (abs (n))

    return ret_ls


def lg_ls (ls):
    if len (ls) == 0:
        return []
    elif len (ls) == 1:
        return ls
    
    ret_val = 1
    first = 1
    for n in ls:
        if first == 1:
            if n == 0:
                return [0]
            elif n == 1:
                return [1]
            else:
                first = 0
                ret_val = n
            
        elif first == 0:
            if n == 0:
                return [1]
            else:
                ret_val = (ret_val ** n)
            
        

    return [ret_val]


def ln_ls (ls):
    if len (ls) == 0:
        return []
    elif len (ls) == 1:
        return ls
    
    ret_val = 1
    first = 1
    for n in ls:
        if first == 1:
            if n == 0:
                return [0]
            elif n == 1:
                return [1]
            else:
                first = 0
                ret_val = n
            
        elif first == 0:
            if n == 0:
                return [1]
            else:
                ret_val = (ret_val ** n)
            
        

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


def sim_random (a, b, run):
    global sim_rng
    if sim_rng == None:
        sim_rng = np.random.default_rng ((124215432 + (run - 1)))
    
    return sim_rng.integers (a, (b + 1))


def append_each (target, values):
    if isinstance (values, Aggregation):
        target.append (values)
    else:
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


def run_diff (r1, r2):
    p1 = sim_cfg [(r1 - 1)] ["M"]
    p2 = sim_cfg [(r2 - 1)] ["M"]
    s1 = set (p1.items ())
    s2 = set (p2.items ())
    return dict ((s1 - s2)), dict ((s2 - s1))


def run_spec (r1):
    p1 = sim_cfg [(r1 - 1)] ["M"]
    return p1


def plot_lines (data, x_vars, y_vars):
    fig = px.line (data, x=x_vars, y=y_vars, facet_col='run', facet_col_wrap=3, height=8000, facet_row_spacing=0.006, template='seaborn')
    fig.update_layout (margin=dict(l=20, r=20, t=20, b=20),)
    return fig


def plot_log_lines (data, x_vars, y_vars):
    fig = px.line (data, x=x_vars, y=y_vars, log_y=True, facet_col='run', facet_col_wrap=3, height=8000, facet_row_spacing=0.006, template='seaborn')
    fig.update_layout (margin=dict(l=20, r=20, t=20, b=20),)
    return fig


def plot_hist (data, var):
    fig = px.histogram (data, x=var, facet_col='run', facet_col_wrap=3, height=8000, facet_row_spacing=0.006, template='seaborn')
    fig.update_layout (margin=dict(l=20, r=20, t=20, b=20),)
    return fig


def adjust_all_flows (_params, substep, sH, s, _input, **kwargs):
    flow_adjustments = {}
    s_adjust_scam_profits_outflow (s, flow_adjustments)
    s_adjust_potential_scam_profits_outflow (s, flow_adjustments)
    s_adjust_scam_page_visits_outflow (s, flow_adjustments)
    s_adjust_page_visits_outflow (s, flow_adjustments)
    s_adjust_potential_page_visits_outflow (s, flow_adjustments)
    s_adjust_airlock_revenue_outflow (s, flow_adjustments)
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


const_growth_1 = 1
const_growth_2 = 1.05
const_growth_3 = 1.1
const_growth_4 = 1.15
const_growth_5 = 1.2
const_power_of_2_trader_distribution_id = 2
const_pow_2_swing_trader = 0.5
const_pow_2_position_trader = 0.25
const_pow_2_investor = 0.125
const_pow_2_hodler = 0.125
const_day_trader = 1
const_swing_trader = 2
const_position_trader = 3
const_diversified_investor = 4
const_hodler = 5
const_power_of_2_trader_distribution = agg_store_records (Aggregation (["type"], "count"), [[[const_day_trader], 8], [[const_swing_trader], 4], [[const_position_trader], 2], [[const_diversified_investor], 1], [[const_hodler], 1]])
const_anchor = 0
const_base_what_if = 0
const_best_case_greedy = 1
const_best_case_generous = 2
const_worst_case_greedy = 3
const_worst_case_generous = 4
const_best_case_x = 5
const_industrialized = 2
const_leading = 1
const_holding = 0
const_lagging = -1
const_terminal = -2
const_no = 0
const_yes = 1
const_half_value = 0.5
const_tenth_value = 0.1
const_firehose = 1
const_trickle = 0.1
const_halted = 0
const_supply_expanding = 1
const_supply_filling = 0
const_halving = -1
const_egalitarian = 0
const_doubling = 1
const_bigdip = -2
const_dip = -1
const_stag = 0
const_up = 1
const_bigup = 2
const_at_market = 1
const_below_market = 0.8
const_above_market = 1.03
const_at_cost = 1
const_below_cost = 0.7
const_above_cost = 1.3
const_price_movement = agg_store_records (Aggregation (["sell", "buy", "mul"], "count"), [[1, -1, 0.8, 1], [0, -1, 0.9, 1], [1, 0, 0.9, 1], [1, 1, 1.0, 1], [-1, -1, 1.0, 1], [0, 0, 1.0, 1], [0, 1, 1.1, 1], [-1, 0, 1.1, 1], [-1, 1, 1.2, 1]])
const_observed_money_growth = agg_store_records (Aggregation (["mult"], "count"), [[0.988, 1], [0.991, 2], [0.992, 2], [0.993, 5], [0.994, 7], [0.995, 10], [0.997, 38], [0.998, 80], [0.999, 124], [1.0, 145], [1.001, 127], [1.002, 105], [1.003, 68], [1.004, 35], [1.005, 27], [1.006, 29], [1.007, 12], [1.008, 4], [1.009, 2], [1.01, 3], [1.017, 1]])
const_observed_expectation_chain_id = 0
const_observed_money_growth_id = 0
const_invest_movement = agg_store_records (Aggregation (["move", "mul"], "sum"), [[[const_bigdip], 0.8], [[const_dip], 0.9], [[const_stag], 1], [[const_up], 1.1], [[const_bigup], 1.2]])
const_observed_expectation_chain = agg_store_records (Aggregation (["in", "out"], "count"), [[[const_bigdip], [const_bigup], 1], [[const_bigdip], [const_dip], 1], [[const_bigdip], [const_up], 6], [[const_dip], [const_bigup], 1], [[const_dip], [const_bigdip], 6], [[const_dip], [const_dip], 7], [[const_dip], [const_up], 10], [[const_stag], [const_bigup], 1], [[const_stag], [const_stag], 1], [[const_stag], [const_dip], 3], [[const_up], [const_bigdip], 2], [[const_up], [const_stag], 3], [[const_up], [const_bigup], 5], [[const_up], [const_dip], 9], [[const_up], [const_up], 11], [[const_bigup], [const_stag], 1], [[const_bigup], [const_up], 4], [[const_bigup], [const_dip], 4], [[const_bigup], [const_bigup], 5]])
const_buy = 0
const_sell = 1
const_growth_spread = agg_store_records (Aggregation (["rate"], "count"), [[1.05, 16], [1.1, 8], [1.15, 4], [1.2, 1]])
def s_update_hodler_order_book (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_token_hold_rate_updates_hodler_order_book (ctx, s, _params)
    s_clock_updates_hodler_order_book (ctx, s, _params)
    s_token_price_updates_hodler_order_book (ctx, s, _params)
    myself = "hodler-order-book"
    hodler_order_book = aggregate (get_new_value (s, "hodler-order-book"), [ctx.get ("buy-price"), ctx.get ("sell-time"), ctx.get ("quantity")])
    return "hodler-order-book", update_state (s, "hodler-order-book", hodler_order_book)


def s_update_investor_order_book (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_investor_order_book_updates_investor_order_book (ctx, s, _params)
    s_token_hold_rate_updates_investor_order_book (ctx, s, _params)
    s_clock_updates_investor_order_book (ctx, s, _params)
    s_token_price_updates_investor_order_book (ctx, s, _params)
    myself = "investor-order-book"
    investor_order_book = aggregate (set_diff_agg (get_new_value (s, "investor-order-book"), ctx.get ("removable")), [ctx.get ("buy-price"), ctx.get ("sell-time"), ctx.get ("quantity")])
    return "investor-order-book", update_state (s, "investor-order-book", investor_order_book)


def s_update_position_order_book (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_position_order_book_updates_position_order_book (ctx, s, _params)
    s_token_hold_rate_updates_position_order_book (ctx, s, _params)
    s_clock_updates_position_order_book (ctx, s, _params)
    s_token_price_updates_position_order_book (ctx, s, _params)
    myself = "position-order-book"
    position_order_book = aggregate (set_diff_agg (get_new_value (s, "position-order-book"), ctx.get ("removable")), [ctx.get ("buy-price"), ctx.get ("sell-time"), ctx.get ("quantity")])
    return "position-order-book", update_state (s, "position-order-book", position_order_book)


def s_update_swing_order_book (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_swing_order_book_updates_swing_order_book (ctx, s, _params)
    s_token_hold_rate_updates_swing_order_book (ctx, s, _params)
    s_clock_updates_swing_order_book (ctx, s, _params)
    s_token_price_updates_swing_order_book (ctx, s, _params)
    myself = "swing-order-book"
    swing_order_book = aggregate (set_diff_agg (get_new_value (s, "swing-order-book"), ctx.get ("removable")), [ctx.get ("buy-price"), ctx.get ("sell-time"), ctx.get ("quantity")])
    return "swing-order-book", update_state (s, "swing-order-book", swing_order_book)


def s_update_token_price_delta (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_token_price_updates_token_price_delta (ctx, s, _params)
    myself = "token-price-delta"
    token_price_delta = min_ls ([1] + max_ls ([-1] + ctx.get ("stim")))
    return "token-price-delta", update_state (s, "token-price-delta", token_price_delta)


def s_update_change_reward_amount (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_anti_user_goal_progress_updates_change_reward_amount (ctx, s, _params)
    s_user_goal_progress_updates_change_reward_amount (ctx, s, _params)
    s_token_price_delta_updates_change_reward_amount (ctx, s, _params)
    myself = "change-reward-amount"
    change_reward_amount = min_ls ([100] + max_ls ([-100] + ctx.get ("points")))
    return "change-reward-amount", update_state (s, "change-reward-amount", change_reward_amount)


def s_update_change_buyback_amount (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_anti_user_goal_progress_updates_change_buyback_amount (ctx, s, _params)
    s_user_goal_progress_updates_change_buyback_amount (ctx, s, _params)
    s_token_price_delta_updates_change_buyback_amount (ctx, s, _params)
    myself = "change-buyback-amount"
    change_buyback_amount = min_ls ([100] + max_ls ([-100] + ctx.get ("points")))
    return "change-buyback-amount", update_state (s, "change-buyback-amount", change_buyback_amount)


def s_update_change_user_fee (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_anti_user_goal_progress_updates_change_user_fee (ctx, s, _params)
    s_user_goal_progress_updates_change_user_fee (ctx, s, _params)
    s_token_price_delta_updates_change_user_fee (ctx, s, _params)
    myself = "change-user-fee"
    change_user_fee = min_ls ([100] + max_ls ([-100] + ctx.get ("points")))
    return "change-user-fee", update_state (s, "change-user-fee", change_user_fee)


def s_update_change_lookup_fee (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_anti_user_goal_progress_updates_change_lookup_fee (ctx, s, _params)
    s_user_goal_progress_updates_change_lookup_fee (ctx, s, _params)
    s_token_price_delta_updates_change_lookup_fee (ctx, s, _params)
    myself = "change-lookup-fee"
    change_lookup_fee = min_ls ([100] + max_ls ([-100] + ctx.get ("points")))
    return "change-lookup-fee", update_state (s, "change-lookup-fee", change_lookup_fee)


def s_update_change_stake_yield (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_token_price_delta_updates_change_stake_yield (ctx, s, _params)
    s_user_goal_progress_updates_change_stake_yield (ctx, s, _params)
    s_anti_user_goal_progress_updates_change_stake_yield (ctx, s, _params)
    myself = "change-stake-yield"
    change_stake_yield = min_ls ([100] + max_ls ([-100] + ctx.get ("points")))
    return "change-stake-yield", update_state (s, "change-stake-yield", change_stake_yield)


def s_update_change_max_stake (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_user_goal_progress_updates_change_max_stake (ctx, s, _params)
    s_token_price_delta_updates_change_max_stake (ctx, s, _params)
    s_anti_user_goal_progress_updates_change_max_stake (ctx, s, _params)
    myself = "change-max-stake"
    change_max_stake = min_ls ([100] + max_ls ([-100] + ctx.get ("points")))
    return "change-max-stake", update_state (s, "change-max-stake", change_max_stake)


def s_update_fitness (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_token_price_updates_fitness (ctx, s, _params)
    s_scam_page_successes_updates_fitness (ctx, s, _params)
    myself = "fitness"
    fitness = min_ls ([1000000000] + max_ls ([0] + div_ls ([1] + ctx.get ("price"))))
    return "fitness", update_state (s, "fitness", fitness)


def s_update_growth_level (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_reward_rate_updates_growth_level (ctx, s, _params)
    myself = "growth-level"
    growth_level = min_ls ([1.25] + max_ls ([1] + sum_ls (agg_choose ([const_growth_spread], [0], s ["run"], []) + [0.05]) if lt_ls (get_new_value (s, "growth-level") + [_params ["max-growth"]]) [0] else get_new_value (s, "growth-level") if gt_ls (ctx.get ("reward-rate-delta") + [0]) [0] else diff_ls (agg_choose ([const_growth_spread], [0], s ["run"], []) + [0.05]) if gt_ls (get_new_value (s, "growth-level") + [1]) [0] else get_new_value (s, "growth-level")))
    return "growth-level", update_state (s, "growth-level", growth_level)


def s_update_reward_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_token_price_updates_reward_rate (ctx, s, _params)
    s_token_reward_to_held_rate_updates_reward_rate (ctx, s, _params)
    s_token_reward_to_sell_rate_updates_reward_rate (ctx, s, _params)
    myself = "reward-rate"
    reward_rate = min_ls ([1000000000] + max_ls ([0] + mul_ls (ctx.get ("price") + div_ls (sum_ls (ctx.get ("rewards-sold") + ctx.get ("rewards-held")) + [2]))))
    return "reward-rate", update_state (s, "reward-rate", reward_rate)


def s_update_heuristic_innovation (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_heuristic_contradictions_updates_heuristic_innovation (ctx, s, _params)
    myself = "heuristic-innovation"
    heuristic_innovation = min_ls ([1] + max_ls ([0] + ctx.get ("urgency")))
    return "heuristic-innovation", update_state (s, "heuristic-innovation", heuristic_innovation)


def s_update_scammer_innovation (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_scam_page_success_rate_updates_scammer_innovation (ctx, s, _params)
    myself = "scammer-innovation"
    scammer_innovation = min_ls ([1] + max_ls ([0] + ctx.get ("urgency")))
    return "scammer-innovation", update_state (s, "scammer-innovation", scammer_innovation)


def s_update_scam_profits_per_page (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    myself = "scam-profits-per-page"
    scam_profits_per_page = min_ls ([100] + max_ls ([1] + [sim_random (1, 100, s ["run"])]))
    return "scam-profits-per-page", update_state (s, "scam-profits-per-page", scam_profits_per_page)


def s_update_stake_yield (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_change_stake_yield_updates_stake_yield (ctx, s, _params)
    myself = "stake-yield"
    stake_yield = min_ls ([100] + max_ls ([1.001] + mul_ls (ctx.get ("mul-stake-yield") + [_params ["base-yield"]])))
    return "stake-yield", update_state (s, "stake-yield", stake_yield)


def s_update_max_stake (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_change_max_stake_updates_max_stake (ctx, s, _params)
    myself = "max-stake"
    max_stake = min_ls ([500] + max_ls ([0] + ctx.get ("mul-max-stake")))
    return "max-stake", update_state (s, "max-stake", max_stake)


def s_update_user_goal_progress (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_airlock_users_updates_user_goal_progress (ctx, s, _params)
    myself = "user-goal-progress"
    user_goal_progress = min_ls ([1] + max_ls ([-1] + ctx.get ("stim")))
    return "user-goal-progress", update_state (s, "user-goal-progress", user_goal_progress)


def s_update_staking_opportunities (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_grey_area_entities_updates_staking_opportunities (ctx, s, _params)
    myself = "staking-opportunities"
    staking_opportunities = min_ls ([3000000000000] + max_ls ([0] + ctx.get ("grey-stake")))
    return "staking-opportunities", update_state (s, "staking-opportunities", staking_opportunities)


def s_update_heuristic_contradictions (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_heuristics_updates_heuristic_contradictions (ctx, s, _params)
    s_anti_heuristics_updates_heuristic_contradictions (ctx, s, _params)
    myself = "heuristic-contradictions"
    heuristic_contradictions = min_ls ([1] + max_ls ([0] + div_ls (ctx.get ("anti") + ctx.get ("heur"))))
    return "heuristic-contradictions", update_state (s, "heuristic-contradictions", heuristic_contradictions)


def s_update_anti_heuristics (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_scammer_innovation_updates_anti_heuristics (ctx, s, _params)
    myself = "anti-heuristics"
    anti_heuristics = min_ls ([100] + max_ls ([1] + sum_ls (get_new_value (s, myself) + ctx.get ("innovation"))))
    return "anti-heuristics", update_state (s, "anti-heuristics", anti_heuristics)


def s_update_heuristics (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_heuristic_innovation_updates_heuristics (ctx, s, _params)
    myself = "heuristics"
    heuristics = min_ls ([100] + max_ls ([1] + sum_ls (get_new_value (s, myself) + ctx.get ("innovation"))))
    return "heuristics", update_state (s, "heuristics", heuristics)


def s_update_anti_user_goal_progress (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_airlock_users_updates_anti_user_goal_progress (ctx, s, _params)
    myself = "anti-user-goal-progress"
    anti_user_goal_progress = min_ls ([1] + max_ls ([-1] + ctx.get ("stim")))
    return "anti-user-goal-progress", update_state (s, "anti-user-goal-progress", anti_user_goal_progress)


def s_update_staking_enthusiasm (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_crypto_hype_updates_staking_enthusiasm (ctx, s, _params)
    myself = "staking-enthusiasm"
    staking_enthusiasm = min_ls ([100] + max_ls ([1] + mul_ls (ctx.get ("expectation-multiplier") + div_ls ([sim_random (5, 25, s ["run"])] + [100]))))
    return "staking-enthusiasm", update_state (s, "staking-enthusiasm", staking_enthusiasm)


def s_update_money_growth_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    myself = "money-growth-rate"
    money_growth_rate = min_ls (div_ls ([1017] + [1000]) + max_ls (div_ls ([988] + [1000]) + agg_choose ([const_observed_money_growth] if eq_ls ([_params ["money-growth"]] + [const_observed_money_growth_id]) [0] else [-999], [0], s ["run"], [])))
    return "money-growth-rate", update_state (s, "money-growth-rate", money_growth_rate)


def s_update_interlock_hype (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_crypto_hype_updates_interlock_hype (ctx, s, _params)
    myself = "interlock-hype"
    interlock_hype = min_ls ([2] + max_ls ([-2] + ctx.get ("crypto-hype")))
    return "interlock-hype", update_state (s, "interlock-hype", interlock_hype)


def s_update_token_profit (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_token_price_updates_token_profit (ctx, s, _params)
    myself = "token-profit"
    token_profit = ctx.get ("price-delta-pct")
    return "token-profit", update_state (s, "token-profit", token_profit)


def s_update_airlock_lookup_price (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_airlock_users_updates_airlock_lookup_price (ctx, s, _params)
    s_token_price_updates_airlock_lookup_price (ctx, s, _params)
    s_change_lookup_fee_updates_airlock_lookup_price (ctx, s, _params)
    s_change_user_fee_updates_airlock_lookup_price (ctx, s, _params)
    s_airlock_lookup_rate_updates_airlock_lookup_price (ctx, s, _params)
    s_airlock_expenses_updates_airlock_lookup_price (ctx, s, _params)
    myself = "airlock-lookup-price"
    airlock_lookup_price = min_ls ([5] + max_ls ([0] + div_ls (sum_ls (mul_ls (min_ls (div_ls (mul_ls (ctx.get ("expenses") + ctx.get ("mul-lookup-fee")) + ctx.get ("users")) + ctx.get ("mul-user-fee")) + ctx.get ("users")) + mul_ls (ctx.get ("lookups") + ctx.get ("mul-lookup-fee"))) + [1])))
    return "airlock-lookup-price", update_state (s, "airlock-lookup-price", airlock_lookup_price)


def s_update_airlock_expenses (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_heuristic_innovation_updates_airlock_expenses (ctx, s, _params)
    myself = "airlock-expenses"
    airlock_expenses = min_ls ([1000000] + max_ls ([1] + sum_ls (get_new_value (s, "airlock-expenses") + ctx.get ("profit-diverted-to-innovate"))))
    return "airlock-expenses", update_state (s, "airlock-expenses", airlock_expenses)


def s_update_token_price (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_token_sell_pool_updates_token_price (ctx, s, _params)
    s_intr_investments_updates_token_price (ctx, s, _params)
    myself = "token-price"
    token_price = min_ls ([60] + max_ls ([0.01] + div_ls (ctx.get ("invest-pool") + ctx.get ("sell-pool"))))
    return "token-price", update_state (s, "token-price", token_price)


def s_update_avg_token_value (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_token_hold_pool_updates_avg_token_value (ctx, s, _params)
    s_intr_investments_updates_avg_token_value (ctx, s, _params)
    myself = "avg-token-value"
    avg_token_value = min_ls ([500000] + max_ls ([1] + div_ls (ctx.get ("invested") + ctx.get ("held"))))
    return "avg-token-value", update_state (s, "avg-token-value", avg_token_value)


def s_update_crypto_hype (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_money_supply_updates_crypto_hype (ctx, s, _params)
    myself = "crypto-hype"
    crypto_hype = min_ls ([2] + max_ls ([-2] + agg_choose (agg_cols ([[1], [2]], agg_rows ([[get_new_value (s, "crypto-hype")]], [const_observed_expectation_chain] if eq_ls ([_params ["expectation-chain"]] + [const_observed_expectation_chain_id]) [0] else [-999])), [0], s ["run"], [])))
    return "crypto-hype", update_state (s, "crypto-hype", crypto_hype)


def s_update_clock (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    myself = "clock"
    clock = min_ls ([1000000] + max_ls ([0] + sum_ls ([1] + get_new_value (s, "clock"))))
    return "clock", update_state (s, "clock", clock)


def s_update_scam_upkeep_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_scammer_innovation_updates_scam_upkeep_rate (ctx, s, _params)
    myself = "scam-upkeep-rate"
    scam_upkeep_rate = mul_ls (get_new_value (s, "scam-profits") + [1.01] + ctx.get ("profit-diverted-to-innovate"))
    return "scam-upkeep-rate", update_state (s, "scam-upkeep-rate", scam_upkeep_rate)


def s_update_scam_profit_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_scam_profits_per_page_updates_scam_profit_rate (ctx, s, _params)
    s_scam_page_successes_updates_scam_profit_rate (ctx, s, _params)
    myself = "scam-profit-rate"
    scam_profit_rate = mul_ls (ctx.get ("total-pages") + ctx.get ("cash-per-page"))
    return "scam-profit-rate", update_state (s, "scam-profit-rate", scam_profit_rate)


def s_update_scam_page_success_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_airlock_users_updates_scam_page_success_rate (ctx, s, _params)
    s_heuristic_contradictions_updates_scam_page_success_rate (ctx, s, _params)
    myself = "scam-page-success-rate"
    scam_page_success_rate = diff_ls (mul_ls ([0.4] + get_new_value (s, "scam-page-visits")) + mul_ls ([0.4] + get_new_value (s, "scam-page-visits") + mul_ls (ctx.get ("pass-through") + ctx.get ("user-share"))))
    return "scam-page-success-rate", update_state (s, "scam-page-success-rate", scam_page_success_rate)


def s_update_scam_page_visit_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    myself = "scam-page-visit-rate"
    scam_page_visit_rate = mul_ls ([1] + [1000000])
    return "scam-page-visit-rate", update_state (s, "scam-page-visit-rate", scam_page_visit_rate)


def s_update_page_visit_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    myself = "page-visit-rate"
    page_visit_rate = mul_ls ([100] + [1000000])
    return "page-visit-rate", update_state (s, "page-visit-rate", page_visit_rate)


def s_update_airlock_upkeep_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_airlock_expenses_updates_airlock_upkeep_rate (ctx, s, _params)
    myself = "airlock-upkeep-rate"
    airlock_upkeep_rate = ctx.get ("expenses")
    return "airlock-upkeep-rate", update_state (s, "airlock-upkeep-rate", airlock_upkeep_rate)


def s_update_airlock_revenue_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    myself = "airlock-revenue-rate"
    airlock_revenue_rate = mul_ls ([_params ["data-value"]] + diff_ls (get_new_value (s, "airlock-data-shared") + get_old_value (s, "airlock-data-shared")))
    return "airlock-revenue-rate", update_state (s, "airlock-revenue-rate", airlock_revenue_rate)


def s_update_airlock_share_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_airlock_lookup_price_updates_airlock_share_rate (ctx, s, _params)
    s_airlock_users_updates_airlock_share_rate (ctx, s, _params)
    myself = "airlock-share-rate"
    airlock_share_rate = mul_ls (mul_ls (ctx.get ("user-share") + get_new_value (s, "browsing-data")) + diff_ls ([1] + [_params ["free-loaders"]]) if gt_ls (ctx.get ("lookup-price") + [0]) [0] else [1])
    return "airlock-share-rate", update_state (s, "airlock-share-rate", airlock_share_rate)


def s_update_resolution_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    myself = "resolution-rate"
    resolution_rate = get_old_value (s, "grey-area-entity-rate")
    return "resolution-rate", update_state (s, "resolution-rate", resolution_rate)


def s_update_grey_area_entity_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_heuristic_contradictions_updates_grey_area_entity_rate (ctx, s, _params)
    myself = "grey-area-entity-rate"
    grey_area_entity_rate = mul_ls (get_new_value (s, "airlock-lookups") + ctx.get ("contradictions"))
    return "grey-area-entity-rate", update_state (s, "grey-area-entity-rate", grey_area_entity_rate)


def s_update_airlock_lookup_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_airlock_users_updates_airlock_lookup_rate (ctx, s, _params)
    s_page_visit_rate_updates_airlock_lookup_rate (ctx, s, _params)
    myself = "airlock-lookup-rate"
    airlock_lookup_rate = mul_ls (ctx.get ("pages-visited") + ctx.get ("user-share") + [2])
    return "airlock-lookup-rate", update_state (s, "airlock-lookup-rate", airlock_lookup_rate)


def s_update_airlock_abandonment_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_token_reward_to_held_rate_updates_airlock_abandonment_rate (ctx, s, _params)
    s_token_reward_to_sell_rate_updates_airlock_abandonment_rate (ctx, s, _params)
    s_heuristic_contradictions_updates_airlock_abandonment_rate (ctx, s, _params)
    myself = "airlock-abandonment-rate"
    airlock_abandonment_rate = ctx.get ("contradiction-delta")
    return "airlock-abandonment-rate", update_state (s, "airlock-abandonment-rate", airlock_abandonment_rate)


def s_update_airlock_adoption_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_airlock_users_updates_airlock_adoption_rate (ctx, s, _params)
    s_growth_level_updates_airlock_adoption_rate (ctx, s, _params)
    s_interlock_hype_updates_airlock_adoption_rate (ctx, s, _params)
    myself = "airlock-adoption-rate"
    airlock_adoption_rate = mul_ls (max_ls ([20] + diff_ls (mul_ls (ctx.get ("users") + ctx.get ("growth")) + ctx.get ("users"))) if lt_ls (get_new_value (s, "airlock-users") + [_params ["max-users"]]) [0] else [0])
    return "airlock-adoption-rate", update_state (s, "airlock-adoption-rate", airlock_adoption_rate)


def s_update_intr_divest_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_crypto_hype_updates_intr_divest_rate (ctx, s, _params)
    s_token_profit_updates_intr_divest_rate (ctx, s, _params)
    myself = "intr-divest-rate"
    intr_divest_rate = mul_ls (ctx.get ("profit-delta-pct") + max_ls ([1] + get_new_value (s, "intr-divest-rate")))
    return "intr-divest-rate", update_state (s, "intr-divest-rate", intr_divest_rate)


def s_update_crypto_divest_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_crypto_hype_updates_crypto_divest_rate (ctx, s, _params)
    myself = "crypto-divest-rate"
    crypto_divest_rate = max_ls ([0] + diff_ls (get_new_value (s, "crypto-investments") + mul_ls (get_new_value (s, "crypto-investments") + agg_to_list (agg_col_to_list (1, agg_rows ([[ctx.get ("crypto-hype")]], [const_invest_movement]))))))
    return "crypto-divest-rate", update_state (s, "crypto-divest-rate", crypto_divest_rate)


def s_update_intr_invest_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_token_price_updates_intr_invest_rate (ctx, s, _params)
    s_airlock_lookup_price_updates_intr_invest_rate (ctx, s, _params)
    s_crypto_hype_updates_intr_invest_rate (ctx, s, _params)
    myself = "intr-invest-rate"
    intr_invest_rate = min_ls (mul_ls ([0.001] + get_new_value (s, "crypto-investments")) + sum_ls (mul_ls (get_new_value (s, "intr-investments") + agg_col_to_list (1, agg_rows ([[ctx.get ("crypto-hype")]], [const_invest_movement])) + [_params ["swing-traders"]]) if lt_eq_ls (ctx.get ("price-delta-pct") + [0.95]) [0] else [0] + mul_ls (get_new_value (s, "intr-investments") + agg_col_to_list (1, agg_rows ([[ctx.get ("crypto-hype")]], [const_invest_movement])) + [_params ["position-traders"]]) if gt_eq_ls (ctx.get ("price-delta-pct") + [1.05]) [0] else [0]))
    return "intr-invest-rate", update_state (s, "intr-invest-rate", intr_invest_rate)


def s_update_crypto_invest_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_crypto_hype_updates_crypto_invest_rate (ctx, s, _params)
    myself = "crypto-invest-rate"
    crypto_invest_rate = max_ls ([0] + min_ls (mul_ls ([0.001] + get_new_value (s, "money-supply")) + diff_ls (mul_ls (get_new_value (s, "crypto-investments") + agg_to_list (agg_col_to_list (1, agg_rows ([[ctx.get ("crypto-hype")]], [const_invest_movement])))) + get_new_value (s, "crypto-investments"))))
    return "crypto-invest-rate", update_state (s, "crypto-invest-rate", crypto_invest_rate)


def s_update_money_mint_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_money_growth_rate_updates_money_mint_rate (ctx, s, _params)
    myself = "money-mint-rate"
    money_mint_rate = diff_ls (mul_ls (get_new_value (s, "money-supply") + ctx.get ("growth")) + get_new_value (s, "money-supply")) if gt_ls (ctx.get ("growth") + [1]) [0] else [0]
    return "money-mint-rate", update_state (s, "money-mint-rate", money_mint_rate)


def s_update_money_reclaim_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_money_growth_rate_updates_money_reclaim_rate (ctx, s, _params)
    myself = "money-reclaim-rate"
    money_reclaim_rate = diff_ls (get_new_value (s, "money-supply") + mul_ls (get_new_value (s, "money-supply") + ctx.get ("growth"))) if lt_ls (ctx.get ("growth") + [1]) [0] else [0]
    return "money-reclaim-rate", update_state (s, "money-reclaim-rate", money_reclaim_rate)


def s_update_token_reward_to_held_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_change_reward_amount_updates_token_reward_to_held_rate (ctx, s, _params)
    s_airlock_data_shared_updates_token_reward_to_held_rate (ctx, s, _params)
    s_stake_yield_updates_token_reward_to_held_rate (ctx, s, _params)
    myself = "token-reward-to-held-rate"
    token_reward_to_held_rate = sum_ls (mul_ls (get_new_value (s, "token-rewards-pool") + diff_ls ([1] + [_params ["token-reward-sellers"]]) + ctx.get ("mul-reward-rate")) + ctx.get ("stake-yield"))
    return "token-reward-to-held-rate", update_state (s, "token-reward-to-held-rate", token_reward_to_held_rate)


def s_update_token_reward_to_sell_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_change_reward_amount_updates_token_reward_to_sell_rate (ctx, s, _params)
    s_airlock_data_shared_updates_token_reward_to_sell_rate (ctx, s, _params)
    myself = "token-reward-to-sell-rate"
    token_reward_to_sell_rate = mul_ls (get_new_value (s, "token-rewards-pool") + [_params ["token-reward-sellers"]] + ctx.get ("mul-reward-rate"))
    return "token-reward-to-sell-rate", update_state (s, "token-reward-to-sell-rate", token_reward_to_sell_rate)


def s_update_token_unstake_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_max_stake_updates_token_unstake_rate (ctx, s, _params)
    s_staking_opportunities_updates_token_unstake_rate (ctx, s, _params)
    s_staking_enthusiasm_updates_token_unstake_rate (ctx, s, _params)
    myself = "token-unstake-rate"
    token_unstake_rate = mul_ls (ctx.get ("enthusiasm") + ctx.get ("staking-ops") + ctx.get ("max-per-entity"))
    return "token-unstake-rate", update_state (s, "token-unstake-rate", token_unstake_rate)


def s_update_token_stake_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_max_stake_updates_token_stake_rate (ctx, s, _params)
    s_staking_opportunities_updates_token_stake_rate (ctx, s, _params)
    s_staking_enthusiasm_updates_token_stake_rate (ctx, s, _params)
    myself = "token-stake-rate"
    token_stake_rate = mul_ls (ctx.get ("enthusiasm") + ctx.get ("staking-ops") + ctx.get ("max-per-entity"))
    return "token-stake-rate", update_state (s, "token-stake-rate", token_stake_rate)


def s_update_token_unhold_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_investor_order_book_updates_token_unhold_rate (ctx, s, _params)
    s_position_order_book_updates_token_unhold_rate (ctx, s, _params)
    s_swing_order_book_updates_token_unhold_rate (ctx, s, _params)
    myself = "token-unhold-rate"
    token_unhold_rate = sum_ls (ctx.get ("quantity") + mul_ls (sum_ls ([833333] + [2701235] + [2666667] + [4166667] + [5555556] + [1666667] + [1041667]) + [_params ["vesting-ratio"]]))
    return "token-unhold-rate", update_state (s, "token-unhold-rate", token_unhold_rate)


def s_update_token_hold_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_change_buyback_amount_updates_token_hold_rate (ctx, s, _params)
    s_airlock_revenue_updates_token_hold_rate (ctx, s, _params)
    s_intr_investments_updates_token_hold_rate (ctx, s, _params)
    myself = "token-hold-rate"
    token_hold_rate = sum_ls (div_ls (ctx.get ("invested") + get_new_value (s, "token-price")) + mul_ls (ctx.get ("revenue-buys") + ctx.get ("mul-buyback-amount")))
    return "token-hold-rate", update_state (s, "token-hold-rate", token_hold_rate)


def s_update_token_mint_reward_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    myself = "token-mint-reward-rate"
    token_mint_reward_rate = mul_ls ([0.489] + div_ls ([27000000] + [4]))
    return "token-mint-reward-rate", update_state (s, "token-mint-reward-rate", token_mint_reward_rate)


def s_update_token_mint_hold_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    myself = "token-mint-hold-rate"
    token_mint_hold_rate = mul_ls ([0.511] + div_ls ([27000000] + [4])) if eq_ls ([_params ["supply-perception"]] + [const_supply_filling]) [0] else [1]
    return "token-mint-hold-rate", update_state (s, "token-mint-hold-rate", token_mint_hold_rate)


def s_update_token_mint_supply_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    myself = "token-mint-supply-rate"
    token_mint_supply_rate = mul_ls ([0.511] + div_ls ([27000000] + [4])) if eq_ls ([_params ["supply-perception"]] + [const_supply_expanding]) [0] else [1]
    return "token-mint-supply-rate", update_state (s, "token-mint-supply-rate", token_mint_supply_rate)


cfg = { "N": 1, "T": range (200), "M": generate_params () }
init_state = {}
init_state ["flow-adjustments"] = {}
init_state ["hodler-order-book"] = initialize_state (Aggregation (["buy-price", "sell-time", "quantity"], "sum"))
init_state ["investor-order-book"] = initialize_state (Aggregation (["buy-price", "sell-time", "quantity"], "sum"))
init_state ["position-order-book"] = initialize_state (Aggregation (["buy-price", "sell-time", "quantity"], "sum"))
init_state ["swing-order-book"] = initialize_state (Aggregation (["buy-price", "sell-time", "quantity"], "sum"))
init_state ["token-price-delta"] = initialize_state (0)
init_state ["change-reward-amount"] = initialize_state (0)
init_state ["change-buyback-amount"] = initialize_state (0)
init_state ["change-user-fee"] = initialize_state (0)
init_state ["change-lookup-fee"] = initialize_state (0)
init_state ["change-stake-yield"] = initialize_state (0)
init_state ["change-max-stake"] = initialize_state (0)
init_state ["fitness"] = initialize_state (0)
init_state ["growth-level"] = initialize_state (1)
init_state ["reward-rate"] = initialize_state (0)
init_state ["heuristic-innovation"] = initialize_state (0)
init_state ["scammer-innovation"] = initialize_state (0)
init_state ["scam-profits-per-page"] = initialize_state (np.median (range (1, 100)))
init_state ["stake-yield"] = initialize_state (1.01)
init_state ["max-stake"] = initialize_state (300)
init_state ["user-goal-progress"] = initialize_state (0)
init_state ["staking-opportunities"] = initialize_state (1)
init_state ["heuristic-contradictions"] = initialize_state (0.01)
init_state ["anti-heuristics"] = initialize_state (1)
init_state ["heuristics"] = initialize_state (5)
init_state ["anti-user-goal-progress"] = initialize_state (0)
init_state ["staking-enthusiasm"] = initialize_state (div_ls ([15] + [100]))
init_state ["money-growth-rate"] = initialize_state (1.0)
init_state ["interlock-hype"] = initialize_state (0)
init_state ["token-profit"] = initialize_state (np.median (range (0, 100)))
init_state ["airlock-lookup-price"] = initialize_state (0)
init_state ["airlock-expenses"] = initialize_state (40229)
init_state ["token-price"] = initialize_state (1.2)
init_state ["avg-token-value"] = initialize_state (1)
init_state ["crypto-hype"] = initialize_state (0)
init_state ["clock"] = initialize_state (0)
init_state ["scam-upkeep"] = initialize_state (0)
init_state ["scam-profits"] = initialize_state (0)
init_state ["potential-scam-profits"] = initialize_state (20000000000)
init_state ["scam-page-successes"] = initialize_state (0)
init_state ["scam-page-visits"] = initialize_state (0)
init_state ["resolved-entities"] = initialize_state (0)
init_state ["grey-area-entities"] = initialize_state (0)
init_state ["airlock-users"] = initialize_state (1000)
init_state ["browser-users"] = initialize_state (3000000000)
init_state ["data-buyer-money"] = initialize_state (300000000000)
init_state ["airlock-upkeep"] = initialize_state (0)
init_state ["airlock-revenue"] = initialize_state (0)
init_state ["airlock-data-shared"] = initialize_state (0)
init_state ["browsing-data"] = initialize_state (3000000000)
init_state ["potential-airlock-lookups"] = initialize_state (3000000000000)
init_state ["airlock-lookups"] = initialize_state (0)
init_state ["page-visits"] = initialize_state (mul_ls ([100] + [1000000]))
init_state ["potential-page-visits"] = initialize_state (3000000000000)
init_state ["intr-investments"] = initialize_state (50000000)
init_state ["crypto-investments"] = initialize_state (18000000000)
init_state ["money-reclaimed"] = initialize_state (0)
init_state ["money-supply"] = initialize_state (1000000000000)
init_state ["money-mint"] = initialize_state (1000000000000)
init_state ["token-hold-pool"] = initialize_state (188622222)
init_state ["token-stake-pool"] = initialize_state (0)
init_state ["token-rewards-pool"] = initialize_state (0)
init_state ["token-sell-pool"] = initialize_state (mul_ls (sum_ls ([833333] + [2701235] + [2666667] + [4166667] + [5555556] + [1666667] + [1041667]) + [0.1]))
init_state ["token-mint"] = initialize_state (811377778)
init_state ["scam-upkeep-rate"] = initialize_state (0)
init_state ["scam-profit-rate"] = initialize_state (0)
init_state ["scam-page-success-rate"] = initialize_state (0)
init_state ["scam-page-visit-rate"] = initialize_state (0)
init_state ["page-visit-rate"] = initialize_state (0)
init_state ["airlock-upkeep-rate"] = initialize_state (0)
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
indicators_and_flows ["hodler-order-book"] = s_update_hodler_order_book
indicators_and_flows ["investor-order-book"] = s_update_investor_order_book
indicators_and_flows ["position-order-book"] = s_update_position_order_book
indicators_and_flows ["swing-order-book"] = s_update_swing_order_book
indicators_and_flows ["token-price-delta"] = s_update_token_price_delta
indicators_and_flows ["change-reward-amount"] = s_update_change_reward_amount
indicators_and_flows ["change-buyback-amount"] = s_update_change_buyback_amount
indicators_and_flows ["change-user-fee"] = s_update_change_user_fee
indicators_and_flows ["change-lookup-fee"] = s_update_change_lookup_fee
indicators_and_flows ["change-stake-yield"] = s_update_change_stake_yield
indicators_and_flows ["change-max-stake"] = s_update_change_max_stake
indicators_and_flows ["fitness"] = s_update_fitness
indicators_and_flows ["growth-level"] = s_update_growth_level
indicators_and_flows ["reward-rate"] = s_update_reward_rate
indicators_and_flows ["heuristic-innovation"] = s_update_heuristic_innovation
indicators_and_flows ["scammer-innovation"] = s_update_scammer_innovation
indicators_and_flows ["scam-profits-per-page"] = s_update_scam_profits_per_page
indicators_and_flows ["stake-yield"] = s_update_stake_yield
indicators_and_flows ["max-stake"] = s_update_max_stake
indicators_and_flows ["user-goal-progress"] = s_update_user_goal_progress
indicators_and_flows ["staking-opportunities"] = s_update_staking_opportunities
indicators_and_flows ["heuristic-contradictions"] = s_update_heuristic_contradictions
indicators_and_flows ["anti-heuristics"] = s_update_anti_heuristics
indicators_and_flows ["heuristics"] = s_update_heuristics
indicators_and_flows ["anti-user-goal-progress"] = s_update_anti_user_goal_progress
indicators_and_flows ["staking-enthusiasm"] = s_update_staking_enthusiasm
indicators_and_flows ["money-growth-rate"] = s_update_money_growth_rate
indicators_and_flows ["interlock-hype"] = s_update_interlock_hype
indicators_and_flows ["token-profit"] = s_update_token_profit
indicators_and_flows ["airlock-lookup-price"] = s_update_airlock_lookup_price
indicators_and_flows ["airlock-expenses"] = s_update_airlock_expenses
indicators_and_flows ["token-price"] = s_update_token_price
indicators_and_flows ["avg-token-value"] = s_update_avg_token_value
indicators_and_flows ["crypto-hype"] = s_update_crypto_hype
indicators_and_flows ["clock"] = s_update_clock
indicators_and_flows ["scam-upkeep-rate"] = s_update_scam_upkeep_rate
indicators_and_flows ["scam-profit-rate"] = s_update_scam_profit_rate
indicators_and_flows ["scam-page-success-rate"] = s_update_scam_page_success_rate
indicators_and_flows ["scam-page-visit-rate"] = s_update_scam_page_visit_rate
indicators_and_flows ["page-visit-rate"] = s_update_page_visit_rate
indicators_and_flows ["airlock-upkeep-rate"] = s_update_airlock_upkeep_rate
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
flow_commit ["airlock-upkeep-rate"] = s_commit_airlock_upkeep_rate
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
stock_reduction ["airlock-revenue"] = s_reduce_airlock_revenue
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
stock_cumulation = {}
stock_cumulation ["scam-upkeep"] = s_cumulate_scam_upkeep
stock_cumulation ["scam-profits"] = s_cumulate_scam_profits
stock_cumulation ["scam-page-successes"] = s_cumulate_scam_page_successes
stock_cumulation ["scam-page-visits"] = s_cumulate_scam_page_visits
stock_cumulation ["page-visits"] = s_cumulate_page_visits
stock_cumulation ["airlock-upkeep"] = s_cumulate_airlock_upkeep
stock_cumulation ["airlock-revenue"] = s_cumulate_airlock_revenue
stock_cumulation ["airlock-data-shared"] = s_cumulate_airlock_data_shared
stock_cumulation ["resolved-entities"] = s_cumulate_resolved_entities
stock_cumulation ["grey-area-entities"] = s_cumulate_grey_area_entities
stock_cumulation ["airlock-lookups"] = s_cumulate_airlock_lookups
stock_cumulation ["browser-users"] = s_cumulate_browser_users
stock_cumulation ["airlock-users"] = s_cumulate_airlock_users
stock_cumulation ["intr-investments"] = s_cumulate_intr_investments
stock_cumulation ["crypto-investments"] = s_cumulate_crypto_investments
stock_cumulation ["money-supply"] = s_cumulate_money_supply
stock_cumulation ["money-reclaimed"] = s_cumulate_money_reclaimed
stock_cumulation ["token-stake-pool"] = s_cumulate_token_stake_pool
stock_cumulation ["token-rewards-pool"] = s_cumulate_token_rewards_pool
stock_cumulation ["token-hold-pool"] = s_cumulate_token_hold_pool
stock_cumulation ["token-sell-pool"] = s_cumulate_token_sell_pool
psubs = [{ "policies": {}, "variables": indicators_and_flows }, { "policies": {}, "variables": stock_driven_flow_adjust }, { "policies": {}, "variables": flow_commit }, { "policies": {}, "variables": stock_reduction }, { "policies": {}, "variables": stock_cumulation }]
def run_top_organism (ls):
    global cfg
    if len (ls) == 0:
        return
    
    splice_individual (ls [0] [0], cfg)
    run_simulation ()


def run_simulation ():
    global sim_res
    global cfg
    global sim_cfg
    global psubs
    global init_state
    sim_cfg = config_sim (cfg)
    exp = Experiment ()
    exp.append_model (initial_state=init_state, model_id='interlock-1', sim_configs=sim_cfg, partial_state_update_blocks=psubs)
    exec_mode = ExecutionMode ()
    local_mode_ctx = ExecutionContext (context=exec_mode.local_mode)
    simulation = Executor (exec_context=local_mode_ctx, configs=exp.configs)
    exec_res = simulation.execute ()
    sim_events = exec_res [0]
    sim_res = pd.DataFrame (sim_events)
    sim_res = sim_res.applymap (tuple_to_value)
    sim_res = sim_res [sim_res.substep == 5]
    return sim_res


sim_res = None
genome_fitness = {}
genome_fitness ["anti-user-goal-progress-change-max-stake"] = [-1, 0, 1]
genome_fitness ["user-goal-progress-change-max-stake"] = [-1, 0, 1]
genome_fitness ["token-price-delta-change-max-stake"] = [-1, 0, 1]
genome_fitness ["anti-user-goal-progress-change-stake-yield"] = [-1, 0, 1]
genome_fitness ["user-goal-progress-change-stake-yield"] = [-1, 0, 1]
genome_fitness ["token-price-delta-change-stake-yield"] = [-1, 0, 1]
genome_fitness ["anti-user-goal-progress-change-lookup-fee"] = [-1, 0, 1]
genome_fitness ["user-goal-progress-change-lookup-fee"] = [-1, 0, 1]
genome_fitness ["token-price-delta-change-lookup-fee"] = [-1, 0, 1]
genome_fitness ["anti-user-goal-progress-change-user-fee"] = [-1, 0, 1]
genome_fitness ["user-goal-progress-change-user-fee"] = [-1, 0, 1]
genome_fitness ["token-price-delta-change-user-fee"] = [-1, 0, 1]
genome_fitness ["anti-user-goal-progress-change-buyback-amount"] = [-1, 0, 1]
genome_fitness ["user-goal-progress-change-buyback-amount"] = [-1, 0, 1]
genome_fitness ["token-price-delta-change-buyback-amount"] = [-1, 0, 1]
genome_fitness ["anti-user-goal-progress-change-reward-amount"] = [-1, 0, 1]
genome_fitness ["user-goal-progress-change-reward-amount"] = [-1, 0, 1]
genome_fitness ["token-price-delta-change-reward-amount"] = [-1, 0, 1]
fitness_top_n = []
def genome_eq (g1, g2):
    same = 0
    total = 0
    for k in g1:
        total = (total + 1)
        if g1 [k] == g2 [k]:
            same = (same + 1)
        

    return same == total


def is_twin (pop, g):
    twins = 0
    for i in pop:
        if genome_eq (g, i [0]):
            twins = (twins + 1)
        
        return twins > 0



def generate_individual (genome):
    individual = {}
    for g in genome:
        values = genome [g]
        individual [g] = random.choice (values)

    return individual


def splice_individual (ind, cfg):
    for g in ind:
        param_list = cfg ["M"] [g]
        i = 0
        while i < len (param_list):
            param_list [i] = ind [g]
            i = (i + 1)




def continue_evolving (pop, gen, max_gens, goal, eq):
    if gen == max_gens:
        return False
    
    for p in pop:
        if (eq == "=" and p [1] == goal):
            return False
        

    return True


def get_fitness (tup):
    return tup [1]


def create_pop (genome, n):
    rn = range (n)
    pop = []
    for i in rn:
        repeat = True
        while repeat:
            ind = generate_individual (genome)
            if not is_twin (pop, ind):
                pop.append ((ind, None))
                repeat = False
            


    return pop


def get_gene_val (pop_genome, g):
    vals = pop_genome [g]
    val = 0
    while val == 0:
        val = random.choice (vals)

    return val


def mutate_maybe (rate):
    chosen = sim_random (1, 100, 0)
    return chosen <= rate


def mutate_flip ():
    chosen = sim_random (0, 1, 0)
    return chosen == 0


def quasi_umad (individual, pop_genome, addrate, remrate):
    new = {}
    for g in individual:
        if mutate_maybe (addrate):
            val = get_gene_val (pop_genome, g)
            if mutate_flip ():
                val = (val * -1)
            
            new [g] = val
        else:
            new [g] = individual [g]
        

    for g in individual:
        if mutate_maybe (remrate):
            new [g] = 0
        else:
            new [g] = individual [g]
        

    return new


def fitness_per_run (data, fitness):
    run_fit = {}
    i = 0
    size = len (data)
    while i < size:
        run = data.iloc [i] ["run"]
        fitval = data.iloc [i] [fitness]
        run_fit [run] = fitval
        i = (i + 1)

    fit_sum = 0
    runs = 0
    for k in run_fit:
        fit_sum = (fit_sum + run_fit [k])
        runs = (runs + 1)

    return (fit_sum / runs)


def run_evolution ():
    global cfg
    fitness = create_pop (genome_fitness, 20)
    global fitness_top_n
    fitness_top_n_ever = []
    fitness_gen = 1
    evolve = True
    while evolve:
        ind_id = 0
        while ind_id < len (fitness):
            ind = fitness [ind_id] [0]
            splice_individual (ind, cfg)
            with io.capture_output() as captured:
                run_simulation ()

            fitness_val = fitness_per_run (sim_res, "fitness")
            fitness [ind_id] = (fitness [ind_id] [0], fitness_val)
            ind_id = (ind_id + 1)

        evolve = (evolve and continue_evolving (fitness, fitness_gen, 100, 0, "="))
        tmp = sorted (fitness, key=get_fitness, reverse=False)
        keep = math.ceil (((20 / 100) * 20))
        del tmp [keep:]
        fitness = tmp
        new = []
        for i in fitness:
            new.append ((quasi_umad (i [0], genome_fitness, 10, 10), None))

        fitness_gen = (fitness_gen + 1)
        fitness_top_n = (fitness_top_n + fitness)
        tmp = sorted (fitness_top_n, key=get_fitness, reverse=False)
        keep = math.ceil (((20 / 100) * 20))
        del tmp [keep:]
        fitness_top_n = tmp
        fitness = new



def main ():
    global sim_res
    genetic = True
    standard = False
    if (genetic == True and standard == True):
        return True
    elif genetic == True:
        run_evolution ()
    else:
        sim_res = run_simulation ()
    


main ()


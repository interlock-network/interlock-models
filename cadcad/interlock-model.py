import numpy as np
import copy as copy
import pandas as pd
import constraint as lim
import plotly
import plotly.express as px
import random
import math
import time
from cadCAD.configuration.utils import bound_norm_random, config_sim, time_step, env_trigger
from cadCAD.configuration import Experiment
from cadCAD.engine import ExecutionMode, ExecutionContext
from cadCAD.engine import Executor
from IPython.utils import io
def s_stim_token_price_delta_updates_change_max_stake (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = (mul_ls (get_new_value (s, "stim-token-price-delta") + [_params ["stim-token-price-delta-change-max-stake"]]) if gt_eq_ls ([_params ["stim-token-price-delta-change-max-stake"]] + [0]) [0] else abs_ls (mul_ls (sum_ls (get_new_value (s, "stim-token-price-delta") + [_params ["stim-token-price-delta-change-max-stake"]]) + [_params ["stim-token-price-delta-change-max-stake"]])))
    append_each (points, new_val)

def s_stim_token_price_delta_updates_change_stake_yield (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = (mul_ls (get_new_value (s, "stim-token-price-delta") + [_params ["stim-token-price-delta-change-stake-yield"]]) if gt_eq_ls ([_params ["stim-token-price-delta-change-stake-yield"]] + [0]) [0] else abs_ls (mul_ls (sum_ls (get_new_value (s, "stim-token-price-delta") + [_params ["stim-token-price-delta-change-stake-yield"]]) + [_params ["stim-token-price-delta-change-stake-yield"]])))
    append_each (points, new_val)

def s_stim_token_price_delta_updates_change_lookup_fee (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = (mul_ls (get_new_value (s, "stim-token-price-delta") + [_params ["stim-token-price-delta-change-lookup-fee"]]) if gt_eq_ls ([_params ["stim-token-price-delta-change-lookup-fee"]] + [0]) [0] else abs_ls (mul_ls (sum_ls (get_new_value (s, "stim-token-price-delta") + [_params ["stim-token-price-delta-change-lookup-fee"]]) + [_params ["stim-token-price-delta-change-lookup-fee"]])))
    append_each (points, new_val)

def s_stim_token_price_delta_updates_change_user_fee (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = (mul_ls (get_new_value (s, "stim-token-price-delta") + [_params ["stim-token-price-delta-change-user-fee"]]) if gt_eq_ls ([_params ["stim-token-price-delta-change-user-fee"]] + [0]) [0] else abs_ls (mul_ls (sum_ls (get_new_value (s, "stim-token-price-delta") + [_params ["stim-token-price-delta-change-user-fee"]]) + [_params ["stim-token-price-delta-change-user-fee"]])))
    append_each (points, new_val)

def s_stim_token_price_delta_updates_change_buyback_amount (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = (mul_ls (get_new_value (s, "stim-token-price-delta") + [_params ["stim-token-price-delta-change-buyback-amount"]]) if gt_eq_ls ([_params ["stim-token-price-delta-change-buyback-amount"]] + [0]) [0] else abs_ls (mul_ls (sum_ls (get_new_value (s, "stim-token-price-delta") + [_params ["stim-token-price-delta-change-buyback-amount"]]) + [_params ["stim-token-price-delta-change-buyback-amount"]])))
    append_each (points, new_val)

def s_stim_token_price_delta_updates_change_sell_amount (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = (mul_ls (get_new_value (s, "stim-token-price-delta") + [_params ["stim-token-price-delta-change-sell-amount"]]) if gt_eq_ls ([_params ["stim-token-price-delta-change-sell-amount"]] + [0]) [0] else abs_ls (mul_ls (sum_ls (get_new_value (s, "stim-token-price-delta") + [_params ["stim-token-price-delta-change-sell-amount"]]) + [_params ["stim-token-price-delta-change-sell-amount"]])))
    append_each (points, new_val)

def s_stim_token_price_delta_updates_change_reward_amount (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = (mul_ls (get_new_value (s, "stim-token-price-delta") + [_params ["stim-token-price-delta-change-reward-amount"]]) if gt_eq_ls ([_params ["stim-token-price-delta-change-reward-amount"]] + [0]) [0] else abs_ls (mul_ls (sum_ls (get_new_value (s, "stim-token-price-delta") + [_params ["stim-token-price-delta-change-reward-amount"]]) + [_params ["stim-token-price-delta-change-reward-amount"]])))
    append_each (points, new_val)

def s_stim_token_price_delta_updates_change_urgency (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = (mul_ls (get_new_value (s, "stim-token-price-delta") + [_params ["stim-token-price-delta-change-urgency"]]) if gt_eq_ls ([_params ["stim-token-price-delta-change-urgency"]] + [0]) [0] else abs_ls (mul_ls (sum_ls (get_new_value (s, "stim-token-price-delta") + [_params ["stim-token-price-delta-change-urgency"]]) + [_params ["stim-token-price-delta-change-urgency"]])))
    append_each (points, new_val)

def s_stim_anti_user_goal_progress_updates_change_max_stake (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = (mul_ls (get_new_value (s, "stim-anti-user-goal-progress") + [_params ["stim-anti-user-goal-progress-change-max-stake"]]) if gt_eq_ls ([_params ["stim-anti-user-goal-progress-change-max-stake"]] + [0]) [0] else abs_ls (mul_ls (sum_ls (get_new_value (s, "stim-anti-user-goal-progress") + [_params ["stim-anti-user-goal-progress-change-max-stake"]]) + [_params ["stim-anti-user-goal-progress-change-max-stake"]])))
    append_each (points, new_val)

def s_stim_anti_user_goal_progress_updates_change_stake_yield (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = (mul_ls (get_new_value (s, "stim-anti-user-goal-progress") + [_params ["stim-anti-user-goal-progress-change-stake-yield"]]) if gt_eq_ls ([_params ["stim-anti-user-goal-progress-change-stake-yield"]] + [0]) [0] else abs_ls (mul_ls (sum_ls (get_new_value (s, "stim-anti-user-goal-progress") + [_params ["stim-anti-user-goal-progress-change-stake-yield"]]) + [_params ["stim-anti-user-goal-progress-change-stake-yield"]])))
    append_each (points, new_val)

def s_stim_anti_user_goal_progress_updates_change_lookup_fee (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = (mul_ls (get_new_value (s, "stim-anti-user-goal-progress") + [_params ["stim-anti-user-goal-progress-change-lookup-fee"]]) if gt_eq_ls ([_params ["stim-anti-user-goal-progress-change-lookup-fee"]] + [0]) [0] else abs_ls (mul_ls (sum_ls (get_new_value (s, "stim-anti-user-goal-progress") + [_params ["stim-anti-user-goal-progress-change-lookup-fee"]]) + [_params ["stim-anti-user-goal-progress-change-lookup-fee"]])))
    append_each (points, new_val)

def s_stim_anti_user_goal_progress_updates_change_user_fee (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = (mul_ls (get_new_value (s, "stim-anti-user-goal-progress") + [_params ["stim-anti-user-goal-progress-change-user-fee"]]) if gt_eq_ls ([_params ["stim-anti-user-goal-progress-change-user-fee"]] + [0]) [0] else abs_ls (mul_ls (sum_ls (get_new_value (s, "stim-anti-user-goal-progress") + [_params ["stim-anti-user-goal-progress-change-user-fee"]]) + [_params ["stim-anti-user-goal-progress-change-user-fee"]])))
    append_each (points, new_val)

def s_stim_anti_user_goal_progress_updates_change_buyback_amount (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = (mul_ls (get_new_value (s, "stim-anti-user-goal-progress") + [_params ["stim-anti-user-goal-progress-change-buyback-amount"]]) if gt_eq_ls ([_params ["stim-anti-user-goal-progress-change-buyback-amount"]] + [0]) [0] else abs_ls (mul_ls (sum_ls (get_new_value (s, "stim-anti-user-goal-progress") + [_params ["stim-anti-user-goal-progress-change-buyback-amount"]]) + [_params ["stim-anti-user-goal-progress-change-buyback-amount"]])))
    append_each (points, new_val)

def s_stim_anti_user_goal_progress_updates_change_sell_amount (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = (mul_ls (get_new_value (s, "stim-anti-user-goal-progress") + [_params ["stim-anti-user-goal-progress-change-sell-amount"]]) if gt_eq_ls ([_params ["stim-anti-user-goal-progress-change-sell-amount"]] + [0]) [0] else abs_ls (mul_ls (sum_ls (get_new_value (s, "stim-anti-user-goal-progress") + [_params ["stim-anti-user-goal-progress-change-sell-amount"]]) + [_params ["stim-anti-user-goal-progress-change-sell-amount"]])))
    append_each (points, new_val)

def s_stim_anti_user_goal_progress_updates_change_reward_amount (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = (mul_ls (get_new_value (s, "stim-anti-user-goal-progress") + [_params ["stim-anti-user-goal-progress-change-reward-amount"]]) if gt_eq_ls ([_params ["stim-anti-user-goal-progress-change-reward-amount"]] + [0]) [0] else abs_ls (mul_ls (sum_ls (get_new_value (s, "stim-anti-user-goal-progress") + [_params ["stim-anti-user-goal-progress-change-reward-amount"]]) + [_params ["stim-anti-user-goal-progress-change-reward-amount"]])))
    append_each (points, new_val)

def s_stim_anti_user_goal_progress_updates_change_urgency (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = (mul_ls (get_new_value (s, "stim-anti-user-goal-progress") + [_params ["stim-anti-user-goal-progress-change-urgency"]]) if gt_eq_ls ([_params ["stim-anti-user-goal-progress-change-urgency"]] + [0]) [0] else abs_ls (mul_ls (sum_ls (get_new_value (s, "stim-anti-user-goal-progress") + [_params ["stim-anti-user-goal-progress-change-urgency"]]) + [_params ["stim-anti-user-goal-progress-change-urgency"]])))
    append_each (points, new_val)

def s_stim_contradiction_rate_updates_change_max_stake (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = (mul_ls (get_new_value (s, "stim-contradiction-rate") + [_params ["stim-contradiction-rate-change-max-stake"]]) if gt_eq_ls ([_params ["stim-contradiction-rate-change-max-stake"]] + [0]) [0] else abs_ls (mul_ls (sum_ls (get_new_value (s, "stim-contradiction-rate") + [_params ["stim-contradiction-rate-change-max-stake"]]) + [_params ["stim-contradiction-rate-change-max-stake"]])))
    append_each (points, new_val)

def s_stim_contradiction_rate_updates_change_stake_yield (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = (mul_ls (get_new_value (s, "stim-contradiction-rate") + [_params ["stim-contradiction-rate-change-stake-yield"]]) if gt_eq_ls ([_params ["stim-contradiction-rate-change-stake-yield"]] + [0]) [0] else abs_ls (mul_ls (sum_ls (get_new_value (s, "stim-contradiction-rate") + [_params ["stim-contradiction-rate-change-stake-yield"]]) + [_params ["stim-contradiction-rate-change-stake-yield"]])))
    append_each (points, new_val)

def s_stim_contradiction_rate_updates_change_lookup_fee (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = (mul_ls (get_new_value (s, "stim-contradiction-rate") + [_params ["stim-contradiction-rate-change-lookup-fee"]]) if gt_eq_ls ([_params ["stim-contradiction-rate-change-lookup-fee"]] + [0]) [0] else abs_ls (mul_ls (sum_ls (get_new_value (s, "stim-contradiction-rate") + [_params ["stim-contradiction-rate-change-lookup-fee"]]) + [_params ["stim-contradiction-rate-change-lookup-fee"]])))
    append_each (points, new_val)

def s_stim_contradiction_rate_updates_change_user_fee (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = (mul_ls (get_new_value (s, "stim-contradiction-rate") + [_params ["stim-contradiction-rate-change-user-fee"]]) if gt_eq_ls ([_params ["stim-contradiction-rate-change-user-fee"]] + [0]) [0] else abs_ls (mul_ls (sum_ls (get_new_value (s, "stim-contradiction-rate") + [_params ["stim-contradiction-rate-change-user-fee"]]) + [_params ["stim-contradiction-rate-change-user-fee"]])))
    append_each (points, new_val)

def s_stim_contradiction_rate_updates_change_buyback_amount (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = (mul_ls (get_new_value (s, "stim-contradiction-rate") + [_params ["stim-contradiction-rate-change-buyback-amount"]]) if gt_eq_ls ([_params ["stim-contradiction-rate-change-buyback-amount"]] + [0]) [0] else abs_ls (mul_ls (sum_ls (get_new_value (s, "stim-contradiction-rate") + [_params ["stim-contradiction-rate-change-buyback-amount"]]) + [_params ["stim-contradiction-rate-change-buyback-amount"]])))
    append_each (points, new_val)

def s_stim_contradiction_rate_updates_change_sell_amount (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = (mul_ls (get_new_value (s, "stim-contradiction-rate") + [_params ["stim-contradiction-rate-change-sell-amount"]]) if gt_eq_ls ([_params ["stim-contradiction-rate-change-sell-amount"]] + [0]) [0] else abs_ls (mul_ls (sum_ls (get_new_value (s, "stim-contradiction-rate") + [_params ["stim-contradiction-rate-change-sell-amount"]]) + [_params ["stim-contradiction-rate-change-sell-amount"]])))
    append_each (points, new_val)

def s_stim_contradiction_rate_updates_change_reward_amount (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = (mul_ls (get_new_value (s, "stim-contradiction-rate") + [_params ["stim-contradiction-rate-change-reward-amount"]]) if gt_eq_ls ([_params ["stim-contradiction-rate-change-reward-amount"]] + [0]) [0] else abs_ls (mul_ls (sum_ls (get_new_value (s, "stim-contradiction-rate") + [_params ["stim-contradiction-rate-change-reward-amount"]]) + [_params ["stim-contradiction-rate-change-reward-amount"]])))
    append_each (points, new_val)

def s_stim_contradiction_rate_updates_change_urgency (ctx, s, _params):
    if ctx.get ("points") == None:
        ctx ["points"] = []
    
    points = ctx.get ("points")
    new_val = (mul_ls (get_new_value (s, "stim-contradiction-rate") + [_params ["stim-contradiction-rate-change-urgency"]]) if gt_eq_ls ([_params ["stim-contradiction-rate-change-urgency"]] + [0]) [0] else abs_ls (mul_ls (sum_ls (get_new_value (s, "stim-contradiction-rate") + [_params ["stim-contradiction-rate-change-urgency"]]) + [_params ["stim-contradiction-rate-change-urgency"]])))
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
    new_val = agg_rows_range_new ([[LessThanEq (get_new_value (s, "clock")), LessThanEq (mul_ls (get_new_value (s, "token-price") + diff_ls ([1] + [_params ["minimum-trade-profit"]])))]], get_new_value (s, "swing-order-book"))
    append_each (removable, new_val)

def s_position_order_book_updates_position_order_book (ctx, s, _params):
    if ctx.get ("removable") == None:
        ctx ["removable"] = []
    
    removable = ctx.get ("removable")
    new_val = agg_rows_range_new ([[LessThanEq (get_new_value (s, "clock")), LessThanEq (mul_ls (get_new_value (s, "token-price") + diff_ls ([1] + [_params ["minimum-trade-profit"]])))]], get_new_value (s, "position-order-book"))
    append_each (removable, new_val)

def s_investor_order_book_updates_investor_order_book (ctx, s, _params):
    if ctx.get ("removable") == None:
        ctx ["removable"] = []
    
    removable = ctx.get ("removable")
    new_val = agg_rows_range_new ([[LessThanEq (get_new_value (s, "clock")), LessThanEq (mul_ls (get_new_value (s, "token-price") + diff_ls ([1] + [_params ["minimum-trade-profit"]])))]], get_new_value (s, "investor-order-book"))
    append_each (removable, new_val)

def s_swing_order_book_updates_token_unhold_rate (ctx, s, _params):
    if ctx.get ("quantity") == None:
        ctx ["quantity"] = []
    
    quantity = ctx.get ("quantity")
    new_val = sum_ls (agg_to_list (agg_col_to_list (2, agg_rows_range_new ([[LessThanEq (get_new_value (s, "clock")), LessThanEq (mul_ls (get_new_value (s, "token-price") + diff_ls ([1] + [_params ["minimum-trade-profit"]])))]], get_new_value (s, "swing-order-book")))))
    append_each (quantity, new_val)

def s_position_order_book_updates_token_unhold_rate (ctx, s, _params):
    if ctx.get ("quantity") == None:
        ctx ["quantity"] = []
    
    quantity = ctx.get ("quantity")
    new_val = sum_ls (agg_to_list (agg_col_to_list (2, agg_rows_range_new ([[LessThanEq (get_new_value (s, "clock")), LessThanEq (mul_ls (get_new_value (s, "token-price") + diff_ls ([1] + [_params ["minimum-trade-profit"]])))]], get_new_value (s, "position-order-book")))))
    append_each (quantity, new_val)

def s_investor_order_book_updates_token_unhold_rate (ctx, s, _params):
    if ctx.get ("quantity") == None:
        ctx ["quantity"] = []
    
    quantity = ctx.get ("quantity")
    new_val = sum_ls (agg_to_list (agg_col_to_list (2, agg_rows_range_new ([[LessThanEq (get_new_value (s, "clock")), LessThanEq (mul_ls (get_new_value (s, "token-price") + diff_ls ([1] + [_params ["minimum-trade-profit"]])))]], get_new_value (s, "investor-order-book")))))
    append_each (quantity, new_val)

def s_crypto_hype_updates_staking_enthusiasm (ctx, s, _params):
    if ctx.get ("expectation-multiplier") == None:
        ctx ["expectation-multiplier"] = []
    
    expectation_multiplier = ctx.get ("expectation-multiplier")
    new_val = ([4] if lt_eq_ls (get_new_value (s, "crypto-hype") + [0]) [0] else [1])
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

def s_interlock_hype_updates_threatslayer_adoption_rate (ctx, s, _params):
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

def s_adjust_community_sale_pool_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "community-sale-hold-rate") [0]
    inventory = get_new_value (s, "community-sale-pool") [0]
    if flow_val < 0:
        flow_val = 0
    
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["community-sale-hold-rate"] = flow_val

def s_reduce_community_sale_pool (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "community-sale-hold-rate"))
    return "community-sale-pool", update_state (s, "community-sale-pool", diff_ls (get_new_value (s, "community-sale-pool") + red))

def s_clock_updates_community_sale_hold_rate (ctx, s, _params):
    if ctx.get ("months") == None:
        ctx ["months"] = []
    
    months = ctx.get ("months")
    new_val = floor_ls (div_ls (get_new_value (s, "clock") + [4]))
    append_each (months, new_val)

def s_commit_community_sale_hold_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "community-sale-hold-rate", update_state (s, "community-sale-hold-rate", [adjusted_flows ["community-sale-hold-rate"]])

def s_community_sale_hold_rate_updates_swing_order_book (ctx, s, _params):
    if ctx.get ("community-sale-quantity") == None:
        ctx ["community-sale-quantity"] = []
    
    community_sale_quantity = ctx.get ("community-sale-quantity")
    new_val = mul_ls ([_params ["swing-traders"]] + get_new_value (s, "community-sale-hold-rate"))
    append_each (community_sale_quantity, new_val)

def s_community_sale_hold_rate_updates_position_order_book (ctx, s, _params):
    if ctx.get ("community-sale-quantity") == None:
        ctx ["community-sale-quantity"] = []
    
    community_sale_quantity = ctx.get ("community-sale-quantity")
    new_val = mul_ls ([_params ["position-traders"]] + get_new_value (s, "community-sale-hold-rate"))
    append_each (community_sale_quantity, new_val)

def s_community_sale_hold_rate_updates_investor_order_book (ctx, s, _params):
    if ctx.get ("community-sale-quantity") == None:
        ctx ["community-sale-quantity"] = []
    
    community_sale_quantity = ctx.get ("community-sale-quantity")
    new_val = mul_ls ([_params ["investors"]] + get_new_value (s, "community-sale-hold-rate"))
    append_each (community_sale_quantity, new_val)

def s_community_sale_hold_rate_updates_hodler_order_book (ctx, s, _params):
    if ctx.get ("community-sale-quantity") == None:
        ctx ["community-sale-quantity"] = []
    
    community_sale_quantity = ctx.get ("community-sale-quantity")
    new_val = mul_ls ([_params ["hodlers"]] + get_new_value (s, "community-sale-hold-rate"))
    append_each (community_sale_quantity, new_val)

def s_community_sale_pool_value_updates_swing_order_book (ctx, s, _params):
    if ctx.get ("community-sale-price") == None:
        ctx ["community-sale-price"] = []
    
    community_sale_price = ctx.get ("community-sale-price")
    new_val = get_new_value (s, "community-sale-pool-value")
    append_each (community_sale_price, new_val)

def s_community_sale_pool_value_updates_position_order_book (ctx, s, _params):
    if ctx.get ("community-sale-price") == None:
        ctx ["community-sale-price"] = []
    
    community_sale_price = ctx.get ("community-sale-price")
    new_val = get_new_value (s, "community-sale-pool-value")
    append_each (community_sale_price, new_val)

def s_community_sale_pool_value_updates_investor_order_book (ctx, s, _params):
    if ctx.get ("community-sale-price") == None:
        ctx ["community-sale-price"] = []
    
    community_sale_price = ctx.get ("community-sale-price")
    new_val = get_new_value (s, "community-sale-pool-value")
    append_each (community_sale_price, new_val)

def s_community_sale_pool_value_updates_hodler_order_book (ctx, s, _params):
    if ctx.get ("community-sale-price") == None:
        ctx ["community-sale-price"] = []
    
    community_sale_price = ctx.get ("community-sale-price")
    new_val = get_new_value (s, "community-sale-pool-value")
    append_each (community_sale_price, new_val)

def s_adjust_presale_1_pool_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "presale-1-hold-rate") [0]
    inventory = get_new_value (s, "presale-1-pool") [0]
    if flow_val < 0:
        flow_val = 0
    
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["presale-1-hold-rate"] = flow_val

def s_reduce_presale_1_pool (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "presale-1-hold-rate"))
    return "presale-1-pool", update_state (s, "presale-1-pool", diff_ls (get_new_value (s, "presale-1-pool") + red))

def s_clock_updates_presale_1_hold_rate (ctx, s, _params):
    if ctx.get ("months") == None:
        ctx ["months"] = []
    
    months = ctx.get ("months")
    new_val = floor_ls (div_ls (get_new_value (s, "clock") + [4]))
    append_each (months, new_val)

def s_commit_presale_1_hold_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "presale-1-hold-rate", update_state (s, "presale-1-hold-rate", [adjusted_flows ["presale-1-hold-rate"]])

def s_presale_1_hold_rate_updates_swing_order_book (ctx, s, _params):
    if ctx.get ("presale-1-quantity") == None:
        ctx ["presale-1-quantity"] = []
    
    presale_1_quantity = ctx.get ("presale-1-quantity")
    new_val = mul_ls ([_params ["swing-traders"]] + get_new_value (s, "presale-1-hold-rate"))
    append_each (presale_1_quantity, new_val)

def s_presale_1_hold_rate_updates_position_order_book (ctx, s, _params):
    if ctx.get ("presale-1-quantity") == None:
        ctx ["presale-1-quantity"] = []
    
    presale_1_quantity = ctx.get ("presale-1-quantity")
    new_val = mul_ls ([_params ["position-traders"]] + get_new_value (s, "presale-1-hold-rate"))
    append_each (presale_1_quantity, new_val)

def s_presale_1_hold_rate_updates_investor_order_book (ctx, s, _params):
    if ctx.get ("presale-1-quantity") == None:
        ctx ["presale-1-quantity"] = []
    
    presale_1_quantity = ctx.get ("presale-1-quantity")
    new_val = mul_ls ([_params ["investors"]] + get_new_value (s, "presale-1-hold-rate"))
    append_each (presale_1_quantity, new_val)

def s_presale_1_hold_rate_updates_hodler_order_book (ctx, s, _params):
    if ctx.get ("presale-1-quantity") == None:
        ctx ["presale-1-quantity"] = []
    
    presale_1_quantity = ctx.get ("presale-1-quantity")
    new_val = mul_ls ([_params ["hodlers"]] + get_new_value (s, "presale-1-hold-rate"))
    append_each (presale_1_quantity, new_val)

def s_presale_1_pool_value_updates_swing_order_book (ctx, s, _params):
    if ctx.get ("presale-1-price") == None:
        ctx ["presale-1-price"] = []
    
    presale_1_price = ctx.get ("presale-1-price")
    new_val = get_new_value (s, "presale-1-pool-value")
    append_each (presale_1_price, new_val)

def s_presale_1_pool_value_updates_position_order_book (ctx, s, _params):
    if ctx.get ("presale-1-price") == None:
        ctx ["presale-1-price"] = []
    
    presale_1_price = ctx.get ("presale-1-price")
    new_val = get_new_value (s, "presale-1-pool-value")
    append_each (presale_1_price, new_val)

def s_presale_1_pool_value_updates_investor_order_book (ctx, s, _params):
    if ctx.get ("presale-1-price") == None:
        ctx ["presale-1-price"] = []
    
    presale_1_price = ctx.get ("presale-1-price")
    new_val = get_new_value (s, "presale-1-pool-value")
    append_each (presale_1_price, new_val)

def s_presale_1_pool_value_updates_hodler_order_book (ctx, s, _params):
    if ctx.get ("presale-1-price") == None:
        ctx ["presale-1-price"] = []
    
    presale_1_price = ctx.get ("presale-1-price")
    new_val = get_new_value (s, "presale-1-pool-value")
    append_each (presale_1_price, new_val)

def s_adjust_presale_2_pool_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "presale-2-hold-rate") [0]
    inventory = get_new_value (s, "presale-2-pool") [0]
    if flow_val < 0:
        flow_val = 0
    
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["presale-2-hold-rate"] = flow_val

def s_reduce_presale_2_pool (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "presale-2-hold-rate"))
    return "presale-2-pool", update_state (s, "presale-2-pool", diff_ls (get_new_value (s, "presale-2-pool") + red))

def s_clock_updates_presale_2_hold_rate (ctx, s, _params):
    if ctx.get ("months") == None:
        ctx ["months"] = []
    
    months = ctx.get ("months")
    new_val = floor_ls (div_ls (get_new_value (s, "clock") + [4]))
    append_each (months, new_val)

def s_commit_presale_2_hold_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "presale-2-hold-rate", update_state (s, "presale-2-hold-rate", [adjusted_flows ["presale-2-hold-rate"]])

def s_presale_2_hold_rate_updates_swing_order_book (ctx, s, _params):
    if ctx.get ("presale-2-quantity") == None:
        ctx ["presale-2-quantity"] = []
    
    presale_2_quantity = ctx.get ("presale-2-quantity")
    new_val = mul_ls ([_params ["swing-traders"]] + get_new_value (s, "presale-2-hold-rate"))
    append_each (presale_2_quantity, new_val)

def s_presale_2_hold_rate_updates_position_order_book (ctx, s, _params):
    if ctx.get ("presale-2-quantity") == None:
        ctx ["presale-2-quantity"] = []
    
    presale_2_quantity = ctx.get ("presale-2-quantity")
    new_val = mul_ls ([_params ["position-traders"]] + get_new_value (s, "presale-2-hold-rate"))
    append_each (presale_2_quantity, new_val)

def s_presale_2_hold_rate_updates_investor_order_book (ctx, s, _params):
    if ctx.get ("presale-2-quantity") == None:
        ctx ["presale-2-quantity"] = []
    
    presale_2_quantity = ctx.get ("presale-2-quantity")
    new_val = mul_ls ([_params ["investors"]] + get_new_value (s, "presale-2-hold-rate"))
    append_each (presale_2_quantity, new_val)

def s_presale_2_hold_rate_updates_hodler_order_book (ctx, s, _params):
    if ctx.get ("presale-2-quantity") == None:
        ctx ["presale-2-quantity"] = []
    
    presale_2_quantity = ctx.get ("presale-2-quantity")
    new_val = mul_ls ([_params ["hodlers"]] + get_new_value (s, "presale-2-hold-rate"))
    append_each (presale_2_quantity, new_val)

def s_presale_2_pool_value_updates_swing_order_book (ctx, s, _params):
    if ctx.get ("presale-2-price") == None:
        ctx ["presale-2-price"] = []
    
    presale_2_price = ctx.get ("presale-2-price")
    new_val = get_new_value (s, "presale-2-pool-value")
    append_each (presale_2_price, new_val)

def s_presale_2_pool_value_updates_position_order_book (ctx, s, _params):
    if ctx.get ("presale-2-price") == None:
        ctx ["presale-2-price"] = []
    
    presale_2_price = ctx.get ("presale-2-price")
    new_val = get_new_value (s, "presale-2-pool-value")
    append_each (presale_2_price, new_val)

def s_presale_2_pool_value_updates_investor_order_book (ctx, s, _params):
    if ctx.get ("presale-2-price") == None:
        ctx ["presale-2-price"] = []
    
    presale_2_price = ctx.get ("presale-2-price")
    new_val = get_new_value (s, "presale-2-pool-value")
    append_each (presale_2_price, new_val)

def s_presale_2_pool_value_updates_hodler_order_book (ctx, s, _params):
    if ctx.get ("presale-2-price") == None:
        ctx ["presale-2-price"] = []
    
    presale_2_price = ctx.get ("presale-2-price")
    new_val = get_new_value (s, "presale-2-pool-value")
    append_each (presale_2_price, new_val)

def s_adjust_presale_3_pool_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "presale-3-hold-rate") [0]
    inventory = get_new_value (s, "presale-3-pool") [0]
    if flow_val < 0:
        flow_val = 0
    
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["presale-3-hold-rate"] = flow_val

def s_reduce_presale_3_pool (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "presale-3-hold-rate"))
    return "presale-3-pool", update_state (s, "presale-3-pool", diff_ls (get_new_value (s, "presale-3-pool") + red))

def s_clock_updates_presale_3_hold_rate (ctx, s, _params):
    if ctx.get ("months") == None:
        ctx ["months"] = []
    
    months = ctx.get ("months")
    new_val = floor_ls (div_ls (get_new_value (s, "clock") + [4]))
    append_each (months, new_val)

def s_commit_presale_3_hold_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "presale-3-hold-rate", update_state (s, "presale-3-hold-rate", [adjusted_flows ["presale-3-hold-rate"]])

def s_presale_3_hold_rate_updates_swing_order_book (ctx, s, _params):
    if ctx.get ("presale-3-quantity") == None:
        ctx ["presale-3-quantity"] = []
    
    presale_3_quantity = ctx.get ("presale-3-quantity")
    new_val = mul_ls ([_params ["swing-traders"]] + get_new_value (s, "presale-3-hold-rate"))
    append_each (presale_3_quantity, new_val)

def s_presale_3_hold_rate_updates_position_order_book (ctx, s, _params):
    if ctx.get ("presale-3-quantity") == None:
        ctx ["presale-3-quantity"] = []
    
    presale_3_quantity = ctx.get ("presale-3-quantity")
    new_val = mul_ls ([_params ["position-traders"]] + get_new_value (s, "presale-3-hold-rate"))
    append_each (presale_3_quantity, new_val)

def s_presale_3_hold_rate_updates_investor_order_book (ctx, s, _params):
    if ctx.get ("presale-3-quantity") == None:
        ctx ["presale-3-quantity"] = []
    
    presale_3_quantity = ctx.get ("presale-3-quantity")
    new_val = mul_ls ([_params ["investors"]] + get_new_value (s, "presale-3-hold-rate"))
    append_each (presale_3_quantity, new_val)

def s_presale_3_hold_rate_updates_hodler_order_book (ctx, s, _params):
    if ctx.get ("presale-3-quantity") == None:
        ctx ["presale-3-quantity"] = []
    
    presale_3_quantity = ctx.get ("presale-3-quantity")
    new_val = mul_ls ([_params ["hodlers"]] + get_new_value (s, "presale-3-hold-rate"))
    append_each (presale_3_quantity, new_val)

def s_presale_3_pool_value_updates_swing_order_book (ctx, s, _params):
    if ctx.get ("presale-3-price") == None:
        ctx ["presale-3-price"] = []
    
    presale_3_price = ctx.get ("presale-3-price")
    new_val = get_new_value (s, "presale-3-pool-value")
    append_each (presale_3_price, new_val)

def s_presale_3_pool_value_updates_position_order_book (ctx, s, _params):
    if ctx.get ("presale-3-price") == None:
        ctx ["presale-3-price"] = []
    
    presale_3_price = ctx.get ("presale-3-price")
    new_val = get_new_value (s, "presale-3-pool-value")
    append_each (presale_3_price, new_val)

def s_presale_3_pool_value_updates_investor_order_book (ctx, s, _params):
    if ctx.get ("presale-3-price") == None:
        ctx ["presale-3-price"] = []
    
    presale_3_price = ctx.get ("presale-3-price")
    new_val = get_new_value (s, "presale-3-pool-value")
    append_each (presale_3_price, new_val)

def s_presale_3_pool_value_updates_hodler_order_book (ctx, s, _params):
    if ctx.get ("presale-3-price") == None:
        ctx ["presale-3-price"] = []
    
    presale_3_price = ctx.get ("presale-3-price")
    new_val = get_new_value (s, "presale-3-pool-value")
    append_each (presale_3_price, new_val)

def s_adjust_team_founders_pool_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "team-founders-hold-rate") [0]
    inventory = get_new_value (s, "team-founders-pool") [0]
    if flow_val < 0:
        flow_val = 0
    
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["team-founders-hold-rate"] = flow_val

def s_reduce_team_founders_pool (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "team-founders-hold-rate"))
    return "team-founders-pool", update_state (s, "team-founders-pool", diff_ls (get_new_value (s, "team-founders-pool") + red))

def s_clock_updates_team_founders_hold_rate (ctx, s, _params):
    if ctx.get ("months") == None:
        ctx ["months"] = []
    
    months = ctx.get ("months")
    new_val = floor_ls (div_ls (get_new_value (s, "clock") + [4]))
    append_each (months, new_val)

def s_commit_team_founders_hold_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "team-founders-hold-rate", update_state (s, "team-founders-hold-rate", [adjusted_flows ["team-founders-hold-rate"]])

def s_team_founders_hold_rate_updates_swing_order_book (ctx, s, _params):
    if ctx.get ("team-founders-quantity") == None:
        ctx ["team-founders-quantity"] = []
    
    team_founders_quantity = ctx.get ("team-founders-quantity")
    new_val = mul_ls ([_params ["swing-traders"]] + get_new_value (s, "team-founders-hold-rate"))
    append_each (team_founders_quantity, new_val)

def s_team_founders_hold_rate_updates_position_order_book (ctx, s, _params):
    if ctx.get ("team-founders-quantity") == None:
        ctx ["team-founders-quantity"] = []
    
    team_founders_quantity = ctx.get ("team-founders-quantity")
    new_val = mul_ls ([_params ["position-traders"]] + get_new_value (s, "team-founders-hold-rate"))
    append_each (team_founders_quantity, new_val)

def s_team_founders_hold_rate_updates_investor_order_book (ctx, s, _params):
    if ctx.get ("team-founders-quantity") == None:
        ctx ["team-founders-quantity"] = []
    
    team_founders_quantity = ctx.get ("team-founders-quantity")
    new_val = mul_ls ([_params ["investors"]] + get_new_value (s, "team-founders-hold-rate"))
    append_each (team_founders_quantity, new_val)

def s_team_founders_hold_rate_updates_hodler_order_book (ctx, s, _params):
    if ctx.get ("team-founders-quantity") == None:
        ctx ["team-founders-quantity"] = []
    
    team_founders_quantity = ctx.get ("team-founders-quantity")
    new_val = mul_ls ([_params ["hodlers"]] + get_new_value (s, "team-founders-hold-rate"))
    append_each (team_founders_quantity, new_val)

def s_team_founders_pool_value_updates_swing_order_book (ctx, s, _params):
    if ctx.get ("team-founders-price") == None:
        ctx ["team-founders-price"] = []
    
    team_founders_price = ctx.get ("team-founders-price")
    new_val = get_new_value (s, "team-founders-pool-value")
    append_each (team_founders_price, new_val)

def s_team_founders_pool_value_updates_position_order_book (ctx, s, _params):
    if ctx.get ("team-founders-price") == None:
        ctx ["team-founders-price"] = []
    
    team_founders_price = ctx.get ("team-founders-price")
    new_val = get_new_value (s, "team-founders-pool-value")
    append_each (team_founders_price, new_val)

def s_team_founders_pool_value_updates_investor_order_book (ctx, s, _params):
    if ctx.get ("team-founders-price") == None:
        ctx ["team-founders-price"] = []
    
    team_founders_price = ctx.get ("team-founders-price")
    new_val = get_new_value (s, "team-founders-pool-value")
    append_each (team_founders_price, new_val)

def s_team_founders_pool_value_updates_hodler_order_book (ctx, s, _params):
    if ctx.get ("team-founders-price") == None:
        ctx ["team-founders-price"] = []
    
    team_founders_price = ctx.get ("team-founders-price")
    new_val = get_new_value (s, "team-founders-pool-value")
    append_each (team_founders_price, new_val)

def s_adjust_outlier_ventures_pool_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "outlier-ventures-hold-rate") [0]
    inventory = get_new_value (s, "outlier-ventures-pool") [0]
    if flow_val < 0:
        flow_val = 0
    
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["outlier-ventures-hold-rate"] = flow_val

def s_reduce_outlier_ventures_pool (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "outlier-ventures-hold-rate"))
    return "outlier-ventures-pool", update_state (s, "outlier-ventures-pool", diff_ls (get_new_value (s, "outlier-ventures-pool") + red))

def s_clock_updates_outlier_ventures_hold_rate (ctx, s, _params):
    if ctx.get ("months") == None:
        ctx ["months"] = []
    
    months = ctx.get ("months")
    new_val = floor_ls (div_ls (get_new_value (s, "clock") + [4]))
    append_each (months, new_val)

def s_commit_outlier_ventures_hold_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "outlier-ventures-hold-rate", update_state (s, "outlier-ventures-hold-rate", [adjusted_flows ["outlier-ventures-hold-rate"]])

def s_outlier_ventures_hold_rate_updates_swing_order_book (ctx, s, _params):
    if ctx.get ("outlier-ventures-quantity") == None:
        ctx ["outlier-ventures-quantity"] = []
    
    outlier_ventures_quantity = ctx.get ("outlier-ventures-quantity")
    new_val = mul_ls ([_params ["swing-traders"]] + get_new_value (s, "outlier-ventures-hold-rate"))
    append_each (outlier_ventures_quantity, new_val)

def s_outlier_ventures_hold_rate_updates_position_order_book (ctx, s, _params):
    if ctx.get ("outlier-ventures-quantity") == None:
        ctx ["outlier-ventures-quantity"] = []
    
    outlier_ventures_quantity = ctx.get ("outlier-ventures-quantity")
    new_val = mul_ls ([_params ["position-traders"]] + get_new_value (s, "outlier-ventures-hold-rate"))
    append_each (outlier_ventures_quantity, new_val)

def s_outlier_ventures_hold_rate_updates_investor_order_book (ctx, s, _params):
    if ctx.get ("outlier-ventures-quantity") == None:
        ctx ["outlier-ventures-quantity"] = []
    
    outlier_ventures_quantity = ctx.get ("outlier-ventures-quantity")
    new_val = mul_ls ([_params ["investors"]] + get_new_value (s, "outlier-ventures-hold-rate"))
    append_each (outlier_ventures_quantity, new_val)

def s_outlier_ventures_hold_rate_updates_hodler_order_book (ctx, s, _params):
    if ctx.get ("outlier-ventures-quantity") == None:
        ctx ["outlier-ventures-quantity"] = []
    
    outlier_ventures_quantity = ctx.get ("outlier-ventures-quantity")
    new_val = mul_ls ([_params ["hodlers"]] + get_new_value (s, "outlier-ventures-hold-rate"))
    append_each (outlier_ventures_quantity, new_val)

def s_outlier_ventures_pool_value_updates_swing_order_book (ctx, s, _params):
    if ctx.get ("outlier-ventures-price") == None:
        ctx ["outlier-ventures-price"] = []
    
    outlier_ventures_price = ctx.get ("outlier-ventures-price")
    new_val = get_new_value (s, "outlier-ventures-pool-value")
    append_each (outlier_ventures_price, new_val)

def s_outlier_ventures_pool_value_updates_position_order_book (ctx, s, _params):
    if ctx.get ("outlier-ventures-price") == None:
        ctx ["outlier-ventures-price"] = []
    
    outlier_ventures_price = ctx.get ("outlier-ventures-price")
    new_val = get_new_value (s, "outlier-ventures-pool-value")
    append_each (outlier_ventures_price, new_val)

def s_outlier_ventures_pool_value_updates_investor_order_book (ctx, s, _params):
    if ctx.get ("outlier-ventures-price") == None:
        ctx ["outlier-ventures-price"] = []
    
    outlier_ventures_price = ctx.get ("outlier-ventures-price")
    new_val = get_new_value (s, "outlier-ventures-pool-value")
    append_each (outlier_ventures_price, new_val)

def s_outlier_ventures_pool_value_updates_hodler_order_book (ctx, s, _params):
    if ctx.get ("outlier-ventures-price") == None:
        ctx ["outlier-ventures-price"] = []
    
    outlier_ventures_price = ctx.get ("outlier-ventures-price")
    new_val = get_new_value (s, "outlier-ventures-pool-value")
    append_each (outlier_ventures_price, new_val)

def s_adjust_advisors_pool_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "advisors-hold-rate") [0]
    inventory = get_new_value (s, "advisors-pool") [0]
    if flow_val < 0:
        flow_val = 0
    
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["advisors-hold-rate"] = flow_val

def s_reduce_advisors_pool (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "advisors-hold-rate"))
    return "advisors-pool", update_state (s, "advisors-pool", diff_ls (get_new_value (s, "advisors-pool") + red))

def s_clock_updates_advisors_hold_rate (ctx, s, _params):
    if ctx.get ("months") == None:
        ctx ["months"] = []
    
    months = ctx.get ("months")
    new_val = floor_ls (div_ls (get_new_value (s, "clock") + [4]))
    append_each (months, new_val)

def s_commit_advisors_hold_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "advisors-hold-rate", update_state (s, "advisors-hold-rate", [adjusted_flows ["advisors-hold-rate"]])

def s_advisors_hold_rate_updates_swing_order_book (ctx, s, _params):
    if ctx.get ("advisors-quantity") == None:
        ctx ["advisors-quantity"] = []
    
    advisors_quantity = ctx.get ("advisors-quantity")
    new_val = mul_ls ([_params ["swing-traders"]] + get_new_value (s, "advisors-hold-rate"))
    append_each (advisors_quantity, new_val)

def s_advisors_hold_rate_updates_position_order_book (ctx, s, _params):
    if ctx.get ("advisors-quantity") == None:
        ctx ["advisors-quantity"] = []
    
    advisors_quantity = ctx.get ("advisors-quantity")
    new_val = mul_ls ([_params ["position-traders"]] + get_new_value (s, "advisors-hold-rate"))
    append_each (advisors_quantity, new_val)

def s_advisors_hold_rate_updates_investor_order_book (ctx, s, _params):
    if ctx.get ("advisors-quantity") == None:
        ctx ["advisors-quantity"] = []
    
    advisors_quantity = ctx.get ("advisors-quantity")
    new_val = mul_ls ([_params ["investors"]] + get_new_value (s, "advisors-hold-rate"))
    append_each (advisors_quantity, new_val)

def s_advisors_hold_rate_updates_hodler_order_book (ctx, s, _params):
    if ctx.get ("advisors-quantity") == None:
        ctx ["advisors-quantity"] = []
    
    advisors_quantity = ctx.get ("advisors-quantity")
    new_val = mul_ls ([_params ["hodlers"]] + get_new_value (s, "advisors-hold-rate"))
    append_each (advisors_quantity, new_val)

def s_advisors_pool_value_updates_swing_order_book (ctx, s, _params):
    if ctx.get ("advisors-price") == None:
        ctx ["advisors-price"] = []
    
    advisors_price = ctx.get ("advisors-price")
    new_val = get_new_value (s, "advisors-pool-value")
    append_each (advisors_price, new_val)

def s_advisors_pool_value_updates_position_order_book (ctx, s, _params):
    if ctx.get ("advisors-price") == None:
        ctx ["advisors-price"] = []
    
    advisors_price = ctx.get ("advisors-price")
    new_val = get_new_value (s, "advisors-pool-value")
    append_each (advisors_price, new_val)

def s_advisors_pool_value_updates_investor_order_book (ctx, s, _params):
    if ctx.get ("advisors-price") == None:
        ctx ["advisors-price"] = []
    
    advisors_price = ctx.get ("advisors-price")
    new_val = get_new_value (s, "advisors-pool-value")
    append_each (advisors_price, new_val)

def s_advisors_pool_value_updates_hodler_order_book (ctx, s, _params):
    if ctx.get ("advisors-price") == None:
        ctx ["advisors-price"] = []
    
    advisors_price = ctx.get ("advisors-price")
    new_val = get_new_value (s, "advisors-pool-value")
    append_each (advisors_price, new_val)

def s_adjust_partners_pool_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "partners-hold-rate") [0]
    inventory = get_new_value (s, "partners-pool") [0]
    if flow_val < 0:
        flow_val = 0
    
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["partners-hold-rate"] = flow_val

def s_reduce_partners_pool (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "partners-hold-rate"))
    return "partners-pool", update_state (s, "partners-pool", diff_ls (get_new_value (s, "partners-pool") + red))

def s_clock_updates_partners_hold_rate (ctx, s, _params):
    if ctx.get ("months") == None:
        ctx ["months"] = []
    
    months = ctx.get ("months")
    new_val = floor_ls (div_ls (get_new_value (s, "clock") + [4]))
    append_each (months, new_val)

def s_commit_partners_hold_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "partners-hold-rate", update_state (s, "partners-hold-rate", [adjusted_flows ["partners-hold-rate"]])

def s_partners_hold_rate_updates_swing_order_book (ctx, s, _params):
    if ctx.get ("partners-quantity") == None:
        ctx ["partners-quantity"] = []
    
    partners_quantity = ctx.get ("partners-quantity")
    new_val = mul_ls ([_params ["swing-traders"]] + get_new_value (s, "partners-hold-rate"))
    append_each (partners_quantity, new_val)

def s_partners_hold_rate_updates_position_order_book (ctx, s, _params):
    if ctx.get ("partners-quantity") == None:
        ctx ["partners-quantity"] = []
    
    partners_quantity = ctx.get ("partners-quantity")
    new_val = mul_ls ([_params ["position-traders"]] + get_new_value (s, "partners-hold-rate"))
    append_each (partners_quantity, new_val)

def s_partners_hold_rate_updates_investor_order_book (ctx, s, _params):
    if ctx.get ("partners-quantity") == None:
        ctx ["partners-quantity"] = []
    
    partners_quantity = ctx.get ("partners-quantity")
    new_val = mul_ls ([_params ["investors"]] + get_new_value (s, "partners-hold-rate"))
    append_each (partners_quantity, new_val)

def s_partners_hold_rate_updates_hodler_order_book (ctx, s, _params):
    if ctx.get ("partners-quantity") == None:
        ctx ["partners-quantity"] = []
    
    partners_quantity = ctx.get ("partners-quantity")
    new_val = mul_ls ([_params ["hodlers"]] + get_new_value (s, "partners-hold-rate"))
    append_each (partners_quantity, new_val)

def s_partners_pool_value_updates_swing_order_book (ctx, s, _params):
    if ctx.get ("partners-price") == None:
        ctx ["partners-price"] = []
    
    partners_price = ctx.get ("partners-price")
    new_val = get_new_value (s, "partners-pool-value")
    append_each (partners_price, new_val)

def s_partners_pool_value_updates_position_order_book (ctx, s, _params):
    if ctx.get ("partners-price") == None:
        ctx ["partners-price"] = []
    
    partners_price = ctx.get ("partners-price")
    new_val = get_new_value (s, "partners-pool-value")
    append_each (partners_price, new_val)

def s_partners_pool_value_updates_investor_order_book (ctx, s, _params):
    if ctx.get ("partners-price") == None:
        ctx ["partners-price"] = []
    
    partners_price = ctx.get ("partners-price")
    new_val = get_new_value (s, "partners-pool-value")
    append_each (partners_price, new_val)

def s_partners_pool_value_updates_hodler_order_book (ctx, s, _params):
    if ctx.get ("partners-price") == None:
        ctx ["partners-price"] = []
    
    partners_price = ctx.get ("partners-price")
    new_val = get_new_value (s, "partners-pool-value")
    append_each (partners_price, new_val)

def s_adjust_rewards_pool_outflow (s, flow_adjustments):
    flow_list = ["reward-to-held-rate", "rewards-unhold-rate"]
    random.shuffle (flow_list)
    inventory = get_new_value (s, "rewards-pool") [0]
    for f in flow_list:
        flow_val = get_new_value (s, f) [0]
        if flow_val < 0:
            flow_val = 0
        
        if inventory >= flow_val:
            inventory = (inventory - flow_val)
        elif inventory == flow_val:
            inventory = 0
        else:
            flow_val = inventory
            inventory = 0
        
        flow_adjustments [f] = flow_val


def s_cumulate_rewards_pool (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "rewards-hold-rate"))
    return "rewards-pool", update_state (s, "rewards-pool", sum_ls (get_new_value (s, "rewards-pool") + agg))

def s_reduce_rewards_pool (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "reward-to-held-rate") + get_new_value (s, "rewards-unhold-rate"))
    return "rewards-pool", update_state (s, "rewards-pool", diff_ls (get_new_value (s, "rewards-pool") + red))

def s_clock_updates_rewards_hold_rate (ctx, s, _params):
    if ctx.get ("months") == None:
        ctx ["months"] = []
    
    months = ctx.get ("months")
    new_val = floor_ls (div_ls (get_new_value (s, "clock") + [4]))
    append_each (months, new_val)

def s_clock_updates_rewards_unhold_rate (ctx, s, _params):
    if ctx.get ("months") == None:
        ctx ["months"] = []
    
    months = ctx.get ("months")
    new_val = floor_ls (div_ls (get_new_value (s, "clock") + [4]))
    append_each (months, new_val)

def s_token_price_updates_rewards_hold_rate (ctx, s, _params):
    if ctx.get ("price") == None:
        ctx ["price"] = []
    
    price = ctx.get ("price")
    new_val = get_new_value (s, "token-price")
    append_each (price, new_val)

def s_threatslayer_revenue_updates_rewards_hold_rate (ctx, s, _params):
    if ctx.get ("money") == None:
        ctx ["money"] = []
    
    money = ctx.get ("money")
    new_val = diff_ls (get_new_value (s, "threatslayer-revenue") + get_old_value (s, "threatslayer-revenue"))
    append_each (money, new_val)

def s_commit_rewards_hold_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "rewards-hold-rate", update_state (s, "rewards-hold-rate", [adjusted_flows ["rewards-hold-rate"]])

def s_threatslayer_expenses_updates_rewards_unhold_rate (ctx, s, _params):
    if ctx.get ("expenses") == None:
        ctx ["expenses"] = []
    
    expenses = ctx.get ("expenses")
    new_val = get_new_value (s, "threatslayer-expenses")
    append_each (expenses, new_val)

def s_threatslayer_revenue_updates_rewards_unhold_rate (ctx, s, _params):
    if ctx.get ("revenue") == None:
        ctx ["revenue"] = []
    
    revenue = ctx.get ("revenue")
    new_val = get_new_value (s, "threatslayer-revenue")
    append_each (revenue, new_val)

def s_token_price_updates_rewards_unhold_rate (ctx, s, _params):
    if ctx.get ("price") == None:
        ctx ["price"] = []
    
    price = ctx.get ("price")
    new_val = get_new_value (s, "token-price")
    append_each (price, new_val)

def s_commit_rewards_unhold_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "rewards-unhold-rate", update_state (s, "rewards-unhold-rate", [adjusted_flows ["rewards-unhold-rate"]])

def s_change_buyback_amount_updates_rewards_hold_rate (ctx, s, _params):
    if ctx.get ("mul-buyback-amount") == None:
        ctx ["mul-buyback-amount"] = []
    
    mul_buyback_amount = ctx.get ("mul-buyback-amount")
    new_val = (abs_ls (get_new_value (s, "change-buyback-amount")) if gt_ls (abs_ls (get_new_value (s, "change-buyback-amount")) + [0]) [0] else [0])
    append_each (mul_buyback_amount, new_val)

def s_change_sell_amount_updates_rewards_unhold_rate (ctx, s, _params):
    if ctx.get ("mul-sell-amount") == None:
        ctx ["mul-sell-amount"] = []
    
    mul_sell_amount = ctx.get ("mul-sell-amount")
    new_val = (abs_ls (get_new_value (s, "change-sell-amount")) if gt_ls (abs_ls (get_new_value (s, "change-sell-amount")) + [0]) [0] else [0])
    append_each (mul_sell_amount, new_val)

def s_rewards_unhold_rate_updates_threatslayer_investment_rate (ctx, s, _params):
    if ctx.get ("tokens-sold") == None:
        ctx ["tokens-sold"] = []
    
    tokens_sold = ctx.get ("tokens-sold")
    new_val = get_new_value (s, "rewards-unhold-rate")
    append_each (tokens_sold, new_val)

def s_rewards_hold_rate_updates_interlock_self_invest_rate (ctx, s, _params):
    if ctx.get ("tokens-bought") == None:
        ctx ["tokens-bought"] = []
    
    tokens_bought = ctx.get ("tokens-bought")
    new_val = get_new_value (s, "rewards-hold-rate")
    append_each (tokens_bought, new_val)

def s_adjust_foundation_pool_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "foundation-unhold-rate") [0]
    inventory = get_new_value (s, "foundation-pool") [0]
    if flow_val < 0:
        flow_val = 0
    
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["foundation-unhold-rate"] = flow_val

def s_cumulate_foundation_pool (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "foundation-hold-rate"))
    return "foundation-pool", update_state (s, "foundation-pool", sum_ls (get_new_value (s, "foundation-pool") + agg))

def s_reduce_foundation_pool (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "foundation-unhold-rate"))
    return "foundation-pool", update_state (s, "foundation-pool", diff_ls (get_new_value (s, "foundation-pool") + red))

def s_clock_updates_foundation_hold_rate (ctx, s, _params):
    if ctx.get ("months") == None:
        ctx ["months"] = []
    
    months = ctx.get ("months")
    new_val = floor_ls (div_ls (get_new_value (s, "clock") + [4]))
    append_each (months, new_val)

def s_clock_updates_foundation_unhold_rate (ctx, s, _params):
    if ctx.get ("months") == None:
        ctx ["months"] = []
    
    months = ctx.get ("months")
    new_val = floor_ls (div_ls (get_new_value (s, "clock") + [4]))
    append_each (months, new_val)

def s_token_price_updates_foundation_hold_rate (ctx, s, _params):
    if ctx.get ("price") == None:
        ctx ["price"] = []
    
    price = ctx.get ("price")
    new_val = get_new_value (s, "token-price")
    append_each (price, new_val)

def s_threatslayer_revenue_updates_foundation_hold_rate (ctx, s, _params):
    if ctx.get ("money") == None:
        ctx ["money"] = []
    
    money = ctx.get ("money")
    new_val = diff_ls (get_new_value (s, "threatslayer-revenue") + get_old_value (s, "threatslayer-revenue"))
    append_each (money, new_val)

def s_commit_foundation_hold_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "foundation-hold-rate", update_state (s, "foundation-hold-rate", [adjusted_flows ["foundation-hold-rate"]])

def s_threatslayer_expenses_updates_foundation_unhold_rate (ctx, s, _params):
    if ctx.get ("expenses") == None:
        ctx ["expenses"] = []
    
    expenses = ctx.get ("expenses")
    new_val = get_new_value (s, "threatslayer-expenses")
    append_each (expenses, new_val)

def s_threatslayer_revenue_updates_foundation_unhold_rate (ctx, s, _params):
    if ctx.get ("revenue") == None:
        ctx ["revenue"] = []
    
    revenue = ctx.get ("revenue")
    new_val = get_new_value (s, "threatslayer-revenue")
    append_each (revenue, new_val)

def s_token_price_updates_foundation_unhold_rate (ctx, s, _params):
    if ctx.get ("price") == None:
        ctx ["price"] = []
    
    price = ctx.get ("price")
    new_val = get_new_value (s, "token-price")
    append_each (price, new_val)

def s_commit_foundation_unhold_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "foundation-unhold-rate", update_state (s, "foundation-unhold-rate", [adjusted_flows ["foundation-unhold-rate"]])

def s_change_buyback_amount_updates_foundation_hold_rate (ctx, s, _params):
    if ctx.get ("mul-buyback-amount") == None:
        ctx ["mul-buyback-amount"] = []
    
    mul_buyback_amount = ctx.get ("mul-buyback-amount")
    new_val = (abs_ls (get_new_value (s, "change-buyback-amount")) if gt_ls (abs_ls (get_new_value (s, "change-buyback-amount")) + [0]) [0] else [0])
    append_each (mul_buyback_amount, new_val)

def s_change_sell_amount_updates_foundation_unhold_rate (ctx, s, _params):
    if ctx.get ("mul-sell-amount") == None:
        ctx ["mul-sell-amount"] = []
    
    mul_sell_amount = ctx.get ("mul-sell-amount")
    new_val = (abs_ls (get_new_value (s, "change-sell-amount")) if gt_ls (abs_ls (get_new_value (s, "change-sell-amount")) + [0]) [0] else [0])
    append_each (mul_sell_amount, new_val)

def s_foundation_unhold_rate_updates_threatslayer_investment_rate (ctx, s, _params):
    if ctx.get ("tokens-sold") == None:
        ctx ["tokens-sold"] = []
    
    tokens_sold = ctx.get ("tokens-sold")
    new_val = get_new_value (s, "foundation-unhold-rate")
    append_each (tokens_sold, new_val)

def s_foundation_hold_rate_updates_interlock_self_invest_rate (ctx, s, _params):
    if ctx.get ("tokens-bought") == None:
        ctx ["tokens-bought"] = []
    
    tokens_bought = ctx.get ("tokens-bought")
    new_val = get_new_value (s, "foundation-hold-rate")
    append_each (tokens_bought, new_val)

def s_adjust_token_sell_pool_outflow (s, flow_adjustments):
    flow_list = ["token-hold-rate", "foundation-hold-rate", "rewards-hold-rate"]
    random.shuffle (flow_list)
    inventory = get_new_value (s, "token-sell-pool") [0]
    for f in flow_list:
        flow_val = get_new_value (s, f) [0]
        if flow_val < 0:
            flow_val = 0
        
        if inventory >= flow_val:
            inventory = (inventory - flow_val)
        elif inventory == flow_val:
            inventory = 0
        else:
            flow_val = inventory
            inventory = 0
        
        flow_adjustments [f] = flow_val


def s_cumulate_token_sell_pool (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "token-unhold-rate") + get_new_value (s, "foundation-unhold-rate") + get_new_value (s, "rewards-unhold-rate"))
    return "token-sell-pool", update_state (s, "token-sell-pool", sum_ls (get_new_value (s, "token-sell-pool") + agg))

def s_reduce_token_sell_pool (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "token-hold-rate") + get_new_value (s, "foundation-hold-rate") + get_new_value (s, "rewards-hold-rate"))
    return "token-sell-pool", update_state (s, "token-sell-pool", diff_ls (get_new_value (s, "token-sell-pool") + red))

def s_adjust_token_stake_pool_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "token-unstake-rate") [0]
    inventory = get_new_value (s, "token-stake-pool") [0]
    if flow_val < 0:
        flow_val = 0
    
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
        if flow_val < 0:
            flow_val = 0
        
        if inventory >= flow_val:
            inventory = (inventory - flow_val)
        elif inventory == flow_val:
            inventory = 0
        else:
            flow_val = inventory
            inventory = 0
        
        flow_adjustments [f] = flow_val


def s_cumulate_token_hold_pool (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "reward-to-held-rate") + get_new_value (s, "token-unstake-rate") + get_new_value (s, "token-hold-rate") + get_new_value (s, "partners-hold-rate") + get_new_value (s, "advisors-hold-rate") + get_new_value (s, "outlier-ventures-hold-rate") + get_new_value (s, "team-founders-hold-rate") + get_new_value (s, "presale-3-hold-rate") + get_new_value (s, "presale-2-hold-rate") + get_new_value (s, "presale-1-hold-rate") + get_new_value (s, "community-sale-hold-rate"))
    return "token-hold-pool", update_state (s, "token-hold-pool", sum_ls (get_new_value (s, "token-hold-pool") + agg))

def s_reduce_token_hold_pool (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "token-stake-rate") + get_new_value (s, "token-unhold-rate"))
    return "token-hold-pool", update_state (s, "token-hold-pool", diff_ls (get_new_value (s, "token-hold-pool") + red))

def s_commit_token_hold_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "token-hold-rate", update_state (s, "token-hold-rate", [adjusted_flows ["token-hold-rate"]])

def s_commit_token_unhold_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "token-unhold-rate", update_state (s, "token-unhold-rate", [adjusted_flows ["token-unhold-rate"]])

def s_commit_token_stake_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "token-stake-rate", update_state (s, "token-stake-rate", [adjusted_flows ["token-stake-rate"]])

def s_rewards_pool_updates_token_stake_rate (ctx, s, _params):
    if ctx.get ("reward-pool-fullness") == None:
        ctx ["reward-pool-fullness"] = []
    
    reward_pool_fullness = ctx.get ("reward-pool-fullness")
    new_val = ([0] if eq_ls (get_new_value (s, "rewards-pool") + [0]) [0] else [1])
    append_each (reward_pool_fullness, new_val)

def s_rewards_pool_updates_token_unstake_rate (ctx, s, _params):
    if ctx.get ("reward-pool-fullness") == None:
        ctx ["reward-pool-fullness"] = []
    
    reward_pool_fullness = ctx.get ("reward-pool-fullness")
    new_val = ([0] if eq_ls (get_old_value (s, "rewards-pool") + [0]) [0] else [1])
    append_each (reward_pool_fullness, new_val)

def s_staking_enthusiasm_updates_token_stake_rate (ctx, s, _params):
    if ctx.get ("enthusiasm") == None:
        ctx ["enthusiasm"] = []
    
    enthusiasm = ctx.get ("enthusiasm")
    new_val = get_new_value (s, "staking-enthusiasm")
    append_each (enthusiasm, new_val)

def s_token_unstake_rate_updates_heuristic_innovation (ctx, s, _params):
    if ctx.get ("urgency") == None:
        ctx ["urgency"] = []
    
    urgency = ctx.get ("urgency")
    new_val = ([6] if gt_ls (get_new_value (s, "token-unstake-rate") + [0]) [0] else [0])
    append_each (urgency, new_val)

def s_commit_token_unstake_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "token-unstake-rate", update_state (s, "token-unstake-rate", [adjusted_flows ["token-unstake-rate"]])

def s_reward_to_held_rate_updates_reward_rate (ctx, s, _params):
    if ctx.get ("rewards-held") == None:
        ctx ["rewards-held"] = []
    
    rewards_held = ctx.get ("rewards-held")
    new_val = get_new_value (s, "reward-to-held-rate")
    append_each (rewards_held, new_val)

def s_reward_to_held_rate_updates_threatslayer_abandonment_rate (ctx, s, _params):
    if ctx.get ("rewards-held") == None:
        ctx ["rewards-held"] = []
    
    rewards_held = ctx.get ("rewards-held")
    new_val = div_ls (get_old_value (s, "reward-to-held-rate") + max_ls ([1] + get_new_value (s, "reward-to-held-rate")))
    append_each (rewards_held, new_val)

def s_clock_updates_reward_to_held_rate (ctx, s, _params):
    if ctx.get ("months") == None:
        ctx ["months"] = []
    
    months = ctx.get ("months")
    new_val = floor_ls (div_ls (get_new_value (s, "clock") + [4]))
    append_each (months, new_val)

def s_commit_reward_to_held_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "reward-to-held-rate", update_state (s, "reward-to-held-rate", [adjusted_flows ["reward-to-held-rate"]])

def s_reward_price_updates_swing_order_book (ctx, s, _params):
    if ctx.get ("reward-price") == None:
        ctx ["reward-price"] = []
    
    reward_price = ctx.get ("reward-price")
    new_val = get_new_value (s, "reward-price")
    append_each (reward_price, new_val)

def s_reward_to_held_rate_updates_swing_order_book (ctx, s, _params):
    if ctx.get ("reward-quantity") == None:
        ctx ["reward-quantity"] = []
    
    reward_quantity = ctx.get ("reward-quantity")
    new_val = mul_ls ([_params ["swing-traders"]] + get_new_value (s, "reward-to-held-rate"))
    append_each (reward_quantity, new_val)

def s_reward_price_updates_position_order_book (ctx, s, _params):
    if ctx.get ("reward-price") == None:
        ctx ["reward-price"] = []
    
    reward_price = ctx.get ("reward-price")
    new_val = get_new_value (s, "reward-price")
    append_each (reward_price, new_val)

def s_reward_to_held_rate_updates_position_order_book (ctx, s, _params):
    if ctx.get ("reward-quantity") == None:
        ctx ["reward-quantity"] = []
    
    reward_quantity = ctx.get ("reward-quantity")
    new_val = mul_ls ([_params ["position-traders"]] + get_new_value (s, "reward-to-held-rate"))
    append_each (reward_quantity, new_val)

def s_reward_price_updates_investor_order_book (ctx, s, _params):
    if ctx.get ("reward-price") == None:
        ctx ["reward-price"] = []
    
    reward_price = ctx.get ("reward-price")
    new_val = get_new_value (s, "reward-price")
    append_each (reward_price, new_val)

def s_reward_to_held_rate_updates_investor_order_book (ctx, s, _params):
    if ctx.get ("reward-quantity") == None:
        ctx ["reward-quantity"] = []
    
    reward_quantity = ctx.get ("reward-quantity")
    new_val = mul_ls ([_params ["investors"]] + get_new_value (s, "reward-to-held-rate"))
    append_each (reward_quantity, new_val)

def s_reward_price_updates_hodler_order_book (ctx, s, _params):
    if ctx.get ("reward-price") == None:
        ctx ["reward-price"] = []
    
    reward_price = ctx.get ("reward-price")
    new_val = get_new_value (s, "reward-price")
    append_each (reward_price, new_val)

def s_reward_to_held_rate_updates_hodler_order_book (ctx, s, _params):
    if ctx.get ("reward-quantity") == None:
        ctx ["reward-quantity"] = []
    
    reward_quantity = ctx.get ("reward-quantity")
    new_val = mul_ls ([_params ["hodlers"]] + get_new_value (s, "reward-to-held-rate"))
    append_each (reward_quantity, new_val)

def s_adjust_money_mint_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "money-mint-rate") [0]
    inventory = get_new_value (s, "money-mint") [0]
    if flow_val < 0:
        flow_val = 0
    
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
        if flow_val < 0:
            flow_val = 0
        
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
        if flow_val < 0:
            flow_val = 0
        
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
    flow_list = ["threatslayer-investment-rate", "intr-divest-rate"]
    random.shuffle (flow_list)
    inventory = get_new_value (s, "intr-investments") [0]
    for f in flow_list:
        flow_val = get_new_value (s, f) [0]
        if flow_val < 0:
            flow_val = 0
        
        if inventory >= flow_val:
            inventory = (inventory - flow_val)
        elif inventory == flow_val:
            inventory = 0
        else:
            flow_val = inventory
            inventory = 0
        
        flow_adjustments [f] = flow_val


def s_cumulate_intr_investments (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "interlock-self-invest-rate") + get_new_value (s, "intr-invest-rate"))
    return "intr-investments", update_state (s, "intr-investments", sum_ls (get_new_value (s, "intr-investments") + agg))

def s_reduce_intr_investments (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "threatslayer-investment-rate") + get_new_value (s, "intr-divest-rate"))
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

def s_token_price_updates_threatslayer_investment_rate (ctx, s, _params):
    if ctx.get ("price") == None:
        ctx ["price"] = []
    
    price = ctx.get ("price")
    new_val = get_new_value (s, "token-price")
    append_each (price, new_val)

def s_commit_threatslayer_investment_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "threatslayer-investment-rate", update_state (s, "threatslayer-investment-rate", [adjusted_flows ["threatslayer-investment-rate"]])

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

def s_threatslayer_expenses_updates_threatslayer_lookup_price (ctx, s, _params):
    if ctx.get ("expenses") == None:
        ctx ["expenses"] = []
    
    expenses = ctx.get ("expenses")
    new_val = get_new_value (s, "threatslayer-expenses")
    append_each (expenses, new_val)

def s_token_price_updates_interlock_self_invest_rate (ctx, s, _params):
    if ctx.get ("price") == None:
        ctx ["price"] = []
    
    price = ctx.get ("price")
    new_val = get_new_value (s, "token-price")
    append_each (price, new_val)

def s_threatslayer_expenses_updates_threatslayer_upkeep_rate (ctx, s, _params):
    if ctx.get ("expenses") == None:
        ctx ["expenses"] = []
    
    expenses = ctx.get ("expenses")
    new_val = get_new_value (s, "threatslayer-expenses")
    append_each (expenses, new_val)

def s_threatslayer_lookup_price_updates_threatslayer_share_rate (ctx, s, _params):
    if ctx.get ("lookup-price") == None:
        ctx ["lookup-price"] = []
    
    lookup_price = ctx.get ("lookup-price")
    new_val = get_new_value (s, "threatslayer-lookup-price")
    append_each (lookup_price, new_val)

def s_threatslayer_lookup_price_updates_intr_invest_rate (ctx, s, _params):
    if ctx.get ("lookup-price") == None:
        ctx ["lookup-price"] = []
    
    lookup_price = ctx.get ("lookup-price")
    new_val = get_new_value (s, "threatslayer-lookup-price")
    append_each (lookup_price, new_val)

def s_token_price_updates_intr_invest_rate (ctx, s, _params):
    if ctx.get ("price-delta-pct") == None:
        ctx ["price-delta-pct"] = []
    
    price_delta_pct = ctx.get ("price-delta-pct")
    new_val = div_ls (get_new_value (s, "token-price") + get_old_value (s, "token-price"))
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

def s_stake_yield_updates_reward_to_held_rate (ctx, s, _params):
    if ctx.get ("stake-yield") == None:
        ctx ["stake-yield"] = []
    
    stake_yield = ctx.get ("stake-yield")
    new_val = mul_ls (get_new_value (s, "token-unstake-rate") + get_new_value (s, "stake-yield"))
    append_each (stake_yield, new_val)

def s_adjust_potential_page_visits_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "page-visit-rate") [0]
    inventory = get_new_value (s, "potential-page-visits") [0]
    if flow_val < 0:
        flow_val = 0
    
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
    if flow_val < 0:
        flow_val = 0
    
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

def s_adjust_threatslayer_lookups_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "grey-area-entity-rate") [0]
    inventory = get_new_value (s, "threatslayer-lookups") [0]
    if flow_val < 0:
        flow_val = 0
    
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["grey-area-entity-rate"] = flow_val

def s_cumulate_threatslayer_lookups (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "threatslayer-lookup-rate"))
    return "threatslayer-lookups", update_state (s, "threatslayer-lookups", sum_ls (get_new_value (s, "threatslayer-lookups") + agg))

def s_reduce_threatslayer_lookups (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "grey-area-entity-rate"))
    return "threatslayer-lookups", update_state (s, "threatslayer-lookups", diff_ls (get_new_value (s, "threatslayer-lookups") + red))

def s_adjust_potential_threatslayer_lookups_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "threatslayer-lookup-rate") [0]
    inventory = get_new_value (s, "potential-threatslayer-lookups") [0]
    if flow_val < 0:
        flow_val = 0
    
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["threatslayer-lookup-rate"] = flow_val

def s_reduce_potential_threatslayer_lookups (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "threatslayer-lookup-rate"))
    return "potential-threatslayer-lookups", update_state (s, "potential-threatslayer-lookups", diff_ls (get_new_value (s, "potential-threatslayer-lookups") + red))

def s_adjust_browsing_data_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "threatslayer-share-rate") [0]
    inventory = get_new_value (s, "browsing-data") [0]
    if flow_val < 0:
        flow_val = 0
    
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["threatslayer-share-rate"] = flow_val

def s_reduce_browsing_data (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "threatslayer-share-rate"))
    return "browsing-data", update_state (s, "browsing-data", diff_ls (get_new_value (s, "browsing-data") + red))

def s_cumulate_threatslayer_data_shared (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "threatslayer-share-rate"))
    return "threatslayer-data-shared", update_state (s, "threatslayer-data-shared", sum_ls (get_new_value (s, "threatslayer-data-shared") + agg))

def s_adjust_threatslayer_revenue_outflow (s, flow_adjustments):
    flow_list = ["threatslayer-upkeep-rate", "interlock-self-invest-rate"]
    random.shuffle (flow_list)
    inventory = get_new_value (s, "threatslayer-revenue") [0]
    for f in flow_list:
        flow_val = get_new_value (s, f) [0]
        if flow_val < 0:
            flow_val = 0
        
        if inventory >= flow_val:
            inventory = (inventory - flow_val)
        elif inventory == flow_val:
            inventory = 0
        else:
            flow_val = inventory
            inventory = 0
        
        flow_adjustments [f] = flow_val


def s_cumulate_threatslayer_revenue (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "threatslayer-revenue-rate") + get_new_value (s, "threatslayer-investment-rate"))
    return "threatslayer-revenue", update_state (s, "threatslayer-revenue", sum_ls (get_new_value (s, "threatslayer-revenue") + agg))

def s_reduce_threatslayer_revenue (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "threatslayer-upkeep-rate") + get_new_value (s, "interlock-self-invest-rate"))
    return "threatslayer-revenue", update_state (s, "threatslayer-revenue", diff_ls (get_new_value (s, "threatslayer-revenue") + red))

def s_cumulate_threatslayer_upkeep (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "threatslayer-upkeep-rate"))
    return "threatslayer-upkeep", update_state (s, "threatslayer-upkeep", sum_ls (get_new_value (s, "threatslayer-upkeep") + agg))

def s_adjust_data_buyer_money_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "threatslayer-revenue-rate") [0]
    inventory = get_new_value (s, "data-buyer-money") [0]
    if flow_val < 0:
        flow_val = 0
    
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["threatslayer-revenue-rate"] = flow_val

def s_reduce_data_buyer_money (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "threatslayer-revenue-rate"))
    return "data-buyer-money", update_state (s, "data-buyer-money", diff_ls (get_new_value (s, "data-buyer-money") + red))

def s_adjust_browser_users_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "threatslayer-adoption-rate") [0]
    inventory = get_new_value (s, "browser-users") [0]
    if flow_val < 0:
        flow_val = 0
    
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["threatslayer-adoption-rate"] = flow_val

def s_cumulate_browser_users (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "threatslayer-abandonment-rate"))
    return "browser-users", update_state (s, "browser-users", sum_ls (get_new_value (s, "browser-users") + agg))

def s_reduce_browser_users (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "threatslayer-adoption-rate"))
    return "browser-users", update_state (s, "browser-users", diff_ls (get_new_value (s, "browser-users") + red))

def s_adjust_threatslayer_users_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "threatslayer-abandonment-rate") [0]
    inventory = get_new_value (s, "threatslayer-users") [0]
    if flow_val < 0:
        flow_val = 0
    
    if flow_val > inventory:
        flow_val = inventory
        inventory = 0
    
    flow_adjustments ["threatslayer-abandonment-rate"] = flow_val

def s_cumulate_threatslayer_users (_params, substep, sH, s, _input, **kwargs):
    agg = sum_ls (get_new_value (s, "threatslayer-adoption-rate"))
    return "threatslayer-users", update_state (s, "threatslayer-users", sum_ls (get_new_value (s, "threatslayer-users") + agg))

def s_reduce_threatslayer_users (_params, substep, sH, s, _input, **kwargs):
    red = sum_ls (get_new_value (s, "threatslayer-abandonment-rate"))
    return "threatslayer-users", update_state (s, "threatslayer-users", diff_ls (get_new_value (s, "threatslayer-users") + red))

def s_adjust_grey_area_entities_outflow (s, flow_adjustments):
    flow_val = get_new_value (s, "resolution-rate") [0]
    inventory = get_new_value (s, "grey-area-entities") [0]
    if flow_val < 0:
        flow_val = 0
    
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
    if flow_val < 0:
        flow_val = 0
    
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
    if flow_val < 0:
        flow_val = 0
    
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
    if flow_val < 0:
        flow_val = 0
    
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

def s_token_price_updates_stim_token_price_delta (ctx, s, _params):
    if ctx.get ("stim") == None:
        ctx ["stim"] = []
    
    stim = ctx.get ("stim")
    new_val = div_ls (diff_ls (get_new_value (s, "token-price") + get_old_value (s, "token-price")) + get_old_value (s, "token-price"))
    append_each (stim, new_val)

def s_threatslayer_users_updates_stim_anti_user_goal_progress (ctx, s, _params):
    if ctx.get ("stim") == None:
        ctx ["stim"] = []
    
    stim = ctx.get ("stim")
    new_val = div_ls (diff_ls ([_params ["max-users"]] + get_new_value (s, "threatslayer-users")) + [_params ["max-users"]])
    append_each (stim, new_val)

def s_heuristic_contradictions_updates_stim_contradiction_rate (ctx, s, _params):
    if ctx.get ("stim") == None:
        ctx ["stim"] = []
    
    stim = ctx.get ("stim")
    new_val = max_ls ([0] + div_ls (diff_ls (get_new_value (s, "heuristic-contradictions") + [const_ideal_contradictions]) + diff_ls ([const_critical_contradictions] + [const_ideal_contradictions])))
    append_each (stim, new_val)

def s_change_urgency_updates_heuristic_innovation (ctx, s, _params):
    if ctx.get ("urgency") == None:
        ctx ["urgency"] = []
    
    urgency = ctx.get ("urgency")
    new_val = div_ls (get_new_value (s, "change-urgency") + [0.25])
    append_each (urgency, new_val)

def s_change_max_stake_updates_max_stake (ctx, s, _params):
    if ctx.get ("mul-max-stake") == None:
        ctx ["mul-max-stake"] = []
    
    mul_max_stake = ctx.get ("mul-max-stake")
    new_val = (mul_ls (get_new_value (s, "change-max-stake") + [500]) if gt_ls (get_new_value (s, "change-max-stake") + [0]) [0] else [0])
    append_each (mul_max_stake, new_val)

def s_change_stake_yield_updates_stake_yield (ctx, s, _params):
    if ctx.get ("mul-stake-yield") == None:
        ctx ["mul-stake-yield"] = []
    
    mul_stake_yield = ctx.get ("mul-stake-yield")
    new_val = (sum_ls ([1] + get_new_value (s, "change-stake-yield")) if gt_ls (get_new_value (s, "change-stake-yield") + [0]) [0] else [0])
    append_each (mul_stake_yield, new_val)

def s_change_lookup_fee_updates_threatslayer_lookup_price (ctx, s, _params):
    if ctx.get ("mul-lookup-fee") == None:
        ctx ["mul-lookup-fee"] = []
    
    mul_lookup_fee = ctx.get ("mul-lookup-fee")
    new_val = (div_ls (mul_ls (get_new_value (s, "change-lookup-fee") + [3]) + [10000]) if gt_ls (get_new_value (s, "change-lookup-fee") + [0]) [0] else [0])
    append_each (mul_lookup_fee, new_val)

def s_change_user_fee_updates_threatslayer_lookup_price (ctx, s, _params):
    if ctx.get ("mul-user-fee") == None:
        ctx ["mul-user-fee"] = []
    
    mul_user_fee = ctx.get ("mul-user-fee")
    new_val = (mul_ls (get_new_value (s, "change-user-fee") + [3]) if gt_ls (get_new_value (s, "change-user-fee") + [0]) [0] else [0])
    append_each (mul_user_fee, new_val)

def s_change_reward_amount_updates_reward_to_held_rate (ctx, s, _params):
    if ctx.get ("mul-reward-rate") == None:
        ctx ["mul-reward-rate"] = []
    
    mul_reward_rate = ctx.get ("mul-reward-rate")
    new_val = get_new_value (s, "change-reward-amount")
    append_each (mul_reward_rate, new_val)

def s_threatslayer_lookup_price_updates_reward_rate (ctx, s, _params):
    if ctx.get ("lookup-fees") == None:
        ctx ["lookup-fees"] = []
    
    lookup_fees = ctx.get ("lookup-fees")
    new_val = get_new_value (s, "threatslayer-lookup-price")
    append_each (lookup_fees, new_val)

def s_threatslayer_users_updates_reward_rate (ctx, s, _params):
    if ctx.get ("users") == None:
        ctx ["users"] = []
    
    users = ctx.get ("users")
    new_val = get_new_value (s, "threatslayer-users")
    append_each (users, new_val)

def s_reward_rate_updates_growth_level (ctx, s, _params):
    if ctx.get ("reward-rate-delta") == None:
        ctx ["reward-rate-delta"] = []
    
    reward_rate_delta = ctx.get ("reward-rate-delta")
    new_val = diff_ls (get_new_value (s, "reward-rate") + get_old_value (s, "reward-rate"))
    append_each (reward_rate_delta, new_val)

def s_growth_level_updates_threatslayer_adoption_rate (ctx, s, _params):
    if ctx.get ("growth") == None:
        ctx ["growth"] = []
    
    growth = ctx.get ("growth")
    new_val = get_new_value (s, "growth-level")
    append_each (growth, new_val)

def s_threatslayer_users_updates_threatslayer_adoption_rate (ctx, s, _params):
    if ctx.get ("users") == None:
        ctx ["users"] = []
    
    users = ctx.get ("users")
    new_val = get_new_value (s, "threatslayer-users")
    append_each (users, new_val)

def s_threatslayer_users_updates_threatslayer_abandonment_rate (ctx, s, _params):
    if ctx.get ("users") == None:
        ctx ["users"] = []
    
    users = ctx.get ("users")
    new_val = get_new_value (s, "threatslayer-users")
    append_each (users, new_val)

def s_commit_threatslayer_adoption_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "threatslayer-adoption-rate", update_state (s, "threatslayer-adoption-rate", [adjusted_flows ["threatslayer-adoption-rate"]])

def s_commit_threatslayer_abandonment_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "threatslayer-abandonment-rate", update_state (s, "threatslayer-abandonment-rate", [adjusted_flows ["threatslayer-abandonment-rate"]])

def s_commit_threatslayer_lookup_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "threatslayer-lookup-rate", update_state (s, "threatslayer-lookup-rate", [adjusted_flows ["threatslayer-lookup-rate"]])

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

def s_commit_threatslayer_share_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "threatslayer-share-rate", update_state (s, "threatslayer-share-rate", [adjusted_flows ["threatslayer-share-rate"]])

def s_commit_threatslayer_revenue_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "threatslayer-revenue-rate", update_state (s, "threatslayer-revenue-rate", [adjusted_flows ["threatslayer-revenue-rate"]])

def s_threatslayer_data_shared_updates_threatslayer_revenue_rate (ctx, s, _params):
    if ctx.get ("shared") == None:
        ctx ["shared"] = []
    
    shared = ctx.get ("shared")
    new_val = diff_ls (get_new_value (s, "threatslayer-data-shared") + get_old_value (s, "threatslayer-data-shared"))
    append_each (shared, new_val)

def s_commit_interlock_self_invest_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "interlock-self-invest-rate", update_state (s, "interlock-self-invest-rate", [adjusted_flows ["interlock-self-invest-rate"]])

def s_commit_threatslayer_upkeep_rate (_params, substep, sH, s, _input, **kwargs):
    adjusted_flows = s.get ("flow-adjustments")
    return "threatslayer-upkeep-rate", update_state (s, "threatslayer-upkeep-rate", [adjusted_flows ["threatslayer-upkeep-rate"]])

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

def s_foundation_pool_updates_fitness (ctx, s, _params):
    if ctx.get ("assets") == None:
        ctx ["assets"] = []
    
    assets = ctx.get ("assets")
    new_val = get_new_value (s, "foundation-pool")
    append_each (assets, new_val)

def s_threatslayer_users_updates_fitness (ctx, s, _params):
    if ctx.get ("users") == None:
        ctx ["users"] = []
    
    users = ctx.get ("users")
    new_val = get_new_value (s, "threatslayer-users")
    append_each (users, new_val)

def s_threatslayer_revenue_updates_fitness (ctx, s, _params):
    if ctx.get ("revenue") == None:
        ctx ["revenue"] = []
    
    revenue = ctx.get ("revenue")
    new_val = max_ls ([1] + get_new_value (s, "threatslayer-revenue"))
    append_each (revenue, new_val)

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

def s_threatslayer_users_updates_scam_page_success_rate (ctx, s, _params):
    if ctx.get ("user-share") == None:
        ctx ["user-share"] = []
    
    user_share = ctx.get ("user-share")
    new_val = div_ls (get_new_value (s, "threatslayer-users") + get_new_value (s, "browser-users"))
    append_each (user_share, new_val)

def s_threatslayer_users_updates_threatslayer_lookup_price (ctx, s, _params):
    if ctx.get ("users") == None:
        ctx ["users"] = []
    
    users = ctx.get ("users")
    new_val = get_new_value (s, "threatslayer-users")
    append_each (users, new_val)

def s_page_visit_rate_updates_threatslayer_lookup_rate (ctx, s, _params):
    if ctx.get ("pages-visited") == None:
        ctx ["pages-visited"] = []
    
    pages_visited = ctx.get ("pages-visited")
    new_val = get_new_value (s, "page-visit-rate")
    append_each (pages_visited, new_val)

def s_threatslayer_users_updates_threatslayer_lookup_rate (ctx, s, _params):
    if ctx.get ("user-share") == None:
        ctx ["user-share"] = []
    
    user_share = ctx.get ("user-share")
    new_val = div_ls (get_new_value (s, "threatslayer-users") + get_new_value (s, "browser-users"))
    append_each (user_share, new_val)

def s_threatslayer_data_shared_updates_reward_to_held_rate (ctx, s, _params):
    if ctx.get ("shared") == None:
        ctx ["shared"] = []
    
    shared = ctx.get ("shared")
    new_val = diff_ls (get_new_value (s, "threatslayer-data-shared") + get_old_value (s, "threatslayer-data-shared"))
    append_each (shared, new_val)

def s_threatslayer_lookup_rate_updates_threatslayer_lookup_price (ctx, s, _params):
    if ctx.get ("lookups") == None:
        ctx ["lookups"] = []
    
    lookups = ctx.get ("lookups")
    new_val = get_new_value (s, "threatslayer-lookup-rate")
    append_each (lookups, new_val)

def s_threatslayer_lookup_rate_updates_threatslayer_share_rate (ctx, s, _params):
    if ctx.get ("lookups") == None:
        ctx ["lookups"] = []
    
    lookups = ctx.get ("lookups")
    new_val = get_new_value (s, "threatslayer-lookup-rate")
    append_each (lookups, new_val)

def s_scam_page_success_rate_updates_scammer_innovation (ctx, s, _params):
    if ctx.get ("urgency") == None:
        ctx ["urgency"] = []
    
    urgency = ctx.get ("urgency")
    new_val = ([1] if lt_ls (div_ls (get_new_value (s, "scam-page-success-rate") + get_old_value (s, "scam-page-success-rate")) + [0.9]) [0] else [0])
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

def s_heuristic_contradictions_updates_threatslayer_abandonment_rate (ctx, s, _params):
    if ctx.get ("contradiction-rate") == None:
        ctx ["contradiction-rate"] = []
    
    contradiction_rate = ctx.get ("contradiction-rate")
    new_val = get_new_value (s, "heuristic-contradictions")
    append_each (contradiction_rate, new_val)

def s_heuristic_contradictions_updates_contradiction_loss (ctx, s, _params):
    if ctx.get ("contradiction-rate") == None:
        ctx ["contradiction-rate"] = []
    
    contradiction_rate = ctx.get ("contradiction-rate")
    new_val = get_new_value (s, "heuristic-contradictions")
    append_each (contradiction_rate, new_val)

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

def s_heuristic_innovation_updates_threatslayer_expenses (ctx, s, _params):
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
            return self.val [0] >= cval
        else:
            return self.val >= cval
        




class GreaterThanEq:
    def __init__ (self, val):
        self.val = val


    def match (self, cval):
        if isinstance (self.val, list):
            return self.val [0] <= cval
        else:
            return self.val <= cval
        




class LessThan:
    def __init__ (self, val):
        self.val = val


    def match (self, cval):
        if isinstance (self.val, list):
            return self.val [0] > cval
        else:
            return self.val > cval
        




class GreaterThan:
    def __init__ (self, val):
        self.val = val


    def match (self, cval):
        if isinstance (self.val, list):
            return self.val [0] < cval
        else:
            return self.val < cval
        




class Aggregation:
    agg_stats = {}
    def __init__ (self, schema, agg, base=0, min_mag=0, max_mag=0, step=0):
        self.schema = schema
        self.agg = agg
        self.root = {}
        self.sub_aggs = {}
        self.base = base
        self.min_mag = min_mag
        self.max_mag = max_mag
        self.step = step


    def def_sub_agg (self, name, matches):
        self.sub_aggs [name] = agg_rows_range_new (matches, self)
        return self


    def agg_dict_walk (self, hasht, func, depth, tup):
        for k in hasht:
            val = hasht [k]
            if isinstance (val, dict):
                self.agg_dict_walk (val, func, depth, (tup + (k,)))
            else:
                func ((tup + (k, val)))
            



    def agg_dict_walk_filt (self, hasht, func, depth, tup, tuple_matches):
        for k in hasht:
            for matches in tuple_matches:
                m = matches [depth]
                if m.match (k):
                    val = hasht [k]
                    if isinstance (val, dict):
                        self.agg_dict_walk_filt (val, func, (depth + 1), (tup + (k,)), tuple_matches)
                    else:
                        func ((tup + (k, val)))
                    
                






def what_if_contradicts_security_users (what_if, security_users):
    return all_true ([not (what_if == const_base_what_if and security_users == 0.1), not (what_if == const_base_what_if and security_users == 0.2), not (what_if == const_base_what_if and security_users == 0.8), not (what_if == const_base_what_if and security_users == 0.9), not (what_if == const_best_case_greedy and not security_users == 0.9), not (what_if == const_worst_case_greedy and not security_users == 0.1), not (what_if == const_best_case_generous and not security_users == 0.1), not (what_if == const_best_case_x and not security_users == 0.1)])


def what_if_contradicts_free_loaders (what_if, free_loaders):
    return all_true ([not (what_if == const_base_what_if and free_loaders == 0.1), not (what_if == const_base_what_if and free_loaders == 0.2), not (what_if == const_base_what_if and free_loaders == 0.8), not (what_if == const_base_what_if and free_loaders == 0.9), not (what_if == const_best_case_greedy and not free_loaders == 0.1), not (what_if == const_worst_case_greedy and not free_loaders == 0.5), not (what_if == const_best_case_generous and not free_loaders == 0.1), not (what_if == const_best_case_x and not free_loaders == 0.1)])


def what_if_contradicts_minimum_trade_profit (what_if, minimum_trade_profit):
    return all_true ([not (what_if == const_base_what_if and minimum_trade_profit == 0.1), not (what_if == const_base_what_if and minimum_trade_profit == 0.2), not (what_if == const_base_what_if and minimum_trade_profit == 0.15), not (what_if == const_best_case_greedy and not minimum_trade_profit == 0.2), not (what_if == const_worst_case_greedy and not minimum_trade_profit == 0.01), not (what_if == const_best_case_generous and not minimum_trade_profit == 0.2), not (what_if == const_best_case_x and not minimum_trade_profit == 0.2)])


def what_if_contradicts_cover_own_costs (what_if, cover_own_costs):
    return all_true ([not (what_if == const_best_case_greedy and not cover_own_costs == const_no), not (what_if == const_best_case_generous and not cover_own_costs == const_no), not (what_if == const_best_case_x and not cover_own_costs == const_no), not (what_if == const_worst_case_greedy and not cover_own_costs == const_yes), not (what_if == const_worst_case_generous and not cover_own_costs == const_yes)])


def what_if_contradicts_token_valuation (what_if, token_valuation):
    return all_true ([not (what_if == const_base_what_if and token_valuation == const_half_value), not (what_if == const_best_case_greedy and not token_valuation == const_half_value), not (what_if == const_worst_case_greedy and not token_valuation == const_minimal_value), not (what_if == const_best_case_x and not token_valuation == const_half_value)])


def what_if_contradicts_heuristic_innovation_scenario (what_if, heuristic_innovation_scenario):
    return all_true ([not (what_if == const_base_what_if and not heuristic_innovation_scenario == const_holding), not (what_if == const_best_case_greedy and not heuristic_innovation_scenario == const_industrialized), not (what_if == const_worst_case_greedy and not heuristic_innovation_scenario == const_industrialized), not (what_if == const_best_case_generous and not heuristic_innovation_scenario == const_industrialized), not (what_if == const_best_case_x and not heuristic_innovation_scenario == const_industrialized)])


def anchor_contradicts_what_if (anchor, what_if):
    return all_true ([not (anchor == const_anchor and not what_if == const_worst_case_greedy), not (anchor == const_anchor and what_if == const_best_case_x), not (anchor == const_anchor and what_if == const_worst_case_generous), not (anchor == const_anchor and what_if == const_best_case_generous), not (anchor == const_anchor and what_if == const_base_what_if)])


def what_if_contradicts_max_growth (what_if, max_growth):
    return all_true ([not (what_if == const_best_case_greedy and not max_growth == 1.1), not (what_if == const_worst_case_greedy and not max_growth == 1.1)])


def what_if_contradicts_token_reward_sellers (what_if, token_reward_sellers):
    return all_true ([not (what_if == const_base_what_if and token_reward_sellers == 0.1), not (what_if == const_base_what_if and token_reward_sellers == 0.9), not (what_if == const_best_case_greedy and not token_reward_sellers == 0.1), not (what_if == const_worst_case_greedy and not token_reward_sellers == 0.9), not (what_if == const_best_case_generous and not token_reward_sellers == 0.1), not (what_if == const_best_case_x and not token_reward_sellers == 0.1)])


def what_if_contradicts_vesting_ratio (what_if, vesting_ratio):
    return all_true ([not (what_if == const_base_what_if and vesting_ratio == 0.1), not (what_if == const_base_what_if and vesting_ratio == 0.5), not (what_if == const_best_case_greedy and not vesting_ratio == 0.1), not (what_if == const_worst_case_greedy and not vesting_ratio == 0.5), not (what_if == const_best_case_generous and not vesting_ratio == 0.1), not (what_if == const_best_case_x and not vesting_ratio == 0.1)])


def what_if_contradicts_pages_per_user (what_if, pages_per_user):
    return all_true ([not (what_if == const_base_what_if and not pages_per_user == 2700), not (what_if == const_best_case_greedy and not pages_per_user == 2700), not (what_if == const_worst_case_greedy and not pages_per_user == 480), not (what_if == const_best_case_generous and not pages_per_user == 2700), not (what_if == const_best_case_x and not pages_per_user == 2700)])


def what_if_contradicts_uniqueness_rate (what_if, uniqueness_rate):
    return all_true ([not (what_if == const_base_what_if and not uniqueness_rate == 0.058), not (what_if == const_best_case_greedy and not uniqueness_rate == 0.058), not (what_if == const_worst_case_greedy and not uniqueness_rate == 0.058), not (what_if == const_best_case_generous and not uniqueness_rate == 0.058), not (what_if == const_best_case_x and not uniqueness_rate == 0.058)])


def what_if_contradicts_maliciousness_rate (what_if, maliciousness_rate):
    return all_true ([not (what_if == const_base_what_if and not maliciousness_rate == 0.0014), not (what_if == const_best_case_greedy and not maliciousness_rate == 0.0014), not (what_if == const_worst_case_greedy and not maliciousness_rate == 3.0e-4), not (what_if == const_best_case_generous and not maliciousness_rate == 0.0014), not (what_if == const_best_case_x and not maliciousness_rate == 0.0014)])


def what_if_contradicts_data_elements_per_url (what_if, data_elements_per_url):
    return all_true ([not (what_if == const_base_what_if and not data_elements_per_url == 2), not (what_if == const_best_case_greedy and not data_elements_per_url == 3), not (what_if == const_worst_case_greedy and not data_elements_per_url == 1), not (what_if == const_best_case_generous and not data_elements_per_url == 3), not (what_if == const_best_case_x and not data_elements_per_url == 3)])


def what_if_contradicts_wants_unique (what_if, wants_unique):
    return all_true ([not (what_if == const_base_what_if and wants_unique == const_no), not (what_if == const_best_case_greedy and not wants_unique == const_yes), not (what_if == const_worst_case_greedy and not wants_unique == const_yes), not (what_if == const_best_case_generous and not wants_unique == const_yes), not (what_if == const_best_case_x and not wants_unique == const_yes)])


def what_if_contradicts_wants_malicious (what_if, wants_malicious):
    return all_true ([not (what_if == const_base_what_if and wants_malicious == const_no), not (what_if == const_best_case_greedy and not wants_malicious == const_yes), not (what_if == const_worst_case_greedy and not wants_malicious == const_yes), not (what_if == const_best_case_generous and not wants_malicious == const_yes), not (what_if == const_best_case_x and not wants_malicious == const_yes)])


def what_if_contradicts_data_value (what_if, data_value):
    return all_true ([not (what_if == const_base_what_if and data_value == 0.6), not (what_if == const_best_case_greedy and not data_value == 0.6), not (what_if == const_worst_case_greedy and not data_value == 0.1), not (what_if == const_best_case_generous and not data_value == 0.6), not (what_if == const_best_case_x and not data_value == 0.6)])


def what_if_contradicts_max_users (what_if, max_users):
    return all_true ([not (what_if == const_best_case_greedy and not max_users == 1000000.0), not (what_if == const_worst_case_greedy and not max_users == 500000.0)])


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


def agg_rows_range_new (tuple_matches, agg_or_ls):
    if isinstance (agg_or_ls, list):
        agg = agg_or_ls [0]
    else:
        agg = agg_or_ls
    
    ret = Aggregation (agg.schema, agg.agg, agg.base, agg.min_mag, agg.max_mag, agg.step)
    def add_tuple (e):
        tlen = len (e)
        plen = (tlen - 1)
        agg_store (ret, e [:plen], e [plen])


    agg.agg_dict_walk_filt (agg.root, add_tuple, 0, (), tuple_matches)
    return ret


def agg_def_sub_agg (name, agg_or_ls, matches):
    if isinstance (agg_or_ls, list):
        agg = agg_or_ls [0]
    else:
        agg = agg_or_ls
    
    return agg.def_sub_agg (name, matches)


def agg_rows_range_ref (name, agg_or_ls):
    if isinstance (agg_or_ls, list):
        agg = agg_or_ls [0]
    else:
        agg = agg_or_ls
    
    ret = agg.sub_aggs [name]
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


def multi_aggregate (agg, multi_keys):
    for keys in multi_keys:
        aggregate (agg, keys)

    return agg


def aggregate (agg, keys):
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
    morph.addVariable ("max-users", [4000.0, 70000.0, 500000.0, 1000000.0, 1.0e7])
    morph.addVariable ("data-value", [0.1, 0.6])
    morph.addVariable ("wants-malicious", [const_yes, const_no])
    morph.addVariable ("wants-unique", [const_yes, const_no])
    morph.addVariable ("data-elements-per-url", [1, 2, 3])
    morph.addVariable ("maliciousness-rate", [0.0014, 3.0e-4])
    morph.addVariable ("uniqueness-rate", [0.025, 0.058])
    morph.addVariable ("pages-per-user", [330, 480, 2700])
    morph.addVariable ("vesting-ratio", [0.1, 0.2, 0.5])
    morph.addVariable ("token-reward-sellers", [0.5, 0.1, 0.9])
    morph.addVariable ("max-growth", [1.05, 1.1, 1.15, 1.2])
    morph.addVariable ("base-yield", [1.01])
    morph.addVariable ("heuristic-innovation-scenario", [const_industrialized, const_leading, const_holding, const_lagging, const_terminal])
    morph.addVariable ("anchor", [const_anchor])
    morph.addVariable ("what-if", [const_base_what_if, const_best_case_greedy, const_best_case_generous, const_best_case_x, const_worst_case_greedy, const_worst_case_generous])
    morph.addVariable ("token-valuation", [const_tenth_value, const_seven_tenths_value, const_minimal_value, const_half_value])
    morph.addVariable ("cover-own-costs", [const_yes, const_no])
    morph.addVariable ("expectation-chain", [const_observed_expectation_chain_id])
    morph.addVariable ("money-growth", [const_observed_money_growth_id])
    morph.addVariable ("minimum-trade-profit", [0.01, 0.05, 0.1, 0.15, 0.2])
    morph.addVariable ("free-loaders", [0.1, 0.2, 0.5, 0.8, 0.9])
    morph.addVariable ("security-users", [0.1, 0.2, 0.5, 0.8, 0.9])
    morph.addVariable ("stim-token-price-delta-change-urgency", [0])
    morph.addVariable ("stim-anti-user-goal-progress-change-urgency", [0])
    morph.addVariable ("stim-contradiction-rate-change-urgency", [0])
    morph.addVariable ("stim-token-price-delta-change-reward-amount", [0])
    morph.addVariable ("stim-anti-user-goal-progress-change-reward-amount", [0])
    morph.addVariable ("stim-contradiction-rate-change-reward-amount", [0])
    morph.addVariable ("stim-token-price-delta-change-sell-amount", [0])
    morph.addVariable ("stim-anti-user-goal-progress-change-sell-amount", [0])
    morph.addVariable ("stim-contradiction-rate-change-sell-amount", [0])
    morph.addVariable ("stim-token-price-delta-change-buyback-amount", [0])
    morph.addVariable ("stim-anti-user-goal-progress-change-buyback-amount", [0])
    morph.addVariable ("stim-contradiction-rate-change-buyback-amount", [0])
    morph.addVariable ("stim-token-price-delta-change-user-fee", [0])
    morph.addVariable ("stim-anti-user-goal-progress-change-user-fee", [0])
    morph.addVariable ("stim-contradiction-rate-change-user-fee", [0])
    morph.addVariable ("stim-token-price-delta-change-lookup-fee", [0])
    morph.addVariable ("stim-anti-user-goal-progress-change-lookup-fee", [0])
    morph.addVariable ("stim-contradiction-rate-change-lookup-fee", [0])
    morph.addVariable ("stim-token-price-delta-change-stake-yield", [0])
    morph.addVariable ("stim-anti-user-goal-progress-change-stake-yield", [0])
    morph.addVariable ("stim-contradiction-rate-change-stake-yield", [0])
    morph.addVariable ("stim-token-price-delta-change-max-stake", [0])
    morph.addVariable ("stim-anti-user-goal-progress-change-max-stake", [0])
    morph.addVariable ("stim-contradiction-rate-change-max-stake", [0])
    morph.addConstraint (what_if_contradicts_security_users, ("what-if", "security-users"))
    morph.addConstraint (what_if_contradicts_free_loaders, ("what-if", "free-loaders"))
    morph.addConstraint (what_if_contradicts_minimum_trade_profit, ("what-if", "minimum-trade-profit"))
    morph.addConstraint (what_if_contradicts_cover_own_costs, ("what-if", "cover-own-costs"))
    morph.addConstraint (what_if_contradicts_token_valuation, ("what-if", "token-valuation"))
    morph.addConstraint (what_if_contradicts_heuristic_innovation_scenario, ("what-if", "heuristic-innovation-scenario"))
    morph.addConstraint (anchor_contradicts_what_if, ("anchor", "what-if"))
    morph.addConstraint (what_if_contradicts_max_growth, ("what-if", "max-growth"))
    morph.addConstraint (what_if_contradicts_token_reward_sellers, ("what-if", "token-reward-sellers"))
    morph.addConstraint (what_if_contradicts_vesting_ratio, ("what-if", "vesting-ratio"))
    morph.addConstraint (what_if_contradicts_pages_per_user, ("what-if", "pages-per-user"))
    morph.addConstraint (what_if_contradicts_uniqueness_rate, ("what-if", "uniqueness-rate"))
    morph.addConstraint (what_if_contradicts_maliciousness_rate, ("what-if", "maliciousness-rate"))
    morph.addConstraint (what_if_contradicts_data_elements_per_url, ("what-if", "data-elements-per-url"))
    morph.addConstraint (what_if_contradicts_wants_unique, ("what-if", "wants-unique"))
    morph.addConstraint (what_if_contradicts_wants_malicious, ("what-if", "wants-malicious"))
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


def mul_pos_ls (ls):
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
                ret_val = ret_val
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
    ret_ls = []
    first = 1
    base = 0
    for n in ls:
        if first == 1:
            if n == 0:
                return [0]
            elif n == 1:
                return [1]
            else:
                first = 0
                base = n
            
        elif first == 0:
            if n == 0:
                return [1]
            else:
                ret_ls.append (math.log (n, base))
            
        

    return ret_ls


def sqrt_ls (ls):
    if len (ls) == 0:
        return []
    
    ret_val = 1
    first = 1
    ret_ls = []
    for n in ls:
        ret_ls.append (math.sqrt (n))

    return ret_ls


def lg2_ls (ls):
    if len (ls) == 0:
        return []
    
    ret_val = 1
    first = 1
    ret_ls = []
    for n in ls:
        ret_ls.append (math.log2 (n))

    return ret_ls


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

    


def push (target, value):
    target.append (value)


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
    s_adjust_threatslayer_revenue_outflow (s, flow_adjustments)
    s_adjust_data_buyer_money_outflow (s, flow_adjustments)
    s_adjust_browsing_data_outflow (s, flow_adjustments)
    s_adjust_grey_area_entities_outflow (s, flow_adjustments)
    s_adjust_threatslayer_lookups_outflow (s, flow_adjustments)
    s_adjust_potential_threatslayer_lookups_outflow (s, flow_adjustments)
    s_adjust_threatslayer_users_outflow (s, flow_adjustments)
    s_adjust_browser_users_outflow (s, flow_adjustments)
    s_adjust_intr_investments_outflow (s, flow_adjustments)
    s_adjust_crypto_investments_outflow (s, flow_adjustments)
    s_adjust_money_mint_outflow (s, flow_adjustments)
    s_adjust_money_supply_outflow (s, flow_adjustments)
    s_adjust_token_stake_pool_outflow (s, flow_adjustments)
    s_adjust_token_hold_pool_outflow (s, flow_adjustments)
    s_adjust_foundation_pool_outflow (s, flow_adjustments)
    s_adjust_rewards_pool_outflow (s, flow_adjustments)
    s_adjust_token_sell_pool_outflow (s, flow_adjustments)
    s_adjust_partners_pool_outflow (s, flow_adjustments)
    s_adjust_advisors_pool_outflow (s, flow_adjustments)
    s_adjust_outlier_ventures_pool_outflow (s, flow_adjustments)
    s_adjust_team_founders_pool_outflow (s, flow_adjustments)
    s_adjust_presale_3_pool_outflow (s, flow_adjustments)
    s_adjust_presale_2_pool_outflow (s, flow_adjustments)
    s_adjust_presale_1_pool_outflow (s, flow_adjustments)
    s_adjust_community_sale_pool_outflow (s, flow_adjustments)
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
const_seven_tenths_value = 0.07
const_minimal_value = 0.01
const_firehose = 1
const_trickle = 0.1
const_halted = 0
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
const_rewards_delay = 0
const_rewards_size = 300000000
const_rewards_period = 48
const_foundation_delay = 1
const_foundation_size = 182597475
const_foundation_period = 84
const_growth_spread = agg_store_records (Aggregation (["rate"], "count"), [[1.025, 32], [1.05, 16], [1.075, 8], [1.1, 3]])
const_critical_contradictions = 0.05
const_ideal_contradictions = 0.007
const_contradiction_loss = agg_store_records (Aggregation (["0.01", "0.02", "0.02"], "count"), [[0.02, 0.03, 0.05], [0.03, 0.04, 0.07], [0.04, 0.05, 0.1], [0.05, 1.1, 0.2]])
def s_update_hodler_order_book (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_reward_to_held_rate_updates_hodler_order_book (ctx, s, _params)
    s_reward_price_updates_hodler_order_book (ctx, s, _params)
    s_partners_pool_value_updates_hodler_order_book (ctx, s, _params)
    s_partners_hold_rate_updates_hodler_order_book (ctx, s, _params)
    s_advisors_pool_value_updates_hodler_order_book (ctx, s, _params)
    s_advisors_hold_rate_updates_hodler_order_book (ctx, s, _params)
    s_outlier_ventures_pool_value_updates_hodler_order_book (ctx, s, _params)
    s_outlier_ventures_hold_rate_updates_hodler_order_book (ctx, s, _params)
    s_team_founders_pool_value_updates_hodler_order_book (ctx, s, _params)
    s_team_founders_hold_rate_updates_hodler_order_book (ctx, s, _params)
    s_presale_3_pool_value_updates_hodler_order_book (ctx, s, _params)
    s_presale_3_hold_rate_updates_hodler_order_book (ctx, s, _params)
    s_presale_2_pool_value_updates_hodler_order_book (ctx, s, _params)
    s_presale_2_hold_rate_updates_hodler_order_book (ctx, s, _params)
    s_presale_1_pool_value_updates_hodler_order_book (ctx, s, _params)
    s_presale_1_hold_rate_updates_hodler_order_book (ctx, s, _params)
    s_community_sale_pool_value_updates_hodler_order_book (ctx, s, _params)
    s_community_sale_hold_rate_updates_hodler_order_book (ctx, s, _params)
    s_token_hold_rate_updates_hodler_order_book (ctx, s, _params)
    s_clock_updates_hodler_order_book (ctx, s, _params)
    s_token_price_updates_hodler_order_book (ctx, s, _params)
    myself = "hodler-order-book"
    hodler_order_book = multi_aggregate (get_new_value (s, "hodler-order-book"), [[ctx.get ("sell-time"), ctx.get ("buy-price"), ctx.get ("quantity")], [ctx.get ("sell-time"), ctx.get ("presale-1-price"), ctx.get ("presale-1-quantity")], [ctx.get ("sell-time"), ctx.get ("presale-2-price"), ctx.get ("presale-2-quantity")], [ctx.get ("sell-time"), ctx.get ("presale-3-price"), ctx.get ("presale-3-quantity")], [ctx.get ("sell-time"), ctx.get ("community-sale-price"), ctx.get ("community-sale-quantity")], [ctx.get ("sell-time"), ctx.get ("team-founders-price"), ctx.get ("team-founders-quantity")], [ctx.get ("sell-time"), ctx.get ("outlier-ventures-price"), ctx.get ("outlier-ventures-quantity")], [ctx.get ("sell-time"), ctx.get ("advisors-price"), ctx.get ("advisors-quantity")], [ctx.get ("sell-time"), ctx.get ("partners-price"), ctx.get ("partners-quantity")], [ctx.get ("sell-time"), ctx.get ("reward-price"), ctx.get ("reward-quantity")]])
    return "hodler-order-book", update_state (s, "hodler-order-book", hodler_order_book)


def s_update_investor_order_book (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_investor_order_book_updates_investor_order_book (ctx, s, _params)
    s_reward_to_held_rate_updates_investor_order_book (ctx, s, _params)
    s_reward_price_updates_investor_order_book (ctx, s, _params)
    s_partners_pool_value_updates_investor_order_book (ctx, s, _params)
    s_partners_hold_rate_updates_investor_order_book (ctx, s, _params)
    s_advisors_pool_value_updates_investor_order_book (ctx, s, _params)
    s_advisors_hold_rate_updates_investor_order_book (ctx, s, _params)
    s_outlier_ventures_pool_value_updates_investor_order_book (ctx, s, _params)
    s_outlier_ventures_hold_rate_updates_investor_order_book (ctx, s, _params)
    s_team_founders_pool_value_updates_investor_order_book (ctx, s, _params)
    s_team_founders_hold_rate_updates_investor_order_book (ctx, s, _params)
    s_presale_3_pool_value_updates_investor_order_book (ctx, s, _params)
    s_presale_3_hold_rate_updates_investor_order_book (ctx, s, _params)
    s_presale_2_pool_value_updates_investor_order_book (ctx, s, _params)
    s_presale_2_hold_rate_updates_investor_order_book (ctx, s, _params)
    s_presale_1_pool_value_updates_investor_order_book (ctx, s, _params)
    s_presale_1_hold_rate_updates_investor_order_book (ctx, s, _params)
    s_community_sale_pool_value_updates_investor_order_book (ctx, s, _params)
    s_community_sale_hold_rate_updates_investor_order_book (ctx, s, _params)
    s_token_hold_rate_updates_investor_order_book (ctx, s, _params)
    s_clock_updates_investor_order_book (ctx, s, _params)
    s_token_price_updates_investor_order_book (ctx, s, _params)
    myself = "investor-order-book"
    investor_order_book = multi_aggregate (set_diff_agg (get_new_value (s, "investor-order-book"), ctx.get ("removable")), [[ctx.get ("sell-time"), ctx.get ("buy-price"), ctx.get ("quantity")], [ctx.get ("sell-time"), ctx.get ("presale-1-price"), ctx.get ("presale-1-quantity")], [ctx.get ("sell-time"), ctx.get ("presale-2-price"), ctx.get ("presale-2-quantity")], [ctx.get ("sell-time"), ctx.get ("presale-3-price"), ctx.get ("presale-3-quantity")], [ctx.get ("sell-time"), ctx.get ("community-sale-price"), ctx.get ("community-sale-quantity")], [ctx.get ("sell-time"), ctx.get ("team-founders-price"), ctx.get ("team-founders-quantity")], [ctx.get ("sell-time"), ctx.get ("outlier-ventures-price"), ctx.get ("outlier-ventures-quantity")], [ctx.get ("sell-time"), ctx.get ("advisors-price"), ctx.get ("advisors-quantity")], [ctx.get ("sell-time"), ctx.get ("partners-price"), ctx.get ("partners-quantity")], [ctx.get ("sell-time"), ctx.get ("reward-price"), ctx.get ("reward-quantity")]])
    return "investor-order-book", update_state (s, "investor-order-book", investor_order_book)


def s_update_position_order_book (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_position_order_book_updates_position_order_book (ctx, s, _params)
    s_reward_to_held_rate_updates_position_order_book (ctx, s, _params)
    s_reward_price_updates_position_order_book (ctx, s, _params)
    s_partners_pool_value_updates_position_order_book (ctx, s, _params)
    s_partners_hold_rate_updates_position_order_book (ctx, s, _params)
    s_advisors_pool_value_updates_position_order_book (ctx, s, _params)
    s_advisors_hold_rate_updates_position_order_book (ctx, s, _params)
    s_outlier_ventures_pool_value_updates_position_order_book (ctx, s, _params)
    s_outlier_ventures_hold_rate_updates_position_order_book (ctx, s, _params)
    s_team_founders_pool_value_updates_position_order_book (ctx, s, _params)
    s_team_founders_hold_rate_updates_position_order_book (ctx, s, _params)
    s_presale_3_pool_value_updates_position_order_book (ctx, s, _params)
    s_presale_3_hold_rate_updates_position_order_book (ctx, s, _params)
    s_presale_2_pool_value_updates_position_order_book (ctx, s, _params)
    s_presale_2_hold_rate_updates_position_order_book (ctx, s, _params)
    s_presale_1_pool_value_updates_position_order_book (ctx, s, _params)
    s_presale_1_hold_rate_updates_position_order_book (ctx, s, _params)
    s_community_sale_pool_value_updates_position_order_book (ctx, s, _params)
    s_community_sale_hold_rate_updates_position_order_book (ctx, s, _params)
    s_token_hold_rate_updates_position_order_book (ctx, s, _params)
    s_clock_updates_position_order_book (ctx, s, _params)
    s_token_price_updates_position_order_book (ctx, s, _params)
    myself = "position-order-book"
    position_order_book = multi_aggregate (set_diff_agg (get_new_value (s, "position-order-book"), ctx.get ("removable")), [[ctx.get ("sell-time"), ctx.get ("buy-price"), ctx.get ("quantity")], [ctx.get ("sell-time"), ctx.get ("presale-1-price"), ctx.get ("presale-1-quantity")], [ctx.get ("sell-time"), ctx.get ("presale-2-price"), ctx.get ("presale-2-quantity")], [ctx.get ("sell-time"), ctx.get ("presale-3-price"), ctx.get ("presale-3-quantity")], [ctx.get ("sell-time"), ctx.get ("community-sale-price"), ctx.get ("community-sale-quantity")], [ctx.get ("sell-time"), ctx.get ("team-founders-price"), ctx.get ("team-founders-quantity")], [ctx.get ("sell-time"), ctx.get ("outlier-ventures-price"), ctx.get ("outlier-ventures-quantity")], [ctx.get ("sell-time"), ctx.get ("advisors-price"), ctx.get ("advisors-quantity")], [ctx.get ("sell-time"), ctx.get ("partners-price"), ctx.get ("partners-quantity")], [ctx.get ("sell-time"), ctx.get ("reward-price"), ctx.get ("reward-quantity")]])
    return "position-order-book", update_state (s, "position-order-book", position_order_book)


def s_update_swing_order_book (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_swing_order_book_updates_swing_order_book (ctx, s, _params)
    s_reward_to_held_rate_updates_swing_order_book (ctx, s, _params)
    s_reward_price_updates_swing_order_book (ctx, s, _params)
    s_partners_pool_value_updates_swing_order_book (ctx, s, _params)
    s_partners_hold_rate_updates_swing_order_book (ctx, s, _params)
    s_advisors_pool_value_updates_swing_order_book (ctx, s, _params)
    s_advisors_hold_rate_updates_swing_order_book (ctx, s, _params)
    s_outlier_ventures_pool_value_updates_swing_order_book (ctx, s, _params)
    s_outlier_ventures_hold_rate_updates_swing_order_book (ctx, s, _params)
    s_team_founders_pool_value_updates_swing_order_book (ctx, s, _params)
    s_team_founders_hold_rate_updates_swing_order_book (ctx, s, _params)
    s_presale_3_pool_value_updates_swing_order_book (ctx, s, _params)
    s_presale_3_hold_rate_updates_swing_order_book (ctx, s, _params)
    s_presale_2_pool_value_updates_swing_order_book (ctx, s, _params)
    s_presale_2_hold_rate_updates_swing_order_book (ctx, s, _params)
    s_presale_1_pool_value_updates_swing_order_book (ctx, s, _params)
    s_presale_1_hold_rate_updates_swing_order_book (ctx, s, _params)
    s_community_sale_pool_value_updates_swing_order_book (ctx, s, _params)
    s_community_sale_hold_rate_updates_swing_order_book (ctx, s, _params)
    s_token_hold_rate_updates_swing_order_book (ctx, s, _params)
    s_clock_updates_swing_order_book (ctx, s, _params)
    s_token_price_updates_swing_order_book (ctx, s, _params)
    myself = "swing-order-book"
    swing_order_book = multi_aggregate (set_diff_agg (get_new_value (s, "swing-order-book"), ctx.get ("removable")), [[ctx.get ("sell-time"), ctx.get ("buy-price"), ctx.get ("quantity")], [ctx.get ("sell-time"), ctx.get ("presale-1-price"), ctx.get ("presale-1-quantity")], [ctx.get ("sell-time"), ctx.get ("presale-2-price"), ctx.get ("presale-2-quantity")], [ctx.get ("sell-time"), ctx.get ("presale-3-price"), ctx.get ("presale-3-quantity")], [ctx.get ("sell-time"), ctx.get ("community-sale-price"), ctx.get ("community-sale-quantity")], [ctx.get ("sell-time"), ctx.get ("team-founders-price"), ctx.get ("team-founders-quantity")], [ctx.get ("sell-time"), ctx.get ("outlier-ventures-price"), ctx.get ("outlier-ventures-quantity")], [ctx.get ("sell-time"), ctx.get ("advisors-price"), ctx.get ("advisors-quantity")], [ctx.get ("sell-time"), ctx.get ("partners-price"), ctx.get ("partners-quantity")], [ctx.get ("sell-time"), ctx.get ("reward-price"), ctx.get ("reward-quantity")]])
    return "swing-order-book", update_state (s, "swing-order-book", swing_order_book)


def s_update_stim_token_price_delta (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_token_price_updates_stim_token_price_delta (ctx, s, _params)
    myself = "stim-token-price-delta"
    stim_token_price_delta = min_ls ([1] + max_ls ([0] + abs_ls (ctx.get ("stim"))))
    return "stim-token-price-delta", update_state (s, "stim-token-price-delta", stim_token_price_delta)


def s_update_change_urgency (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_stim_token_price_delta_updates_change_urgency (ctx, s, _params)
    s_stim_anti_user_goal_progress_updates_change_urgency (ctx, s, _params)
    s_stim_contradiction_rate_updates_change_urgency (ctx, s, _params)
    myself = "change-urgency"
    change_urgency = min_ls ([1] + max_ls ([0] + mul_pos_ls (ctx.get ("points"))))
    return "change-urgency", update_state (s, "change-urgency", change_urgency)


def s_update_change_reward_amount (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_stim_token_price_delta_updates_change_reward_amount (ctx, s, _params)
    s_stim_anti_user_goal_progress_updates_change_reward_amount (ctx, s, _params)
    s_stim_contradiction_rate_updates_change_reward_amount (ctx, s, _params)
    myself = "change-reward-amount"
    change_reward_amount = min_ls ([1] + max_ls ([0] + mul_pos_ls (ctx.get ("points"))))
    return "change-reward-amount", update_state (s, "change-reward-amount", change_reward_amount)


def s_update_change_sell_amount (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_stim_token_price_delta_updates_change_sell_amount (ctx, s, _params)
    s_stim_contradiction_rate_updates_change_sell_amount (ctx, s, _params)
    s_stim_anti_user_goal_progress_updates_change_sell_amount (ctx, s, _params)
    myself = "change-sell-amount"
    change_sell_amount = min_ls ([1] + max_ls ([0] + mul_pos_ls (ctx.get ("points"))))
    return "change-sell-amount", update_state (s, "change-sell-amount", change_sell_amount)


def s_update_change_buyback_amount (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_stim_contradiction_rate_updates_change_buyback_amount (ctx, s, _params)
    s_stim_anti_user_goal_progress_updates_change_buyback_amount (ctx, s, _params)
    s_stim_token_price_delta_updates_change_buyback_amount (ctx, s, _params)
    myself = "change-buyback-amount"
    change_buyback_amount = min_ls ([1] + max_ls ([0] + mul_pos_ls (ctx.get ("points"))))
    return "change-buyback-amount", update_state (s, "change-buyback-amount", change_buyback_amount)


def s_update_change_user_fee (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_stim_contradiction_rate_updates_change_user_fee (ctx, s, _params)
    s_stim_anti_user_goal_progress_updates_change_user_fee (ctx, s, _params)
    s_stim_token_price_delta_updates_change_user_fee (ctx, s, _params)
    myself = "change-user-fee"
    change_user_fee = min_ls ([1] + max_ls ([0] + mul_pos_ls (ctx.get ("points"))))
    return "change-user-fee", update_state (s, "change-user-fee", change_user_fee)


def s_update_change_lookup_fee (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_stim_contradiction_rate_updates_change_lookup_fee (ctx, s, _params)
    s_stim_anti_user_goal_progress_updates_change_lookup_fee (ctx, s, _params)
    s_stim_token_price_delta_updates_change_lookup_fee (ctx, s, _params)
    myself = "change-lookup-fee"
    change_lookup_fee = min_ls ([1] + max_ls ([0] + mul_pos_ls (ctx.get ("points"))))
    return "change-lookup-fee", update_state (s, "change-lookup-fee", change_lookup_fee)


def s_update_change_stake_yield (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_stim_token_price_delta_updates_change_stake_yield (ctx, s, _params)
    s_stim_anti_user_goal_progress_updates_change_stake_yield (ctx, s, _params)
    s_stim_contradiction_rate_updates_change_stake_yield (ctx, s, _params)
    myself = "change-stake-yield"
    change_stake_yield = min_ls ([1] + max_ls ([0] + mul_pos_ls (ctx.get ("points"))))
    return "change-stake-yield", update_state (s, "change-stake-yield", change_stake_yield)


def s_update_change_max_stake (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_stim_anti_user_goal_progress_updates_change_max_stake (ctx, s, _params)
    s_stim_token_price_delta_updates_change_max_stake (ctx, s, _params)
    s_stim_contradiction_rate_updates_change_max_stake (ctx, s, _params)
    myself = "change-max-stake"
    change_max_stake = min_ls ([1] + max_ls ([0] + mul_pos_ls (ctx.get ("points"))))
    return "change-max-stake", update_state (s, "change-max-stake", change_max_stake)


def s_update_fitness (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_threatslayer_revenue_updates_fitness (ctx, s, _params)
    s_threatslayer_users_updates_fitness (ctx, s, _params)
    s_foundation_pool_updates_fitness (ctx, s, _params)
    s_token_price_updates_fitness (ctx, s, _params)
    s_scam_page_successes_updates_fitness (ctx, s, _params)
    myself = "fitness"
    fitness = min_ls ([1000000000] + max_ls ([0] + div_ls ([1] + max_ls ([1] + sum_ls (ceil_ls (lg2_ls (max_ls ([1] + mul_ls (ctx.get ("users") + ctx.get ("price") + sum_ls (ctx.get ("assets")))))))))))
    return "fitness", update_state (s, "fitness", fitness)


def s_update_growth_level (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_reward_rate_updates_growth_level (ctx, s, _params)
    myself = "growth-level"
    growth_level = min_ls ([1.1] + max_ls ([1] + (min_ls ([1.1] + sum_ls (agg_choose ([const_growth_spread], [0], s ["run"], []) + [0.025])) if gt_ls (ctx.get ("reward-rate-delta") + [0]) [0] else max_ls ([1] + diff_ls (agg_choose ([const_growth_spread], [0], s ["run"], []) + [0.025])))))
    return "growth-level", update_state (s, "growth-level", growth_level)


def s_update_reward_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_threatslayer_users_updates_reward_rate (ctx, s, _params)
    s_threatslayer_lookup_price_updates_reward_rate (ctx, s, _params)
    s_token_price_updates_reward_rate (ctx, s, _params)
    s_reward_to_held_rate_updates_reward_rate (ctx, s, _params)
    myself = "reward-rate"
    reward_rate = min_ls ([1000000000] + max_ls ([0] + diff_ls (div_ls (mul_ls (ctx.get ("price") + ctx.get ("rewards-held")) + ctx.get ("users")) + ctx.get ("lookup-fees"))))
    return "reward-rate", update_state (s, "reward-rate", reward_rate)


def s_update_heuristic_innovation (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_change_urgency_updates_heuristic_innovation (ctx, s, _params)
    s_token_unstake_rate_updates_heuristic_innovation (ctx, s, _params)
    myself = "heuristic-innovation"
    heuristic_innovation = min_ls ([1000] + max_ls ([0] + ([0] if eq_ls (get_new_value (s, "heuristics") + [1000]) [0] else sum_ls (ctx.get ("urgency")))))
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


def s_update_watch_stake_yield (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    myself = "watch-stake-yield"
    watch_stake_yield = min_ls ([1.0e18] + max_ls ([0] + mul_ls (get_new_value (s, "token-unstake-rate") + get_new_value (s, "stake-yield"))))
    return "watch-stake-yield", update_state (s, "watch-stake-yield", watch_stake_yield)


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


def s_update_stim_anti_user_goal_progress (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_threatslayer_users_updates_stim_anti_user_goal_progress (ctx, s, _params)
    myself = "stim-anti-user-goal-progress"
    stim_anti_user_goal_progress = min_ls ([1] + max_ls ([0] + abs_ls (ctx.get ("stim"))))
    return "stim-anti-user-goal-progress", update_state (s, "stim-anti-user-goal-progress", stim_anti_user_goal_progress)


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
    anti_heuristics = min_ls ([1000] + max_ls ([0] + sum_ls (get_new_value (s, myself) + ctx.get ("innovation"))))
    return "anti-heuristics", update_state (s, "anti-heuristics", anti_heuristics)


def s_update_heuristics (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_heuristic_innovation_updates_heuristics (ctx, s, _params)
    myself = "heuristics"
    heuristics = min_ls ([1000] + max_ls ([1] + sum_ls (get_new_value (s, myself) + ctx.get ("innovation"))))
    return "heuristics", update_state (s, "heuristics", heuristics)


def s_update_reward_price (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    myself = "reward-price"
    reward_price = min_ls ([0] + max_ls ([0] + get_new_value (s, "reward-price")))
    return "reward-price", update_state (s, "reward-price", reward_price)


def s_update_stim_contradiction_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_heuristic_contradictions_updates_stim_contradiction_rate (ctx, s, _params)
    myself = "stim-contradiction-rate"
    stim_contradiction_rate = min_ls ([1] + max_ls ([0] + abs_ls (ctx.get ("stim"))))
    return "stim-contradiction-rate", update_state (s, "stim-contradiction-rate", stim_contradiction_rate)


def s_update_staking_enthusiasm (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_crypto_hype_updates_staking_enthusiasm (ctx, s, _params)
    myself = "staking-enthusiasm"
    staking_enthusiasm = min_ls ([100] + max_ls ([1] + mul_ls (ctx.get ("expectation-multiplier") + div_ls ([sim_random (5, 25, s ["run"])] + [100]))))
    return "staking-enthusiasm", update_state (s, "staking-enthusiasm", staking_enthusiasm)


def s_update_watch_unhold_mismatch (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    myself = "watch-unhold-mismatch"
    watch_unhold_mismatch = min_ls ([100] + max_ls ([0] + div_ls (diff_ls (get_old_value (s, "token-hold-pool") + get_new_value (s, "token-hold-pool")) + max_ls ([1] + sum_ls (diff_ls (get_new_value (s, "token-stake-pool") + get_old_value (s, "token-stake-pool")) + diff_ls (get_new_value (s, "token-sell-pool") + get_old_value (s, "token-sell-pool")))))))
    return "watch-unhold-mismatch", update_state (s, "watch-unhold-mismatch", watch_unhold_mismatch)


def s_update_partners_pool_value (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    myself = "partners-pool-value"
    partners_pool_value = min_ls ([100] + max_ls ([0] + get_new_value (s, "partners-pool-value")))
    return "partners-pool-value", update_state (s, "partners-pool-value", partners_pool_value)


def s_update_advisors_pool_value (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    myself = "advisors-pool-value"
    advisors_pool_value = min_ls ([100] + max_ls ([0] + get_new_value (s, "advisors-pool-value")))
    return "advisors-pool-value", update_state (s, "advisors-pool-value", advisors_pool_value)


def s_update_outlier_ventures_pool_value (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    myself = "outlier-ventures-pool-value"
    outlier_ventures_pool_value = min_ls ([100] + max_ls ([0] + get_new_value (s, "outlier-ventures-pool-value")))
    return "outlier-ventures-pool-value", update_state (s, "outlier-ventures-pool-value", outlier_ventures_pool_value)


def s_update_team_founders_pool_value (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    myself = "team-founders-pool-value"
    team_founders_pool_value = min_ls ([100] + max_ls ([0] + get_new_value (s, "team-founders-pool-value")))
    return "team-founders-pool-value", update_state (s, "team-founders-pool-value", team_founders_pool_value)


def s_update_presale_3_pool_value (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    myself = "presale-3-pool-value"
    presale_3_pool_value = min_ls ([100] + max_ls ([0] + get_new_value (s, "presale-3-pool-value")))
    return "presale-3-pool-value", update_state (s, "presale-3-pool-value", presale_3_pool_value)


def s_update_presale_2_pool_value (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    myself = "presale-2-pool-value"
    presale_2_pool_value = min_ls ([100] + max_ls ([0] + get_new_value (s, "presale-2-pool-value")))
    return "presale-2-pool-value", update_state (s, "presale-2-pool-value", presale_2_pool_value)


def s_update_presale_1_pool_value (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    myself = "presale-1-pool-value"
    presale_1_pool_value = min_ls ([100] + max_ls ([0] + get_new_value (s, "presale-1-pool-value")))
    return "presale-1-pool-value", update_state (s, "presale-1-pool-value", presale_1_pool_value)


def s_update_community_sale_pool_value (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    myself = "community-sale-pool-value"
    community_sale_pool_value = min_ls ([100] + max_ls ([0] + get_new_value (s, "community-sale-pool-value")))
    return "community-sale-pool-value", update_state (s, "community-sale-pool-value", community_sale_pool_value)


def s_update_money_growth_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    myself = "money-growth-rate"
    money_growth_rate = min_ls (div_ls ([1017] + [1000]) + max_ls (div_ls ([988] + [1000]) + agg_choose (([const_observed_money_growth] if eq_ls ([_params ["money-growth"]] + [const_observed_money_growth_id]) [0] else [-999]), [0], s ["run"], [])))
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


def s_update_threatslayer_lookup_price (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_threatslayer_users_updates_threatslayer_lookup_price (ctx, s, _params)
    s_change_lookup_fee_updates_threatslayer_lookup_price (ctx, s, _params)
    s_change_user_fee_updates_threatslayer_lookup_price (ctx, s, _params)
    s_threatslayer_lookup_rate_updates_threatslayer_lookup_price (ctx, s, _params)
    s_threatslayer_expenses_updates_threatslayer_lookup_price (ctx, s, _params)
    myself = "threatslayer-lookup-price"
    threatslayer_lookup_price = min_ls ([5] + max_ls ([0] + div_ls (sum_ls (mul_ls (min_ls (div_ls (mul_ls (ctx.get ("expenses") + ctx.get ("mul-lookup-fee")) + ctx.get ("users")) + ctx.get ("mul-user-fee")) + ctx.get ("users")) + mul_ls (ctx.get ("lookups") + ctx.get ("mul-lookup-fee"))) + [1])))
    return "threatslayer-lookup-price", update_state (s, "threatslayer-lookup-price", threatslayer_lookup_price)


def s_update_threatslayer_expenses (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_heuristic_innovation_updates_threatslayer_expenses (ctx, s, _params)
    myself = "threatslayer-expenses"
    threatslayer_expenses = min_ls ([1000000] + max_ls ([1] + sum_ls ([40229] + ctx.get ("profit-diverted-to-innovate"))))
    return "threatslayer-expenses", update_state (s, "threatslayer-expenses", threatslayer_expenses)


def s_update_token_price (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_token_sell_pool_updates_token_price (ctx, s, _params)
    s_intr_investments_updates_token_price (ctx, s, _params)
    myself = "token-price"
    token_price = min_ls ([6.0e10] + max_ls ([0.001] + div_ls (ceil_ls (mul_ls (div_ls (ctx.get ("invest-pool") + max_ls ([1] + ctx.get ("sell-pool"))) + [100])) + [100])))
    return "token-price", update_state (s, "token-price", token_price)


def s_update_contradiction_loss (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_heuristic_contradictions_updates_contradiction_loss (ctx, s, _params)
    myself = "contradiction-loss"
    contradiction_loss = min_ls ([1] + max_ls ([0] + agg_col_to_list (2, agg_rows_range_new ([[LessThanEq (ctx.get ("contradiction-rate")), GreaterThan (ctx.get ("contradiction-rate"))]], [const_contradiction_loss]))))
    return "contradiction-loss", update_state (s, "contradiction-loss", contradiction_loss)


def s_update_crypto_hype (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_money_supply_updates_crypto_hype (ctx, s, _params)
    myself = "crypto-hype"
    crypto_hype = min_ls ([2] + max_ls ([-2] + agg_choose (agg_cols ([[1], [2]], agg_rows ([[get_new_value (s, "crypto-hype")]], ([const_observed_expectation_chain] if eq_ls ([_params ["expectation-chain"]] + [const_observed_expectation_chain_id]) [0] else [-999]))), [0], s ["run"], [])))
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
    s_threatslayer_users_updates_scam_page_success_rate (ctx, s, _params)
    s_heuristic_contradictions_updates_scam_page_success_rate (ctx, s, _params)
    myself = "scam-page-success-rate"
    scam_page_success_rate = diff_ls (mul_ls ([0.4] + get_new_value (s, "scam-page-visits")) + mul_ls ([0.4] + get_new_value (s, "scam-page-visits") + mul_ls (ctx.get ("pass-through") + ctx.get ("user-share"))))
    return "scam-page-success-rate", update_state (s, "scam-page-success-rate", scam_page_success_rate)


def s_update_scam_page_visit_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    myself = "scam-page-visit-rate"
    scam_page_visit_rate = mul_ls (get_new_value (s, "page-visits") + [_params ["maliciousness-rate"]])
    return "scam-page-visit-rate", update_state (s, "scam-page-visit-rate", scam_page_visit_rate)


def s_update_page_visit_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    myself = "page-visit-rate"
    page_visit_rate = mul_ls (sum_ls (get_new_value (s, "browser-users") + get_new_value (s, "threatslayer-users")) + [_params ["pages-per-user"]])
    return "page-visit-rate", update_state (s, "page-visit-rate", page_visit_rate)


def s_update_threatslayer_upkeep_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_threatslayer_expenses_updates_threatslayer_upkeep_rate (ctx, s, _params)
    myself = "threatslayer-upkeep-rate"
    threatslayer_upkeep_rate = sum_ls (ctx.get ("expenses"))
    return "threatslayer-upkeep-rate", update_state (s, "threatslayer-upkeep-rate", threatslayer_upkeep_rate)


def s_update_interlock_self_invest_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_token_price_updates_interlock_self_invest_rate (ctx, s, _params)
    s_foundation_hold_rate_updates_interlock_self_invest_rate (ctx, s, _params)
    s_rewards_hold_rate_updates_interlock_self_invest_rate (ctx, s, _params)
    myself = "interlock-self-invest-rate"
    interlock_self_invest_rate = mul_ls (ctx.get ("price") + sum_ls (ctx.get ("tokens-bought")))
    return "interlock-self-invest-rate", update_state (s, "interlock-self-invest-rate", interlock_self_invest_rate)


def s_update_threatslayer_revenue_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_threatslayer_data_shared_updates_threatslayer_revenue_rate (ctx, s, _params)
    myself = "threatslayer-revenue-rate"
    threatslayer_revenue_rate = mul_ls ([_params ["data-value"]] + ctx.get ("shared"))
    return "threatslayer-revenue-rate", update_state (s, "threatslayer-revenue-rate", threatslayer_revenue_rate)


def s_update_threatslayer_share_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_threatslayer_lookup_price_updates_threatslayer_share_rate (ctx, s, _params)
    s_threatslayer_lookup_rate_updates_threatslayer_share_rate (ctx, s, _params)
    myself = "threatslayer-share-rate"
    threatslayer_share_rate = mul_ls (sum_ls (mul_ls (ctx.get ("lookups") + [_params ["wants-malicious"]] + [_params ["maliciousness-rate"]] + [_params ["data-elements-per-url"]]) + mul_ls (ctx.get ("lookups") + [_params ["wants-unique"]] + [_params ["uniqueness-rate"]] + [_params ["data-elements-per-url"]])) + (diff_ls ([1] + [_params ["free-loaders"]]) if gt_ls (ctx.get ("lookup-price") + [0]) [0] else [1]))
    return "threatslayer-share-rate", update_state (s, "threatslayer-share-rate", threatslayer_share_rate)


def s_update_resolution_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    myself = "resolution-rate"
    resolution_rate = get_old_value (s, "grey-area-entity-rate")
    return "resolution-rate", update_state (s, "resolution-rate", resolution_rate)


def s_update_grey_area_entity_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_heuristic_contradictions_updates_grey_area_entity_rate (ctx, s, _params)
    myself = "grey-area-entity-rate"
    grey_area_entity_rate = mul_ls (get_new_value (s, "threatslayer-lookups") + ctx.get ("contradictions"))
    return "grey-area-entity-rate", update_state (s, "grey-area-entity-rate", grey_area_entity_rate)


def s_update_threatslayer_lookup_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_threatslayer_users_updates_threatslayer_lookup_rate (ctx, s, _params)
    s_page_visit_rate_updates_threatslayer_lookup_rate (ctx, s, _params)
    myself = "threatslayer-lookup-rate"
    threatslayer_lookup_rate = mul_ls (ctx.get ("pages-visited") + ctx.get ("user-share"))
    return "threatslayer-lookup-rate", update_state (s, "threatslayer-lookup-rate", threatslayer_lookup_rate)


def s_update_threatslayer_abandonment_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_reward_to_held_rate_updates_threatslayer_abandonment_rate (ctx, s, _params)
    s_heuristic_contradictions_updates_threatslayer_abandonment_rate (ctx, s, _params)
    s_threatslayer_users_updates_threatslayer_abandonment_rate (ctx, s, _params)
    myself = "threatslayer-abandonment-rate"
    threatslayer_abandonment_rate = mul_ls (ctx.get ("users") + max_ls ([0] + agg_col_to_list (2, agg_rows_range_new ([[LessThanEq (ctx.get ("contradiction-rate")), GreaterThan (ctx.get ("contradiction-rate"))]], [const_contradiction_loss]))))
    return "threatslayer-abandonment-rate", update_state (s, "threatslayer-abandonment-rate", threatslayer_abandonment_rate)


def s_update_threatslayer_adoption_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_interlock_hype_updates_threatslayer_adoption_rate (ctx, s, _params)
    s_threatslayer_users_updates_threatslayer_adoption_rate (ctx, s, _params)
    s_growth_level_updates_threatslayer_adoption_rate (ctx, s, _params)
    myself = "threatslayer-adoption-rate"
    threatslayer_adoption_rate = mul_ls ((max_ls ([20] + diff_ls (mul_ls (ctx.get ("users") + ctx.get ("growth")) + ctx.get ("users"))) if lt_ls (get_new_value (s, "threatslayer-users") + [_params ["max-users"]]) [0] else [0]))
    return "threatslayer-adoption-rate", update_state (s, "threatslayer-adoption-rate", threatslayer_adoption_rate)


def s_update_threatslayer_investment_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_token_price_updates_threatslayer_investment_rate (ctx, s, _params)
    s_foundation_unhold_rate_updates_threatslayer_investment_rate (ctx, s, _params)
    s_rewards_unhold_rate_updates_threatslayer_investment_rate (ctx, s, _params)
    myself = "threatslayer-investment-rate"
    threatslayer_investment_rate = mul_ls (sum_ls (ctx.get ("tokens-sold")) + ctx.get ("price"))
    return "threatslayer-investment-rate", update_state (s, "threatslayer-investment-rate", threatslayer_investment_rate)


def s_update_intr_divest_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_crypto_hype_updates_intr_divest_rate (ctx, s, _params)
    s_token_profit_updates_intr_divest_rate (ctx, s, _params)
    myself = "intr-divest-rate"
    intr_divest_rate = max_ls ([0] + diff_ls (get_new_value (s, "intr-investments") + mul_ls (get_new_value (s, "intr-investments") + agg_to_list (agg_col_to_list (1, agg_rows ([[ctx.get ("crypto-hype")]], [const_invest_movement]))))))
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
    s_crypto_hype_updates_intr_invest_rate (ctx, s, _params)
    s_threatslayer_lookup_price_updates_intr_invest_rate (ctx, s, _params)
    myself = "intr-invest-rate"
    intr_invest_rate = min_ls (mul_ls ([1.0e-4] + get_new_value (s, "crypto-investments")) + sum_ls ((mul_ls (get_new_value (s, "intr-investments") + agg_col_to_list (1, agg_rows ([[ctx.get ("crypto-hype")]], [const_invest_movement])) + [_params ["swing-traders"]]) if lt_eq_ls (ctx.get ("price-delta-pct") + [0.95]) [0] else [0]) + (mul_ls (get_new_value (s, "intr-investments") + agg_col_to_list (1, agg_rows ([[ctx.get ("crypto-hype")]], [const_invest_movement])) + [_params ["position-traders"]]) if gt_eq_ls (ctx.get ("price-delta-pct") + [1.05]) [0] else [0])))
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
    money_mint_rate = (diff_ls (mul_ls (get_new_value (s, "money-supply") + ctx.get ("growth")) + get_new_value (s, "money-supply")) if gt_ls (ctx.get ("growth") + [1]) [0] else [0])
    return "money-mint-rate", update_state (s, "money-mint-rate", money_mint_rate)


def s_update_money_reclaim_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_money_growth_rate_updates_money_reclaim_rate (ctx, s, _params)
    myself = "money-reclaim-rate"
    money_reclaim_rate = (diff_ls (get_new_value (s, "money-supply") + mul_ls (get_new_value (s, "money-supply") + ctx.get ("growth"))) if lt_ls (ctx.get ("growth") + [1]) [0] else [0])
    return "money-reclaim-rate", update_state (s, "money-reclaim-rate", money_reclaim_rate)


def s_update_reward_to_held_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_change_reward_amount_updates_reward_to_held_rate (ctx, s, _params)
    s_threatslayer_data_shared_updates_reward_to_held_rate (ctx, s, _params)
    s_stake_yield_updates_reward_to_held_rate (ctx, s, _params)
    s_clock_updates_reward_to_held_rate (ctx, s, _params)
    myself = "reward-to-held-rate"
    reward_to_held_rate = sum_ls ((mul_ls (ctx.get ("mul-reward-rate") + diff_ls (mul_ls (div_ls ([const_rewards_size] + [const_rewards_period]) + ctx.get ("months")) + diff_ls ([const_rewards_size] + get_new_value (s, "rewards-pool")))) if gt_ls (ctx.get ("months") + [const_rewards_delay]) [0] else [0]) + ctx.get ("stake-yield"))
    return "reward-to-held-rate", update_state (s, "reward-to-held-rate", reward_to_held_rate)


def s_update_token_unstake_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_max_stake_updates_token_unstake_rate (ctx, s, _params)
    s_staking_opportunities_updates_token_unstake_rate (ctx, s, _params)
    s_staking_enthusiasm_updates_token_unstake_rate (ctx, s, _params)
    s_rewards_pool_updates_token_unstake_rate (ctx, s, _params)
    myself = "token-unstake-rate"
    token_unstake_rate = mul_ls (ctx.get ("enthusiasm") + ctx.get ("staking-ops") + ctx.get ("max-per-entity"))
    return "token-unstake-rate", update_state (s, "token-unstake-rate", token_unstake_rate)


def s_update_token_stake_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_max_stake_updates_token_stake_rate (ctx, s, _params)
    s_staking_opportunities_updates_token_stake_rate (ctx, s, _params)
    s_staking_enthusiasm_updates_token_stake_rate (ctx, s, _params)
    s_rewards_pool_updates_token_stake_rate (ctx, s, _params)
    myself = "token-stake-rate"
    token_stake_rate = mul_ls (ctx.get ("enthusiasm") + ctx.get ("staking-ops") + ctx.get ("max-per-entity") + ctx.get ("reward-pool-fullness"))
    return "token-stake-rate", update_state (s, "token-stake-rate", token_stake_rate)


def s_update_token_unhold_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_investor_order_book_updates_token_unhold_rate (ctx, s, _params)
    s_position_order_book_updates_token_unhold_rate (ctx, s, _params)
    s_swing_order_book_updates_token_unhold_rate (ctx, s, _params)
    myself = "token-unhold-rate"
    token_unhold_rate = sum_ls (ctx.get ("quantity") + [0])
    return "token-unhold-rate", update_state (s, "token-unhold-rate", token_unhold_rate)


def s_update_token_hold_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_intr_investments_updates_token_hold_rate (ctx, s, _params)
    myself = "token-hold-rate"
    token_hold_rate = div_ls (ctx.get ("invested") + get_new_value (s, "token-price"))
    return "token-hold-rate", update_state (s, "token-hold-rate", token_hold_rate)


def s_update_foundation_unhold_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_token_price_updates_foundation_unhold_rate (ctx, s, _params)
    s_change_sell_amount_updates_foundation_unhold_rate (ctx, s, _params)
    s_threatslayer_revenue_updates_foundation_unhold_rate (ctx, s, _params)
    s_threatslayer_expenses_updates_foundation_unhold_rate (ctx, s, _params)
    s_clock_updates_foundation_unhold_rate (ctx, s, _params)
    myself = "foundation-unhold-rate"
    foundation_unhold_rate = (sum_ls (mul_ls (max_ls ([0] + div_ls (diff_ls (ctx.get ("expenses") + ctx.get ("revenue")) + ctx.get ("price"))) + [_params ["cover-own-costs"]]) + mul_ls (ctx.get ("mul-sell-amount") + diff_ls (mul_ls (div_ls ([182597475] + [84]) + ctx.get ("months")) + diff_ls ([182597475] + get_new_value (s, "foundation-pool"))))) if gt_ls (ctx.get ("months") + [1]) [0] else [0])
    return "foundation-unhold-rate", update_state (s, "foundation-unhold-rate", foundation_unhold_rate)


def s_update_foundation_hold_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_token_price_updates_foundation_hold_rate (ctx, s, _params)
    s_change_buyback_amount_updates_foundation_hold_rate (ctx, s, _params)
    s_threatslayer_revenue_updates_foundation_hold_rate (ctx, s, _params)
    s_clock_updates_foundation_hold_rate (ctx, s, _params)
    myself = "foundation-hold-rate"
    foundation_hold_rate = div_ls (mul_ls (ctx.get ("money") + ctx.get ("mul-buyback-amount")) + ctx.get ("price"))
    return "foundation-hold-rate", update_state (s, "foundation-hold-rate", foundation_hold_rate)


def s_update_rewards_unhold_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_token_price_updates_rewards_unhold_rate (ctx, s, _params)
    s_change_sell_amount_updates_rewards_unhold_rate (ctx, s, _params)
    s_threatslayer_revenue_updates_rewards_unhold_rate (ctx, s, _params)
    s_threatslayer_expenses_updates_rewards_unhold_rate (ctx, s, _params)
    s_clock_updates_rewards_unhold_rate (ctx, s, _params)
    myself = "rewards-unhold-rate"
    rewards_unhold_rate = (sum_ls (mul_ls (max_ls ([0] + div_ls (diff_ls (ctx.get ("expenses") + ctx.get ("revenue")) + ctx.get ("price"))) + [_params ["cover-own-costs"]]) + mul_ls (ctx.get ("mul-sell-amount") + diff_ls (mul_ls (div_ls ([300000000] + [48]) + ctx.get ("months")) + diff_ls ([300000000] + get_new_value (s, "rewards-pool"))))) if gt_ls (ctx.get ("months") + [0]) [0] else [0])
    return "rewards-unhold-rate", update_state (s, "rewards-unhold-rate", rewards_unhold_rate)


def s_update_rewards_hold_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_token_price_updates_rewards_hold_rate (ctx, s, _params)
    s_change_buyback_amount_updates_rewards_hold_rate (ctx, s, _params)
    s_threatslayer_revenue_updates_rewards_hold_rate (ctx, s, _params)
    s_clock_updates_rewards_hold_rate (ctx, s, _params)
    myself = "rewards-hold-rate"
    rewards_hold_rate = div_ls (mul_ls (ctx.get ("money") + ctx.get ("mul-buyback-amount")) + ctx.get ("price"))
    return "rewards-hold-rate", update_state (s, "rewards-hold-rate", rewards_hold_rate)


def s_update_partners_hold_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_clock_updates_partners_hold_rate (ctx, s, _params)
    myself = "partners-hold-rate"
    partners_hold_rate = (diff_ls (mul_ls (div_ls ([37000000] + [1]) + ctx.get ("months")) + diff_ls ([37000000] + get_new_value (s, "partners-pool"))) if gt_ls (ctx.get ("months") + [0]) [0] else [0])
    return "partners-hold-rate", update_state (s, "partners-hold-rate", partners_hold_rate)


def s_update_advisors_hold_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_clock_updates_advisors_hold_rate (ctx, s, _params)
    myself = "advisors-hold-rate"
    advisors_hold_rate = (diff_ls (mul_ls (div_ls ([25000000] + [24]) + ctx.get ("months")) + diff_ls ([25000000] + get_new_value (s, "advisors-pool"))) if gt_ls (ctx.get ("months") + [1]) [0] else [0])
    return "advisors-hold-rate", update_state (s, "advisors-hold-rate", advisors_hold_rate)


def s_update_outlier_ventures_hold_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_clock_updates_outlier_ventures_hold_rate (ctx, s, _params)
    myself = "outlier-ventures-hold-rate"
    outlier_ventures_hold_rate = (diff_ls (mul_ls (div_ls ([40000000] + [24]) + ctx.get ("months")) + diff_ls ([40000000] + get_new_value (s, "outlier-ventures-pool"))) if gt_ls (ctx.get ("months") + [1]) [0] else [0])
    return "outlier-ventures-hold-rate", update_state (s, "outlier-ventures-hold-rate", outlier_ventures_hold_rate)


def s_update_team_founders_hold_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_clock_updates_team_founders_hold_rate (ctx, s, _params)
    myself = "team-founders-hold-rate"
    team_founders_hold_rate = (diff_ls (mul_ls (div_ls ([200000000] + [36]) + ctx.get ("months")) + diff_ls ([200000000] + get_new_value (s, "team-founders-pool"))) if gt_ls (ctx.get ("months") + [6]) [0] else [0])
    return "team-founders-hold-rate", update_state (s, "team-founders-hold-rate", team_founders_hold_rate)


def s_update_presale_3_hold_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_clock_updates_presale_3_hold_rate (ctx, s, _params)
    myself = "presale-3-hold-rate"
    presale_3_hold_rate = (diff_ls (mul_ls (div_ls ([93750000] + [12]) + ctx.get ("months")) + diff_ls ([93750000] + get_new_value (s, "presale-3-pool"))) if gt_ls (ctx.get ("months") + [1]) [0] else [0])
    return "presale-3-hold-rate", update_state (s, "presale-3-hold-rate", presale_3_hold_rate)


def s_update_presale_2_hold_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_clock_updates_presale_2_hold_rate (ctx, s, _params)
    myself = "presale-2-hold-rate"
    presale_2_hold_rate = (diff_ls (mul_ls (div_ls ([20000000] + [15]) + ctx.get ("months")) + diff_ls ([20000000] + get_new_value (s, "presale-2-pool"))) if gt_ls (ctx.get ("months") + [1]) [0] else [0])
    return "presale-2-hold-rate", update_state (s, "presale-2-hold-rate", presale_2_hold_rate)


def s_update_presale_1_hold_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_clock_updates_presale_1_hold_rate (ctx, s, _params)
    myself = "presale-1-hold-rate"
    presale_1_hold_rate = (diff_ls (mul_ls (div_ls ([48622222] + [18]) + ctx.get ("months")) + diff_ls ([48622222] + get_new_value (s, "presale-1-pool"))) if gt_ls (ctx.get ("months") + [1]) [0] else [0])
    return "presale-1-hold-rate", update_state (s, "presale-1-hold-rate", presale_1_hold_rate)


def s_update_community_sale_hold_rate (_params, substep, sH, s, _input, **kwargs):
    ctx = {}
    s_clock_updates_community_sale_hold_rate (ctx, s, _params)
    myself = "community-sale-hold-rate"
    community_sale_hold_rate = (diff_ls (mul_ls (div_ls ([3030303] + [1]) + ctx.get ("months")) + diff_ls ([3030303] + get_new_value (s, "community-sale-pool"))) if gt_ls (ctx.get ("months") + [0]) [0] else [0])
    return "community-sale-hold-rate", update_state (s, "community-sale-hold-rate", community_sale_hold_rate)


cfg = { "N": 1, "T": range (200), "M": generate_params () }
init_state = {}
init_state ["flow-adjustments"] = {}
init_state ["hodler-order-book"] = initialize_state (Aggregation (["sell-time", "buy-price", "quantity"], "sum"))
init_state ["investor-order-book"] = initialize_state (Aggregation (["sell-time", "buy-price", "quantity"], "sum"))
init_state ["position-order-book"] = initialize_state (Aggregation (["sell-time", "buy-price", "quantity"], "sum"))
init_state ["swing-order-book"] = initialize_state (Aggregation (["sell-time", "buy-price", "quantity"], "sum"))
init_state ["stim-token-price-delta"] = initialize_state (0)
init_state ["change-urgency"] = initialize_state (0)
init_state ["change-reward-amount"] = initialize_state (0)
init_state ["change-sell-amount"] = initialize_state (0)
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
init_state ["watch-stake-yield"] = initialize_state (0)
init_state ["stake-yield"] = initialize_state (1.01)
init_state ["max-stake"] = initialize_state (300)
init_state ["stim-anti-user-goal-progress"] = initialize_state (0)
init_state ["staking-opportunities"] = initialize_state (1)
init_state ["heuristic-contradictions"] = initialize_state (0.01)
init_state ["anti-heuristics"] = initialize_state (0)
init_state ["heuristics"] = initialize_state (20)
init_state ["reward-price"] = initialize_state (0)
init_state ["stim-contradiction-rate"] = initialize_state (0)
init_state ["staking-enthusiasm"] = initialize_state (div_ls ([15] + [100]))
init_state ["watch-unhold-mismatch"] = initialize_state (0)
init_state ["partners-pool-value"] = initialize_state (0)
init_state ["advisors-pool-value"] = initialize_state (0)
init_state ["outlier-ventures-pool-value"] = initialize_state (0)
init_state ["team-founders-pool-value"] = initialize_state (0)
init_state ["presale-3-pool-value"] = initialize_state (0.032)
init_state ["presale-2-pool-value"] = initialize_state (0.03)
init_state ["presale-1-pool-value"] = initialize_state (0.045)
init_state ["community-sale-pool-value"] = initialize_state (0.033)
init_state ["money-growth-rate"] = initialize_state (1.0)
init_state ["interlock-hype"] = initialize_state (0)
init_state ["token-profit"] = initialize_state (np.median (range (0, 100)))
init_state ["threatslayer-lookup-price"] = initialize_state (0)
init_state ["threatslayer-expenses"] = initialize_state (40229)
init_state ["token-price"] = initialize_state (0.035)
init_state ["contradiction-loss"] = initialize_state (0)
init_state ["crypto-hype"] = initialize_state (0)
init_state ["clock"] = initialize_state (0)
init_state ["scam-upkeep"] = initialize_state (0)
init_state ["scam-profits"] = initialize_state (0)
init_state ["potential-scam-profits"] = initialize_state (2.0e10)
init_state ["scam-page-successes"] = initialize_state (0)
init_state ["scam-page-visits"] = initialize_state (0)
init_state ["resolved-entities"] = initialize_state (0)
init_state ["grey-area-entities"] = initialize_state (0)
init_state ["threatslayer-users"] = initialize_state (5000.0)
init_state ["browser-users"] = initialize_state (3.0e9)
init_state ["data-buyer-money"] = initialize_state (3.0e11)
init_state ["threatslayer-upkeep"] = initialize_state (0)
init_state ["threatslayer-revenue"] = initialize_state (120000.0)
init_state ["threatslayer-data-shared"] = initialize_state (0)
init_state ["browsing-data"] = initialize_state (1.2e18)
init_state ["potential-threatslayer-lookups"] = initialize_state (2.0e17)
init_state ["threatslayer-lookups"] = initialize_state (0)
init_state ["page-visits"] = initialize_state (0)
init_state ["potential-page-visits"] = initialize_state (2.0e17)
init_state ["intr-investments"] = initialize_state (1750000)
init_state ["crypto-investments"] = initialize_state (1.8e11)
init_state ["money-reclaimed"] = initialize_state (0)
init_state ["money-supply"] = initialize_state (1000000000000)
init_state ["money-mint"] = initialize_state (1000000000000)
init_state ["token-hold-pool"] = initialize_state (0)
init_state ["token-stake-pool"] = initialize_state (0)
init_state ["token-sell-pool"] = initialize_state (50000000)
init_state ["foundation-pool"] = initialize_state (182597475)
init_state ["rewards-pool"] = initialize_state (300000000)
init_state ["partners-pool"] = initialize_state (37000000)
init_state ["advisors-pool"] = initialize_state (25000000)
init_state ["outlier-ventures-pool"] = initialize_state (40000000)
init_state ["team-founders-pool"] = initialize_state (200000000)
init_state ["presale-3-pool"] = initialize_state (93750000)
init_state ["presale-2-pool"] = initialize_state (20000000)
init_state ["presale-1-pool"] = initialize_state (48622222)
init_state ["community-sale-pool"] = initialize_state (3030303)
init_state ["scam-upkeep-rate"] = initialize_state (0)
init_state ["scam-profit-rate"] = initialize_state (0)
init_state ["scam-page-success-rate"] = initialize_state (0)
init_state ["scam-page-visit-rate"] = initialize_state (0)
init_state ["page-visit-rate"] = initialize_state (0)
init_state ["threatslayer-upkeep-rate"] = initialize_state (0)
init_state ["interlock-self-invest-rate"] = initialize_state (0)
init_state ["threatslayer-revenue-rate"] = initialize_state (0)
init_state ["threatslayer-share-rate"] = initialize_state (0)
init_state ["resolution-rate"] = initialize_state (0)
init_state ["grey-area-entity-rate"] = initialize_state (0)
init_state ["threatslayer-lookup-rate"] = initialize_state (0)
init_state ["threatslayer-abandonment-rate"] = initialize_state (0)
init_state ["threatslayer-adoption-rate"] = initialize_state (0)
init_state ["threatslayer-investment-rate"] = initialize_state (0)
init_state ["intr-divest-rate"] = initialize_state (0)
init_state ["crypto-divest-rate"] = initialize_state (0)
init_state ["intr-invest-rate"] = initialize_state (0)
init_state ["crypto-invest-rate"] = initialize_state (0)
init_state ["money-mint-rate"] = initialize_state (0)
init_state ["money-reclaim-rate"] = initialize_state (0)
init_state ["reward-to-held-rate"] = initialize_state (0)
init_state ["token-unstake-rate"] = initialize_state (0)
init_state ["token-stake-rate"] = initialize_state (0)
init_state ["token-unhold-rate"] = initialize_state (0)
init_state ["token-hold-rate"] = initialize_state (0)
init_state ["foundation-unhold-rate"] = initialize_state (0)
init_state ["foundation-hold-rate"] = initialize_state (0)
init_state ["rewards-unhold-rate"] = initialize_state (0)
init_state ["rewards-hold-rate"] = initialize_state (0)
init_state ["partners-hold-rate"] = initialize_state (0)
init_state ["advisors-hold-rate"] = initialize_state (0)
init_state ["outlier-ventures-hold-rate"] = initialize_state (0)
init_state ["team-founders-hold-rate"] = initialize_state (0)
init_state ["presale-3-hold-rate"] = initialize_state (0)
init_state ["presale-2-hold-rate"] = initialize_state (0)
init_state ["presale-1-hold-rate"] = initialize_state (0)
init_state ["community-sale-hold-rate"] = initialize_state (0)
indicators_and_flows = {}
indicators_and_flows ["hodler-order-book"] = s_update_hodler_order_book
indicators_and_flows ["investor-order-book"] = s_update_investor_order_book
indicators_and_flows ["position-order-book"] = s_update_position_order_book
indicators_and_flows ["swing-order-book"] = s_update_swing_order_book
indicators_and_flows ["stim-token-price-delta"] = s_update_stim_token_price_delta
indicators_and_flows ["change-urgency"] = s_update_change_urgency
indicators_and_flows ["change-reward-amount"] = s_update_change_reward_amount
indicators_and_flows ["change-sell-amount"] = s_update_change_sell_amount
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
indicators_and_flows ["watch-stake-yield"] = s_update_watch_stake_yield
indicators_and_flows ["stake-yield"] = s_update_stake_yield
indicators_and_flows ["max-stake"] = s_update_max_stake
indicators_and_flows ["stim-anti-user-goal-progress"] = s_update_stim_anti_user_goal_progress
indicators_and_flows ["staking-opportunities"] = s_update_staking_opportunities
indicators_and_flows ["heuristic-contradictions"] = s_update_heuristic_contradictions
indicators_and_flows ["anti-heuristics"] = s_update_anti_heuristics
indicators_and_flows ["heuristics"] = s_update_heuristics
indicators_and_flows ["reward-price"] = s_update_reward_price
indicators_and_flows ["stim-contradiction-rate"] = s_update_stim_contradiction_rate
indicators_and_flows ["staking-enthusiasm"] = s_update_staking_enthusiasm
indicators_and_flows ["watch-unhold-mismatch"] = s_update_watch_unhold_mismatch
indicators_and_flows ["partners-pool-value"] = s_update_partners_pool_value
indicators_and_flows ["advisors-pool-value"] = s_update_advisors_pool_value
indicators_and_flows ["outlier-ventures-pool-value"] = s_update_outlier_ventures_pool_value
indicators_and_flows ["team-founders-pool-value"] = s_update_team_founders_pool_value
indicators_and_flows ["presale-3-pool-value"] = s_update_presale_3_pool_value
indicators_and_flows ["presale-2-pool-value"] = s_update_presale_2_pool_value
indicators_and_flows ["presale-1-pool-value"] = s_update_presale_1_pool_value
indicators_and_flows ["community-sale-pool-value"] = s_update_community_sale_pool_value
indicators_and_flows ["money-growth-rate"] = s_update_money_growth_rate
indicators_and_flows ["interlock-hype"] = s_update_interlock_hype
indicators_and_flows ["token-profit"] = s_update_token_profit
indicators_and_flows ["threatslayer-lookup-price"] = s_update_threatslayer_lookup_price
indicators_and_flows ["threatslayer-expenses"] = s_update_threatslayer_expenses
indicators_and_flows ["token-price"] = s_update_token_price
indicators_and_flows ["contradiction-loss"] = s_update_contradiction_loss
indicators_and_flows ["crypto-hype"] = s_update_crypto_hype
indicators_and_flows ["clock"] = s_update_clock
indicators_and_flows ["scam-upkeep-rate"] = s_update_scam_upkeep_rate
indicators_and_flows ["scam-profit-rate"] = s_update_scam_profit_rate
indicators_and_flows ["scam-page-success-rate"] = s_update_scam_page_success_rate
indicators_and_flows ["scam-page-visit-rate"] = s_update_scam_page_visit_rate
indicators_and_flows ["page-visit-rate"] = s_update_page_visit_rate
indicators_and_flows ["threatslayer-upkeep-rate"] = s_update_threatslayer_upkeep_rate
indicators_and_flows ["interlock-self-invest-rate"] = s_update_interlock_self_invest_rate
indicators_and_flows ["threatslayer-revenue-rate"] = s_update_threatslayer_revenue_rate
indicators_and_flows ["threatslayer-share-rate"] = s_update_threatslayer_share_rate
indicators_and_flows ["resolution-rate"] = s_update_resolution_rate
indicators_and_flows ["grey-area-entity-rate"] = s_update_grey_area_entity_rate
indicators_and_flows ["threatslayer-lookup-rate"] = s_update_threatslayer_lookup_rate
indicators_and_flows ["threatslayer-abandonment-rate"] = s_update_threatslayer_abandonment_rate
indicators_and_flows ["threatslayer-adoption-rate"] = s_update_threatslayer_adoption_rate
indicators_and_flows ["threatslayer-investment-rate"] = s_update_threatslayer_investment_rate
indicators_and_flows ["intr-divest-rate"] = s_update_intr_divest_rate
indicators_and_flows ["crypto-divest-rate"] = s_update_crypto_divest_rate
indicators_and_flows ["intr-invest-rate"] = s_update_intr_invest_rate
indicators_and_flows ["crypto-invest-rate"] = s_update_crypto_invest_rate
indicators_and_flows ["money-mint-rate"] = s_update_money_mint_rate
indicators_and_flows ["money-reclaim-rate"] = s_update_money_reclaim_rate
indicators_and_flows ["reward-to-held-rate"] = s_update_reward_to_held_rate
indicators_and_flows ["token-unstake-rate"] = s_update_token_unstake_rate
indicators_and_flows ["token-stake-rate"] = s_update_token_stake_rate
indicators_and_flows ["token-unhold-rate"] = s_update_token_unhold_rate
indicators_and_flows ["token-hold-rate"] = s_update_token_hold_rate
indicators_and_flows ["foundation-unhold-rate"] = s_update_foundation_unhold_rate
indicators_and_flows ["foundation-hold-rate"] = s_update_foundation_hold_rate
indicators_and_flows ["rewards-unhold-rate"] = s_update_rewards_unhold_rate
indicators_and_flows ["rewards-hold-rate"] = s_update_rewards_hold_rate
indicators_and_flows ["partners-hold-rate"] = s_update_partners_hold_rate
indicators_and_flows ["advisors-hold-rate"] = s_update_advisors_hold_rate
indicators_and_flows ["outlier-ventures-hold-rate"] = s_update_outlier_ventures_hold_rate
indicators_and_flows ["team-founders-hold-rate"] = s_update_team_founders_hold_rate
indicators_and_flows ["presale-3-hold-rate"] = s_update_presale_3_hold_rate
indicators_and_flows ["presale-2-hold-rate"] = s_update_presale_2_hold_rate
indicators_and_flows ["presale-1-hold-rate"] = s_update_presale_1_hold_rate
indicators_and_flows ["community-sale-hold-rate"] = s_update_community_sale_hold_rate
stock_driven_flow_adjust = {}
stock_driven_flow_adjust ["flow-adjustments"] = adjust_all_flows
flow_commit = {}
flow_commit ["scam-upkeep-rate"] = s_commit_scam_upkeep_rate
flow_commit ["scam-profit-rate"] = s_commit_scam_profit_rate
flow_commit ["scam-page-success-rate"] = s_commit_scam_page_success_rate
flow_commit ["scam-page-visit-rate"] = s_commit_scam_page_visit_rate
flow_commit ["page-visit-rate"] = s_commit_page_visit_rate
flow_commit ["threatslayer-upkeep-rate"] = s_commit_threatslayer_upkeep_rate
flow_commit ["interlock-self-invest-rate"] = s_commit_interlock_self_invest_rate
flow_commit ["threatslayer-revenue-rate"] = s_commit_threatslayer_revenue_rate
flow_commit ["threatslayer-share-rate"] = s_commit_threatslayer_share_rate
flow_commit ["resolution-rate"] = s_commit_resolution_rate
flow_commit ["grey-area-entity-rate"] = s_commit_grey_area_entity_rate
flow_commit ["threatslayer-lookup-rate"] = s_commit_threatslayer_lookup_rate
flow_commit ["threatslayer-abandonment-rate"] = s_commit_threatslayer_abandonment_rate
flow_commit ["threatslayer-adoption-rate"] = s_commit_threatslayer_adoption_rate
flow_commit ["threatslayer-investment-rate"] = s_commit_threatslayer_investment_rate
flow_commit ["intr-divest-rate"] = s_commit_intr_divest_rate
flow_commit ["crypto-divest-rate"] = s_commit_crypto_divest_rate
flow_commit ["intr-invest-rate"] = s_commit_intr_invest_rate
flow_commit ["crypto-invest-rate"] = s_commit_crypto_invest_rate
flow_commit ["money-mint-rate"] = s_commit_money_mint_rate
flow_commit ["money-reclaim-rate"] = s_commit_money_reclaim_rate
flow_commit ["reward-to-held-rate"] = s_commit_reward_to_held_rate
flow_commit ["token-unstake-rate"] = s_commit_token_unstake_rate
flow_commit ["token-stake-rate"] = s_commit_token_stake_rate
flow_commit ["token-unhold-rate"] = s_commit_token_unhold_rate
flow_commit ["token-hold-rate"] = s_commit_token_hold_rate
flow_commit ["foundation-unhold-rate"] = s_commit_foundation_unhold_rate
flow_commit ["foundation-hold-rate"] = s_commit_foundation_hold_rate
flow_commit ["rewards-unhold-rate"] = s_commit_rewards_unhold_rate
flow_commit ["rewards-hold-rate"] = s_commit_rewards_hold_rate
flow_commit ["partners-hold-rate"] = s_commit_partners_hold_rate
flow_commit ["advisors-hold-rate"] = s_commit_advisors_hold_rate
flow_commit ["outlier-ventures-hold-rate"] = s_commit_outlier_ventures_hold_rate
flow_commit ["team-founders-hold-rate"] = s_commit_team_founders_hold_rate
flow_commit ["presale-3-hold-rate"] = s_commit_presale_3_hold_rate
flow_commit ["presale-2-hold-rate"] = s_commit_presale_2_hold_rate
flow_commit ["presale-1-hold-rate"] = s_commit_presale_1_hold_rate
flow_commit ["community-sale-hold-rate"] = s_commit_community_sale_hold_rate
stock_reduction = {}
stock_reduction ["scam-profits"] = s_reduce_scam_profits
stock_reduction ["potential-scam-profits"] = s_reduce_potential_scam_profits
stock_reduction ["scam-page-visits"] = s_reduce_scam_page_visits
stock_reduction ["page-visits"] = s_reduce_page_visits
stock_reduction ["potential-page-visits"] = s_reduce_potential_page_visits
stock_reduction ["threatslayer-revenue"] = s_reduce_threatslayer_revenue
stock_reduction ["data-buyer-money"] = s_reduce_data_buyer_money
stock_reduction ["browsing-data"] = s_reduce_browsing_data
stock_reduction ["grey-area-entities"] = s_reduce_grey_area_entities
stock_reduction ["threatslayer-lookups"] = s_reduce_threatslayer_lookups
stock_reduction ["potential-threatslayer-lookups"] = s_reduce_potential_threatslayer_lookups
stock_reduction ["threatslayer-users"] = s_reduce_threatslayer_users
stock_reduction ["browser-users"] = s_reduce_browser_users
stock_reduction ["intr-investments"] = s_reduce_intr_investments
stock_reduction ["crypto-investments"] = s_reduce_crypto_investments
stock_reduction ["money-mint"] = s_reduce_money_mint
stock_reduction ["money-supply"] = s_reduce_money_supply
stock_reduction ["token-stake-pool"] = s_reduce_token_stake_pool
stock_reduction ["token-hold-pool"] = s_reduce_token_hold_pool
stock_reduction ["foundation-pool"] = s_reduce_foundation_pool
stock_reduction ["rewards-pool"] = s_reduce_rewards_pool
stock_reduction ["token-sell-pool"] = s_reduce_token_sell_pool
stock_reduction ["partners-pool"] = s_reduce_partners_pool
stock_reduction ["advisors-pool"] = s_reduce_advisors_pool
stock_reduction ["outlier-ventures-pool"] = s_reduce_outlier_ventures_pool
stock_reduction ["team-founders-pool"] = s_reduce_team_founders_pool
stock_reduction ["presale-3-pool"] = s_reduce_presale_3_pool
stock_reduction ["presale-2-pool"] = s_reduce_presale_2_pool
stock_reduction ["presale-1-pool"] = s_reduce_presale_1_pool
stock_reduction ["community-sale-pool"] = s_reduce_community_sale_pool
stock_cumulation = {}
stock_cumulation ["scam-upkeep"] = s_cumulate_scam_upkeep
stock_cumulation ["scam-profits"] = s_cumulate_scam_profits
stock_cumulation ["scam-page-successes"] = s_cumulate_scam_page_successes
stock_cumulation ["scam-page-visits"] = s_cumulate_scam_page_visits
stock_cumulation ["page-visits"] = s_cumulate_page_visits
stock_cumulation ["threatslayer-upkeep"] = s_cumulate_threatslayer_upkeep
stock_cumulation ["threatslayer-data-shared"] = s_cumulate_threatslayer_data_shared
stock_cumulation ["resolved-entities"] = s_cumulate_resolved_entities
stock_cumulation ["grey-area-entities"] = s_cumulate_grey_area_entities
stock_cumulation ["threatslayer-lookups"] = s_cumulate_threatslayer_lookups
stock_cumulation ["browser-users"] = s_cumulate_browser_users
stock_cumulation ["threatslayer-users"] = s_cumulate_threatslayer_users
stock_cumulation ["threatslayer-revenue"] = s_cumulate_threatslayer_revenue
stock_cumulation ["intr-investments"] = s_cumulate_intr_investments
stock_cumulation ["crypto-investments"] = s_cumulate_crypto_investments
stock_cumulation ["money-supply"] = s_cumulate_money_supply
stock_cumulation ["money-reclaimed"] = s_cumulate_money_reclaimed
stock_cumulation ["token-stake-pool"] = s_cumulate_token_stake_pool
stock_cumulation ["foundation-pool"] = s_cumulate_foundation_pool
stock_cumulation ["token-sell-pool"] = s_cumulate_token_sell_pool
stock_cumulation ["rewards-pool"] = s_cumulate_rewards_pool
stock_cumulation ["token-hold-pool"] = s_cumulate_token_hold_pool
psubs = [{ "policies": {}, "variables": indicators_and_flows }, { "policies": {}, "variables": stock_driven_flow_adjust }, { "policies": {}, "variables": flow_commit }, { "policies": {}, "variables": stock_reduction }, { "policies": {}, "variables": stock_cumulation }]
def run_organism (o):
    global cfg
    if isinstance (o, dict):
        splice_individual (o, cfg)
    elif isinstance (o, tuple):
        splice_individual (o [0], cfg)
    
    run_simulation ()


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
genome_pin_fitness = {}
genome_pin_fitness ["stim-contradiction-rate-change-max-stake"] = 0
genome_pin_fitness ["stim-contradiction-rate-change-lookup-fee"] = 0
genome_fitness ["stim-contradiction-rate-change-max-stake"] = [-1, -0.66, -0.33, 0, 0.33, 0.66, 1]
genome_fitness ["stim-anti-user-goal-progress-change-max-stake"] = [-1, -0.66, -0.33, 0, 0.33, 0.66, 1]
genome_fitness ["stim-token-price-delta-change-max-stake"] = [-1, -0.66, -0.33, 0, 0.33, 0.66, 1]
genome_fitness ["stim-contradiction-rate-change-stake-yield"] = [-1, -0.66, -0.33, 0, 0.33, 0.66, 1]
genome_fitness ["stim-anti-user-goal-progress-change-stake-yield"] = [-1, -0.66, -0.33, 0, 0.33, 0.66, 1]
genome_fitness ["stim-token-price-delta-change-stake-yield"] = [-1, -0.66, -0.33, 0, 0.33, 0.66, 1]
genome_fitness ["stim-contradiction-rate-change-lookup-fee"] = [-1, -0.66, -0.33, 0, 0.33, 0.66, 1]
genome_fitness ["stim-anti-user-goal-progress-change-lookup-fee"] = [-1, -0.66, -0.33, 0, 0.33, 0.66, 1]
genome_fitness ["stim-token-price-delta-change-lookup-fee"] = [-1, -0.66, -0.33, 0, 0.33, 0.66, 1]
genome_fitness ["stim-contradiction-rate-change-user-fee"] = [-1, -0.66, -0.33, 0, 0.33, 0.66, 1]
genome_fitness ["stim-anti-user-goal-progress-change-user-fee"] = [-1, -0.66, -0.33, 0, 0.33, 0.66, 1]
genome_fitness ["stim-token-price-delta-change-user-fee"] = [-1, -0.66, -0.33, 0, 0.33, 0.66, 1]
genome_fitness ["stim-contradiction-rate-change-buyback-amount"] = [-1, -0.66, -0.33, 0, 0.33, 0.66, 1]
genome_fitness ["stim-anti-user-goal-progress-change-buyback-amount"] = [-1, -0.66, -0.33, 0, 0.33, 0.66, 1]
genome_fitness ["stim-token-price-delta-change-buyback-amount"] = [-1, -0.66, -0.33, 0, 0.33, 0.66, 1]
genome_fitness ["stim-contradiction-rate-change-sell-amount"] = [-1, -0.66, -0.33, 0, 0.33, 0.66, 1]
genome_fitness ["stim-anti-user-goal-progress-change-sell-amount"] = [-1, -0.66, -0.33, 0, 0.33, 0.66, 1]
genome_fitness ["stim-token-price-delta-change-sell-amount"] = [-1, -0.66, -0.33, 0, 0.33, 0.66, 1]
genome_fitness ["stim-contradiction-rate-change-reward-amount"] = [-1, -0.66, -0.33, 0, 0.33, 0.66, 1]
genome_fitness ["stim-anti-user-goal-progress-change-reward-amount"] = [-1, -0.66, -0.33, 0, 0.33, 0.66, 1]
genome_fitness ["stim-token-price-delta-change-reward-amount"] = [-1, -0.66, -0.33, 0, 0.33, 0.66, 1]
genome_fitness ["stim-contradiction-rate-change-urgency"] = [-1, -0.66, -0.33, 0, 0.33, 0.66, 1]
genome_fitness ["stim-anti-user-goal-progress-change-urgency"] = [-1, -0.66, -0.33, 0, 0.33, 0.66, 1]
genome_fitness ["stim-token-price-delta-change-urgency"] = [-1, -0.66, -0.33, 0, 0.33, 0.66, 1]
fitness_top_n = []
fitness_top_n_per_gen = []
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



def generate_individual (genome, pin):
    individual = {}
    for g in genome:
        if pin.get (g) == None:
            values = genome [g]
            individual [g] = random.choice (values)
        else:
            individual [g] = pin.get (g)
        

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


def create_pop (genome, pin, n):
    rn = range (n)
    pop = []
    for i in rn:
        repeat = True
        while repeat:
            ind = generate_individual (genome, pin)
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


def quasi_umad (individual, pop_genome, pop_pin, addrate, remrate):
    new = {}
    for g in individual:
        if (not pop_pin.get (g) and mutate_maybe (addrate)):
            val = get_gene_val (pop_genome, g)
            if mutate_flip ():
                val = (val * -1)
            
            new [g] = val
        elif pop_pin.get (g):
            new [g] = pop_pin.get (g)
        else:
            new [g] = individual [g]
        

    for g in individual:
        if (not pop_pin.get (g) and mutate_maybe (remrate)):
            new [g] = 0
        elif pop_pin.get (g):
            new [g] = pop_pin.get (g)
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
    start_time = time.time ()
    fitness = create_pop (genome_fitness, genome_pin_fitness, 40)
    global fitness_top_n
    global fitness_top_n_per_gen
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

        evolve = (evolve and continue_evolving (fitness, fitness_gen, 150, 0, "="))
        tmp = sorted (fitness, key=get_fitness, reverse=False)
        keep = math.ceil (((20 / 100) * 40))
        del tmp [keep:]
        fitness = tmp
        push (fitness_top_n_per_gen, fitness)
        new = []
        kids = math.floor ((40 / keep))
        for i in fitness:
            k = 0
            while k < kids:
                new.append ((quasi_umad (i [0], genome_fitness, genome_pin_fitness, 6, 6), None))
                k = (k + 1)


        fitness_gen = (fitness_gen + 1)
        fitness_top_n = (fitness_top_n + fitness)
        tmp = sorted (fitness_top_n, key=get_fitness, reverse=False)
        keep = math.ceil (((20 / 100) * 40))
        del tmp [keep:]
        fitness_top_n = tmp
        fitness = new

    end_time = time.time ()
    return (end_time - start_time)


def main ():
    global sim_res
    genetic = True
    standard = False
    if (genetic == True and standard == True):
        return True
    elif genetic == True:
        total_time = run_evolution ()
        print (total_time)
    else:
        sim_res = run_simulation ()
    


main ()


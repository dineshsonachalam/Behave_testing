from behave import *
from twentyone import *

# 1
@given('a hand {total}')
def step_impl(context,total):
    context.dealer = Dealer()
    context.total = total


# 2
@given('a dealer')
def step_impl(context):
    context.dealer = Dealer()

# 3
@given('a {hand}')
def step_impl(context, hand):
    context.dealer = Dealer()
    context.dealer.hand = hand.split(',')
    # context object passed from step to step and its where we can store info used by other steps





# 1
@when('the round starts')
def step_imp(context):
    context.dealer.new_round()

# 2
@when('the dealer sums the cards')
def step_impl(context):
    context.dealer_total = context.dealer.get_hand_total()

# 3
@when('the dealer determines a play')
def step_impl(context):
    context.dealer_play = context.dealer.determine_play(context.total)




# 1
@then('the {total:d} is correct')
def step_impl(context, total):
    assert (context.dealer_total == total)




# 2
@then('the dealer gives itself two cards')
def step_impl(context):
    assert (len(context.dealer.hand)==2)

# 3
@then('the {play} is correct')
def step_impl(context,play):
    assert (context.dealer_play==play)



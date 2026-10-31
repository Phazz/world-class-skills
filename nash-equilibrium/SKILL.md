---
name: nash-equilibrium
description: Analyze strategic interactions through best responses and Nash equilibrium. Use for coordination, incentive design, or choices whose payoffs depend on other actors.
---

# Nash equilibrium: test incentives under mutual response

A Nash equilibrium is a strategy profile in which no player can improve their payoff by changing only their own strategy while the others keep theirs fixed. It need not be fair, efficient, unique, or the outcome people actually reach.

## Construct the game

Identify players, feasible strategies, information, timing, and payoffs. Distinguish simultaneous choices from observed sequential choices. Ask whether interaction repeats. Include outside options and reputational effects when relevant.

Use evidence for incentives. When only qualitative preferences are known, use rankings and conditional conclusions. Do not invent numerical utilities and then present the computed result as an empirical prediction. Mixed-strategy calculations require meaningful cardinal payoffs, not just rankings.

## Find and verify responses

For a small simultaneous game, present a payoff matrix with a clear player order and payoff convention. For each fixed choice by the other player, identify every best response, including ties. Pure equilibria are cells that are best responses for both players.

Check every claimed equilibrium using the unilateral-deviation test. State whether the search is exhaustive; checking selected profiles establishes only those candidates.

For a mixed-strategy analysis, or a sequential or incomplete-information game, read [advanced games](references/advanced-games.md). A pure-strategy search alone does not enumerate mixed equilibria.

## Use the result

This decision procedure is an applied adaptation:

1. Explain which incentives sustain the outcome and who would prefer a different one.
2. Separate individual stability from joint welfare. Explain what blocks an apparently better outcome.
3. Test sensitivity to uncertain payoffs, timing, information, and outside options.
4. If asked to improve the outcome, evaluate a concrete change to incentives, commitments, observability, or rules. Recompute responses after the change.
5. Return a conditional recommendation and the missing evidence most likely to change it. Do not treat a mathematical existence result as a behavioral forecast.

## Sanity example

An illustrative game, with higher numbers preferred and payoffs ordered (row, column):

| | Column cooperates | Column defects |
| --- | --- | --- |
| Row cooperates | (3, 3) | (0, 5) |
| Row defects | (5, 0) | (1, 1) |

Defection is each player's best response to either action, so mutual defection is the unique equilibrium of this one-shot game. Mutual cooperation benefits both more, but unilateral defection is profitable there. Repetition alone does not prove cooperation will occur.

## Completion check

The analysis is ready when every reported equilibrium passes the unilateral-deviation check, payoff assumptions and game timing are explicit, and the scope of the search is stated. If evidence supports only rankings, keep conclusions ordinal and conditional.

## Sources

- [Nash, Equilibrium points in n-person games (1950)](https://doi.org/10.1073/pnas.36.1.48).
- [Nash, Non-Cooperative Games, Princeton dissertation (1950)](https://library.princeton.edu/sites/g/files/toruqf6021/files/documents/Non-Cooperative_Games_Nash.pdf).

The practical workflow and example are pedagogical adaptations. Sequential, Bayesian, and repeated-game refinements extend beyond the basic equilibrium definition.

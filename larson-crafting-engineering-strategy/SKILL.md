---
name: larson-crafting-engineering-strategy
description: Develop engineering policies using Crafting Engineering Strategy. Use when recurring technical decisions need shared defaults, exceptions, and rollout mechanisms.
---

# Crafting Engineering Strategy: make decisions coherent

Apply a selective synthesis of Will Larson's *Crafting Engineering Strategy* (2025). Strategy should help real decisions converge under actual constraints. A project list, inspirational vision, or technology preference does not accomplish that on its own.

## Develop the strategy

1. **Explore.** Identify the recurring decision and why resolving it matters. Examine internal precedents, relevant external approaches, and the current environment. Bound research to what could change the decision.
2. **Diagnose.** Describe the constraints, tensions, and causal problems before choosing a solution. Seek perspectives that disagree with the initial framing. Distinguish observations from assumptions. Include organizational resistance and resource limits as conditions the strategy must address.
3. **Refine.** Test candidate approaches against the diagnosis. Use concrete cases, prototypes, or models when they resolve uncertainty. Update the diagnosis when tests reveal that the original problem was misunderstood.
4. **Set policy.** State the decisions people should make, the tradeoffs accepted, and the situations in which the policy applies. Connect each policy to the diagnosis. Include exceptions where real conditions require them.
5. **Operate.** Put the policy into the mechanisms where decisions happen. Establish accountability, feedback, and revision rather than treating publication as completion.

These stages are iterative: do not wait for a perfect diagnosis before testing a consequential assumption.

## Make the output usable

Use this original working format, shortened to fit the task:

- **Decision and scope:** who needs to decide what, and which situations are outside scope.
- **Diagnosis:** facts, constraints, competing perspectives, and consequential uncertainties.
- **Policies:** each chosen default, its rationale, rejected alternative, and cost accepted.
- **Execution:** first concrete actions, resources, owners, and the mechanism that makes the policy part of normal work.
- **Exceptions and revision:** who decides an exception, how its rationale is recorded, and what evidence triggers reconsideration.

Prefer wording that changes a decision. Replace “favor simplicity” with an applicable choice and its rationale. Keep a vision's desired future distinct from a strategy's choices and a plan's scheduled work.

## Stress-test

Apply the draft to two plausible decisions, including an awkward exception. Can separate teams reach compatible choices? Does any policy contradict another? Can the owners execute it with available resources? Does a disputed assumption have a practical test?

For example, a database-standardization policy must address migration cost and legitimate workload differences; merely naming the preferred database leaves the difficult decisions unanswered.

## Completion check

The draft is ready when the two decision trials produce compatible choices or explicit exceptions, each policy has a rationale and tradeoff, and adoption and revision have owners. Label untested assumptions and proposed ownership.

## Sources

- [Steps to build an engineering strategy](https://craftingengstrategy.com/strategy-steps/).
- [Diagnosis](https://craftingengstrategy.com/diagnosis/).
- [Setting policy](https://craftingengstrategy.com/policy/).
- [Operations](https://craftingengstrategy.com/operations/).

The working format and stress-test are adaptations. The diagnosis/policy tradition also draws on Richard Rumelt; do not attribute the entire tradition exclusively to Larson.

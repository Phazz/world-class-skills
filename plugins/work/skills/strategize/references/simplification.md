# Musk's simplification algorithm

Use the engineering method described in the 2021 Everyday Astronaut interview. Apply the method without imitating Musk's personality. Preserve this order: question requirements, delete, simplify, accelerate, automate.

## Run the sequence

1. **Question requirements.** Identify each requirement's purpose, supporting evidence, and accountable person. Distinguish actual constraints from inherited implementation choices. Expertise and seniority do not make an assumption correct.
2. **Delete.** Challenge whether each part or process step needs to exist. A deletion proposal should precede work to improve the same component. Occasional restoration can be evidence of real experimentation; do not turn the interview's deletion heuristic into a mandatory removal quota.
3. **Simplify and optimize.** Improve only what survived. Reduce unnecessary interfaces, handoffs, special cases, and duplication while retaining the intended outcome.
4. **Accelerate.** Shorten the remaining cycle after understanding the process. Do not make unnecessary work happen faster.
5. **Automate.** Automate the useful, understood process that remains. Revisit earlier steps when automation exposes an unnecessary requirement or step.

## Apply to an actual task

The following are agent-specific adaptations:

- Establish the outcome and a baseline: completion time, cost, error rate, or another metric the user values. Separate working time from queue time.
- Build a small ledger: item, purpose, evidence, owner or unknown owner, proposed action, and consequence. Prioritize consequential items rather than documenting every trivial detail.
- For deletion candidates, inspect consumers and dependencies. Define the smallest reversible trial, success signal, and restoration condition. An unidentified owner is a research gap, not permission to delete.
- Preserve verified safety, security, legal, and compatibility obligations while challenging how they are implemented. Resolve uncertain obligations before removing their protection.
- Measure the whole workflow after the change. A faster local step is not a win if it increases downstream failures or total effort.
- Before automation, compare saved recurring effort with implementation, maintenance, and exception-handling costs. Name a failure owner and a fallback when relevant.

In advisory work, return proposals. In implementation work, make only authorized changes and verify the affected behavior. The framework does not authorize destructive actions.

## Deliverable

Return the outcome, challenged assumptions, ordered changes, expected or measured effect, and next experiment. Clearly distinguish proposals from completed deletions. When a later step is premature, explain the earlier uncertainty that must be resolved.

## Completion check

The proposal is ready when each retained improvement follows a deletion decision and each deletion has a dependency check and restoration condition. For implementation, report observed whole-workflow results and unresolved failures; for advice, label effects as estimates. Stop at the earliest unresolved stage.

## Source

[Everyday Astronaut's Starbase tour and interview](https://everydayastronaut.com/starbase-tour-and-interview-with-elon-musk/) documents the five-step sequence. The ledger, measurements, and execution checks are original adaptations for agent work.

# World-class skills

Thinking frameworks for Claude Code, organized by the job you are doing rather than by author. Each skill is a job; inside it, the classic frameworks (Rumelt, Voss, Grove, Buffett, Taleb, Larson, and others) are lenses that the skill picks and loads only when the situation calls for them. You rarely need to name a skill: it triggers when you are researching, drafting, or reviewing a document that does that job.

## Install

One command installs every skill into every supported agent on the machine (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, Amp, and others):

```bash
npx skills add Phazz/world-class-skills -g -a '*' -y
```

Update all agents at once with `npx skills update -g -y`. See `npx skills add --help` to install a subset of skills or agents.

### Alternative: native plugins

The repo is also a Claude Code and Codex plugin marketplace (`work` and `personal` plugins), which adds background auto-update in Claude Code. Do not combine this with the `npx skills` install, or each skill will load twice.

```bash
claude plugin marketplace add Phazz/world-class-skills && claude plugin install work@world-class-skills
codex plugin marketplace add Phazz/world-class-skills && codex plugin add work@world-class-skills
```

## Skills

### Work

| Skill | Use it when you are... | Lenses |
| --- | --- | --- |
| `wc-negotiate` | preparing, evaluating, or replying in a negotiation with terms at stake | interests and BATNA, tactical empathy, deal setup |
| `wc-strategize` | writing or reviewing a strategy, setting technical policy, cutting something bloated down | strategy kernel, engineering policy, simplification |
| `wc-decide` | judging a consequential bet: a company, a long commitment, downside risk, others' reactions | owner economics, fragility, game theory |
| `wc-plan` | allocating across projects, annual or exec planning, writing or grading OKRs | project portfolio, engineering executive, OKRs |
| `wc-manage` | leading a team that is not delivering, delegating, preparing 1:1s, Staff+ leadership | managerial output, team states, one-on-ones, staff engineer |
| `wc-communicate` | writing a status update or a sensitive message, preparing a hard conversation | weekly update, cooperative conversations |
| `wc-grow` | designing offers, pricing, acquisition, or funnel economics | offers, leads, and money models |

### Personal

| Skill | Use it when you are... |
| --- | --- |
| `wc-get-direction` | deciding where your own time goes, choosing a role, or processing a setback |
| `wc-invest` | reviewing household investments, allocation, rebalancing, or an investment policy |
| `wc-learn` | starting memory-palace or Dominic number training (manual only: `/wc-learn` in Claude Code) |

## Layout

```
.claude-plugin/marketplace.json
plugins/<plugin>/.claude-plugin/plugin.json
plugins/<plugin>/skills/wc-<job>/SKILL.md          # description + lens router
plugins/<plugin>/skills/wc-<job>/references/*.md   # one framework per file, loaded on demand
plugins/<plugin>/evals/<case>/                  # trigger tests
```

## Maintain

- Every push to `main` is a release: `npx skills update -g -y` picks it up, and plugins have no `version`, so plugin installs track commits too.
- Before pushing: `claude plugin validate .`
- After changing a description, re-run the trigger tests: `claude plugin eval work --ablation none --runs 3 --no-publish` (and the same for `personal`). Each case asserts which skill fires; the `negative-*` cases assert that none does.
- Skill links between `work` and `personal` are relative paths that assume every `wc-*` folder sits side by side, as `npx skills` installs them.
- Add a framework by dropping a file into the right job's `references/` and adding a row to that job's lens table. Add a new job only when no existing description fits.

## Sources

Each lens file ends with its sources. The workflows are original operational adaptations of selected ideas, not summaries or reproductions of the books.

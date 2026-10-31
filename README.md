# Phazz skills

Thinking frameworks for Claude Code, organized by the job you are doing rather than by author. Each skill is a job; inside it, the classic frameworks (Rumelt, Voss, Grove, Buffett, Taleb, Larson, and others) are lenses that the skill picks and loads only when the situation calls for them. You rarely need to name a skill: it triggers when you are researching, drafting, or reviewing a document that does that job.

## Install

```bash
claude plugin marketplace add Phazz/skills
claude plugin install work@phazz-skills
claude plugin install personal@phazz-skills   # optional, personal machines
```

Then turn on background updates once per machine: `/plugin` → Marketplaces → `phazz-skills` → Enable auto-update. Without it, run `claude plugin marketplace update phazz-skills`.

The repository is public, so no credentials are needed. On a machine without a GitHub SSH key, set `CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1` so in-session installs and updates clone over HTTPS.

## Skills

### `work` plugin

| Skill | Use it when you are... | Lenses |
| --- | --- | --- |
| `work:negotiate` | preparing, evaluating, or replying in a negotiation with terms at stake | interests and BATNA, tactical empathy, deal setup |
| `work:strategize` | writing or reviewing a strategy, setting technical policy, cutting something bloated down | strategy kernel, engineering policy, simplification |
| `work:decide` | judging a consequential bet: a company, a long commitment, downside risk, others' reactions | owner economics, fragility, game theory |
| `work:plan` | allocating across projects, annual or exec planning, writing or grading OKRs | project portfolio, engineering executive, OKRs |
| `work:manage` | leading a team that is not delivering, delegating, preparing 1:1s, Staff+ leadership | managerial output, team states, one-on-ones, staff engineer |
| `work:communicate` | writing a status update or a sensitive message, preparing a hard conversation | weekly update, cooperative conversations |
| `work:grow` | designing offers, pricing, acquisition, or funnel economics | offers, leads, and money models |

### `personal` plugin

| Skill | Use it when you are... |
| --- | --- |
| `personal:get-direction` | deciding where your own time goes, choosing a role, or processing a setback |
| `personal:invest` | reviewing household investments, allocation, rebalancing, or an investment policy |
| `personal:learn` | starting memory-palace or Dominic number training (manual only: `/personal:learn`) |

## Layout

```
.claude-plugin/marketplace.json
plugins/<plugin>/.claude-plugin/plugin.json
plugins/<plugin>/skills/<job>/SKILL.md          # description + lens router
plugins/<plugin>/skills/<job>/references/*.md   # one framework per file, loaded on demand
plugins/<plugin>/evals/<case>/                  # trigger tests
```

## Maintain

- Plugins have no `version`, so every push to `main` is an update.
- Before pushing: `claude plugin validate .`
- After changing a description, re-run the trigger tests: `claude plugin eval work --ablation none --runs 3 --no-publish` (and the same for `personal`). Each case asserts which skill fires; the `negative-*` cases assert that none does.
- Add a framework by dropping a file into the right job's `references/` and adding a row to that job's lens table. Add a new job only when no existing description fits.

## Other agents

The SKILL.md files follow the open Agent Skills format. For Codex or other agents that read `~/.agents/skills`, clone the repo and symlink the job folders:

```bash
git clone https://github.com/Phazz/skills ~/src/phazz-skills && ln -s ~/src/phazz-skills/plugins/*/skills/* ~/.agents/skills/
```

Skill references between plugins use the `plugin:skill` names, which only resolve in Claude Code.

## Sources

Each lens file ends with its sources. The workflows are original operational adaptations of selected ideas, not summaries or reproductions of the books.

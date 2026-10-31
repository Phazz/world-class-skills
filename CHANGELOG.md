# Changelog

All notable changes to World-Class Skills are listed here. Versions follow [semantic versioning](https://semver.org/): a major version renames or removes a playbook, a minor version adds a playbook or framework, a patch version improves wording or triggering.

## [1.0.0] - 2026-10-31

First stable release.

### Added
- Eleven playbooks organized by the job to be done: `negotiation-playbook`, `strategy-playbook`, `decision-playbook`, `planning-playbook`, `management-playbook`, `communication-playbook`, `growth-playbook`, `ui-design-playbook`, `direction-playbook`, `investing-playbook`, `memory-playbook`.
- `ui-design-playbook`, adapting Anshu Chimala's seed-string, critic-loop, and cutting techniques and Sakana AI's String Seed of Thought research.
- Hand-drawn owl icon for both plugins, README header, and social preview.
- Line-art portraits of sixteen authors behind the playbooks, with per-image credits and licences.
- Trigger tests for every playbook, plus negative cases.
- Continuous integration and a tag-driven release workflow.

### Changed
- Renamed every skill from the `wc-` prefix to a `-playbook` suffix. Reinstall with `npx skills add Phazz/world-class-skills -g -y` and remove the old `wc-*` skills (`npx skills remove`).

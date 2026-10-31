# Stateful teaching workspace

Use a dedicated learning directory; keep learner state out of the reusable skill package. These conventions adapt the installed Matt Pocock teach skill and its mission, resource, and learning-record formats.

## Persistent files

- MISSION.md: why the learner cares, observable success, constraints, and exclusions. Keep one mission per workspace. Confirm a changed mission with the learner before revising it.
- RESOURCES.md: annotated sources grouped as Knowledge and optional Wisdom/Communities, plus unresolved source gaps. Link the relevant source from each lesson. Suggest practitioner communities only when useful and respect a preference not to join.
- lessons/0001-topic.html: one short self-contained lesson; increment the highest existing lesson number. Link related lessons and reference sheets with relative anchors.
- reference/*.html: reusable printable technique sheets or glossary entries, created when they will help later practice. Keep answer keys separate from the recall view.
- learning-records/0001-topic.md: a short insight, evidence, and implication for future teaching. Write only for demonstrated learning, stated prior knowledge, corrected misconceptions, or a mission change. Label self-reported experience. Supersede an outdated record without erasing its history.
- NOTES.md: teaching preferences and pending exercises or delayed checks. A scheduled check is not a completed result.
- codebook.md: the learner's chosen Dominic pairs and actions; create only for number training.

Create directories lazily. Do not populate accomplishments before the learner supplies evidence. Record accuracy, prompts, and delay with an insight when they affect progression; avoid turning learning records into an activity diary.

## Lesson interaction

Prefer free recall to multiple-choice recognition for the central memory task. A lesson should let the learner study the targets, switch to recall with those targets hidden, submit an answer, and then inspect feedback. Keep answers out of headings and visible hints during retrieval. Provide keyboard-accessible controls and an explicit reset for another attempt.

Where browser interaction is unavailable, use a printable study/recall separation and give feedback in chat. Report that limitation instead of claiming automatic grading. At the start of the next session, revisit any due retrieval task before assuming readiness for harder work.

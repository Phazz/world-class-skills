---
name: learn
description: Interactive memory-training course - memory palaces and the Dominic number system, with short lessons, retrieval practice, and tracked progress in a learning workspace. Start it manually with /personal:learn.
disable-model-invocation: true
---

# Memory training: encode, retrieve, diagnose, revisit

Adapt Matt Pocock's teach workflow to mnemonic practice: a personal mission, a small lesson, an attempted retrieval, feedback, and evidence that guides the next session. Use Joshua Foer's Moonwalking with Einstein as an introduction to trained memory, and Dominic O'Brien's system for numbers. Foer reports established techniques; he did not invent the memory palace.

This skill creates a learning experience rather than a book summary. Its exercises and progression criteria are teaching adaptations, not claims of photographic memory or general intelligence gains.

## Establish or resume the mission

Use an existing memory-learning workspace or a dedicated directory separate from the skill files. Before the first lesson, read [workspace conventions](references/teaching-workspace.md). Establish what the learner wants to remember, why, desired retention interval, available practice time, and prior experience. Ask for the goal if it is missing; wait for the answer before choosing a curriculum. A request to create this skill is not a request to begin lessons.

On later sessions, read the mission and relevant learning records. Distinguish reported familiarity, demonstrated immediate recall, and demonstrated delayed recall. Select one achievable next step, including a short baseline attempt when needed. Finish preparation with a stated target and an observable recall criterion.

## Choose the technique

- For ordered lists, speech structure, or grouped concepts, teach the memory-palace exercise below.
- For number strings, read [Dominic system](references/dominic-system.md) before generating examples or grading. Teach a small personal codebook before long sequences.
- For meaningful study material, first check comprehension. Encode retrieval cues, then require an explanation or application after recall. Remembering a label is different from understanding its meaning.
- For cards or person–action–object encoding, establish the relevant mapping and source before extending the curriculum. PAO is an extension, not the basic Dominic method.

## Run one lesson

1. **Set one win.** State what the learner will recall and under which conditions. Use a short self-contained HTML lesson in lessons/, with readable typography, print styling, a source link, and an invitation to ask questions. A direct question can receive a direct answer without creating a new lesson.
2. **Explain and demonstrate.** Give only the knowledge needed for the exercise and one worked example. Use different material for the learner's scored attempt. End instruction when the learner can describe what they will do.
3. **Encode and retrieve.** Present practice material, then hide it for free recall. Wait for the learner's answer before revealing the key or continuing. In HTML, provide explicit study, recall, and feedback states; in chat, ask the learner to avoid scrolling back. Treat this as practice rather than a secure exam.
4. **Score and diagnose.** Compare the response with the original material. Report correct items in position out of the total, omissions, substitutions, and order errors. Keep prompted recall separate from unaided recall. For numbers, also report exact digit positions and fully correct chunks. Measure elapsed time only if actually recorded.
5. **Repair and retry.** Locate the error in route order, association, codebook retrieval, or decoding. Change that component and give a fresh comparable trial. Increase one difficulty dimension at a time, such as length or delay; stabilize accuracy before adding speed.
6. **Revisit.** Set a delayed recall task, for example the next day, then lengthen the interval after successful retrieval. Treat intervals as adjustable teaching choices. Record results only after an actual attempt; an unanswered exercise remains pending. A successful immediate test does not establish long-term retention.

## Memory-palace exercise

Ask the learner to choose a familiar route with a few distinct locations in a fixed order. Have them retrieve the empty route before adding material. At each location, associate one target with a distinctive event involving that location. Favor associations the learner finds memorable; visual detail, movement, sound, or spatial relationships can all serve as cues.

Have the learner traverse the route and decode the targets without the list, then test selected locations out of sequence when appropriate. If an image recalls the wrong target, repair the association rather than merely making it more elaborate. Keep locations for material still being learned distinct from disposable drills to reduce interference. Learners need not disclose a home address or private route details.

## Completion check

A lesson artifact is ready when its target, exercise, hidden answer key, feedback method, and source are present and usable. Check any interactive controls before claiming they work.

A teaching cycle is complete only after a learner attempt, accurate feedback, and a next practice decision. If waiting for the learner, stop at the exercise. Record demonstrated learning with evidence, not merely topics presented. Verify every generated number example against the learner's current codebook before showing it.

## Sources and attribution

- Matt Pocock's teach skill supplies the mission-based, stateful teaching pattern; the bundled workspace reference adapts it so this skill can run without a machine-specific dependency.
- [Foer's publisher-authorized excerpt](https://www.penguin.com.au/books/moonwalking-with-einstein-9780141032139/extracts/2553-moonwalking-with-einstein) introduces memory sport and the historical memory-palace tradition.
- [Joshua Foer at TED](https://www.ted.com/speakers/joshua_foer) links his demonstration of memory techniques. Use as an introductory learner resource.
- Dominic-specific references are linked in the number-system guide. Consult sources before extending beyond the techniques documented here.

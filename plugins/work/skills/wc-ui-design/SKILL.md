---
name: wc-ui-design
description: Use when creating or redesigning the visual design of something - a landing page, app screen, dashboard, component, prototype, logo, icon, or theme - especially when the result must not look generic or AI-made. Seeds the creative direction with a random string, sets an ambitious brief, runs an independent critic loop, then strips what adds nothing. Not for fixing layout bugs, accessibility-only audits, or copywriting (use wc-communicate).
---

# UI design: escape the default, then earn the result

Models cannot act randomly, so asked for "a nice design" they converge on the most predictable one. This skill forces variety first and quality second. It adapts the techniques in Anshu Chimala's [How to turn your AI into a world-class designer](https://www.lennysnewsletter.com/p/how-to-turn-your-ai-into-a-world) (Lenny's Newsletter, 2026), whose seed-string technique applies Sakana AI's [String Seed of Thought](https://pub.sakana.ai/ssot/) research ([Misaki & Akiba, arXiv:2510.21150](https://arxiv.org/abs/2510.21150)).

## 1. Seed the direction

1. Generate a fresh random string with a shell command; never invent one:
   `head -c 48 /dev/urandom | base64 | tr -dc 'A-Za-z0-9' | head -c 32`
2. Before designing, derive the direction from the string and write the mapping down: e.g. character codes or a hash choose the hue family and palette, letter versus digit runs choose curves versus angles, symmetry, density, type personality, and the concept or metaphor. The mapping must actually constrain choices.
3. Use the string only as inspiration. It never appears in the design.
4. For several options, use one new string per option so they differ from each other, not just from the default.

Skip seeding when the user or an existing brand already fixes the direction; seed only the parts left open.

## 2. Write an ambitious brief

Turn the seeded direction into a specific brief: a named inspiration (a game, an era, a material, an interior style) and how it shapes colour, layout, type, and motion. When unsure, sketch several broad directions, let the user pick or combine, then write the build prompt for the chosen one. Ambition is the goal; generic "clean and modern" is the failure mode.

## 3. Build, then let an independent critic judge

1. Build the design and capture screenshots at the sizes that matter (for icons: 512, 32, and 16 px; for pages: desktop and mobile).
2. Ask a separate critic - a subagent with a fresh context that sees only the screenshots and the brief - for a 0-10 score and specific feedback. Keep the critic prompt identical across rounds.
3. Iterate until the critic gives 9/10 or higher, or until two rounds stop improving the score; then report the plateau instead of looping.

## 4. Enrich only where it earns its place

Where the brief calls for it and tools are available, add generated imagery, textures, or motion (looping clips on a solid background with the background removed, or transitions between keyframes). Keep API keys in a gitignored file and set a spend limit; never ship keys.

## 5. Cut

Models rarely remove things. End with a deletion pass: drop glows, gradients, redundant labels, unnecessary containers, and custom components where native ones work. Re-run the critic after cutting.

## Deliverable

Return the design (or options), and for each: the seed string, the string-to-design mapping, the brief, the critic's final score and remaining notes, and what was cut. For icons and logos, include a contact sheet at all target sizes on light and dark backgrounds.

## Sources

- Anshu Chimala, [How to turn your AI into a world-class designer](https://www.lennysnewsletter.com/p/how-to-turn-your-ai-into-a-world), Lenny's Newsletter, 2026: seed strings, ambitious prompts, critic subagents, image and video generation, and cutting elements.
- Sakana AI, [String Seed of Thought](https://pub.sakana.ai/ssot/); Kou Misaki and Takuya Akiba, [String Seed of Thought: Prompting LLMs for Distribution-Faithful and Diverse Generation](https://arxiv.org/abs/2510.21150), arXiv:2510.21150.

The workflow above is an operational adaptation of these sources, not a reproduction of the article.

---
name: image-prompt-qa
description: Diagnose and repair an existing image prompt for the exact failure reported by the user, including human references, photobook compositions, product identity, lighting, composition, editing, and unnecessary repetition. Preserve working decisions and use the smallest correction that solves the problem. Use for requested repairs, not new creative briefs or automatic review after prompt creation.
---

# Image Prompt QA

Repair an existing image prompt when the user asks for a correction. This skill works independently with prompts from GORVET, photobook templates, or any other source. It does not require a prior creative-direction approval, run after every prompt, generate images, or rebuild the creative brief.

## Routing within Creative Suite

Select this skill for an explicitly requested repair of an existing prompt, including prompts for promotional designs. Do not select it merely because the user shows a poster and wants its content, layout, or hierarchy redesigned: read `../poster-promotional-design/SKILL.md` for that task when available. New scene direction and image-prompt development belong to `../luces-camara-prompt/SKILL.md`. Do not chain these skills automatically or claim a missing sibling skill was applied.

## Repair contract

Use the original prompt as the base. Identify the reported failure and change only the instructions responsible for it. Preserve all working decisions, wording, paragraph order, and template blocks unless changing them is necessary to solve that failure.

A repair may add, replace, or remove a phrase or block. Prefer replacing an ambiguous instruction to appending several synonyms. Do not polish or expand unrelated content. If the user asks to shorten or deduplicate the prompt, removing repetition and joining blocks are permitted; preserve every distinct visual decision and constraint.

## Inputs and diagnosis

1. Read the original prompt and the user's stated problem. If the prompt is missing, request it. Ask for a missing detail only when it changes the repair.
2. Determine the intended scene and which reference controls each attribute. Use supplied images when the host can inspect them; do not claim to have viewed an absent image or promise a guaranteed result.
3. Identify the instruction likely responsible for the failure and select the smallest repair. Without a result image, frame the diagnosis as a likely textual cause rather than a confirmed visual observation.
4. Return the complete repaired prompt in its original language. If the user supplied parallel language versions, apply the equivalent correction to both without adding new details.

## References and selection

A reference may control a person's identity, a product, pose, clothing, composition, style, or a base image for editing. Preserve only the attributes assigned to it. Do not inherit its people or background when it is only a style or lighting reference.

For human identity:

- Preserve the identity of each selected person, their relevant proportions, and any age or gender constraints already requested.
- Follow the requested selection: everyone, one identified person, the person in the foreground, or another specified subset. If that selection is genuinely ambiguous and affects the correction, ask instead of inventing it.
- Preserve `the reference person(s)` when it is an established photobook convention. Do not replace it with `group`, `person`, or another label just to improve style.
- In other prompts, keep the existing unambiguous reference wording; there is no mandatory English label. Clarify singular, plural, or selection only when needed to solve the reported failure.
- Keep `Maintain the exact number of people from the reference image.` when all people must appear. If only a subset is requested, correct a conflicting count instruction to that subset; do not import everyone automatically.
- A selfie supplied as an identity reference does not require a selfie composition in the final image. If unintended selfie framing is the reported failure, adjust the framing or the reference's role. If the user wants a selfie composition, preserve it.

For product or object references, preserve the requested design, proportions, geometry, colors, label, and branding. Do not introduce human-reference rules into a product prompt.

## Repair focus

Select the relevant case; do not fill every category:

- **Identity or selection:** clarify who to preserve and what the reference controls.
- **Anatomy or proportion:** correct the responsible pose, framing, scale, or proportion instruction while retaining identity.
- **Pasted-face appearance or compositing:** correct continuity of face, neck, body, light, shadows, color, reflections, or perspective only where it fails.
- **Product fidelity:** clarify the reference's design constraints; do not redesign the object or repeat the same fidelity instruction in several forms.
- **Lighting or composition:** resolve the conflicting light source, focus, framing, scale, hierarchy, or text area. Retain compatible decisions.
- **Theme or narrative:** correct the mismatched wardrobe, setting, props, action, emotion, or tone that the user identified.
- **Editing or restoration:** delimit the requested change and preserve unaffected areas and original attributes.
- **Length or repetition:** keep one formulation per visual decision, remove equivalent adjectives and explanations, and retain distinct requirements. Do not impose a word quota or a two-line template.

For a GORVET prompt, its story, environment, technique, emotion, narrative structure, and tone are decisions to preserve or repair as relevant. They are not six new sections to add. A photobook template does not need conversion to GORVET.

## Template preservation

Keep the opening, `If male:` / `If female:` blocks, wardrobe, pose, environment, and restrictions unless they cause the reported failure. If multiple lines encode the same conflicting instruction, correct those lines together; one-line changes must not leave the contradiction elsewhere.

Do not add a creative-direction phase, a marketing closing, a GORVET attribution, or image-generation instructions to the repaired prompt. Keep existing material outside the prompt separate from the text intended for the generator.

## Output

Use the user's language for a brief diagnosis, then return the complete corrected prompt. Preserve the prompt's language and format except where the requested repair requires a change. No second approval is needed for a requested repair.

## Final review

Verify that the reported problem has been addressed, all unrelated decisions remain intact, references select the intended people or objects, and no contradictory instruction survives. Every added phrase must add control needed for the repair. If a contradiction reflects an unresolved user choice, ask for that choice rather than silently dropping a requirement.

## Examples of scope

- A photobook prompt uses `the reference person(s)` and the user reports a pasted-face appearance: preserve that label, person count, theme, and wardrobe blocks; repair only the integration instruction.
- A perfume prompt repeats its atmosphere and the user asks to shorten it: remove equivalent mood descriptions while preserving product identity, lighting, background, copy space, and aspect ratio.
- A reference contains three people but the user wants only the foreground person: preserve that person's identity and correct any instruction that unnecessarily requires all three. Do not rewrite the scene around a group.

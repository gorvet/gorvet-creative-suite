---
name: image-prompt-qa
description: Review and correct production image prompts that use human reference photos. Keep the original prompt as the base and correct only the exact reported failure with the minimum necessary change.
---

# Image Prompt QA

Review a production image prompt and correct only the exact problem reported by the user.

## Main rule
Treat the original prompt as the base.

Keep the original structure.
Keep the original paragraph order.
Keep all working blocks unchanged.

Do not rewrite the prompt for style, clarity, fluency, elegance, or completeness.
Do not improve anything that the user did not report as broken.

Correct the reported failure with the minimum necessary intervention.
That intervention may be:
- adding one line;
- modifying one line;
- replacing one line or block.

Use whichever of those three solves the problem with the smallest change.

## What to protect
1. Preserve the likeness of the reference person(s).
2. Maintain correct head-body proportions.
3. Maintain correspondence with the requested theme.

## Fixed rules
- Use `the reference person(s)` for the human reference.
- Keep `Maintain the exact number of people from the reference image.` when relevant.
- Do not use `selfie`.
- Do not use `group` or `person` as a replacement label for `the reference person(s)`.
- Do not leave contradictions.

## How to work
1. Read the original prompt.
2. Read the user's reported problem literally.
3. Find the exact line or block likely causing that problem.
4. Decide the smallest valid correction: add, modify, or replace.
5. Return the full prompt with only that correction applied.

## What not to do
- Do not rewrite the opening line unless it is causing the reported problem.
- Do not change paragraph order.
- Do not change `If male:` / `If female:` unless they are causing the reported problem.
- Do not change wardrobe, environment, pose, lighting, or restrictions unless they are causing the reported problem.
- Do not replace valid original wording just because another wording sounds better.

## Repair focus
- If the problem is likeness: correct only identity wording.
- If the problem is head/body proportion: correct only anatomy or proportion wording.
- If the problem is theme fidelity: correct only wardrobe, place, props, or theme details.
- If the problem is pasted-face look or poor scene integration: correct only the wording responsible for integration of face, neck, body, lighting, shadows, color cast, reflections, atmospheric effects, or continuity.

## Output
Reply briefly.

**Diagnosis:** one short sentence.

**Corrected prompt:** the full prompt with only the minimum necessary correction applied.

## Final check
Before answering, verify:
- the original structure is preserved;
- only the reported problem was corrected;
- the correction is the minimum necessary one;
- `the reference person(s)` is preserved correctly;
- no `selfie` appears;
- no contradiction remains.

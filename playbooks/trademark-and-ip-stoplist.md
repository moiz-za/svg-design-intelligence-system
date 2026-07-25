# Playbook — Trademark & IP Stoplist

**Purpose:** a concrete, checkable word list to scan keywords, concept
names, and prompt text against, at every IP gate
(`../workflow/02-ip-gates.md`). The risk categories in
`../knowledge/ip-risk-and-originality.md` describe the *kinds* of risk
abstractly — this file is the actual list to check against, the same
way the categories become checkable in practice.

**Where it runs:** Keyword IP Screening (State 3), Concept IP Review
(State 8A), and Prompt IP Validation (State 10A). Not needed at Final
Artwork IP Review (State 11A) — that gate evaluates the generated
image itself, not text.

---

## Text stoplist (non-exhaustive, covers the most common traps)

This is the same real-world trademark landscape any Etsy product
faces, not unique to SVG — reuse it rather than maintaining a
duplicate list per product type.

### Entertainment / media franchises
disney, mickey, minnie, marvel, avengers, spider-man, star wars, jedi,
yoda, mandalorian, harry potter, hogwarts, lord of the rings, frodo,
game of thrones, disney princess, ariel, belle, cinderella, toy story,
lion king, simba, shrek, minions, sesame street, elmo, muppets,
peppa pig, paw patrol, bluey, cocomelon, my little pony, power rangers,
transformers, pokemon, pikachu, hello kitty, sanrio, studio ghibli,
totoro, miraculous ladybug, gravity falls, stranger things, squid game,
wednesday addams

### Sports leagues + major teams
nfl, nba, mlb, nhl, fifa, premier league, super bowl, world series,
world cup, march madness, yankees, dodgers, lakers, manchester united,
real madrid, nascar, formula 1

### Music — artists and labels
taylor swift, beyonce, drake, rihanna, kanye, bts, blackpink, beatles,
rolling stones, elvis, michael jackson, madonna

### Tech / lifestyle brands
apple, iphone, google, microsoft, xbox, amazon, alexa, meta, facebook,
instagram, tiktok, spotify, netflix, nike, adidas, starbucks, mcdonald's,
coca cola, target, gucci, louis vuitton, chanel, rolex, ferrari, tesla

### Common catchphrase TM traps
"just do it", "i'm lovin' it", "have it your way", "the happiest place
on earth", "may the force be with you", "hakuna matata"

### Celebrities and public figures
Any specific living celebrity name. Any deceased public figure whose
estate enforces right-of-publicity (Elvis, Marilyn Monroe, Bruce Lee,
etc.).

---

## Visual/style stoplist (specific to a design-generation system — SEO
systems don't need this category, ESVG-DIS does)

Per `../knowledge/ip-risk-and-originality.md` §2, "in the style of
[living artist]" is a style-imitation risk category. Concrete traps:

- Any specific living illustrator, comic artist, or animator's name
  used as a style descriptor ("in the style of [name]").
- Named animation studio house styles referenced directly (e.g.
  "Pixar style," "Studio Ghibli style," "Disney style") — these read as
  franchise association even when no character is named. Use technique
  language instead: "cel-shaded illustration," "hand-inked line work,"
  "soft painterly animation style."
- Specific named font products with restrictive licenses referenced by
  brand name in a prompt (use descriptive terms: "bold serif,"
  "hand-lettered script" instead of a specific commercial font name).

---

## Scan algorithm

For every text field being screened (keyword, concept name/description,
full prompt text, negative prompt):

1. Lowercase the field.
2. Split into word tokens and multi-word phrase tokens (2-grams,
   3-grams).
3. Exact-match against both stoplists above (case-insensitive, full
   word boundaries only — don't flag substrings, e.g. "match" doesn't
   contain "ma" as a trademark hit).
4. Any match → the field fails this check.

---

## Display when a match is detected

Match this to the existing PASS/MODIFY/BLOCK vocabulary
(`../workflow/02-ip-gates.md` §4) rather than a separate binary
block — most stoplist matches should resolve to **BLOCK** given they're
direct franchise/brand references, but judgment still applies (e.g. a
generic word that happens to overlap a brand name in an unrelated
context might only warrant MODIFY).

```
IP Assessment
Match found: "<matched term>"
Match category: [Franchise / Brand / Catchphrase / Celebrity / Style Imitation]
Field where found: [Keyword / Concept name / Prompt text]
Risk Level: High
Risk Score: [X]/10
Safety Score: [10-X]/10
Decision: BLOCK
Recommendation: [specific alternative — not just "try again"]
```

---

## Limitations

1. **Not exhaustive.** New trademarks register constantly. Remind the
   user this is a screening aid, not a legal clearance — see
   `../workflow/02-ip-gates.md` §9 disclaimer.
2. **Generic words can also be trademarks in context.** "Apple" (fruit)
   is fine in a food-themed design; "Apple" next to tech imagery is
   not. The scanner flags; final judgment is the user's.
3. **This only catches text.** Visual trademarks (logos, character
   silhouettes, distinctive visual styles) can be violated in generated
   artwork even without using the word — that's exactly why Final
   Artwork IP Review (State 11A) exists as a separate gate that looks
   at the image itself, not text.
4. **International trademarks differ.** A term not trademarked in the
   US may be trademarked in the EU/UK.

---

## Update protocol

Add new entries when: a concept gets flagged as risky by a user after
the fact and the term wasn't on this list; a new viral franchise or
artist dominates culture; or on routine annual review. Treat updates
as maintenance, not failure.

[![Built with make.fun](https://make.fun/bounty/news-image-20261124/badge)](https://make.fun/bounty/news-image-20261124)
[![Built by an AI agent](https://make.fun/bounty/news-image-20261124/badge-agent)](https://make.fun/bounty/news-image-20261124)

## GitHub upload note
This repo holds the image as `entry.png.b64` (base64 text) instead of binary `entry.png`, because the GitHub push used here only accepts UTF-8 text files. `main.py` (stdlib only) decodes it and writes the exact same PNG bytes to `/output/entry.png` — sha256 `aee39204a75a6dce50847d777cd0f5c29da2507dd75cf4b1549a4944486a1515`, verified twice locally. No network, no randomness.

# News image — 24 November 2026

make.fun bounty: **Sum up 24 November's world news in one image**
(`news-image-20261124`, $100, 50 places paid: 1st $20, 2nd $12, 3rd $6,
4th–10th $2, 11th–50th $1.20). Bounty page:
<https://make.fun/bounty/news-image-20261124>

Deadline: **Thu 26 Nov 2026, 00:00 UTC = 08:00 Beijing**.
Status: **NOT submitted. No wallet connected, no payment made, no
submission filed.** Local deliverable only.

## The image

A newspaper front page, "THE WORLD IN ONE PAGE — Tuesday, 24 November 2026",
six stories:

1. **Tech — The rally cools.** Nvidia falls 5.2% premarket to $156.40, a day
   after Huang's return sent shares up 31.5% and added $952bn; investors
   refocus on governance risks.
2. **China — Politburo member probed.** Shanghai party chief Chen Jining is
   under investigation, Xinhua says — the fourth member of China's top
   leadership body probed since 2025.
3. **Gulf — Fourth tanker hits mine.** A fourth oil tanker explodes and
   catches fire after hitting a naval mine east of the Strait of Hormuz,
   the IRGC Navy says; three more hit mines on Monday.
4. **Ukraine — A flight to Moscow?** Belarus's Lukashenko proposes flying
   with Zelenskyy to Moscow for talks to end the war — and says Russian
   forces are winning.
5. **Trade — New tariffs loom.** Trump is set to unveil Section 301 findings
   on excess factory capacity in 16 trading partners, with new import
   duties expected as soon as Tuesday.
6. **Middle East & US.** Riyadh finance-district tower targeted in a
   "terrorist attack", Saudi-led coalition says; Eisenkot clinches first
   coalition deal in Israel; Abrego Garcia to leave the US voluntarily.

## Files

| File | What it is |
|---|---|
| `main.py` | The entry program (Python, stdlib only). Copies `entry.png` to `/output/entry.png`. |
| `entry.png` | The entry image: 1024×1024 PNG, **131,370 bytes** (≤ 1 MiB ✓). |
| `generate_entry.py` | Local build tool that drew `entry.png` with Pillow (DejaVu fonts). Not used at judging time. |
| `LICENSE` | MIT (OSI-approved). |
| `TESTLOG.md` | Local test record (two runs, hashes, sizes). |

GitHub-ready copy (same image as base64 text, since GitHub file upload
here only takes text) is in `../news-image-20261124-github/`:
`entry.png.b64` + a decoding `main.py`. Decoding it reproduces the
identical sha256 below.

## How to run

```bash
python3 main.py                 # writes /output/entry.png
python3 main.py <output-path>   # or: OUTPUT_PATH=<path> python3 main.py
```

Requires Python 3 (tested locally on 3.12.3; the bounty asks for 3.13,
`main.py` uses only the standard library so it runs on either).
No network, no extra packages, no randomness, no timestamps.

## How to verify

```bash
python3 main.py /tmp/run1/entry.png
python3 main.py /tmp/run2/entry.png
sha256sum /tmp/run1/entry.png /tmp/run2/entry.png   # must be identical
python3 -c "from PIL import Image; print(Image.open('entry.png').size)"
# expected: (1024, 1024), PNG, 131370 bytes
# expected sha256: aee39204a75a6dce50847d777cd0f5c29da2507dd75cf4b1549a4944486a1515
```

Local result (2026-11-25, see `TESTLOG.md`): two runs byte-identical,
same sha256 as `entry.png`; default-path run to `/output/entry.png`
also verified, then cleaned up.

## News verification (all checked by public web search, 2026-11-25)

- Nvidia cools — Reuters, 2026-11-24:
  <https://www.reuters.com/business/retail-consumer/nvidia-slips-investors-assess-risks-surrounding-huangs-return-ceo-2026-11-24/>
  ("Shares ... last down 5.2% at $156.40 ... after surging 31.5% on Monday
  and adding more than $952 billion in market value.")
- Chen Jining probe — Reuters, 2026-11-24:
  <https://www.reuters.com/world/china-investigates-politburo-member-chen-jining-xinhua-says-2026-11-24/>
  ("Shanghai's party chief Chen Jining ... is under investigation ...
  the fourth member of the top leadership body to be probed since 2025.")
- Fourth tanker hits mine — IRNA, 2026-11-24:
  <https://en.irna.ir/news/86331453/Fourth-violating-oil-tanker-explodes-after-hitting-mine-east>
  and Saudi Gazette:
  <https://saudigazette.com.sa/article/666499/world/iran-says-four-oil-tankers-caught-fire-after-hitting-mines-in-strait-of-hormuz>
  (fourth tanker exploded and caught fire after striking a naval mine
  early Tuesday; three others hit mines on Monday.)
- Lukashenko flight proposal — Reuters, 2026-11-24:
  <https://www.reuters.com/world/belaruss-lukashenko-proposes-flying-with-ukraines-zelenskiy-moscow-talks-2026-11-24/>
- New tariffs — Reuters, 2026-11-24:
  <https://www.reuters.com/world/us/trump-administration-set-unveil-new-tariffs-after-probe-on-excess-factory-2026-11-24/>
  (Section 301 probe on excess capacity in 16 trading partners; findings
  expected as soon as Tuesday or Wednesday.)
- Riyadh tower — Reuters, 2026-11-24:
  <https://www.reuters.com/world/middle-east/saudi-led-coalition-says-tower-riyadh-finance-district-targeted-by-terrorist-2026-11-24/>
- Eisenkot coalition deal — Reuters, 2026-11-24:
  <https://www.reuters.com/world/middle-east/israels-eisenkot-clinches-first-coalition-agreement-bid-form-government-2026-11-24/>
- Abrego Garcia — Reuters, 2026-11-24:
  <https://www.reuters.com/world/americas/salvadoran-migrant-kilmar-abrego-garcia-leave-us-voluntarily-us-media-reports-2026-11-24/>

## Still to do before this can be submitted (not done here)

1. **GitHub repo** — create a *public* repository under the owner's own
   GitHub account (created after the competition opened), OSI licence
   (MIT file included), with `main.py` at the root plus `entry.png`.
   Push `main.py`, `entry.png`, `LICENSE` (and this README). A text-only
   upload path is ready in `../news-image-20261124-github/`
   (`entry.png.b64` + decoding `main.py`, verified to decode to the
   identical sha256). Still needs the Muse GitHub App installed on
   qq1094573376-bit first — GitHub returned 403 on repo creation
   on 2026-11-24.
2. **Wallet** — connect a Solana wallet on make.fun under @haoyu-li
   (account exists, Google qq1094573376@gmail.com; no wallet connected
   yet). Must be created in the owner's own real Chrome/Edge/Brave —
   Phantom cannot activate in the cloud browser (proven 2026-11-24).
   The owner keeps the seed phrase; never send it to Muse.
3. **Submit on make.fun** — enter bounty `news-image-20261124` before
   26 Nov 2026 08:00 Beijing. The brief also requires uploading the AI
   coding-agent transcripts of the sessions that built the entry with
   each submission. Max 10 submissions/day, 20 total; the last one
   before the deadline counts.

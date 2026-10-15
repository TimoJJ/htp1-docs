# User Manual screenshot status

The approved default-state 1200 px captures have been adopted. They use the unmodified shipped WebUI
(0b726dc, assembled build 3f128c9b) with isolated settings seeded from the firmware's
empty-state initialization. They are not captures of a physically factory-reset unit.
The capture viewport was 1200 × 900 CSS pixels; full-page images can be taller.
No physical-unit configuration was changed. Hardware-default confirmation remains pending.

## Adopted

- [x] `ui-home.jpg`
- [x] `ui-calibration.jpg`
- [x] `ui-calibration-advanced.jpg`
- [x] `ui-balance.jpg`
- [x] `ui-device-settings.jpg`
- [x] `ui-inputs.jpg`
- [x] `ui-inputs-advanced.jpg`
- [x] `ui-macros.jpg`
- [x] `ui-loudness.jpg`
- [x] `ui-upmix.jpg`
- [x] `ui-signal-generator.jpg`
- [x] `ui-volume-setup.jpg`
- [x] `ui-volume-advanced.jpg`
- [x] `ui-speakers.jpg`
- [x] `ui-peq.jpg`
- [x] `ui-seat-shaker.jpg`
- [x] `ui-tone-control.jpg`
- [x] `ui-personalize.jpg`
- [x] `ui-help.jpg`
- [x] `ui-export-preview.jpg` replaces the obsolete embedded configuration pane.
- [x] `ui-addons.jpg` added to the Addons chapter.

- [x] `ui-inputs-cec.jpg`
- [x] `ui-loudness-vintage-custom.jpg`
- [x] `ui-peq-editor.jpg`
- [x] `ui-peq-options-dialog.jpg`
- [x] `ui-speakers-layout-dialog.jpg`
- [x] `ui-sinewave.jpg`
- [x] `ui-import-default-match.jpg`

- [x] `ui-network.jpg` (DHCP overview with illustrative connection data).
- [x] `ui-network-static.jpg` (static fields revealed with default blank addresses and mask).
- [x] `ui-bass-eq-author.jpg` (live catalogue, Author filter).
- [x] `ui-bass-eq-applied-browsed.jpg` (applied entry distinct from browsed entry).

Network addresses and MAC addresses in this batch are illustrative runtime data.
No network configuration was applied. BEQ application was confined to the isolated preview.
The external BEQ artwork failed to load; artwork-complete replacements remain pending.

## Adopted active meter captures

- [x] `ui-peak-monitor.jpg` (Table, 1200 px wide).
- [x] `ui-peak-monitor-bars.jpg` (Bars with Peak hold, 1200 px wide).
- [x] `fp-level-meter.png` (native front-panel capture, 800 × 480).
- [x] `fp-peak-monitor.png` (native Peak Monitor footer, 800 × 480, real signal data).

These captures use real signal data and the physical unit's current speaker configuration,
including Seat Shaker. They are not default-state examples. The user started playback
and opened the Level Meter; no playback or speaker settings were changed by the capture work.

## Adopted Help and Remote captures

- [x] `fp-help.png` (physical front-panel Help/hostname, native 800 × 480).
- [x] `remote.jpg` (Mobile Remote with default controls, 414 × 896 portrait viewport).

Help shows the unit's actual hostname, QR code and Wi-Fi connection; no network settings
were changed. Remote uses production controls and styling with source-initialized defaults
and cleared browser preferences; only its connection transport was redirected to the isolated
preview. The smaller portrait viewport reflects the Remote page's phone-oriented layout.

## Adopted calibrated-state captures

- [x] `ui-dirac-active-calibrated.jpg`: active ART and measured delay/trim table; Stereo and Movie Night slot labels. Replaces the legacy `p55-1.jpg` and `art-p14-1.png` illustrations.
- [x] `ui-calibration-slot-rename.jpg`: Movie Night custom label and original Dirac filter name.

Captured at 1200 px from an isolated copy of the physical unit calibration state.
Only display labels were changed; the physical unit was unchanged.

## Adopted main-panel and PEQ button captures

- [x] `fp-main.png`: native 800 × 480 Default-theme panel, actual playback state; replaces `fp-p01-1.png`.
- [x] `ui-peq-options-button.jpg`: Change PEQ Configuration button detail from a 1200 px default-state preview; replaces `art-p09-1.png`.

Alternative-panel theme, mini-labels and text-color controls remain text-only by request.
No screenshots are required for those features.

## Available detail captures

These approved images are retained for later placement; they do not replace the
pending active-state illustrations.

- `ui-macros-expanded.jpg`
- `ui-context-help.jpg`
- `ui-peak-monitor-off.jpg`

## Pending release captures

These placeholders are tracking assets, not product screenshots. The existing
System Status screenshot remains until a suitable public-release capture is available.

- [ ] System Status: [placeholder](../user-guide/images/pending/ui-system-status-pending.png).
- [ ] Version history: [placeholder](../user-guide/images/pending/ui-version-history-pending.png).

## Remaining screenshot work

- [ ] BEQ: replace the adopted Author and applied-versus-browsed captures when external catalogue artwork is available.
- [ ] Dirac recovery states, only when safely reproducible.
- [ ] Import differences example with a nonmatching configuration file; the matching-file preview already shows the restart explanation.
- [ ] 1.13.3 ART Upgrade Preparation screen, clearly identified as legacy.
- [ ] Current third-party Dirac app workflow images.
- [ ] Signal-flow diagram agreement with Pre/Post PEQ placement.
- [ ] Recheck all remaining hardware/measurement figures during rendered review.
- [ ] Confirm source-seeded defaults against a physical unit.
- [ ] Final rendered-page and image-readability review.

The Home status cards are blank because the isolated default preview has no audio stream.
The default Calibration image has empty slots; it does not demonstrate active filtering.

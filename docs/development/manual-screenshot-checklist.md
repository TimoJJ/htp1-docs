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
- [x] `ui-inputs-advanced-crop.png` — approved PCM Detect Sensitivity detail crop.
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
- [x] `ui-export-preview-crop.png` replaces the obsolete embedded configuration pane.
- [x] `ui-addons.jpg` added to the Addons chapter.

- [x] `ui-inputs-cec-crop.png`
- [x] `ui-loudness-vintage-custom-crop.png`
- [x] `ui-peq-editor-crop.png`
- [x] `ui-peq-options-dialog-crop.png`
- [x] `ui-speakers-layout-dialog-crop.png`
- [x] `ui-sinewave-crop.png`
- [x] `ui-import-default-match-crop.png`

- [x] `ui-network.jpg` (DHCP overview with illustrative connection data).
- [x] `ui-network-static-crop.png` (static fields revealed with default blank addresses and mask).
- [x] `ui-bass-eq-author.jpg` (live catalogue, Author filter).
- [x] `ui-bass-eq-applied-browsed.jpg` (applied entry distinct from browsed entry).

Network addresses and MAC addresses in this batch are illustrative runtime data.
No network configuration was applied. BEQ application was confined to the isolated preview.
The BEQ captures were subsequently replaced with artwork-loaded mobe1969 catalogue entries.
Both replacement captures retain the 1200 px viewport; BEQ application stayed in the isolated preview.

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
- [x] `ui-calibration-slot-rename-crop.png`: Movie Night custom label and original Dirac filter name.

Captured at 1200 px from an isolated copy of the physical unit calibration state.
Only display labels were changed; the physical unit was unchanged.

## Adopted main-panel and PEQ button captures

- [x] `fp-main.png`: native 800 × 480 Default-theme panel, actual playback state; replaces `fp-p01-1.png`.
- [x] `ui-peq-options-button.jpg`: Change PEQ Configuration button detail from a 1200 px default-state preview; replaces `art-p09-1.png`.

Alternative-panel theme, mini-labels and text-color controls remain text-only by request.
No screenshots are required for those features.

## Adopted import differences capture

- [x] `ui-import-differences-detail.png`: relevant Import section cropped from the 1200 px preview, with context above and below. The example changes unit name to Living Room and lip-sync to 20 ms. No import was performed.

## Adopted legacy upgrade capture

- [x] `legacy-1-13-3-art-upgrade-preparation-detail.jpg`: original 1.13.3 preparation page rendered locally at a 1200 px viewport; labelled for the 1.x upgrade procedure. No upgrade action was performed.

## Adopted bass-management and Speaker Map follow-up

- [x] `ui-speakers-21.png`: isolated 1200 px example with Left/Right Small, the source-default 80 Hz crossover, and one subwoofer enabled. LPF for LFE remains 120 Hz and Reinforce Bass remains off. Used in Bass Management; this is an illustrative 2.1 configuration, not the default speaker layout.
- [x] `ui-speaker-map-detail.png`: dedicated crop showing the Speaker Map heading, warning, legend, and complete rear panel for the default 2.0 layout, with Left and Right highlighted green. Replaces the repeated overview image in Speaker Setup.

Both captures use the shipped WebUI in the isolated preview. The preview supplies the
firmware-derived output mapping needed to render the map; no physical-unit settings
were changed. Physical-default confirmation remains pending, as do release captures
and safe recovery captures. Third-party Dirac app replacements remain deferred until
after release.

## Available detail captures

These approved images are retained for later placement; they do not replace the
pending active-state illustrations.

- `ui-macros-expanded.jpg`
- `ui-context-help.jpg`
- `ui-peak-monitor-off.jpg`

## Adopted rc1 release captures

- [x] System Status: `ui-system-status.png`.
- [x] Version history: `ui-version-history.png`.

Approved 1200 px captures use the exact public V2.2.0 Release Candidate 1 WebUI
(9055a744, public release 1cc90056) in an isolated default-setting preview. Release
and hardware metadata were read from the physical unit. The preview represents a
customer unit without a development remote; no physical settings were changed.

## Remaining screenshot work

- [ ] Dirac recovery states, only when safely reproducible.
- [ ] Current third-party Dirac app workflow images — deferred until after release.
- [x] Signal-flow diagrams reviewed for Pre/Post PEQ placement; current figure clarified and historical figure warning strengthened.
- [x] Remaining hardware and measurement figures reviewed; retained without replacement.
- [ ] Confirm source-seeded defaults against a physical unit.
- [x] Rendered-page and image-readability review completed at 1200 px; four approved caption/context corrections applied.

The Home status cards are blank because the isolated default preview has no audio stream.
The default Calibration image has empty slots; it does not demonstrate active filtering.

## Approved detail crops

Ten detail illustrations now use the reviewed crops. Source captures were made at
1200 px viewport width; crops preserve their original pixels without rescaling.
Page overviews and native front-panel captures are unchanged.

- [x] `ui-calibration-slot-rename-crop.png`
- [x] `ui-inputs-cec-crop.png`
- [x] `ui-import-default-match-crop.png`
- [x] `ui-loudness-vintage-custom-crop.png`
- [x] `ui-peq-editor-crop.png`
- [x] `ui-sinewave-crop.png`
- [x] `ui-speakers-layout-dialog-crop.png`
- [x] `ui-peq-options-dialog-crop.png`
- [x] `ui-network-static-crop.png`
- [x] `ui-export-preview-crop.png`

All unfinished screenshot items listed above remain pending.

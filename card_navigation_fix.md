# Card Navigation Fix Report

## Problem

The previous implementation removed the visible "Open" button text but kept the `st.button` widget rendered in the DOM. Since Streamlit always renders a widget row for every `st.button` call regardless of styling, each experiment card had an empty grey button bar underneath it.

## Root Cause

`st.button()` in Streamlit is a **server-side widget** — it always occupies DOM space. Styling it transparent with CSS hides the text but never removes the layout row. There is no way to truly suppress this row while keeping the `st.button` call.

## Solution Implemented

Completely replaced the `st.button` approach with a **pure JavaScript + query-params navigation pattern**:

### How It Works
1. Each experiment card `<div>` has an `onclick` attribute that sets `window.parent.location.href` to the current URL with `?nav=<experiment_key>` appended.
2. At the very top of `app.py`, Streamlit checks for the `nav` query param on every run.
3. If found, it clears the param, updates `session_state.current_page`, and calls `st.rerun()`.
4. Navigation is seamless — no button widgets, no extra DOM rows.

## Changes Made

### `app.py`
| Section | Change |
|---|---|
| Session state init | Added query-param nav handler (`st.query_params`) |
| CSS — overlay button block | **Deleted** entirely. Replaced with `.exp-card` and `.exp-card:hover` rules. |
| Card rendering loop | Removed `st.button`, `st.markdown` overlay wrappers, and all button containers. Added `onclick` directly to the card `<div>`. |

## Hover Effect

The `.exp-card:hover` CSS now provides:
- `cursor: pointer` — entire card shows a hand cursor
- `translateY(-5px) scale(1.015)` — smooth elevation on hover
- Green-tinted drop shadow (`rgba(16, 185, 129, 0.2)`) — accent highlight
- `border-color: #10B981` — green border activates on hover

## Dashboard Layout Result

```
┌────────────────────┐
│ Exp 05             │
│ Line Graph         │
│ Ready              │
│ Hardcoded Demo     │
└────────────────────┘
   ← nothing below →
```

All 11 experiment cards are clickable. No empty rows remain.

# Configuration parameters for the Mandala PDF Generator (config.json)

This document describes all configuration options available in config.json, updated to match the current code and the recent changes discussed in the conversation.

---

## Example structure

```json
{
    "color_hint_mode": "number",
    "color_mode": "advanced",
    "batch_count": 2,
    "mandala_style": "easy_mandala",
    "mandala_max_radius": 1.32
}
```

---

## Parameters

### 1. `color_hint_mode`
- Type: string (`"none"`, `"name"`, `"number"`)
- Description: controls how coloring hints are shown inside mandala areas:
  - `"none"`: no hints.
  - `"name"`: the color name is printed inside each closed area (legacy behavior).
  - `"number"`: a number is printed inside each area; a legend (number ↔ color name) is added to the same page.
- Legend placement and layout (when `"number"` is active):
  - The legend is added to the PDF page at the bottom-left.
  - The table is horizontal in column pairs (No. + Color Name).
  - The table uses a maximum of 5 composed columns per row (to avoid overflowing the right margin).
  - If more entries are needed, the table wraps to additional rows; the layout is calculated to never exceed the A4 page margins.
- Backward compatibility: if an older config still uses `write_color_names`, the script converts it automatically:
  - `write_color_names: true` → `color_hint_mode: "name"`
  - `write_color_names: false` → `color_hint_mode: "none"`

---

### 2. `color_mode`
- Type: string (`"basic"` or `"advanced"`)
- Description: chooses which list of color names is used for hints.
  - `"basic"`: simple palette (Red, Blue, Yellow, ...).
  - `"advanced"`: richer palette (Crimson, Indigo, Turquoise, ...).

---

### 3. `batch_count`
- Type: integer (1, 2, 3, ...)
- Description: how many PDFs to generate in one run.

---

### 4. `mandala_style`
- Type: string (`"random"`, `"geometric"`, `"easy_mandala"`)
- Description: selects the mandala generation style:
  - `"random"`: mandalas made of randomly distributed motifs (flowers, spirals, leaves, etc.).
  - `"geometric"`: symmetric, radial mandalas with classical geometric structures.
  - `"easy_mandala"`: new "book-like" centered radial mandala (implemented as easy_mandala) — features:
    - richer center shapes (regular polygons, composite stars, overlapping triangles, nested polygons, etc.);
    - sector divisions suitable for numbering;
    - rings of petals/ovals and outer small circles (or small polygons) that can be numbered;
    - optimized for "color-by-number" worksheets similar to the photographed book examples.
- Note: "easy_mandala" was added in recent revisions and is available as a valid value.

---

### 5. `mandala_max_radius`
- Type: number (float), e.g. 1.35, 1.42, 1.48
- Description: sets the maximum radius/scale of the mandala for styles that use it (notably `"geometric"` and `"easy_mandala"`). Larger values will occupy more page surface.
- Suggested values:
  - 1.35 (safe default)
  - 1.42 (larger output)
  - up to 1.48 (may reach page margins — test before printing)

---

## File location

Place `config.json` in the same folder as `main.py`.  
If it is missing, the script will prompt for the parameters interactively and create the file.

---

## Options planned / not yet implemented

- `"seed"`: reproducible generation (not yet implemented in the current code; can be added on request).
- `"output_path"`: custom folder for generated PDFs.
- `"image_format"`: export to PNG/SVG in addition to PDF.
- `"center_style"` (for easy_mandala): choose a sub-style for the center (e.g., `"star"`, `"polygon"`, `"triangles"`) — can be exposed in config if you want explicit control.

---

## Technical notes and behaviors

- Legend in `"number"` mode:
  - Built from the color name → number mapping created during drawing and sorted by number for the output table.
  - LaTeX layout produces composed columns (No. + Color Name) with a hard limit of 5 composed columns per row to avoid right-margin overflow; the table wraps to additional rows as needed.
  - The table is anchored bottom-left of the page.
- Backward compatibility:
  - The script automatically converts the old `write_color_names` boolean into the new `color_hint_mode` string if present.

---

If you want, I can:
- add the `"seed"` option and show an example in config.json,
- expose a `center_style` parameter for `easy_mandala`,
- update the repository README with this English markdown file.

Would you like me to add the `"seed"` option and an example config entry?

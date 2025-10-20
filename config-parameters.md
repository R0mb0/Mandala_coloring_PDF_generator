# Configuration Parameters for Mandala PDF Generator (`config.json`)

Below is a full explanation of every configuration option you can use in `config.json`.

---

## Structure Example

```json
{
    "color_hint_mode": "number",
    "color_mode": "advanced",
    "batch_count": 2,
    "mandala_style": "geometric",
    "mandala_max_radius": 1.42
}
```

---

## Parameters

### 1. `color_hint_mode`
- **Type:** string (`"none"`, `"name"`, or `"number"`)
- **Description:**  
  Controls how coloring hints appear inside the mandala areas:
  - `"none"`: no hint
  - `"name"`: a color name is printed inside every closed area (as before)
  - `"number"`: a number is printed in every area, and a legend table (number ↔ color name) is added to the PDF.  
    The legend will be placed at the bottom left of the page, with a horizontal layout (1-2 rows), so it never exceeds the boundaries of the A4 paper.
- **Values:**
  - `"none"`: no color hints
  - `"name"`: show color names in every area
  - `"number"`: show a number in each area, with a horizontal legend table at the bottom left

#### Backward compatibility:
If only `write_color_names` is present, `"name"` mode is used if true, `"none"` if false.

---

### 2. `color_mode`
- **Type:** string (`"basic"` or `"advanced"`)
- **Description:**  
  Controls which list of colors is used for the hints.
- **Values:**
  - `"basic"`: simple colors (`Red`, `Blue`, etc.).
  - `"advanced"`: fancy and varied colors (`Crimson`, `Indigo`, etc.).

---

### 3. `batch_count`
- **Type:** integer (`1`, `2`, `3`, ...)
- **Description:**  
  How many different PDFs to generate per run.
- **Values:**
  - `1`: single PDF
  - Any positive integer

---

### 4. `mandala_style`
- **Type:** string (`"random"` or `"geometric"`)
- **Description:**  
  Selects the mandala style:
  - `"random"`: random distributed motifs (flowers, circles, spirals, etc.).
  - `"geometric"`: classical, symmetric, radial mandalas.

---

### 5. `mandala_max_radius`
- **Type:** decimal (e.g., `1.35`, `1.42`, `1.48`)
- **Description:**  
  Sets the maximum radius for the geometric mandala (only for `"geometric"` style).  
  Higher values use more paper surface.  
  Recommended values: `1.35` (safe), up to `1.48` (test before printing).
- **Values:**
  - `1.35` (safe default)
  - `1.42` (recommended for maximum size)
  - Up to `1.48` (may touch paper edges)

---

## Location

`config.json` must be placed in the same folder as `main.py`.  
If missing, the script will ask you for each parameter and generate the file.

---

## Editing

Open and edit `config.json` with any text editor (Notepad, VSCode, Nano, etc.).  
Run the script again to use new settings.

---

## Future Options (planned, not yet implemented)

- `"output_path"`: custom output folder.
- `"image_format"`: export as PNG/SVG as well as PDF.
- `"min_motifs"` / `"max_motifs"`: control motif count per page.
- `"seed"`: for reproducible random generation.

---

**Need more options? Request a feature!**

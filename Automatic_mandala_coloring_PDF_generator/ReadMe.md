# Configuration Parameters for Mandala PDF Generator (`config.json`)

Below is a full explanation of every configuration option you can use in `config.json`.

---

## Structure Example

```json
{
    "write_color_names": true,
    "color_mode": "advanced",
    "batch_count": 2,
    "mandala_style": "geometric",
    "mandala_max_radius": 1.42
}
```

---

## Parameters

### 1. `write_color_names`
- **Type:** boolean (`true` or `false`)
- **Description:**  
  If `true`, a color name will be printed inside every closed area (petal, polygon, circle).  
  Useful for educational purposes or guided coloring.
- **Values:**
  - `true`: show color names in every area.
  - `false`: do not show color names.

---

### 2. `color_mode`
- **Type:** string (`"basic"` or `"advanced"`)
- **Description:**  
  Controls which list of colors is used for the color names.
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

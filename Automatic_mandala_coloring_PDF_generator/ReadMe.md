# Configuration Parameters for Mandala PDF Generator (`config.json`)

Below is a full explanation of every configuration option you can use in `config.json`.

---

## Structure Example

```json
{
    "color_hint_mode": "number",
    "color_mode": "advanced",
    "batch_count": 2,
    "mandala_style": "easy_mandala",
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
  - `"name"`: a color name is printed inside every closed area
  - `"number"`: a number is printed in every area, and a legend table (number ↔ color name) is added to the PDF.  
    The legend will be placed at the bottom left of the page, with a horizontal layout (max 5 columns per row), wrapping to additional rows as needed.

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
- **Type:** string (`"random"`, `"geometric"` or `"easy_mandala"`)
- **Description:**  
  Selects the mandala style:
  - `"random"`: random distributed motifs (flowers, circles, spirals, etc.).
  - `"geometric"`: classical, symmetric, radial mandalas.
  - `"easy_mandala"`: centered, radial mandala with sectors/petals/stars and rim circles — similar to the photographed book examples, optimized for coloring-by-number.

---

### 5. `mandala_max_radius`
- **Type:** decimal (e.g., `1.35`, `1.42`, `1.48`)
- **Description:**  
  Sets the maximum radius for the geometric or easy mandala.  
  Higher values use more paper surface.  
  Recommended values: `1.35` (safe), up to `1.48` (test before printing).

---

## Location

`config.json` must be placed in the same folder as `main.py`.  
If missing, the script will ask you for each parameter and generate the file.

---

## Editing

Open and edit `config.json` with any text editor (Notepad, VSCode, Nano, etc.).  
Run the script again to use new settings.

---

**Need more options? Request a feature!**
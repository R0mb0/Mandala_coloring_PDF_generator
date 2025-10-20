import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle, Polygon
import matplotlib.patheffects as path_effects

COLOR_NAMES_BASIC = [
    'Red', 'Blue', 'Yellow', 'Green', 'Orange', 'Purple', 'Pink', 'Brown', 'Black', 'White', 'Gray'
]
COLOR_NAMES_ADVANCED = [
    'Crimson', 'Indigo', 'Turquoise', 'Gold', 'Silver', 'Teal', 'Violet', 'Magenta',
    'Lime', 'Coral', 'Azure', 'Tan', 'Olive', 'Lavender', 'Peach', 'Mint', 'Navy',
    'Cyan', 'Beige', 'Chocolate', 'Mustard', 'Amber', 'Emerald', 'Rose', 'Salmon',
    'Ruby', 'Sapphire', 'Ivory', 'Platinum', 'Brass', 'Copper'
]

def centroid(points):
    arr = np.array(points)
    return arr.mean(axis=0)

def point_in_polygon(point, polygon):
    x, y = point
    poly = np.array(polygon)
    n = len(poly)
    inside = False
    px1, py1 = poly[0]
    for i in range(1, n+1):
        px2, py2 = poly[i % n]
        if y > min(py1, py2):
            if y <= max(py1, py2):
                if x <= max(px1, px2):
                    if py1 != py2:
                        xints = (y - py1) * (px2 - px1) / (py2 - py1 + 1e-12) + px1
                    if px1 == px2 or x <= xints:
                        inside = not inside
        px1, py1 = px2, py2
    return inside

def next_number(used):
    # Returns the next unused integer > 0
    n = 1
    while n in used:
        n += 1
    return n

def draw_flower(ax, center, r, lw, color_list=None, color_hint_mode="none", color_map=None):
    circle = Circle(center, r*0.18, edgecolor='black', facecolor='none', lw=lw)
    ax.add_patch(circle)
    for i in np.linspace(0.4, 1.0, 3):
        c_center = center
        c_radius = r*i
        c = Circle(c_center, c_radius, edgecolor='black', facecolor='none', lw=lw)
        ax.add_patch(c)
    num_petals = np.random.choice([10, 12, 14, 16, 18, 20, 24])
    angles = np.linspace(0, 2*np.pi, num_petals, endpoint=False)
    for t in angles:
        dx = np.cos(t)
        dy = np.sin(t)
        petal_center = (center[0] + dx*r*0.6, center[1] + dy*r*0.6)
        petal_width = r * np.random.uniform(0.42, 0.65)
        petal_height = r * np.random.uniform(0.15, 0.22)
        petal = Ellipse(
            petal_center,
            width=petal_width,
            height=petal_height,
            angle=np.degrees(t),
            edgecolor='black',
            facecolor='none',
            lw=lw
        )
        ax.add_patch(petal)
    # Hints (center + petals)
    if color_list and color_hint_mode != "none":
        hint_targets = [center] + [(
            center[0] + np.cos(t)*r*0.6, center[1] + np.sin(t)*r*0.6
        ) for t in angles]
        for idx, pos in enumerate(hint_targets):
            color = np.random.choice(color_list)
            if color_hint_mode == "name":
                txt_hint = color
            elif color_hint_mode == "number":
                if color not in color_map:
                    color_map[color] = next_number(set(color_map.values()))
                txt_hint = str(color_map[color])
            else:
                continue
            txt = ax.text(pos[0], pos[1], txt_hint,
                fontsize=max(r*13 if idx==0 else r*8, 9), color='black',
                ha='center', va='center', weight='bold', zorder=10, clip_on=True)
            txt.set_path_effects([path_effects.Stroke(linewidth=1.5, foreground='white'), path_effects.Normal()])

def draw_spiral(ax, center, r, lw, color_list=None, color_hint_mode="none", color_map=None):
    n_turns = np.random.randint(4, 9)
    theta = np.linspace(0, n_turns * 2 * np.pi, 120)
    a = r*0.18
    b = r*0.13
    x = center[0] + (a + b * theta/(2*np.pi)) * np.cos(theta)
    y = center[1] + (a + b * theta/(2*np.pi)) * np.sin(theta)
    ax.plot(x, y, color='black', lw=lw)
    for i in np.linspace(0.4, 1.0, 3):
        c = Circle(center, r*i, edgecolor='black', facecolor='none', lw=lw)
        ax.add_patch(c)
    if color_list and color_hint_mode != "none":
        n_colors = np.random.randint(1, 4)
        steps = np.linspace(0.15, 0.85, n_colors)
        for s in steps:
            idx_pt = int(s * len(theta))
            color = np.random.choice(color_list)
            if color_hint_mode == "name":
                txt_hint = color
            elif color_hint_mode == "number":
                if color not in color_map:
                    color_map[color] = next_number(set(color_map.values()))
                txt_hint = str(color_map[color])
            else:
                continue
            txt = ax.text(x[idx_pt], y[idx_pt], txt_hint,
                fontsize=max(r*11, 9), color='black',
                ha='center', va='center', weight='bold', zorder=10)
            txt.set_path_effects([path_effects.Stroke(linewidth=1.3, foreground='white'), path_effects.Normal()])

def draw_leaf(ax, center, r, lw, color_list=None, color_hint_mode="none", color_map=None):
    num_leaves = np.random.choice([3, 4, 5])
    angles = np.linspace(0, 2*np.pi, num_leaves, endpoint=False)
    for t in angles:
        dx = np.cos(t)
        dy = np.sin(t)
        leaf_center = (center[0] + dx*r*0.45, center[1] + dy*r*0.45)
        leaf_width = r * np.random.uniform(0.22, 0.32)
        leaf_height = r * np.random.uniform(0.33, 0.48)
        leaf = Ellipse(
            leaf_center,
            width=leaf_width,
            height=leaf_height,
            angle=np.degrees(t)+90,
            edgecolor='black',
            facecolor='none',
            lw=lw
        )
        ax.add_patch(leaf)
        ax.plot([center[0], leaf_center[0]], [center[1], leaf_center[1]], color='black', lw=lw*0.5)
        if color_list and color_hint_mode != "none":
            color = np.random.choice(color_list)
            if color_hint_mode == "name":
                txt_hint = color
            elif color_hint_mode == "number":
                if color not in color_map:
                    color_map[color] = next_number(set(color_map.values()))
                txt_hint = str(color_map[color])
            else:
                continue
            txt = ax.text(leaf_center[0], leaf_center[1], txt_hint,
                fontsize=max(leaf_height*12, 8), color='black',
                ha='center', va='center', weight='bold', zorder=10, rotation=np.degrees(t), clip_on=True)
            txt.set_path_effects([path_effects.Stroke(linewidth=1.0, foreground='white'), path_effects.Normal()])
    circle = Circle(center, r*0.13, edgecolor='black', facecolor='none', lw=lw)
    ax.add_patch(circle)
    if color_list and color_hint_mode != "none":
        color = np.random.choice(color_list)
        if color_hint_mode == "name":
            txt_hint = color
        elif color_hint_mode == "number":
            if color not in color_map:
                color_map[color] = next_number(set(color_map.values()))
            txt_hint = str(color_map[color])
        else:
            return
        txt = ax.text(center[0], center[1], txt_hint,
            fontsize=max(r*9, 7), color='black',
            ha='center', va='center', weight='bold', zorder=10)
        txt.set_path_effects([path_effects.Stroke(linewidth=1.2, foreground='white'), path_effects.Normal()])

def draw_ray_mandala(ax, center, r, lw, color_list=None, color_hint_mode="none", color_map=None):
    num_rays = np.random.choice([20, 24, 28, 32])
    angles = np.linspace(0, 2*np.pi, num_rays, endpoint=False)
    for t in angles:
        dx = np.cos(t)
        dy = np.sin(t)
        x0 = center[0] + dx*r*0.22
        y0 = center[1] + dy*r*0.22
        x1 = center[0] + dx*r*0.95
        y1 = center[1] + dy*r*0.95
        ax.plot([x0, x1], [y0, y1], color='black', lw=lw*0.7)
        a = r*0.08
        b = r*0.05
        theta = np.linspace(0, 2*np.pi, 60)
        xs = x0 + (a + b * theta/(2*np.pi)) * np.cos(theta + t)
        ys = y0 + (a + b * theta/(2*np.pi)) * np.sin(theta + t)
        ax.plot(xs, ys, color='black', lw=lw*0.5)
    for i in np.linspace(0.33, 1.0, 4):
        c = Circle(center, r*i, edgecolor='black', facecolor='none', lw=lw)
        ax.add_patch(c)
    if color_list and color_hint_mode != "none":
        color = np.random.choice(color_list)
        if color_hint_mode == "name":
            txt_hint = color
        elif color_hint_mode == "number":
            if color not in color_map:
                color_map[color] = next_number(set(color_map.values()))
            txt_hint = str(color_map[color])
        else:
            return
        txt = ax.text(center[0], center[1], txt_hint,
            fontsize=max(r*15, 11), color='black',
            ha='center', va='center', weight='bold', zorder=10)
        txt.set_path_effects([path_effects.Stroke(linewidth=1.5, foreground='white'), path_effects.Normal()])
        n_ext_colors = np.random.randint(1, 6)
        ext_angles = np.linspace(0, 2*np.pi, n_ext_colors+1)[:-1] + np.random.uniform(-0.25, 0.25, n_ext_colors)
        for ang in ext_angles:
            dx = np.cos(ang)
            dy = np.sin(ang)
            ext_x = center[0] + dx * r * 0.85
            ext_y = center[1] + dy * r * 1.10
            color = np.random.choice(color_list)
            if color_hint_mode == "name":
                txt_hint = color
            elif color_hint_mode == "number":
                if color not in color_map:
                    color_map[color] = next_number(set(color_map.values()))
                txt_hint = str(color_map[color])
            else:
                continue
            txt = ax.text(ext_x, ext_y, txt_hint,
                fontsize=max(r*10, 8), color='black',
                ha='center', va='center', weight='bold', zorder=10)
            txt.set_path_effects([path_effects.Stroke(linewidth=1.3, foreground='white'), path_effects.Normal()])

def draw_geometric_mandala(ax, center, r_max, lw, color_list=None, color_hint_mode="none", color_map=None):
    levels = np.random.randint(4, 7)
    shapes_drawn = []
    for level in range(1, levels+1):
        radius = r_max * (level/levels)
        shape_type = np.random.choice(['polygon', 'petal', 'triangle'])
        n_shapes = np.random.choice([8, 10, 12, 14, 16, 18, 20])
        angles = np.linspace(0, 2*np.pi, n_shapes, endpoint=False)
        if shape_type == 'polygon':
            for ang in angles:
                points = []
                for k in range(5):
                    th = ang + (2*np.pi*k/n_shapes)
                    points.append([center[0] + np.cos(th)*radius,
                                   center[1] + np.sin(th)*radius])
                poly = Polygon(points, closed=True, edgecolor='black', facecolor='none', lw=lw)
                ax.add_patch(poly)
                shapes_drawn.append(('polygon', points))
        elif shape_type == 'triangle':
            for ang in angles:
                p0 = [center[0] + np.cos(ang)*radius, center[1] + np.sin(ang)*radius]
                p1 = [center[0] + np.cos(ang + np.pi/n_shapes)*radius*0.87,
                      center[1] + np.sin(ang + np.pi/n_shapes)*radius*0.87]
                p2 = [center[0] + np.cos(ang - np.pi/n_shapes)*radius*0.87,
                      center[1] + np.sin(ang - np.pi/n_shapes)*radius*0.87]
                tri = Polygon([p0, p1, p2], closed=True, edgecolor='black', facecolor='none', lw=lw)
                ax.add_patch(tri)
                shapes_drawn.append(('triangle', [p0, p1, p2]))
        elif shape_type == 'petal':
            for ang in angles:
                dx = np.cos(ang)
                dy = np.sin(ang)
                petal_center = (center[0] + dx*radius, center[1] + dy*radius)
                petal_width = radius * 0.38
                petal_height = radius * 0.87
                petal = Ellipse(
                    petal_center,
                    width=petal_width,
                    height=petal_height,
                    angle=np.degrees(ang),
                    edgecolor='black',
                    facecolor='none',
                    lw=lw
                )
                ax.add_patch(petal)
                shapes_drawn.append(('petal', petal_center, petal_width, petal_height, np.degrees(ang)))
        c = Circle(center, radius, edgecolor='black', facecolor='none', lw=lw)
        ax.add_patch(c)
    c = Circle(center, r_max*0.12, edgecolor='black', facecolor='none', lw=lw)
    ax.add_patch(c)

    all_points = []
    for shape in shapes_drawn:
        if shape[0] == 'polygon' or shape[0] == 'triangle':
            all_points.extend(shape[1])
        elif shape[0] == 'petal':
            x, y = shape[1]
            all_points.append([x, y])
    all_points = np.array(all_points)
    x_min, x_max = all_points[:, 0].min(), all_points[:, 0].max()
    y_min, y_max = all_points[:, 1].min(), all_points[:, 1].max()

    margin = 0.04 * r_max
    ax.set_xlim(x_min-margin, x_max+margin)
    ax.set_ylim(y_min-margin, y_max+margin)

    if color_list and color_hint_mode != "none":
        for shape in shapes_drawn:
            if shape[0] == 'polygon' or shape[0] == 'triangle':
                pts = shape[1]
                cx, cy = centroid(pts)
                if point_in_polygon((cx, cy), pts) and \
                   (x_min+margin < cx < x_max-margin) and (y_min+margin < cy < y_max-margin):
                    color = np.random.choice(color_list)
                    if color_hint_mode == "name":
                        txt_hint = color
                    elif color_hint_mode == "number":
                        if color not in color_map:
                            color_map[color] = next_number(set(color_map.values()))
                        txt_hint = str(color_map[color])
                    else:
                        continue
                    txt = ax.text(cx, cy, txt_hint,
                        fontsize=9, color='black',
                        ha='center', va='center', weight='bold', zorder=10, clip_on=True)
                    txt.set_path_effects([path_effects.Stroke(linewidth=1.2, foreground='white'), path_effects.Normal()])
            elif shape[0] == 'petal':
                cx, cy = shape[1]
                angle = shape[4]
                if (x_min+margin < cx < x_max-margin) and (y_min+margin < cy < y_max-margin):
                    color = np.random.choice(color_list)
                    if color_hint_mode == "name":
                        txt_hint = color
                    elif color_hint_mode == "number":
                        if color not in color_map:
                            color_map[color] = next_number(set(color_map.values()))
                        txt_hint = str(color_map[color])
                    else:
                        continue
                    txt = ax.text(cx, cy, txt_hint,
                        fontsize=9, color='black',
                        ha='center', va='center', weight='bold', zorder=10, rotation=angle, clip_on=True)
                    txt.set_path_effects([path_effects.Stroke(linewidth=1.0, foreground='white'), path_effects.Normal()])
        if (x_min+margin < center[0] < x_max-margin) and (y_min+margin < center[1] < y_max-margin):
            color = np.random.choice(color_list)
            if color_hint_mode == "name":
                txt_hint = color
            elif color_hint_mode == "number":
                if color not in color_map:
                    color_map[color] = next_number(set(color_map.values()))
                txt_hint = str(color_map[color])
            else:
                txt_hint = None
            if txt_hint:
                txt = ax.text(center[0], center[1], txt_hint,
                    fontsize=10, color='black',
                    ha='center', va='center', weight='bold', zorder=10)
                txt.set_path_effects([path_effects.Stroke(linewidth=1.8, foreground='white'), path_effects.Normal()])

def flower_can_fit(new_center, new_r, centers, radii, min_overlap=0.32):
    for (c, r) in zip(centers, radii):
        dist = np.hypot(c[0]-new_center[0], c[1]-new_center[1])
        allowed = (new_r + r) * min_overlap
        if dist < (new_r + r - allowed):
            return False
    return True

def generate_mandala_image(output_path, color_hint_mode="none", color_mode="advanced", mandala_style="random", mandala_max_radius=1.35):
    if color_mode == "basic":
        color_list = COLOR_NAMES_BASIC
    else:
        color_list = COLOR_NAMES_ADVANCED

    fig, ax = plt.subplots(figsize=(7.7, 10.2), dpi=150)
    ax.set_aspect('equal')
    ax.axis('off')
    color_map = {}  # color name -> number

    if mandala_style == "geometric":
        center = (0, 0)
        r_max = mandala_max_radius
        lw = np.random.uniform(1.7, 2.2)
        draw_geometric_mandala(
            ax, center, r_max, lw,
            color_list=color_list if color_hint_mode != "none" else None,
            color_hint_mode=color_hint_mode, color_map=color_map
        )
    else:
        min_elements = 14
        max_elements = 22
        n_elements = np.random.randint(min_elements, max_elements)
        centers = []
        radii = []

        tries = 0
        max_tries = 4000
        min_overlap = 0.33
        r_min = 0.34
        r_max = 0.68

        def random_center(r):
            x = np.random.uniform(-0.97 + r, 0.97 - r)
            y = np.random.uniform(-1.35 + r, 1.35 - r)
            return (x, y)

        while len(centers) < n_elements and tries < max_tries:
            if tries > max_tries // 2 and min_overlap < 0.48:
                min_overlap += 0.01
                r_max -= 0.01
            tries += 1
            r = np.random.uniform(r_min, r_max)
            new_center = random_center(r)
            if flower_can_fit(new_center, r, centers, radii, min_overlap=min_overlap):
                centers.append(new_center)
                radii.append(r)

        while len(centers) < min_elements and tries < max_tries*2:
            tries += 1
            r = np.random.uniform(0.28, 0.38)
            new_center = random_center(r)
            if flower_can_fit(new_center, r, centers, radii, min_overlap=min_overlap*0.8):
                centers.append(new_center)
                radii.append(r)

        shape_functions = [draw_flower, draw_spiral, draw_leaf, draw_ray_mandala]
        for i, center in enumerate(centers):
            r = radii[i]
            lw = np.random.uniform(1.4, 2.1)
            shape_fn = np.random.choice(shape_functions)
            shape_fn(
                ax, center, r, lw,
                color_list=color_list if color_hint_mode != "none" else None,
                color_hint_mode=color_hint_mode, color_map=color_map
            )

    plt.tight_layout(pad=0)
    fig.savefig(output_path, transparent=True, bbox_inches='tight', pad_inches=0)
    plt.close(fig)

    # If number mode, return the legend mapping (sorted by number)
    if color_hint_mode == "number" and len(color_map) > 0:
        legend = sorted([(num, color) for color, num in color_map.items()], key=lambda x: x[0])
        return legend
    else:
        return None
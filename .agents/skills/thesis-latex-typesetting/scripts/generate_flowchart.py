import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path

def create_flowchart(output_path):
    plt.rcParams['mathtext.fontset'] = 'cm'
    plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']

    fig, ax = plt.subplots(figsize=(14.8, 3.8), dpi=300)
    ax.set_xlim(0, 20.8)
    ax.set_ylim(0, 5.0)
    ax.axis('off')

    # Color palette - Refined Academic Style (IEEE / ACM / NeurIPS)
    c_slate_dark = '#0F172A'    # Primary dark text
    c_slate_mid = '#334155'     # Borders & arrows
    c_slate_muted = '#475569'   # Subtitles
    c_slate_light = '#F8FAFC'   # Light neutral fill

    c_amber_border = '#D97706'  # Amber-600
    c_amber_fill = '#FEF3C7'    # Amber-100
    c_amber_text = '#78350F'    # Amber-900

    c_green_border = '#059669'  # Emerald-600
    c_green_fill = '#ECFDF5'    # Emerald-50
    c_green_text = '#065F46'    # Emerald-800

    c_red_border = '#DC2626'    # Red-600
    c_red_fill = '#FEF2F2'      # Red-50
    c_red_text = '#991B1B'      # Red-800

    c_blue_border = '#2563EB'   # Blue-600
    c_blue_fill = '#EFF6FF'     # Blue-50
    c_blue_title = '#1E3A8A'    # Blue-900

    def draw_card(x, y, w, h, fill, border, r=0.14, lw=1.4):
        box = patches.FancyBboxPatch(
            (x - w/2, y - h/2), w, h,
            boxstyle=f"round,pad=0,rounding_size={r}",
            facecolor=fill, edgecolor=border, linewidth=lw
        )
        ax.add_patch(box)

    # -------------------------------------------------------------
    # 1. Start Node: Sample Transition
    # -------------------------------------------------------------
    draw_card(1.85, 2.5, 3.1, 1.4, c_slate_light, c_slate_mid)
    ax.text(1.85, 2.82, "Sample Transition", ha='center', va='center', fontsize=9.2, fontweight='bold', color=c_slate_dark)
    ax.text(1.85, 2.22, r"from $\mathcal{D}$: $(s, a, r, s^\prime)$", ha='center', va='center', fontsize=9.0, color=c_slate_muted)

    # Arrow 1 -> Diamond
    ax.annotate('', xy=(4.40, 2.5), xytext=(3.40, 2.5),
                arrowprops=dict(facecolor=c_slate_mid, edgecolor=c_slate_mid, width=1.3, headwidth=5.5, headlength=6))

    # -------------------------------------------------------------
    # 2. Decision Diamond: Center (5.9, 2.5), dx=1.5, dy=1.3
    # -------------------------------------------------------------
    diamond = patches.Polygon([[5.9, 3.8], [7.4, 2.5], [5.9, 1.2], [4.4, 2.5]], closed=True,
                              facecolor=c_amber_fill, edgecolor=c_amber_border, linewidth=1.4)
    ax.add_patch(diamond)
    ax.text(5.9, 2.84, r"Is $r = 0$", ha='center', va='center', fontsize=9.2, fontweight='bold', color=c_amber_text)
    ax.text(5.9, 2.50, "and", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#92400E')
    ax.text(5.9, 2.16, r"$\mathrm{rand}(0, 1) < \rho$ ?", ha='center', va='center', fontsize=9.0, fontweight='bold', color=c_amber_text)

    # -------------------------------------------------------------
    # Branches from Diamond
    # -------------------------------------------------------------
    # Top Branch: YES
    ax.text(6.35, 4.15, 'YES', ha='center', va='center', fontsize=9.2, fontweight='bold', color=c_green_border)
    ax.annotate('', xy=(7.90, 3.85), xytext=(5.9, 3.8),
                arrowprops=dict(arrowstyle='->', lw=1.3, color=c_green_border, connectionstyle='arc3,rad=-0.18'))

    # Top Action: Set Optimistic Reward
    draw_card(9.55, 3.85, 3.3, 1.3, c_green_fill, c_green_border)
    ax.text(9.55, 4.15, "Set Optimistic Reward", ha='center', va='center', fontsize=9.0, fontweight='bold', color=c_green_text)
    ax.text(9.55, 3.60, r"$\tilde{r} = 1$", ha='center', va='center', fontsize=10.2, fontweight='bold', color=c_green_border)

    # Bottom Branch: NO
    ax.text(6.35, 0.85, 'NO', ha='center', va='center', fontsize=9.2, fontweight='bold', color=c_red_border)
    ax.annotate('', xy=(7.90, 1.15), xytext=(5.9, 1.2),
                arrowprops=dict(arrowstyle='->', lw=1.3, color=c_red_border, connectionstyle='arc3,rad=0.18'))

    # Bottom Action: Preserve Base Reward
    draw_card(9.55, 1.15, 3.3, 1.3, c_red_fill, c_red_border)
    ax.text(9.55, 1.45, "Preserve Base Reward", ha='center', va='center', fontsize=9.0, fontweight='bold', color=c_red_text)
    ax.text(9.55, 0.90, r"$\tilde{r} = r$", ha='center', va='center', fontsize=10.2, fontweight='bold', color=c_red_border)

    # -------------------------------------------------------------
    # Junction / Convergence of Branches into Bellman Target
    # -------------------------------------------------------------
    # Right edge of action boxes is at x = 11.20
    # Paths curve into a clean junction line at x = 11.90
    verts_top = [(11.20, 3.85), (11.90, 3.85), (11.90, 2.5)]
    codes_top = [Path.MOVETO, Path.CURVE3, Path.CURVE3]
    path_top = patches.PathPatch(Path(verts_top, codes_top), facecolor='none', edgecolor=c_slate_mid, lw=1.3)
    ax.add_patch(path_top)

    verts_bot = [(11.20, 1.15), (11.90, 1.15), (11.90, 2.5)]
    codes_bot = [Path.MOVETO, Path.CURVE3, Path.CURVE3]
    path_bot = patches.PathPatch(Path(verts_bot, codes_bot), facecolor='none', edgecolor=c_slate_mid, lw=1.3)
    ax.add_patch(path_bot)

    # Small junction dot at (11.90, 2.5)
    dot = patches.Circle((11.90, 2.5), 0.05, facecolor=c_slate_mid, edgecolor=c_slate_mid)
    ax.add_patch(dot)

    # Single horizontal entry arrow from junction (11.90, 2.5) to Bellman box (12.50, 2.5)
    ax.annotate('', xy=(12.50, 2.5), xytext=(11.90, 2.5),
                arrowprops=dict(facecolor=c_slate_mid, edgecolor=c_slate_mid, width=1.3, headwidth=5.5, headlength=6))
    # Small label for the effective reward signal
    ax.text(12.20, 2.80, r"$\tilde{r}$", ha='center', va='center', fontsize=9.5, fontweight='bold', color=c_slate_dark)

    # -------------------------------------------------------------
    # 3. Node: Compute Bellman TD Target
    # -------------------------------------------------------------
    # Center: (14.85, 2.5), W: 4.7, H: 1.65
    draw_card(14.85, 2.5, 4.7, 1.65, c_blue_fill, c_blue_border, lw=1.4)
    ax.text(14.85, 2.95, "Compute Bellman TD Target", ha='center', va='center', fontsize=9.2, fontweight='bold', color=c_blue_title)
    ax.text(14.85, 2.22, r"$y = \tilde{r} + \gamma \, \mathrm{max}_{a^\prime} Q(s^\prime, a^\prime; \theta^\prime)$",
            ha='center', va='center', fontsize=9.8, color=c_slate_dark)

    # Arrow Bellman -> Policy Update
    ax.annotate('', xy=(17.80, 2.5), xytext=(17.20, 2.5),
                arrowprops=dict(facecolor=c_slate_mid, edgecolor=c_slate_mid, width=1.3, headwidth=5.5, headlength=6))

    # -------------------------------------------------------------
    # 4. Node: Update Policy
    # -------------------------------------------------------------
    # Center: (19.15, 2.5), W: 2.7, H: 1.4
    draw_card(19.15, 2.5, 2.7, 1.4, c_slate_light, c_slate_mid)
    ax.text(19.15, 2.82, "Update Policy", ha='center', va='center', fontsize=9.2, fontweight='bold', color=c_slate_dark)
    ax.text(19.15, 2.22, r"$\theta \leftarrow \theta - \alpha \nabla_\theta \mathcal{L}(\theta)$",
            ha='center', va='center', fontsize=9.0, color=c_slate_dark)

    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Publication-grade flowchart saved to {output_path}")

if __name__ == '__main__':
    create_flowchart('figures/reward-shaping.png')

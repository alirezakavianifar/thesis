import matplotlib.pyplot as plt
import numpy as np

def create_proposition1_bound_figure(output_path):
    plt.rcParams['mathtext.fontset'] = 'cm'
    plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']

    fig = plt.figure(figsize=(15.2, 6.2), dpi=300)
    
    # -------------------------------------------------------------
    # Subplot 1: Geometric Cross-Polytope Lattice (3D-like projection)
    # -------------------------------------------------------------
    ax1 = fig.add_subplot(1, 2, 1)
    
    # Color palette
    c_slate_dark = '#0F172A'
    c_slate_muted = '#64748B'
    c_grid = '#F1F5F9'
    c_blue = '#2563EB'
    c_blue_fill = '#DBEAFE'
    c_emerald = '#059669'
    c_emerald_fill = '#D1FAE5'
    c_purple = '#7C3AED'
    c_rose = '#E11D48'
    c_rose_fill = '#FFE4E6'

    ax1.set_xlim(-2.4, 2.4)
    ax1.set_ylim(-2.4, 2.4)
    ax1.set_aspect('equal')
    ax1.grid(True, linestyle='--', color=c_grid, alpha=0.8, zorder=0)

    # 1. Full L_inf 1-step search cube (in 2D projection)
    rect = plt.Rectangle((-1.0, -1.0), 2.0, 2.0, facecolor=c_rose_fill, edgecolor=c_rose,
                         linestyle=':', linewidth=1.5, alpha=0.35, zorder=1,
                         label=r'Unconstrained $L_\infty$ 1-Step: $3^m = 27$ candidates')
    ax1.add_patch(rect)

    # Diagonal pruned points in L_inf where sum|delta| > 1
    diag_pts = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for px, py in diag_pts:
        ax1.scatter(px, py, color=c_rose, s=55, marker='x', linewidth=2.0, zorder=3)
    ax1.text(1.05, 1.05, r'Pruned by $L_1$: $\sum |[a]_j - [a_0]_j| > 1$', color=c_rose, fontsize=8.5,
             fontweight='bold', zorder=4)

    # 2. L1 Cross-Polytope (Diamond in 2D projection for top-2 of top-m)
    diamond = plt.Polygon([(0, 1), (1, 0), (0, -1), (-1, 0)],
                          facecolor=c_blue_fill, edgecolor=c_blue,
                          linestyle='-', linewidth=2.2, alpha=0.45, zorder=2,
                          label=r'Top-$m$ $L_1$ Neighborhood: $|\mathcal{N}(a_0)| \leq 2m + 1$')
    ax1.add_patch(diamond)

    # Shaded Infeasible Parameter Region below physical boundary
    ax1.axhspan(-2.4, -0.65, color='#FEE2E2', alpha=0.55, zorder=1)
    ax1.axhline(-0.65, color='#DC2626', linestyle='-.', linewidth=1.8, zorder=3)
    ax1.text(-2.3, -0.95, r'$\mathbf{Physically\ Infeasible\ Region:}$' + '\n' + r'$[a_0]_2 - 1 < a_{\min}$ (Parameter Bound Collision)',
             color='#991B1B', fontsize=8.2, fontweight='bold', zorder=6)

    # Coordinate axes
    ax1.axhline(0, color=c_slate_dark, linewidth=1.2, linestyle='-', zorder=2)
    ax1.axvline(0, color=c_slate_dark, linewidth=1.2, linestyle='-', zorder=2)

    # 3D projection axis (third axis e_3 tilted at 45 degrees)
    diag_len = 0.707
    ax1.plot([-diag_len, diag_len], [-diag_len, diag_len], color=c_purple, linewidth=1.5,
             linestyle='--', zorder=2)

    # Candidate points on the 1-hop cross-polytope
    candidates = [
        (0, 0, r'$a_0$ (Nominal Proposal)', c_emerald, 140, 'center', 'bottom', (0, 0.12)),
        (1, 0, r'$a_0 + e_1$', c_blue, 90, 'left', 'center', (0.1, 0)),
        (-1, 0, r'$a_0 - e_1$', c_blue, 90, 'right', 'center', (-0.1, 0)),
        (0, 1, r'$a_0 + e_2$', c_blue, 90, 'center', 'bottom', (0, 0.1)),
        (0, -1, r'$a_0 - e_2$ (Truncated)', '#DC2626', 100, 'center', 'top', (0, -0.12)),
        (diag_len, diag_len, r'$a_0 + e_3$', c_purple, 90, 'left', 'bottom', (0.08, 0.08)),
        (-diag_len, -diag_len, r'$a_0 - e_3$', c_purple, 90, 'right', 'top', (-0.08, -0.08)),
    ]

    for cx, cy, lbl, col, sz, ha, va, (ox, oy) in candidates:
        if 'Truncated' in lbl:
            ax1.scatter(cx, cy, color='#FEE2E2', s=sz, marker='o', edgecolors='#DC2626',
                        linewidth=2.2, linestyle='--', zorder=5)
            ax1.scatter(cx, cy, color='#DC2626', s=45, marker='x', linewidth=2.0, zorder=6)
            ax1.text(cx + ox, cy + oy, lbl, color='#991B1B', fontsize=8.2, fontweight='bold',
                     ha=ha, va=va, zorder=6)
        elif cx == 0 and cy == 0:
            ax1.scatter(cx, cy, color=col, s=sz, marker='*', edgecolors=c_slate_dark,
                        linewidth=1.2, zorder=6)
            ax1.text(cx + ox, cy + oy, lbl, color=col, fontsize=9.2, fontweight='bold',
                     ha=ha, va=va, zorder=6)
        else:
            ax1.scatter(cx, cy, color=col, s=sz, marker='o', edgecolors=c_slate_dark,
                        linewidth=1.0, zorder=5)
            ax1.text(cx + ox, cy + oy, lbl, color=c_slate_dark, fontsize=8.5,
                     ha=ha, va=va, zorder=6)

    ax1.set_title(r'(a) Geometric $L_1$ Neighborhood Topology ($\mathcal{N}(a_0)$)',
                  fontsize=11.5, color=c_slate_dark, fontweight='bold', pad=12)
    ax1.set_xlabel(r'Sensitive Coordinate Dimension $j_1 \in \mathrm{Top-}m$', fontsize=9.5, color=c_slate_dark)
    ax1.set_ylabel(r'Sensitive Coordinate Dimension $j_2 \in \mathrm{Top-}m$', fontsize=9.5, color=c_slate_dark)
    ax1.legend(loc='upper left', fontsize=8.2, framealpha=0.95, edgecolor=c_slate_muted)

    # -------------------------------------------------------------
    # Subplot 2: Scalability and Complexity Growth (Log Scale)
    # -------------------------------------------------------------
    ax2 = fig.add_subplot(1, 2, 2)
    
    dims = np.array([1, 2, 3, 5, 10, 20, 37])
    
    full_linf = 3.0 ** dims
    full_l1 = 2.0 * dims + 1.0
    m_fixed = 3
    proposed_bound = np.full_like(dims, 2 * m_fixed + 1)
    
    ax2.plot(dims, full_linf, 's--', color=c_rose, linewidth=2.2, markersize=6,
             label=r'Full $L_\infty$ Grid: $3^{d_A}$ (Combinatorial Explosion)')
    ax2.plot(dims, full_l1, 'o-', color='#D97706', linewidth=2.0, markersize=6,
             label=r'Full $L_1$ Search: $2d_A + 1$ (Unconstrained)')
    ax2.plot(dims, proposed_bound, 'D-', color=c_emerald, linewidth=2.6, markersize=7,
             label=r'Proposition 1 Bound: $|\mathcal{N}(a_0)| \leq 2m + 1$ ($m=3$)')

    # Hard Real-Time Budget Line
    ax2.axhline(15, color='#2563EB', linestyle=':', linewidth=2.0,
                label=r'Real-Time Feasibility Limit ($\leq 15$ Candidates for $t \leq 3.5\,\mathrm{ms}$)')
    ax2.axhspan(1, 15, color='#DBEAFE', alpha=0.35)

    ax2.set_yscale('log')
    ax2.set_xlim(0, 40)
    ax2.set_ylim(1, 1e18)
    ax2.grid(True, linestyle='--', color='#E2E8F0', alpha=0.8)

    # Annotation for DeltaIoT (d_A = 37)
    ax2.scatter(37, 3**37, color=c_rose, s=80, zorder=6)
    ax2.annotate(r'DeltaIoT ($d_A=37$):' + '\n' + r'$4.5 \times 10^{17}$ Candidates',
                 xy=(37, 3**37), xytext=(22, 1e13),
                 arrowprops=dict(facecolor=c_rose, shrink=0.08, width=1.5, headwidth=6),
                 fontsize=8.5, fontweight='bold', color=c_rose,
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF1F2', edgecolor=c_rose, alpha=0.9))

    # Annotation for Proposed Bound at d_A = 37
    ax2.scatter(37, 7, color=c_emerald, s=90, zorder=6)
    ax2.annotate(r'Proposed Bound ($m=3$):' + '\n' + r'Strictly $\leq 7$ Candidates',
                 xy=(37, 7), xytext=(20, 25),
                 arrowprops=dict(facecolor=c_emerald, shrink=0.08, width=1.5, headwidth=6),
                 fontsize=8.5, fontweight='bold', color=c_emerald,
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='#ECFDF5', edgecolor=c_emerald, alpha=0.9))

    ax2.set_title(r'(b) Candidate Space Growth vs. Action Dimensions ($d_A$)',
                  fontsize=11.5, color=c_slate_dark, fontweight='bold', pad=12)
    ax2.set_xlabel(r'Total Control Action Dimensions ($d_A$)', fontsize=9.5, color=c_slate_dark)
    ax2.set_ylabel(r'Number of Evaluated Candidates $|\mathcal{N}|$ (Log Scale)', fontsize=9.5, color=c_slate_dark)
    ax2.legend(loc='center left', fontsize=8.2, framealpha=0.95, edgecolor=c_slate_muted)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Proposition 1 figure successfully saved to: {output_path}")

if __name__ == '__main__':
    create_proposition1_bound_figure("e:/projects/thesis/figures/fig_proposition1_bound.png")

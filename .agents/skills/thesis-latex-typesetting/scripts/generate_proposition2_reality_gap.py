import matplotlib.pyplot as plt
import numpy as np

def create_proposition2_reality_gap_figure(output_path):
    plt.rcParams['mathtext.fontset'] = 'cm'
    plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15.4, 6.2), dpi=300)

    # Color palette
    c_slate_dark = '#0F172A'
    c_slate_muted = '#64748B'
    c_grid = '#F1F5F9'
    c_blue = '#2563EB'
    c_emerald = '#059669'
    c_emerald_fill = '#D1FAE5'
    c_amber = '#D97706'
    c_amber_fill = '#FEF3C7'
    c_rose = '#E11D48'
    c_rose_fill = '#FFE4E6'

    # -------------------------------------------------------------
    # Subplot 1: Surrogate Margin vs True Physical Margin Phase-Space
    # -------------------------------------------------------------
    eps_max = 0.15  # Uniform calibration error bound sup|M_k - M_k*| <= eps_max
    x_vals = np.linspace(-0.6, 0.6, 300)

    # Reality Gap Tube around y = x: y in [x - eps_max, x + eps_max]
    y_center = x_vals
    y_upper = x_vals + eps_max
    y_lower = x_vals - eps_max

    ax1.set_xlim(-0.55, 0.55)
    ax1.set_ylim(-0.55, 0.55)
    ax1.grid(True, linestyle='--', color=c_grid, alpha=0.8, zorder=0)

    # Shade Reality Gap Uncertainty Tube
    ax1.fill_between(x_vals, y_lower, y_upper, color='#E2E8F0', alpha=0.6, zorder=1,
                     label=r'Reality Gap Tube: $|M_k(s, a) - M_k^*(s, a)| \leq \epsilon_{\max}$')

    # Ideal Zero Reality Gap Line (y = x)
    ax1.plot(x_vals, y_center, color=c_slate_muted, linestyle='--', linewidth=1.5, zorder=2,
             label=r'Ideal Zero Gap ($M_k \equiv M_k^*$)')

    # Bounding curves of the tube
    ax1.plot(x_vals, y_upper, color='#94A3B8', linestyle=':', linewidth=1.2, zorder=2)
    ax1.plot(x_vals, y_lower, color='#94A3B8', linestyle=':', linewidth=1.2, zorder=2)

    # Safety Threshold Boundaries (x=0 and y=0)
    ax1.axvline(0, color=c_slate_dark, linewidth=1.4, linestyle='-', zorder=3)
    ax1.axhline(0, color=c_slate_dark, linewidth=1.4, linestyle='-', zorder=3)

    # Bounded Physical Error Line: Delta^* = -epsilon_max
    ax1.axhline(-eps_max, color=c_rose, linewidth=1.8, linestyle='-.', zorder=3,
                label=r'Clause 1 & 2 Lower Bound: $\Delta^*_{\min} \geq -\epsilon_{\max}$')

    # Severe Violation Threshold: Delta_surr = -2*epsilon_max
    ax1.axvline(-2 * eps_max, color=c_amber, linewidth=1.6, linestyle=':', zorder=3,
                label=r'Clause 2 Severe Violation: $\Delta_{\min}(a_0) < -2\epsilon_{\max}$')

    # Shading Critical Physical Zones
    ax1.axhspan(0, 0.55, color=c_emerald_fill, alpha=0.25, zorder=0)
    ax1.axhspan(-eps_max, 0, color=c_amber_fill, alpha=0.25, zorder=0)
    ax1.axhspan(-0.55, -eps_max, color=c_rose_fill, alpha=0.2, zorder=0)

    # Annotate Zones cleanly along right margin
    ax1.text(0.535, 0.45, 'Physical Safe Zone\n' + r'($\Delta^*_{\min} \geq 0$)', ha='right', color='#065F46', fontsize=7.8, fontweight='bold')
    ax1.text(0.535, -0.075, 'Bounded Error Zone\n' + r'($-\epsilon_{\max} \leq \Delta^* < 0$)', ha='right', va='center', color='#92400E', fontsize=7.4, fontweight='bold')
    ax1.text(0.535, -0.45, 'Catastrophic Zone\n' + r'($\Delta^* < -\epsilon_{\max}$)', ha='right', color='#991B1B', fontsize=7.5, fontweight='bold')

    # Case 1: Compliant Nominal Proposal a0 in N_sat (Clause 1)
    a0_surr = 0.08
    a0_phys = a0_surr - 0.12  # dips into bounded error zone (-0.04 >= -0.15)
    ax1.scatter(a0_surr, a0_phys, color=c_blue, s=90, marker='o', edgecolors=c_slate_dark, linewidth=1.2, zorder=6)
    ax1.text(a0_surr + 0.02, a0_phys - 0.06, r'Clause 1: Nominal $a_0 \in \mathcal{N}_{\mathrm{sat}}$' + '\n' + r'($\Delta_{\min} \geq 0 \rightarrow \Delta^* \geq -\epsilon_{\max}$)',
             color=c_blue, fontsize=7.8, fontweight='bold', zorder=7)

    # Refined Candidate a* with deeper safety margin
    astar_surr = 0.28
    astar_phys = astar_surr - 0.06
    ax1.scatter(astar_surr, astar_phys, color=c_emerald, s=120, marker='*', edgecolors=c_slate_dark, linewidth=1.2, zorder=6)
    ax1.text(astar_surr - 0.03, astar_phys + 0.05, r'Refined $a^* = \arg\max \mathcal{J}$' + '\n' + r'($\Delta^* \geq 0$ since $\Delta_{\min} \geq \epsilon_{\max}$)',
             ha='center', color=c_emerald, fontsize=8.0, fontweight='bold', zorder=7)

    ax1.annotate('', xy=(astar_surr, astar_phys), xytext=(a0_surr, a0_phys),
                 arrowprops=dict(arrowstyle="->", color=c_emerald, lw=2.0, shrinkA=5, shrinkB=5))

    # Case 2: Severe Violation Case a0 with Delta_surr < -2*eps_max (Clause 2)
    b0_surr = -0.42
    b0_phys = b0_surr + 0.06  # = -0.36 < -eps_max (-0.15)
    ax1.scatter(b0_surr, b0_phys, color=c_rose, s=80, marker='s', edgecolors=c_slate_dark, linewidth=1.2, zorder=6)
    ax1.text(b0_surr + 0.03, b0_phys - 0.05, r'Clause 2: Severe $a_0$' + '\n' + r'($\Delta_{\min}(a_0) < -2\epsilon_{\max}$)',
             ha='left', va='top', color=c_rose, fontsize=7.8, fontweight='bold', zorder=7,
             bbox=dict(boxstyle='round,pad=0.18', facecolor='#FFF1F2', edgecolor='none', alpha=0.85))

    # Recovered Candidate b* in N_sat (Clause 2: Delta_surr >= 0)
    bstar_surr = 0.12
    bstar_phys = bstar_surr - 0.08  # = +0.04 >= -eps_max
    ax1.scatter(bstar_surr, bstar_phys, color='#D97706', s=95, marker='^', edgecolors=c_slate_dark, linewidth=1.2, zorder=6)
    ax1.annotate(r'Clause 2: $a^* \in \mathcal{N}_{\mathrm{sat}}$' + '\n' + r'($\Delta^*_{\min}(a^*) > \Delta^*_{\min}(a_0)$)',
                 xy=(bstar_surr, bstar_phys), xytext=(-0.03, 0.13),
                 ha='right', va='bottom',
                 arrowprops=dict(arrowstyle='->', color='#D97706', lw=1.2, shrinkA=2, shrinkB=5),
                 color='#B45309', fontsize=7.8, fontweight='bold', zorder=7,
                 bbox=dict(boxstyle='round,pad=0.18', facecolor='#FFFBEB', edgecolor='#D97706', lw=0.7, alpha=0.92))

    ax1.annotate('', xy=(bstar_surr, bstar_phys), xytext=(b0_surr, b0_phys),
                 arrowprops=dict(arrowstyle="->", color=c_amber, lw=2.0, linestyle='--', shrinkA=5, shrinkB=5))

    ax1.set_title(r'(a) Safety Margin Phase-Space Under Reality Gap ($\epsilon_{\max}$)',
                  fontsize=11.2, color=c_slate_dark, fontweight='bold', pad=12)
    ax1.set_xlabel(r'Surrogate Estimated Margin $\Delta_{\min}(s, a) = \min_k (M_k - \tau_k)$',
                   fontsize=9.5, color=c_slate_dark)
    ax1.set_ylabel(r'True Physical Margin $\Delta^*_{\min}(s, a) = \min_k (M^*_k - \tau_k)$',
                   fontsize=9.5, color=c_slate_dark)
    ax1.legend(loc='upper left', fontsize=7.6, framealpha=0.95, edgecolor=c_slate_muted)

    # -------------------------------------------------------------
    # Subplot 2: Utility Loss Bound under Reality Gap (Proposition 2)
    # -------------------------------------------------------------
    lambda_tie = 0.05
    loss_bound = 2 * lambda_tie * eps_max  # 2 * 0.05 * 0.15 = 0.015

    u_labels = [r'$a_1$', r'$a_2$', r'$a_0$ (Nominal)', r'$a_4$', r'$a^*$ (Selected)']
    j_surr = np.array([0.72, 0.79, 0.85, 0.83, 0.88])
    j_phys = np.array([0.71, 0.80, 0.84, 0.82, 0.875])

    x_pos = np.arange(len(u_labels))
    width = 0.35

    ax2.bar(x_pos - width/2, j_surr, width, label=r'Surrogate Objective $\mathcal{J}(s, a) = u(a) + \lambda_{\mathrm{tie}}\,\bar{\Delta}(s, a)$',
            color=c_blue, alpha=0.85, edgecolor=c_slate_dark)
    ax2.bar(x_pos + width/2, j_phys, width, label=r'True Physical Objective $\mathcal{J}^*(s, a) = u(a) + \lambda_{\mathrm{tie}}\,\bar{\Delta}^{\!*}(s, a)$',
            color=c_emerald, alpha=0.85, edgecolor=c_slate_dark)

    j_star_a0 = j_phys[2]
    j_star_bound = j_star_a0 - loss_bound

    ax2.axhline(j_star_a0, color=c_slate_dark, linestyle=':', linewidth=1.2,
                label=r'Nominal Physical Objective $\mathcal{J}^*(a_0) = 0.84$')
    ax2.axhline(j_star_bound, color=c_rose, linestyle='-.', linewidth=1.8,
                label=r'Clause 1 Lower Bound: $\mathcal{J}^*(a^*) \geq \mathcal{J}^*(a_0) - 2\lambda_{\mathrm{tie}}\epsilon_{\max}$')
    ax2.axhspan(j_star_bound, j_star_a0, color=c_rose_fill, alpha=0.35)

    # Explicit visual bracket for the bound loss
    ax2.annotate('', xy=(1.5, j_star_bound), xytext=(1.5, j_star_a0),
                 arrowprops=dict(arrowstyle='<->', color='#B91C1C', lw=1.5))
    ax2.text(1.58, (j_star_bound + j_star_a0)/2, r'Max Loss: $2\lambda_{\mathrm{tie}}\epsilon_{\max} = 0.015$',
             color='#B91C1C', fontsize=8.0, fontweight='bold', va='center')

    ax2.set_xticks(x_pos)
    ax2.set_xticklabels(u_labels, fontsize=8.8)
    ax2.set_ylim(0.65, 0.95)
    ax2.grid(True, linestyle='--', color='#E2E8F0', alpha=0.8)

    ax2.annotate(r'Refined Selection:' + '\n' + r'$\mathcal{J}^*(a^*) = 0.875 \geq \mathcal{J}^*(a_0)$' + '\n' + r'(Strict Physical Improvement)',
                 xy=(4 + width/2, 0.875), xytext=(2.3, 0.905),
                 arrowprops=dict(facecolor=c_emerald, shrink=0.08, width=1.4, headwidth=5),
                 fontsize=8.2, fontweight='bold', color=c_emerald,
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='#ECFDF5', edgecolor=c_emerald, alpha=0.9))

    ax2.set_title(r'(b) Physical Utility Preservation ($\mathcal{J}^*$) under Reality Gap',
                  fontsize=11.2, color=c_slate_dark, fontweight='bold', pad=12)
    ax2.set_xlabel(r'Candidate Configurations in Sensitivity Neighborhood $\mathcal{N}(a_0)$',
                   fontsize=9.5, color=c_slate_dark)
    ax2.set_ylabel(r'Objective Evaluation Metric $\mathcal{J}$ and $\mathcal{J}^*$',
                   fontsize=9.5, color=c_slate_dark)
    ax2.legend(loc='lower left', fontsize=7.8, framealpha=0.95, edgecolor=c_slate_muted)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Proposition 2 figure successfully saved to: {output_path}")

if __name__ == '__main__':
    create_proposition2_reality_gap_figure("e:/projects/thesis/figures/fig_proposition2_reality_gap.png")

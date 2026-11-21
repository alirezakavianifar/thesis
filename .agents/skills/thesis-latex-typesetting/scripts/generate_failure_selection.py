import matplotlib.pyplot as plt
import numpy as np

def create_failure_selection(output_path):
    plt.rcParams['mathtext.fontset'] = 'cm'
    plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15.0, 5.8), dpi=300)

    # Palette
    c_slate_dark = '#0F172A'
    c_slate_muted = '#475569'
    c_grid = '#E2E8F0'

    # ---------------------------------------------------------
    # Subplot 1: Near-Miss Constraint Margin Reshaping
    # ---------------------------------------------------------
    K = 12
    n_sat = np.arange(0, K + 1)
    n_sat_ratio = n_sat / K
    alpha = 2.0
    sigma_delta = 0.08
    rho_base = 0.65
    gamma_u = 0.40
    u_inc = 0.60  # nominal utility incentive

    def calc_p_reshape(n_s, delta_def):
        m_rec = ((n_s / K) ** alpha) * np.exp(-delta_def / sigma_delta)
        p = rho_base * m_rec * ((1 - gamma_u) + gamma_u * u_inc)
        return p

    deficits = [
        (0.01, '#4A0E4E', '-o', 'Mean Deficit $\\bar{\\Delta}_{\\mathrm{def}} = 0.01$'),
        (0.05, '#9C179E', '-o', 'Mean Deficit $\\bar{\\Delta}_{\\mathrm{def}} = 0.05$'),
        (0.15, '#ED6925', '-o', 'Mean Deficit $\\bar{\\Delta}_{\\mathrm{def}} = 0.15$'),
        (0.35, '#FB9A06', '-o', 'Mean Deficit $\\bar{\\Delta}_{\\mathrm{def}} = 0.35$')
    ]

    for d_val, col, fmt, lbl in deficits:
        p_vals = calc_p_reshape(n_sat, d_val)
        ax1.plot(n_sat, p_vals, fmt, color=col, label=lbl, linewidth=2.2, markersize=5.5)

    # Baseline RS-DRL constant rho = 0.30
    ax1.axhline(0.30, color='#DC2626', linestyle='--', linewidth=2.0, label=r'Baseline RS-DRL ($\rho = 0.30$)')
    ax1.axhspan(0.28, 0.32, color='#DC2626', alpha=0.15)

    # Ceiling rho_base = 0.65
    ax1.axhline(rho_base, color='#059669', linestyle=':', linewidth=2.0, label=r'Ceiling: $\rho_{\mathrm{base}} = 0.65$')

    ax1.set_title(r"Near-Miss Constraint Margin Reshaping $P_{\mathrm{reshape}}(s, a)$",
                  fontsize=12.0, fontweight='bold', color=c_slate_dark, pad=12)
    ax1.set_xlabel(r"Satisfied Constraints $n_{\mathrm{sat}}$ (Normalized Ratio $n_{\mathrm{sat}}/K$)",
                   fontsize=10.5, color=c_slate_dark)
    ax1.set_ylabel(r"Failure Reshaping Probability $P_{\mathrm{reshape}}(s, a)$",
                   fontsize=10.5, color=c_slate_dark)
    ax1.set_xlim(-0.3, K + 0.3)
    ax1.set_ylim(-0.02, 0.82)
    ax1.grid(True, linestyle='-', color=c_grid, alpha=0.8)

    # Custom ticks showing both n_sat and ratio
    ax1.set_xticks(np.arange(0, K + 1, 2))
    ax1.set_xticklabels([f"{n} ({n/K:.2f})" for n in np.arange(0, K + 1, 2)], fontsize=8.8)

    # Annotations
    ax1.annotate("Catastrophic Crashes\n(Strictly Filtered: $P_{\\mathrm{reshape}} \\to 0$)",
                 xy=(1.5, 0.02), xytext=(0.5, 0.28),
                 arrowprops=dict(facecolor='#991B1B', edgecolor='#991B1B', width=1.4, headwidth=6.0, headlength=7.0),
                 fontsize=8.5, fontweight='bold', color='#991B1B')

    ax1.annotate("Recoverable Near-Misses\n(Ceiling: $\\rho_{\\mathrm{base}} = 0.65$)",
                 xy=(11.5, 0.65), xytext=(6.5, 0.70),
                 arrowprops=dict(facecolor='#065F46', edgecolor='#065F46', width=1.4, headwidth=6.0, headlength=7.0),
                 fontsize=8.5, fontweight='bold', color='#065F46')

    ax1.legend(loc='upper left', fontsize=8.2, frameon=True, framealpha=0.92)

    # ---------------------------------------------------------
    # Subplot 2: Utility-Driven Target Reshaping
    # ---------------------------------------------------------
    u_vals = np.linspace(0.0, 1.0, 100)
    r_mu = 0.30 + 0.40 * (u_vals ** 1.5)  # dynamic target
    r_rs = np.ones_like(u_vals) * 1.0     # static target

    ax2.plot(u_vals, r_mu, color='#059669', linewidth=2.8,
             label=r"MU-RS-DRL Adaptive Target $\tilde{r}_{\mathrm{opt}}(s, a)$")
    ax2.plot(u_vals, r_rs, color='#DC2626', linestyle='--', linewidth=2.4,
             label=r"Baseline RS-DRL (Fixed $\tilde{r}_{\mathrm{opt}} = 1.0$)")

    ax2.set_title("Utility-Driven Target Reshaping",
                  fontsize=12.0, fontweight='bold', color=c_slate_dark, pad=12)
    ax2.set_xlabel(r"Action Utility Incentive $\mathcal{U}_{\mathrm{inc}}(a) = (u(a)/u^{\max})^\beta$",
                   fontsize=10.5, color=c_slate_dark)
    ax2.set_ylabel(r"Optimistic Target Reward $\tilde{r}_{\mathrm{opt}}$",
                   fontsize=10.5, color=c_slate_dark)
    ax2.set_xlim(0.0, 1.0)
    ax2.set_ylim(0.2, 1.1)
    ax2.grid(True, linestyle='-', color=c_grid, alpha=0.8)
    ax2.legend(loc='center right', fontsize=8.8, frameon=True, framealpha=0.92)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Publication-grade failure selection mechanism plot saved to {output_path}")

if __name__ == '__main__':
    create_failure_selection('figures/fig_failure_selection_mechanism.png')


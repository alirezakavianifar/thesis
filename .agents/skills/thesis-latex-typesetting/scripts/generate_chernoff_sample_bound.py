import matplotlib.pyplot as plt
import numpy as np

def create_chernoff_sample_bound_figure(output_path):
    plt.rcParams['mathtext.fontset'] = 'cm'
    plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15.2, 6.2), dpi=300)

    # Color palette
    c_slate_dark = '#0F172A'
    c_slate_muted = '#64748B'
    c_emerald = '#059669'
    c_emerald_fill = '#D1FAE5'
    c_rose = '#E11D48'

    # -------------------------------------------------------------
    # Subplot 1: Chernoff-Hoeffding Sample Complexity Curves
    # -------------------------------------------------------------
    delta = np.linspace(0.01, 0.08, 200)

    alphas = [
        (0.01, '#7C3AED', '-', r'$\alpha = 0.01$ (99% Confidence Level)'),
        (0.05, '#2563EB', '-', r'$\alpha = 0.05$ (95% Confidence Level, Nominal)'),
        (0.10, '#059669', '--', r'$\alpha = 0.10$ (90% Confidence Level)')
    ]

    for a_val, col, ls, lbl in alphas:
        n_sim = np.log(2.0 / a_val) / (2.0 * delta**2)
        ax1.plot(delta, n_sim, linestyle=ls, color=col, linewidth=2.2, label=lbl)

    # Mark nominal operational point (alpha=0.05, delta=0.02)
    delta_nom = 0.02
    n_nom = np.log(2.0 / 0.05) / (2.0 * delta_nom**2)  # ~4611.1 -> 4612
    ax1.scatter(delta_nom, n_nom, color=c_rose, s=95, zorder=5, edgecolors=c_slate_dark)
    ax1.annotate(r'Nominal Benchmark Point:' + '\n' + r'$\delta = 0.02, \alpha = 0.05 \rightarrow N_{\mathrm{sim}} \geq 4{,}612$',
                 xy=(delta_nom, n_nom), xytext=(delta_nom + 0.012, n_nom + 1200),
                 arrowprops=dict(facecolor=c_rose, shrink=0.08, width=1.5, headwidth=6),
                 fontsize=8.5, fontweight='bold', color=c_rose,
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF1F2', edgecolor=c_rose, alpha=0.95))

    # Mark relaxed point delta = 0.05, alpha = 0.05 -> N_sim = 738
    delta_sub = 0.05
    n_sub = np.log(2.0 / 0.05) / (2.0 * delta_sub**2)  # ~738
    ax1.scatter(delta_sub, n_sub, color='#D97706', s=80, zorder=5, edgecolors=c_slate_dark)
    ax1.annotate(r'Relaxed Point:' + '\n' + r'$\delta = 0.05 \rightarrow N_{\mathrm{sim}} = 738$',
                 xy=(delta_sub, n_sub), xytext=(delta_sub + 0.008, n_sub + 1800),
                 arrowprops=dict(facecolor='#D97706', shrink=0.08, width=1.4, headwidth=5),
                 fontsize=8.0, fontweight='bold', color='#D97706',
                 bbox=dict(boxstyle='round,pad=0.25', facecolor='#FEF3C7', edgecolor='#D97706', alpha=0.9))

    ax1.set_xlim(0.01, 0.08)
    ax1.set_ylim(0, 10000)
    ax1.grid(True, linestyle='--', color='#E2E8F0', alpha=0.8)

    ax1.set_title(r'(a) Chernoff-Hoeffding Sample Bound: $N_{\mathrm{sim}} \geq \frac{\ln(2/\alpha)}{2\delta^2}$',
                  fontsize=11.2, color=c_slate_dark, fontweight='bold', pad=12)
    ax1.set_xlabel(r'Approximation Error Margin ($\delta$)', fontsize=9.5, color=c_slate_dark)
    ax1.set_ylabel(r'Minimum Required Stochastic Simulations ($N_{\mathrm{sim}}$)', fontsize=9.5, color=c_slate_dark)
    ax1.legend(loc='upper right', fontsize=8.2, framealpha=0.95, edgecolor=c_slate_muted)

    # -------------------------------------------------------------
    # Subplot 2: Execution Latency vs Hard CPS Control Deadlines
    # -------------------------------------------------------------
    sim_counts = np.array([500, 1000, 2000, 3000, 4612, 6000, 8000])
    latency_sec = sim_counts * 0.0012

    ax2.plot(sim_counts, latency_sec, 's-', color='#2563EB', linewidth=2.2, markersize=6,
             label=r'UPPAAL-SMC Latency ($\approx 1.2\,\mathrm{ms}$ / simulation)')

    # Point for nominal N_sim = 4612
    lat_nom = 4612 * 0.0012  # 5.53 seconds (analytical at 1.2 ms/sim)
    ax2.scatter(4612, lat_nom, color=c_rose, s=90, zorder=6, edgecolors=c_slate_dark)
    ax2.annotate(r'CPS Model Baseline:' + '\n' + r'$N_{\mathrm{sim}} = 4{,}612 \rightarrow t \approx 5.53\,\mathrm{s}$' + '\n' + r'($110\times$ Over Deadline)',
                 xy=(4612, lat_nom), xytext=(2400, 7.6),
                 arrowprops=dict(facecolor=c_rose, shrink=0.08, width=1.5, headwidth=6),
                 fontsize=8.2, fontweight='bold', color=c_rose,
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF1F2', edgecolor=c_rose, alpha=0.95))

    # Point for empirical DeltaIoT on Ryzen 9 5950X (3.82 s)
    lat_deltaiot = 3.82
    ax2.scatter(4612, lat_deltaiot, color='#059669', s=90, zorder=6, edgecolors=c_slate_dark)
    ax2.annotate(r'DeltaIoT Empirical Batch:' + '\n' + r'$N_{\mathrm{sim}} = 4{,}612 \rightarrow t = 3.82\,\mathrm{s}$' + '\n' + r'($76\times$ Over Deadline)',
                 xy=(4612, lat_deltaiot), xytext=(5200, 3.8),
                 arrowprops=dict(facecolor='#059669', shrink=0.08, width=1.5, headwidth=6),
                 fontsize=8.2, fontweight='bold', color='#059669',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='#F0FDF4', edgecolor='#059669', alpha=0.95))

    # Hard Real-Time CPS Control Deadline (50ms = 0.05s)
    deadline_sec = 0.05
    ax2.axhline(deadline_sec, color='#DC2626', linestyle='--', linewidth=2.0,
                label=r'Hard CPS Deadline ($T_{\mathrm{deadline}} = 50\,\mathrm{ms} = 0.05\,\mathrm{s}$)')
    ax2.axhspan(0, deadline_sec, color=c_emerald_fill, alpha=0.35,
                label=r'Admissible Control Window ($t \leq 50\,\mathrm{ms}$)')

    ax2.set_xlim(0, 8500)
    ax2.set_ylim(0, 10.5)
    ax2.grid(True, linestyle='--', color='#E2E8F0', alpha=0.8)

    # Explanatory annotation box
    box_text = ("Architectural Consequence:\n"
                "Synchronous runtime SMC in the direct path\n"
                "causes catastrophic control loop starvation.\n"
                r"$\Rightarrow$ Asynchronous Background Verification" + "\n"
                "in the feedback loop is strictly mandatory.")
    ax2.text(4400, 1.0, box_text,
             fontsize=8.3, color=c_slate_dark,
             bbox=dict(boxstyle='round,pad=0.35', facecolor='#F8FAFC', edgecolor='#CBD5E1', alpha=0.95))

    # Inset Axes for Magnifying the Sub-100ms Region
    # Inset showing: RS-DRL+ Nominal (0.485ms), PG-ALR Refinement (<3.5ms), and 50ms Deadline
    axins = ax2.inset_axes([0.11, 0.25, 0.30, 0.32])
    
    methods = [r'Nominal ($a_0$)', r'PG-ALR ($a^*$)', r'CPS Deadline']
    lat_ms = [0.485, 3.435, 50.0]
    colors_ms = ['#2563EB', '#059669', '#DC2626']
    
    x_pos = np.arange(len(methods))
    bars = axins.bar(x_pos, lat_ms, color=colors_ms, width=0.55, edgecolor=c_slate_dark)
    axins.set_xticks(x_pos)
    axins.set_xticklabels(methods, fontsize=7.2, rotation=15)
    axins.set_yscale('log')
    axins.set_ylim(0.1, 80)
    axins.grid(True, linestyle=':', color='#CBD5E1', alpha=0.7)
    axins.set_ylabel(r'Latency [$\mathrm{ms}$]', fontsize=7.2)
    axins.set_title(r'Real-Time Window ($\leq 50\,\mathrm{ms}$)', fontsize=7.8, fontweight='bold', color=c_slate_dark)

    for bar, val in zip(bars, lat_ms):
        yval = bar.get_height()
        axins.text(bar.get_x() + bar.get_width()/2.0, yval * 1.15, f'{val} ms',
                   ha='center', va='bottom', fontsize=6.8, fontweight='bold')

    ax2.set_title(r'(b) Verification Latency vs. Hard Real-Time CPS Deadlines',
                  fontsize=11.2, color=c_slate_dark, fontweight='bold', pad=12)
    ax2.set_xlabel(r'Number of SMC Simulation Runs ($N_{\mathrm{sim}}$)', fontsize=9.5, color=c_slate_dark)
    ax2.set_ylabel(r'Total Verification Latency (Seconds)', fontsize=9.5, color=c_slate_dark)
    ax2.legend(loc='upper left', fontsize=8.0, framealpha=0.95, edgecolor=c_slate_muted)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Chernoff sample bound figure successfully saved to: {output_path}")

if __name__ == '__main__':
    create_chernoff_sample_bound_figure("e:/projects/thesis/figures/fig_chernoff_sample_bound.png")

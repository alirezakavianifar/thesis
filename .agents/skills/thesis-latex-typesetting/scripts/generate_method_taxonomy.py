import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path

def create_method_taxonomy(output_path):
    plt.rcParams['mathtext.fontset'] = 'cm'
    plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']

    # Dimensions: 17.0 x 12.0 inches, 300 DPI publication grade
    fig, ax = plt.subplots(figsize=(17.0, 12.0), dpi=300)
    ax.set_xlim(0, 22.0)
    ax.set_ylim(0, 15.6)
    ax.axis('off')

    # Color palette
    c_slate_dark = '#0F172A'
    c_slate_mid = '#334155'
    c_slate_muted = '#475569'
    c_border_gray = '#CBD5E1'

    c_blue_border = '#2563EB'
    c_blue_fill = '#EFF6FF'
    c_blue_title = '#1E3A8A'

    c_emerald_border = '#059669'
    c_emerald_fill = '#ECFDF5'
    c_emerald_title = '#065F46'

    c_teal_border = '#0D9488'
    c_teal_fill = '#F0FDFA'
    c_teal_title = '#115E59'

    c_amber_border = '#D97706'
    c_amber_fill = '#FEF3C7'
    c_amber_title = '#78350F'

    c_purple_border = '#7C3AED'
    c_purple_fill = '#F5F3FF'
    c_purple_title = '#4C1D95'

    c_rose_border = '#E11D48'
    c_rose_fill = '#FFF1F2'
    c_rose_title = '#881337'

    c_indigo_border = '#4F46E5'
    c_indigo_fill = '#EEF2FF'
    c_indigo_title = '#312E81'

    def draw_card(x, y, w, h, fill, border, r=0.18, lw=1.4):
        box = patches.FancyBboxPatch(
            (x - w/2, y - h/2), w, h,
            boxstyle=f"round,pad=0,rounding_size={r}",
            facecolor=fill, edgecolor=border, linewidth=lw
        )
        ax.add_patch(box)

    # =============================================================
    # 0. ROOT CARD (Taxonomy Title)
    # Center (11.0, 14.65), width 15.0, height 1.35
    # =============================================================
    draw_card(11.0, 14.65, 15.0, 1.35, '#FFFFFF', c_blue_border, r=0.25, lw=1.8)
    ax.text(11.0, 15.02, "Self-Adaptive Software Adaptation Method Families",
            ha='center', va='center', fontsize=12.5, fontweight='bold', color=c_blue_title)
    ax.text(11.0, 14.62, "Taxonomy of Decision-Making Paradigms: From Unbounded Search to Real-Time Two-Tier Synthesis (RS-DRL+)",
            ha='center', va='center', fontsize=8.2, fontweight='bold', color=c_slate_dark)
    ax.text(11.0, 14.22, "Domain-Agnostic Patterns (SG-OS & CA-EPV) Instantiated on Aerial CPS (DARTSim 6-DOF) & Discrete WSN (DeltaIoT)",
            ha='center', va='center', fontsize=7.5, color=c_slate_muted)

    # Root Branching Lines: Leaves (11.0, 13.975) -> splits to x=4.2 and x=14.8 at y=13.45
    path_root_l = [
        (Path.MOVETO, (11.0, 13.975)),
        (Path.LINETO, (11.0, 13.45)),
        (Path.LINETO, (4.2, 13.45)),
        (Path.LINETO, (4.2, 13.15))
    ]
    codes_l, verts_l = zip(*path_root_l)
    ax.add_patch(patches.PathPatch(Path(verts_l, codes_l), facecolor='none', edgecolor=c_slate_mid, lw=1.5))
    ax.annotate('', xy=(4.2, 13.15), xytext=(4.2, 13.35),
                arrowprops=dict(facecolor=c_slate_mid, edgecolor=c_slate_mid, width=1.2, headwidth=5.0, headlength=5.5))

    path_root_r = [
        (Path.MOVETO, (11.0, 13.45)),
        (Path.LINETO, (14.8, 13.45)),
        (Path.LINETO, (14.8, 13.15))
    ]
    codes_r, verts_r = zip(*path_root_r)
    ax.add_patch(patches.PathPatch(Path(verts_r, codes_r), facecolor='none', edgecolor=c_slate_mid, lw=1.5))
    ax.annotate('', xy=(14.8, 13.15), xytext=(14.8, 13.35),
                arrowprops=dict(facecolor=c_slate_mid, edgecolor=c_slate_mid, width=1.2, headwidth=5.0, headlength=5.5))

    # =============================================================
    # 1. LEFT COLUMN: SEARCH-BASED & FORMAL ASSURANCE BASELINES
    # Header: x = 4.2, width 7.0, height 1.00
    # Cards: center x = 4.2, width 6.8
    # =============================================================
    draw_card(4.2, 12.65, 7.0, 1.00, c_rose_fill, c_rose_border, lw=1.6)
    ax.text(4.2, 12.92, "Search-Based & Formal Guard Baselines",
            ha='center', va='center', fontsize=9.8, fontweight='bold', color=c_rose_title)
    ax.text(4.2, 12.48, r"Online Iterative Search & Verification $\cdot$ Latency $62\,\mathrm{ms} - 133\,\mathrm{s}$",
            ha='center', va='center', fontsize=7.6, color=c_rose_title)

    # Vertical hierarchy distribution bus for left column:
    # Drops from (4.2, 12.15) -> (4.2, 11.85) -> (0.50, 11.85) -> down to y = 5.25
    path_sbse_bus = [
        (Path.MOVETO, (4.2, 12.15)),
        (Path.LINETO, (4.2, 11.85)),
        (Path.LINETO, (0.50, 11.85)),
        (Path.LINETO, (0.50, 5.25))
    ]
    codes_sbse, verts_sbse = zip(*path_sbse_bus)
    ax.add_patch(patches.PathPatch(Path(verts_sbse, codes_sbse), facecolor='none', edgecolor=c_rose_border, lw=1.4))

    # Horizontal branch arrows into each card from the left spine (0.50 -> 0.80):
    y_cards_l = [10.95, 9.05, 7.15, 5.25]
    for y_c in y_cards_l:
        ax.plot([0.50, 0.80], [y_c, y_c], color=c_rose_border, lw=1.3)
        ax.annotate('', xy=(0.80, y_c), xytext=(0.50, y_c),
                    arrowprops=dict(facecolor=c_rose_border, edgecolor=c_rose_border, width=1.1, headwidth=4.5, headlength=5.0))

    # Card 1: XDA-II (x = 4.2, y = 10.95, height 1.35)
    draw_card(4.2, 10.95, 6.8, 1.35, c_rose_fill, c_rose_border)
    ax.text(4.2, 11.42, "XDA-II: Explainable Guided Search (Prior Art)", ha='center', va='center', fontsize=8.4, fontweight='bold', color=c_rose_title)
    xda_text = (
        "• White-box attributions (TreeSHAP / PFI / PDP) guide 1D search\n"
        r"• Online Latency: $62.61 - 205.40\,\mathrm{ms}$ (misses hard sub-second deadlines)" "\n"
        r"• Reality Gap: Flight survival drops to $50.0\%$ in strict flight dynamics"
    )
    ax.text(4.2, 10.78, xda_text, ha='center', va='center', fontsize=6.8, color=c_slate_dark, linespacing=1.2)

    # Card 2: NSGA-III & FITEST (x = 4.2, y = 9.05, height 1.35)
    draw_card(4.2, 9.05, 6.8, 1.35, c_rose_fill, c_rose_border)
    ax.text(4.2, 9.52, "Multi-Objective Evolutionary Search (NSGA-III / FITEST)", ha='center', va='center', fontsize=8.2, fontweight='bold', color=c_rose_title)
    moo_text = (
        "• Reference-point Pareto non-dominated sorting across conflicting QoS\n"
        r"• Latency: $> 133\,\mathrm{seconds}$ (FITEST) / $205.4\,\mathrm{ms}$ (NSGA-III)" "\n"
        r"• Airspeed Throttling: Severe degradation ($d_{\mathrm{norm}} = 0.3546$), unviable for real-time CPS"
    )
    ax.text(4.2, 8.88, moo_text, ha='center', va='center', fontsize=6.8, color=c_slate_dark, linespacing=1.2)

    # Card 3: Runtime Shielded Baselines (x = 4.2, y = 7.15, height 1.35)
    draw_card(4.2, 7.15, 6.8, 1.35, c_purple_fill, c_purple_border)
    ax.text(4.2, 7.62, "Runtime Shielded Baselines (Weyns et al. / ActivFORMS)", ha='center', va='center', fontsize=8.2, fontweight='bold', color=c_purple_title)
    shield_text = (
        "• Post-hoc formal verifier / surrogate guard wrapped around unverified policy\n"
        r"• High surrogate compliance ($76.0\%$), but reality gap exposes $65.0\%$ physical survival" "\n"
        r"• Latency: Injects $130\,\mathrm{ms}$ verification overhead (exceeds real-time deadlines)"
    )
    ax.text(4.2, 6.98, shield_text, ha='center', va='center', fontsize=6.8, color=c_slate_dark, linespacing=1.2)

    # Card 4: Random Search (x = 4.2, y = 5.25, height 1.35)
    draw_card(4.2, 5.25, 6.8, 1.35, '#F8FAFC', c_border_gray)
    ax.text(4.2, 5.72, "Random Search (Negative Control Baseline)", ha='center', va='center', fontsize=8.2, fontweight='bold', color=c_slate_dark)
    rnd_text = (
        r"• Uniform unguided stochastic sampling across controllable parameter space $\mathcal{A}$" "\n"
        r"• Feasibility Compliance: $1.0\%$ (near-total constraint violation)" "\n"
        r"• Flight Survival: $25.0\%$ (uninformed baseline lower bound)"
    )
    ax.text(4.2, 5.08, rnd_text, ha='center', va='center', fontsize=6.8, color=c_slate_muted, linespacing=1.2)

    # =============================================================
    # 2. RIGHT COLUMN: REINFORCEMENT LEARNING & POLICY COMPILATION
    # Header: x = 14.8, width 13.4, height 1.00
    # =============================================================
    draw_card(14.8, 12.65, 13.4, 1.00, c_emerald_fill, c_emerald_border, lw=1.6)
    ax.text(14.8, 12.92, "Reinforcement Learning (RL) Policy Compilation & Synthesis",
            ha='center', va='center', fontsize=10.2, fontweight='bold', color=c_emerald_title)
    ax.text(14.8, 12.48, r"Offline Experience Replay $\to$ Deterministic $\mathcal{O}(1)$ Runtime Inference ($< 0.5\,\mathrm{ms}$, $1.7\,\mathrm{KB}$ RAM)",
            ha='center', va='center', fontsize=7.6, color=c_emerald_title)

    # Symmetrical sub-column coordinates:
    # Column 1 center: x = 11.0, width = 5.30 (x in [8.35, 13.65])
    # Column 2 center: x = 18.6, width = 5.30 (x in [15.95, 21.25])
    # Central gap: x in [13.65, 15.95] (width = 2.30)
    x_col1 = 11.0
    x_col2 = 18.6
    w_card_r = 5.30

    # Distribution Bus to RL Baselines
    # Spine: drops from (14.8, 12.15) to (14.8, 11.85)
    # Horizontal bus: from x = 11.0 to x = 18.6 at y = 11.85
    ax.plot([14.8, 14.8], [12.15, 11.85], color=c_emerald_border, lw=1.4)
    ax.plot([x_col1, x_col2], [11.85, 11.85], color=c_emerald_border, lw=1.4)
    ax.annotate('', xy=(x_col1, 11.625), xytext=(x_col1, 11.85),
                arrowprops=dict(facecolor=c_emerald_border, edgecolor=c_emerald_border, width=1.1, headwidth=4.5, headlength=5.0))
    ax.annotate('', xy=(x_col2, 11.625), xytext=(x_col2, 11.85),
                arrowprops=dict(facecolor=c_emerald_border, edgecolor=c_emerald_border, width=1.1, headwidth=4.5, headlength=5.0))

    # Card 1: Baseline DQN (x = 11.0, y = 10.95, width 5.30, height 1.35)
    draw_card(x_col1, 10.95, w_card_r, 1.35, c_blue_fill, c_blue_border)
    ax.text(x_col1, 11.45, r"Baseline DQN (Unshaped, $\rho = 0.0$)", ha='center', va='center', fontsize=8.4, fontweight='bold', color=c_blue_title)
    dqn_text = (
        "• Standard TD Q-learning (no failure reshaping assistance)\n"
        r"• Severe failure regime dominance ($90.98\%$ transitions violate)" "\n"
        r"• Depressed Q-values ($\max Q \approx 0.988$), high variance ($\sigma_d = 0.165$)"
    )
    ax.text(x_col1, 10.82, dqn_text, ha='center', va='center', fontsize=6.8, color=c_slate_dark, linespacing=1.2)

    # Card 2: Foundational RS-DRL (x = 18.6, y = 10.95, width 5.30, height 1.35)
    draw_card(x_col2, 10.95, w_card_r, 1.35, c_blue_fill, c_blue_border)
    ax.text(x_col2, 11.45, "Foundational RS-DRL (Prior Art)", ha='center', va='center', fontsize=8.4, fontweight='bold', color=c_blue_title)
    rsdrl_text = (
        r"• Uniform Bernoulli failure replacement with fixed probability $\rho = 0.30$" "\n"
        r"• Static optimistic reward ($\tilde{r}_{\mathrm{opt}} = 1.0$), blind to severity/utility" "\n"
        "• WSN Baselines: Retained for DeltaIoT discrete comparison (HER/SHER)"
    )
    ax.text(x_col2, 10.82, rsdrl_text, ha='center', va='center', fontsize=6.8, color=c_slate_dark, linespacing=1.2)

    # =============================================================
    # 3. PROPOSED FRAMEWORK CONTAINER (OURS)
    # x in [8.1, 21.5] (width 13.4, height 9.40), y in [0.65, 10.05]
    # =============================================================
    box_ours = patches.FancyBboxPatch(
        (8.1, 0.65), 13.4, 9.40,
        boxstyle="round,pad=0,rounding_size=0.35",
        facecolor='#FFFBEB', edgecolor=c_amber_border, linewidth=1.8, linestyle='--'
    )
    ax.add_patch(box_ours)

    # Banner Header for Proposed Box
    draw_card(14.8, 9.75, 12.8, 0.44, c_amber_fill, c_amber_border, r=0.10, lw=1.2)
    ax.text(14.8, 9.75, "PROPOSED RS-DRL+ ARCHITECTURAL PATTERNS & FRAMEWORK (THIS THESIS)",
            ha='center', va='center', fontsize=9.2, fontweight='bold', color=c_amber_title)

    # Connection from RL distribution bus down to Proposed Box Banner
    ax.plot([14.8, 14.8], [11.85, 10.05], color=c_emerald_border, lw=1.4)
    ax.annotate('', xy=(14.8, 9.97), xytext=(14.8, 10.35),
                arrowprops=dict(facecolor=c_emerald_border, edgecolor=c_emerald_border, width=1.1, headwidth=4.5, headlength=5.0))

    # Fork bus from bottom of banner into MU-RS-DRL and CM-RS-DRL:
    # Drops from (14.8, 9.53) -> (14.8, 9.20) -> splits to x = 11.0 and x = 18.6
    ax.plot([14.8, 14.8], [9.53, 9.20], color=c_amber_border, lw=1.4)
    ax.plot([x_col1, x_col2], [9.20, 9.20], color=c_amber_border, lw=1.4)
    ax.annotate('', xy=(x_col1, 8.92), xytext=(x_col1, 9.20),
                arrowprops=dict(facecolor=c_emerald_border, edgecolor=c_emerald_border, width=1.1, headwidth=4.5, headlength=5.0))
    ax.annotate('', xy=(x_col2, 8.92), xytext=(x_col2, 9.20),
                arrowprops=dict(facecolor=c_teal_border, edgecolor=c_teal_border, width=1.1, headwidth=4.5, headlength=5.0))

    # -------------------------------------------------------------
    # ROW 1 (y = 7.75): PATTERN 1 (SG-OS: Specification-Guided Offline Synthesis)
    # -------------------------------------------------------------
    # Instantiation A: MU-RS-DRL (x = 11.0, y = 7.75, width 5.30, height 2.30)
    draw_card(x_col1, 7.75, w_card_r, 2.30, c_emerald_fill, c_emerald_border, lw=1.5)
    ax.text(x_col1, 8.65, "Pattern 1 (SG-OS): MU-RS-DRL", ha='center', va='center', fontsize=8.6, fontweight='bold', color=c_emerald_title)
    ax.text(x_col1, 8.32, "Margin-Aware Utility Failure Reshaping", ha='center', va='center', fontsize=7.4, fontweight='bold', color='#047857')
    mu_text = (
        r"• Invariant: $\lim_{n_{\mathrm{sat}} \to 0} \mathcal{M} = 0, \quad \tilde{r}_{\mathrm{opt}} = r_{\mathrm{base}}^{\mathrm{MU}} + \mu \mathcal{U}_{\mathrm{inc}}(a)$" "\n"
        r"• Recoverability: $\mathcal{M}(s, a) = (n_{\mathrm{sat}}/K)^\alpha \exp(-\bar{\Delta}_{\mathrm{def}}/\sigma_\Delta)$" "\n"
        r"• Utility Incentive: $\mathcal{U}_{\mathrm{inc}}(a) = (u(a)/u^{\max})^\beta$ (curbs inaction)" "\n"
        r"• Performance: $70.0\%$ flight safety, $0.48\,\mathrm{ms}$ ($130\times$ faster than XDA-II)"
    )
    ax.text(x_col1, 7.42, mu_text, ha='center', va='center', fontsize=6.8, color=c_slate_dark, linespacing=1.2)

    # Instantiation B: CM-RS-DRL (x = 18.6, y = 7.75, width 5.30, height 2.30)
    draw_card(x_col2, 7.75, w_card_r, 2.30, c_teal_fill, c_teal_border, lw=1.5)
    ax.text(x_col2, 8.65, "Pattern 1 (SG-OS): CM-RS-DRL", ha='center', va='center', fontsize=8.6, fontweight='bold', color=c_teal_title)
    ax.text(x_col2, 8.32, "Confidence-Margin Augmented Reshaping", ha='center', va='center', fontsize=7.4, fontweight='bold', color='#0F766E')
    cm_text = (
        r"• Invariant: Boundary penalty via normalized cushion $\bar{\mathcal{B}}(s, a)$" "\n"
        r"• Cushion: $\bar{\mathcal{B}}(s, a) = \frac{1}{K}\sum_{k} \frac{\max(0, M_k - \tau_k)}{1 - \tau_k} \in [0, 1]$" "\n"
        r"• Reshaping: $\tilde{r}_{\mathrm{CM}} = r_{\mathrm{base}}^{\mathrm{CM}} + \lambda_{\mathrm{margin}}\bar{\mathcal{B}} + \lambda_{\mathrm{util}}\mathcal{U}_{\mathrm{inc}}$" "\n"
        r"• Performance: Tightest flight consistency ($\sigma_d = 0.087$), amortized"
    )
    ax.text(x_col2, 7.42, cm_text, ha='center', va='center', fontsize=6.8, color=c_slate_dark, linespacing=1.2)

    # Dotted bus between MU and CM (indicating alternate offline synthesis formulations)
    ax.plot([13.65, 15.95], [7.75, 7.75], color=c_teal_border, lw=1.2, linestyle=':')

    # -------------------------------------------------------------
    # ROW 2 (y = 4.05): PATTERN 2 (CA-EPV) & FULL ARCHITECTURE (RS-DRL+)
    # -------------------------------------------------------------
    # Pattern 2 (CA-EPV): PG-ALR Online Anytime Refiner (x = 11.0, y = 4.05, width 5.30, height 2.35)
    draw_card(x_col1, 4.05, w_card_r, 2.35, c_indigo_fill, c_indigo_border, lw=1.5)
    ax.text(x_col1, 4.98, "Pattern 2 (CA-EPV): PG-ALR", ha='center', va='center', fontsize=8.6, fontweight='bold', color=c_indigo_title)
    ax.text(x_col1, 4.65, "Policy-Guided Anytime Local Refiner & Shield", ha='center', va='center', fontsize=7.4, fontweight='bold', color='#4338CA')
    pg_text = (
        r"• Stage 1: Nominal proposal $a_0 = \arg\max Q(s, a)$ ($0.485\,\mathrm{ms}$)" "\n"
        r"• Stage 2: Threat gate $\Delta_{\min}(s, a_0) \geq 0 \wedge \mathcal{E}(of) \leq \epsilon_{\mathrm{threshold}}$" "\n"
        r"• Stage 3: XAI 1-hop micro-neighborhood $\mathcal{N}(a_0)$ along top-$m$ SHAP" "\n"
        r"• Contract-Anytime: Strictly bounded $< 3.5\,\mathrm{ms}$, non-degradation"
    )
    ax.text(x_col1, 3.75, pg_text, ha='center', va='center', fontsize=6.8, color=c_slate_dark, linespacing=1.2)

    # Integrated RS-DRL+ Two-Tier Architecture (x = 18.6, y = 4.05, width 5.30, height 2.35)
    draw_card(x_col2, 4.05, w_card_r, 2.35, c_amber_fill, c_amber_border, lw=1.8)
    ax.text(x_col2, 4.98, "RS-DRL+ (Full Two-Tier Architecture)", ha='center', va='center', fontsize=8.6, fontweight='bold', color=c_amber_title)
    ax.text(x_col2, 4.65, "SG-OS Offline Synthesis + CA-EPV Online Refinement", ha='center', va='center', fontsize=7.4, fontweight='bold', color='#B45309')
    plus_text = (
        r"• Unified Dual-Tier: Fast-path SG-OS dispatch ($0.48\,\mathrm{ms}$ nominal)" "\n"
        r"• Anytime Shield: Context-aware stress gate $\mathcal{E}$ + refiner ($< 3.5\,\mathrm{ms}$)" "\n"
        r"• Peak CPS Safety: $70.5\%$ survival under severe turbulence & WSN Pareto" "\n"
        r"• Full Reusability: 0 core rewrites across DARTSim (continuous) & DeltaIoT"
    )
    ax.text(x_col2, 3.75, plus_text, ha='center', va='center', fontsize=6.8, color=c_slate_dark, linespacing=1.2)

    # -------------------------------------------------------------
    # CLEAN INTER-PATTERN INTEGRATION BUSES & PILL BADGES
    # Gap between Row 1 and Row 2: y in [5.225, 6.60], delta_y = 1.375
    # Gap between Left and Right: x in [13.65, 15.95], delta_x = 2.30
    # ZERO OVERLAPS GUARANTEED!
    # -------------------------------------------------------------
    y_badge_vert = 5.9125

    # 1. Nominal Weights Transfer: MU-RS-DRL -> PG-ALR (x = 11.0)
    ax.plot([x_col1, x_col1], [6.60, y_badge_vert + 0.18], color=c_emerald_border, lw=1.3)
    ax.plot([x_col1, x_col1], [y_badge_vert - 0.18, 5.24], color=c_emerald_border, lw=1.3)
    ax.annotate('', xy=(x_col1, 5.24), xytext=(x_col1, 5.50),
                arrowprops=dict(facecolor=c_emerald_border, edgecolor=c_emerald_border, width=1.2, headwidth=5.0, headlength=5.5))
    draw_card(x_col1, y_badge_vert, 2.50, 0.36, '#ECFDF5', c_emerald_border, r=0.08, lw=0.9)
    ax.text(x_col1, y_badge_vert, r"Nominal Weights $\theta_{\mathrm{active}}$", ha='center', va='center', fontsize=6.6, fontweight='bold', color=c_emerald_title)

    # 2. Tier 1 Policy Dispatch: CM-RS-DRL -> RS-DRL+ (x = 18.6)
    ax.plot([x_col2, x_col2], [6.60, y_badge_vert + 0.18], color=c_amber_border, lw=1.3)
    ax.plot([x_col2, x_col2], [y_badge_vert - 0.18, 5.24], color=c_amber_border, lw=1.3)
    ax.annotate('', xy=(x_col2, 5.24), xytext=(x_col2, 5.50),
                arrowprops=dict(facecolor=c_amber_border, edgecolor=c_amber_border, width=1.2, headwidth=5.0, headlength=5.5))
    draw_card(x_col2, y_badge_vert, 2.50, 0.36, '#FEF3C7', c_amber_border, r=0.08, lw=0.9)
    ax.text(x_col2, y_badge_vert, "Tier 1: SG-OS Offline Policy", ha='center', va='center', fontsize=6.6, fontweight='bold', color=c_amber_title)

    # 3. Tier 2 Online Anytime Shield: PG-ALR -> RS-DRL+ (horizontal at y = 4.05)
    # Gap is x in [13.65, 15.95] (width 2.30). Pill badge width 1.50 (x in [14.05, 15.55])
    # Left margin: 14.05 - 13.65 = 0.40; Right margin: 15.95 - 15.55 = 0.40
    x_badge_h = 14.80
    w_badge_h = 1.50
    ax.plot([13.65, x_badge_h - w_badge_h/2], [4.05, 4.05], color=c_indigo_border, lw=1.3)
    ax.plot([x_badge_h + w_badge_h/2, 15.93], [4.05, 4.05], color=c_indigo_border, lw=1.3)
    ax.annotate('', xy=(15.93, 4.05), xytext=(15.65, 4.05),
                arrowprops=dict(facecolor=c_indigo_border, edgecolor=c_indigo_border, width=1.2, headwidth=5.0, headlength=5.5))
    draw_card(x_badge_h, 4.05, w_badge_h, 0.36, '#EEF2FF', c_indigo_border, r=0.08, lw=0.9)
    ax.text(x_badge_h, 4.05, "Tier 2: CA-EPV Shield", ha='center', va='center', fontsize=6.6, fontweight='bold', color=c_indigo_title)

    # =============================================================
    # 4. BOTTOM FOOTER BANNER
    # Center (14.8, 1.25), width 12.8, height 0.50
    # =============================================================
    draw_card(14.8, 1.25, 12.8, 0.50, '#FFFFFF', c_amber_border, r=0.10, lw=1.2)
    banner_text = (
        "Domain-Agnostic Core: SG-OS Synthesis Invariant + CA-EPV Contract-Anytime Bound  |  "
        r"Domain-Specific: State $\mathcal{S}$, Action $\mathcal{A}$, Utility $\mathcal{U}(a)$, Stress $\mathcal{E}(of)$"
    )
    ax.text(14.8, 1.25, banner_text, ha='center', va='center', fontsize=7.4, fontweight='bold', color=c_amber_title)

    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Publication-grade method taxonomy tree saved to {output_path}")

if __name__ == '__main__':
    create_method_taxonomy('figures/fig_method_taxonomy_tree.png')

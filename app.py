import streamlit as st

st.set_page_config(
    page_title="DG Cold Chain ROI — EROAD",
    page_icon="❄️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Password Gate ───
def check_password():
    """Simple password gate. Set password in .streamlit/secrets.toml or Streamlit Cloud secrets."""
    correct = st.secrets.get("password", "eroad2026")

    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if st.session_state.authenticated:
        return True

    st.markdown("<div style='max-width:400px; margin:80px auto;'>", unsafe_allow_html=True)
    st.image("https://www.eroad.com/wp-content/uploads/2025/10/EROAD_LogoWithWordmark_RGB.png", width=180)
    st.markdown("#### Cold Chain ROI Calculator")
    pwd = st.text_input("Password", type="password", placeholder="Enter access password")
    if pwd:
        if pwd == correct:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Incorrect password.")
    st.markdown("</div>", unsafe_allow_html=True)
    return False

if not check_password():
    st.stop()

# Minimal CSS — just EROAD branding + cleanup
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&display=swap');
#MainMenu, footer {visibility: hidden;}
.block-container {padding-top: 1rem; max-width: 1100px;}
[data-testid="stNumberInput"] input,
[data-testid="stMetricValue"] {font-family: 'JetBrains Mono', monospace !important;}

/* Make the native sidebar toggle bigger and visible */
button[data-testid="stBaseButton-headerNoPadding"] {
    background: #1869b8 !important;
    color: white !important;
    border-radius: 8px !important;
    width: 40px !important;
    height: 40px !important;
    position: fixed !important;
    top: 12px !important;
    left: 12px !important;
    z-index: 999999 !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.15) !important;
}
button[data-testid="stBaseButton-headerNoPadding"] svg {
    width: 22px !important;
    height: 22px !important;
    stroke: white !important;
}
</style>
""", unsafe_allow_html=True)

# ─── Sidebar toggle hint (visible when sidebar is closed) ───
st.markdown("""
<div id="sidebar-hint" style="position:fixed; top:14px; left:60px; z-index:999998;
     background:#1869b8; color:white; font-size:0.75rem; font-weight:600;
     padding:6px 14px; border-radius:6px; box-shadow:0 2px 8px rgba(0,0,0,0.12);
     pointer-events:none; opacity:0.9;">
    ← Adjust Inputs
</div>
<script>
    // Hide hint when sidebar is open
    const observer = new MutationObserver(() => {
        const sidebar = document.querySelector('[data-testid="stSidebar"]');
        const hint = document.getElementById('sidebar-hint');
        if (sidebar && hint) {
            const collapsed = sidebar.getAttribute('aria-expanded') === 'false'
                || sidebar.classList.contains('st-emotion-cache-1gwvy71');
            hint.style.display = collapsed ? 'block' : 'none';
        }
    });
    observer.observe(document.body, {attributes: true, subtree: true, attributeFilter: ['aria-expanded', 'class']});
</script>
""", unsafe_allow_html=True)

# ─── Logos + Title ───
st.markdown("""
<div style="display:flex; align-items:center; gap:20px; margin-bottom:6px;">
    <img src="https://www.eroad.com/wp-content/uploads/2025/10/EROAD_LogoWithWordmark_RGB.png"
         height="36" onerror="this.outerHTML='<span style=color:#1869b8;font-weight:800;font-size:1.4rem>EROAD</span>'" />
    <span style="color:#bbb; font-size:1.4rem; font-weight:300;">&times;</span>
    <span style="background:#000; color:#FFC220; font-weight:800; font-size:1.05rem; padding:4px 12px; border-radius:4px; letter-spacing:1px;">DOLLAR GENERAL</span>
</div>
""", unsafe_allow_html=True)

st.title("Cold Chain ROI Calculator")
st.caption("EROAD Value Engineering — Discovery Call Tool")

# ─── Value Story ───
st.markdown("""
<div style="background:#f5f6f8; border-left:4px solid #1869b8; border-radius:6px; padding:16px 20px; margin:12px 0 8px 0;">
    <div style="font-weight:700; color:#1869b8; margin-bottom:6px; font-size:0.95rem;">The Dollar General Cold Chain Problem</div>
    <div style="font-size:0.88rem; line-height:1.7; color:#444;">
        DG moves perishables through <strong>~1,000 reefer trailers</strong> across one of the largest store networks in the U.S.
        Today, Orbcomm monitors <strong>return air only</strong> — a sensor that spikes 15–20&deg;F every door open
        even when product is fine. The result: hundreds of daily false alerts that FSQA learns to ignore,
        real excursions that get missed, rejected loads that cost thousands each, and drivers
        still probing product by hand at every stop.
        <br><br>
        EROAD <strong>CoreTemp</strong> replaces guesswork with physics — predicting actual product core temperature
        using thermal mass modeling. That single shift eliminates false alarms, catches real excursions before
        they become rejections, removes manual probing, and cuts reefer fuel waste.
        <strong>Four value drivers, one platform.</strong>
        <br><br>
        <span style="color:#888; font-size:0.82rem;">
            Context: July 2025 FDA Class II temperature recall at DG stores.
            FSMA 204 traceability rules tightening in 2026.
        </span>
    </div>
</div>
""", unsafe_allow_html=True)

# ─── Value Map ───
st.subheader("Value Map")
st.caption("DG Strategic Objectives (10-K) \u2192 Operational Priorities \u2192 EROAD Value Drivers")

# Tier 1: DG Strategic Objectives
st.markdown("**DG Strategic Objectives** *(FY2024 10-K / Earnings)*")
obj1, obj2, obj3 = st.columns(3)
with obj1:
    st.info("**Driving Profitable Sales Growth**\n\nProtect perishable revenue, reduce spoilage losses, improve DG Fresh availability\n\n`Target: 2-3% same-store comp`")
with obj2:
    st.info("**Low-Cost Operator / Save to Serve**\n\nReduce fleet operating costs, eliminate manual labor waste, lower SG&A burden\n\n`Target: 6-7% operating margin`")
with obj3:
    st.info("**Shrink Reduction**\n\n\\#1 margin tailwind -- temperature abuse is invisible shrink in cold chain\n\n`90+ bps improvement (Q3 FY25)`")

st.markdown("<div style='text-align:center; color:#bbb; font-size:1.2rem; margin:-8px 0 -4px 0;'>\u25be \u25be \u25be</div>", unsafe_allow_html=True)

# Tier 2: DG Operational Priorities
st.markdown("**DG Operational Priorities** *(Cold Chain Impact)*")
op1, op2, op3, op4 = st.columns(4)
with op1:
    st.warning("**DG Fresh Self-Distribution**\n\nPerishables to 19,000+ stores via 10 cold DCs. Orbcomm return-air creates blind spots.")
with op2:
    st.warning("**OTIF Improvement**\n\n\\#1 supply chain priority. Rejected loads = failed OTIF. +470 bps on-time so far.")
with op3:
    st.warning("**Private Fleet Efficiency**\n\n2,412 tractors, 8,075 trailers. 20% savings vs 3PL. Reefer fuel is controllable.")
with op4:
    st.warning("**FSMA / Food Safety**\n\nFDA Class II recall (July '25). FSMA 204 deadline ahead. Audit-ready records required.")

st.markdown("<div style='text-align:center; color:#bbb; font-size:1.2rem; margin:-8px 0 -4px 0;'>\u25be \u25be \u25be</div>", unsafe_allow_html=True)

# Tier 3: EROAD Value Drivers
st.markdown("**EROAD CoreTemp Value Drivers** *(Quantified Below)*")
vd1, vd2, vd3, vd4 = st.columns(4)
with vd1:
    st.success("**Fuel Optimization**\n\nSmarter pre-cool + op mode = less diesel burn per trailer per day\n\n`Save to Serve`")
with vd2:
    st.success("**Rejected Load Prevention**\n\nPredict excursions before delivery -- fix in transit, not at the dock\n\n`Shrink` `OTIF`")
with vd3:
    st.success("**Probing Elimination**\n\nCoreTemp replaces handheld thermometers -- driver time back to driving\n\n`SG&A` `Fleet Efficiency`")
with vd4:
    st.success("**False Alarm Reduction**\n\nCore temp vs return air -- FSQA focuses on real risk, not noise\n\n`Shrink` `Compliance`")


# ─── Helpers ───
def fmt(n):
    if abs(n) >= 1_000_000:
        return f"${n / 1_000_000:.1f}M"
    if abs(n) >= 1_000:
        return f"${n / 1_000:,.0f}k"
    return f"${n:,.0f}"


# ─── Sidebar ───
with st.sidebar:
    st.header("Fleet Inputs")
    st.caption("DG has ~8,075 total trailers. Est 800–1,500 reefers.")
    fleet = st.number_input("Reefer Fleet Size", 50, 5000, 1000, step=50)
    shift_hrs = st.number_input("Shift Duration (hrs/day)", 4, 24, 12)
    fuel_burn = st.number_input("Fuel Burn (gal/hr)", 0.5, 3.0, 1.0, step=0.1, format="%.1f")
    op_days = st.number_input("Op Days/Year", 200, 365, 260, step=5)
    diesel = st.number_input("Diesel ($/gal)", 2.00, 7.00, 3.50, step=0.10, format="%.2f")
    eroad_cost = st.number_input("EROAD $/truck/mo", 20, 150, 55, step=5,
                                 help="Placeholder — confirm with Travis")

    st.divider()
    tier = st.radio("Show tier defaults", ["Moderate (recommended)", "Conservative", "Aggressive"],
                    index=0, help="Pre-fills the value drivers below. You can still override any number.")

    # Tier defaults
    defaults = {
        "Conservative":            {"pc": 30,  "op": 0.20, "rl": 8,  "rc": 5000,  "rr": 40,
                                    "pd": 400, "ps": 8,  "pm": 2.0, "ph": 25, "pdays": 250, "pe": 80,
                                    "fa": 200, "fr": 70, "fi": 3.0, "fh": 35, "fdays": 260, "fd": 50},
        "Moderate (recommended)":  {"pc": 60,  "op": 0.30, "rl": 10, "rc": 8000,  "rr": 60,
                                    "pd": 600, "ps": 10, "pm": 3.0, "ph": 35, "pdays": 250, "pe": 100,
                                    "fa": 350, "fr": 80, "fi": 5.0, "fh": 50, "fdays": 260, "fd": 70},
        "Aggressive":              {"pc": 90,  "op": 0.40, "rl": 15, "rc": 12000, "rr": 80,
                                    "pd": 800, "ps": 12, "pm": 4.0, "ph": 40, "pdays": 250, "pe": 100,
                                    "fa": 500, "fr": 90, "fi": 7.0, "fh": 65, "fdays": 260, "fd": 90},
    }
    d = defaults[tier]

    st.divider()
    st.subheader("Fuel Improvements")
    precool = st.number_input("Pre-Cool Improvement (min)", 0, 300, d["pc"], step=5)
    opmode = st.number_input("Op Mode Reduction (gal/hr)", 0.00, 2.00, d["op"], step=0.05, format="%.2f")

    st.divider()
    st.subheader("Rejected Load Prevention")
    rej_loads = st.number_input("Rejected Loads/Month", 0, 100, d["rl"])
    rej_cost = st.number_input("Cost per Rejection ($)", 0, 50000, d["rc"], step=500)
    rej_rate = st.number_input("Reduction Rate (%)", 0, 100, d["rr"], step=5)

    st.divider()
    st.subheader("Probing Elimination")
    prob_drv = st.number_input("Drivers", 0, 5000, d["pd"], step=50)
    prob_stp = st.number_input("Stops/Driver/Day", 0, 30, d["ps"])
    prob_min = st.number_input("Minutes/Stop", 0.0, 15.0, d["pm"], step=0.5, format="%.1f")
    prob_hr = st.number_input("Driver $/hr", 0, 100, d["ph"], step=5)
    prob_days = st.number_input("Working Days/Yr", 200, 365, d["pdays"], step=5)
    prob_elim = st.number_input("Elimination Rate (%)", 0, 100, d["pe"], step=5)

    st.divider()
    st.subheader("False Alarm Reduction")
    fa_alerts = st.number_input("Alerts/Day", 0, 2000, d["fa"], step=25)
    fa_rate = st.number_input("False Alarm Rate (%)", 0, 100, d["fr"], step=5)
    fa_min = st.number_input("Investigation Min/Alert", 0.0, 30.0, d["fi"], step=0.5, format="%.1f")
    fa_hr = st.number_input("FSQA $/hr", 0, 150, d["fh"], step=5)
    fa_days = st.number_input("Op Days/Yr", 200, 365, d["fdays"], step=5)
    fa_red = st.number_input("Reduction w/ CoreTemp (%)", 0, 100, d["fd"], step=5)


# ─── Calculations ───
fuel_precool = fleet * fuel_burn * op_days * diesel * (precool / 60)
fuel_opmode = fleet * shift_hrs * fuel_burn * op_days * diesel * opmode
fuel_total = fuel_precool + fuel_opmode

rej_total = rej_loads * rej_cost * (rej_rate / 100) * 12

prob_total = prob_drv * prob_stp * (prob_min / 60) * prob_hr * prob_days * (prob_elim / 100)

fa_total = fa_alerts * (fa_rate / 100) * (fa_min / 60) * fa_hr * fa_days * (fa_red / 100)

gross = fuel_total + rej_total + prob_total + fa_total
investment = fleet * eroad_cost * 12
net = gross - investment
roi = gross / investment if investment > 0 else 0
payback = (investment / gross * 12) if gross > 0 else 0


# ─── Dashboard ───
st.divider()

# Summary metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Annual Value", fmt(gross))
col2.metric("Net Value (after EROAD)", fmt(net))
col3.metric("ROI", f"{roi:.1f}x")
col4.metric("Payback", f"{payback:.1f} months")

st.divider()

# Value drivers with drill-down
st.subheader("Value Drivers")

# 1. Fuel
c1, c2 = st.columns([3, 1])
c1.markdown("**Fuel Optimization** — Pre-cool time reduction + operating mode efficiency")
c2.markdown(f"<div style='text-align:right; font-family:JetBrains Mono,monospace; font-size:1.3rem; font-weight:700; color:#1a8c3f;'>{fmt(fuel_total)}</div>", unsafe_allow_html=True)
with st.expander("Show calculation"):
    st.markdown(f"""
**Pre-Cool Savings**
- `{fleet:,} trucks` x `{fuel_burn} gal/hr` x `{op_days} days` x `${diesel:.2f}/gal` x `{precool} min / 60`
- = **{fmt(fuel_precool)}** /year

**Operating Mode Savings**
- `{fleet:,} trucks` x `{shift_hrs} hrs/day` x `{fuel_burn} gal/hr` x `{op_days} days` x `${diesel:.2f}/gal` x `{opmode:.2f} gal/hr reduction`
- = **{fmt(fuel_opmode)}** /year

**Combined: {fmt(fuel_total)}**
""")

# 2. Rejected Loads
c1, c2 = st.columns([3, 1])
c1.markdown("**Rejected Load Prevention** — CoreTemp product temp prediction reduces rejections")
c2.markdown(f"<div style='text-align:right; font-family:JetBrains Mono,monospace; font-size:1.3rem; font-weight:700; color:#1a8c3f;'>{fmt(rej_total)}</div>", unsafe_allow_html=True)
with st.expander("Show calculation"):
    st.markdown(f"""
- `{rej_loads} rejected loads/mo` x `${rej_cost:,}/load` x `{rej_rate}% reduction` x `12 months`
- = **{fmt(rej_total)}** /year
""")

# 3. Probing
c1, c2 = st.columns([3, 1])
c1.markdown("**Manual Probing Elimination** — CoreTemp replaces handheld thermometer probing")
c2.markdown(f"<div style='text-align:right; font-family:JetBrains Mono,monospace; font-size:1.3rem; font-weight:700; color:#1a8c3f;'>{fmt(prob_total)}</div>", unsafe_allow_html=True)
with st.expander("Show calculation"):
    st.markdown(f"""
- `{prob_drv:,} drivers` x `{prob_stp} stops/day` x `{prob_min:.1f} min/stop / 60` x `${prob_hr}/hr` x `{prob_days} days` x `{prob_elim}% elimination`
- = **{fmt(prob_total)}** /year
""")

# 4. False Alarms
c1, c2 = st.columns([3, 1])
c1.markdown("**False Alarm Reduction** — CoreTemp vs. Orbcomm return-air-only monitoring")
c2.markdown(f"<div style='text-align:right; font-family:JetBrains Mono,monospace; font-size:1.3rem; font-weight:700; color:#1a8c3f;'>{fmt(fa_total)}</div>", unsafe_allow_html=True)
with st.expander("Show calculation"):
    st.markdown(f"""
- `{fa_alerts:,} alerts/day` x `{fa_rate}% false` x `{fa_min:.1f} min/alert / 60` x `${fa_hr}/hr` x `{fa_days} days` x `{fa_red}% reduction`
- = **{fmt(fa_total)}** /year
""")

st.divider()

# Investment
st.markdown(f"""
**EROAD Investment:** `{fleet:,} units` x `${eroad_cost}/mo` x `12 months` = **{fmt(investment)}** /year
""")

st.divider()

# Orbcomm context
with st.expander("Why these savings exist — Orbcomm displacement context"):
    st.markdown("""
**Current state:** DG uses Orbcomm for return-air-only temperature monitoring.

**The problem:** Return air spikes 15-20°F every time a door opens, but actual product temperature stays stable
(thermal mass). This creates hundreds of false alerts daily. FSQA teams learn to ignore them. Then a real
excursion gets missed.

**CoreTemp difference:** Predicts actual product core temperature using AI + thermal mass modeling.
Monitors what matters — the product, not the air. Eliminates false alerts while catching real excursions.

**Cost of inaction:** July 2025 FDA Class II recall at Dollar General stores. Temperature monitoring
failures lead to regulatory action, brand damage, and liability exposure.
""")

# Sources
with st.expander("Sources & notes"):
    st.markdown("""
- Fleet size: DG public filings — ~8,075 total trailers, est 800–1,500 refrigerated
- Fuel burn: 1 gal/hr standard reefer unit (Carrier / Thermo King specs)
- Diesel: EIA weekly retail on-highway, Q1 2026
- Rejected loads: $5k–$12k/incident (USDA/FDA cold chain benchmarks, IARW industry data)
- Probing: IRTA benchmarks, Golden State Foods ($600k/yr), QCD, E.A. Sween case studies
- False alarms: 70-90% false positive rate from return-air-only systems in multi-stop delivery
- FDA recall: FDA Enforcement Reports, July 2025
- EROAD pricing: placeholder — **confirm with Travis**
- All figures are estimates for discovery discussion. Formal proposal uses validated DG inputs.
""")

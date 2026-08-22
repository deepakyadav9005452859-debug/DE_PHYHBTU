# DE_PHYHBTU
import streamlit as st
import math

# ---------------------------------------------------------
# Magnetic SI ↔ CGS Unit Converter
# Based on the conversion table provided by the user
# ---------------------------------------------------------

st.set_page_config(
    page_title="Magnetic Unit Converter",
    page_icon="🧲",
    layout="centered"
)

st.title("🧲 Magnetic Unit Converter")
st.write("Convert magnetic quantities between SI and CGS units.")

# ---------------------------------------------------------
# Conversion data
#
# factor = CGS value / SI value
#
# Example:
# 1 Tesla = 10^4 Gauss
# factor = 10^4
# ---------------------------------------------------------

quantities = { "Magnetic induction (B)": {
        "symbol": "B",
        "si": "tesla (T)",
        "cgs": "gauss (G)",
        "factor": 1e4
    },

    "Magnetic field (H)": {
        "symbol": "H",
        "si": "A m⁻¹",
        "cgs": "oersted (Oe)",
        "factor": 4 * math.pi * 1e-3
    },
    "Magnetic induction (B)": {
        "symbol": "B",
        "si": "tesla (T)",
        "cgs": "gauss (G)",
        "factor": 1e4
    },

    "Magnetic field (H)": {
        "symbol": "H",
        "si": "A m⁻¹",
        "cgs": "oersted (Oe)",
        "factor": 4 * math.pi * 1e-3
    },

    "Magnetization (M)": {
        "symbol": "M",
        "si": "A m⁻¹",
        "cgs": "emu cm⁻³",
        "factor": 1e-3
    },

    "Magnetic polarization (J)": {
        "symbol": "J",
        "si": "tesla (T)",
        "cgs": "emu cm⁻³",
        "factor": 1e4 / (4 * math.pi)
    },

    "Magnetic moment (m)": {
        "symbol": "m",
        "si": "A m²",
        "cgs": "emu",
        "factor": 1e3
    },

    "Magnetic moment per unit mass (σ)": {
        "symbol": "σ",
        "si": "A m² kg⁻¹",
        "cgs": "emu g⁻¹",
        "factor": 1
    },

    "Volume magnetic susceptibility (κ)": {
        "symbol": "κ",
        "si": "dimensionless",
        "cgs": "dimensionless",
        "factor": 1 / (4 * math.pi)
    },

    "Mass magnetic susceptibility (χ)": {
        "symbol": "χ",
        "si": "m³ kg⁻¹",
        "cgs": "emu Oe⁻¹ g⁻¹",
        "factor": 1e3 / (4 * math.pi)
    },

    "Molar magnetic susceptibility (χm)": {
        "symbol": "χm",
        "si": "m³ mol⁻¹",
        "cgs": "emu Oe⁻¹ g⁻¹ mol⁻¹",
        "factor": 1e6 / (4 * math.pi)
    },

    "Magnetic permeability (μ)": {
        "symbol": "μ",
        "si": "H m⁻¹",
        "cgs": "G Oe⁻¹",
        "factor": 1e7 / (4 * math.pi)
    },

    "Magnetic flux (Φ)": {
        "symbol": "Φ",
        "si": "weber (Wb)",
        "cgs": "maxwell (Mx)",
        "factor": 1e8
    },

    "Magnetic scalar potential / Magnetomotive force (φ)": {
        "symbol": "φ",
        "si": "ampere (A)",
        "cgs": "gilbert",
        "factor": 4 * math.pi / 10
    },

    "Magnetic vector potential (A)": {
        "symbol": "A",
        "si": "Wb m⁻¹",
        "cgs": "emu = G cm",
        "factor": 1e6
    },

    "Magnetic pole strength (p)": {
        "symbol": "p",
        "si": "A m",
        "cgs": "emu = G cm²",
        "factor": 10
    },

    "Demagnetizing factor (N)": {
        "symbol": "N",
        "si": "dimensionless",
        "cgs": "dimensionless",
        "factor": 4 * math.pi
    },

    "Magnetostriction constant (λ)": {
        "symbol": "λ",
        "si": "dimensionless",
        "cgs": "dimensionless",
        "factor": 1
    },

    "Anisotropy constant (K)": {
        "symbol": "K",
        "si": "J m⁻³",
        "cgs": "erg cm⁻³",
        "factor": 10
    },
    "Magnetostatic energy (Em)": {
        "symbol": "Em",
        "si": "J m⁻³",
        "cgs": "erg cm⁻³",
        "factor": 10
    },

    "Energy product (BH)max": {
        "symbol": "(BH)max",
        "si": "J m⁻³",
        "cgs": "erg cm⁻³",
        "factor": 10
    },
    "Magnetostatic energy (Em)": {
        "symbol": "Em",
        "si": "J m⁻³",
        "cgs": "erg cm⁻³",
        "factor": 10
    },

    "Energy product (BH)max": {
        "symbol": "(BH)max",
        "si": "J m⁻³",
        "cgs": "erg cm⁻³",
        "factor": 10
    }

}

# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------

st.sidebar.header("⚙️ Settings")

quantity_name = st.sidebar.selectbox(
    "Select Physical Quantity",
    list(quantities.keys())
)

direction = st.sidebar.radio(
    "Conversion Direction",
    [
        "SI → CGS",
        "CGS → SI"
    ]
)

data = quantities[quantity_name]

# ---------------------------------------------------------
# Main interface
# ---------------------------------------------------------

st.subheader(f"{data['symbol']} — {quantity_name}")

col1, col2 = st.columns(2)

with col1:
    value = st.number_input(
        f"Enter value in {'SI' if direction == 'SI → CGS' else 'CGS'}",
        value=1.0,
        format="%.10g"
    )

with col2:
    st.write("")

    if direction == "SI → CGS":
        st.info(
            f"SI Unit\n\n**{data['si']}**"
        )
    else:
        st.info(
            f"CGS Unit\n\n**{data['cgs']}**"
        )

# ---------------------------------------------------------
# Conversion
# ---------------------------------------------------------

if direction == "SI → CGS":

    result = value * data["factor"]

    st.success("### Conversion Result")

    st.metric(
        label=f"{data['cgs']}",
        value=f"{result:.10g}"
    )

    st.write(
        f"**{value:g} {data['si']} = {result:.10g} {data['cgs']}**"
    )

else:

    result = value / data["factor"]

    st.success("### Conversion Result")

    st.metric(
        label=f"{data['si']}",
        value=f"{result:.10g}"
    )

    st.write(
        f"**{value:g} {data['cgs']} = {result:.10g} {data['si']}**"
    )

# ---------------------------------------------------------
# Formula
# ---------------------------------------------------------

st.divider()

st.subheader("📐 Conversion Formula")

if direction == "SI → CGS":
    st.code(
        f"CGS = SI × {data['factor']:.10g}"
    )
else:
    st.code(
        f"SI = CGS ÷ {data['factor']:.10g}"
    )

# ---------------------------------------------------------
# Reference information
# ---------------------------------------------------------

with st.expander("ℹ️ Unit Information"):
    st.write(f"**Quantity:** {quantity_name}")
    st.write(f"**Symbol:** {data['symbol']}")
    st.write(f"**SI Unit:** {data['si']}")
    st.write(f"**CGS Unit:** {data['cgs']}")
    st.write(f"**SI → CGS factor:** {data['factor']:.10g}")

# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

st.divider()

st.caption(
    "Magnetic SI ↔ CGS Converter | Built with Python + Streamlit"
)

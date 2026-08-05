# packages
# Run with: py -m streamlit run laser_database_app_working.py
import base64
import hashlib
import os
import subprocess
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from streamlit.runtime.scriptrunner import get_script_run_ctx


# If this file is started with Python/VS Code Run, launch it correctly with Streamlit.
if get_script_run_ctx() is None:
    subprocess.run(
        [sys.executable, "-m", "streamlit", "run", os.path.abspath(__file__)],
        check=False,
    )
    raise SystemExit(0)


# --------------------------------------------------
# Streamlit background
# --------------------------------------------------
@st.cache_data
def get_base64_of_bin_file(bin_file):
    with open(bin_file, "rb") as file:
        data = file.read()
    return base64.b64encode(data).decode()


def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)

    page_bg_img = f"""
    <style>
    .stApp {{
        position: relative;
        background: black;
    }}

    .stApp::before {{
        content: "";
        position: fixed;
        inset: 0;
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: 30%;
        background-position: center;
        background-repeat: repeat;
        background-attachment: fixed;
        opacity: 0.15;
        z-index: 0;
        pointer-events: none;
    }}

    .stApp > * {{
        position: relative;
        z-index: 1;
    }}
    </style>
    """

    st.markdown(page_bg_img, unsafe_allow_html=True)


# Optional local background image beside this Python file.
BACKGROUND_FILE = Path(__file__).resolve().with_name("background.png")

if BACKGROUND_FILE.exists():
    set_png_as_page_bg(str(BACKGROUND_FILE))


# --------------------------------------------------
# Synthetic CSV dataset
# --------------------------------------------------
MAIN_TABLE = "databank"
DATA_FILE = Path(__file__).resolve().with_name(
    "synthetic_laser_databank.csv"
)


st.title("Laser Database Search")
st.caption("Search, filter and visualize synthetic laser experiment data.")


try:
    df = pd.read_csv(DATA_FILE, encoding="utf-8-sig")
except Exception as error:
    st.error("Could not load the synthetic dataset.")
    st.exception(error)
    st.stop()
    raise SystemExit(1)


# --------------------------------------------------
# Prepare the main dataset
# --------------------------------------------------
df = df.rename(
    columns={
        "Area-ID": "experiment_name",
        "Laser": "laserunite",
    }
)

df = df.drop(columns=["No"], errors="ignore")

comment_columns = [
    column
    for column in ["commproc", "commmeas"]
    if column in df.columns
]

if comment_columns:
    df["UserComment"] = (
        df[comment_columns]
        .fillna("")
        .astype(str)
        .agg(", ".join, axis=1)
        .str.strip(", ")
    )
    df = df.drop(columns=comment_columns)


# Create a stable source hash for each imported row.
df["unique ID"] = df.apply(
    lambda row: hashlib.sha256(
        "|".join(map(str, row.values)).encode("utf-8")
    ).hexdigest(),
    axis=1,
)


# --------------------------------------------------
# Prepared logical data groups
# Nothing is written to a database at this stage.
# --------------------------------------------------
entry_table = df[
    [
        "unique ID",
        "experiment_name",
        "Material",
        "laserunite",
        "UserComment",
    ]
]

laser_parameters = df[
    [
        "unique ID",
        "λ [nm]",
        "Pproc/Pout",
        "PL",
        "Pav_out [W]",
        "fB [MHz]",
        "fP [MHz]",
        "nP",
        "tP [ps]",
        "Polarization",
        "Compressor mode",
        "Compr. Pos. [um]",
    ]
]

scanner = df[
    [
        "unique ID",
        "Scanner",
        "f [mm]",
        "w0 [um]",
        "zr [um]",
    ]
]

scan_regime = df[
    [
        "unique ID",
        "Filling method",
        "lproc [mm]",
        "bproc [mm]",
        "v [m/s]",
        "z-z0 [um]",
        "Ldprim [um]",
        "Ldsec [um]",
        "nobject",
        "s [um]",
        "Offset [um]",
    ]
]

riblet_analysis = df[
    [
        "unique ID",
        "Measurement",
        "Measure-ID",
        "ASub_meas [mm²]",
        "AAdd_meas [mm²]",
        "sav [mm]",
        "sσ [mm]",
        "hav [mm]",
        "hσ [mm]",
        "ttop_av [mm]",
        "ttop_σ [mm]",
        "tmid_av [mm]",
        "tmid_σ [mm]",
        "tbottom_av [mm]",
        "tbottom_σ [mm]",
        "αav [°]",
        "ασ [°]",
        "β1_av [°]",
        "β1_σ [°]",
        "β2_av [°]",
        "β2_σ [°]",
        "(ref-max)av [mm]",
        "(ref-max)σ [mm]",
    ]
]

calculated_parameters = df[
    [
        "unique ID",
        "Pav_proc [W]",
        "w [um]",
        "tia [ns]",
        "Eia [uJ]",
        "Hia [J/cm²]",
        "DCB",
        "tB [ns]",
        "EB [uJ]",
        "HB [J/cm²]",
        "Bd [um]",
        "EP [uJ]",
        "HP [J/cm²]",
        "Pd [um]",
        "I0 [W/cm²]",
        "nscan",
        "ηfill",
        "Hav [kJ/cm²]",
        "Vmeas [mm³]",
        "DPO [um]",
        "SDR [nm∙cm²/J]",
        "SRR [um³/uJ]",
        "SRR [mm³/min/W]",
        "RV [mm³/min]",
        "RA [cm²/min]",
        "h/s",
        "t/s",
        "Dbottom [um]",
    ]
]

logical_groups = {
    "Entry information": entry_table,
    "Laser parameters": laser_parameters,
    "Scanner parameters": scanner,
    "Scan regime": scan_regime,
    "Riblet analysis": riblet_analysis,
    "Calculated parameters": calculated_parameters,
}

with st.expander("Preview prepared logical data groups"):
    selected_group = st.selectbox(
        "Choose a prepared data group",
        list(logical_groups.keys()),
    )
    st.dataframe(logical_groups[selected_group])


# --------------------------------------------------
# Parameter descriptions
# --------------------------------------------------
descriptions = {
    "experiment_name": "An ID: a combination of date and grid-position on the sample (not unique).",
    "Material": "Sample material.",
    "laserunite": "Laser source.",
    "λ [nm]": "Laser wavelength.",
    "Pproc/Pout": "Laser power efficiency on the target (0..1).",
    "PL": "Power level 0..1.",
    "Pav_out [W]": "Laser power output.",
    "fB [MHz]": "Burst repetition rate.",
    "fP [MHz]": "Pulse repetition rate.",
    "nP": "Number of pulses per burst.",
    "tP [ps]": "Laser pulse duration.",
    "Polarization": "Laser polarization.",
    "Compressor mode": "Compressor mode for pulse duration.",
    "Compr. Pos. [um]": "Compressor position for pulse duration.",
    "Scanner": "Scanner module.",
    "f [mm]": "Scan focal length.",
    "w0 [um]": "Laser spot focal radius.",
    "zr [um]": "Rayleigh length.",
    "lproc [mm]": "Scan-object length.",
    "bproc [mm]": "Scan-object width.",
    "v [m/s]": "Scan speed.",
    "z-z0 [um]": "Focal offset to sample surface.",
    "Ldprim [um]": "Line distance primary.",
    "Ldsec [um]": "Line distance secondary.",
    "nobject": "Number of fills.",
    "s [um]": "Nominal riblet period.",
    "Offset [um]": "Laser-wall offset.",
    "Filling method": "Line filling: uni- or bidirectional.",
    "UserComment": "Process and measurement comments.",
    "lmeas [mm]": "Field size length of measurement.",
    "bmeas [mm]": "Field size width of measurement.",
    "Measurement": "Measurement system used to gather the microstructure.",
    "Measure-ID": "Name of the analyzed measurement (not unique).",
    "ASub_meas [mm²]": "Removed area from reference.",
    "AAdd_meas [mm²]": "Added area to reference.",
    "sav [mm]": "Average riblet distance.",
    "sσ [mm]": "Standard deviation of riblet distance.",
    "hav [mm]": "Average riblet height.",
    "hσ [mm]": "Standard deviation of riblet height.",
    "ttop_av [mm]": "Average riblet width at top.",
    "ttop_σ [mm]": "Standard deviation of riblet width at top.",
    "tmid_av [mm]": "Average riblet width at middle.",
    "tmid_σ [mm]": "Standard deviation of riblet width at middle.",
    "tbottom_av [mm]": "Average riblet width at bottom.",
    "tbottom_σ [mm]": "Standard deviation of riblet width at bottom.",
    "αav [°]": "Average riblet tip angle.",
    "ασ [°]": "Standard deviation of riblet tip angle.",
    "β1_av [°]": "Average left riblet flank angle.",
    "β1_σ [°]": "Standard deviation of left riblet flank angle.",
    "β2_av [°]": "Average right riblet flank angle.",
    "β2_σ [°]": "Standard deviation of right riblet flank angle.",
    "(ref-max)av [mm]": "Average distance from riblet tip to reference level.",
    "(ref-max)σ [mm]": "Standard deviation of distance from riblet tip to reference level.",
    "Pav_proc [W]": "Average laser power in process.",
    "w [um]": "Laser spot radius on surface.",
    "tia [ns]": "Exposure duration for a point (interaction time).",
    "Eia [uJ]": "Interaction energy.",
    "Hia [J/cm²]": "Interaction fluence.",
    "DCB": "Duty cycle burst.",
    "tB [ns]": "Burst duration.",
    "EB [uJ]": "Burst energy.",
    "HB [J/cm²]": "Burst fluence.",
    "Bd [um]": "Burst distance.",
    "EP [uJ]": "Pulse energy.",
    "HP [J/cm²]": "Pulse fluence.",
    "Pd [um]": "Pulse distance.",
    "I0 [W/cm²]": "Pulse intensity.",
    "nscan": "Number of scans.",
    "ηfill": "Area fill rate.",
    "Hav [kJ/cm²]": "Total energy per area.",
    "Vmeas [mm³]": "Removed volume in measure area.",
    "DPO [um]": "Removal depth per object.",
    "SDR [nm∙cm²/J]": "Specific removal depth rate.",
    "SRR [um³/uJ]": "Specific removal volume rate.",
    "SRR [mm³/min/W]": "Specific removal volume rate.",
    "RV [mm³/min]": "Removal volume rate.",
    "RA [cm²/min]": "Processed area rate.",
    "h/s": "Riblet aspect ratio.",
    "t/s": "Riblet aspect ratio 1.",
    "Dbottom [um]": "Riblet bottom level.",
}


# --------------------------------------------------
# Choose the available synthetic table
# --------------------------------------------------
tables = [MAIN_TABLE]

selected_table = st.selectbox(
    "Choose one table",
    tables,
)

selected_df = df.copy()

if selected_df.empty:
    st.warning("The selected table contains no data.")
    st.stop()

st.write(f"Selected table: **{selected_table}**")
st.write(f"Rows loaded: **{len(selected_df)}**")
st.dataframe(selected_df)


# Show descriptions only for columns that exist in the selected table.
available_descriptions = {
    column: description
    for column, description in descriptions.items()
    if column in selected_df.columns
}

if available_descriptions:
    selected_component = st.selectbox(
        "Select a component to see its description",
        list(available_descriptions.keys()),
    )
    st.info(available_descriptions[selected_component])


# --------------------------------------------------
# Convert suitable columns to numeric values
# --------------------------------------------------
numeric_df = selected_df.copy()

for column in numeric_df.columns:
    cleaned_values = (
        numeric_df[column]
        .astype(str)
        .str.replace(",", ".", regex=False)
        .str.strip()
    )

    converted_values = pd.to_numeric(
        cleaned_values,
        errors="coerce",
    )

    non_empty_values = (
        selected_df[column].notna()
        & selected_df[column].astype(str).str.strip().ne("")
    )

    if (
        non_empty_values.any()
        and converted_values[non_empty_values].notna().mean() >= 0.8
    ):
        numeric_df[column] = converted_values

numeric_columns = [
    column
    for column in numeric_df.select_dtypes(include="number").columns
    if numeric_df[column].notna().any()
]

if not numeric_columns:
    st.warning("No numeric columns were found in the selected table.")
    st.stop()


# --------------------------------------------------
# Filter and visualize data
# --------------------------------------------------
st.subheader("Filter and visualization")

filter_column = st.selectbox(
    "Select column for filtering",
    numeric_columns,
)

column_min = float(numeric_df[filter_column].min())
column_max = float(numeric_df[filter_column].max())

minimum_column, maximum_column = st.columns(2)

with minimum_column:
    min_value = st.number_input(
        f"Minimum {filter_column}",
        value=column_min,
    )

with maximum_column:
    max_value = st.number_input(
        f"Maximum {filter_column}",
        value=column_max,
    )

x_column = st.selectbox(
    "Select X axis",
    numeric_columns,
)

y_column = st.selectbox(
    "Select Y axis",
    numeric_columns,
    index=min(1, len(numeric_columns) - 1),
)

if st.button("Search"):
    if min_value > max_value:
        st.error("Minimum value cannot be greater than maximum value.")
        st.stop()

    filter_mask = numeric_df[filter_column].between(
        min_value,
        max_value,
        inclusive="both",
    )

    result = selected_df.loc[filter_mask].copy()
    plot_data = numeric_df.loc[
        filter_mask,
        [x_column, y_column],
    ].dropna()

    st.write(f"Number of rows: **{len(result)}**")
    st.dataframe(result)

    if result.empty:
        st.warning("No rows match the selected range.")
    elif plot_data.empty:
        st.warning(
            "No valid numeric data is available for the selected axes."
        )
    else:
        figure, axis = plt.subplots(figsize=(8, 5))

        axis.scatter(
            plot_data[x_column],
            plot_data[y_column],
        )

        axis.set_title(f"{y_column} versus {x_column}")
        axis.set_xlabel(x_column)
        axis.set_ylabel(y_column)
        axis.grid(True)

        figure.tight_layout()
        st.pyplot(figure)
        plt.close(figure)

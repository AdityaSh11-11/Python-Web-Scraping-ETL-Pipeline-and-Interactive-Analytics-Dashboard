import streamlit as st
import pandas as pd
import json
from io import BytesIO

from database import get_all_quotes
from utils.helper import dataframe

st.set_page_config(
    page_title="Export",
    page_icon="📁",
    layout="wide"
)

st.title("Export Data")

df = dataframe(get_all_quotes())

if df.empty:

    st.warning("Nothing to export.")

    st.stop()

st.success(f"{len(df)} records available")

st.dataframe(

    df.head(10),

    use_container_width=True

)

# ---------------------------------
# CSV
# ---------------------------------

csv = df.to_csv(

    index=False

).encode("utf-8")

st.download_button(

    label="Download CSV",

    data=csv,

    file_name="quotes.csv",

    mime="text/csv"

)

# ---------------------------------
# Excel
# ---------------------------------

excel_buffer = BytesIO()

with pd.ExcelWriter(

    excel_buffer,

    engine="openpyxl"

) as writer:

    df.to_excel(

        writer,

        index=False,

        sheet_name="Quotes"

    )

st.download_button(

    label="Download Excel",

    data=excel_buffer.getvalue(),

    file_name="quotes.xlsx",

    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

)

# ---------------------------------
# JSON
# ---------------------------------

json_data = json.dumps(

    df.to_dict(

        orient="records"

    ),

    indent=4

)

st.download_button(

    label="Download JSON",

    data=json_data,

    file_name="quotes.json",

    mime="application/json"

)

st.divider()

st.subheader("Dataset Summary")

st.write(f"Total Quotes : **{len(df)}**")

st.write(f"Unique Authors : **{df['Author'].nunique()}**")

st.write(
    f"Unique Tags : **{df['Tags'].str.split(',').explode().nunique()}**"
)

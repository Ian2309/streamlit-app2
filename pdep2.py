import streamlit as st
import pandas as pd

# --- Title ---
st.title("Linux Distribution Usage Trends (2000–2026)")
st.write("This Web-App shows percentage usage of major Linux distributions from 2000 to 2026")

# --- Sidebar: About Section ---
st.sidebar.header("About")
with st.sidebar.expander("Click here to know about this app"):
    st.markdown("""
    **What is the Web-App about?**  
    This app visualizes the **usage trends of major Linux distributions** from 2000 to 2026.  

    **Who is the target user?**  
    - Students learning Linux or data visualization  
    - Linux enthusiasts  
    - Teachers and researchers analyzing Linux usage

    **Inputs collected:**  
    - Selected Linux distribution from the sidebar dropdown

    **Outputs displayed:**  
    - Line chart of percentage usage trends  
    - Table of distribution usage in percentages  
    - Distribution info
    """)

# --- Dataset ---
data = {
    "Year": list(range(2000, 2027)),
    "Ubuntu": [0,0,0,0,5,10,15,20,25,28,30,32,34,35,36,38,39,40,41,42,43,44,45,46,47,48,49],
    "Debian": [20,21,22,23,23,24,25,26,27,27,28,28,29,29,30,30,31,31,32,32,33,33,34,34,35,35,36],
    "Fedora": [5,6,7,8,9,10,11,12,13,14,15,15,16,16,17,17,18,18,19,19,20,20,21,21,22,22,23],
    "Arch": [0,0,0,1,1,2,3,4,5,6,7,8,9,10,12,14,16,18,20,22,24,26,28,30,32,34,36],
    "Linux Mint": [0,0,0,0,0,3,6,9,12,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33]
}

df = pd.DataFrame(data)
df.set_index("Year", inplace=True)

# --- Convert to percentage ---
df_percent = df.div(df.sum(axis=1), axis=0) * 100
df_display = df_percent.copy()
df_display.index = df_display.index.astype(str)

# --- Sidebar: Inputs ---
st.sidebar.header("Filter Options")

# 1. Select Linux distribution
distro = st.sidebar.selectbox(
    "Select Linux Distribution",
    ["All", "Ubuntu", "Debian", "Fedora", "Arch", "Linux Mint"]
)

# 2. Select year range
year_min, year_max = st.sidebar.slider(
    "Select Year Range",
    min_value=2000,
    max_value=2026,
    value=(2000, 2026),
    step=1
)

# 3. Checkbox: Show data table
show_table = st.sidebar.checkbox("Show dataset table", value=True)

# 4. Radio: Choose chart type
chart_type = st.sidebar.radio(
    "Choose chart type",
    ["Line Chart", "Area Chart"]
)

# 5. Multiselect: Highlight distros
highlight_distros = st.sidebar.multiselect(
    "Highlight Distros (Optional)",
    ["Ubuntu", "Debian", "Fedora", "Arch", "Linux Mint"]
)

# --- Filter data by year ---
df_percent_filtered = df_percent.loc[year_min:year_max]

# --- Display Chart ---
st.subheader("📈 Percentage Usage Trend")
if chart_type == "Line Chart":
    if distro == "All":
        st.line_chart(df_percent_filtered)
    else:
        st.line_chart(df_percent_filtered[[distro]])
else:  # Area Chart
    if distro == "All":
        st.area_chart(df_percent_filtered)
    else:
        st.area_chart(df_percent_filtered[[distro]])

# --- Keep numeric index for slicing ---
df_display = df_percent.copy()  # index stays as int

# --- Display Table ---
if show_table:
    st.subheader("📊 Dataset in Percentage")
    if highlight_distros:
        st.dataframe(
            df_display.loc[year_min:year_max, highlight_distros]
            .round(2)
            .rename_axis(index=str)  # convert index to string for display only
        )
    else:
        st.dataframe(
            df_display.loc[year_min:year_max]
            .round(2)
            .rename_axis(index=str)
        )

# --- About Distros Section ---
st.subheader("About the Distributions")
st.markdown("""
- <span style='color:#ff4d00'><b>Ubuntu</b></span> - Beginner-friendly Linux distribution widely used for desktops and servers.
- <span style='color:#800080'><b>Debian</b></span> - One of the oldest and most stable Linux distributions.
- <span style='color:#800000'><b>Fedora</b></span> - Cutting-edge Linux distribution sponsored by Red Hat.
- <span style='color:#005b96'><b>Arch Linux</b></span> - Minimalist distribution known for customization and rolling releases.
- <span style='color:#00ff44'><b>Linux Mint</b></span> - Popular Ubuntu-based distro focused on ease of use and desktop stability.
""", unsafe_allow_html=True)

# --- Other UI components for demonstration ---
st.caption("!Data is estimated for educational purposes only.!")
st.caption("Christian Hebres - 2026")

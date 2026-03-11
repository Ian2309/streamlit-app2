import streamlit as st
import pandas as pd
import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Linux Distro Trends",
    page_icon="🐧",
    layout="wide"
)

# ---------------- LANDING PAGE ----------------
page = st.sidebar.radio("Navigate", ["Home", "Dashboard"])

if page == "Home":

    st.title("🐧 Linux Distribution Usage Trends App")

    st.image("https://upload.wikimedia.org/wikipedia/commons/a/af/Tux.png", width=150)

    st.markdown("""
    ### Welcome!

    This **Streamlit Web App** visualizes the **usage trends of major Linux distributions from 2000–2026**.

    It is designed for:
    - 🎓 Students learning Linux
    - 💻 Linux enthusiasts
    - 📊 Researchers studying open-source adoption

    Use the **Dashboard** page to explore interactive charts and datasets.
    """)

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Distros", "5")
    col2.metric("Years Covered", "27")
    col3.metric("Data Type", "Usage %")

    st.progress(60)

    if st.button("Enter Dashboard"):
        st.toast("Opening Dashboard 🚀")

    st.info("Use the sidebar to navigate to the dashboard.")

# ---------------- DATASET ----------------
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

df_percent = df.div(df.sum(axis=1), axis=0) * 100

# ---------------- DASHBOARD ----------------
if page == "Dashboard":

    st.title("📊 Linux Distribution Usage Trends (2000–2026)")

    # Sidebar inputs
    st.sidebar.header("Filter Options")

    distro = st.sidebar.selectbox(
        "Select Linux Distribution",
        ["All", "Ubuntu", "Debian", "Fedora", "Arch", "Linux Mint"]
    )

    year_range = st.sidebar.select_slider(
        "Select Year Range",
        options=list(range(2000, 2027)),
        value=(2000, 2026)
    )

    chart_type = st.sidebar.radio(
        "Chart Type",
        ["Line Chart", "Area Chart"]
    )

    highlight = st.sidebar.multiselect(
        "Highlight Distros",
        ["Ubuntu", "Debian", "Fedora", "Arch", "Linux Mint"]
    )

    show_table = st.sidebar.toggle("Show Dataset Table", True)

    theme_color = st.sidebar.color_picker("Pick Chart Color", "#ff4d00")

    rows_to_show = st.sidebar.number_input(
        "Rows to Display",
        min_value=5,
        max_value=27,
        value=10
    )

    selected_date = st.sidebar.date_input(
        "Select analysis date",
        datetime.date.today()
    )

    # Filter data
    df_filtered = df_percent.loc[year_range[0]:year_range[1]]

    # ---------------- TABS ----------------
    tab1, tab2, tab3 = st.tabs(["📈 Chart", "📄 Data", "ℹ️ Info"])

    # ----- CHART TAB -----
    with tab1:

        st.subheader("Usage Trend")

        col1, col2 = st.columns(2)

        col1.metric("Start Year", year_range[0])
        col2.metric("End Year", year_range[1])

        if chart_type == "Line Chart":
            if distro == "All":
                st.line_chart(df_filtered)
            else:
                st.line_chart(df_filtered[[distro]])
        else:
            if distro == "All":
                st.area_chart(df_filtered)
            else:
                st.area_chart(df_filtered[[distro]])

        st.success("Chart updated successfully!")

    # ----- DATA TAB -----
    with tab2:

        st.subheader("Dataset")

        df_display = df_percent.copy()

        if highlight:
            st.dataframe(
                df_display.loc[year_range[0]:year_range[1], highlight]
                .round(2)
                .head(rows_to_show)
            )
        else:
            st.dataframe(
                df_display.loc[year_range[0]:year_range[1]]
                .round(2)
                .head(rows_to_show)
            )

        csv = df_display.to_csv().encode("utf-8")

        st.download_button(
            "Download Dataset CSV",
            csv,
            "linux_distro_data.csv",
            "text/csv"
        )

    # ----- INFO TAB -----
    with tab3:

        with st.expander("About the Distributions"):

            st.markdown("""
            **Ubuntu** – Beginner-friendly Linux distribution widely used for desktops and servers.

            **Debian** – One of the oldest and most stable Linux distributions.

            **Fedora** – Cutting-edge Linux distribution sponsored by Red Hat.

            **Arch Linux** – Minimalist distro known for customization and rolling releases.

            **Linux Mint** – Popular Ubuntu-based distro focused on ease of use.
            """)

        st.warning("Data is estimated for educational purposes only.")

        st.caption("Christian Hebres - (c)2026")
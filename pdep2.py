import streamlit as st
import pandas as pd
import datetime

st.set_page_config(
    page_title="Linux Distro Trends",
    page_icon="🐧",
    layout="wide"
)

page = st.sidebar.radio("Navigation", ["Home", "Dashboard"])

#dataset
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

if page == "Home":

    st.title("Linux Distribution Usage Trends")

    st.markdown("""
    ### Explore Linux popularity from **2000 to 2026**

    This interactive web application visualizes how major Linux distributions
    have evolved in popularity over time.""")

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/3/35/Tux.svg",
        width=200
    )

    st.divider()

    st.subheader("Project Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Linux Distros", "5")
    col2.metric("Years Analyzed", "27")
    col3.metric("Data Points", "135+")
    col4.metric("Interactive Charts", "2")

    st.divider()

    st.subheader("Features")

    f1, f2, f3 = st.columns(3)

    with f1:
        st.info("""
        📈 **Interactive Charts**

        View Linux distribution usage trends
        using line charts or area charts.
        """)

    with f2:
        st.success("""
        🔍 **Custom Filters**

        Select distributions and choose
        specific year ranges to analyze.
        """)

    st.divider()

    st.subheader("About the Distributions")

    st.markdown("""
    **Ubuntu** - Beginner-friendly Linux distribution widely used for desktops and servers.

    **Debian** - One of the oldest and most stable Linux distributions.

    **Fedora** - Cutting-edge Linux distribution sponsored by Red Hat.

    **Arch Linux** - Minimalist distro known for customization and rolling releases.

    **Linux Mint** - Ubuntu-based distro focused on ease of use and stability.
    """)

    st.warning("Data is estimated for educational purposes only.")

    st.caption("Christian Hebres - Streamlit Project (2026)")

if page == "Dashboard":

    st.title("📊 Linux Distribution Usage Trends (2000-2026)")

    #sidebar components
    st.sidebar.subheader("Filter Options")

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

    selected_date = st.sidebar.date_input(
        "Select analysis date",
        datetime.date.today()
    )

    df_filtered = df_percent.loc[year_range[0]:year_range[1]]

    #3 tabs
    tab1, tab2, tab3 = st.tabs(["📈 Chart", "📄 Data", "ℹ️ Info"])

    with tab1:
        st.subheader("Usage Trend")

        c1, c2 = st.columns(2)
        c1.metric("Start Year", year_range[0])
        c2.metric("End Year", year_range[1])

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

    with tab2:
        st.subheader("Dataset")

        df_display = df_percent.copy()

        selected_distros = st.multiselect(
            "Select Linux Distributions to Display",
            options=["Ubuntu", "Debian", "Fedora", "Arch", "Linux Mint"],
            default=["Ubuntu", "Debian", "Fedora", "Arch", "Linux Mint"]
        )

        if selected_distros:
            st.dataframe(
                df_display.loc[year_range[0]:year_range[1], selected_distros].round(2)
            )
        else:
            st.dataframe(
                df_display.loc[year_range[0]:year_range[1]].round(2)
            )

        csv = df_display.to_csv().encode("utf-8")
        st.download_button(
            "Download Dataset CSV",
            csv,
            "linux_distro_data.csv",
            "text/csv"
        )
        
    with tab3:
        st.markdown("""This is the breakdown of Streamlit API Documentation used in my WEBAPP

| #  | Component Names            | Description                        |

| 1  | `st.set_page_config`       | Sets page title, icon, layout      |
| 2  | `st.sidebar.radio`         | Navigation or chart type selection |
| 3  | `st.sidebar.selectbox`     | Select Linux distribution          |
| 4  | `st.sidebar.select_slider` | Year range filter                  |
| 5  | `st.sidebar.date_input`    | Analysis date picker               |
| 6  | `st.sidebar.subheader`     | Filter options header              |
| 7  | `st.title`                 | Page titles                        |
| 8  | `st.subheader`             | Section or tab headers             |
| 9  | `st.markdown`              | Text content / descriptions        |
| 10 | `st.image`                 | Display images                     |
| 11 | `st.divider`               | Divider line                       |
| 12 | `st.columns`               | Layout columns                     |
| 13 | `st.metric`                | Metrics display (numeric stats)    |
| 14 | `st.info`                  | Info card / feature highlight      |
| 15 | `st.success`               | Success card / messages            |
| 16 | `st.warning`               | Warning / disclaimer               |
| 17 | `st.caption`               | Footer / author info               |
| 18 | `st.tabs`                  | Tabs for Chart / Data / Info       |
| 19 | `st.line_chart`            | Line chart visualization           |
| 20 | `st.area_chart`            | Area chart visualization           |
| 21 | `st.dataframe`             | Display DataFrame                  |
| 22 | `st.download_button`       | Download CSV button                |

Streamlit Project (CHRISTIAN B. HEBRES) 2026
""")
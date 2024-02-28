import streamlit as st
import streamlit.components.v1 as stc
import pickle
import joblib
import pandas as pd
import numpy as np
import altair as alt

# with open('./data/final_model.pkl','rb') as file:
#     Final_Model = pickle.load(file)

def main():
    # stc.html(html_temp)
    # st.title("House Price Prediction App")
    st.markdown("""
            <p style="font-size: 44px; color: #023047;font-weight: bold">House Price Prediction App</p>
            """, unsafe_allow_html=True)
    st.markdown("This application was created for the Capstone Project Tetris Batch 4 from DQLab")

    with st.sidebar:
        st.image("house_price.jpg")

        menu = ["Overview"]
        choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Overview":
        st.header("Overview")
        st.markdown("This is a dashboard for analyzing the prices of houses sold in the Jakarta, Bogor, Depok, Tangerang, Bekasi and South Tangerang areas.")

        st.markdown("""
            <p style="font-size: 16px; font-weight: bold">Dataset Overview</p>
            """, unsafe_allow_html=True)

        url = "https://raw.githubusercontent.com/ekobw/house_price_prediction/main/data/clean_house_price.csv"
        df = pd.read_csv(url)
        top_10_rows = df.head(10)
        st.table(top_10_rows)

        text1 = """

                - This dataset consists of a total of 7,252 rows (entries) and contains 5 columns of variable.
                - The dataset contains house information data from 6 regions, namely **Jakarta**, **Bogor**, **Depok**, **Tangerang**, **Bekasi** and **Tangerang Selatan**.
                - The independent variables consist of **kamar_tidur**, **luas_bangunan_m2**, **luas_tanah_m2**, and **lokasi** which contain information about the house specifications.
                - The dependent variable is **harga**, which informs the selling price of the house.

                Features:

                - **kamar_tidur** : Number of bedrooms
                - **luas_bangunan_m2** : Building area of the house in square meters
                - **luas_tanah_m2** : Land area of the house in square meters
                - **kota** : Name of the city where the house is being sold
                - **harga** : The price of the house being sold
                """

        text2 = """
                From the histogram chart above, we can see that the graph is right-skewed. \
                This means that the range of data values is quite wide, but the data distribution is not evenly distributed. \
                Most of the data has a low value, meaning that the most sold houses have specifications and prices that are still quite affordable.
                """

        text3 = """
                From the bar chart above, we can see that the number of houses being sold for each region is more or less the same. \
                Likewise for the Jakarta area, if it is accumulated, the total is around 1300 houses for sale for the entire Jakarta area.
                """

        text4 = """
                From the bar chart above, we can see that the average price of houses sold in the Jakarta area is higher than in areas outside Jakarta. \
                Almost all areas of Jakarta are in the top position, except East Jakarta which is below South Tangerang. \
                This may occur due to the unequal amount of data in the two cities, where data for the East Jakarta area is less than for South Tangerang area.
                """

        text5 = """
                Correlation Matrix shows that luas_bangunan_m2 and luas_tanah_m2 variables have a stronger relationship than the kamar_tidur variable. \
                It can be concluded that houses that have a larger building area or land area tend to have higher prices than houses that have many bedrooms.
                """

        st.markdown("""
            <p style="font-size: 16px; font-weight: bold">Dataset Description</p>
            """, unsafe_allow_html=True)

        st.markdown(text1)

        # Display the chart title
        st.title("Distribution of Data")

        # Create Altair chart
        chart = alt.Chart(df).mark_bar().encode(
            x=alt.X('values:Q', bin=True),
            y='count()'
        ).properties(
            width=500,
            height=300
        )

        # Add labels and title separately below the chart
        st.altair_chart(chart)

        st.markdown(text2)


        # Display the chart title and explanation
        st.title("Number of Houses for Sale per City")
        st.write("This chart visualizes the distribution of houses across different cities.")

        # Sort and filter data for better visualization (optional)
        value_counts = df['kota'].value_counts().sort_values(ascending=True)

        # # Create the bar chart within a Streamlit container
        with st.container():
            plt.figure(figsize=(8, 6))
            bars1 = plt.barh(value_counts.index, value_counts, color='skyblue')
            plt.title('Number of Houses for Sale per City')
            plt.ylabel('City')
            plt.xlabel('Number of Houses')

            # Add labels to bars
            plt.bar_label(bars1, fontsize=10)

            plt.tight_layout()
            st.pyplot(plt)

        st.markdown(text3)


        # Display the chart title and explanation
        st.title("Average House Price per City")
        st.write("This chart visualizes the average sale price of houses across different cities.")

        # Sort and filter data for better presentation (optional)
        mean_prices = df.groupby('kota')['harga'].mean().sort_values(ascending=True)

        # Create the bar chart within a Streamlit container
        with st.container():
            plt.figure(figsize=(8, 6))
            bars2 = plt.barh(mean_prices.index, mean_prices, color='lightgreen')
            plt.title('Average House Price per City')
            plt.ylabel('City')
            plt.xlabel('Average Price')

            # Add labels to bars
            plt.bar_label(bars2, fontsize=10)

            plt.tight_layout()
            st.pyplot(plt)

        st.markdown(text4)


        # Display the chart title
        st.title("Correlation Matrix of Numeric Variables")

        # Filter out columns with object data type
        numeric_df = df.select_dtypes(include=['float64', 'int64'])

        # Calculate correlation matrix
        correlation_matrix = numeric_df.corr()

        # Create a new figure and axis
        fig, ax = plt.subplots(figsize=(8, 6))

        # Create heatmap
        sns.heatmap(correlation_matrix, annot=True, linewidths=0.5, ax=ax)
        ax.set_title('Correlation Matrix of Numeric Variables')

        # Display heatmap
        st.pyplot(fig)

        st.markdown(text5)


if __name__ == "__main__":
    main()
import streamlit as st
import pandas as pd
import duckdb
import io

csv1 = '''
    beverage,price
    orange juice,2.5
    Expresso,2
    Tea,3
'''
beverages = pd.read_csv(io.StringIO(csv1))

csv2 = '''
    food_item,food_price
    cookie,2.5
    chocolatine,2
    muffin,3
'''
food_items = pd.read_csv(io.StringIO(csv2))

answer_str = """
    SELECT * FROM beverages
    CROSS JOIN food_items
"""
solution_df = duckdb.sql(answer_str).df()

st.write("Spaced Repetition System SQL practice")
with st.sidebar:
    option = st.selectbox(
        "What would you like to review ?",
        ("Join", "Group By", "Windows Functions"),
        index=None,
        placeholder="Select a theme...",
    )
    st.write("You selected:", option)

st.header ("enter your code:")
query = st.text_area (label="Votre code SQL ici", key="user _input")
if query:
    result = duckdb.sql(query) .df()
    st. dataframe(result)

    if len(result.columns) != len(
        solution_df.columns
    ): # replace with try result = result[solution.columns]
        st.write("Some columns are missing")

    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError as e:
        st.write("Some columns are missing")
    n_lines_difference = result.shape[0] - solution_df.shape[0]
    if n_lines_difference != 0:
        st.write(
            f"result has a {n_lines_difference} lines difference with the solution"
        )

tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:
    st.write("table: beverages")
    st.dataframe (beverages)
    st.write("table: food_items")
    st.dataframe(food_items)
    st.write("expected:")
    st.dataframe(solution_df)

with tab3:
    st.write(answer_str)
import streamlit as st

def main():
    st.title("Simple Streamlit App")
    st.write("Welcome to this Streamlit app!")

    # Add some interactive elements
    name = st.text_input("Enter your name:", "Your Name")
    age = st.slider("Select your age:", 1, 100, 25)

    # Display the user's input
    st.write(f"Hello, {name}! You are {age} years old.")

    # Display an image
    st.image("https://www.streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png",
             caption="Streamlit Logo", use_column_width=True)

    # Add a chart
    chart_data = {'x': [1, 2, 3, 4, 5],
                  'y': [10, 20, 30, 40, 50]}
    st.line_chart(chart_data)

if __name__ == "__main__":
    main()

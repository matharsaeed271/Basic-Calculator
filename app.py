import streamlit as st

st.set_page_config(page_title="Calculator", layout="centered")

# Button layout like your tkinter version
button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]


# Session state setup
if "display" not in st.session_state:
    st.session_state.display = "0"

if "A" not in st.session_state:
    st.session_state.A = None

if "operator" not in st.session_state:
    st.session_state.operator = None


def clear_all():
    st.session_state.display = "0"
    st.session_state.A = None
    st.session_state.operator = None


def remove_zero_decimal(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)


def button_clicked(value):
    display = st.session_state.display

    # Right-side operators
    if value in right_symbols:

        if value == "=":
            if st.session_state.A is not None and st.session_state.operator is not None:
                B = float(display)
                A = float(st.session_state.A)

                if st.session_state.operator == "+":
                    result = A + B
                elif st.session_state.operator == "-":
                    result = A - B
                elif st.session_state.operator == "×":
                    result = A * B
                elif st.session_state.operator == "÷":
                    if B != 0:
                        result = A / B
                    else:
                        st.session_state.display = "Error"
                        st.session_state.A = None
                        st.session_state.operator = None
                        return

                st.session_state.display = remove_zero_decimal(result)
                st.session_state.A = None
                st.session_state.operator = None

        elif value in ["+", "-", "×", "÷"]:
            st.session_state.A = display
            st.session_state.operator = value
            st.session_state.display = "0"

    # Top symbols
    elif value in top_symbols:

        if value == "AC":
            clear_all()

        elif value == "+/-":
            result = float(display) * -1
            st.session_state.display = remove_zero_decimal(result)

        elif value == "%":
            result = float(display) / 100
            st.session_state.display = remove_zero_decimal(result)

    # Square root
    elif value == "√":
        num = float(display)
        if num >= 0:
            st.session_state.display = remove_zero_decimal(num ** 0.5)
        else:
            st.session_state.display = "Error"

    # Numbers and decimal
    else:
        if value == ".":
            if "." not in display:
                st.session_state.display += "."

        elif value in "0123456789":
            if display == "0":
                st.session_state.display = value
            else:
                st.session_state.display += value


# Title
st.title("Calculator")

# Display
st.markdown(
    f"""
    <div style="
        background-color: black;
        color: white;
        padding: 20px;
        font-size: 40px;
        text-align: right;
        border-radius: 10px;
        margin-bottom: 20px;
    ">
        {st.session_state.display}
    </div>
    """,
    unsafe_allow_html=True
)

# Buttons layout
for row in button_values:
    cols = st.columns(4)

    for i, value in enumerate(row):
        with cols[i]:
            if st.button(value, use_container_width=True):
                button_clicked(value)
                st.rerun()

st.write("\n" * 15)
# Add a bold line above the footer
st.markdown("<hr style='border: 2px solid black;'>", unsafe_allow_html=True)
# Footer content
st.write("Copy© 2026 M.Athar | Made With Muhammad Athar Ur Rahman")

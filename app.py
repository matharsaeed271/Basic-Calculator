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

#########################################################################################################
### Now, Its for Window operating system, not deployning., because GUI implemnent on this code


# import tkinter
# import streamlit as st
# button_values = [
#     ["AC", "+/-", "%", "÷"],
#     ["7", "8", "9", "×"],
#     ["4", "5", "6", "-"],
#     ["1", "2", "3", "+"],
#     ["0", ".", "√", "="]
# ]

# right_symbols = ["÷", "×", "-", "+", "="]
# top_symbols = ["AC", "+/-", "%"]

# row_count = len(button_values)  # 5
# column_count = len(button_values[0])  # 4

# color_light_gray = "#D4D4D2"
# color_black = "#1C1C1C"
# color_dark_gray = "#505050"
# color_orange = "#FF9500"
# color_white = "white"

# # window setup
# window = tkinter.Tk()  # create the window
# window.title("Calculator")
# window.resizable(False, False)

# frame = tkinter.Frame(window)
# label = tkinter.Label(frame, text="0", font=("Arial", 45), background=color_black,
#                       foreground=color_white, anchor="e", width=column_count)

# label.grid(row=0, column=0, columnspan=column_count, sticky="we")

# for row in range(row_count):
#     for column in range(column_count):
#         value = button_values[row][column]
#         button = tkinter.Button(frame, text=value, font=("Arial", 30),
#                                 width=column_count - 1, height=1,
#                                 command=lambda value=value: button_clicked(value))

#         if value in top_symbols:
#             button.config(foreground=color_black, background=color_light_gray)
#         elif value in right_symbols:
#             button.config(foreground=color_white, background=color_orange)
#         else:
#             button.config(foreground=color_white, background=color_dark_gray)

#         button.grid(row=row + 1, column=column)

# frame.pack()

# # A+B, A-B, A*B, A/B
# A = "0"
# operator = None
# B = None


# def clear_all():
#     global A, B, operator
#     A = "0"
#     operator = None
#     B = None


# def remove_zero_decimal(num):
#     if num % 1 == 0:
#         num = int(num)
#     return str(num)


# def button_clicked(value):
#     global right_symbols, top_symbols, label, A, B, operator

#     if value in right_symbols:
#         if value == "=":
#             if A is not None and operator is not None:
#                 B = label["text"]
#                 numA = float(A)
#                 numB = float(B)

#                 if operator == "+":
#                     label["text"] = remove_zero_decimal(numA + numB)
#                 elif operator == "-":
#                     label["text"] = remove_zero_decimal(numA - numB)
#                 elif operator == "×":
#                     label["text"] = remove_zero_decimal(numA * numB)
#                 elif operator == "÷":
#                     label["text"] = remove_zero_decimal(numA / numB)

#                 clear_all()

#         elif value in "+-×÷":  # 500 +, *
#             if operator is None:
#                 A = label["text"]
#                 label["text"] = "0"
#                 B = "0"

#             operator = value

#     elif value in top_symbols:
#         if value == "AC":
#             clear_all()
#             label["text"] = "0"

#         elif value == "+/-":
#             result = float(label["text"]) * -1
#             label["text"] = remove_zero_decimal(result)

#         elif value == "%":
#             result = float(label["text"]) / 100
#             label["text"] = remove_zero_decimal(result)

#     else:  # digits or .
#         if value == ".":
#             if value not in label["text"]:
#                 label["text"] += value

#         elif value in "0123456789":
#             if label["text"] == "0":
#                 label["text"] = value  # replace 0
#             else:
#                 label["text"] += value  # append digit


# # center the window
# window.update()  # update window with the new size dimensions
# window_width = window.winfo_width()
# window_height = window.winfo_height()
# screen_width = window.winfo_screenwidth()
# screen_height = window.winfo_screenheight()

# window_x = int((screen_width / 2) - (window_width / 2))
# window_y = int((screen_height / 2) - (window_height / 2))

# # format "(w)x(h)+(x)+(y)"
# window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# window.mainloop()

# st.write("\n" * 15)
# # Add a bold line above the footer
# st.markdown("<hr style='border: 2px solid black;'>", unsafe_allow_html=True)
# # Footer content
# st.write("Copy© 2026 M.Athar | Made With Muhammad Athar Ur Rahman")


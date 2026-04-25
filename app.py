# import streamlit as st

# st.set_page_config(page_title="Calculator", layout="centered")

# # Button layout like your tkinter version
# button_values = [
#     ["AC", "+/-", "%", "÷"],
#     ["7", "8", "9", "×"],
#     ["4", "5", "6", "-"],
#     ["1", "2", "3", "+"],
#     ["0", ".", "√", "="]
# ]

# right_symbols = ["÷", "×", "-", "+", "="]
# top_symbols = ["AC", "+/-", "%"]


# # Session state setup
# if "display" not in st.session_state:
#     st.session_state.display = "0"

# if "A" not in st.session_state:
#     st.session_state.A = None

# if "operator" not in st.session_state:
#     st.session_state.operator = None


# def clear_all():
#     st.session_state.display = "0"
#     st.session_state.A = None
#     st.session_state.operator = None


# def remove_zero_decimal(num):
#     if num % 1 == 0:
#         num = int(num)
#     return str(num)


# def button_clicked(value):
#     display = st.session_state.display

#     # Right-side operators
#     if value in right_symbols:

#         if value == "=":
#             if st.session_state.A is not None and st.session_state.operator is not None:
#                 B = float(display)
#                 A = float(st.session_state.A)

#                 if st.session_state.operator == "+":
#                     result = A + B
#                 elif st.session_state.operator == "-":
#                     result = A - B
#                 elif st.session_state.operator == "×":
#                     result = A * B
#                 elif st.session_state.operator == "÷":
#                     if B != 0:
#                         result = A / B
#                     else:
#                         st.session_state.display = "Error"
#                         st.session_state.A = None
#                         st.session_state.operator = None
#                         return

#                 st.session_state.display = remove_zero_decimal(result)
#                 st.session_state.A = None
#                 st.session_state.operator = None

#         elif value in ["+", "-", "×", "÷"]:
#             st.session_state.A = display
#             st.session_state.operator = value
#             st.session_state.display = "0"

#     # Top symbols
#     elif value in top_symbols:

#         if value == "AC":
#             clear_all()

#         elif value == "+/-":
#             result = float(display) * -1
#             st.session_state.display = remove_zero_decimal(result)

#         elif value == "%":
#             result = float(display) / 100
#             st.session_state.display = remove_zero_decimal(result)

#     # Square root
#     elif value == "√":
#         num = float(display)
#         if num >= 0:
#             st.session_state.display = remove_zero_decimal(num ** 0.5)
#         else:
#             st.session_state.display = "Error"

#     # Numbers and decimal
#     else:
#         if value == ".":
#             if "." not in display:
#                 st.session_state.display += "."

#         elif value in "0123456789":
#             if display == "0":
#                 st.session_state.display = value
#             else:
#                 st.session_state.display += value


# # Title
# st.title("Calculator")

# # Display
# st.markdown(
#     f"""
#     <div style="
#         background-color: black;
#         color: white;
#         padding: 20px;
#         font-size: 40px;
#         text-align: right;
#         border-radius: 10px;
#         margin-bottom: 20px;
#     ">
#         {st.session_state.display}
#     </div>
#     """,
#     unsafe_allow_html=True
# )

# # Buttons layout
# for row in button_values:
#     cols = st.columns(4)

#     for i, value in enumerate(row):
#         with cols[i]:
#             if st.button(value, use_container_width=True):
#                 button_clicked(value)
#                 st.rerun()

# st.write("\n" * 15)
# # Add a bold line above the footer
# st.markdown("<hr style='border: 2px solid black;'>", unsafe_allow_html=True)
# # Footer content
# st.write("Copy© 2026 M.Athar | Made With Muhammad Athar Ur Rahman")


###########################################################################################################################

# import streamlit as st
# import math

# # --- CONFIG & STYLES ---
# st.set_page_config(page_title="Pro Calculator", layout="centered")

# # Custom CSS to make it look "Human-Designed" and polished
# st.markdown("""
#     <style>
#     div.stButton > button {
#         height: 3em;
#         font-size: 20px;
#         font-weight: 500;
#         border-radius: 10px;
#     }
#     .main {
#         background-color: #f5f5f5;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # --- APP STATE MANAGEMENT ---
# def init_state():
#     if "display" not in st.session_state:
#         st.session_state.display = "0"
#     if "operand_a" not in st.session_state:
#         st.session_state.operand_a = None
#     if "operator" not in st.session_state:
#         st.session_state.operator = None
#     if "new_num" not in st.session_state:
#         st.session_state.new_num = False

# init_state()

# # --- LOGIC FUNCTIONS ---
# def format_number(val):
#     """Formats float to string, stripping .0 if it's an integer."""
#     try:
#         return f"{int(val):,}" if val % 1 == 0 else f"{val:g}"
#     except:
#         return "Error"

# def calculate():
#     if st.session_state.operand_a is None or st.session_state.operator is None:
#         return

#     try:
#         a = float(st.session_state.operand_a)
#         b = float(st.session_state.display.replace(",", ""))
        
#         ops = {
#             "+": lambda x, y: x + y,
#             "-": lambda x, y: x - y,
#             "×": lambda x, y: x * y,
#             "÷": lambda x, y: x / y if y != 0 else "Error"
#         }
        
#         result = ops[st.session_state.operator](a, b)
#         st.session_state.display = format_number(result) if result != "Error" else "Error"
#     except Exception:
#         st.session_state.display = "Error"
    
#     st.session_state.operand_a = None
#     st.session_state.operator = None

# def handle_click(key):
#     display = st.session_state.display

#     if key.isdigit() or key == ".":
#         if st.session_state.new_num or display == "0":
#             st.session_state.display = key if key != "." else "0."
#             st.session_state.new_num = False
#         else:
#             if key == "." and "." in display:
#                 return
#             st.session_state.display += key

#     elif key == "AC":
#         st.session_state.display = "0"
#         st.session_state.operand_a = None
#         st.session_state.operator = None

#     elif key == "+/-":
#         val = float(display.replace(",", "")) * -1
#         st.session_state.display = format_number(val)

#     elif key == "%":
#         val = float(display.replace(",", "")) / 100
#         st.session_state.display = format_number(val)

#     elif key == "√":
#         val = float(display.replace(",", ""))
#         st.session_state.display = format_number(math.sqrt(val)) if val >= 0 else "Error"

#     elif key in ["+", "-", "×", "÷"]:
#         st.session_state.operand_a = display.replace(",", "")
#         st.session_state.operator = key
#         st.session_state.new_num = True

#     elif key == "=":
#         calculate()

# # --- UI LAYOUT ---
# st.title("🧮 Modern Calculator")

# # High-end display panel
# st.markdown(f"""
#     <div style="background-color:#1e1e1e; color:#00ff00; padding:30px; 
#                 text-align:right; font-size:50px; font-family:monospace; 
#                 border-radius:10px; margin-bottom:20px; border: 4px solid #333;">
#         {st.session_state.display}
#     </div>
# """, unsafe_allow_html=True)

# # Grid Layout
# buttons = [
#     ["AC", "+/-", "%", "÷"],
#     ["7", "8", "9", "×"],
#     ["4", "5", "6", "-"],
#     ["1", "2", "3", "+"],
#     ["0", ".", "√", "="]
# ]

# for row in buttons:
#     cols = st.columns(4)
#     for i, label in enumerate(row):
#         if cols[i].button(label, use_container_width=True, key=f"btn_{label}"):
#             handle_click(label)
#             st.rerun()


##################################################################################################################


import tkinter as tk

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("Modern Calculator")
root.geometry("350x500")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

# ---------------- DISPLAY ----------------
expression = ""

display = tk.Entry(root, font=("Arial", 24), bg="#2d2d2d", fg="white",
                   justify="right", bd=0)
display.pack(fill="both", ipadx=8, ipady=25, padx=10, pady=20)

# ---------------- FUNCTIONS ----------------
def press(num):
    global expression
    expression += str(num)
    display.delete(0, tk.END)
    display.insert(tk.END, expression)

def clear():
    global expression
    expression = ""
    display.delete(0, tk.END)

def backspace():
    global expression
    expression = expression[:-1]
    display.delete(0, tk.END)
    display.insert(tk.END, expression)

def equal():
    global expression
    try:
        result = str(eval(expression))
        display.delete(0, tk.END)
        display.insert(tk.END, result)
        expression = result
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        expression = ""

# ---------------- BUTTON STYLE ----------------
btn_font = ("Arial", 18)
btn_bg = "#333333"
btn_fg = "white"
btn_active = "#555555"

def create_button(text, row, col, command, colspan=1):
    btn = tk.Button(root, text=text, font=btn_font,
                    bg=btn_bg, fg=btn_fg,
                    activebackground=btn_active,
                    bd=0, command=command)
    btn.place(x=20 + col*80, y=120 + row*80,
              width=70, height=70)

# ---------------- BUTTONS ----------------
# Row 0
create_button("C", 0, 0, clear)
create_button("⌫", 0, 1, backspace)
create_button("/", 0, 2, lambda: press("/"))
create_button("*", 0, 3, lambda: press("*"))

# Row 1
create_button("7", 1, 0, lambda: press("7"))
create_button("8", 1, 1, lambda: press("8"))
create_button("9", 1, 2, lambda: press("9"))
create_button("-", 1, 3, lambda: press("-"))

# Row 2
create_button("4", 2, 0, lambda: press("4"))
create_button("5", 2, 1, lambda: press("5"))
create_button("6", 2, 2, lambda: press("6"))
create_button("+", 2, 3, lambda: press("+"))

# Row 3
create_button("1", 3, 0, lambda: press("1"))
create_button("2", 3, 1, lambda: press("2"))
create_button("3", 3, 2, lambda: press("3"))
create_button("=", 3, 3, equal)

# Row 4
create_button("0", 4, 0, lambda: press("0"))
create_button(".", 4, 1, lambda: press("."))
create_button("(", 4, 2, lambda: press("("))
create_button(")", 4, 3, lambda: press(")"))

# ---------------- RUN ----------------
root.mainloop()



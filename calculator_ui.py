import os
import streamlit as st

HISTORY_FILE = "history.txt"
st.set_page_config(page_title="Calculator", page_icon="🧮")
st.title("🧮 Calculator")

ops = {"+": lambda a, b: a + b, "-": lambda a, b: a - b,
       "*": lambda a, b: a * b, "/": lambda a, b: a / b}

st.session_state.setdefault("num1", 0.0)
st.session_state.setdefault("last", None)

def use_result():
    st.session_state.num1 = st.session_state.last

def new_calc():
    st.session_state.num1 = 0.0
    st.session_state.last = None

c1, c2, c3 = st.columns([2, 1, 2])
n1 = c1.number_input("First number", key="num1", format="%g")
op = c2.selectbox("Operation", list(ops))
n2 = c3.number_input("Second number", value=0.0, format="%g")

if st.button("Calculate", type="primary"):
    try:
        out = ops[op](n1, n2)
        eq = f"{n1} {op} {n2} = {out}"
        st.session_state.last = out
        with open(HISTORY_FILE, "a") as f:
            f.write(eq + "\n")
        st.success(eq)
    except ZeroDivisionError:
        st.error("Cannot divide by zero.")

if st.session_state.last is not None:
    b1, b2 = st.columns(2)
    b1.button(f"Continue with {st.session_state.last}", on_click=use_result)
    b2.button("Start new calculation", on_click=new_calc)

st.subheader("History")
if st.button("Clear history"):
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)
        st.success("History cleared.")
    else:
        st.info("No history to clear.")
if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE) as f:
        st.code("".join(f) or "(empty)")
else:
    st.caption("No history exists yet.")

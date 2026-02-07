import streamlit as st

# THIS MUST BE FIRST
st.set_page_config(page_title="Rocket Safety System", page_icon="🚀")

st.title("🚀 Rocket Launch Safety System")
st.write("If you see this text, the app is running correctly.")

st.divider()

st.subheader("Launch Conditions")

temperature = st.number_input("Temperature (°C)", value=22.0)
wind = st.number_input("Wind Speed (m/s)", value=15.0)
fuel = st.number_input("Fuel Level (%)", value=80.0)
pressure = st.number_input("Pressure (kPa)", value=100.0)
battery = st.number_input("Battery (%)", value=90.0)

def evaluate(t, w, f, p, b):
    no_go = []
    hold = []

    if w > 25:
        no_go.append("Wind too high")
    if f < 40:
        no_go.append("Fuel too low")
    if p < 90 or p > 110:
        no_go.append("Pressure out of range")
    if b < 30:
        no_go.append("Battery too low")
    if t < -5 or t > 45:
        no_go.append("Temperature out of range")

    if not no_go:
        if 18 <= w <= 25:
            hold.append("Wind near limit")
        if 40 <= f <= 55:
            hold.append("Fuel near limit")

    if no_go:
        return "NO-GO", no_go
    if hold:
        return "HOLD", hold
    return "GO", ["All conditions safe"]

if st.button("Check Rocket Safety"):
    status, reasons = evaluate(temperature, wind, fuel, pressure, battery)

    if status == "GO":
        st.success("STATUS: GO ✅")
    elif status == "HOLD":
        st.warning("STATUS: HOLD ⚠️")
    else:
        st.error("STATUS: NO-GO ❌")

    for r in reasons:
        st.write("•", r)
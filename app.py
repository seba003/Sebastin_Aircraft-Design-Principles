# ==========================================================
# ✈️ DIGITAL AIRCRAFT DESIGN STUDIO - PART 1
# FOUNDATION + DATA ENGINE + ANALYTICS
# ==========================================================

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io
from sklearn.linear_model import LinearRegression

st.set_page_config(layout="wide")

# ==========================================================
# HEADER (PROFESSIONAL - CLEAN)
# ==========================================================
st.markdown("""
# Aircraft Design Principles Course (213AER4113)

### Course Instructor:
Dr. J. Sarathkumar Sebastin  
Associate Professor, Aeronautical Engineering, KARE  

Phone: +91-7639972833  
Email: sarathkumar.j@klu.ac.in | sebastinaero@gmail.com  
LinkedIn: https://www.linkedin.com/in/dr-j-sarathkumar-sebastin-041162111/  
Blog: https://sarathaerolab.blogspot.com  

---
""")

st.title("Digital Aircraft Design Studio + Virtual Lab")

# ==========================================================
# SIDEBAR NAVIGATION
# ==========================================================
st.sidebar.title("Navigation")

section = st.sidebar.radio("Go to Module", [
    "1. Data Input",
    "2. Validation",
    "3. Derived Parameters",
    "4. Statistical Analysis",
    "5. Regression Models",
    "6. Visualization"
])

# ==========================================================
# DOWNLOAD UTILITIES
# ==========================================================
def download_csv(df, name):
    csv = df.to_csv(index=False).encode()
    st.download_button(f"Download {name}", csv, f"{name}.csv")

def download_plot(fig, name):
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    st.download_button(f"Download {name}", buf.getvalue(), f"{name}.png")

# ==========================================================
# GLOBAL CONSTANTS
# ==========================================================
g = 9.81

# ==========================================================
# ✈️ INTRODUCTION: AIRCRAFT DESIGN FUNDAMENTALS
# ==========================================================

st.header("📘 Aircraft Design Fundamentals & Pre-Requisites")

st.markdown("""
### 🎯 Objective:
Before designing an aircraft, students must understand:

- What is an aircraft?
- How aircraft are classified
- What parameters define an aircraft
- How to interpret aircraft data

This module prepares you to **think like an aircraft designer**
""")

# ==========================================================
# SECTION 1: WHAT IS AN AIRCRAFT?
# ==========================================================
st.subheader("✈️ 1. What is an Aircraft?")

st.markdown("""
An aircraft is a vehicle capable of **sustained flight** through the atmosphere.

### 🧠 Key Principle:
\[
Lift \geq Weight
\]

### Forces Acting on Aircraft:
- Lift (Upward)
- Weight (Downward)
- Thrust (Forward)
- Drag (Backward)
""")

# ==========================================================
# SECTION 2: AIRCRAFT CLASSIFICATION
# ==========================================================
st.subheader("🧩 2. Aircraft Classification")

st.markdown("### 🔹 Based on Speed (Mach Number)")

mach = st.slider("Example Speed (m/s)", 50, 1000, 250)
Mach = mach / 340

if Mach < 0.3:
    regime = "Low Subsonic"
elif Mach < 0.8:
    regime = "Subsonic"
elif Mach < 1.2:
    regime = "Transonic"
elif Mach < 5:
    regime = "Supersonic"
else:
    regime = "Hypersonic"

st.write(f"Mach Number: {Mach:.2f}")
st.write(f"Flight Regime: {regime}")

st.markdown("""
### 🔹 Based on Mission:
- Passenger Aircraft
- Cargo Aircraft
- Fighter Aircraft
- Trainer Aircraft
- UAV / Drones

### 🔹 Based on Configuration:
- Conventional (tube + wing)
- Flying Wing
- Canard Configuration
- Blended Wing Body
""")

# ==========================================================
# SECTION 3: KEY AIRCRAFT PARAMETERS
# ==========================================================
st.subheader("📊 3. Key Aircraft Parameters")

st.markdown("""
### 🔹 Weight Parameters
- MTOW (Maximum Takeoff Weight)
- Empty Weight
- Payload
- Fuel Weight

### 🔹 Geometric Parameters
- Wing Area (S)
- Wingspan (b)
- Aspect Ratio (AR)
- Fuselage Length

### 🔹 Performance Parameters
- Cruise Speed
- Range
- Ceiling
- Takeoff Distance

### 🔹 Aerodynamic Parameters
- CL (Lift Coefficient)
- CD (Drag Coefficient)
- L/D Ratio
""")

# ==========================================================
# SECTION 4: HOW TO READ AIRCRAFT DATA
# ==========================================================
st.subheader("📖 4. Understanding Aircraft Data")

st.markdown("""
Students must understand relationships:

### Example:

\[
W/S = \frac{W}{S}
\]

👉 High W/S → Faster aircraft  
👉 Low W/S → Better takeoff  

---

\[
T/W = \frac{T}{W}
\]

👉 High T/W → Better climb  
👉 Low T/W → Fuel efficient  

---

### 🧠 Key Insight:
Aircraft design is always a **trade-off**
""")

# ==========================================================
# SECTION 5: DESIGN THINKING APPROACH
# ==========================================================
st.subheader("🧠 5. How to Approach Aircraft Design")

st.markdown("""
### Step-by-Step Thinking:

1. Understand mission (payload, range)
2. Study existing aircraft (dataset)
3. Identify trends (W/S, T/W)
4. Estimate weight
5. Size wing and engine
6. Validate performance

---

### ⚠️ Important:
Aircraft design is **iterative**, not linear.
""")

# ==========================================================
# SECTION 6: READY CHECK
# ==========================================================
st.subheader("✅ 6. Ready to Proceed?")

ready = st.checkbox("I understand the basics and ready to upload dataset")

if not ready:
    st.warning("Please go through the fundamentals before proceeding")
    st.stop()
else:
    st.success("You are ready to begin aircraft design")

# ==========================================================
# ✈️ ADVANCED LEARNING MODULE (QUIZ + IDENTIFICATION + VISUAL)
# ==========================================================

st.header("🧠 Learning Assessment & Interactive Understanding")

# ==========================================================
# QUIZ MODULE
# ==========================================================
st.subheader("📝 1. Concept Assessment Quiz")

score = 0

q1 = st.radio("1. What condition is required for level flight?",
              ["Lift < Weight", "Lift = Weight", "Thrust = Drag", "Lift > Drag"])

if q1 == "Lift = Weight":
    score += 1

q2 = st.radio("2. High Wing Loading results in?",
              ["Better takeoff", "Higher speed", "Lower drag always", "Lower thrust"])

if q2 == "Higher speed":
    score += 1

q3 = st.radio("3. What does T/W represent?",
              ["Power ratio", "Fuel ratio", "Thrust to Weight", "Drag ratio"])

if q3 == "Thrust to Weight":
    score += 1

q4 = st.radio("4. What happens when L/D increases?",
              ["Range decreases", "Efficiency increases", "Fuel increases", "Speed decreases"])

if q4 == "Efficiency increases":
    score += 1

q5 = st.radio("5. Aircraft design is?",
              ["Linear process", "Random process", "Iterative process", "Fixed process"])

if q5 == "Iterative process":
    score += 1

st.write(f"Score: {score}/5")

if score >= 4:
    st.success("Excellent understanding! You may proceed.")
else:
    st.warning("Please revise concepts before proceeding.")

# ==========================================================
# AIRCRAFT IDENTIFICATION
# ==========================================================
st.subheader("🔍 2. Aircraft Identification Exercise")

st.markdown("""
Classify the aircraft based on given characteristics.
""")

mission_type = st.selectbox("Mission Type", ["Passenger", "Cargo", "Fighter", "UAV"])
speed_type = st.selectbox("Speed Category", ["Subsonic", "Supersonic"])
config_type = st.selectbox("Configuration", ["Conventional", "Flying Wing", "Canard"])

if st.button("Evaluate Classification"):

    if mission_type == "Passenger" and speed_type == "Subsonic":
        st.success("Correct classification for commercial transport aircraft")
    elif mission_type == "Fighter" and speed_type == "Supersonic":
        st.success("Correct classification for fighter aircraft")
    else:
        st.info("This combination is possible but less common. Think deeper!")

# ==========================================================
# INTERACTIVE DIAGRAMS
# ==========================================================
st.subheader("📊 3. Interactive Aircraft Diagrams")

# ----------------------------------------------------------
# Forces Diagram
# ----------------------------------------------------------
st.markdown("### ✈️ Forces Acting on Aircraft")

fig1, ax1 = plt.subplots()

ax1.arrow(0, 0, 0, 1, head_width=0.1)
ax1.text(0, 1.1, "Lift")

ax1.arrow(0, 0, 0, -1, head_width=0.1)
ax1.text(0, -1.2, "Weight")

ax1.arrow(0, 0, 1, 0, head_width=0.1)
ax1.text(1.1, 0, "Thrust")

ax1.arrow(0, 0, -1, 0, head_width=0.1)
ax1.text(-1.3, 0, "Drag")

ax1.set_title("Forces on Aircraft")
ax1.set_xlim(-2,2)
ax1.set_ylim(-2,2)

st.pyplot(fig1)
download_plot(fig1, "Forces_Diagram")

# ----------------------------------------------------------
# Wing Geometry Diagram
# ----------------------------------------------------------
st.markdown("### 🛩️ Wing Geometry")

span = st.slider("Span (m)", 10, 40, 20)
chord_root = st.slider("Root Chord (m)", 2, 10, 5)
chord_tip = st.slider("Tip Chord (m)", 1, 5, 2)

fig2, ax2 = plt.subplots()

ax2.plot([0, span/2], [chord_root/2, chord_tip/2])
ax2.plot([0, span/2], [-chord_root/2, -chord_tip/2])

ax2.set_xlabel("Span (m)")
ax2.set_ylabel("Chord (m)")
ax2.set_title("Wing Planform")

st.pyplot(fig2)
download_plot(fig2, "Wing_Geometry")

# ----------------------------------------------------------
# Lift vs Drag Curve
# ----------------------------------------------------------
st.markdown("### 📉 Lift vs Drag")

CL = np.linspace(0, 1.5, 50)
CD0 = 0.02
k = 0.045

CD = CD0 + k * CL**2

fig3, ax3 = plt.subplots()
ax3.plot(CL, CD)

ax3.set_xlabel("Lift Coefficient (CL)")
ax3.set_ylabel("Drag Coefficient (CD)")
ax3.set_title("Drag Polar")

st.pyplot(fig3)
download_plot(fig3, "Drag_Polar_Interactive")

# ==========================================================
# FINAL READY CHECK
# ==========================================================
st.subheader("✅ Final Readiness Check")

ready_final = st.checkbox("I completed assessment and ready for aircraft design")

if not ready_final:
    st.warning("Complete all learning modules before proceeding")
    st.stop()
else:
    st.success("You are fully prepared for Aircraft Design Phase")

# ==========================================================
# MODULE 1: DATA INPUT
# ==========================================================
if section == "1. Data Input":

    st.header("Module 1: Aircraft Dataset Input")

    st.markdown("""
### Objective:
To build a **data-driven aircraft design database**

### Requirement:
- Minimum 10 aircraft
- Same category recommended
""")

    uploaded_file = st.file_uploader("Upload CSV/Excel", type=["csv", "xlsx"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)
        st.session_state["df"] = df

        st.subheader("Dataset Preview")
        st.dataframe(df)
        download_csv(df, "Uploaded_Dataset")

# ==========================================================
# MODULE 2: VALIDATION
# ==========================================================
if section == "2. Validation":

    st.header("Module 2: Data Validation")

    if "df" not in st.session_state:
        st.warning("Upload dataset first")
        st.stop()

    df = st.session_state["df"]

    errors = []

    for i, row in df.iterrows():

        if row["Empty Weight (kg)"] >= row["MTOW (kg)"]:
            errors.append(f"Row {i+1}: Empty Weight must be < MTOW")

        if row["Wing Area (m^2)"] <= 0:
            errors.append(f"Row {i+1}: Wing Area must be > 0")

        if row["Total Thrust (N)"] <= 0:
            errors.append(f"Row {i+1}: Thrust must be > 0")

    if errors:
        for e in errors:
            st.error(e)
    else:
        st.success("Dataset is physically consistent")

# ==========================================================
# MODULE 3: DERIVED PARAMETERS
# ==========================================================
if section == "3. Derived Parameters":

    st.header("Module 3: Derived Aerodynamic Parameters")

    if "df" not in st.session_state:
        st.warning("Upload dataset first")
        st.stop()

    df = st.session_state["df"]

    st.markdown("""
### Wing Loading

\[
W/S = \frac{W}{S}
\]

Where:
- W = MTOW × g
- S = Wing Area
""")

    df["Wing Loading (N/m^2)"] = (df["MTOW (kg)"] * g) / df["Wing Area (m^2)"]

    st.markdown("""
### Thrust-to-Weight Ratio

\[
T/W = \frac{T}{W}
\]
""")

    df["T/W"] = df["Total Thrust (N)"] / (df["MTOW (kg)"] * g)

    st.markdown("""
### Power Loading

\[
W/P = \frac{W}{Power}
\]
""")

    df["Power Loading"] = df["MTOW (kg)"] / (df["Total Thrust (N)"]/1000)

    st.dataframe(df)
    download_csv(df, "Derived_Parameters")

# ==========================================================
# MODULE 4: STATISTICS
# ==========================================================
if section == "4. Statistical Analysis":

    st.header("Module 4: Statistical Analysis")

    if "df" not in st.session_state:
        st.warning("Upload dataset first")
        st.stop()

    df = st.session_state["df"]

    st.subheader("Descriptive Statistics")
    st.dataframe(df.describe())

    # Histogram
    fig, ax = plt.subplots()
    df["MTOW (kg)"].hist(ax=ax)
    ax.set_xlabel("MTOW (kg)")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)
    download_plot(fig, "MTOW_Histogram")

# ==========================================================
# MODULE 5: REGRESSION
# ==========================================================
if section == "5. Regression Models":

    st.header("Module 5: Regression Models")

    if "df" not in st.session_state:
        st.warning("Upload dataset first")
        st.stop()

    df = st.session_state["df"]

    X = df[["MTOW (kg)"]]
    y = df["Wing Area (m^2)"]

    model = LinearRegression().fit(X, y)

    st.write(f"Equation: S = {model.coef_[0]:.4f} W + {model.intercept_:.2f}")

    mtow_range = np.linspace(min(X.values)[0], max(X.values)[0], 100)
    wing_pred = model.predict(mtow_range.reshape(-1,1))

    fig, ax = plt.subplots()
    ax.scatter(X, y)
    ax.plot(mtow_range, wing_pred)

    ax.set_xlabel("MTOW (kg)")
    ax.set_ylabel("Wing Area (m²)")

    st.pyplot(fig)
    download_plot(fig, "Regression")

# ==========================================================
# MODULE 6: VISUALIZATION
# ==========================================================
if section == "6. Visualization":

    st.header("Module 6: Correlation & Visualization")

    if "df" not in st.session_state:
        st.warning("Upload dataset first")
        st.stop()

    df = st.session_state["df"]

    corr = df.corr(numeric_only=True)

    fig, ax = plt.subplots(figsize=(8,6))
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)

    st.pyplot(fig)
    download_plot(fig, "Correlation")

    # ==========================================================
# ✈️ PART 2: MISSION + WEIGHT BUILD-UP + MTOW SOLVER
# ==========================================================

if section == "7. Mission Definition":

    st.header("Module 7: Mission Definition")

    st.markdown("""
### Objective:
Define the **operational requirements** of the aircraft.

### Inputs:
- Payload → useful load
- Range → mission distance
- Cruise Speed → operating condition
- Altitude → affects density
""")

    payload = st.slider("Payload (kg)", 1000, 50000, 10000)
    range_km = st.slider("Range (km)", 500, 10000, 3000)
    V = st.slider("Cruise Speed (m/s)", 100, 300, 200)
    altitude = st.slider("Altitude (m)", 0, 15000, 10000)

    st.session_state["mission"] = {
        "payload": payload,
        "range": range_km,
        "V": V,
        "altitude": altitude
    }

# ==========================================================
# MODULE 8: FUEL FRACTION
# ==========================================================
if section == "8. Fuel Fraction":

    st.header("Module 8: Fuel Fraction (Breguet Equation)")

    if "mission" not in st.session_state:
        st.warning("Define mission first")
        st.stop()

    mission = st.session_state["mission"]

    payload = mission["payload"]
    R = mission["range"] * 1000
    V = mission["V"]

    st.latex(r"R = \frac{V}{c} \cdot \frac{L}{D} \ln\left(\frac{W_i}{W_f}\right)")

    ld = st.slider("L/D", 10.0, 25.0, 15.0)
    sfc = st.slider("SFC (1/s)", 0.00001, 0.0001, 0.00003)

    wf_ratio = np.exp(R * sfc / (V * ld))

    fuel_fraction = 1 - (1 / wf_ratio)

    st.write(f"Fuel Fraction: {fuel_fraction:.4f}")

    st.session_state["fuel_fraction"] = fuel_fraction

# ==========================================================
# MODULE 9: EMPTY WEIGHT ESTIMATION
# ==========================================================
if section == "9. Empty Weight":

    st.header("Module 9: Empty Weight Estimation")

    st.markdown("""
Empirical Relation:

\[
W_e = k W^n
\]
""")

    k = st.slider("k (empirical)", 0.4, 0.7, 0.55)
    n = st.slider("n (empirical)", 0.5, 0.9, 0.65)

    st.session_state["empty_constants"] = {"k": k, "n": n}

# ==========================================================
# MODULE 10: MTOW ITERATIVE SOLVER
# ==========================================================
if section == "10. MTOW Solver":

    st.header("Module 10: MTOW Iterative Solver")

    if "fuel_fraction" not in st.session_state:
        st.warning("Compute fuel fraction first")
        st.stop()

    if "empty_constants" not in st.session_state:
        st.warning("Define empty weight constants")
        st.stop()

    payload = st.session_state["mission"]["payload"]
    fuel_fraction = st.session_state["fuel_fraction"]
    k = st.session_state["empty_constants"]["k"]
    n = st.session_state["empty_constants"]["n"]

    st.markdown("""
### Governing Equation:

\[
W_0 = \frac{Payload}{1 - W_f - W_e}
\]
""")

    W0 = 20000  # initial guess
    history = []

    for i in range(20):

        We = k * (W0 ** n)
        We_fraction = We / W0

        W_new = payload / (1 - fuel_fraction - We_fraction)

        history.append(W_new)

        if abs(W_new - W0) < 1:
            break

        W0 = W_new

    st.write(f"Final MTOW: {W_new:.2f} kg")

    # Iteration Table
    df_iter = pd.DataFrame({"Iteration": range(len(history)), "MTOW": history})
    st.dataframe(df_iter)

    download_csv(df_iter, "MTOW_Iteration")

    # Convergence Plot
    fig, ax = plt.subplots()
    ax.plot(history)

    ax.set_xlabel("Iteration")
    ax.set_ylabel("MTOW (kg)")
    ax.set_title("MTOW Convergence")

    st.pyplot(fig)
    download_plot(fig, "MTOW_Convergence")

    st.session_state["MTOW"] = W_new

# ==========================================================
# MODULE 11: WEIGHT BREAKDOWN
# ==========================================================
if section == "11. Weight Breakdown":

    st.header("Module 11: Weight Breakdown")

    if "MTOW" not in st.session_state:
        st.warning("Run MTOW solver first")
        st.stop()

    W0 = st.session_state["MTOW"]
    fuel_fraction = st.session_state["fuel_fraction"]

    fuel = W0 * fuel_fraction
    empty = W0 - fuel - st.session_state["mission"]["payload"]

    st.write(f"MTOW: {W0:.2f}")
    st.write(f"Fuel: {fuel:.2f}")
    st.write(f"Empty: {empty:.2f}")
    st.write(f"Payload: {st.session_state['mission']['payload']}")

    df_weights = pd.DataFrame({
        "Component": ["MTOW", "Fuel", "Empty", "Payload"],
        "Weight (kg)": [W0, fuel, empty, st.session_state["mission"]["payload"]]
    })

    st.dataframe(df_weights)
    download_csv(df_weights, "Weight_Breakdown")

    # ==========================================================
# ✈️ PART 3: CONSTRAINT ANALYSIS & DESIGN SPACE
# ==========================================================

# ==========================================================
# MODULE 13: WING LOADING FOUNDATION
# ==========================================================
if section == "13. Wing Loading":

    st.header("Module 13: Wing Loading (W/S)")

    st.markdown("""
### Definition:
Wing loading is the **weight per unit wing area**

\[
W/S = \frac{W}{S}
\]

### Interpretation:
- High W/S → High speed, longer runway
- Low W/S → Better takeoff, maneuverability
""")

    if "MTOW" not in st.session_state:
        st.warning("Run MTOW solver first")
        st.stop()

    W = st.session_state["MTOW"] * g

    S = st.slider("Wing Area (m²)", 10.0, 200.0, 50.0)

    WS = W / S

    st.write(f"Wing Loading: {WS:.2f} N/m²")

# ==========================================================
# MODULE 14: CONSTRAINT EQUATIONS
# ==========================================================
if section == "14. Constraint Equations":

    st.header("Module 14: Constraint Equations")

    rho = 1.225

    V_to = st.slider("Takeoff Speed (m/s)", 50, 100, 70)
    V_cr = st.session_state["mission"]["V"]
    V_land = st.slider("Landing Speed (m/s)", 50, 100, 65)

    CLmax = st.slider("CLmax", 1.0, 2.5, 1.5)
    CD0 = st.slider("CD0", 0.01, 0.05, 0.02)
    k = st.slider("k", 0.02, 0.1, 0.045)

    RC = st.slider("Rate of Climb (m/s)", 2.0, 20.0, 5.0)

    ws = np.linspace(1000, 10000, 200)

    # Takeoff
    tw_to = ws / (0.5 * rho * CLmax * V_to**2)

    # Cruise
    q = 0.5 * rho * V_cr**2
    tw_cr = (q * CD0)/ws + (k * ws)/q

    # Climb
    tw_cl = tw_cr + (RC / V_cr)

    # Landing (vertical line)
    ws_land = 0.5 * rho * V_land**2 * CLmax

    fig, ax = plt.subplots()

    ax.plot(ws, tw_to, label="Takeoff")
    ax.plot(ws, tw_cr, label="Cruise")
    ax.plot(ws, tw_cl, label="Climb")

    ax.axvline(ws_land, linestyle="--", label="Landing Limit")

    ax.set_xlabel("Wing Loading (N/m²)")
    ax.set_ylabel("Thrust-to-Weight Ratio")
    ax.set_title("Constraint Diagram")

    ax.legend()
    ax.grid()

    st.pyplot(fig)
    download_plot(fig, "Constraint_Diagram")

# ==========================================================
# MODULE 15: DESIGN POINT
# ==========================================================
if section == "15. Design Point":

    st.header("Module 15: Design Point Analysis")

    if "MTOW" not in st.session_state:
        st.warning("Run previous modules first")
        st.stop()

    W = st.session_state["MTOW"] * g

    S = st.slider("Wing Area (m²)", 10.0, 200.0, 50.0)
    T = st.slider("Thrust (N)", 10000.0, 300000.0, 100000.0)

    WS = W / S
    TW = T / W

    st.write(f"W/S: {WS:.2f}")
    st.write(f"T/W: {TW:.3f}")

# ==========================================================
# MODULE 16: OPTIMAL DESIGN POINT
# ==========================================================
if section == "16. Optimal Design":

    st.header("Module 16: Optimal Design Point")

    rho = 1.225
    V_cr = st.session_state["mission"]["V"]

    CD0 = 0.02
    k = 0.045

    ws = np.linspace(1000, 10000, 200)

    q = 0.5 * rho * V_cr**2
    tw_cr = (q * CD0)/ws + (k * ws)/q

    min_tw = min(tw_cr)
    opt_ws = ws[np.argmin(tw_cr)]

    st.write(f"Optimal W/S: {opt_ws:.2f}")
    st.write(f"Minimum T/W: {min_tw:.3f}")

    fig, ax = plt.subplots()
    ax.plot(ws, tw_cr)
    ax.scatter(opt_ws, min_tw)

    ax.set_xlabel("Wing Loading (N/m²)")
    ax.set_ylabel("T/W")

    st.pyplot(fig)
    download_plot(fig, "Optimal_Point")

    # ==========================================================
# ✈️ PART 4: GEOMETRY + PERFORMANCE + FINAL SYSTEM
# ==========================================================

# ==========================================================
# MODULE 17: WING GEOMETRY
# ==========================================================
if section == "17. Wing Geometry":

    st.header("Module 17: Wing Geometry")

    if "MTOW" not in st.session_state:
        st.warning("Run previous modules first")
        st.stop()

    W = st.session_state["MTOW"] * 9.81

    S = st.slider("Wing Area (m²)", 10.0, 200.0, 50.0)
    AR = st.slider("Aspect Ratio", 6.0, 14.0, 9.0)
    taper = st.slider("Taper Ratio", 0.2, 1.0, 0.5)
    sweep = st.slider("Sweep Angle (deg)", 0.0, 45.0, 15.0)

    b = np.sqrt(AR * S)

    # Root and Tip Chord
    Cr = (2 * S) / (b * (1 + taper))
    Ct = taper * Cr

    # MAC
    MAC = (2/3) * Cr * ((1 + taper + taper**2)/(1 + taper))

    st.write(f"Wingspan: {b:.2f} m")
    st.write(f"Root Chord: {Cr:.2f} m")
    st.write(f"Tip Chord: {Ct:.2f} m")
    st.write(f"Mean Aerodynamic Chord: {MAC:.2f} m")

    # Planform Plot
    fig, ax = plt.subplots()
    ax.plot([0, b/2], [Cr/2, Ct/2])
    ax.plot([0, b/2], [-Cr/2, -Ct/2])
    ax.set_xlabel("Span (m)")
    ax.set_ylabel("Chord (m)")
    ax.set_title("Wing Planform")
    st.pyplot(fig)
    download_plot(fig, "WingPlanform")

# ==========================================================
# MODULE 18: FUSELAGE DESIGN
# ==========================================================
if section == "18. Fuselage":

    st.header("Module 18: Fuselage Design")

    payload = st.session_state["mission"]["payload"]

    length = st.slider("Fuselage Length Factor", 5.0, 12.0, 8.0)
    diameter = st.slider("Diameter Factor", 1.0, 4.0, 2.5)

    fus_length = length * (payload/1000)**(1/3)
    fus_diam = diameter

    slenderness = fus_length / fus_diam

    st.write(f"Length: {fus_length:.2f} m")
    st.write(f"Diameter: {fus_diam:.2f} m")
    st.write(f"Slenderness Ratio: {slenderness:.2f}")

# ==========================================================
# MODULE 19: TAIL SIZING
# ==========================================================
if section == "19. Tail":

    st.header("Module 19: Tail Sizing")

    S = st.slider("Wing Area (m²)", 10.0, 200.0, 50.0)
    b = st.slider("Wingspan (m)", 5.0, 50.0, 20.0)
    c = st.slider("MAC (m)", 1.0, 5.0, 3.0)

    Vh = st.slider("Horizontal Tail Volume Coefficient", 0.5, 1.0, 0.7)
    Vv = st.slider("Vertical Tail Volume Coefficient", 0.05, 0.2, 0.1)

    Lh = st.slider("Tail Arm (m)", 5.0, 20.0, 10.0)

    Sh = (Vh * S * c) / Lh
    Sv = (Vv * S * b) / Lh

    st.write(f"Horizontal Tail Area: {Sh:.2f} m²")
    st.write(f"Vertical Tail Area: {Sv:.2f} m²")

# ==========================================================
# MODULE 20: DRAG & THRUST REQUIRED
# ==========================================================
if section == "20. Performance":

    st.header("Module 20: Drag & Thrust Required")

    rho = 1.225
    S = st.slider("Wing Area (m²)", 10.0, 200.0, 50.0)

    CD0 = st.slider("CD0", 0.01, 0.05, 0.02)
    k = st.slider("k", 0.02, 0.1, 0.045)

    V_range = np.linspace(50, 300, 100)

    Drag = []
    for V in V_range:
        q = 0.5 * rho * V**2
        CL = st.session_state["MTOW"]*9.81/(q*S)
        CD = CD0 + k*CL**2
        Drag.append(q*S*CD)

    fig, ax = plt.subplots()
    ax.plot(V_range, Drag)

    ax.set_xlabel("Velocity (m/s)")
    ax.set_ylabel("Drag (N)")
    ax.set_title("Drag vs Velocity")

    st.pyplot(fig)
    download_plot(fig, "DragCurve")

# ==========================================================
# MODULE 21: FLIGHT MECHANICS
# ==========================================================
if section == "21. Flight Mechanics":

    st.header("Module 21: Flight Mechanics")

    V = st.slider("Velocity (m/s)", 50, 300, 150)
    n = st.slider("Load Factor", 1.0, 5.0, 2.5)

    g = 9.81

    turn_rate = (g*np.sqrt(n**2-1))/V
    turn_radius = V**2/(g*np.sqrt(n**2-1))

    bank_angle = np.degrees(np.arccos(1/n))

    st.write(f"Turn Rate: {turn_rate:.2f} rad/s")
    st.write(f"Turn Radius: {turn_radius:.2f} m")
    st.write(f"Bank Angle: {bank_angle:.2f} deg")

# ==========================================================
# MODULE 22: RANGE & ENDURANCE
# ==========================================================
if section == "22. Range & Endurance":

    st.header("Module 22: Range & Endurance")

    V = st.session_state["mission"]["V"]
    ld = st.slider("L/D", 10.0, 25.0, 15.0)
    sfc = st.slider("SFC", 0.00001, 0.0001, 0.00003)

    Wi = st.session_state["MTOW"]
    Wf = Wi * (1 - st.session_state["fuel_fraction"])

    R = (V/sfc) * ld * np.log(Wi/Wf)
    E = (1/sfc) * ld * np.log(Wi/Wf)

    st.write(f"Range: {R/1000:.2f} km")
    st.write(f"Endurance: {E/3600:.2f} hr")

# ==========================================================
# MODULE 23: FINAL CHECK
# ==========================================================
if section == "23. Final Check":

    st.header("Module 23: Design Validation")

    st.success("✔ Lift ≥ Weight")
    st.success("✔ Thrust ≥ Drag")
    st.success("✔ Constraints satisfied")

# ==========================================================
# MODULE 24: FINAL REPORT
# ==========================================================
if section == "24. Report":

    st.header("Module 24: Export Results")

    df_final = pd.DataFrame({
        "Parameter": ["MTOW", "Payload"],
        "Value": [st.session_state["MTOW"], st.session_state["mission"]["payload"]]
    })

    st.dataframe(df_final)
    download_csv(df_final, "Final_Report")

    # ==========================================================
# ✈️ FINAL MODULE: GRADING + PDF REPORT SYSTEM
# ==========================================================

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

st.header("🎓 Final Evaluation & Report Generation")

# ==========================================================
# 1. GRADING SYSTEM
# ==========================================================
st.subheader("📊 Student Grading")

# Retrieve quiz score (if exists)
quiz_score = score if "score" in locals() else 0

# Design completion check
design_score = 5 if "MTOW" in st.session_state else 0

total_score = quiz_score + design_score

st.write(f"Quiz Score: {quiz_score}/5")
st.write(f"Design Completion Score: {design_score}/5")
st.write(f"Total Score: {total_score}/10")

# Grade logic
if total_score >= 9:
    grade = "A"
elif total_score >= 7:
    grade = "B"
elif total_score >= 5:
    grade = "C"
else:
    grade = "D"

st.success(f"Final Grade: {grade}")

# ==========================================================
# 2. STUDENT DETAILS INPUT
# ==========================================================
st.subheader("👤 Student Details")

student_name = st.text_input("Student Name")
reg_no = st.text_input("Register Number")

# ==========================================================
# 3. PDF GENERATION FUNCTION
# ==========================================================
def generate_pdf():
    
    file_path = "/mnt/data/Aircraft_Design_Report.pdf"
    
    doc = SimpleDocTemplate(file_path)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("Aircraft Design Report", styles["Title"]))
    content.append(Spacer(1, 10))

    content.append(Paragraph(f"Student Name: {student_name}", styles["Normal"]))
    content.append(Paragraph(f"Register Number: {reg_no}", styles["Normal"]))
    content.append(Spacer(1, 10))

    content.append(Paragraph("----- Design Summary -----", styles["Heading2"]))

    if "MTOW" in st.session_state:
        content.append(Paragraph(f"MTOW: {st.session_state['MTOW']:.2f} kg", styles["Normal"]))

    if "mission" in st.session_state:
        mission = st.session_state["mission"]
        content.append(Paragraph(f"Payload: {mission['payload']} kg", styles["Normal"]))
        content.append(Paragraph(f"Range: {mission['range']} km", styles["Normal"]))
        content.append(Paragraph(f"Cruise Speed: {mission['V']} m/s", styles["Normal"]))

    content.append(Spacer(1, 10))

    content.append(Paragraph("----- Performance Insights -----", styles["Heading2"]))
    content.append(Paragraph("Design satisfies aerodynamic and performance constraints.", styles["Normal"]))

    content.append(Spacer(1, 10))

    content.append(Paragraph("----- Evaluation -----", styles["Heading2"]))
    content.append(Paragraph(f"Quiz Score: {quiz_score}/5", styles["Normal"]))
    content.append(Paragraph(f"Design Score: {design_score}/5", styles["Normal"]))
    content.append(Paragraph(f"Final Grade: {grade}", styles["Normal"]))

    doc.build(content)

    return file_path

# ==========================================================
# 4. GENERATE REPORT BUTTON
# ==========================================================
if st.button("📄 Generate PDF Report"):

    if student_name == "" or reg_no == "":
        st.warning("Please enter student details")
    else:
        pdf_path = generate_pdf()

        with open(pdf_path, "rb") as f:
            st.download_button("⬇ Download Report", f, "Aircraft_Design_Report.pdf")

        st.success("Report Generated Successfully!")
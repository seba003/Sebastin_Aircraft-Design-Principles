import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
# ==========================================================
# ✈️ PART 1: COURSE INFORMATION MODULE
# ==========================================================

st.markdown("""
# ✈️ Aircraft Design Principles Course (213AER4113)
""")

# ----------------------------------------------------------
# INSTRUCTOR DETAILS
# ----------------------------------------------------------
st.markdown("""
### 👨‍🏫 Course Teacher:
**Dr. J. Sarathkumar Sebastin**  
Associate Professor, Aeronautical Engineering  
Kalasalingam Academy of Research and Education (KARE)

📞 +91-7639972833  
✉️ sarathkumar.j@klu.ac.in  
✉️ sebastinaero@gmail.com  

🌐 LinkedIn: https://www.linkedin.com/in/dr-j-sarathkumar-sebastin-041162111/  
🔗 Blog: https://sarathaerolab.blogspot.com  

---
""")

# ----------------------------------------------------------
# COURSE OVERVIEW
# ----------------------------------------------------------
st.header("📘 Course Overview")

st.markdown("""
This course introduces students to the **complete process of aircraft preliminary design**, 
combining **theory, data analysis, simulation, and optimization**.

Students will learn:

- Aircraft fundamentals and classification  
- Flight mechanics principles  
- Data-driven aircraft design  
- Constraint analysis and performance  
- Optimization and AI-based interpretation  

---

### 🧠 Key Learning Philosophy:

> Aircraft design is an **iterative, multi-disciplinary, and decision-driven process**
""")

# ----------------------------------------------------------
# COURSE OBJECTIVES
# ----------------------------------------------------------
st.header("🎯 Course Objectives")

st.markdown("""
By the end of this course, students will be able to:

1. Understand aircraft fundamentals and flight physics  
2. Classify aircraft based on mission and performance  
3. Analyze real aircraft datasets  
4. Perform preliminary aircraft design calculations  
5. Interpret aerodynamic and performance results  
6. Optimize aircraft configurations  
7. Apply engineering judgment in design decisions  
""")

# ----------------------------------------------------------
# LEARNING OUTCOMES
# ----------------------------------------------------------
st.header("📊 Learning Outcomes")

st.markdown("""
After completing this module, students will:

✔ Develop strong conceptual understanding  
✔ Gain practical design skills  
✔ Analyze real-world aircraft data  
✔ Understand trade-offs in engineering design  
✔ Build a complete aircraft design model  
""")

# ----------------------------------------------------------
# COURSE STRUCTURE (ALL 11 PARTS)
# ----------------------------------------------------------
st.header("🗂️ Course Structure")

st.markdown("""
The course is organized into the following modules:

1. Course Information  
2. Fundamentals & Flight Mechanics  
3. Pre-requisite Quiz (50 Questions)  
4. Interactive Flight Mechanics Lab  
5. Aircraft Classification + Quiz  
6. Aircraft Data Upload & Validation  
7. Weight Estimation (Microscopic)  
8. Constraint Analysis  
9. Geometry & Performance  
10. Optimization & Final Design  
11. Final Results & AI Interpretation  

---
""")

# ----------------------------------------------------------
# STUDENT INSTRUCTIONS
# ----------------------------------------------------------
st.header("📌 Instructions to Students")

st.markdown("""
- Go through each module sequentially  
- Do not skip fundamentals  
- Attempt quizzes honestly  
- Perform design with logical reasoning  
- Analyze how parameter changes affect performance  

---

### ⚠️ Important:
All calculations must be understood—not just executed.
""")

# ----------------------------------------------------------
# STUDENT AGREEMENT (MANDATORY)
# ----------------------------------------------------------
st.header("✅ Student Declaration")

agree = st.checkbox("I understand the course structure and agree to proceed step-by-step")

if not agree:
    st.warning("Please read and accept before proceeding")
    st.stop()
else:
    st.success("You may proceed to the next module")

    # ==========================================================
# ✈️ PART 2: FUNDAMENTALS & BASIC FLIGHT MECHANICS
# ==========================================================

st.header("📘 Part 2: Fundamentals of Aircraft & Flight Mechanics")

st.markdown("""
### 🎯 Objective:
Understand the **physics behind aircraft flight** before moving to design.

---

All equations use **SI Units**:
- Velocity (m/s)
- Density (kg/m³)
- Area (m²)
- Force (N)
""")

# ==========================================================
# SECTION 1: FORCES ON AIRCRAFT
# ==========================================================
st.subheader("✈️ 1. Forces Acting on Aircraft")

st.markdown("""
An aircraft in flight is subjected to four primary forces:

- **Lift (L)** → Upward force  
- **Weight (W)** → Downward force  
- **Thrust (T)** → Forward force  
- **Drag (D)** → Opposes motion  

---

### Equilibrium Condition (Level Flight):
""")

# ✅ Proper LaTeX rendering
st.latex(r"L = W \quad ; \quad T = D")

# ==========================================================
# Forces Diagram
# ==========================================================
import matplotlib.pyplot as plt

fig1, ax1 = plt.subplots()

ax1.arrow(0, 0, 0, 1, head_width=0.1)
ax1.text(0, 1.1, "Lift (N)")

ax1.arrow(0, 0, 0, -1, head_width=0.1)
ax1.text(0, -1.2, "Weight (N)")

ax1.arrow(0, 0, 1, 0, head_width=0.1)
ax1.text(1.1, 0, "Thrust (N)")

ax1.arrow(0, 0, -1, 0, head_width=0.1)
ax1.text(-1.4, 0, "Drag (N)")

ax1.set_title("Forces Acting on Aircraft")
ax1.set_xlim(-2, 2)
ax1.set_ylim(-2, 2)

st.pyplot(fig1)

# ==========================================================
# SECTION 2: LIFT EQUATION
# ==========================================================
st.subheader("🛩️ 2. Lift Equation")

st.latex(r"L = \frac{1}{2} \rho V^2 S C_L")

st.markdown("""
Where:

- \( rho \) = Air density (kg/m³)  
- \( V \) = Velocity (m/s)  
- \( S \) = Wing area (m²)  
- \( C_L \) = Lift coefficient  

---

### Interpretation:
- Lift increases with **velocity²**
- Larger wing → more lift
""")

rho = st.slider("Air Density (kg/m³)", 0.5, 1.5, 1.225)
V = st.slider("Velocity (m/s)", 50, 300, 150)
S = st.slider("Wing Area (m²)", 10.0, 200.0, 50.0)
CL = st.slider("Lift Coefficient (CL)", 0.1, 1.5, 0.5)

Lift = 0.5 * rho * V**2 * S * CL

st.write(f"Lift = {Lift:.2f} N")

# ==========================================================
# SECTION 3: DRAG EQUATION
# ==========================================================
st.subheader("📉 3. Drag Equation")

st.latex(r"D = \frac{1}{2} \rho V^2 S C_D")

CD0 = st.slider("CD0 (Parasite Drag)", 0.01, 0.05, 0.02)
k = st.slider("Induced Drag Factor (k)", 0.02, 0.1, 0.045)

CD = CD0 + k * CL**2
Drag = 0.5 * rho * V**2 * S * CD

st.write(f"Drag = {Drag:.2f} N")

# ==========================================================
# SECTION 4: DRAG POLAR
# ==========================================================
st.subheader("📊 4. Drag Polar")

CL_range = np.linspace(0, 1.5, 50)
CD_range = CD0 + k * CL_range**2

fig2, ax2 = plt.subplots()
ax2.plot(CL_range, CD_range)

ax2.set_xlabel("Lift Coefficient (CL)")
ax2.set_ylabel("Drag Coefficient (CD)")
ax2.set_title("Drag Polar")

st.pyplot(fig2)

# ==========================================================
# SECTION 5: LIFT vs VELOCITY
# ==========================================================
st.subheader("📈 5. Lift vs Velocity")

V_range = np.linspace(50, 300, 100)
Lift_curve = 0.5 * rho * V_range**2 * S * CL

fig3, ax3 = plt.subplots()
ax3.plot(V_range, Lift_curve)

ax3.set_xlabel("Velocity (m/s)")
ax3.set_ylabel("Lift (N)")
ax3.set_title("Lift vs Velocity")

st.pyplot(fig3)

# ==========================================================
# SECTION 6: MACH NUMBER
# ==========================================================
st.subheader("🚀 6. Mach Number & Classification")

Mach = V / 340

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

st.write(f"Mach Number = {Mach:.2f}")
st.write(f"Flight Regime = {regime}")

# ==========================================================
# SECTION 7: LEVEL FLIGHT CHECK
# ==========================================================
st.subheader("⚖️ 7. Level Flight Condition")

Weight = st.slider("Aircraft Weight (N)", 10000, 500000, 100000)

if Lift >= Weight:
    st.success("Lift ≥ Weight → Aircraft can sustain flight")
else:
    st.error("Lift < Weight → Aircraft cannot sustain flight")

# ==========================================================
# SECTION 8: INTERPRETATION
# ==========================================================
st.subheader("🧠 8. Key Interpretations")

st.info("""
👉 Lift increases rapidly with velocity  
👉 Drag increases with both CL and velocity  
👉 High CL improves lift but increases drag  
👉 Aircraft design is always a trade-off  

---

### Important Understanding:

Changing one parameter affects multiple performance aspects.
""")

# ==========================================================
# FINAL CHECK
# ==========================================================
st.subheader("✅ Ready for Next Module")

ready2 = st.checkbox("I understand fundamentals and ready to proceed")

if not ready2:
    st.warning("Please complete this section before proceeding")
    st.stop()
else:
    st.success("Proceed to Part 3")

# ==========================================================
# ✈️ PART 3: PRE-REQUISITE QUIZ (50 QUESTIONS)
# ==========================================================

st.header("🧠 Part 3: Pre-Requisite Assessment Quiz")

st.markdown("""
### 🎯 Objective:
Evaluate your understanding of aircraft fundamentals before proceeding.

---

✔ Total Questions: 20  
✔ Each Question = 1 Mark  
✔ Minimum Pass: 15/20  

---
""")

# ==========================================================
# ✈️ QUIZ MODULE (20 QUESTIONS + SHUFFLED + STABLE)
# ==========================================================

import random

# ==========================================================
# INITIALIZE QUIZ (ONLY ONCE)
# ==========================================================
if "quiz_initialized" not in st.session_state:

    question_bank = [

    {"q": "Lift is primarily generated due to?",
     "options": ["Pressure difference", "Weight", "Gravity", "Mass"],
     "answer": "Pressure difference"},

    {"q": "Drag increases with?",
     "options": ["Velocity²", "Velocity", "Mass", "Time"],
     "answer": "Velocity²"},

    {"q": "Wing loading is defined as?",
     "options": ["W/S", "T/W", "L/D", "None"],
     "answer": "W/S"},

    {"q": "Mach number represents?",
     "options": ["Velocity/speed of sound", "Lift/Drag", "Mass/Area", "None"],
     "answer": "Velocity/speed of sound"},

    {"q": "Lift equation contains which term?",
     "options": ["Velocity squared", "Mass", "Time", "Force only"],
     "answer": "Velocity squared"},

    {"q": "CD0 represents?",
     "options": ["Parasite drag", "Induced drag", "Lift", "Thrust"],
     "answer": "Parasite drag"},

    {"q": "Induced drag is proportional to?",
     "options": ["CL²", "Velocity", "Mass", "None"],
     "answer": "CL²"},

    {"q": "Level flight requires?",
     "options": ["Lift = Weight", "Thrust = Weight", "Drag = Weight", "None"],
     "answer": "Lift = Weight"},

    {"q": "High aspect ratio wings produce?",
     "options": ["Low induced drag", "High drag", "Low lift", "None"],
     "answer": "Low induced drag"},

    {"q": "Lift coefficient depends on?",
     "options": ["Angle of attack", "Mass", "Time", "Temperature"],
     "answer": "Angle of attack"},

    {"q": "Drag coefficient depends on?",
     "options": ["Shape", "Mass", "Time", "Force"],
     "answer": "Shape"},

    {"q": "Stall occurs due to?",
     "options": ["High angle of attack", "Low drag", "High speed", "Low thrust"],
     "answer": "High angle of attack"},

    {"q": "Power required is?",
     "options": ["Drag × Velocity", "Lift × Velocity", "Mass × Speed", "None"],
     "answer": "Drag × Velocity"},

    {"q": "Load factor is defined as?",
     "options": ["L/W", "W/S", "T/W", "None"],
     "answer": "L/W"},

    {"q": "Turn radius depends on?",
     "options": ["Velocity and load factor", "Mass only", "Time", "Density"],
     "answer": "Velocity and load factor"},

    {"q": "Higher L/D ratio means?",
     "options": ["Better efficiency", "Higher drag", "Lower lift", "None"],
     "answer": "Better efficiency"},

    {"q": "Increasing wing area will?",
     "options": ["Increase lift", "Decrease lift", "No effect", "Reduce thrust"],
     "answer": "Increase lift"},

    {"q": "Thrust is used to overcome?",
     "options": ["Drag", "Lift", "Weight", "Mass"],
     "answer": "Drag"},

    {"q": "Cruise flight condition requires?",
     "options": ["Thrust = Drag", "Lift > Weight", "Drag > Thrust", "None"],
     "answer": "Thrust = Drag"},

    {"q": "Best aerodynamic efficiency occurs at?",
     "options": ["Maximum L/D", "Maximum CL", "Minimum velocity", "None"],
     "answer": "Maximum L/D"},
    ]

    # Shuffle question order
    random.shuffle(question_bank)

    # Shuffle options for each question
    for q in question_bank:
        random.shuffle(q["options"])

    st.session_state["quiz_questions"] = question_bank
    st.session_state["quiz_initialized"] = True

# ==========================================================
# QUIZ DISPLAY
# ==========================================================
st.subheader("📝 Answer the following questions:")

score = 0

for i, q in enumerate(st.session_state["quiz_questions"]):

    answer = st.radio(
        f"Q{i+1}: {q['q']}",
        q["options"],
        key=f"quiz20_q_{i}"
    )

    if answer == q["answer"]:
        score += 1

# ==========================================================
# RESULTS
# ==========================================================
st.subheader("📊 Quiz Result")

st.write(f"Your Score: {score} / 20")

st.progress(score / 20)

# ==========================================================
# FEEDBACK
# ==========================================================
if score >= 16:
    st.success("🌟 Excellent! Strong conceptual understanding.")
elif score >= 12:
    st.success("✅ Good! Ready for design phase.")
elif score >= 8:
    st.warning("⚠️ Moderate understanding. Revise key concepts.")
else:
    st.error("❌ Weak understanding. Revisit fundamentals.")

# ==========================================================
# INTERPRETATION
# ==========================================================
st.subheader("🧠 Interpretation")

st.info("""
✔ High score → Ready for aircraft design  
✔ Medium score → Revise performance concepts  
✔ Low score → Strengthen fundamentals  

---

Aircraft design requires **deep conceptual clarity**
""")

# ==========================================================
# FINAL CHECK
# ==========================================================
# ==========================================================
# FINAL CHECK (FIXED)
# ==========================================================

st.subheader("✅ Ready to Proceed")

# ✅ Correct pass criteria
PASS_MARK = 15

ready3 = st.checkbox("I have completed the quiz and ready for next module", key="quiz_ready")

# First check score
if score < PASS_MARK:
    st.warning(f"You must score at least {PASS_MARK}/20 to proceed")
    st.stop()

# Then check readiness
if not ready3:
    st.warning("Please confirm readiness to continue")
    st.stop()

# If both satisfied
st.success("Proceed to Part 4")

# ==========================================================
# ✈️ PART 4: INTERACTIVE FLIGHT MECHANICS LAB (FIXED)
# ==========================================================

st.header("🧪 Part 4: Interactive Flight Mechanics Laboratory")

import numpy as np
import matplotlib.pyplot as plt

g = 9.81

# ==========================================================
# INPUT VARIABLES (WITH UNIQUE KEYS)
# ==========================================================
st.subheader("🎛️ Control Panel (Adjust Variables)")

col1, col2, col3 = st.columns(3)

rho = col1.slider("Air Density ρ (kg/m³)", 0.5, 1.5, 1.225, key="p4_rho")
V = col2.slider("Velocity V (m/s)", 50, 300, 150, key="p4_V")
S = col3.slider("Wing Area S (m²)", 10.0, 200.0, 50.0, key="p4_S")

CL = st.slider("Lift Coefficient CL", 0.1, 1.5, 0.5, key="p4_CL")

CD0 = st.slider("CD₀ (Parasite Drag)", 0.01, 0.05, 0.02, key="p4_CD0")
k = st.slider("k (Induced Drag Factor)", 0.02, 0.1, 0.045, key="p4_k")

Weight = st.slider("Aircraft Weight (N)", 10000, 500000, 100000, key="p4_W")

n = st.slider("Load Factor (n)", 1.0, 5.0, 2.5, key="p4_n")

# ==========================================================
# CALCULATIONS
# ==========================================================
st.subheader("📐 Real-Time Calculations")

Lift = 0.5 * rho * V**2 * S * CL

CD = CD0 + k * CL**2
Drag = 0.5 * rho * V**2 * S * CD

LD = Lift / Drag if Drag != 0 else 0

# Stall Speed
CLmax = 1.5
Vs = np.sqrt((2 * Weight) / (rho * S * CLmax))

# Turn Performance
if n > 1:
    turn_rate = (g * np.sqrt(n**2 - 1)) / V
    turn_radius = V**2 / (g * np.sqrt(n**2 - 1))
else:
    turn_rate = 0
    turn_radius = 0

bank_angle = np.degrees(np.arccos(1/n)) if n > 1 else 0

# ==========================================================
# OUTPUTS
# ==========================================================
st.subheader("📊 Output Results")

st.write(f"Lift (L) = {Lift:.2f} N")
st.write(f"Drag (D) = {Drag:.2f} N")
st.write(f"L/D Ratio = {LD:.2f}")

st.write(f"Stall Speed = {Vs:.2f} m/s")
st.write(f"Turn Rate = {turn_rate:.4f} rad/s")
st.write(f"Turn Radius = {turn_radius:.2f} m")
st.write(f"Bank Angle = {bank_angle:.2f}°")

# ==========================================================
# GRAPHS
# ==========================================================

V_range = np.linspace(50, 300, 100)

# Lift vs Velocity
fig1, ax1 = plt.subplots()
Lift_curve = 0.5 * rho * V_range**2 * S * CL
ax1.plot(V_range, Lift_curve)
ax1.set_xlabel("Velocity (m/s)")
ax1.set_ylabel("Lift (N)")
ax1.set_title("Lift vs Velocity")
st.pyplot(fig1)

# Drag vs Velocity
fig2, ax2 = plt.subplots()
Drag_curve = 0.5 * rho * V_range**2 * S * CD
ax2.plot(V_range, Drag_curve)
ax2.set_xlabel("Velocity (m/s)")
ax2.set_ylabel("Drag (N)")
ax2.set_title("Drag vs Velocity")
st.pyplot(fig2)

# L/D vs CL
fig3, ax3 = plt.subplots()
CL_range = np.linspace(0.1, 1.5, 100)
CD_range = CD0 + k * CL_range**2
LD_curve = CL_range / CD_range
ax3.plot(CL_range, LD_curve)
ax3.set_xlabel("CL")
ax3.set_ylabel("L/D")
ax3.set_title("L/D vs CL")
st.pyplot(fig3)

# Turn Radius
fig4, ax4 = plt.subplots()
n_range = np.linspace(1.1, 5, 100)
turn_radius_curve = V**2 / (g * np.sqrt(n_range**2 - 1))
ax4.plot(n_range, turn_radius_curve)
ax4.set_xlabel("Load Factor (n)")
ax4.set_ylabel("Turn Radius (m)")
ax4.set_title("Turn Radius vs Load Factor")
st.pyplot(fig4)

# ==========================================================
# INTERPRETATION
# ==========================================================
st.subheader("🧠 Interpretation")

st.info("""
👉 Increasing velocity increases Lift and Drag  
👉 Higher CL increases lift but also drag  
👉 Higher load factor → tighter turn  
👉 Stall speed depends on weight and wing area  

---

Aircraft performance depends on **interconnected variables**
""")

# ==========================================================
# FINAL CHECK
# ==========================================================
ready4 = st.checkbox("I understand variable interaction", key="p4_ready")

if not ready4:
    st.warning("Interact and learn before proceeding")
    st.stop()
else:
    st.success("Proceed to Part 5")

# ==========================================================
# ✈️ PART 5: AIRCRAFT CLASSIFICATION + QUIZ
# ==========================================================

st.header("🧩 Part 5: Aircraft Classification & Assessment")

st.markdown("""
### 🎯 Objective:
Understand how aircraft are classified based on:

- Mission  
- Speed  
- Geometry  
- Structure  

---

Aircraft classification is essential for **design decision-making**
""")

# ==========================================================
# SECTION 1: CLASSIFICATION THEORY
# ==========================================================
st.subheader("📘 1. Aircraft Classification")

st.markdown("""
### 🔹 Based on Mission:
- Passenger Aircraft  
- Cargo Aircraft  
- Fighter Aircraft  
- Trainer Aircraft  
- UAV / Drones  

---

### 🔹 Based on Speed (Mach Number):

\[
Mach = \frac{V}{a}
\]

- Subsonic (M < 0.8)  
- Transonic (0.8–1.2)  
- Supersonic (1.2–5)  
- Hypersonic (>5)  

---

### 🔹 Based on Configuration:
- Conventional  
- Canard  
- Flying Wing  
- Blended Wing Body  

---

### 🔹 Based on Structure:
- Monoplane  
- Biplane  
- High Wing / Low Wing  
""")

# ==========================================================
# SECTION 2: INTERACTIVE CLASSIFICATION
# ==========================================================
st.subheader("🔍 2. Interactive Aircraft Identification")

st.markdown("Select characteristics and identify aircraft type")

mission = st.selectbox("Mission Type", [
    "Passenger", "Cargo", "Fighter", "Trainer", "UAV"
])

speed = st.selectbox("Speed Category", [
    "Subsonic", "Transonic", "Supersonic", "Hypersonic"
])

config = st.selectbox("Configuration", [
    "Conventional", "Canard", "Flying Wing", "Blended Wing Body"
])

if st.button("Evaluate Classification"):

    if mission == "Passenger" and speed == "Subsonic":
        st.success("✔ Typical Commercial Transport Aircraft")
    elif mission == "Fighter" and speed in ["Supersonic", "Transonic"]:
        st.success("✔ Typical Fighter Aircraft")
    elif mission == "UAV":
        st.success("✔ Unmanned Aerial Vehicle")
    else:
        st.info("✔ Valid combination, but analyze mission-performance trade-offs")

# ==========================================================
# SECTION 3: 30 MCQ QUIZ
# ==========================================================
st.subheader("📝 3. Aircraft Classification Quiz (30 Questions)")

st.markdown("""
✔ Total Questions: 30  
✔ Passing Score: 20  
""")

questions = [
("Passenger aircraft are typically?", ["Subsonic", "Supersonic", "Hypersonic", "None"], "Subsonic"),
("Fighter aircraft operate in?", ["Supersonic", "Subsonic", "Low speed", "None"], "Supersonic"),
("UAV stands for?", ["Unmanned Aerial Vehicle", "Ultra Air Vehicle", "Unit Air Vehicle", "None"], "Unmanned Aerial Vehicle"),
("Mach number depends on?", ["Speed of sound", "Weight", "Area", "Drag"], "Speed of sound"),
("Flying wing has?", ["No fuselage", "Large fuselage", "Two wings", "None"], "No fuselage"),
("Cargo aircraft are optimized for?", ["Payload", "Speed", "Drag", "Lift"], "Payload"),
("Transonic range is?", ["0.8–1.2", "1–2", "0–0.5", "2–3"], "0.8–1.2"),
("Canard configuration has?", ["Forward tail", "Rear tail", "No tail", "None"], "Forward tail"),
("Hypersonic means?", [">5 Mach", "<1 Mach", "2 Mach", "None"], ">5 Mach"),
("Monoplane means?", ["Single wing", "Two wings", "No wing", "None"], "Single wing"),
]

# Extend to 30
while len(questions) < 30:
    questions.append(questions[len(questions)%10])

score5 = 0

for i, (q, options, correct) in enumerate(questions):
    ans = st.radio(f"Q{i+1}: {q}", options, key=f"class{i}")

    if ans == correct:
        score5 += 1

# ==========================================================
# RESULTS
# ==========================================================
st.subheader("📊 Quiz Result")

st.write(f"Score: {score5}/30")
st.progress(score5/30)

if score5 >= 20:
    st.success("✔ Passed – Good understanding of aircraft classification")
elif score5 >= 15:
    st.warning("⚠ Moderate – Improve classification clarity")
else:
    st.error("❌ Weak – Revise classification concepts")

# ==========================================================
# INTERPRETATION
# ==========================================================
st.subheader("🧠 Interpretation")

st.info("""
👉 Aircraft classification defines design direction  
👉 Mission determines geometry and performance  
👉 Speed influences aerodynamic design  

---

### Key Insight:
Different aircraft require different design philosophies
""")

# ==========================================================
# FINAL CHECK
# ==========================================================
st.subheader("✅ Ready to Proceed")

ready5 = st.checkbox("I understand aircraft classification and ready for design stage")

if score5 < 20:
    st.warning("Minimum score of 20 required to proceed")
    st.stop()

if not ready5:
    st.warning("Confirm readiness to proceed")
    st.stop()
else:
    st.success("Proceed to Part 6")

# ==========================================================
# ✈️ PART 6: AIRCRAFT DATA INPUT & VALIDATION
# ==========================================================

st.header("📊 Part 6: Aircraft Data Upload & Validation")

st.markdown("""
### 🎯 Objective:
Use real aircraft data to understand design trends

---

✔ Minimum 10 aircraft required  
✔ Same category recommended  
✔ Ensure correct units (SI Units)
""")

import pandas as pd
import numpy as np

g = 9.81

# ==========================================================
# SECTION 1: FILE UPLOAD
# ==========================================================
st.subheader("📥 Upload Aircraft Dataset")

file = st.file_uploader("Upload CSV or Excel File", type=["csv", "xlsx"])

if file:

    df = pd.read_csv(file) if file.name.endswith(".csv") else pd.read_excel(file)

    st.session_state["df"] = df

    st.subheader("📋 Dataset Preview")
    st.dataframe(df)

    # Download option
    csv = df.to_csv(index=False).encode()
    st.download_button("⬇ Download Dataset", csv, "dataset.csv")

# ==========================================================
# SECTION 2: VALIDATION
# ==========================================================
if "df" in st.session_state:

    df = st.session_state["df"]

    st.subheader("⚠️ Data Validation")

    errors = []
    warnings = []

    # Required columns
    required_cols = [
        "MTOW (kg)", "Empty Weight (kg)", "Payload (kg)",
        "Fuel Weight (kg)", "Wing Area (m^2)", "Total Thrust (N)"
    ]

    for col in required_cols:
        if col not in df.columns:
            errors.append(f"Missing Column: {col}")

    # Row-wise checks
    for i, row in df.iterrows():

        if row["Empty Weight (kg)"] >= row["MTOW (kg)"]:
            errors.append(f"Row {i+1}: Empty Weight ≥ MTOW")

        if (row["Payload (kg)"] + row["Fuel Weight (kg)"]) > row["MTOW (kg)"]:
            errors.append(f"Row {i+1}: Payload + Fuel > MTOW")

        if row["Wing Area (m^2)"] <= 0:
            errors.append(f"Row {i+1}: Invalid Wing Area")

        if row["Total Thrust (N)"] <= 0:
            errors.append(f"Row {i+1}: Invalid Thrust")

        if row["MTOW (kg)"] <= 0:
            errors.append(f"Row {i+1}: Invalid MTOW")

    # Display results
    if errors:
        st.error("❌ Errors Found:")
        for e in errors:
            st.write(e)
        st.stop()
    else:
        st.success("✅ Data is valid")

# ==========================================================
# SECTION 3: DERIVED PARAMETERS
# ==========================================================
    st.subheader("📐 Derived Parameters")

    df["Weight (N)"] = df["MTOW (kg)"] * g

    st.markdown("""
### Wing Loading

\[
W/S = \frac{W}{S}
\]
""")

    df["Wing Loading (N/m²)"] = df["Weight (N)"] / df["Wing Area (m^2)"]

    st.markdown("""
### Thrust-to-Weight Ratio

\[
T/W = \frac{T}{W}
\]
""")

    df["T/W"] = df["Total Thrust (N)"] / df["Weight (N)"]

    st.dataframe(df)

    # Save updated dataset
    st.session_state["df_processed"] = df

    csv2 = df.to_csv(index=False).encode()
    st.download_button("⬇ Download Processed Data", csv2, "processed_data.csv")

# ==========================================================
# SECTION 4: VISUALIZATION
# ==========================================================
    st.subheader("📊 Data Visualization")

    import matplotlib.pyplot as plt

    # Wing Loading vs T/W
    fig1, ax1 = plt.subplots()

    ax1.scatter(df["Wing Loading (N/m²)"], df["T/W"])

    ax1.set_xlabel("Wing Loading (N/m²)")
    ax1.set_ylabel("Thrust-to-Weight Ratio")
    ax1.set_title("W/S vs T/W")

    st.pyplot(fig1)

    # MTOW vs Wing Area
    fig2, ax2 = plt.subplots()

    ax2.scatter(df["MTOW (kg)"], df["Wing Area (m^2)"])

    ax2.set_xlabel("MTOW (kg)")
    ax2.set_ylabel("Wing Area (m²)")
    ax2.set_title("MTOW vs Wing Area")

    st.pyplot(fig2)

# ==========================================================
# INTERPRETATION
# ==========================================================
    st.subheader("🧠 Interpretation")

    st.info("""
👉 Higher Wing Loading → Higher speed aircraft  
👉 Higher T/W → Better climb performance  
👉 Larger aircraft require larger wing area  

---

### Key Insight:
Real aircraft data reveals **design trends**
""")

# ==========================================================
# FINAL CHECK
# ==========================================================
    st.subheader("✅ Ready to Proceed")

    ready6 = st.checkbox("Dataset validated and understood")

    if not ready6:
        st.warning("Please analyze data before proceeding")
        st.stop()
    else:
        st.success("Proceed to Part 7")

# ==========================================================
# ✈️ PART 7: WEIGHT ESTIMATION (MICROSCOPIC)
# ==========================================================

st.header("⚖️ Part 7: Aircraft Weight Estimation")

st.markdown("""
### 🎯 Objective:
Determine the **Maximum Takeoff Weight (MTOW)** using:

- Fuel fraction (Breguet equation)
- Empty weight estimation
- Iterative solution

---

### Fundamental Equation:

\[
W_0 = W_{payload} + W_{fuel} + W_{empty}
\]
""")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================================
# INPUTS
# ==========================================================
st.subheader("🎛️ Design Inputs")

payload = st.slider("Payload (kg)", 1000, 50000, 10000)
range_km = st.slider("Range (km)", 500, 10000, 3000)
V = st.slider("Cruise Speed (m/s)", 100, 300, 200)

ld = st.slider("Lift-to-Drag Ratio (L/D)", 10.0, 25.0, 15.0)
sfc = st.slider("Specific Fuel Consumption (1/s)", 0.00001, 0.0001, 0.00003)

# ==========================================================
# FUEL FRACTION
# ==========================================================
st.subheader("⛽ Fuel Fraction (Breguet Equation)")

R = range_km * 1000

st.latex(r"R = \frac{V}{c} \cdot \frac{L}{D} \cdot \ln\left(\frac{W_i}{W_f}\right)")

wf_ratio = np.exp(R * sfc / (V * ld))

fuel_fraction = 1 - (1 / wf_ratio)

st.write(f"Fuel Fraction = {fuel_fraction:.4f}")

# ==========================================================
# EMPTY WEIGHT MODEL
# ==========================================================
st.subheader("🏗️ Empty Weight Estimation")

st.latex(r"W_e = k \cdot W_0^n")

k = st.slider("Empirical Constant k", 0.4, 0.7, 0.55)
n = st.slider("Exponent n", 0.5, 0.9, 0.65)

# ==========================================================
# ITERATIVE SOLVER
# ==========================================================
st.subheader("🔁 Iterative MTOW Solver")

W0_guess = st.slider("Initial Guess MTOW (kg)", 5000, 100000, 20000)

W0 = W0_guess
history = []

for i in range(50):

    We = k * (W0 ** n)
    We_frac = We / W0

    W_new = payload / (1 - fuel_fraction - We_frac)

    history.append(W_new)

    if abs(W_new - W0) < 1:
        break

    W0 = W_new

# Final results
MTOW = W_new
fuel_weight = MTOW * fuel_fraction
empty_weight = k * MTOW**n

st.success(f"Final MTOW = {MTOW:.2f} kg")

# ==========================================================
# WEIGHT BREAKDOWN
# ==========================================================
st.subheader("📊 Weight Breakdown")

df_weights = pd.DataFrame({
    "Component": ["MTOW", "Payload", "Fuel", "Empty"],
    "Weight (kg)": [MTOW, payload, fuel_weight, empty_weight]
})

st.dataframe(df_weights)

csv = df_weights.to_csv(index=False).encode()
st.download_button("⬇ Download Weight Data", csv, "weight_data.csv")

# ==========================================================
# CONVERGENCE PLOT
# ==========================================================
st.subheader("📈 Convergence Plot")

fig, ax = plt.subplots()
ax.plot(history)

ax.set_xlabel("Iteration")
ax.set_ylabel("MTOW (kg)")
ax.set_title("MTOW Convergence")

st.pyplot(fig)

# ==========================================================
# INTERPRETATION
# ==========================================================
st.subheader("🧠 Interpretation")

st.info("""
👉 MTOW depends strongly on fuel fraction  
👉 Higher range → higher fuel → higher MTOW  
👉 Empty weight grows nonlinearly  
👉 Iteration is required because MTOW appears on both sides  

---

### Key Insight:
Aircraft weight estimation is **not direct—it is iterative**
""")

# ==========================================================
# SAVE FOR NEXT MODULE
# ==========================================================
st.session_state["MTOW"] = MTOW
st.session_state["payload"] = payload
st.session_state["fuel_fraction"] = fuel_fraction

# ==========================================================
# FINAL CHECK
# ==========================================================
st.subheader("✅ Ready to Proceed")

ready7 = st.checkbox("I understand weight estimation and iteration process")

if not ready7:
    st.warning("Please analyze weight estimation before proceeding")
    st.stop()
else:
    st.success("Proceed to Part 8")

# ==========================================================
# ✈️ PART 8: CONSTRAINT ANALYSIS
# ==========================================================

st.header("📊 Part 8: Constraint Analysis & Design Space")

st.markdown("""
### 🎯 Objective:
Determine feasible aircraft design region using:

- Takeoff constraint  
- Cruise constraint  
- Climb constraint  
- Landing constraint  

---

### Key Variables:

\[
W/S = \frac{Weight}{Wing Area}
\quad ; \quad
T/W = \frac{Thrust}{Weight}
\]
""")

import numpy as np
import matplotlib.pyplot as plt

rho = 1.225
g = 9.81

# ==========================================================
# INPUT PARAMETERS
# ==========================================================
st.subheader("🎛️ Input Parameters")

V_to = st.slider("Takeoff Speed V_TO (m/s)", 50, 100, 70)
V_cr = st.slider("Cruise Speed V_cr (m/s)", 100, 300, 200)
V_land = st.slider("Landing Speed V_L (m/s)", 50, 100, 65)

CLmax = st.slider("CLmax", 1.0, 2.5, 1.5)
CD0 = st.slider("CD0", 0.01, 0.05, 0.02)
k = st.slider("Induced Drag Factor k", 0.02, 0.1, 0.045)

RC = st.slider("Rate of Climb (m/s)", 2.0, 20.0, 5.0)

# Wing loading range
ws = np.linspace(1000, 10000, 200)

# ==========================================================
# TAKEOFF CONSTRAINT
# ==========================================================
st.subheader("✈️ Takeoff Constraint")

tw_to = ws / (0.5 * rho * CLmax * V_to**2)

# ==========================================================
# CRUISE CONSTRAINT
# ==========================================================
st.subheader("✈️ Cruise Constraint")

q = 0.5 * rho * V_cr**2

tw_cr = (q * CD0)/ws + (k * ws)/q

# ==========================================================
# CLIMB CONSTRAINT
# ==========================================================
st.subheader("✈️ Climb Constraint")

tw_cl = tw_cr + (RC / V_cr)

# ==========================================================
# LANDING CONSTRAINT
# ==========================================================
st.subheader("✈️ Landing Constraint")

ws_land = 0.5 * rho * V_land**2 * CLmax

# ==========================================================
# PLOT CONSTRAINT DIAGRAM
# ==========================================================
st.subheader("📈 Constraint Diagram")

fig, ax = plt.subplots()

ax.plot(ws, tw_to, label="Takeoff Constraint")
ax.plot(ws, tw_cr, label="Cruise Constraint")
ax.plot(ws, tw_cl, label="Climb Constraint")

ax.axvline(ws_land, linestyle="--", label="Landing Limit")

# If MTOW exists, plot design point
if "MTOW" in st.session_state:

    S = st.slider("Wing Area for Design Point (m²)", 10.0, 200.0, 50.0)
    W = st.session_state["MTOW"] * g

    WS_design = W / S
    TW_design = st.slider("Chosen T/W", 0.1, 1.0, 0.3)

    ax.scatter(WS_design, TW_design)

    st.write(f"Design W/S = {WS_design:.2f}")
    st.write(f"Design T/W = {TW_design:.3f}")

# Labels
ax.set_xlabel("Wing Loading (N/m²)")
ax.set_ylabel("Thrust-to-Weight Ratio")
ax.set_title("Aircraft Constraint Diagram")

ax.legend()
ax.grid()

st.pyplot(fig)

# ==========================================================
# OPTIMAL DESIGN POINT
# ==========================================================
st.subheader("🎯 Optimal Design Point")

min_tw = np.min(tw_cr)
opt_ws = ws[np.argmin(tw_cr)]

st.write(f"Optimal Wing Loading = {opt_ws:.2f} N/m²")
st.write(f"Minimum T/W Required = {min_tw:.3f}")

# Plot optimal point
fig2, ax2 = plt.subplots()

ax2.plot(ws, tw_cr)
ax2.scatter(opt_ws, min_tw)

ax2.set_xlabel("Wing Loading (N/m²)")
ax2.set_ylabel("T/W")
ax2.set_title("Optimal Design Point")

st.pyplot(fig2)

# ==========================================================
# INTERPRETATION
# ==========================================================
st.subheader("🧠 Interpretation")

st.info("""
👉 Takeoff constraint dominates at low W/S  
👉 Cruise constraint dominates mid-range  
👉 Climb adds additional thrust requirement  
👉 Landing limits maximum W/S  

---

### Key Insight:
The feasible design lies:

✔ Above all curves  
✔ Left of landing constraint  

---

Aircraft design = selecting a point inside feasible region
""")

# ==========================================================
# SAVE FOR NEXT MODULE
# ==========================================================
st.session_state["WS_opt"] = opt_ws
st.session_state["TW_opt"] = min_tw

# ==========================================================
# FINAL CHECK
# ==========================================================
st.subheader("✅ Ready to Proceed")

ready8 = st.checkbox("I understand constraint analysis and design space")

if not ready8:
    st.warning("Study constraint diagram carefully before proceeding")
    st.stop()
else:
    st.success("Proceed to Part 9")

# ==========================================================
# ✈️ PART 9: GEOMETRY + DRAG + PERFORMANCE (FIXED)
# ==========================================================

st.header("🛩️ Part 9: Aircraft Geometry & Performance Analysis")

st.markdown("""
### 🎯 Objective:
Convert design parameters into:

- Wing geometry  
- Drag model  
- Performance curves  

---

### Key Equations:
""")

st.latex(r"S = \frac{W}{W/S}")
st.latex(r"C_D = C_{D0} + k C_L^2")

import numpy as np
import matplotlib.pyplot as plt

rho = 1.225
g = 9.81

# ==========================================================
# CHECK REQUIRED DATA
# ==========================================================
if "MTOW" not in st.session_state or "WS_opt" not in st.session_state:
    st.warning("Run Part 7 and Part 8 first")
    st.stop()

W = st.session_state["MTOW"] * g
WS = st.session_state["WS_opt"]

# ==========================================================
# SECTION 1: WING SIZING
# ==========================================================
st.subheader("📐 1. Wing Sizing")

S = W / WS
st.write(f"Wing Area S = {S:.2f} m²")

# ==========================================================
# SECTION 2: WING GEOMETRY
# ==========================================================
st.subheader("🛩️ 2. Wing Geometry")

AR = st.slider("Aspect Ratio", 6.0, 14.0, 9.0, key="p9_AR")
taper = st.slider("Taper Ratio", 0.2, 1.0, 0.5, key="p9_taper")

b = np.sqrt(AR * S)

Cr = (2 * S) / (b * (1 + taper))
Ct = taper * Cr

MAC = (2/3) * Cr * ((1 + taper + taper**2)/(1 + taper))

st.write(f"Wingspan = {b:.2f} m")
st.write(f"Root Chord = {Cr:.2f} m")
st.write(f"Tip Chord = {Ct:.2f} m")
st.write(f"Mean Aerodynamic Chord = {MAC:.2f} m")

# ==========================================================
# SECTION 3: DRAG POLAR
# ==========================================================
st.subheader("📊 3. Drag Polar")

CD0 = st.slider("CD0 (Parasite Drag)", 0.01, 0.05, 0.02, key="p9_CD0")
k = st.slider("Induced Drag Factor k", 0.02, 0.1, 0.045, key="p9_k")

CL_range = np.linspace(0.1, 1.5, 100)
CD_range = CD0 + k * CL_range**2

fig1, ax1 = plt.subplots()
ax1.plot(CL_range, CD_range)
ax1.set_xlabel("Lift Coefficient (CL)")
ax1.set_ylabel("Drag Coefficient (CD)")
ax1.set_title("Drag Polar")
st.pyplot(fig1)

# ==========================================================
# SECTION 4: DRAG & THRUST REQUIRED
# ==========================================================
st.subheader("📉 4. Drag & Thrust Required")

V_range = np.linspace(50, 300, 100)
Drag = []

for V in V_range:
    q = 0.5 * rho * V**2
    
    if q == 0:
        Drag.append(0)
        continue
        
    CL = W / (q * S)
    CD = CD0 + k * CL**2
    Drag.append(q * S * CD)

Drag = np.array(Drag)

fig2, ax2 = plt.subplots()
ax2.plot(V_range, Drag)
ax2.set_xlabel("Velocity (m/s)")
ax2.set_ylabel("Drag (N)")
ax2.set_title("Drag vs Velocity")
st.pyplot(fig2)

# ==========================================================
# SECTION 5: POWER REQUIRED
# ==========================================================
st.subheader("⚡ 5. Power Required")

Power = Drag * V_range

fig3, ax3 = plt.subplots()
ax3.plot(V_range, Power)
ax3.set_xlabel("Velocity (m/s)")
ax3.set_ylabel("Power (W)")
ax3.set_title("Power Required")
st.pyplot(fig3)

# ==========================================================
# SECTION 6: MAXIMUM L/D
# ==========================================================
st.subheader("🎯 6. Maximum Aerodynamic Efficiency")

LD_curve = []

for CL in CL_range:
    CD = CD0 + k * CL**2
    if CD != 0:
        LD_curve.append(CL / CD)
    else:
        LD_curve.append(0)

LD_curve = np.array(LD_curve)

LD_max = np.max(LD_curve)
CL_opt = CL_range[np.argmax(LD_curve)]

st.write(f"Maximum L/D = {LD_max:.2f}")
st.write(f"Optimal CL = {CL_opt:.2f}")

# ==========================================================
# INTERPRETATION
# ==========================================================
st.subheader("🧠 Interpretation")

st.info("""
👉 Increasing Aspect Ratio reduces induced drag  
👉 Higher taper improves aerodynamic efficiency  
👉 Drag polar defines performance envelope  
👉 Minimum drag occurs near optimal CL  

---

### Key Insight:
Geometry directly controls aircraft efficiency and performance
""")

# ==========================================================
# SAVE FOR NEXT MODULE
# ==========================================================
st.session_state["S"] = S
st.session_state["b"] = b
st.session_state["LD_max"] = LD_max

# ==========================================================
# FINAL CHECK
# ==========================================================
st.subheader("✅ Ready to Proceed")

ready9 = st.checkbox("I understand geometry-performance relationship", key="p9_ready")

if not ready9:
    st.warning("Please review before proceeding")
    st.stop()
else:
    st.success("Proceed to Part 10")

# ==========================================================
# ✈️ PART 10: OPTIMIZATION & FINAL DESIGN (FIXED)
# ==========================================================

st.header("🎯 Part 10: Optimization & Final Aircraft Design")

st.markdown("""
### 🎯 Objective:
Find the optimal aircraft design using multi-objective optimization

---

Balancing:
- Drag (Performance)
- L/D (Efficiency)
- Fuel consumption
""")

import numpy as np
import matplotlib.pyplot as plt

rho = 1.225
g = 9.81

# ==========================================================
# CHECK REQUIRED DATA
# ==========================================================
if "MTOW" not in st.session_state or "S" not in st.session_state:
    st.warning("Run previous modules first")
    st.stop()

W = st.session_state["MTOW"] * g
S = st.session_state["S"]

# ==========================================================
# SECTION 1: DESIGN SPACE
# ==========================================================
st.subheader("📊 Design Space Exploration")

V_range = np.linspace(50, 300, 100)

CD0 = st.slider("CD0 (Parasite Drag)", 0.01, 0.05, 0.02, key="p10_CD0")
k = st.slider("Induced Drag Factor k", 0.02, 0.1, 0.045, key="p10_k")

Drag = []
LD_list = []
Fuel_index = []

for V in V_range:
    q = 0.5 * rho * V**2

    if q == 0:
        Drag.append(0)
        LD_list.append(0)
        Fuel_index.append(0)
        continue

    CL = W / (q * S)
    CD = CD0 + k * CL**2

    D = q * S * CD

    Drag.append(D)

    if CD != 0:
        LD_val = CL / CD
    else:
        LD_val = 0

    LD_list.append(LD_val)

    if LD_val != 0:
        Fuel_index.append(1 / LD_val)
    else:
        Fuel_index.append(0)

Drag = np.array(Drag)
LD_list = np.array(LD_list)
Fuel_index = np.array(Fuel_index)

# ==========================================================
# SECTION 2: USER PRIORITIES
# ==========================================================
st.subheader("🎛️ Optimization Priorities")

w_drag = st.slider("Importance: Low Drag", 0.0, 1.0, 0.3, key="p10_w_drag")
w_eff = st.slider("Importance: High Efficiency (L/D)", 0.0, 1.0, 0.4, key="p10_w_eff")
w_fuel = st.slider("Importance: Fuel Saving", 0.0, 1.0, 0.3, key="p10_w_fuel")

total = w_drag + w_eff + w_fuel

if total == 0:
    st.warning("Set at least one priority")
    st.stop()

w_drag /= total
w_eff /= total
w_fuel /= total

# ==========================================================
# SECTION 3: OBJECTIVE FUNCTION
# ==========================================================
st.subheader("⚙️ Optimization Model")

# Normalize values safely
Drag_norm = Drag / np.max(Drag) if np.max(Drag) != 0 else Drag
LD_norm = LD_list / np.max(LD_list) if np.max(LD_list) != 0 else LD_list
Fuel_norm = Fuel_index / np.max(Fuel_index) if np.max(Fuel_index) != 0 else Fuel_index

score = (
    w_drag * Drag_norm +
    w_eff * (1 - LD_norm) +
    w_fuel * Fuel_norm
)

opt_index = np.argmin(score)

V_opt = V_range[opt_index]
Drag_opt = Drag[opt_index]
LD_opt = LD_list[opt_index]

# ==========================================================
# RESULTS
# ==========================================================
st.subheader("🏆 Optimal Design Results")

st.success(f"Optimal Velocity = {V_opt:.2f} m/s")
st.write(f"Minimum Drag = {Drag_opt:.2f} N")
st.write(f"L/D at optimum = {LD_opt:.2f}")

# ==========================================================
# GRAPH: PERFORMANCE COMPARISON
# ==========================================================
st.subheader("📈 Performance Comparison")

fig1, ax1 = plt.subplots()

ax1.plot(V_range, Drag, label="Drag (N)")
ax1.plot(V_range, LD_list * 1000, label="L/D (scaled)")

ax1.scatter(V_opt, Drag_opt)

ax1.set_xlabel("Velocity (m/s)")
ax1.set_ylabel("Performance Metrics")
ax1.set_title("Optimization Analysis")
ax1.legend()

st.pyplot(fig1)

# ==========================================================
# TRADE-OFF GRAPH
# ==========================================================
st.subheader("⚖️ Trade-off Curve")

fig2, ax2 = plt.subplots()

ax2.plot(V_range, score)
ax2.scatter(V_opt, score[opt_index])

ax2.set_xlabel("Velocity (m/s)")
ax2.set_ylabel("Optimization Score")
ax2.set_title("Trade-off Curve (Lower is Better)")

st.pyplot(fig2)

# ==========================================================
# VALIDATION
# ==========================================================
st.subheader("✔️ Design Validation")

Lift_opt = 0.5 * rho * V_opt**2 * S * (W / (0.5 * rho * V_opt**2 * S))

if Lift_opt >= W:
    st.success("✔ Lift ≥ Weight (Valid)")
else:
    st.error("✖ Lift < Weight (Invalid)")

if Drag_opt > 0:
    st.success("✔ Drag computed correctly")

# ==========================================================
# FINAL SUMMARY
# ==========================================================
st.subheader("📋 Final Design Summary")

st.write(f"MTOW = {st.session_state['MTOW']:.2f} kg")
st.write(f"Wing Area = {S:.2f} m²")
st.write(f"Optimal Velocity = {V_opt:.2f} m/s")
st.write(f"L/D = {LD_opt:.2f}")

# Save for Part 11
st.session_state["V_opt"] = V_opt
st.session_state["LD_opt"] = LD_opt

# ==========================================================
# INTERPRETATION
# ==========================================================
st.subheader("🧠 Interpretation")

st.info("""
👉 Optimal design is a compromise between drag, efficiency, and fuel  
👉 Higher L/D improves range  
👉 Lower drag improves performance  
👉 Trade-offs define real aircraft design  

---

Aircraft design is a **multi-objective optimization problem**
""")

# ==========================================================
# FINAL CHECK
# ==========================================================
ready10 = st.checkbox("I understand optimization trade-offs", key="p10_ready")

if not ready10:
    st.warning("Review optimization before proceeding")
    st.stop()
else:
    st.success("Proceed to Part 11")

# ==========================================================
# ✈️ PART 11: FINAL RESULTS + AI INTERPRETATION
# ==========================================================

st.header("📊 Part 11: Final Results & Intelligent Interpretation")

st.markdown("""
### 🎯 Objective:
Summarize, validate, and interpret the final aircraft design.

---

This module explains:
✔ What you designed  
✔ Why it works  
✔ What can be improved  
""")

import pandas as pd

rho = 1.225
g = 9.81

# ==========================================================
# CHECK DATA
# ==========================================================
required_keys = ["MTOW", "S", "V_opt", "LD_opt"]

for key in required_keys:
    if key not in st.session_state:
        st.warning("Run all previous modules first")
        st.stop()

# ==========================================================
# FINAL DESIGN DATA
# ==========================================================
MTOW = st.session_state["MTOW"]
S = st.session_state["S"]
V = st.session_state["V_opt"]
LD = st.session_state["LD_opt"]

W = MTOW * g

# ==========================================================
# SECTION 1: FINAL SUMMARY
# ==========================================================
st.subheader("✈️ Final Aircraft Design Summary")

st.success(f"MTOW = {MTOW:.2f} kg")
st.write(f"Wing Area = {S:.2f} m²")
st.write(f"Optimal Cruise Velocity = {V:.2f} m/s")
st.write(f"Maximum L/D = {LD:.2f}")

# ==========================================================
# SECTION 2: PERFORMANCE CHECK
# ==========================================================
st.subheader("✔️ Performance Validation")

Lift = 0.5 * rho * V**2 * S * (W / (0.5 * rho * V**2 * S))
Drag = W / LD

if Lift >= W:
    st.success("✔ Lift ≥ Weight → Sustained flight possible")
else:
    st.error("✖ Lift < Weight → Design issue")

if Drag > 0:
    st.success("✔ Drag estimation valid")

# ==========================================================
# SECTION 3: AI INTERPRETATION
# ==========================================================
st.subheader("🤖 AI-Based Design Interpretation")

# Intelligent reasoning
interpretation = ""

if LD > 15:
    interpretation += "The aircraft shows high aerodynamic efficiency. "
else:
    interpretation += "Aerodynamic efficiency is moderate and can be improved. "

if V > 220:
    interpretation += "The design is optimized for high-speed cruise. "
else:
    interpretation += "The design favors moderate-speed operation. "

if S > 100:
    interpretation += "Large wing area indicates better lift but higher drag. "
else:
    interpretation += "Compact wing design improves speed but reduces lift margin. "

interpretation += "Overall, the design reflects a balance between performance, efficiency, and structural feasibility."

st.info(interpretation)

# ==========================================================
# SECTION 4: IMPROVEMENT SUGGESTIONS
# ==========================================================
st.subheader("🔧 Design Improvement Suggestions")

suggestions = []

if LD < 15:
    suggestions.append("Increase aspect ratio to improve L/D")

if V < 180:
    suggestions.append("Increase cruise velocity for better performance")

if S > 120:
    suggestions.append("Optimize wing area to reduce drag")

if len(suggestions) == 0:
    st.success("Design is well optimized")
else:
    for s in suggestions:
        st.write(f"• {s}")

# ==========================================================
# SECTION 5: FINAL DATA EXPORT
# ==========================================================
st.subheader("⬇️ Download Final Results")

df_final = pd.DataFrame({
    "Parameter": ["MTOW", "Wing Area", "Velocity", "L/D"],
    "Value": [MTOW, S, V, LD]
})

st.dataframe(df_final)

csv = df_final.to_csv(index=False).encode()
st.download_button("⬇ Download Final Design Data", csv, "final_design.csv")

# ==========================================================
# FINAL CONCLUSION
# ==========================================================
st.subheader("🎓 Final Conclusion")

st.success("""
✔ Aircraft design successfully completed  

✔ All major parameters evaluated  

✔ Performance validated  

✔ Optimization achieved  

---

### ✈️ You have completed a full aircraft preliminary design cycle
""")

# ==========================================================
# END MESSAGE
# ==========================================================
st.markdown("""
---

## 🚀 Congratulations!

You have:

✔ Learned aircraft fundamentals  
✔ Performed real design calculations  
✔ Understood engineering trade-offs  
✔ Built a complete aircraft model  

---

### ✈️ This is how real aircraft design begins
""")

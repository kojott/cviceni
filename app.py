import streamlit as st
from datetime import datetime, timedelta
import time
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Load beep sound
beep_sound = pygame.mixer.Sound('beep.wav')

# Define the workout plan for each day in Czech
workout_plan_czech = [
    ("Celé tělo", [("Rozcvička", 120, "Pochod na místě pro zvýšení tepové frekvence")] + [("Kliky", 30, "Lehněte si na břicho, ruce položte vedle ramen a zvedejte tělo nahoru a dolů"), ("Dřepy", 30, "Postavte se, nohy na šířku ramen, a snižujte se, jako byste si chtěli sednout na židli"), ("Plank", 30, "Držení těla ve vzpěru na předloktích a špičkách nohou pro posílení středu těla"), ("Odpočinek", 30, "")] * 3),
    ("Střed těla a Kardio", [("Rozcvička", 120, "Běh na místě")] + [("Horolezci", 30, "Ve vzporu střídavě přitahujte kolena k hrudníku"), ("Zvedání nohou", 30, "Lehněte si na záda, ruce pod hýždě a zvedejte natažené nohy směrem vzhůru"), ("Skákající panák", 30, "Skákací cvik na místě, při kterém se rozpažujete a rozkročujete"), ("Odpočinek", 30, "")] * 3),
    ("Spodní část těla", [("Rozcvička", 120, "Mávání nohou a výpady s vlastní vahou")] + [("Dřepy", 30, "Postavte se, nohy na šířku ramen, a snižujte se, jako byste si chtěli sednout na židli"), ("Výpady", 30, "Střídavě kročte jednou nohou vpřed a pokrčte kolena, dokud zadní koleno není těsně nad zemí"), ("Sed u zdi", 30, "Opřete se zády o stěnu, snižte se do dřepu a držte tuto pozici"), ("Odpočinek", 30, "")] * 3),
    ("Horní část těla a střed těla", [("Rozcvička", 120, "Kroužení pažemi a stínový box")] + [("Kliky", 30, "Lehněte si na břicho, ruce položte vedle ramen a zvedejte tělo nahoru a dolů"), ("Tricepsové dipy", 30, "Položte ruce na okraj židle za sebou, nohy natáhněte před sebe a snižujte tělo dolů a nahoru"), ("Jízdní kolo", 30, "Lehněte si na záda, ruce za hlavu a střídavě přitahujte kolena k protilehlým loktům"), ("Odpočinek", 30, "")] * 3),
    ("Celé tělo", [("Rozcvička", 120, "Lehký strečink a kroužení krkem")] + [("Worm", 30, "Z pozice ve stoje se ohýbejte, až se dotknete rukama země, a poté ručkujte dopředu do planku"), ("Plank to push-up", 30, "Z pozice planku se střídavě zvedejte do pozice kliku a vracejte se zpět"), ("Vysoká kolena", 30, "Běh na místě s vysokým zvedáním kolen"), ("Odpočinek", 30, "")] * 3),
    ("Strečink a regenerace", [("Strečink", 600, "10 minut různých strečinkových cviků zaměřených na všechny hlavní svalové skupiny")]),
    ("Smíšené Kardio", [("Rozcvička", 120, "Vysoká kolena a kopání do zadku")] + [("Burpees", 30, "Z pozice ve stoje skočte do dřepu, poté do planku, udělejte klik, a skočte zpět do stoje s výskokem"), ("Boční výpady", 30, "Střídavě vykračujte do strany a pokrčujte koleno, druhá noha zůstává natažená"), ("Rychlé nohy", 30, "Rychlé střídání nohou na místě pro zvýšení tepové frekvence"), ("Odpočinek", 30, "")] * 3)
]

# Get current date
today = datetime.now().date()

# Find the workout for today
workout_today = workout_plan_czech[today.weekday() % 7]
workout_name, workout_exercises = workout_today

# Calculate total workout time
total_workout_time = sum(exercise_time for _, exercise_time, _ in workout_exercises)

# Define timer states
if 'exercise_index' not in st.session_state:
    st.session_state.exercise_index = 0
    st.session_state.time_left = workout_exercises[0][1]
    st.session_state.running = False
    st.session_state.total_time_left = total_workout_time

# Timer controls
def start_timer():
    st.session_state.running = True

def stop_timer():
    st.session_state.running = False

def reset_timer():
    st.session_state.exercise_index = 0
    st.session_state.time_left = workout_exercises[0][1]
    st.session_state.total_time_left = total_workout_time
    st.session_state.running = False

def next_exercise():
    if st.session_state.exercise_index < len(workout_exercises) - 1:
        st.session_state.total_time_left -= st.session_state.time_left
        st.session_state.exercise_index += 1
        st.session_state.time_left = workout_exercises[st.session_state.exercise_index][1]
        st.session_state.running = True
        
        # Play beep sound
        beep_sound.play()
    else:
        st.session_state.running = False

def prev_exercise():
    if st.session_state.exercise_index > 0:
        st.session_state.exercise_index -= 1
        st.session_state.time_left = workout_exercises[st.session_state.exercise_index][1]
        st.session_state.total_time_left = total_workout_time - sum(exercise_time for _, exercise_time, _ in workout_exercises[:st.session_state.exercise_index])
        st.session_state.running = True
    else:
        st.session_state.running = False

# Display workout for today
st.title(f"Denní Cvičení: {workout_name}")

# Display all exercises
st.subheader("Seznam dnešních cviků")
for i, (exercise_name, exercise_time, exercise_desc) in enumerate(workout_exercises):
    if i == st.session_state.exercise_index:
        st.write(f"<h4>➡️ {i + 1}. {exercise_name} - {exercise_time} sekund</h4>", unsafe_allow_html=True)
        st.write(f"**{exercise_desc}**")
    else:
        st.write(f"<h5>{i + 1}. {exercise_name} - {exercise_time} sekund</h5>", unsafe_allow_html=True)
        st.write(f"{exercise_desc}")

# Timer display
exercise_name, exercise_time, exercise_desc = workout_exercises[st.session_state.exercise_index]
st.subheader(f"Aktuální cvik: {exercise_name}")
st.write(f"Popis: {exercise_desc}")
st.write(f"Zbývající čas: {st.session_state.time_left} sekund")

# Display total time left
st.write(f"Zbývající čas do konce cvičení: {str(timedelta(seconds=st.session_state.total_time_left))}")

# Progress bars
st.progress(1 - st.session_state.total_time_left / total_workout_time)
st.progress(1 - st.session_state.time_left / exercise_time)

# Timer buttons
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.button("Předchozí", on_click=prev_exercise)

with col2:
    st.button("Start", on_click=start_timer)

with col3:
    st.button("Stop", on_click=stop_timer)

with col4:
    st.button("Reset", on_click=reset_timer)

with col5:
    st.button("Další", on_click=next_exercise)

# Timer logic
if st.session_state.running:
    time.sleep(1)
    st.session_state.time_left -= 1
    if st.session_state.time_left <= 0:
        next_exercise()
    st.rerun()

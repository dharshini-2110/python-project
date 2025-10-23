import streamlit as st
import random
import time

# --- PAGE CONFIG ---
st.set_page_config(page_title="Typing Speed Test", page_icon="⌨️", layout="centered")

# --- INITIAL SESSION STATE ---
if "words" not in st.session_state:
    st.session_state.words = [
        "python", "streamlit", "programming", "challenge", "keyboard",
        "application", "interface", "developer", "coding", "accuracy"
    ]
if "current_word" not in st.session_state:
    st.session_state.current_word = ""
if "score" not in st.session_state:
    st.session_state.score = 0
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "time_left" not in st.session_state:
    st.session_state.time_left = 60
if "game_started" not in st.session_state:
    st.session_state.game_started = False


# --- HELPER FUNCTIONS ---
def start_game():
    st.session_state.game_started = True
    st.session_state.score = 0
    st.session_state.time_left = 60
    st.session_state.start_time = time.time()
    next_word()

def next_word():
    st.session_state.current_word = random.choice(st.session_state.words)

def reset_game():
    st.session_state.game_started = False
    st.session_state.score = 0
    st.session_state.time_left = 60
    st.session_state.current_word = ""
    st.session_state.start_time = None

def update_timer():
    if st.session_state.start_time:
        elapsed = int(time.time() - st.session_state.start_time)
        st.session_state.time_left = max(60 - elapsed, 0)
        if st.session_state.time_left == 0:
            st.session_state.game_started = False


# --- UI ELEMENTS ---
st.title("⌨️ Typing Speed Test")
st.write("Type the word shown below as fast as you can. You have **60 seconds!**")

# --- START AND RESET BUTTONS ---
col1, col2 = st.columns(2)
with col1:
    if st.button("▶️ Start Game"):
        start_game()
with col2:
    if st.button("🔄 Reset"):
        reset_game()

# --- GAME AREA ---
update_timer()

if st.session_state.game_started:
    st.subheader(f"⏱️ Time Left: {st.session_state.time_left} seconds")
    st.subheader(f"🏆 Score: {st.session_state.score}")

    st.markdown(f"## **{st.session_state.current_word}**")

    typed_word = st.text_input("Type the word here:", key=f"input_{st.session_state.score}")

    if typed_word.strip().lower() == st.session_state.current_word.lower():
        st.session_state.score += 1
        next_word()
        st.rerun()  # ✅ Modern rerun function

    if st.session_state.time_left <= 0:
        st.session_state.game_started = False
        st.rerun()

else:
    if st.session_state.start_time:
        st.markdown("### 🏁 Game Over!")
        st.write(f"**Your final score:** {st.session_state.score}")
        st.balloons()

import streamlit as st

# --- Set Background ---
def set_background():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://raw.githubusercontent.com/Moondeep73/LoveApp/main/assets/Background.jpg");
            background-size: cover;
            background-position: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# --- Set Up State ---
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.score = 0

# --- Question & Answer Logic ---
set_background()

if st.session_state.step == 0:
    st.markdown("## 💘 How do you feel about love today?")
    answer = st.radio(
        "Choose one:",
        ["I hate it", "Not feeling great", "Meh, it's okay", "Feeling warm fuzzies", "I'm floating in love! 💖"]
    )

    if st.button("Next"):
        st.session_state.score = [1, 2, 3, 4, 5][
            ["I hate it", "Not feeling great", "Meh, it's okay", "Feeling warm fuzzies", "I'm floating in love! 💖"].index(answer)
        ]
        st.session_state.step = 1
        st.experimental_rerun()

# --- Show Result ---
elif st.session_state.step == 1:
    st.markdown("## 💖 Your Love Mood:")

    score = st.session_state.score
    gif_map = {
        1: "Angry.gif",
        2: "Upset.gif",
        3: "Neutral.gif",
        4: "Happy.gif",
        5: "Euphoric.gif"
    }

    gif_url = f"https://raw.githubusercontent.com/Moondeep73/LoveApp/main/assets/{gif_map[score]}"
    st.image(gif_url)

    if st.button("Restart"):
        st.session_state.step = 0
        st.session_state.score = 0
        st.experimental_rerun()

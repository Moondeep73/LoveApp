import streamlit as st

# --- Set Background ---
def set_background():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://raw.githubusercontent.com/Moondeep73/LoveApp/main/assets/Background.jpeg");
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
    st.session_state.score = None

# --- Main Flow ---
set_background()

if st.session_state.step == 0:
    st.markdown("## 💘 How do you feel about love today?")
    answer = st.radio(
        "Choose one:",
        ["I hate it", "Not feeling great", "Meh, it's okay", "Feeling warm fuzzies", "I'm floating in love! 💖"]
    )

    if st.button("Next"):
        st.session_state.score = (
            ["I hate it", "Not feeling great", "Meh, it's okay", "Feeling warm fuzzies", "I'm floating in love! 💖"].index(answer) + 1
        )
        st.session_state.step = 1
        st.rerun()

elif st.session_state.step == 1:
    st.markdown("## 💖 Your Love Mood:")

    gif_map = {
        1: "Angry.gif",
        2: "Upset.gif",
        3: "Neutral.gif",
        4: "Happy.gif",
        5: "Love.gif"
    }

    score = st.session_state.get("score")

    if score in gif_map:
        gif_url = f"https://raw.githubusercontent.com/Moondeep73/LoveApp/main/assets/{gif_map[score]}"
        st.image(gif_url)
    else:
        st.warning("No valid score found.")

    if st.button("Restart"):
        st.session_state.step = 0
        st.session_state.score = None
        st.rerun()

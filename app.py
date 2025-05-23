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

# --- Custom CSS for text styling ---
st.markdown("""
<style>
/*
.big-question {
    font-size: 30px;
    color: #e91e63;
    font-weight: bold;
    text-align: center;
}

.stButton > button {
    font-size: 20px;
    background-color: #f06292;
    color: black;
    padding: 0.5em 2em;
    border-radius: 10px;
}
*/

/* Radio text only (deep green) */
/*
#
# [data-baseweb="radio"] > div > label > div:nth-child(2) {
#     color: #1b5e20 !important;
#     font-size: 20px !important;
#     font-weight: bold !important;
# }
*/

</style>
""", unsafe_allow_html=True)

# --- State Init ---
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.score = None

# --- Main App Flow ---
# set_background()

if st.session_state.step == 0:
    # Big question as-is
    st.markdown('<div class="big-question">💘 How do you feel about love today?</div>', unsafe_allow_html=True)

    # Visual container using columns
    left, center, right = st.columns([1, 6, 1])
    with center:
        # Background for center column (simulating a box)
        # st.markdown(
        #     """
        #     <div style='background-color: #e8f5e9; padding: 20px; border-radius: 15px;'>
        #     <style>
        #     [data-baseweb="radio"] label > div:nth-child(2) {
        #         color: #1b5e20 !important;
        #         font-size: 18px !important;
        #         font-weight: bold !important;
        #     }
        #     </style>
        #     """, unsafe_allow_html=True
        # )

        answer = st.radio(
            label="Choose one:",
            options=[
                "I hate it",
                "Not feeling great",
                "Meh, it's okay",
                "Feeling warm fuzzies",
                "I'm floating in love! 💖"
            ],
            key="love_feel",
            label_visibility="collapsed"
        )

        st.markdown("</div>", unsafe_allow_html=True)

    # Button stays below
    if st.button("Next"):
        st.session_state.score = (
            ["I hate it", "Not feeling great", "Meh, it's okay", "Feeling warm fuzzies", "I'm floating in love! 💖"].index(answer) + 1
        )
        st.session_state.step = 1
        st.rerun()


elif st.session_state.step == 1:
    st.markdown('<div class="big-question">💖 Your Love Mood</div>', unsafe_allow_html=True)

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

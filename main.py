import streamlit as st
import random

# Set page config
st.set_page_config(page_title="SELAMAT LULUS SIDANG SIPE", page_icon="🎓", layout="wide")

# Custom CSS to make it more festive
st.markdown("""
    <style>
    .main {
        background-color: #f0f8ff;
    }
    h1, h2, H3 {
        color: #4b0082;
    }
    .stButton>button {
        color: #4b0082;
        background-color: #ff69b4;
        border-radius: 20px;
    }
    p {
        color: #242424;
    }
    </style>
    """, unsafe_allow_html=True)

# Main title
st.title("🎉 AKHIRNYAAA SIDANGGG CONGRATSSS SIPEEEE! 🎓")

# Name input
# name = st.text_input("Enter your name:")
name = "Syifa Hadiarti Aulia"

st.header(f"Hip Hip Hooray, {name}! 🥳")

# Personalized message
st.write(f"Makasih yaaa udah berjuang sejauh ini 🥹. Aku tau perjalanannya berat bangettt bisa sampe titik ini :')")
st.write("Kamu udah super keren bisa bertahan sampe akhir di tengah semua hal yang pusing pusing ituu.")

# Interactive elements
if st.button("Click for a Special Message"):
    messages = [
        "KEREN BANGETTTT 🌟",
        "KAMU HEBATTT 😋",
        "SELAMATTT YEAAYYY AKHIRNYA BERES SIDANG 🥳",
        "I'm so proud of you 🥹",
        "Semoga kamu tetap bersinar dan akan selalu bersinar sipe ❤️"
    ]
    st.success(random.choice(messages))

# Fireworks animation
st.balloons()

# Accomplishment reflection
accomplishment = st.text_area("Apa yang paling berkesan dari perjalaan TA kamu sejauh iniii?")
if accomplishment:
    st.write("Semoga semuanya terbayarkan dan lega yaaa :)")

# Future plans
st.subheader("Abis beres sidang kamu mau ngapainnn " + name + "? Wkwkwkwk")
options = st.multiselect(
    'Mau ngapainn abis selesai sidangg?',
    ['Hiling', 'Hibernasi', 'Mukbang', 'Gawe', 'Gatau dah awokwokwok']
)

if options:
    st.write("Niceee apapun pilihan kamuuu, selamat yaa udah selesai sidang :) Selamat narik nafas sejenak hehe")

# Celebration song
audio_file = open('good_time.ogg', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/ogg')

# Final message
st.markdown("### 🎊 Sekali lagi, SELAMAT YAAAAA! 🎊")


# Footer
st.markdown("---")
st.markdown("Dengan ❤️untuk sipe!")

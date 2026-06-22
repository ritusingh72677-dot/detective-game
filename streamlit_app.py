import streamlit as st

from murder_mystery import (
    accuse_suspect,
    create_game,
    interrogate_suspect,
    suspect_list,
)


def reset_case():
    st.session_state.game = create_game()
    st.session_state.interrogation = None
    st.session_state.accusation = None
    st.session_state.message = ""


if "game" not in st.session_state:
    reset_case()

st.title("Murder Mystery")
st.write(
    "A detective has to solve a crime. Interrogate suspects, gather clues, and accuse the hidden murderer."
)

if st.button("Start a new case"):
    reset_case()

suspects = st.session_state.game["suspects"]
suspect_names = [suspect["name"] for suspect in suspects]

st.subheader("Suspects")
for suspect in suspect_list(suspects):
    st.write(f"**{suspect['name']}** — {suspect['occupation']}, age {suspect['age']}")

st.divider()

if st.session_state.game["game_over"]:
    st.success(st.session_state.message)
    if "Congratulations" in st.session_state.message:
        st.balloons()
    st.info("Press 'Start a new case' to play again.")
else:
    selected_name = st.selectbox("Choose a suspect", suspect_names)
    selected_index = suspect_names.index(selected_name)

    if st.button("Interrogate suspect"):
        st.session_state.interrogation = interrogate_suspect(suspects, selected_index)

    if st.session_state.interrogation:
        interrogation = st.session_state.interrogation
        st.subheader(f"Interrogating {interrogation['name']}")
        st.write(f"**Alibi:** {interrogation['alibi']}")
        st.write(f"**Clue:** {interrogation['clue']}")

    if st.button("Accuse suspect"):
        guilty = accuse_suspect(suspects, selected_index)
        st.session_state.game["game_over"] = True
        if guilty:
            st.session_state.message = f"You accused {selected_name}. Congratulations! You found the murderer!"
        else:
            st.session_state.message = (
                f"You accused {selected_name}, but they are innocent. The real murderer got away this time."
            )

    if st.session_state.message:
        if "Congratulations" in st.session_state.message:
            st.success(st.session_state.message)
            st.balloons()
        else:
            st.error(st.session_state.message)

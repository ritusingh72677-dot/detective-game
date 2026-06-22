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
    st.session_state.message = ""


if "game" not in st.session_state:
    reset_case()

st.set_page_config(page_title="Murder Mystery Detective", page_icon="🕵️‍♂️")
st.title("Murder Mystery Detective")
st.write(
    "Solve the case by interrogating suspects, collecting evidence, and accusing the right person before your accusations run out."
)

if st.button("Start a new case"):
    reset_case()

game = st.session_state.game
suspects = game["suspects"]
suspect_names = [suspect["name"] for suspect in suspects]

with st.expander("Case Summary", expanded=True):
    st.write(
        "A wealthy collector has been murdered in his manor. The suspects are all connected to the estate in different ways. "
        "Interrogate each one carefully and look for contradictions in their stories."
    )
    st.write(f"**Remaining accusations:** {game['remaining_accusations']}")
    if game["evidence"]:
        st.write("**Collected evidence:**")
        for evidence in game["evidence"]:
            st.write(f"- **{evidence['name']}**: {evidence['clue']}")

st.subheader("Suspects")
for suspect in suspect_list(suspects):
    status = "(questioned)" if suspect["interrogated"] else "(not questioned)"
    st.write(
        f"**{suspect['name']}** — {suspect['occupation']}, age {suspect['age']} {status}"
    )

st.divider()

if game["game_over"]:
    if game["case_solved"]:
        st.success(game["message"])
        st.balloons()
    else:
        st.error(game["message"])
    st.info("Press 'Start a new case' to try again.")
else:
    selected_name = st.selectbox("Choose a suspect", suspect_names)
    selected_index = suspect_names.index(selected_name)

    if st.button("Interrogate suspect"):
        st.session_state.interrogation = interrogate_suspect(game, selected_index)

    if st.session_state.interrogation:
        interrogation = st.session_state.interrogation
        st.subheader(f"Interrogating {interrogation['name']}")
        st.write(f"**Personality:** {interrogation['personality']}")
        st.write(f"**Alibi:** {interrogation['alibi']}")
        st.write(f"**Clue:** {interrogation['clue']}")
        st.write(f"**Motive:** {interrogation['motive']}")

    if st.button("Accuse suspect"):
        accuse_suspect(game, selected_index)
        if game["case_solved"]:
            st.success(game["message"])
            st.balloons()
        else:
            st.warning(game["message"])

    if game["message"] and not game["game_over"]:
        st.info(game["message"])

with st.expander("Detective Journal", expanded=False):
    if game["log"]:
        for entry in game["log"]:
            st.write(f"- {entry}")
    else:
        st.write("No interactions yet. Start by interrogating a suspect.")

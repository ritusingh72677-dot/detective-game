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

st.set_page_config(page_title="Murder Mystery Detective", page_icon="🕵️‍♂️", layout="wide")
st.title("🕵️‍♂️ Murder Mystery Detective")
st.markdown(
    "Solve the manor mystery by questioning suspects, gathering clues, and making the correct accusation before your chances run out."
)

if st.button("Start a new case 🆕"):
    reset_case()

game = st.session_state.game
suspects = game["suspects"]
suspect_names = [suspect["name"] for suspect in suspects]

with st.sidebar:
    st.header("🧩 How to play")
    st.write(
        "- 🗣️ Interrogate suspects to reveal their alibis, motives, and clues.\n"
        "- 🔎 Collect evidence carefully and compare statements.\n"
        "- ⚖️ You have three accusations; choose wisely.\n"
    )
    st.metric("Remaining accusations", game["remaining_accusations"])
    if game["evidence"]:
        st.markdown("**🧾 Collected evidence**")
        for evidence in game["evidence"]:
            st.write(f"- {evidence['name']}: {evidence['clue']}")
    st.divider()
    st.markdown("**🕵️‍♀️ Suspect overview**")
    for suspect in suspect_list(suspects):
        status = "✅" if suspect["interrogated"] else "❌"
        st.write(f"{status} {suspect['name']} — {suspect['occupation']}")

col1, col2 = st.columns([2, 1])

with col1:
    with st.expander("📜 Case summary", expanded=True):
        st.write(
            "A wealthy collector has been murdered in his manor. "
            "Each suspect has a motive, but only one is the true killer. "
            "Use your detective instincts to separate truth from lies."
        )

    st.subheader("📝 Suspects")
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
        selected_name = st.selectbox("Choose a suspect 🔎", suspect_names)
        selected_index = suspect_names.index(selected_name)

        if st.button("🗣️ Interrogate suspect"):
            st.session_state.interrogation = interrogate_suspect(game, selected_index)

        if st.session_state.interrogation:
            interrogation = st.session_state.interrogation
            st.subheader(f"Interrogating {interrogation['name']}")
            st.write(f"**Personality:** {interrogation['personality']}")
            st.write(f"**Alibi:** {interrogation['alibi']}")
            st.write(f"**Clue:** {interrogation['clue']}")
            st.write(f"**Motive:** {interrogation['motive']}")

        if game["remaining_accusations"] > 0:
            if st.button("Accuse suspect"):
                accuse_suspect(game, selected_index)
                if game["case_solved"]:
                    st.success(game["message"])
                    st.balloons()
                else:
                    st.warning(game["message"])
        else:
            st.error("No accusations left. Start a new case to play again.")

        if game["message"] and not game["game_over"]:
            st.info(game["message"])

with col2:
    st.subheader("Toolbox")
    st.info("Use the sidebar to track evidence and suspect progress.")
    st.write("**Next step**: interrogate suspects to collect more clues.")
    if game["game_over"]:
        st.write("Game over. Restart to solve a new case.")
    else:
        st.write("You can interrogate suspects first, then accuse when ready.")

with st.expander("Detective Journal", expanded=False):
    if game["log"]:
        for entry in game["log"]:
            st.write(f"- {entry}")
    else:
        st.write("No interactions yet. Start by interrogating a suspect.")

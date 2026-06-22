import streamlit as st

from murder_mystery import (
    accuse_suspect,
    case_list,
    create_game,
    interrogate_suspect,
    suspect_list,
)


def reset_case(case_index=None):
    if case_index is None:
        case_index = st.session_state.get("case_index", 0)
    st.session_state.case_index = case_index
    st.session_state.game = create_game(case_index)
    st.session_state.interrogation = None
    st.session_state.message = ""


if "case_index" not in st.session_state:
    st.session_state.case_index = 0

if "game" not in st.session_state or "case_title" not in st.session_state.get("game", {}):
    reset_case(st.session_state.case_index)

st.set_page_config(page_title="Murder Mystery Detective", page_icon="🕵️‍♂️", layout="wide")
st.title("🕵️‍♂️ Murder Mystery Detective")
st.markdown(
    "Solve mysterious murder cases by questioning suspects, gathering clues, and making the correct accusation before your chances run out."
)

case_options = case_list()
case_titles = [case["title"] for case in case_options]
selected_case = st.selectbox("Choose a case 🗂️", case_titles, index=st.session_state.case_index)
selected_case_index = case_titles.index(selected_case)
if selected_case_index != st.session_state.case_index:
    reset_case(selected_case_index)

if st.button("Start a new case 🆕"):
    reset_case(selected_case_index)

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
    with st.expander(f"📜 Case summary: {game['case_title']}", expanded=True):
        st.write(f"**Location:** {game['case_location']}")
        st.write(game["case_description"])

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

import streamlit as st

# Initialize Session State
if 'to_do_list' not in st.session_state:
    st.session_state.to_do_list = []

st.title("🎩 Hat of Good Times 🎩")

# Add new idea
idea = st.text_input("Add a fun idea to your hat:")
if st.button("Add to Hat"):
    if idea:
        st.session_state.to_do_list.append({"text": idea, "checked": False})

# Display list with checkboxes
st.subheader("Your Fun Ideas:")
for index, item in enumerate(st.session_state.to_do_list):
    checked = st.checkbox(item["text"], key=f"checkbox_{index}", value=item["checked"])
    if checked:
        # Style completed items
        st.write(f'<del style="color: gray;">{item["text"]}</del>', unsafe_allow_html=True)
        st.session_state.to_do_list[index]["checked"] = True

# "Empty the hat" button
if st.button("Empty the Hat"):
    st.session_state.to_do_list = []

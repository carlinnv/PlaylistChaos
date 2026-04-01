def render_playlist(label, songs):
    st.subheader(f"{label} playlist")
    if not songs:
        st.write("No songs in this playlist.")
        return

    query = st.text_input(f"Search {label} playlist by artist", key=f"search_{label}")
    filtered = search_songs(songs, query, field="artist")
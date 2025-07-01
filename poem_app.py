import streamlit as st
import random

# Lists of words for poem generation
adjectives = ['whispering', 'radiant', 'mystic', 'gentle', 'fading', 'vibrant', 'silent', 'golden']
nouns = ['moonlight', 'forest', 'river', 'shadow', 'breeze', 'mountain', 'ocean', 'star']
verbs = ['dances', 'sings', 'wanders', 'gleams', 'flows', 'soars', 'flickers', 'dreams']
adverbs = ['softly', 'boldly', 'quietly', 'freely', 'gently', 'swiftly', 'calmly', 'brightly']

def generate_poem(lines=4):
    poem = []
    for _ in range(lines):
        line = (
            f"The {random.choice(adjectives)} {random.choice(nouns)} "
            f"{random.choice(verbs)} {random.choice(adverbs)}"
        )
        poem.append(line)
    return "\n".join(poem)

# Streamlit app
st.title("Poem Generator")
st.write("Create a unique poem with the click of a button!")

# Number of lines input
num_lines = st.slider("Number of lines", min_value=2, max_value=10, value=4)

# Generate button
if st.button("Generate Poem"):
    poem = generate_poem(num_lines)
    st.write("### Your Poem")
    st.write(poem)

# Option to save poem
if 'poem' in locals():
    st.download_button(
        label="Download Poem",
        data=poem,
        file_name="generated_poem.txt",
        mime="text/plain"
    )
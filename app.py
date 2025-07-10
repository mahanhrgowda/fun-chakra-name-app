import streamlit as st

# Hardcoded English phoneme to chakra map based on chat data
phoneme_to_chakra = {
    '/s/': 'Muladhara',
    '/z/': 'Muladhara',
    '/ʃ/': 'Muladhara',
    '/ʒ/': 'Muladhara',
    '/m/': 'Svadhisthana',
    '/n/': 'Svadhisthana',
    '/w/': 'Svadhisthana',
    '/j/': 'Svadhisthana',
    '/l/': 'Svadhisthana',
    '/r/': 'Svadhisthana',
    '/p/': 'Manipura',
    '/b/': 'Manipura',
    '/t/': 'Manipura',
    '/d/': 'Manipura',
    '/k/': 'Manipura',
    '/ɡ/': 'Manipura',
    '/f/': 'Manipura',
    '/v/': 'Manipura',
    '/θ/': 'Manipura',
    '/ð/': 'Manipura',
    '/tʃ/': 'Anahata',
    '/dʒ/': 'Anahata',
    '/h/': 'Anahata',
    '/ŋ/': 'Anahata',
    '/æ/': 'Anahata',
    '/ɛ/': 'Anahata',
    '/ɪ/': 'Anahata',
    '/ʌ/': 'Anahata',
    '/ɒ/': 'Anahata',
    '/ʊ/': 'Anahata',
    '/ə/': 'Anahata',
    '/ɔː/': 'Anahata',
    '/iː/': 'Vishuddha',
    '/uː/': 'Vishuddha',
    '/eɪ/': 'Vishuddha',
    '/aɪ/': 'Vishuddha',
    '/aʊ/': 'Vishuddha',
    '/ɔɪ/': 'Vishuddha',
    '/ɑː/': 'Vishuddha',
    # For unassigned, from reasoning: reassigned to Vishuddha and Ajna
    '/ɪ/': 'Vishuddha',
    '/ɛ/': 'Vishuddha',
    '/æ/': 'Vishuddha',
    '/ʌ/': 'Vishuddha',
    '/ɒ/': 'Vishuddha',
    '/ʊ/': 'Vishuddha',
    '/ə/': 'Vishuddha',
    '/ɔː/': 'Vishuddha',
    '/ŋ/': 'Vishuddha',
    '/tʃ/': 'Ajna',
    '/dʒ/': 'Ajna'
}

# Simple letter to phoneme approximation (rule-based, no libraries)
letter_to_phoneme = {
    'a': '/æ/',
    'b': '/b/',
    'c': '/k/',  # or /s/, but simple
    'd': '/d/',
    'e': '/ɛ/',
    'f': '/f/',
    'g': '/ɡ/',
    'h': '/h/',
    'i': '/ɪ/',
    'j': '/dʒ/',
    'k': '/k/',
    'l': '/l/',
    'm': '/m/',
    'n': '/n/',
    'o': '/ɒ/',
    'p': '/p/',
    'q': '/k/',
    'r': '/r/',
    's': '/s/',
    't': '/t/',
    'u': '/ʌ/',
    'v': '/v/',
    'w': '/w/',
    'x': '/ks/',
    'y': '/j/',
    'z': '/z/'
}

def approximate_phonemes(name):
    name = name.lower()
    phonemes = []
    i = 0
    while i < len(name):
        letter = name[i]
        if letter in letter_to_phoneme:
            phonemes.append(letter_to_phoneme[letter])
        i += 1
    return list(set(phonemes))  # Unique phonemes

st.title("Fun Name Chakra App 🌟")

st.markdown("Based on phonemes and chakras from ancient Maheshwara Sutras! Enter your name to see which chakras it activates with fun messages! 🎉")

name = st.text_input("Enter your name:", placeholder="Mahan H R Gowda")

if name:
    st.success(f"Hello, {name}! 👋 Let's explore the chakras in your name!")

    # Approximate phonemes
    phonemes = approximate_phonemes(name)
    st.info(f"Your name's approximated phonemes: {', '.join(phonemes)} 🔊")

    # Map to chakras
    activated_chakras = set()
    for p in phonemes:
        if p in phoneme_to_chakra:
            activated_chakras.add(phoneme_to_chakra[p])

    if activated_chakras:
        st.warning(f"Your name activates these chakras: {', '.join(activated_chakras)} ✨")
    else:
        st.warning("Your name's phonemes don't map to any chakra yet – it's unique! 🌈")

    # Fun outputs
    reversed_name = name[::-1]
    st.error(f"Your name backwards: **{reversed_name}** 🔄 – A secret chakra code? 🕵️")

    length = len(name)
    if length < 5:
        msg = "Short and sweet, like Muladhara's grounding energy! 🏔️"
    elif length < 8:
        msg = "Balanced, like Svadhisthana's flow! 🌊"
    else:
        msg = "Epic, like Sahasrara's enlightenment! 🌟"
    st.success(f"Name length {length}: {msg}")

    # Personalized emoji message
    emoji_msg = f"{name}, your phonemes light up the chakras like a rainbow! 🌈 Keep vibrating high! 🚀"
    st.balloons()
    st.markdown(emoji_msg)
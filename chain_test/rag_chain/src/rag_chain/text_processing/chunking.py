def chunk_text(text, chunk_size=512):
    # Example chunking logic
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]


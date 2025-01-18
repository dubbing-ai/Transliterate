from phonemizer.backend.espeak.wrapper import EspeakWrapper

def setup_espeak(library_path: str):
    """Set up espeak library path."""
    EspeakWrapper.set_library(library_path)
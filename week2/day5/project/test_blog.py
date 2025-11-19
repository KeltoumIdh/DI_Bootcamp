import os
import builtins
import types
import pytest
from unittest.mock import patch, MagicMock
from blog import Blog


# Behaviors under test:
# 1) Should translate content using Translator with correct languages
# 2) Should create audio folder if missing and save TTS mp3 to expected path
# 3) Should select correct OS playback command and call os.system accordingly
# 4) Should return structured dict with translated_text and audio_file_path on success
# 5) Should gracefully handle exceptions and return error info


@pytest.fixture
def blog_with_id():
    # Provide a blog instance with an id to build file path deterministically
    b = Blog(title="T", content="Hello world", id=42)
    return b


@pytest.fixture
def ensure_clean_audio(tmp_path, monkeypatch):
    # Use a temp directory for the audio output to avoid touching real FS
    audio_dir = tmp_path / "audio"
    monkeypatch.chdir(tmp_path)
    return audio_dir


def test_translate_and_speak_translates_with_correct_langs(blog_with_id, ensure_clean_audio):
    with patch("blog.Translator") as MockTranslator, \
         patch("blog.gTTS") as MockTTS, \
         patch("blog.platform.system", return_value="Linux"), \
         patch("blog.os.system") as mock_system:
        instance = MockTranslator.return_value
        instance.translate.return_value = "Bonjour le monde"
        tts_instance = MagicMock()
        MockTTS.return_value = tts_instance

        res = blog_with_id.translate_and_speak("en", "fr")

        MockTranslator.assert_called_once_with(from_lang="en", to_lang="fr")
        instance.translate.assert_called_once_with("Hello world")
        assert res["translated_text"] == "Bonjour le monde"


def test_translate_and_speak_creates_folder_and_saves_mp3(blog_with_id, ensure_clean_audio):
    with patch("blog.Translator") as MockTranslator, \
         patch("blog.gTTS") as MockTTS, \
         patch("blog.platform.system", return_value="Linux"), \
         patch("blog.os.system"):
        MockTranslator.return_value.translate.return_value = "Salut"
        tts_instance = MagicMock()
        MockTTS.return_value = tts_instance

        res = blog_with_id.translate_and_speak("en", "fr")

        # Verify folder created and save path
        expected_folder = os.path.join("audio")
        expected_path = os.path.join(expected_folder, f"blog_{blog_with_id.id}_audio.mp3")
        MockTTS.assert_called_once_with(text="Salut", lang="fr")
        tts_instance.save.assert_called_once_with(expected_path)
        assert os.path.dirname(res["audio_file_path"]) == expected_folder


def test_translate_and_speak_linux_calls_mpg123(blog_with_id, ensure_clean_audio):
    with patch("blog.Translator") as MockTranslator, \
         patch("blog.gTTS") as MockTTS, \
         patch("blog.platform.system", return_value="Linux"), \
         patch("blog.os.system") as mock_system:
        MockTranslator.return_value.translate.return_value = "Salut"
        MockTTS.return_value = MagicMock()

        res = blog_with_id.translate_and_speak("en", "fr")

        expected_path = os.path.join("audio", f"blog_{blog_with_id.id}_audio.mp3")
        mock_system.assert_called_once_with(f"mpg123 '{expected_path}'")
        assert res["audio_file_path"] == expected_path


def test_translate_and_speak_windows_calls_start(blog_with_id, ensure_clean_audio):
    with patch("blog.Translator") as MockTranslator, \
         patch("blog.gTTS") as MockTTS, \
         patch("blog.platform.system", return_value="Windows"), \
         patch("blog.os.system") as mock_system:
        MockTranslator.return_value.translate.return_value = "Hi"
        MockTTS.return_value = MagicMock()

        blog_with_id.translate_and_speak("fr", "en")

        expected_path = os.path.join("audio", f"blog_{blog_with_id.id}_audio.mp3")
        mock_system.assert_called_once_with(f"start {expected_path}")


def test_translate_and_speak_handles_exception(blog_with_id, ensure_clean_audio):
    with patch("blog.Translator") as MockTranslator, \
         patch("blog.gTTS") as MockTTS, \
         patch("blog.platform.system", return_value="Linux"), \
         patch("blog.os.system"):
        # Force Translator to raise to simulate upstream failure
        MockTranslator.side_effect = RuntimeError("translator down")

        res = blog_with_id.translate_and_speak("en", "fr")

        assert res["translated_text"] is None
        assert res["audio_file_path"] is None
        assert "translator down" in res["error"]

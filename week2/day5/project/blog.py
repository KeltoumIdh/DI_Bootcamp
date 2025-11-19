# blog.py
from datetime import datetime
from db import get_connection
from translate import Translator
from gtts import gTTS
import os
import platform

class Blog:
    def __init__(self, title, content, id=None, created_at=None, updated_at=None):
        self.id = id
        self.title = title
        self.content = content
        self.created_at = created_at
        self.updated_at = updated_at


    def save(self):
        conn = None
        try:
            conn = get_connection()
            # This block inserts a new blog entry into the 'blogs' table in the PostgreSQL database.
            # It uses a SQL command to add the title and content, and then fetches the generated id,
            # created_at, and updated_at fields from the inserted row.

            # Steps:
            # 1. Open a new database cursor using 'with conn.cursor() as cur'.
            # 2. Define a parameterized SQL INSERT statement with RETURNING to get key values.
            # 3. Execute the SQL, passing self.title and self.content as parameters.
            # 4. Retrieve the returned row (containing id, created_at, updated_at).
            # 5. If successful, set these fields on the Blog instance and commit the transaction.
            # 6. If not, raise an error indicating the data could not be retrieved.

            with conn.cursor() as cur:
                sql = """
                    INSERT INTO blogs (title, content)
                    VALUES (%s, %s)
                    RETURNING id, created_at, updated_at;
                """
                cur.execute(sql, (self.title, self.content))
                row = cur.fetchone()
                if row:
                    self.id, self.created_at, self.updated_at = row
                    conn.commit()
                    print(f"Blog saved with id={self.id}")
                else:
                    raise ValueError("Failed to retrieve inserted blog data")
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"Error saving blog: {e}")
            raise
        finally:
            if conn:
                conn.close()


    def update(self):
        conn = None
        try:
            conn = get_connection()
            with conn.cursor() as cur:
                sql = """
                    UPDATE blogs
                    SET title = %s, content = %s, updated_at = NOW()
                    WHERE id = %s
                    RETURNING id, created_at, updated_at;
                """
                cur.execute(sql, (self.title, self.content, self.id))
                row = cur.fetchone()
                if row:
                    self.id, self.created_at, self.updated_at = row
                    conn.commit()
                    print(f"Blog updated with id={self.id}")
                else:
                    raise ValueError(f"No blog found with id={self.id}")
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"Error updating blog: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def delete(self):
        conn = None
        try:
            conn = get_connection()
            with conn.cursor() as cur:
                sql = """
                    DELETE FROM blogs
                    WHERE id = %s
                    RETURNING id;
                """
                cur.execute(sql, (self.id,))
                row = cur.fetchone()
                if row:
                    conn.commit()
                    print(f"Blog deleted with id={row[0]}")
                else:
                    raise ValueError(f"No blog found with id={self.id}")
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"Error deleting blog: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def translate_and_speak(self, source_lang, target_lang):
        """
        Translates the blog content from source_lang to target_lang
        and generates speech audio for the translation.
        Returns translated text and the audio file path.
        """
        translated_text = None
        audio_file_path = None

        try:
            # 1. Translate blog content
            translator = Translator(from_lang=source_lang, to_lang=target_lang)
            translated_text = translator.translate(self.content)

            # 2. Generate speech audio file
            audio_folder = "audio"
            if not os.path.exists(audio_folder):
                os.makedirs(audio_folder)
            audio_file_path = os.path.join(audio_folder, f"blog_{self.id}_audio.mp3")
            tts = gTTS(text=translated_text, lang=target_lang)
            tts.save(audio_file_path)

            # 3. Play audio depending on the OS
            os_type = platform.system()
            if os_type == 'Darwin':
                play_command = f"afplay '{audio_file_path}'"
            elif os_type == 'Linux':
                play_command = f"mpg123 '{audio_file_path}'"
            elif os_type == 'Windows':
                play_command = f"start {audio_file_path}"
            else:
                play_command = None

            if play_command:
                os.system(play_command)
            else:
                print("Audio playback not supported on this OS.")

            return {
                "translated_text": translated_text,
                "audio_file_path": audio_file_path
            }
        except Exception as e:
            print("Error during translation or TTS:", e)
            return {
                "translated_text": None,
                "audio_file_path": None,
                "error": str(e)
            }


    @staticmethod
    def to_dict(blog):
        """Return a dict suitable for JSON serialization from a Blog instance."""
        return {
            "id": blog.id,
            "title": blog.title,
            "content": blog.content,
            "created_at": blog.created_at.isoformat() if isinstance(blog.created_at, (datetime,)) and blog.created_at else blog.created_at,
            "updated_at": blog.updated_at.isoformat() if isinstance(blog.updated_at, (datetime,)) and blog.updated_at else blog.updated_at
        }

    @staticmethod
    def get_all():
        conn = None
        blogs = []
        try:
            conn = get_connection()
            with conn.cursor() as cur:
                sql = "SELECT id, title, content, created_at, updated_at FROM blogs ORDER BY id ASC"
                cur.execute(sql)
                rows = cur.fetchall()
                # Use map with lambda as per the constraints
                blogs = list(map(lambda row: Blog(
                    id=row[0], title=row[1], content=row[2],
                    created_at=row[3], updated_at=row[4]
                ), rows))
            return blogs
        except Exception as e:
            print("Error fetching all blogs:", e)
            return []
        finally:
            if conn:
                conn.close()

    @staticmethod
    def get_by_id(id):
        conn = None
        try:
            conn = get_connection()
            with conn.cursor() as cur:
                sql = "SELECT id, title, content, created_at, updated_at FROM blogs WHERE id = %s"
                cur.execute(sql, (id,))
                row = cur.fetchone()
                if row:
                    return Blog(
                        id=row[0], title=row[1], content=row[2],
                        created_at=row[3], updated_at=row[4]
                    )
                else:
                    return None
        except Exception as e:
            print("Error fetching blog by id:", e)
            return None
        finally:
            if conn:
                conn.close()

if __name__ == "__main__":
    blog = Blog(title="My First Blog", content="This is the content of my first blog.")
    blog.save()
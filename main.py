import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
import yt_dlp
import threading

class SavageDownloader(App):
    def build(self):
        self.title = "Savage Downloader 💀"
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        header = Label(text="⚡ SAVAGE DOWNLOADER ⚡", font_size='24sp', bold=True, color=(0, 1, 0, 1))
        layout.add_widget(header)
        self.url_input = TextInput(hint_text="Link or Artist - Song...", multiline=False, size_hint_y=None, height=100)
        layout.add_widget(self.url_input)
        self.btn = Button(text="RIP IT! 💀", background_color=(0, 0.5, 0, 1), size_hint_y=None, height=100)
        self.btn.bind(on_press=self.start_download_thread)
        layout.add_widget(self.btn)
        self.log = Label(text="Status: Ready...", halign='center', color=(0.8, 0.8, 0.8, 1))
        layout.add_widget(self.log)
        return layout

    def update_log(self, text):
        Clock.schedule_once(lambda dt: setattr(self.log, 'text', text))

    def start_download_thread(self, instance):
        threading.Thread(target=self.download_logic).start()

    def download_logic(self):
        text = self.url_input.text.strip()
        if not text:
            self.update_log("❌ Enter something, bobo! 🤣")
            return
        self.update_log("🚀 Ripping content... ⚡")
        download_path = "/storage/emulated/0/Download/SavageDownloader/"
        if not os.path.exists(download_path): os.makedirs(download_path)
        try:
            if text.startswith("http"):
                if "open.spotify.com" in text:
                    self.update_log("❌ Spotify links blocked! Use Artist - Song 🎵")
                    return
                target_url = text
                if "tiktok.com" in text:
                    ydl_opts = {'format': 'best', 'outtmpl': f"{download_path}%(title)s.%(ext)s"}
                elif "facebook.com" in text or "fb.watch" in text:
                    ydl_opts = {'format': 'best', 'outtmpl': f"{download_path}%(title)s.%(ext)s"}
                else:
                    ydl_opts = {'format': 'best[height<=720]+bestaudio/best[height<=720]', 'outtmpl': f"{download_path}%(title)s.%(ext)s", 'merge_output_format': 'mp4'}
            else:
                target_url = f"ytsearch:{text}"
                ydl_opts = {'format': 'bestaudio/best', 'outtmpl': f"{download_path}%(title)s.%(ext)s", 'noplaylist': True}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(target_url, download=True)
                if isinstance(info, list): info = info[0]
            self.update_log(f"✅ SUCCESS!\nSaved to Download folder 🎯")
        except Exception as e:
            self.update_log(f"❌ ERROR: {str(e)}")

if __name__ == "__main__":
    SavageDownloader().run()

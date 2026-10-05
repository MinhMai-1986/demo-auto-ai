import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ContextSyncHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            return
        print(f"[AUTO-SYNC] Phát hiện thay đổi: {event.src_path}")
        try:
            subprocess.run(["git", "add", ".context"], check=True)
            subprocess.run(["git", "commit", "-m", "Auto sync context from NotebookLM"], check=False)
            subprocess.run(["git", "push"], check=True)
            print("[AUTO-SYNC] Đã tự động đồng bộ thành công lên GitHub!")
        except Exception as e:
            print(f"[AUTO-SYNC LỖI] {e}")

if __name__ == "__main__":
    path = ".context"
    event_handler = ContextSyncHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    print(f"[AUTO-SYNC MANAGER] Đang theo dõi thư mục: {path}...")
    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

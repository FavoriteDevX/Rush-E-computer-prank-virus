"""
Rush E Synchronized Advanced Prank Engine
Author: GitHub Prank Architect
Description: A highly complex, harmless simulation prank that synchronizes advanced UI 
             anomalies (terminal mock screens, bouncing apps, and error matrix cascades) 
             with the accelerating tempo of the "Rush E" melody.
License: MIT
"""

import tkinter as tk
from tkinter import messagebox
import threading
import time
import random
import sys

if sys.platform == "win32":
    import winsound
    def play_tone(frequency, duration):
        try:
            winsound.Beep(frequency, duration)
        except:
            pass
else:
    import os as platform_os
    def play_tone(frequency, duration):
        platform_os.system(f'play -n synth {duration/1000} sin {frequency} > /dev/null 2>&1')

class RushEPrankEngine:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.is_running = True
        self.spawned_windows = []
        self.bouncing_apps = []
        
        # Comprehensive Rush E Melodic Array (Frequency in Hz, Duration in ms)
        self.rush_e_notes = [
            # Phase 1: Slow Intro (Melodic buildup)
            (659, 400), (659, 400), (659, 400), (523, 300), (659, 400), (784, 600), (392, 600),
            (440, 400), (349, 400), (440, 400), (523, 300), (587, 400), (494, 600), (329, 600),
            # Phase 2: Acceleration & Simulated File Transfers
            (659, 300), (659, 300), (659, 300), (523, 200), (659, 300), (784, 400), (392, 400),
            (440, 250), (440, 250), (523, 200), (587, 250), (659, 250), (698, 250), (784, 300),
            # Phase 3: Frenetic Bouncing Apps & Terminal Matrices
            (659, 150), (659, 150), (659, 150), (659, 150), (659, 150), (659, 150), (659, 150), (659, 150),
            (659, 120), (698, 120), (784, 120), (880, 120), (659, 120), (698, 120), (784, 120), (880, 120),
            # Phase 4: Extreme Mode (Maximum Chaos Climax)
            (1318, 80), (1318, 80), (1318, 80), (1318, 80), (1244, 80), (1244, 80), (1244, 80), (1244, 80),
            (1175, 60), (1175, 60), (1175, 60), (1175, 60), (1109, 60), (1109, 60), (1109, 60), (1109, 60),
            (1046, 40), (1046, 40), (1046, 40), (1046, 40), (987, 40),  (987, 40),  (987, 40),  (987, 40)
        ]

    def show_disclaimer(self):
        return messagebox.askyesno(
            "Safe Prank Initialization",
            "This script is a harmless prank simulator that creates visual artifacts and sounds.\n\n"
            "It will NOT delete your files or damage your system.\n"
            "Press ESC or wait for the sequence to end to close all generated windows.\n\n"
            "Do you want to proceed?"
        )

    def trigger_visual_event(self, note_index, duration):
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()

        # Phase 1: Terminal Matrix Logs
        if note_index < 14:
            self.create_mock_terminal(sw, sh)
        
        # Phase 2: Fake File Deletions & Trash Simulation
        elif 14 <= note_index < 28:
            fake_files = ["System32_Core.dll", "User_Credentials_Backup.db", "Financial_Statement_2026.xlsx", "PrivateKey.pem"]
            chosen_file = random.choice(fake_files)
            self.create_fake_glitch_window(
                "Recycle Bin Overflow", 
                f"Moving critical resource to Trash: {chosen_file}", 
                sw, sh, bg_color="#d9534f", fg_color="white"
            )
        
        # Phase 3: Bouncing Apps & Swapping Window Coordinates
        elif 28 <= note_index < 44:
            app_names = ["Chrome.exe", "Discord.exe", "Spotify.exe", "Minecraft.exe", "Photoshop.exe", "Terminal.exe"]
            self.spawn_bouncing_app(random.choice(app_names), sw, sh)
            
            for app, dx, dy in self.bouncing_apps:
                try:
                    geom = app.geometry().split("+")
                    w_h = geom[0]
                    curr_x = int(geom[1])
                    curr_y = int(geom[2])
                    new_x = (curr_x + dx * 2) % (sw - 200)
                    new_y = (curr_y + dy * 2) % (sh - 150)
                    app.geometry(f"{w_h}+{new_x}+{new_y}")
                except:
                    pass
        
        # Phase 4: Extreme Audio-Visual Frenzy
        else:
            self.flash_screen()
            for app, _, _ in self.bouncing_apps:
                try:
                    app.geometry(f"160x100+{random.randint(50, sw-210)}+{random.randint(50, sh-160)}")
                except:
                    pass

    def create_mock_terminal(self, sw, sh):
        win = tk.Toplevel(self.root)
        win.title("Administrator: Command Prompt")
        win.configure(bg="black")
        win.attributes("-topmost", True)
        
        w, h = 400, 200
        x = random.randint(50, sw - 450)
        y = random.randint(50, sh - 250)
        win.geometry(f"{w}x{h}+{x}+{y}")
        
        txt = tk.Text(win, bg="black", fg="#00FF00", font=("Consolas", 9), bd=0, highlightthickness=0)
        txt.pack(expand=True, fill="both", padx=5, pady=5)
        
        logs = [
            "[-] Connecting to remote payload delivery systems...",
            "[!] Warning: System internal core registers overriding.",
            "[*] Bypassing administrative user control loops...",
            "[-] Allocating dynamic RAM addresses for Rush_E.dll",
            "[+] Local storage indexing completed successfully."
        ]
        
        def type_log(index=0):
            if index < len(logs):
                try:
                    txt.insert(tk.END, logs[index] + "\n")
                    txt.see(tk.END)
                    win.after(120, type_log, index + 1)
                except:
                    pass
        
        type_log()
        self.spawned_windows.append(win)

    def spawn_bouncing_app(self, app_name, sw, sh):
        win = tk.Toplevel(self.root)
        win.title(app_name)
        win.geometry(f"160x100+{random.randint(100, sw-300)}+{random.randint(100, sh-250)}")
        win.configure(bg="#1e1e24")
        win.attributes("-topmost", True)
        
        lbl = tk.Label(win, text=f"⚠️ {app_name}\nRelocating...", bg="#1e1e24", fg="#f5cb5c", font=("Arial", 10, "bold"))
        lbl.pack(expand=True)
        
        dx = random.choice([-25, -15, 15, 25])
        dy = random.choice([-25, -15, 15, 25])
        
        self.bouncing_apps.append((win, dx, dy))
        self.spawned_windows.append(win)

    def create_fake_glitch_window(self, title, message, sw, sh, bg_color="white", fg_color="black"):
        win = tk.Toplevel(self.root)
        win.title(title)
        win.attributes("-topmost", True)
        
        w, h = 340, 130
        x = random.randint(100, sw - 440)
        y = random.randint(100, sh - 240)
        win.geometry(f"{w}x{h}+{x}+{y}")
        
        win.configure(bg=bg_color)
        label = tk.Label(win, text=message, bg=bg_color, fg=fg_color, font=("Courier", 10, "bold"), wraplength=300)
        label.pack(expand=True, fill="both", padx=10, pady=10)
        
        self.spawned_windows.append(win)
        
        for _ in range(4):
            win.geometry(f"{w}x{h}+{x + random.randint(-15, 15)}+{y + random.randint(-15, 15)}")
            win.update()
            time.sleep(0.02)

    def flash_screen(self):
        flash = tk.Toplevel(self.root)
        flash.attributes("-fullscreen", True, "-topmost", True)
        flash.configure(bg=random.choice(["#000000", "#ff0055", "#0055ff"]))
        flash.update()
        time.sleep(0.04)
        flash.destroy()

    def run_audio_engine(self):
        for idx, (freq, dur) in enumerate(self.rush_e_notes):
            if not self.is_running:
                break
            
            self.root.after(0, self.trigger_visual_event, idx, dur)
            play_tone(freq, dur)
            time.sleep(0.02)
            
        if self.is_running:
            self.root.after(0, self.trigger_fake_bsod)

    def trigger_fake_bsod(self):
        bsod = tk.Toplevel(self.root)
        bsod.attributes("-fullscreen", True, "-topmost", True)
        bsod.configure(bg="#0078D7")
        
        bsod_text = (
            ":( \n\n"
            "Your PC ran into a problem and needs to restart. We're just\n"
            "collecting some error info, and then we'll restart for you.\n\n"
            "0% complete\n\n"
            "For more information about this issue and possible fixes, visit:\n"
            "https://github.com/yourusername/rush-e-advanced-engine\n\n"
            "Stop Code: RUSH_E_INSTRUMENTAL_OVERLOAD\n"
            "What failed: PianoSmasher.sys"
        )
        
        lbl = tk.Label(bsod, text=bsod_text, bg="#0078D7", fg="white", font=("Segoe UI", 22), justify="left")
        lbl.pack(anchor="w", padx=100, pady=150)
        
        self.root.after(6000, self.terminate_engine)

    def bind_safety_keys(self):
        self.root.bind_all("<Escape>", lambda e: self.terminate_engine())

    def terminate_engine(self):
        self.is_running = False
        for win in self.spawned_windows:
            try:
                win.destroy()
            except:
                pass
        self.root.destroy()
        sys.exit()

if __name__ == "__main__":
    engine = RushEPrankEngine()
    if engine.show_disclaimer():
        engine.bind_safety_keys()
        
        audio_thread = threading.Thread(target=engine.run_audio_engine, daemon=True)
        audio_thread.start()
        
        engine.root.mainloop()
    else:
        sys.exit()

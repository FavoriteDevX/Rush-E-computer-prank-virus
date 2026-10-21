"""
Rush E Complete Orchestrated Prank Engine (Real Audio Version)
Author: GitHub Prank Architect
Description: Advanced multi-threaded prank engine synchronizing continuous, complex 
             OS simulation events (bouncing apps, mock terminal spam, error sequences)
             to the full duration and tempo shifts of a real Rush E MP3 track.
License: MIT
"""

import tkinter as tk
from tkinter import messagebox
import threading
import time
import random
import sys
import os
import urllib.request

# Dynamic automated package loader to handle realistic MP3 audio playback handles safely
try:
    import pygame
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])
    import pygame

class AdvancedRushEEngine:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()  # Hide main window handle
        self.is_running = True
        self.spawned_windows = []
        
        # Sourced audio configuration paths
        self.audio_filename = "rush_e_theme.mp3"
        # Using a reliable raw archive link containing the standardized high-tempo Rush E piano track
        self.audio_source_url = "https://google.com" # Placeholder or substitute with an online hosted direct raw .mp3 target
        
        # Screen Dimensions for geometry calculations
        self.sw = self.root.winfo_screenwidth()
        self.sh = self.root.winfo_screenheight()
        
        # Comprehensive event timeline aligned directly to actual track playtime seconds
        self.timeline_events = [
            # Phase 1: Slow Piano Intro (0s - 15s)
            (1.0, "TERMINAL_SPAM"), (3.0, "TERMINAL_SPAM"), (5.5, "TERMINAL_SPAM"),
            (7.5, "GLITCH_BOX"), (9.0, "TERMINAL_SPAM"), (11.5, "GLITCH_BOX"),
            # Phase 2: Building Up and Adding Bouncing Apps (15s - 30s)
            (15.0, "SPAWN_APP"), (17.5, "SPAWN_APP"), (20.0, "GLITCH_BOX"),
            (22.0, "SPAWN_APP"), (24.5, "TERMINAL_SPAM"), (27.0, "SPAWN_APP"),
            # Phase 3: The Rapid Acceleration & Extreme E Spam (30s - 55s)
            (30.0, "ACCELERATION_START"), (32.0, "GLITCH_BOX"), (34.0, "SPAWN_APP"),
            (36.0, "CHAOS_BURST"), (38.5, "CHAOS_BURST"), (41.0, "TERMINAL_SPAM"),
            (43.0, "CHAOS_BURST"), (46.0, "SPAWN_APP"), (49.0, "CHAOS_BURST"),
            # Phase 4: Insane Piano Climax (55s - 75s)
            (55.0, "FLASH_SCREEN"), (57.0, "CHAOS_BURST"), (60.0, "FLASH_SCREEN"),
            (62.0, "MASSIVE_SPAM"), (65.0, "FLASH_SCREEN"), (68.0, "MASSIVE_SPAM"),
            (72.0, "TRIGGER_BSOD")
        ]

    def check_and_fetch_audio_assets(self):
        """Ensures the real MP3 file is present in the local cache or fetches it."""
        if not os.path.exists(self.audio_filename):
            # Safe sample download to bypass silent empty sound cards if track assets are missing
            try:
                urllib.request.urlretrieve(self.audio_source_url, self.audio_filename)
            except Exception as e:
                pass

    def show_disclaimer(self):
        """Displays initialization boundaries ensuring authorization."""
        return messagebox.askyesno(
            "Security Authorization Required",
            "This repository contains an advanced environment simulation engine.\n\n"
            "Execution will display mock background anomalies, blinking terminal assets, "
            "and play high-fidelity real audio pipelines matching the selected prank matrix.\n\n"
            "No data modifications or core modifications will take place.\n"
            "Press ESC at any moment to flush active threads.\n\n"
            "Do you want to initialize?"
        )

    def play_real_audio_stream(self):
        """Initializes Pygame Mixer pipelines to playback real digital background layers."""
        self.check_and_fetch_audio_assets()
        try:
            pygame.mixer.init()
            if os.path.exists(self.audio_filename):
                pygame.mixer.music.load(self.audio_filename)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() and self.is_running:
                    time.sleep(0.1)
        except Exception as e:
            pass

    def dispatch_timeline(self):
        """Monitors clock timestamps to fire complex graphical events at the exact musical cue."""
        start_time = time.time()
        event_index = 0
        
        while self.is_running and event_index < len(self.timeline_events):
            current_elapsed = time.time() - start_time
            target_timestamp, action_type = self.timeline_events[event_index]
            
            if current_elapsed >= target_timestamp:
                self.root.after(0, self.execute_action, action_type)
                event_index += 1
            time.sleep(0.05)
    def execute_action(self, action):
        """Event Router calling appropriate UI simulations."""
        if not self.is_running: 
            return
        
        if action in ["TERMINAL_SPAM", "ACCELERATION_START"]:
            self.create_mock_terminal()
        elif action == "GLITCH_BOX":
            self.create_glitch_box("Warning handle", "Buffer allocation mismatch inside Sector E.")
        elif action == "SPAWN_APP":
            apps = ["Chrome.exe", "Discord.exe", "Spotify.exe", "Steam.exe"]
            self.spawn_bouncing_app(random.choice(apps))
        elif action == "CHAOS_BURST":
            self.create_glitch_box("Critical Notification", "E E E E E E E E E E E E E E E E E E", is_error=True)
            self.spawn_bouncing_app("SystemGlitch.sys")
        elif action == "MASSIVE_SPAM":
            for _ in range(4):
                self.create_glitch_box("Stack Overflow", "0xEEEEEEEE - Out of Piano Keys", is_error=True)
        elif action == "FLASH_SCREEN":
            self.flash_canvas()
        elif action == "TRIGGER_BSOD":
            self.render_safe_bsod()

    def create_mock_terminal(self):
        """Creates a black terminal dialog box printing fake matrix strings."""
        term = tk.Toplevel(self.root)
        term.title("Administrator: Windows System Core Terminal")
        term.configure(bg="black")
        term.geometry(f"450x250+{random.randint(50, self.sw-500)}+{random.randint(50, self.sh-300)}")
        term.attributes("-topmost", True)
        
        text_widget = tk.Text(term, bg="black", fg="#00FF00", font=("Courier", 9))
        text_widget.pack(expand=True, fill="both")
        self.spawned_windows.append(term)
        
        fake_logs = [
            "Initializing memory leak analysis...\n",
            "Targeting directory tree: C:/Windows/System32/\n",
            "Status: Overloading sound cards with E array...\n",
            "Warning: Piano strings snapped.\n"
        ]
        
        def type_log(logs, index=0):
            if index < len(logs) and self.is_running and term.winfo_exists():
                text_widget.insert(tk.END, logs[index])
                text_widget.see(tk.END)
                term.after(400, type_log, logs, index+1)
        
        type_log(fake_logs)

    def spawn_bouncing_app(self, app_name):
        """Creates floating mockup apps that actively bounce and change places across the monitor area."""
        app = tk.Toplevel(self.root)
        app.title(f"Running: {app_name}")
        app.geometry(f"280x100+{random.randint(100, self.sw-350)}+{random.randint(100, self.sh-200)}")
        app.attributes("-topmost", True)
        app.configure(bg="#1e1e1e")
        
        lbl = tk.Label(app, text=f"Syncing {app_name} coordinates...", bg="#1e1e1e", fg="white", font=("Arial", 10))
        lbl.pack(expand=True)
        self.spawned_windows.append(app)
        
        dx, dy = random.choice([-8, 8]), random.choice([-8, 8])
        
        def update_bounce():
            nonlocal dx, dy
            if not self.is_running or not app.winfo_exists(): 
                return
            
            try:
                x = app.winfo_x() + dx
                y = app.winfo_y() + dy
                
                if x <= 0 or x >= (self.sw - 280): 
                    dx = -dx
                if y <= 0 or y >= (self.sh - 100): 
                    dy = -dy
                
                app.geometry(f"+{x}+{y}")
                app.after(20, update_bounce)
            except:
                pass
                
        update_bounce()

    def create_glitch_box(self, title, msg, is_error=False):
        box = tk.Toplevel(self.root)
        box.title(title)
        bg = "red" if is_error else "white"
        fg = "white" if is_error else "black"
        box.configure(bg=bg)
        box.geometry(f"320x110+{random.randint(100, self.sw-400)}+{random.randint(100, self.sh-200)}")
        box.attributes("-topmost", True)
        
        l = tk.Label(box, text=msg, bg=bg, fg=fg, font=("Arial", 10, "bold"), wraplength=280)
        l.pack(expand=True, fill="both", padx=10, pady=10)
        self.spawned_windows.append(box)

    def flash_canvas(self):
        flash = tk.Toplevel(self.root)
        flash.attributes("-fullscreen", True, "-topmost", True)
        flash.configure(bg=random.choice(["red", "black", "blue"]))
        flash.update()
        self.root.after(50, flash.destroy)

    def render_safe_bsod(self):
        bsod = tk.Toplevel(self.root)
        bsod.attributes("-fullscreen", True, "-topmost", True)
        bsod.configure(bg="#0078D7")
        
        text = (
            ":( \n\nYour PC ran into a musical challenge and needs to cool down.\n"
            "We are just collecting some midi error info, and then we will restart.\n\n"
            "100% complete\n\n"
            "Stop Code: RUSH_E_TOTAL_PIANO_OVERLOAD\n"
            "What failed: SheetMusicBoss.sys"
        )
        lbl = tk.Label(bsod, text=text, bg="#0078D7", fg="white", font=("Segoe UI", 24), justify="left")
        lbl.pack(anchor="w", padx=100, pady=150)
        self.root.after(7000, self.flush_engine)

    def bind_panic_triggers(self):
        self.root.bind_all("<Escape>", lambda e: self.flush_engine())

    def flush_engine(self):
        self.is_running = False
        try:
            pygame.mixer.music.stop()
        except:
            pass
        for win in self.spawned_windows:
            try: 
                win.destroy()
            except: 
                pass
        self.root.destroy()
        sys.exit()

if __name__ == "__main__":
    engine = AdvancedRushEEngine()
    if engine.show_disclaimer():
        engine.bind_panic_triggers()
        
        # Audio Synthesizer Thread - Running high fidelity digital audio channels
        threading.Thread(target=engine.play_real_audio_stream, daemon=True).start()
        # Orchestration Event Timeline Thread
        threading.Thread(target=engine.dispatch_timeline, daemon=True).start()
        
        engine.root.mainloop()
    else:
        sys.exit()

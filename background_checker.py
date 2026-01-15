import json
import os
import sys
import random
from datetime import datetime
from plyer import notification
import pygame
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align

console = Console()
current_dir = os.path.dirname(os.path.abspath(__file__)) # gets the directory path
json_path = os.path.join(current_dir, 'birthdays.json') # defines the file path to the database
sound_path = os.path.join(current_dir, 'alert.mp3') #alert sound import
# randomized gift ideas
GIFT_IDEAS = [
    "Portable Power Bank", "Insulated Water Bottle", "Bluetooth Speaker", 
    "₱250 in their Gcash", "Scented Candle", "Wireless Earbuds", 
    "Desk Plant (Succulent)", "Comfortable Hoodie", "Coffee/Tea Set",
    "Digital Photo Frame", "Board Game (e.g Monopoly)", "Journal & Pen Set", "An Umbrella"
]
#initializes the alert sound
def play_alert_sound():
    if os.path.exists(sound_path):
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(sound_path)
            pygame.mixer.music.play()
        except: pass
#the notification popup
def show_popup_console(title, message, border_color):
    play_alert_sound() #plays "alert.mp3"
    os.system('cls' if os.name == 'nt' else 'clear')
    
    gift = random.choice(GIFT_IDEAS)
    full_message = f"{message}\n\n[bold white]🎁 Gift Idea:[/bold white] [italic]{gift}[/italic]"
    
    panel = Panel(
        Align.center(full_message),
        title=f"[bold white]{title}[/bold white]",
        subtitle="[dim]Press Enter to see next or close[/dim]",
        style="white",
        padding=(2, 4),
        border_style=border_color 
    )
    console.print(panel)
    input()
# checks what day/date it is and who has a birthday
def check_reminders():
    if not os.path.exists(json_path): return
    with open(json_path, 'r') as f:
        try: birthdays = json.load(f)
        except: return

    today = datetime.now()
    found_event = False
    
    for person in birthdays:
        try:
            bday = datetime(today.year, person["month"], person["day"])
            delta = (bday.date() - today.date()).days #for the date delta algo

            if delta == 0:
                # Today popup
                notification.notify(title="Birthday Today! 🎂", message=f"It's {person['name']}'s birthday!", timeout=10)
                
                show_popup_console(
                    "🎉 HAPPY BIRTHDAY! 🎉", 
                    f"\n[bold cyan1]{person['name']}[/bold cyan1] is celebrating today!\nGreet them immediately!", 
                    "gold1"
                )
                found_event = True

            elif delta == 1:
                # Popup a day before the birthday
                notification.notify(title="Upcoming Birthday 📅", message=f"{person['name']} tomorrow! yes tomorrow!!", timeout=10)
                show_popup_console(
                    "⚠️ UPCOMING EVENT ⚠️", 
                    f"\n[bold cyan1]{person['name']}[/bold cyan1] has a birthday tomorrow!!\nTime to buy a card.", 
                    "yellow"
                )
                found_event = True

            elif delta == 2:
                # Popup 2 days before the birthday
                notification.notify(title="Upcoming Birthday 📅", message=f"{person['name']} in 2 days!", timeout=10)
                show_popup_console(
                    "⚠️ UPCOMING EVENT ⚠️", 
                    f"\n[bold cyan1]{person['name']}[/bold cyan1] has a birthday in 2 Days!\nTime to buy a card.", 
                    "yellow"
                )
                found_event = True

        except: continue #ignores bad data
    #waits for input and prevents forever playing of alert 
    if found_event:
        try: pygame.mixer.music.stop()
        except: pass # prevents crashes if no sound loaded

if __name__ == "__main__":
    check_reminders()
import sys 
import os
import time
import subprocess #messenger between python and windows 
import calendar
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.align import Align
from rich.progress import track
from rich.prompt import Prompt
from rich import box
from hash_table import BirthdayHash
from utils import is_valid_date

CONSOLE = Console()
ht = BirthdayHash() 

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
# Simulation of loading bars
def anim_load(desc="Processing...", duration=0.03, steps=50):
    for _ in track(range(steps), description=f"[gold1]{desc}[/gold1]", transient=True):
        time.sleep(duration)
# sets up the window task scheduler using windows command
def background_reminder():
    CONSOLE.print(Panel("[gold1]Setup Persistent Reminders[/gold1]", border_style="gold1"))
    
    python_exe = sys.executable # Ensures python runs on the correct version
    script_dir = os.path.dirname(os.path.abspath(__file__)) # gets the dir path
    checker_script = os.path.join(script_dir, "background_checker.py") #checks background_checker.py
    bat_script = os.path.join(script_dir, "launcher.bat") # creates the launcher

    anim_load("Configuring Launcher Script...")
    with open(bat_script, "w") as f:
        f.write(f'@echo off\ncd /d "{script_dir}"\n"{python_exe}" "{checker_script}"\nif %errorlevel% neq 0 pause\n')

    CONSOLE.print("\n[cyan]Enter the time you want to be notified daily.[/cyan]")
    user_time = Prompt.ask("[bold white]Time (HH:MM 24h format)[/bold white]").strip() # strip removes the white spaces
    
    if ":" not in user_time:
        CONSOLE.print("[red]Invalid Format[/red]")
        time.sleep(1); return #requires user to use ":"

    anim_load("Registering with Windows Task Scheduler...", duration=0.05)
    task_name = "YagballsBirthdayCheck" #name of the task
    
    cmd = ['schtasks', '/Create', '/SC', 'DAILY', '/TN', task_name, '/TR', f'"{bat_script}"', '/ST', user_time, '/F'] # the windows command
    subprocess.run(cmd, capture_output=True)
    
    # shell command to run even on battery 
    ps_cmd = (
        f"powershell -Command \"$t = Get-ScheduledTask -TaskName '{task_name}'; "
        f"$t.Settings.StartWhenAvailable = $true; "
        f"$t.Settings.AllowStartIfOnBatteries = $true; "
        f"$t.Settings.DontStopIfGoingOnBatteries = $true; "
        f"Set-ScheduledTask -InputObject $t\""
    )
    subprocess.run(ps_cmd, shell=True, capture_output=True) #ensures we use powershell commands rather than standar CMD ones
    
    CONSOLE.print(f"[green bold]Success! Reminder set for {user_time}.[/green bold]")
    time.sleep(2)
  #Generates a mini calendar table for a single month.
def get_month_panel(year, month, all_bdays):
    cal_table = Table(
        title=f"[bold cyan]{calendar.month_name[month]}[/bold cyan]", 
        box=box.SIMPLE_HEAD, 
        padding=0, 
        expand=True
    )
    for day in list(calendar.day_abbr):
        cal_table.add_column(day, justify="center", style="dim white")

    month_days = calendar.monthcalendar(year, month)
    today = datetime.now()

    for week in month_days:
        week_row = []
        for day in week:
            if day == 0:
                week_row.append("")
            else:
                names = [b['name'] for b in all_bdays if b['month'] == month and b['day'] == day]
                day_str = str(day)
                if today.year == year and today.month == month and today.day == day:
                    day_str = f"[black on green]{day}[/]" # Today
                elif names:
                    day_str = f"[bold white on red]{day}[/]" # Birthday
                week_row.append(day_str)
        cal_table.add_row(*week_row)
    return Panel(cal_table, border_style="dim blue")
#displays the people who has birthday today
def get_todays_panel(all_bdays):
    today = datetime.now()
    todays_names = [b['name'] for b in all_bdays if b['month'] == today.month and b['day'] == today.day]
    
    content = ""
    if todays_names:
        content = "\n".join([f"🎂 [bold cyan1]{name}[/bold cyan1]" for name in todays_names])
    else:
        content = "[dim white]No birthdays today[/dim white]"

    return Panel(
        Align.center(f"\n{content}\n"),
        title="[bold gold1]✨ TODAY ✨[/bold gold1]", 
        style="white", 
        border_style="gold1", 
        expand=True
    )
#the grid to display all 12 months, 5 months per row
def display_year_view(year):
    """Displays 12 months in a 5-column grid."""
    CONSOLE.print(f"\n[bold gold1]--- YEAR VIEW: {year} ---[/bold gold1]", justify="center")
    
    all_bdays = ht.get_all_birthdays()
    
    grid = Table.grid(padding=1)
    for _ in range(5): grid.add_column()
    
    for q in range(0, 12, 5):
        row_panels = []
        for i in range(5):
            month_idx = q + i + 1
            if month_idx <= 12:
                row_panels.append(get_month_panel(year, month_idx, all_bdays))
            else:
                if month_idx == 13:
                    row_panels.append(get_todays_panel(all_bdays))
                else:
                    row_panels.append("")
        
        grid.add_row(*row_panels)

    CONSOLE.print(Align.center(grid))
# THE MAIN MENU
def main_menu():
    today = datetime.now()
    view_year = today.year
#prevents the prev screen to show up again
    clear_screen()
    anim_load("Initializing SYSTEM...", steps=20)

    while True:
        clear_screen()
        CONSOLE.print(Panel(Align.center("[bold cyan1 underline]🎂 YAGBALLS BIRTHDAY TRACKER 🎂[/bold cyan1 underline]\n[dim]DSA Project - Season 2[/dim]"), border_style="gold1"))
        
        display_year_view(view_year)
        
        CONSOLE.print(Align.center("[dim]Legend: [green]Today[/green] | [red]Birthday[/red][/dim]\n"))
        menu = Table.grid(padding=(0, 2))
        menu.add_column(style="bold white"); menu.add_column(style="bold white")
        menu.add_row("[gold1 bold][1][/gold1 bold]", "[green bold]Add Birthday 📝[/green bold]",     "[gold1 bold][5][/gold1 bold]", "[green bold]Next Year ➡️[/green bold]")
        menu.add_row("[gold1 bold][2][/gold1 bold]", "[green bold]Search Birthday 🔍[/green bold]",   "[gold1 bold][6][/gold1 bold]", "[green bold]Prev Year ⬅️[/green bold]")
        menu.add_row("[gold1 bold][3][/gold1 bold]", "[green bold]Delete Birthday 🗑️[/green bold]",    "[gold1 bold][7][/gold1 bold]", "[green bold]Exit 🚪[/green bold]")
        menu.add_row("[gold1 bold][4][/gold1 bold]", "[green bold]Enable Reminders 🔔[/green bold]",  "", "")
        CONSOLE.print(Align.center(menu))
        
        choice = Prompt.ask("\n[cyan]Select an option[/cyan]", choices=['1', '2', '3', '4', '5', '6', '7'])

        if choice == '1':
            CONSOLE.print(Panel("[gold1]Add New Entry[/gold1]", border_style="gold1"))
            name = Prompt.ask("[cyan]Name[/cyan]")
            date_str = Prompt.ask("[cyan]Date (MM-DD)[/cyan]")
            
            anim_load("Checking database...")
            if is_valid_date(date_str):
                m, d = map(int, date_str.split('-'))
                all_b = ht.get_all_birthdays()
                is_duplicate = any(b['name'].lower() == name.lower() and b['month'] == m and b['day'] == d for b in all_b)
                #prevents duplicate 
                if is_duplicate:
                     CONSOLE.print(f"[red bold]Warning: '{name}' with birthday {m}-{d} already exists![/red bold]")
                     if Prompt.ask("[yellow]Add anyway? (y/n)[/yellow]") != 'y':
                         continue
                
                ht.add_birthday(name, f"{m}-{d}") 
                CONSOLE.print("[green bold]Success! Entry Saved.[/green bold]")
            else:
                CONSOLE.print("[red bold]Invalid Date Format![/red bold]")
            time.sleep(1.5)

        
        elif choice == '2':
            CONSOLE.print(Panel("[gold1]Search Database[/gold1]", border_style="gold1"))
            query = Prompt.ask("[cyan]Enter Name or Date (MM-DD)[/cyan]").strip()
            
            anim_load("Searching...")
            
            results = []
            all_b = ht.get_all_birthdays()

            # Check if it's a DATE first
            if is_valid_date(query):
                m, d = map(int, query.split('-'))
                results = [b for b in all_b if b['month'] == m and b['day'] == d]
            else:
                # If not a date, assume it's a NAME
                results = [b for b in all_b if query.lower() in b['name'].lower()]
            
            if results:
                for f in results:
                    CONSOLE.print(f"[green]Found:[/green] {f['name']} on {f['month']}/{f['day']}")
            else:
                CONSOLE.print(f"[red]No matches found for '{query}'.[/red]")
            
            Prompt.ask("[dim]Press Enter...[/dim]")

        elif choice == '3':
            CONSOLE.print(Panel("[gold1]Delete Entry[/gold1]", border_style="gold1"))
            all_b = ht.get_all_birthdays()
            if not all_b:
                CONSOLE.print("[yellow]Database is empty.[/yellow]")
            else:
                list_table = Table(title="Available Entries", box=box.SIMPLE)
                list_table.add_column("Name", style="cyan")
                list_table.add_column("Date", style="magenta")
                for b in all_b:
                    list_table.add_row(b['name'], f"{b['month']}-{b['day']}")
                CONSOLE.print(list_table)
                
                name = Prompt.ask("[cyan]Name to delete[/cyan]")
                anim_load("Removing...")
                if ht.delete_birthday(name):
                    CONSOLE.print(f"[green]Deleted {name}.[/green]")
                else:
                    CONSOLE.print("[red]Name not found.[/red]")
            time.sleep(2)

        elif choice == '4': background_reminder()
        elif choice == '5': view_year += 1
        elif choice == '6': view_year -= 1
        elif choice == '7':
            anim_load("Saving Data...", steps=20)
            break

if __name__ == "__main__":
    try: main_menu()
    except KeyboardInterrupt: CONSOLE.print("\n[red]Force Exit.[/red]")
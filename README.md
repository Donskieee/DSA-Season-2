### YAGBALLS TEAM PRESENTS
# Y- Yeah A-Amazing G-Great. 
# Balls!? because we play ball YOLO!


# DSA-Season-2
Project for DSA (Hashing)
# 🎂 Yagballs Birthday Tracker (DSA Season 2)


A robust, console-based Birthday Calendar System built with Python. It features a custom **Hash Table** data structure for efficient data management, a beautiful Terminal User Interface (TUI), and persistent background reminders that work even after a PC restart.

---

## ✨ Key Features

### 🖥️ **Interactive Dashboard**
* **Year-at-a-Glance:** A dynamic 5-column grid layout displaying all 12 months.
* **Today Panel:** A special Golden Panel highlights anyone celebrating their birthday *today*.
* **Rich UI:** Professional styling with Gold borders and Cyan text using the `rich` library.
* **Loading Animations:** Smooth loading bars for system processes.

### 🔔 **Smart Persistent Reminders**
* **Background Worker:** Runs silently in the background using Windows Task Scheduler.
* **Custom Schedule:** Users choose exactly what time they want to be notified (e.g., 7:00 AM).
* **Resilient Logic:** If the PC is off during the scheduled time, the reminder auto-launches within 10 minutes of the next startup.

### 🎁 **Visual & Audio Alerts**
* **Popup Console:** A colorful window pops up on top of other apps to alert you.
* **Audio Alerts:** Plays `alert.mp3` when a birthday is found.
* **Gift Recommendations:** Randomly suggests a unisex gift idea (e.g., "Bluetooth Speaker", "Scented Candle") for the celebrant.

### 🧠 **Data Structures & Algorithms (DSA)**
* **Custom Hash Table:** Implements a hash map from scratch (no Python `dict` for storage).
* **Collision Handling:** Uses **Chaining** (Linked Lists/Arrays) to handle multiple birthdays on the same hash index.
* **Complexity:** Achieves **O(1)** average time complexity for adding, searching, and deleting entries.

---

## 📂 Project Structure

| File | Description |
| :--- | :--- |
| **`main.py`** | The main application interface. Handles the menu, calendar rendering, and user input. |
| **`hash_table.py`** | The custom Data Structure class. Handles hashing, buckets, and JSON saving/loading. |
| **`background_checker.py`** | The logic for the background task. Checks dates, triggers notifications, and plays sound. |
| **`utils.py`** | Helper functions for date validation. |
| **`birthdays.json`** | The database where student data is stored (Auto-created). |
| **`alert.mp3`** | The audio file played during notifications. |

---

## 🚀 Installation & Setup

### 1. Prerequisites
Ensure you have Python installed. Then, install the required dependencies:

```bash
pip install rich plyer pygame
```
### 2. Audio Setup
Place an MP3 file named **`alert.mp3`** inside the project folder. (Required for sound to work).

### 3. Run the App
Open your terminal (Command Prompt or PowerShell) and run Make sure its Administrator!:
```bash
python main.py
```
---

## 📖 How to Use

### Main Menu Options
1. **Add Birthday 📝**: Enter a Name and Date (MM-DD). The system checks for duplicates automatically.
2. **Search Birthday 🔍**: Find birthdays by Name or Date.
3. **Delete Birthday 🗑️**: View a table of all entries and select a name to remove.
4. **Enable Reminders 🔔**:
   * Input a time (e.g., `16:30`).
   * The app creates a **Windows Task**.
   * You can now close the app; you will be notified daily at that time!
5. **Disable Reminders 🔕**: Turns off the background task.
6. **Navigation**: Use **Next Year** and **Prev Year** to scroll through the calendar view.

---

## 🛠️ Troubleshooting

**"The reminders didn't pop up!"**
* Ensure you ran `main.py` as **Administrator** if you have permission issues.
* Check if `alert.mp3` exists in the folder.
* Check Windows "Focus Assist" or "Do Not Disturb" settings.

**"Module not found error"**
* Make sure you installed the requirements: `pip install rich plyer pygame`

---

## 👨‍💻 Credits

**DSA Yagballs Squad**
* Caiga, Ceasar Ivan A. - main.py, background_checker.py
* Calayag, James Mathew - main.py (menu section)
* Clarete, Marc Arthur -hash_table.py
* Magsila, Benjamin T III - main.py (calendar section)
* Noriesta, Don B. - utils.py

---
*Submitted to: Polytechnic University of the Philippines - Quezon City Branch*

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

### 2. Audio Setup
Place an MP3 file named **`alert.mp3`** inside the project folder. (Required for sound to work).

### 3. Run the App
Open your terminal (Command Prompt or PowerShell) and run Make sure its Administrator!:


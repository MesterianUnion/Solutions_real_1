import datetime
import json
import bot
import tkinter as tk
from tkinter import ttk, messagebox
from discord import app_commands
from models import Base, BotAnswer, BotSession
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import threading

# Database setup
engine = create_engine('sqlite:///bot_database.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


# GUI code

class BotControlGUI:
    def __init__(self, master):
        self.master = master
        master.title("Discord Bot Control")

        self.start_button = tk.Button(master, text="Start Bot", command=self.start_bot)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop Bot", command=self.stop_bot)
        self.stop_button.pack()

        self.create_answers_table()
        self.create_sessions_table()

    def start_bot(self):
        # Placeholder: Add code to start the bot
        messagebox.showinfo("Bot Control", "Bot started successfully.")

    def stop_bot(self):
        # Placeholder: Add code to stop the bot
        messagebox.showinfo("Bot Control", "Bot stopped successfully.")

    def create_answers_table(self):
        answers_frame = ttk.Frame(self.master)
        answers_frame.pack(pady=10)

        self.answers_tree = ttk.Treeview(answers_frame)
        self.answers_tree["columns"] = ("ID", "Answer", "Command Used", "User", "Timestamp")

        # Set the width of the "ID" column to a maximum of 20
        self.answers_tree.column("#1", width=50)
        self.answers_tree.column("#4", width=150)

        # Set the width of the The treeview
        self.answers_tree.column("#0", width=0)

        self.answers_tree.heading("#1", text="ID")
        self.answers_tree.heading("#2", text="Answer")
        self.answers_tree.heading("#3", text="Command Used")
        self.answers_tree.heading("#4", text="User")
        self.answers_tree.heading("#5", text="Timestamp")
        self.answers_tree.pack()

        self.populate_answers_table()



    def create_sessions_table(self):
        sessions_frame = ttk.Frame(self.master)
        sessions_frame.pack(pady=10)

        self.sessions_tree = ttk.Treeview(sessions_frame)
        self.sessions_tree["columns"] = ("ID", "Start Time", "End Time")
        self.sessions_tree.heading("#1", text="ID")
        self.sessions_tree.heading("#2", text="Start Time")
        self.sessions_tree.heading("#3", text="End Time")
        self.sessions_tree.pack()

        self.populate_sessions_table()

    def populate_answers_table(self):
        # Fetch data from the 'bot_answers' table and display it
        session = Session()
        answers = session.query(BotAnswer).all()

        # Clear existing items in the Treeview
        for item in self.answers_tree.get_children():
            self.answers_tree.delete(item)

        # Display data in the Treeview
        ######
        for answer in answers:
            self.answers_tree.insert("", "end", values=(answer.id, answer.answer, answer.command_used, answer.user, answer.timestamp))

    def populate_sessions_table(self):
        # Fetch data from the 'bot_sessions' table and display it
        session = Session()
        sessions = session.query(BotSession).all()

        # Clear existing items in the Treeview
        for item in self.sessions_tree.get_children():
            self.sessions_tree.delete(item)

        # Display data in the Treeview
        for session_data in sessions:
            self.sessions_tree.insert("", "end", values=(session_data.id, session_data.start_time, session_data.end_time))


if __name__ == '__main__':
    # Run the bot in a separate thread
    def run_bot():
        bot.run_discord_bot()

    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()

    # Create and run the GUI
    root = tk.Tk()
    gui = BotControlGUI(root)
    root.mainloop()

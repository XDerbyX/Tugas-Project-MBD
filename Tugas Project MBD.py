import tkinter as tk
from ttkbootstrap import Separator, Window
from tkinter import messagebox
from tkinter.ttk import Treeview, Scrollbar
import mysql.connector

# Kelompok Servis Bengkel Mobil
# D121221082 | Muh. Naufal Jalaluddin
# D121221072 | Muh. Wahyu Ramadhan

# Functions
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="123456",
            database="Servis_Mobil"
        )
        return connection
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to connect to database: {error}")
        return None

def search_pelanggan(search_term):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(prepared=True) # Prepared Statement
        query = "SELECT * FROM Pelanggan WHERE Nama_Pelanggan LIKE %s"
        cursor.execute(query, ('%' + search_term + '%',))
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result

def display_search_results(search_results):
    # Clear previous search results
    for row in output_table.get_children():
        output_table.delete(row)

    # Insert new search results
    for i, pelanggan in enumerate(search_results):
        output_table.insert("", "end", values=pelanggan)

def open_insert_window():
    insert_window = tk.Toplevel(root)
    insert_window.title("Insert Data Pelanggan")
    
    # Input Label
    label_input = tk.Label(insert_window, text="Input Data-Data Pelanggan", font=("Helvetica", 15, "bold"))
    label_input.grid(row=0, column=0, columnspan=5, padx=(0,0), pady=(0,115), sticky="ew")
    
    separator = Separator(insert_window, orient="horizontal")
    separator.grid(row=0, column=0, columnspan=5,padx=(0,0), pady=(0,60), sticky="ew")
    
    # Labels
    tk.Label(insert_window, text="Name                    :", font=("Helvetica", 12, "bold")).grid(row=0, column=1, columnspan=1, padx=(15,0), pady=(0,0), sticky="w")
    tk.Label(insert_window, text="Address               :", font=("Helvetica", 12, "bold")).grid(row=0, column=1, columnspan=1, padx=(15,0), pady=(75,0), sticky="w")
    tk.Label(insert_window, text="Phone Number  :", font=("Helvetica", 12, "bold")).grid(row=0, column=1, columnspan=1, padx=(15,0), pady=(150,0), sticky="w")
    
    # Entry
    name_entry = tk.Entry(insert_window, font=("Helvetica", 12), width=90)
    name_entry.grid(row=0, column=2, columnspan=1, padx=(0,15), pady=(0,0), sticky="w")
    address_entry = tk.Entry(insert_window, font=("Helvetica", 12), width=90)
    address_entry.grid(row=0, column=2, columnspan=1, padx=(0,15), pady=(75,0), sticky="w")
    phone_entry = tk.Entry(insert_window, font=("Helvetica", 12), width=90)
    phone_entry.grid(row=0, column=2, columnspan=1, padx=(0,15), pady=(150,0), sticky="w")
    
    separator = Separator(insert_window, orient="horizontal")
    separator.grid(row=1, column=1, columnspan=5,padx=(0,0), pady=(15, 45), sticky="sew")

    # Submit button
    submit_button = tk.Button(insert_window, text="Submit", command=lambda: insert_data(name_entry.get(), address_entry.get(), phone_entry.get()), font=("Helvetica", 12, "bold"))
    submit_button.grid(row=1, column=1, columnspan=6, padx=(0,0), pady=(0,0), sticky="sew")
    
    insert_window.grid_rowconfigure(0, weight=0)
    insert_window.grid_rowconfigure(1, weight=1)
    insert_window.grid_columnconfigure(0, weight=0)
    insert_window.grid_columnconfigure(1, weight=1)
    insert_window.grid_columnconfigure(2, weight=1)
    
    # Set minimum window size
    insert_window.minsize(1000, 236)
    insert_window.maxsize(1000, 236)

def insert_pelanggan(name, address, phone):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(prepared=True)
        query = "INSERT INTO Pelanggan (Nama_Pelanggan, Alamat_Pelanggan, Nomor_Telephone) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, address, phone))
        connection.commit()
        cursor.close()
        connection.close()
        messagebox.showinfo("Success", "Record inserted successfully.")

def validate_input(name, address, phone):
    # Check if name and address are not empty
    if not name or not address:
        messagebox.showerror("Error", "Please Fill in the Data!")
        return False
    
    if not address:
        messagebox.showerror("Error", "Address Required!")
        return False
    
    if not name:
        messagebox.showerror("Error", "Name Required!")
        return False
    
    if not phone:
        messagebox.showerror("Error", "Phone Number Required!")
        return False
    
    # Check if phone number contains only digits and follows the format
    if not phone.isdigit():
        messagebox.showerror("Error", "Invalid phone number. Please enter numeric digits only.")
        return False
    
    return True

def insert_data(name, address, phone):
    if validate_input(name, address, phone):
        insert_pelanggan(name, address, phone)

def open_delete_window():
    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Pelanggan")
    
    def delete_record():
        # Get the ID from the entry widget
        id_pelanggan = id_entry.get()

        # Call the delete_pelanggan function to delete the record
        delete_pelanggan(id_pelanggan)

        # Close the delete window after deletion
        delete_window.destroy()
        
    # Delete Label
    label_input = tk.Label(delete_window, text="Input ID Pelanggan Yang Ingin Dihapus", font=("Helvetica", 15, "bold"))
    label_input.grid(row=0, column=0, columnspan=3, padx=(0,0), pady=(15,125), sticky="ew")
        
    separator = Separator(delete_window, orient="horizontal")
    separator.grid(row=0, column=0, columnspan=3,padx=(0,0), pady=(0,60), sticky="ew")

    # Label
    label_input = tk.Label(delete_window, text="ID Pelanggan  :", font=("Helvetica", 12, "bold"))
    label_input.grid(row=0, column=1, columnspan=1, padx=(15,0), pady=(25,0), sticky="w")
    
    # Entry
    id_entry = tk.Entry(delete_window, font=("Helvetica", 12, "bold"), width=30)
    id_entry.grid(row=0, column=2, columnspan=1, padx=(0,15), pady=(25,0), sticky="w")
    
    separator = Separator(delete_window, orient="horizontal")
    separator.grid(row=1, column=1, columnspan=3,padx=(0,0), pady=(15, 45), sticky="ew")

    # Delete Button
    delete_button = tk.Button(delete_window, text="Delete", command=delete_record, font=("Helvetica", 12, "bold"))
    delete_button.grid(row=1, column=1, columnspan=3, padx=(0,0), pady=(0,0), sticky="sew")
    
    delete_window.grid_rowconfigure(0, weight=0)
    delete_window.grid_rowconfigure(1, weight=1)
    delete_window.grid_columnconfigure(0, weight=0)
    delete_window.grid_columnconfigure(1, weight=1)
    delete_window.grid_columnconfigure(2, weight=1)
    
    # Set minimum window size
    delete_window.minsize(450, 235)
    delete_window.maxsize(450, 235)

def delete_pelanggan(id_pelanggan):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        query = "DELETE FROM Pelanggan WHERE ID_Pelanggan = %s"
        cursor.execute(query, (id_pelanggan,))
        connection.commit()
        cursor.close()
        connection.close()
        messagebox.showinfo("Success", "Record deleted successfully.")

def open_reset_window():
    reset_window = tk.Toplevel(root)
    reset_window.title("Reset Auto Increment")

    # Labels
    tk.Label(reset_window, text="Start Value:").grid(row=0, column=0, padx=5, pady=5)

    # Entry field
    start_entry = tk.Entry(reset_window)
    start_entry.grid(row=0, column=1, padx=5, pady=5)

    # Submit button
    submit_button = tk.Button(reset_window, text="Submit", command=lambda: reset_auto_increment("Pelanggan", start_entry.get()))
    submit_button.grid(row=1, columnspan=2, padx=5, pady=5)  

def reset_auto_increment(table_name, start_value):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            cursor.execute(f"ALTER TABLE {table_name} AUTO_INCREMENT = {start_value};")
            connection.commit()
            messagebox.showinfo("Success", "Auto-increment reset successfully.")
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to reset auto-increment: {error}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            
def create_indexes():
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            # Create index for ID_Pelanggan column
            cursor.execute("CREATE INDEX idx_ID_pelanggan ON Pelanggan (ID_Pelanggan)")
            connection.commit()
            messagebox.showinfo("Success", "Indexes created successfully.")
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to create indexes: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Optimization
last_update_time = 0

# Constants
BUFFER_TIME = 1000  # Buffer time in milliseconds
UPDATE_DELAY = 1000  # Delay for updating display during window movements in milliseconds

def on_window_configure(event):
    # Update the display after resizing the window
    update_display()

def update_display():
    # Update the display of the Treeview widget
    display_search_results(search_pelanggan(entry_search.get()))
    
def update_display_with_delay(event=None):
    root.after(UPDATE_DELAY, update_display)
    
def update_display_with_event(event=None):
    update_display()
    
def update_display_with_idle_task(event=None):
    root.after_idle(update_display)
    
def update_display_with_buffer():
    global last_update_time
    current_time = int(root.after_idle(update_display))
    if current_time - int(last_update_time) >= BUFFER_TIME:
        last_update_time = current_time
        
# GUI Program
def main():
    global root, entry_search, output_table
    root = Window(themename="superhero")
    root.title("GUI Servis Bengkel Mobil")

    # Search Term Label
    label_search = tk.Label(root, text="Search Name:",  width=20, height=2, font=("Helvetica", 20, "bold"))
    label_search.grid(row=0, column=1, columnspan=3, padx=(0,0), pady=(0, 70))

    entry_search = tk.Entry(root, width=18, font=("Helvetica", 12))
    entry_search.grid(row=0, column=1, columnspan=3, padx=5, pady=(0, 0))

    # Search Button
    btn_search = tk.Button(root, text="Search", command=update_display_with_buffer, width=12, height=1, font=("Helvetica", 12, "bold"))
    btn_search.grid(row=0, column=1, columnspan=3, padx=5, pady=(75, 0))

    separator = Separator(root, orient="horizontal")
    separator.grid(row=1, column=1, columnspan=3, pady=(0, 0), sticky="ew")

    # Table Ouput
    output_table = Treeview(root, columns=("ID", "Name", "Address", "Phone Number"), show="headings",
                            selectmode="browse", height=55)
    output_table.heading("ID", text="ID", anchor="center")
    output_table.heading("Name", text="Name", anchor="center")
    output_table.heading("Address", text="Address", anchor="center")
    output_table.heading("Phone Number", text="Phone Number", anchor="center")

    # Set alignment for each column
    output_table.column("ID", anchor="center")
    output_table.column("Name", anchor="center")
    output_table.column("Address", anchor="center")
    output_table.column("Phone Number", anchor="center")

    # Set column widths
    output_table.column("ID", width=35)
    output_table.column("Name", width=250)
    output_table.column("Address", width=350)
    output_table.column("Phone Number", width=250)

    output_table.grid(row=2, column=1, columnspan=2, padx=25, pady=(10,10), sticky="new")
    
    # Scrollbar
    scrollbar = Scrollbar(root, orient="vertical", command=output_table.yview)
    scrollbar.grid(row=2, column=3, sticky='ns')
    output_table.configure(yscrollcommand=scrollbar.set)

    separator = Separator(root, orient="horizontal")
    separator.grid(row=3, column=1, columnspan=3, pady=(0, 0), sticky="ew")
    
    # Index Button
    btn_create_index = tk.Button(root, text="Create Index", command=create_indexes, font=("Helvetica", 12, "bold"))
    btn_create_index.grid(row=0, column=2, columnspan=3, padx=(0, 0), pady=(25, 35), sticky="s")

    # Insert Button
    btn_insert = tk.Button(root, text="Insert Data", command=open_insert_window, font=("Helvetica", 12, "bold"))
    btn_insert.grid(row=4, column=0, columnspan=2, padx=(0, 0), pady=(25,35), sticky="s")

    # Delete Button
    btn_delete = tk.Button(root, text="Delete Data", command=open_delete_window, font=("Helvetica", 12, "bold"))
    btn_delete.grid(row=4, column=1, columnspan=3, padx=(0, 0), pady=(25,35), sticky="s")

    # Reset Button
    btn_reset = tk.Button(root, text="Reset Increment", command=open_reset_window, font=("Helvetica", 12, "bold"))
    btn_reset.grid(row=4, column=2, columnspan=3, padx=(0, 0), pady=(25,35), sticky="s")

    # Optimization
    root.bind("<Configure>", update_display_with_event)
    root.bind("<Configure>", update_display_with_idle_task)
    
    # Window Expansion Shenanigans
    root.grid_rowconfigure(0, weight=0)
    root.grid_rowconfigure(1, weight=0)
    root.grid_rowconfigure(2, weight=1)
    root.grid_rowconfigure(3, weight=0)
    root.grid_rowconfigure(4, weight=0)
    root.grid_columnconfigure(0, weight=0)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)
    root.grid_columnconfigure(3, weight=0)
    
    # Set minimum window size
    root.minsize(800, 600)

    root.mainloop()

if __name__ == "__main__":
    main()

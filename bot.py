import tkinter as tk
from tkinter import messagebox
from twilio.rest import Client 

# Twilio credentials (replace with your own)
account_sid = 'ACd5e54869259e557165150dc6c8587c23'
auth_token = '5e0d7db04f648f8473384979e87759a5'
client = Client(account_sid, auth_token)

# Global variable for doctor availability
doctor_availability = {
    'doc1': '10am-12pm',
    'doc2': '2pm-4pm',
    'doc3': '5pm-7pm'
}

# Function to send WhatsApp message
def send_whatsapp_message(phone, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',  # Twilio Sandbox WhatsApp number
            body=message_body,              # The message body with dynamic content
            to=f'whatsapp:{phone}'          # Recipient's WhatsApp number with country code
        )
        print(f"Message sent successfully with SID: {message.sid}")
    except Exception as e:
        print(f"Error sending WhatsApp message: {e}")

# Check doctor availability and send a message
def check_availability():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    gender = gender_entry.get()
    issue = issue_entry.get()
    doctor = doctor_entry.get()

    if doctor in doctor_availability:
        available_time = doctor_availability[doctor]
        message_body = f"Dear {name}, your appointment with {doctor} is confirmed for {available_time}."
    else:
        alt_times = ', '.join([f"{doc}: {time}" for doc, time in doctor_availability.items()])
        message_body = f"Dear {name}, sorry for the inconvenience, {doctor} is not available. " \
                       f"Alternative available times: {alt_times}."

    send_whatsapp_message(phone, message_body)
    messagebox.showinfo("Notification", "WhatsApp Message Sent")

# Change doctor availability
def update_availability():
    doc1_time = doc1_entry.get()
    doc2_time = doc2_entry.get()
    doc3_time = doc3_entry.get()

    doctor_availability['doc1'] = doc1_time
    doctor_availability['doc2'] = doc2_time
    doctor_availability['doc3'] = doc3_time

    messagebox.showinfo("Notification", "Doctor availability updated")

# Create the GUI for input
root = tk.Tk()
root.title("Hospital Appointment System")

# Patient Information Input
tk.Label(root, text="Name").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Phone Number (with country code)").grid(row=1, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1)

tk.Label(root, text="Email").grid(row=2, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)

tk.Label(root, text="Gender").grid(row=3, column=0)
gender_entry = tk.Entry(root)
gender_entry.grid(row=3, column=1)

tk.Label(root, text="Issue").grid(row=4, column=0)
issue_entry = tk.Entry(root)
issue_entry.grid(row=4, column=1)

tk.Label(root, text="Doctor Name").grid(row=5, column=0)
doctor_entry = tk.Entry(root)
doctor_entry.grid(row=5, column=1)

# Submit button to check availability and send WhatsApp message
submit_button = tk.Button(root, text="Check Availability", command=check_availability)
submit_button.grid(row=6, columnspan=2)

# Doctor Availability Update Section
tk.Label(root, text="Update Doctor Availability").grid(row=7, columnspan=2)

tk.Label(root, text="Doc  Shreyash").grid(row=8, column=0)
doc1_entry = tk.Entry(root)
doc1_entry.insert(0, doctor_availability['doc1'])
doc1_entry.grid(row=8, column=1)

tk.Label(root, text="Doc Prathamesh").grid(row=9, column=0)
doc2_entry = tk.Entry(root)
doc2_entry.insert(0, doctor_availability['doc2'])
doc2_entry.grid(row=9, column=1)

tk.Label(root, text="Doc Avdhut").grid(row=10, column=0)
doc3_entry = tk.Entry(root)
doc3_entry.insert(0, doctor_availability['doc3'])
doc3_entry.grid(row=10, column=1)

# Button to update doctor availability
update_button = tk.Button(root, text="Update Availability", command=update_availability)
update_button.grid(row=11, columnspan=2)

root.mainloop()
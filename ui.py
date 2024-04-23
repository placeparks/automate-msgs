import streamlit as st
import pywhatkit
import threading

def send_message(phone, message, hour, minute):
    pywhatkit.sendwhatmsg(phone, message, hour, minute)

def main():
    st.title('WhatsApp Message Scheduler')

    # Form to collect user input
    with st.form("whatsapp_form", clear_on_submit=True):
        phone = st.text_input("Enter phone number with country code")
        message = st.text_area("Enter your message")
        hour = st.number_input("Enter the hour (24-hour format)", min_value=0, max_value=23, step=1)
        minute = st.number_input("Enter the minute", min_value=0, max_value=59, step=1)
        submit_button = st.form_submit_button("Send Message")

        if submit_button:
            # Handling sending messages in a non-blocking way
            thread = threading.Thread(target=send_message, args=(phone, message, int(hour), int(minute)))
            thread.start()
            st.success("Message scheduled successfully! Check your phone at the scheduled time.")

if __name__ == "__main__":
    main()

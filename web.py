import streamlit as st
import pandas as pd
from database import add_ticket, get_tickets, update_ticket_status


st.set_page_config(
    page_title="IT Helpdesk",
    page_icon="💻",
    layout="wide"
)

st.title("💻 IT Helpdesk Ticketing System")

st.write("Welcome to the Helpdesk Ticketing System! This application allows you to create, view, and update IT support tickets.")

st.subheader("Please scroll through the sections below.")

st.info("Here you will be able to see all the already existing Tickets, you can update yours or create a new one.")




st.divider()

st.header("📋 All Support Tickets")

tickets = get_tickets()

if tickets:
    df = pd.DataFrame(
        tickets,
        columns=["Ticket ID", "Name", "Problem", "Priority", "Status"]
    )

    st.dataframe(df, hide_index=True)
else:
    st.info("No support tickets found.")



st.divider()

st.header("🎫 Create a Support Ticket")

with st.form("ticket_form"):
    name = st.text_input("Your Name")

    problem = st.text_area("Describe your IT problem")

    priority = st.selectbox(
        "Priority",
        ["Low", "Medium", "High"]
    )

    submitted = st.form_submit_button("Submit Ticket")

    if submitted:
        if name.strip() and problem.strip():
            add_ticket(name.strip(), problem.strip(), priority)
            st.success("Ticket submitted successfully!")
        else:
            st.error("Please enter your name and describe your problem.")







st.divider()

st.header("✏️ Update Ticket Status")

tickets = get_tickets()

if tickets:
    ticket_ids = [ticket[0] for ticket in tickets]

    selected_id = st.selectbox(
        "Select Ticket ID",
        ticket_ids
    )

    new_status = st.selectbox(
        "New Status",
        ["Open", "In Progress", "Closed"]
    )

    if st.button("Update Status"):
        update_ticket_status(selected_id, new_status)

        st.success("Ticket status updated successfully!")

        st.rerun()
else:
    st.info("No tickets available to update.")
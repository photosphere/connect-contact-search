import os
import streamlit as st
import pandas as pd
import boto3
import json
import os

connect_client = boto3.client("connect")

st.set_page_config(
    page_title="Amazon Connect Contact Search Tool!", layout="wide")

# app title
st.header(f"Amazon Connect Contact Search Tool!")

connect_instance_id = ''

if os.path.exists('connect.json'):
    with open('connect.json') as f:
        connect_data = json.load(f)
        connect_instance_id = connect_data['Id']
        connect_instance_arn = connect_data['Arn']

# connect configuration
connect_instance_id = st.text_input(
    'Connect Instance Id', value=connect_instance_id)

contact_attributes_input = ''

if os.path.exists('attributes.json'):
    with open('attributes.json') as f:
        contact_attributes_input = json.load(f)


# contacts
uploaded_files = st.file_uploader(
    "Choose a CSV file", accept_multiple_files=True, type="csv")
if uploaded_files:
    dfs = [pd.read_csv(f) for f in uploaded_files]
    df = pd.concat(dfs)
    df = df.reset_index(drop=True)
    st.dataframe(df)
    df.to_csv("contacts.csv", index=False)

    contact_attributes = st.text_input(
        'Attributes', value=contact_attributes_input)

    load_button = st.button('Load Configuration')
    if load_button:
        with st.spinner('Loading......'):
            # connect configuration
            res = connect_client.describe_instance(
                InstanceId=connect_instance_id)
            connect_filtered = {k: v for k, v in res['Instance'].items() if k in [
                'Id', 'Arn']}
            with open('attributes.json', 'w') as f:
                json.dump(contact_attributes, f)

            # attributes
            with open('connect.json', 'w') as f:
                json.dump(connect_filtered, f)

            cols = contact_attributes.split(",")
            for col in cols:
                print(col)
                df[col] = None
                df[col] = df[col].astype(str)

            for index, row in df.iterrows():
                print(row['Contact ID'])
                res = connect_client.get_contact_attributes(
                    InstanceId=connect_instance_id, InitialContactId=row['Contact ID'])
                print(res['Attributes'])
                print(contact_attributes)
                for col in cols:
                    if col in res['Attributes']:
                        print(res['Attributes'][col])
                        df.loc[index, col] = res['Attributes'][col]

            st.dataframe(df)

            btn = st.download_button(
                label="Download data as CSV",
                data=df.to_csv().encode('utf-8'),
                file_name="contacts.csv",
                mime="application/csv"
            )

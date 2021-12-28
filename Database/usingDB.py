import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model import Smartphone

engine=create_engine("sqlite:///mydatabase.sqlite")

MakeSession=sessionmaker(bind=engine)
sess=MakeSession()



st.title("Add New Smartphone Data")
st.markdown("---")

st.image("download.jpg", use_column_width=True)
st.title("General Features")
brand_v=st.text_input("Brand")
Model_v=st.text_input("Model Name")
Colour_v=st.text_input("Colour")
Sim_v=st.text_input("SIM Type")
Hybrid_v=st.selectbox("Hybrid Sim Slot",["Yes","No"])
Touch=st.selectbox("Touch Screen",["Yes","No"])
OTG_v=st.selectbox("OTG Compatible",["Yes","No"])
Quickcharge_v=st.selectbox("Quick charge",["Yes","No"])

st.title("Display Features")
Display_v=st.text_input("Display Size")
D_type=st.text_input("Display Type")
Resolution_v=st.text_input("Resolution")
R_type=st.text_input("Resolution Type")
D_Colour=st.text_input("Display colours")

st.title("Os and Processor Features")
Oprating_v=st.text_input("Operating System")
P_type=st.text_input("Processor Type")
P_core=st.text_input("Processor core")
primary_v=st.text_input("Primary Clock Speed")
secondary_v=st.text_input("Secondary Clock Speed")

st.title("Memory and Storage Feature")
internal_v=st.text_input("Internal Storage")
ram_v=st.text_input("Ram")

st.title("Camera Features")
pcamera_v=st.text_input("Primary Camera")
scamera_v=st.text_input("Secondary Camera")
flash_v=st.text_input("Flash")
Hdrecording_v=st.selectbox("HD Recording",["Yes","No"])
fHdrecording_v=st.selectbox("Full HD Recording",["Yes","No"])
videorecording_v=st.selectbox("Video Recording",["Yes","No"])
framerate_v=st.text_input("Frame Rate")

st.title("Call Features")
videocall_v=st.selectbox("Video call Support",["Yes","No"])
callrecording_v=st.selectbox("Call Recording",["Yes","No"])

st.title("Connectivity Features")
networktype_v=st.text_input("Network Type")
internetconn_v=st.text_input("Internet Connectivity")
Gprs_v=st.selectbox("GPRS",["Yes","No"])
Blutooth_v=st.selectbox("Blutooth Support",["Yes","No"])
wifi_v=st.selectbox("Wi-Fi",["Yes","No"])
wifihots_v=st.selectbox("Wi-Fi Hotspot",["Yes","No"])
usb_v=st.selectbox("USB Connectivity",["Yes","No"])
Gps_v=st.selectbox("GPS Support",["Yes","No"])

st.title("Other Details")
simsize_v=st.text_input("SIM Size")
graphics_v=st.text_input("Graphics")
sms_v=st.selectbox("SMS",["Yes","No"])
battery_v=st.text_input("Battery")

st.title("Dimensions")
width_v=st.text_input("Width")
height_v=st.text_input("Height")
depth_v=st.text_input("Depth")
weight_v=st.text_input("Weight")

st.title("Warranty")
warranty_v=st.text_input("Warranty Summary")
Domestic_v=st.text_input("Domestic Warranty")

st.markdown("""
#
#
""")
btn=st.button("Add Data")

if btn:
    smrtphn=Smartphone(Brand=brand_v, Model_Name=Model_v, Colour=Colour_v, SIM_Type=Sim_v, Display_Size=Display_v,Display_Type=D_type, Resolution=Resolution_v,Resolution_Type=R_type, Display_Colours=D_Colour,Operating_System=Oprating_v,Processor_Type=P_type,Processor_core=P_core,Primary_Clock_Speed=primary_v,Secondary_Clock_Speed=secondary_v,Internal_Storage=internal_v, Ram=ram_v, Primary_Camera=pcamera_v,Secondary_Camera=scamera_v,Flash=flash_v,Frame_Rate=framerate_v,Network_Type=networktype_v,Internet_Connectivity=internetconn_v,SIM_Size=simsize_v,Graphics=graphics_v,Battery=battery_v,Width=width_v,Height=height_v,Depth=depth_v,Weight=weight_v,Warranty_Summary=warranty_v,Domestic_Warranty=Domestic_v)
    sess.add(smrtphn)
    sess.commit()

    st.success('Data Saved!!')
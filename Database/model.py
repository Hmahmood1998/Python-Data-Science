from sqlalchemy import Column,Integer,String,create_engine, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session,sessionmaker

Base=declarative_base()

class Smartphone(Base):

    __tablename__="smartphone"

    id=Column(Integer,autoincrement=True,primary_key=True)
    Brand=Column(String)
    Model_Name=Column(String)
    Colour=Column(String)
    SIM_Type=Column(String)
    Display_Size=Column(String)
    Display_Type=Column(String)
    Resolution=Column(String)
    Resolution_Type=Column(String)
    Display_Colours=Column(String)
    Operating_System=Column(String)
    Processor_Type=Column(String)
    Processor_core=Column(String)
    Primary_Clock_Speed=Column(String)
    Secondary_Clock_Speed=Column(String)
    Internal_Storage=Column(String)
    Ram=Column(String)
    Primary_Camera=Column(String)
    Secondary_Camera=Column(String)
    Flash=Column(String)
    
    Frame_Rate=Column(String)
    Network_Type=Column(String)
    Internet_Connectivity=Column(String)
    Blutooth_version=Column(String)
    Audio_Jack=Column(String)
    SIM_Size=Column(String)
    Graphics=Column(String)
    Battery=Column(String)
    Width=Column(String)
    Height=Column(String)
    Depth=Column(String)
    Weight=Column(String)
    Warranty_Summary=Column(String)
    Domestic_Warranty=Column(String)


if __name__=="__main__":
    engine=create_engine("sqlite:///mydatabase.sqlite")

# connect to your database
    Base.metadata.create_all(engine)
    Session=sessionmaker(bind=engine)
    session=Session()


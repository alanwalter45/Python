import pydicom
from pydicom.data import get_testdata_file
#filename = get_testdata_file("./FluroWithDisplayShutter.dcm")
ds = pydicom.dcmread("./FluroWithDisplayShutter.dcm")
print(ds.PatientName)
print(ds.timestamp)
print(ds.values())
ds.save_as("revisado.dcm")

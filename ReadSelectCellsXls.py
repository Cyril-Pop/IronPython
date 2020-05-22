#Copyright(c) Cyril P.
#Read xls file data with filter on view (read only cells selected)

import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

#import Revit API
clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import *


clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument

import System
clr.AddReferenceByName('Microsoft.Office.Interop.Excel, Version=11.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c' )
from Microsoft.Office.Interop import Excel
from System.Runtime.InteropServices import Marshal

refreshBoolean = IN[0]

def checkInteger(val):
	try:
		check = int(val)
		return True
	except: return False	

class Lst_Xls():
	def __init__(self):
		try:
			ex = System.Runtime.InteropServices.Marshal.GetActiveObject("Excel.Application")
			ex.Visible = True
			self.app = ex 
			self.error = None
			self.data = []
			
			workbook = ex.ActiveWorkbook
			ws = ex.ActiveSheet
			self.selectRange = ex.Selection 
			for r in self.selectRange:
				self.data.append(r.Value2)
		except Exception as ex:
			self.error   = str(ex)		
objxls = Lst_Xls()	
if objxls.error is None:
	outElem = []
	for val in objxls.data:
		if checkInteger(val):
			elemId = ElementId(int(val))
			elem = doc.GetElement(elemId)
			if elem is not None:
				outElem.append(elem)
	OUT = outElem
else: OUT = None	
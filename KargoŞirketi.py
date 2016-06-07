import arcpy 
from arcpy import env

env.workspace = 'E:\CBS Project\MyGdb.mdb'

arcpy.Intersect_analysis(["KrgNok","Export_Output"],"Turkiye_Out","ALL","","INPUT")
#env.workspace= 'E:\CBS Project'
arcpy.MeanCenter_stats("Turkiye_Out","KargoEnIyi" , "Turkiye_NUFUS_2000","","")

#arcpy.MakeFeatureLayer_management("E:\CBS Project\MyGdb.mdb\KargoEnIyi", "KrgSlct")
#arcpy.SelectLayerByAttribute_management("KrgSlct", "NEW_SELECTION","")
#arcpy.SelectLayerByAttribute_management("KargoEnIyi","NEW_SELECTION")
arcpy.SelectLayerByLocation_management("Export_Output","CONTAINS","KargoEnIyi","","NEW_SELECTION")


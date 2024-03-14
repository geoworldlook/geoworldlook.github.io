from Renewable_energy_optimum_location_function import *



# Przykładowe wywołanie funkcji:
base_input_path = "../PILOT/EKSPOZYCJA"
base_output_path = "../PILOT/TEST_SKRYPTU"


#1 Define layers which use to look
layer_paths = [
    'D:/GEOWORLDLOOK/OZE/PILOT/BDOT/PL.PZGiK.335.BDOT10k.20_OT_PTGN_A.shp',
    'D:/GEOWORLDLOOK/OZE/PILOT/BDOT/PL.PZGiK.335.BDOT10k.20_OT_PTRK_A.shp',
    'D:/GEOWORLDLOOK/OZE/PILOT/WARSTWY/PL.PZGiK.335.BDOT10k.20_OT_PTTR_A_ROSLINOSC_TRAWIASTA.shp'
]

#Output path
output_file_name_1 = 'merge_layers.shp'
#Merge layers
merge_vector_layers(layer_paths,base_output_path = base_output_path,output_file_name_1 =output_file_name_1)

#2 Cut sunlight data base on mask for each month

months = [
        "styczen", "luty", "marzec", "kwiecien",
    "maj", "czerwiec", "lipiec", "sierpien",
    "wrzesien", "pazdziernik", "listopad", "grudzien"
        ]

# Paths to the input and output data folders
input_folder = "D:/GEOWORLDLOOK/OZE/PILOT/SURFACE_RADIATION_1991_2020"
output_folder = "D:/GEOWORLDLOOK/OZE/PILOT/TEST_SCRIPT/TEST_CLIP_RADIATION/"

# Mask shapefile path
mask_shapefile = "D:/GEOWORLDLOOK/OZE/PILOT/WARSTWY/PODLASKIE_SHP.shp"

# Ensure the output folder exists
create_directory_if_not_exists(output_folder)

# Process sunlight data
process_sunlight_data(months, input_folder, output_folder, mask_shapefile)


#3 Terrain aspect

# Input paths
input_folder_aspect_3 = "D:/GEOWORLDLOOK/OZE/PILOT/TEST_SKRYPTU"
input_file_aspect_3 = "podlaskie_geotif.tif"

# Output paths
output_folder_aspect_3 = "D:\GEOWORLDLOOK\OZE\PILOT\TEST_SCRIPT"
output_file_aspect_3 = "podlaskie_aspect.tif"

calculate_terrain_aspect(input_folder_aspect_3, input_file_aspect_3, output_folder_aspect_3, output_file_aspect_3)


#4 Convert terrain aspect to vector data

# Paths to the input raster and output folders
output_folder_aspect = "D:/GEOWORLDLOOK/OZE/PILOT/TEST_SCRIPT"
output_file_aspect = "podlaskie_aspect.tif"
raster_input = os.path.join(output_folder_aspect, output_file_aspect)

output_folder_raster = "D:/GEOWORLDLOOK/OZE/PILOT/TEST_SCRIPT/TEST_EXPOSURE_WS_S_ES"
output_raster_file = "RASTER_WS_S_ES.tif"

output_vector_folder = "D:/GEOWORLDLOOK/OZE/PILOT/TEST_SCRIPT/TEST_RASTER_TO_VECTOR"
output_vector_file = "SURFACE_VECTOR.shp"

# Perform raster to vector conversion
raster_to_vector_conversion(raster_input, output_folder_raster, output_raster_file, output_vector_folder, output_vector_file)


#5 Filter value, where area fit to cryterium
filter_value = '"DN" = 1'
input_filename = "RASTER_WS_S_ES_TO_VECTOR.tif.shp"
output_file_5 = "WEKTOR_EKSPOZYCJA_TRUE.shp"

filter_values_condition_1(filter_value_5 = filter_value, base_input_path_5= base_input_path ,input_filename_5=input_filename, base_output_path_5 = base_output_path
                          ,output_file_5 = output_file_5)




#6 Select area fit to cryterium and to free area from bdot

input_filename = "RASTER_WS_S_ES_TO_VECTOR.shp"
output_file_5 = "WEKTOR_EKSPOZYCJA_TRUE.shp"
output_file_name_6 = '6_common_area.shp'
intersection_exposure_bdot(base_output_path,base_layer=output_file_5,overlay_layer=output_file_name_1,output_file_name_6 = output_file_name_6)

#7 Split to single parts
output_file_name_7 = "TEST_ROZBITE_NA_POJEDYNCZE.shp"

split_into_single_parts(base_output_path = base_output_path,input_file_name=output_file_name_6 ,output_file_name_7 = output_file_name_7)

#8 calculate area
output_file_8 = "TEST_OBLCIZENIE_POWIERZCHNI.shp"
calculate_area_on_split_elements(base_output_path,input_file_8=output_file_name_7,output_file_8 = output_file_8)

#9 Select area more than value (individual parametr)
output_file_9 = "TEST_FILTR_AREA_POWYZEJ_20000.shp"
variable ='"AREA" > 20000'
filter_areas_above_20000(base_output_path = base_output_path,input_file_9 = output_file_8,output_file_9 = output_file_9, variable = variable)

#10 Add id to column to select by id in next steps
output_file_10 = "TEST_FILTR_AREA_POWYZEJ_20000_Z_ID.shp"
add_id_column_to_filtered_data(base_output_path,output_file_10 = output_file_10)

input_voltage_path_11 = '../PILOT/BDOT/PL.PZGiK.335.BDOT10k.20_OT_SULN_L.shp'
output_file_name_11 = "LINIE_SN.shp"
#11 select specific voltage lines
select_medium_voltage_lines(base_output_path = base_output_path,input_voltage_path_11 = input_voltage_path_11,  output_file_name_11 = output_file_name_11)


#12 calculate distanse to power lines
output_file_name_12 = "12_ODLEGLOSC_DO_LINII_ENERGETYCZNYCH.shp"
calculate_distance(base_output_path,source_layer = output_file_10, destination_layer = output_file_name_11,output_file_name = output_file_name_12)


#13 Join to calculeted area by id
field_1 = 'ID'
field_2 ='ID'
field_to_copy = 'distance'
output_file_name_13 = "13_POWIERZCHNIE_Z_ODLEGLOSCIAMI.shp"

join_attributes_with_distances(base_output_path = base_output_path,field_1 = field_1, field_2 = field_2, field_to_copy = field_to_copy
                               ,base_file=output_file_10,file_from_copy=output_file_name_12,output_file_name =output_file_name_13)

#14 Filter area by parametr
variable_14 = '"distance" < 500'
output_file_name_14 = "14_POWIERZCHNIE_BLISKO_LINII.shp"
filter_areas_close_to_lines(base_output_path = base_output_path, variable_14 = variable_14,layer_to_filter = output_file_name_13, output_file_name_14 = output_file_name_14)

#15 Rename distance to voltage column
new_name = 'LINE_DISTANCE'
field_to_rename ='distance'
output_file_name_15 = "15_POWIERZCHNIE_BLISKO_LINII.shp"
rename_column(base_output_path = base_output_path, file_to_rename=output_file_name_14,field_to_rename = field_to_rename
, new_name= new_name, output_file_name = output_file_name_15)

#16 Calculate distance to roads

output_file_name_16 = "16_ODLEGLOSC_DO_DROG.shp"
road_file_path = '../PILOT/BDOT/PL.PZGiK.335.BDOT10k.20_OT_SKJZ_L.shp'


calculate_distance(base_output_path = base_output_path,source_layer=output_file_name_15,destination_layer =road_file_path ,output_file_name = output_file_name_16)

#17 Select column by id from vector with distance to new column in area data
output_file_name_17 = "17_POWIERZCHNIE_Z_ODLEGLOSCIAMI_DO_DROG.shp"
field_1 = 'ID'
field_2 = 'ID'
field_to_copy = 'distance'
join_attributes_with_distances(field_1,field_2
    ,field_to_copy,base_output_path,base_file= output_file_name_15, file_from_copy=output_file_name_16,output_file_name =output_file_name_17)


#18 Rename column with distance to road
output_file_name_18 = "18_KONCOWE_ZMIANY_W_ATRYBUTACH.shp"
rename_column(base_output_path=base_output_path,file_to_rename=output_file_name_17,field_to_rename = 'distance',new_name='ROAD_DISTANCE',output_file_name = output_file_name_18)
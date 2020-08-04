import struct
import gc
import re
import os
import csv
import datetime
import numpy as np
import soundfile as sf

fmt = np.dtype([("gyro_x", np.int16), ("gyro_y", np.int16), ("gyro_z", np.int16), ("acc_x", np.int16), ("acc_y", np.int16), ("acc_z", np.int16)])

time = datetime.datetime.now()
time_fmt = time.strftime("%d%m%y_%H%M%S")

def csvWrite_BIN(namepart, file_count, pdir, gyro_x, gyro_y, gyro_z, acc_x, acc_y, acc_z):

    print("Writing" + str(pdir) + str("/") + "sdd_bin_" + str(time_fmt) + "_" + str(namepart) + ".csv\n")
    with open(str(pdir) + "sdd_bin_" + str(time_fmt) + "_" + str(namepart) + ".csv", 'w+', newline="") as csvfile:
        fieldnames = ["times", "gyro_x", "gyro_y", "gyro_z", "accel_x", "accel_y", "accel_z"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for i in range(len(times)):
            try:
                writer.writerow({'gyro_x': gyro_x[i], 'gyro_y': gyro_y[i], "gyro_z": gyro_z[i], "accel_x": acc_x[i], "accel_y": acc_y[i], "accel_z": acc_z[i]})

                
            except IndexError:
                pass

        csvfile.close()

def csvWrite_Smoke(timestamps, namepart, pdir, mc1p0, mc2p5, mc4p0, mc10p0, nc0p5, nc1p0, nc2p5, nc4p0, nc10p0):

    print("Writing " + str(pdir) + str("/") + "smoke_data_" + str(time_fmt) + str("_") + str(namepart) + ".csv\n")
    
    with open(str(pdir) + "/smoke_data_" + str(time_fmt) + str(namepart) + ".csv", 'w+', newline="") as csvfile:
        fieldnames = ["times","mc1p0", "mc2p5", "mc4p0", "mc10p0", "nc0p5", "nc1p0", "nc2p5", "nc4p0", "nc10p0"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for i in range(len(mc10p0)):
            try:
                writer.writerow({'times':timestamps[i], 'mc1p0': mc1p0[i], 'mc2p5': mc2p5[i], "mc4p0": mc4p0[i], "mc10p0": mc10p0[i], "nc0p5": nc0p5[i], "nc1p0": nc1p0[i], "nc2p5": nc2p5[i], "nc4p0":nc4p0[i], "nc10p0": nc10p0[i]})

            except IndexError:
                pass

def parseFiles(parseRawFlag):

    ''' A function to extract data from sdd.bin and write it to a csv file'''

    pdir = ["."] 
    loop_count = 0
    count = 0
    file_count = 0

    try:

        for filename in os.listdir(str(pdir[0])):
            
            if filename.endswith(".bin"):
                times = parseLog(str(pdir[0]), str(filename), str(":SDD"))
                print("Extracting from " + pdir[0] + filename)
                data = np.fromfile(os.path.join(pdir[0], filename), dtype=fmt)
                namepart = filename[4:11]

                gyro_x = []
                gyro_y = []
                gyro_z = []
                acc_x = []
                acc_y = []
                acc_z = []

                for entry in data:

                    gx, gy, gz = entry["gyro_x"], entry["gyro_y"], entry["gyro_z"]
                    ax, ay, az = entry["acc_x"], entry["acc_y"], entry["acc_z"]
                    
                    if gx >= 32768:
                        gx -= 65535

                    if gy >= 32768:   
                        gy -= 65535

                    if gz >= 32768:   
                        gz -= 65535

                    if ax >= 32768:   
                        ax -= 65535

                    if ay >= 32768:   
                        ay -= 65535  
                        
                    if az >= 32768:   
                        az -= 65535 
            
                    gx *= 0.0305008235
                    gy *= 0.0305008235
                    gz *= 0.0305008235
                    ax *= 0.00024414
                    ay *= 0.00024414
                    az *= 0.00024414
                    
                    ## Append Gyroscope/Acc values to their respected lists
                    gyro_x.append(gx)
                    gyro_y.append(gy)
                    gyro_z.append(gz)

                    acc_x.append(ax)
                    acc_y.append(ay)
                    acc_z.append(az)
 
                file_count += 1
                
                
                csvWrite_BIN(namepart, file_count, times, pdir[0], gyro_x, gyro_y, gyro_z, acc_x, acc_y, acc_z)
        
            elif filename.endswith(".log"):
                times = parseLog(str(pdir[0]), str(filename), str(":smoke"))
                ## Temp list for storing data to parse
                data_list = []
                ## MC values
                mc1p0 = []
                mc2p5 = []
                mc4p0 = []
                mc10p0 = []

                ## NC Values
                nc0p5 = []
                nc1p0 = []
                nc2p5 = []
                nc4p0 = []
                nc10p0 = []
                    
                with open(str(pdir[0]) + "/" + str(filename), "r+") as log:
                    namepart = filename[4:25]
                    ## Read each line of the halt log file
                    data = log.readlines()
                    ## Append each line of the log file to the empty list init above
                    data_list.append(data)
                    ## A loop to iterate over each string created in the empty data_list list
                    for string in data_list:
                        
                        ## A regex expression to find all mc and nc values in the halt.log file
                        mc = re.compile("mc_*")
                        nc = re.compile("nc_*")                
                        
                        ## Another loop to iterate over each string and further filter data
                        for data in string:
                        
                            ## If the data is an "MC" value then strip the "mc_*=" variable tag and keep only the value stored as a float point
                            if mc.search(data):

                                mc_stripped = data.partition("=")[2]
                                cleaned_values = float(str(mc_stripped.replace("\'", "")).lstrip())
                                #print("mc_" + str(count) + " = " + str(cleaned_values))
                                
                                if count == 0:
                                    mc1p0.append(cleaned_values)
                                
                                elif count == 1:
                                    mc2p5.append(cleaned_values)
                                
                                elif count == 2:
                                    mc4p0.append(cleaned_values)
                                
                                elif count == 3:
                                    mc10p0.append(cleaned_values)

                                ## Increment a counter so you can tell which mc value you are at in a given smoke event
                                count += 1

                            elif nc.search(data):
                                
                                nc_stripped = data.partition("=")[2]
                                cleaned_values = float(str(nc_stripped.replace("\'", "")).lstrip())
                                #print("nc_" + str(count) + " = " + str(cleaned_values))
                                
                                if count == 4:
                                    nc0p5.append(cleaned_values)
                                
                                elif count == 5:
                                    nc1p0.append(cleaned_values)
                                
                                elif count == 6:
                                    nc2p5.append(cleaned_values)
                                
                                elif count == 7:
                                    nc4p0.append(cleaned_values)

                                elif count == 8:
                                    nc10p0.append(cleaned_values)

                                ## Increment a counter so you can tell which mc value you are at in a given smoke event
                                count += 1

                            elif "typical_particle_size=" in data:
                                
                                data_stripped = data.partition("=")[2]
                                cleaned_values = float(str(data_stripped.replace("\'", "")).lstrip())
                                #print("\nTypical Particle Size = " + str(cleaned_values) + "\n")
                                ## Reset the counter to 0 once a smoke event has ended (This assumed to end after the typical particle size is displayed)
                                
                                count = 0
                                
                            else:
                                ## All other misc data that is irrelevant for the time being will be skipped
                                pass

                    ## Write smoke values to file
                    csvWrite_Smoke(times, namepart, pdir[0], mc10p0, mc2p5, mc4p0, mc10p0, nc0p5, nc1p0, nc2p5, nc4p0, nc10p0)              
            
            elif filename.endswith(".raw") and parseRawFlag:

                try: 
                    data, samplerate = sf.read(str(pdir[0]) + filename, channels=2, samplerate=44100, subtype="FLOAT")
                    namepart = filename[:7]

                    with open(str(pdir[0]) + "sdd_raw_" + str(time_fmt) + "_" + namepart + ".csv", 'w+', newline="") as csvfile:
                        fieldnames = ["left_channel", "right_channel"]
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        writer.writeheader()

                        print("Get comfy, because this is going to be a while...")
                        print("Writing " + str(pdir[0]) + "sdd_raw_" + str(time_fmt) + "_" + namepart + ".csv to file.")
                        
                        for item in data:
                            
                            if item[0] != "nan" or item[1] != "nan":
                                writer.writerow({'left_channel':str(item[0]), 'right_channel':str(item[1])})
                            
                            elif item[0] == "nan" or item[1] == "nan":
                                if item[0] == "nan":
                                    writer.writerow({'left_channel':str("0"), 'right_channel':str(item[1])})

                                elif item[1] == "nan":
                                    writer.writerow({'left_channel':str(item[0]), 'right_channel':str("0")})
                            
                            elif item[0] == "nan" and item[1] == "nan":
                                writer.writerow({'left_channel':str("0"), 'right_channel':str("0")})

                    csvfile.close()
                    print("\nDone.\n")
                
                except MemoryError:
                    continue 

        ##Arbitrary counter to prevent data from being overwritten if more than one bin in a dir        
        file_count = 0
        loop_count += 1
                    
    except FileNotFoundError:
        print("\nError locating folders. Please ensure your folder structure matches and try again!")

def parseLog(pdir, filename, patt):

    ''' A function to parse the log file and pull timestamps for further analysis of data
        Passes - Path (file directory variable)
        Returns - Times [list]
    '''
    patt = patt
    times = []
    data_list = []
    with open(str(pdir[0]) + "/" + str(filename), "r+") as log:
        
        ## Read each line of the halt log file
        data = log.readlines()
        ## Append each line of the log file to the empty list init above
        data_list.append(data)
        
        print("\nParsing log file. Please wait...")
        ## A loop to iterate over each string created in the empty data_list list
        for string in data_list:
            
            ## A regex expression to find all mc and nc values in the halt.log file
            pattern = re.compile(str(patt))

            for data in string:
                
                if "1980" in data:
                    pass

                elif pattern.search(data):

                    isolate_stamp = data.split(":")[0]
                    isolate_time = isolate_stamp.split("-")[1]
                    time_of_event = isolate_time[0:4]
                    times.append(time_of_event)
                
                else:
                    pass
    return(times)

parsingCheck = True
while parsingCheck:

    parse_raw = input("Do you want to parse all of the RAW audio files? (WARNING, THIS CAN TAKE A LONG TIME!): ")
    
    if parse_raw.lower() == "y":
        parsingCheck = False
        parseRawFlag = True
        print("\nParsing all BIN, RAW & log files\n"), parseFiles(parseRawFlag), print("All done!")

    elif parse_raw.lower() == "n":
        parsingCheck = False
        parseRawFlag = False
        print("\nParsing all BIN, RAW, & log files\n"), parseFiles(parseRawFlag), print("All done!")

    else:
        print("Invalid entry. Please enter (y)es or (n)o to continue.")
        parsingCheck = True
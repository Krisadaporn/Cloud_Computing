import multiprocessing as mp
from passenger import PASSENGER

# assign variables of file path to access the data in the file
file_path = "AComp_Passenger_data_no_error.csv"
colnames = ["passenger_id","flight_id","departure_code","arrive_code","departure_time","flight_time"]

if __name__ == '__main__':
    with mp.Pool(processes=mp.cpu_count()) as pool:
        
        #call the PASSENGER class with the previous assign variables of file path
        passenger1 = PASSENGER(file_path,colnames)
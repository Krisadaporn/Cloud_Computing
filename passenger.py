import csv
import sys
import pandas as pd

#create class for re-usability
class PASSENGER:
    
    def __init__(self, file_path, colnames):
        #assign parameter to get data from the file path
        self.file_path = file_path
        self.colnames = colnames
        self.df = pd.read_csv(self.file_path, names=self.colnames, header=None)
        
        #call the mapper method using information from " df"and save it as attribute "mapper_out"
        self.mapper_out = self.mapper(self.df["passenger_id"],self.df["flight_id"])
        
        #call the shuffle method using mapper_out as input and save it as attribute "reduce_in"
        self.reduce_in = self.shuffle(self.mapper_out)
        
        #call the reducer method using reduce_in as input and save it as attribute "reduce_out"
        self.reduce_out = self.reducer(self.reduce_in)
        
        #call the max_passenger method using reduce_out as input
        self.max_passenger(self.reduce_out)
        

    def mapper(self, passengers_list, flights_list):
        """Iterate over each rows of input data"""
        
        #create an empty list to store list of tuples of (passenger_id, 1)
        self.mapper_out = []
        
        #loop through rows of column passengers_list and column flights_list
        for passenger, flight in zip(passengers_list,flights_list):
            
            #add the tuple to the mapper_out list
            self.mapper_out.append((passenger, 1))
            
        #check output mapper_out
        print(self.mapper_out)
        
        return self.mapper_out
    

    def shuffle(self, mapper_out):
        """ Organise the mapped values by key """
        
        #create an empty dictionary to collect passenger_id as key and list of count of flights as values
        self.reduce_in = {}
        
        #loop through list of tuples
        for passenger, flight in mapper_out:
            
            #check if the dictionary, then add the passenger as key and a list of flight as value
            if passenger not in self.reduce_in: 
                self.reduce_in[passenger] = [flight]
                
            #else if it already in the dictionary, then append the count of flight to the value
            else:
                self.reduce_in[passenger].append(flight)
        
        #check output of reduce_in
        print(self.reduce_in)
        
        return self.reduce_in

    def reducer(self, reduce_in):
        """ Sum the number of flights """
        
        #create an empty dictionary to collect passenger_id as key and sum of the list of count of flights as values
        self.reduce_out = {}
        
        #loop through reduce_in dictionary to get the passenger_id and list of count of flights
        for passenger, flight_list in reduce_in.items():
            
            #assign the value to be sum of the count of flights
            self.reduce_out[passenger] = sum(flight_list)
            
        #use DataFrame to record output from dictionary and export to csv file
        df = pd.DataFrame.from_dict(self.reduce_out, orient="index")
        df.to_csv("reduce_output.csv")
        
        #check output of reducer
        print(self.reduce_out)
        
        return self.reduce_out
    
    def max_passenger(self, reduce_out):
        """ Find Passenger ID which has the highest number of flights """
        
        #assign max_passenger as the key of maximum value of reduce_out
        self.max_passenger = max(reduce_out, key=reduce_out.get)
        
        #assign max_flight as the sum of count of flights of max_passenger
        max_flight = self.reduce_out[self.max_passenger]
        
        #print result
        print("Passenger ID " + self.max_passenger + " has highest number of flights at "+ str(max_flight))
        
        return self.max_passenger
#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#importing the requried libraries
import numpy as np
import pandas as pd
import os
import csv
import matplotlib.pyplot as plt
import random
global df
global option_a,option_b,option_c,initial_option
option_a,option_b,option_c,initial_option=0,0,0,1

class o():
    
    def datafile():
        try:#Declaring the file path
            file_path=input("Please enter the file name with extention \n")
            #Creating an global variable
            #Opening file and saving it as an Data Frame 
            global df
            df=pd.read_csv(file_path,header=0)
            #Using display funtion reduces the column visibility hence using max_columns, max_rows to fix that.
            pd.set_option('display.max_columns', None)
            pd.set_option('display.max_rows', None)
            return df
        except IOError:
            print("File not found")
#Class for (b) Requirment
class a():

    def individual_car_by_id(cid):
        try:
            #function to get the car record by id
            return df.query(f"car_ID == {cid}")
        except SyntaxError:
            print("Please enter the car id value")
            cid=input()
            return(a.individual_car_by_id(cid))
    
    def cars_by_no_of_cyl(no_cyl):
        #function to get the car record by no_cyl
        
        try:
            #function to get the car record by id
            return df.query(f"cylindernumber == {no_cyl}")
        except SyntaxError:
            print("Please enter the car id value")
            no_cyl=input()
            return(a.cars_by_no_of_cyl(cid))
    
    def cars_by_body(t_cb):
        try:
        #funtion to get car records based on carbody
            return df[df['carbody']==t_cb.lower()]
        except initialoptions:
            t_cb=input("Please enter a valid car body")
            return(a.cars_by_body(t_cb))
    
    def no_col_of_individual_car_by_id(id,n_col):
        #function to get no of columns by ID
        if n_col == "r" or n_col == "R" and id is int:
            return df.iloc[id,:(random.randint(1,19))].to_frame().transpose()
        elif int(n_col)>0 and int(n_col)< 20:
            return df.iloc[id,:int(n_col)].to_frame().transpose()
        else:
            id = input("Enter a valid  car id ")
            n_col = input("Enter number of Columns or enter R or r to get an. random no of Columns")
            return (a.no_col_of_individual_car_by_id(id,n_col))

#Class for (c) Requirment
class b():
    def car_names_alphabetical():
        #funtion to sort the car names alphabeticaly
        return df.sort_values(by = ["CarName"], ascending=True)[["CarName"]]
    def car_price_body():
        #funtion to get the car price avg by car body type
        car_b_df=df.groupby(["carbody"])
        for group, item_in_group in car_b_df:
            if group =="convertible":
                temp=(item_in_group.mean()["price"])
                print(f"Convertable : {temp}")
            elif group =="sedan":
                temp=(item_in_group.mean()["price"])
                print(f"Sedan : {temp}")
            elif group =="hatchback":
                temp=(item_in_group.mean()["price"])
                print(f"Hatchback : {temp}")
            elif group =="wagon":
                temp=(item_in_group.mean()["price"])
                print(f"Wagon : {temp}")
            elif group =="hardtop":
                temp=(item_in_group.mean()["price"])
                print(f"Hardtop : {temp}")
                
    def car_top5_body():
        #funtion to get top 5 cars by price and by body type
        temp=df.sort_values(by = ["price"], ascending=False)[["price"]].head(5)
        print(f"Retrieving the top 5 car sale by price \n{temp}")
        car_b_df=df.groupby(["carbody"])
        print("Top 5 car price by High to Low by body")
        for group, item_in_group in car_b_df:
            if group =="convertible":
                temp=item_in_group.sort_values(by = ["price"], ascending=False)[["price"]].head(5)
                print(f"Convertable : \n {temp}")
            elif group =="sedan":
                temp=(item_in_group.sort_values(by = ["price"], ascending=False))[["price"]].head(5)
                print(f"Sedan :\n{temp}")
            elif group =="hatchback":
                temp=(item_in_group.sort_values(by = ["price"], ascending=False))[["price"]].head(5)
                print(f"Hatchback : \n{temp}")
            elif group =="wagon":
                temp=(item_in_group.sort_values(by = ["price"], ascending=False))[["price"]].head(5)
                print(f"Wagon : \n{temp}")
            elif group =="hardtop":
                temp=(item_in_group.sort_values(by = ["price"], ascending=False))[["price"]].head(5)
                print(f"Hardtop : \n{temp}")
    def user_choice_hp(hp):
        #function to get the car records with respect to hp
        try:
            return df.query(f"horsepower <= {hp} ")
        except SyntaxError:
            print("Please enter the a valid horse power")
            hp=input()
            return(b.user_choice_hp(hp))

#Class for (d) requirement
class c():

       
    def bar(v,x_lable,y_lable,title):
        #function to plot graph for engine type
        get_ipython().run_line_magic('matplotlib', 'inline')
        fig= plt.figure()
        plt.hist(df[[v]],edgecolor="black")
        # set x/y labels and plot title
        plt.xlabel(x_lable)
        plt.ylabel(title)
        plt.show()
    def top_5_cheap_hp():
        #function for Sorting based on price and getting the required columns 
        temp=df.sort_values(by = ["price"], ascending=True)[["horsepower","CarName"]].head(5)
        # Declaring the size of the plots
        fig, ax = plt.subplots(figsize=(15, 12))
        

        plt.suptitle("Horsepower (hp) of car top 5 cheapest car ", fontsize=18, y=0.95)

        #Get the car name from the grouped dataframe and covert to list
        car_name = temp['CarName'].to_list()
    
        #Get the hp from the grouped dataframe and convert to list
        hp = temp['horsepower'].to_list()


        # loop through the length of car list in dataframe 5 gears car and keep track of index
        for i in range(len(temp['CarName'])):
            # add a new subplot iteratively
            ax = plt.subplot(1, 5, i + 1)
    
            # filter df and plot hp on the new subplot axis
            #df_cars_5gears[df_cars_5gears['hp']].p(ax=ax)
            ax.bar(car_name[i],hp[i])

            # chart formatting 
            ax.set_ylim(0,100) # set y-xais limit value
    def buying_behavior():
        
        #using heat map to identify the buying behavior of customers
        #declaring Figure size
        f = plt.figure(figsize=(10,7))
        plt.matshow(df.corr(), fignum=f.number)
        #x and y axis lable parameter initializaion
        plt.xticks(range(df.select_dtypes(['number']).shape[1]), df.select_dtypes(['number']).columns, fontsize=14, rotation=75)
        plt.yticks(range(df.select_dtypes(['number']).shape[1]), df.select_dtypes(['number']).columns, fontsize=14)
        cb = plt.colorbar()
        cb.ax.tick_params(labelsize=14)
        plt.title('Buying Behavior Correlation Matrix', fontsize=16);
        
        
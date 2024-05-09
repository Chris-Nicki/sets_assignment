# Sets Assignment
# 1. Python Sets Adventure
"""Objective:
The aim of this assignment is to deepen your understanding and application of Python sets 
in various scenarios, ranging from basic operations to advanced manipulations and best practices. 
You will correct given codes, use sets in everyday contexts, and tackle challenges that require 
creative thinking and problem-solving.
"""
# Task 1: Flight Route Comparison
"""Imagine you work for an airline and need to compare the flight routes of your airline with a 
competitor. You have two sets of flight destinations, one for each airline. Write a Python program 
to find out:

Destinations that both airlines fly to.
Destinations unique to your airline.
Whether there are any destinations that neither airline shares.
"""
print("Shared Routes")
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
common_destinations = our_routes.intersection(competitor_routes)
print(common_destinations)
print()
print("Proprietary Routes")
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
proprietary_routes = our_routes.difference(competitor_routes)
print(proprietary_routes)
print()
print("Unavailable Routes")
joint_routes = our_routes.union(competitor_routes)
available_routes = {"LAX", "HOU", "DEN", "JFK", "DXB", "MDW", "CDG", "BKK", "LHR"}
unavailable_routes = available_routes.difference(joint_routes)
print(unavailable_routes)
print()
# 2. Set Operations in Data Analysis
"""Objective:
The aim of this assignment is to enhance your skills in using Python sets for data analysis tasks. 
You will apply various set operations to handle real-world data scenarios, focusing on their practical 
application and efficiency.
"""
# Task 1: Duplicate Entries Cleanup
"""You are given a list of customer IDs, some of which are duplicated. Write a Python script to remove 
duplicates and display the unique customer IDs.
"""
# Example Code:
print("Customer ID")
customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
print(customer_ids)
no_dupes = set(customer_ids)
print()
print("No Duplicates")
guest_list =list(no_dupes)
print(customer_ids)
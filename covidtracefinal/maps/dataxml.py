# from xml.dom import minidom
# import os
# import mysql.connector
# import MySQLdb
# import pprint
# import requests
# from django.http import HttpResponse, HttpResponseRedirect


# headers = {'Content-Type': 'text/xml', 'Accept': 'application/xml'}

# #Start XML file, create parent node
# root = minidom.Document() 
# xml = root.createElement('markers') #create root eleemtn
# root.appendChild(xml) 

# try:
#     #Open connection to MySQL Serve + #Set the active MySQL Database
#     cnx = mysql.connector.connect(user='root', password = '25305002740', host='127.0.0.1', database = 'finalcovid_project')
# except:
#     print("mysql connecter connection failed")


# #Select all the rows in the markers table
# cursor = cnx.cursor()

# sql = "SELECT * FROM maps_location"

# try:
#     cursor.execute(sql) #run sql command
#     results = cursor.fetchall()
# except:
#     print("could not run sql command")
    
# headers = {'content-type': 'text/xml; charset=utf-8'}

# #Iterate through the rows, adding XML nodes for each
# for row in results:

#     #Add to XML document code
#     rootchild = root.createElement('marker')

#     rootchild.setAttribute("id", str(row[0]))
#     rootchild.setAttribute("address", str(row[1]))
#     rootchild.setAttribute("latitude", str(row[2]))
#     rootchild.setAttribute("longitude", str(row[3]))
#     # rootchild.setAttribute("city", str(row[4]))
#     rootchild.setAttribute("loc_type", str(row[5]))

#     # xml.appendChild(rootchild)

#     xml_str = root.toprettyxml(indent="\t")

#     save_path_file = '/Users/shaneshimizu/Desktop/VSCode/finalcovid_project/covidtracefinal/maps/sample.xml'

#     with open(save_path_file, "w") as f:
#         f.write(xml_str)

# # url = 'http://google.com'
# # response = requests.request("POST", url, headers = headers, data = save_path_file)
# # print(response.text.encode('utf8'))
# #Dump to browser
# # print(save_path_file)
# #Close server connection
# cnx.close()
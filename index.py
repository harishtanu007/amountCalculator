import json

from flask import Flask,render_template,request
import mysql.connector
import subprocess
import os

# if the script don't need output.
import requests



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password",
  database="mydatabase"
)


mycursor = mydb.cursor()

def printTable(tablename):
    mycursor.execute("SELECT * FROM "+tablename)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)



def createlandrateTable():
    mycursor.execute(
        "CREATE TABLE landrate (id INT AUTO_INCREMENT PRIMARY KEY, pincode INT UNIQUE, price INT)")
    print("table created successfully")

def insertlandrateTable(pincode,price):
    sql = "INSERT INTO landrate (pincode,price) VALUES (%s, %s)"
    val = (pincode, price)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")


def createCustomerTable():
    mycursor.execute(
        "CREATE TABLE customer (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255),email VARCHAR(255) UNIQUE,doorno VARCHAR(255),locality VARCHAR(255),city VARCHAR(255),district VARCHAR(255),state VARCHAR(255),pincode VARCHAR(255),mobile VARCHAR(255) UNIQUE)")
    print("table created successfully")


#printTable("landrate")
#os.system("php location.php")

#createlandrateTable()
#insertlandrateTable("landrate","500058","3000")
#printTable("landrate")
#createCustomerTable()
#printTable("customer")
# result = subprocess.run(
#     ['php', 'location.php'],    # program and arguments
#     stdout=subprocess.PIPE,  # capture stdout
#     check=True               # raise exception if program fails
# )
# print(result.stdout)

app=Flask("__name__")

@app.route("/",methods=['GET', 'POST'])
def index():
    return render_template("mymap.html")

@app.route("/client")
def client():
    printTable("landrate")
    print("---------------------------------------")
    mycursor.execute("SELECT * FROM landrate" )
    myresult = mycursor.fetchall()
    for x in myresult:
        print (x[0], x[1])

    return render_template("client.html")

@app.route('/process', methods=['POST'])
def view_do_something():

    if request.method == 'POST':
        #your database process here
       # print(request.get_json())
        #print("lat="+request.args.get("lat"))
        #print("lng="+request.args.get("lng"))
        url = "http://apis.mapmyindia.com/advancedmaps/v1/9tn2n9znekwy67wf89m8sxt7bb5zkors/rev_geocode?lat=17.51&lng=78.35"

        response = requests.get(url)
       # print()
        json_data = json.loads(response.text)
        print(json_data)
        # da= json.loads(response)
        #print(data["results"]["locality"])
        return "OK"
    else:
        return "NO OK"

@app.route("/map")
def map():
    return render_template("mymap.html")

@app.route("/inserttable",methods=['GET', 'POST'])
def inserttable():
    price = request.form['price']
    pincode = request.form['pincode']
    insertlandrateTable(pincode,price)
    printTable("landrate")
    return render_template("inserttable.html",pincode=pincode,price=price)

@app.route("/details",methods=['GET', 'POST'])
def details():
    doorno = request.form['doorno']
    locality = request.form['locality']
    district = request.form['district']
    city = request.form['city']
    sqft = request.form['sqft']
    state = request.form['state']
    address = request.form['address']
    pincode = request.form['pincode']
    phone = request.form['phone']
    email = request.form['email']

    print("---------------------------------------")
    mycursor.execute("SELECT * FROM landrate where pincode="+pincode)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x[0], x[1])
    landrate=int(x[2])
    totalrate=int(x[2])*int(sqft)
    return render_template("userdetails.html",doorno=doorno,locality=locality,district=district,city=city,state=state,address=address,pincode=pincode,phone=phone,email=email,sqft=sqft,totalrate=totalrate,landrate=landrate)

if __name__=="__main__":
    app.run()
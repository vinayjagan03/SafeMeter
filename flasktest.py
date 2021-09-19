# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 18:18:55 2021

@author: vinay
"""

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

num_contours = [0]
num_shots = [0]

@app.route("/output")
def get_data():
    print(num_contours)
    return str(num_contours[0])

@app.route("/input/<data>")
def update_data(data):
    num_contours[0] = int(data) 
    return str(num_contours[0])

@app.route("/")
def index():
    return render_template("index.html", found=num_contours[0] > 0, shots=num_shots[0])

@app.route("/why")
def why():
    return render_template("why.html")

@app.route("/bac")
def bac():
    return render_template("bac.html")

@app.route('/handle_data', methods=['POST'])
def handle_data():
    percentage = float(request.form['percentage'])/100.0
    proof = float(request.form['proof'])
    num_shots[0] += (12 * percentage / 1.5) * (proof / 80.0)
    return redirect("/")
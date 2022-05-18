
from flask import Flask, render_template, url_for, redirect, request, Blueprint

admin=Blueprint("admin",__name__)
@admin.route("/adminuser")
def user():
    return render_template("adminUser.html")
@admin.route("/admin", methods=['GET','POST'])
def home():
    return render_template("adminUser.html")
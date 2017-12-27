from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask("DSA")


@app.route("/")
def home():
    return "App is running."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1306)

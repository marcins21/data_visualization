from flask import Flask,render_template

app = Flask(__name__)
   

@app.route("/")
def home():
    d = {"marcin":15,"tomek":20,"artur":50}
    info_func(kwargs=d)

    return render_template("landing_page.html",my_dict=d)

def info_func(*args,**kwargs):
    new_list = {**kwargs}
    print(f"\n\nDictionary Given to Landing_page.html \n{new_list}\n")



if __name__ == "__main__":
   
   app.run(debug=True)
from flask import Flask, redirect, render_template, request
from Task import Task

app = Flask(__name__)
task = Task()

@app.route("/")
def home():
    return render_template("home.html", li = task.display_tasks())

@app.route('/edit/<int:task_id>')
def get_edit(task_id):
    ind = task.is_valid(task_id)
    if ind:
        result = task.display_task(ind - 1)
        return render_template("edit.html", result = result)
    return redirect("/", code=303)

@app.route('/add', methods=['POST'])
def add():
    data = request.json
    try: # this code may throw an exception
        priority = int(data.get('priority'))
        task.add_task(task = data.get('task'), priority = priority)
    except:
        return "Wrong information", 404
    return "Succeed", 200

@app.route('/delete', methods=['POST'])
def delete():
    data = request.json
    ind = task.is_valid(data.get('id'))
    if ind:
        task.delete_task(ind -1)
        return "Succeed", 200
    return "Not Found", 404

@app.route('/edit', methods=['POST'])
def edit():
    data = request.json
    ind = task.is_valid(data.get('id'))
    if ind:
        try: # this code may throw an exception
            priority = int(data.get('priority'))
            result = task.edit_task(ind -1, data.get('task'), priority, data.get('is_completed'))
            if result:
                return "Succeed", 200 
        except:
            return "Wrong information", 404
    return "Not Found", 404

if __name__=="__main__":
    app.run(debug=True)
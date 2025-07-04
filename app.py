from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append({'task': task})
    return redirect(url_for('index'))

@app.route('/delete/<int:task_num>')
def delete_task(task_num):
    if 0 < task_num <= len(tasks):
        tasks.pop(task_num - 1)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
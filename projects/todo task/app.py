from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    search_query = request.args.get('search', '').strip().lower()
    sort_by = request.args.get('sort_by', '')
    if search_query:
        filtered_tasks = [task for task in tasks if search_query in task['content'].lower()]
    else:
        filtered_tasks = tasks[:]

    if sort_by == 'deadline':
        filtered_tasks.sort(key=lambda t: t.get('deadline') or '', reverse=False)
    elif sort_by == 'category':
        filtered_tasks.sort(key=lambda t: t.get('category') or '')
    elif sort_by == 'completed':
        filtered_tasks.sort(key=lambda t: t.get('completed', False))

    return render_template('index.html', tasks=filtered_tasks, search_query=search_query, sort_by=sort_by)
@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    if 0 <= task_id < len(tasks):
        if request.method == 'POST':
            new_content = request.form.get('task')
            new_deadline = request.form.get('deadline')
            new_category = request.form.get('category')
            if new_content:
                tasks[task_id]['content'] = new_content
                tasks[task_id]['deadline'] = new_deadline
                tasks[task_id]['category'] = new_category
            return redirect(url_for('index'))
        return render_template('edit.html', task=tasks[task_id], task_id=task_id)
    return redirect(url_for('index'))

@app.route('/add', methods=['POST'])
def add_task():
    task_content = request.form.get('task')
    deadline = request.form.get('deadline')
    category = request.form.get('category')
    if task_content:
        now = datetime.now()
        tasks.append({
            'content': task_content,
            'completed': False,
            'created_at': now.strftime('%Y-%m-%d %I:%M %p'),
            'deadline': deadline,
            'category': category
        })
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['completed'] = True
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

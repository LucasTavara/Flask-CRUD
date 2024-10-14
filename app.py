from flask import Flask, request, jsonify
from Models.Tasks import Task

app = Flask(__name__)

tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
   global task_id_control
   data = request.get_json()
   new_task = Task(id=task_id_control, title=data['title'], description=data.get("description", ""))
   task_id_control + 1
   tasks.append(new_task)
   print(tasks)
   return jsonify({"menssage":"nova tarefa criada com sucesso!"})

@app.route('/tasks', methods=['GET'])
def lista_task():  
     task_list = [Task.to_dict() for Task in tasks]

     output = {
       "task": task_list,
       "total_task": len(task_list)
      }
     return jsonify(output)

@app.route('/tasks/<int:id>', methods=['GET'])
def Lista_por_id(id):
   for t in tasks:
      if t.id == id:
          return jsonify(t.to_dict())
   return jsonify({"message":"Não foi possível encontrar a atividade"}), 404


if __name__ =="__main__":
 app.run(debug=True)


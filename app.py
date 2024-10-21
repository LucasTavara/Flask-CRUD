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
   return jsonify({"message":"nova tarefa criada com sucesso!", "id": new_task.id})

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

@app.route('/tasks/<int:id>', methods=['PUT'])
def Atualizar_tarefa(id):
   task = None
   for t in tasks:
      if t.id == id:
         task = t
   print(task)
   if task == None:
      return jsonify({"message": "Não foi possivel encontrar a atividade"}), 404

   data = request.get_json()
   task.title = data['title']
   task.description = data['description']
   task.completed = data['completed']
   return jsonify({"message": "Tarefa atualizada com sucesso"})

@app.route('/tasks/<int:id>', methods=['DELETE'])
def deletar_tarefa(id):
   task = None
   for t in tasks:
      if t.id == id:
         task = t
         break
   if not task:
      return jsonify({"message":"Não foi possivel encontrar a atividade "}), 404
   
   tasks.remove(task)
   return jsonify({"message":"Tarefa foi deletada com sucesso!"})

if __name__ =="__main__":
 app.run(debug=True)


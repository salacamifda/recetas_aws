from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Recipe:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under30 = data['under30']
        self.date_made = data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

        self.first_name = data['first_name']
    
    @staticmethod
    def valida_receta(formulario):
        es_valido = True

        if len(formulario['name']) < 3:
            flash("El nombre de la receta debe tener al menos 3 caracteres", "receta")
            es_valido = False
        
        if len(formulario['description']) < 3:
            flash("La descripción de la receta debe tener al menos 3 caracteres", "receta")
            es_valido = False
        
        if len(formulario['instructions']) < 3:
            flash("Las instrucciones de la receta deben tener al menos 3 caracteres", "receta")
            es_valido = False
        
        if formulario['date_made'] == "":
            flash("Ingrese una fecha", "receta")
            es_valido = False
        
        return es_valido 
    
    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO recipes (name, under30, description, instructions, date_made, user_id) VALUES ( %(name)s, %(under30)s, %(description)s, %(instructions)s, %(date_made)s, %(user_id)s )"
        nuevoId = connectToMySQL('recetas').query_db(query, formulario)
        return nuevoId

    @classmethod
    def get_all(cls):
        query = "SELECT recipes.*, first_name FROM recipes LEFT JOIN users ON users.id = recipes.user_id" #LEFT JOIN users
        results = connectToMySQL('recetas').query_db(query) #Lista de diccionarios
        recetas = []
        for receta in results:
            recetas.append(cls(receta)) #cls(receta) -> Instancia de receta, Agregamos la instancia a mi lista de recetas
        return recetas

    
    @classmethod
    def get_by_id(cls, formulario): #recibir formulario_receta
        query = "SELECT recipes.*, first_name FROM recipes LEFT JOIN users ON users.id = recipes.user_id WHERE recipes.id = %(id)s" #LEFT JOIN users
        result = connectToMySQL('recetas').query_db(query, formulario) #recibimos una lista 
        recipe = cls(result[0]) #Creamos una instancia de receta
        return recipe

    @classmethod
    def update(cls, formulario): #Recibir el formulario. OJO con todo y el ID de la receta
        query = "UPDATE recipes SET name = %(name)s, under30 = %(under30)s, description = %(description)s, instructions = %(instructions)s, date_made = %(date_made)s WHERE id = %(id)s"
        result = connectToMySQL('recetas').query_db(query, formulario)
        return result

    @classmethod
    def delete(cls, formulario): #Recibe formulario con id de receta a borrar
        query = "DELETE FROM recipes WHERE id = %(id)s"
        result = connectToMySQL('recetas').query_db(query, formulario)
        return result
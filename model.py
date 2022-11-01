from flask import Flask

tasks = [
    {
      'id': 1,
      'name': 'task1',
      'description': 'This is task 1'  
    },
    
    {
      'id': 2,
      'name': 'task2',
      'description': 'This is task 2'  
    },
    
    {
      'id': 3,
      'name': 'task3',
      'description': 'This is task 3'  
    }
]

class Calc():
    def somar(n, n1):
        soma = n + n1
        
        return { 'resultado': soma }
    
    def jsonReturn():
        return tasks
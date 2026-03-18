# Практическая работа №3: бэкенд-разработка на Python и Django

## 🛠 Проверка ORM (Задание 3)

Для тестирования CRUD-операций в Django Shell были выполнены следующие команды:

### 1. Создание задач
```python
from todo.models import Task
Task.objects.create(title="Задача 1", description="Описание 1")
Task.objects.create(title="Задача 2", description="Описание 2")
Task.objects.create(title="Задача 3", description="Описание 3")
```

### 2. Получение списка всех задач
```python
tasks = Task.objects.all()
for t in tasks:
    print(f"{t.id}: {t.title} — {t.completed}")
```

### 3. Обновление статуса
```python
task = Task.objects.get(title="Задача 1")
task.completed = True
task.save()
print(f"Задача '{task.title}' выполнена: {task.completed}")
```

### 4. Удаление задачи
```python
task_to_del = Task.objects.get(title="Задача 3")
task_to_del.delete()
```

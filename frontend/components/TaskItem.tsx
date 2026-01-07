import { Task } from '../types/task';
import { formatDate } from '../utils/date';

interface TaskItemProps {
  task: Task;
  onToggleCompletion: (id: number) => void;
  onEdit: (task: Task) => void;
  onDelete: (id: number) => void;
}

export default function TaskItem({ task, onToggleCompletion, onEdit, onDelete }: TaskItemProps) {
  const handleToggle = () => {
    onToggleCompletion(task.id);
  };

  const handleEdit = () => {
    onEdit(task);
  };

  const handleDelete = () => {
    if (confirm('Are you sure you want to delete this task?')) {
      onDelete(task.id);
    }
  };

  return (
    <div className="p-5 bg-white border border-gray-200 rounded-xl shadow-sm hover:shadow-md transition-shadow">
      <div className="flex items-start">
        <input
          type="checkbox"
          checked={task.completed}
          onChange={handleToggle}
          className="mt-1 h-5 w-5 text-primary-600 rounded focus:ring-primary-500 focus:ring-2"
        />

        <div className="ml-4 flex-1 min-w-0">
          <h3
            className={`text-lg font-medium ${
              task.completed ? 'text-gray-500 line-through' : 'text-gray-900'
            }`}
          >
            {task.title}
          </h3>

          {task.description && (
            <p className={`mt-2 text-gray-600 ${task.completed ? 'line-through' : ''}`}>
              {task.description}
            </p>
          )}

          <div className="mt-3 flex items-center text-sm text-gray-500">
            <span>Created: {formatDate(task.created_at)}</span>
            {task.updated_at !== task.created_at && (
              <span className="ml-3">Updated: {formatDate(task.updated_at)}</span>
            )}
          </div>
        </div>

        <div className="flex space-x-3">
          <button
            onClick={handleEdit}
            className="text-primary-600 hover:text-primary-800 text-sm font-medium px-3 py-1 rounded-md hover:bg-primary-50 transition-colors"
          >
            Edit
          </button>
          <button
            onClick={handleDelete}
            className="text-red-600 hover:text-red-800 text-sm font-medium px-3 py-1 rounded-md hover:bg-red-50 transition-colors"
          >
            Delete
          </button>
        </div>
      </div>
    </div>
  );
}
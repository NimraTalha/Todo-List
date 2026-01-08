import { Task, TaskCreate, TaskUpdate } from '../types/task';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8001/api';

// Create a base request function that includes the JWT token
async function apiRequest<T>(
  endpoint: string,
  options: RequestInit = {}
): Promise<T> {
  // Get token from wherever it's stored (localStorage, context, etc.)
  const token = localStorage.getItem('better-auth-token');

  const headers = {
    'Content-Type': 'application/json',
    ...(token && { 'Authorization': `Bearer ${token}` }),
    ...options.headers,
  };

  const response = await fetch(`${API_BASE_URL}${endpoint}`, {
    ...options,
    headers,
  });

  if (!response.ok) {
    if (response.status === 401) {
      // Redirect to login if unauthorized
      window.location.href = '/login';
      throw new Error('Unauthorized - please log in');
    }
    throw new Error(`API request failed: ${response.status} ${response.statusText}`);
  }

  return response.json();
}

// Task API functions
export const taskApi = {
  // GET /api/tasks
  getTasks: (status?: 'all' | 'pending' | 'completed', sort?: 'created' | 'title'): Promise<Task[]> => {
    const params = new URLSearchParams();
    if (status) params.append('status', status);
    if (sort) params.append('sort', sort);

    const queryString = params.toString();
    const endpoint = queryString ? `/tasks?${queryString}` : '/tasks';

    return apiRequest<Task[]>(endpoint);
  },

  // POST /api/tasks
  createTask: (taskData: TaskCreate): Promise<Task> => {
    return apiRequest<Task>('/tasks', {
      method: 'POST',
      body: JSON.stringify(taskData),
    });
  },

  // GET /api/tasks/{id}
  getTask: (id: number): Promise<Task> => {
    return apiRequest<Task>(`/tasks/${id}`);
  },

  // PUT /api/tasks/{id}
  updateTask: (id: number, taskData: TaskUpdate): Promise<Task> => {
    return apiRequest<Task>(`/tasks/${id}`, {
      method: 'PUT',
      body: JSON.stringify(taskData),
    });
  },

  // DELETE /api/tasks/{id}
  deleteTask: (id: number): Promise<void> => {
    return apiRequest<void>(`/tasks/${id}`, {
      method: 'DELETE',
    });
  },

  // PATCH /api/tasks/{id}/complete
  toggleTaskCompletion: (id: number): Promise<{ id: number; completed: boolean }> => {
    return apiRequest<{ id: number; completed: boolean }>(`/tasks/${id}/complete`, {
      method: 'PATCH',
    });
  },
};
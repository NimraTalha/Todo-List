// Define types for authentication
export interface UserCredentials {
  email: string;
  name: string;
  password: string;
}

export interface UserLogin {
  email: string;
  password: string;
}

export interface AuthResponse {
  access_token: string;
  token_type: string;
}

export interface UserSession {
  id: string;
  email: string;
  name: string;
}

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8001/api';

/**
 * Authentication API functions
 */
export const authApi = {
  // POST /api/auth/signup
  signup: async (userData: UserCredentials): Promise<AuthResponse> => {
    const response = await fetch(`${API_BASE_URL}/auth/signup`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(userData),
    });

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.detail || 'Signup failed');
    }

    return response.json();
  },

  // POST /api/auth/signin
  signin: async (credentials: UserLogin): Promise<AuthResponse> => {
    const response = await fetch(`${API_BASE_URL}/auth/signin`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(credentials),
    });

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.detail || 'Login failed');
    }

    return response.json();
  },

  // POST /api/auth/signout
  signout: async (): Promise<void> => {
    // For JWT-based auth, we just remove the token from localStorage
    localStorage.removeItem('better-auth-token');
  },

  // GET /api/auth/session
  getSession: async (): Promise<UserSession> => {
    const token = localStorage.getItem('better-auth-token');

    const response = await fetch(`${API_BASE_URL}/auth/session`, {
      headers: {
        'Authorization': `Bearer ${token}`,
      },
    });

    if (!response.ok) {
      throw new Error('Session invalid');
    }

    return response.json();
  },
};
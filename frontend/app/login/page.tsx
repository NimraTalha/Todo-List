'use client';

import { useState } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';
import { authApi } from '../../lib/authApi';

export default function LoginPage() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const router = useRouter();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      const credentials = { email, password };
      const response = await authApi.signin(credentials);

      // Store the token in localStorage (as per spec)
      localStorage.setItem('better-auth-token', response.access_token);

      // Redirect to tasks page
      router.push('/tasks');
      router.refresh();
    } catch (err: any) {
      setError(err.message || 'An error occurred during login');
      console.error(err);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-primary-50 to-secondary-100">
      <div className="container mx-auto px-4 py-8">
        <div className="flex justify-center">
          <div className="w-full max-w-md">
            <div className="text-center mb-8">
              <button
                onClick={() => router.push('/')}
                className="inline-flex items-center text-primary-600 hover:text-primary-800 mb-4"
              >
                <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 19l-7-7m0 0l7-7m-7 7h18" />
                </svg>
                Back to Home
              </button>
              <h1 className="text-3xl font-bold text-gray-900">Sign In</h1>
              <p className="mt-2 text-gray-600">Access your account to continue</p>
            </div>

            <div className="bg-white rounded-2xl shadow-xl p-8">
              {error && (
                <div className="p-3 text-red-700 bg-red-50 rounded-lg border border-red-200 mb-4">
                  {error}
                </div>
              )}

              <form onSubmit={handleSubmit} className="space-y-4">
                <div>
                  <input
                    id="email"
                    type="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                    placeholder="Enter your email"
                    className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition-colors"
                  />
                </div>

                <div>
                  <input
                    id="password"
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                    placeholder="Enter your password"
                    className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition-colors"
                  />
                </div>

                <button
                  type="submit"
                  className="w-full px-4 py-3 bg-primary-600 text-white font-medium rounded-lg hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500 transition-colors shadow-sm"
                >
                  Sign In
                </button>
              </form>

              <div className="mt-6 text-center text-sm text-gray-600">
                Don't have an account?{' '}
                <Link href="/signup" className="font-medium text-primary-600 hover:text-primary-500 transition-colors">
                  Sign up
                </Link>
              </div>
            </div>

            <div className="mt-6 text-center text-xs text-gray-500">
              <ul className="space-y-1">
                <li>✓ Free forever, no credit card required</li>
                <li>✓ Sync across all your devices</li>
                <li>✓ Advanced task management features</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
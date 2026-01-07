import Link from 'next/link';

export default function HomePage() {
  const features = [
    {
      title: "Bank-Level Security",
      description: "Your data is protected with enterprise-grade encryption and security protocols",
      icon: "🔒"
    },
    {
      title: "Lightning Fast",
      description: "Optimized performance ensures your tasks load instantly, anywhere, anytime",
      icon: "⚡"
    },
    {
      title: "Smart Prioritization",
      description: "AI-powered algorithms help you focus on what matters most for maximum productivity",
      icon: "🤖"
    },
    {
      title: "Team Collaboration",
      description: "Share projects, assign tasks, and collaborate seamlessly with your team members",
      icon: "👥"
    }
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-primary-50 to-secondary-100 dark:from-dark-900 dark:to-dark-800">
      {/* Hero Section */}
      <div className="py-12">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <div className="mb-4">
              <span className="inline-block px-4 py-1 text-sm font-medium text-primary-600 bg-primary-100 rounded-full dark:text-primary-300 dark:bg-primary-900/30">
                New: AI-Powered Task Management
              </span>
            </div>
            <h1 className="text-4xl md:text-6xl font-bold text-gray-900 mb-6 dark:text-white">
              Organize Your Life with
              <span className="text-primary-600 dark:text-primary-400"> Todo Pro</span>
            </h1>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto mb-10 dark:text-gray-300">
              Transform your productivity with intelligent task management, smart prioritization and seamless collaboration tools.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
              <Link
                href="/signup"
                className="px-8 py-4 bg-primary-600 text-white font-semibold text-lg rounded-lg hover:bg-primary-700 transition-colors shadow-lg text-center dark:bg-secondary-600 dark:hover:bg-secondary-700"
              >
                Start Free Today
              </Link>
              <Link
                href="/login"
                className="px-8 py-4 bg-white text-gray-700 font-semibold text-lg rounded-lg border border-gray-300 hover:bg-gray-50 transition-colors shadow-sm text-center dark:bg-dark-700 dark:text-white dark:border-dark-600 dark:hover:bg-dark-600"
              >
                Sign In
              </Link>
            </div>
            <div className="mt-6 flex flex-col sm:flex-row items-center justify-center gap-6 text-sm text-gray-600 dark:text-gray-400">
              <div className="flex items-center">
                <svg className="w-5 h-5 text-green-500 mr-2 dark:text-green-400" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                </svg>
                Free Forever
              </div>
              <div className="flex items-center">
                <svg className="w-5 h-5 text-green-500 mr-2 dark:text-green-400" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                </svg>
                No Credit Card
              </div>
              <div className="flex items-center">
                <svg className="w-5 h-5 text-green-500 mr-2 dark:text-green-400" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                </svg>
                Setup in 2 Minutes
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Features Section */}
      <div className="py-16 bg-white dark:bg-dark-800">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl font-bold text-gray-900 mb-4 dark:text-white">
              Everything You Need to
              <span className="text-primary-600 dark:text-primary-400"> Stay Organized</span>
            </h2>
            <p className="text-lg text-gray-600 max-w-2xl mx-auto dark:text-gray-300">
              Powerful features designed to boost your productivity and help you achieve your goals faster than ever before.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            {features.map((feature, index) => (
              <div key={index} className="bg-gray-50 rounded-xl p-6 hover:shadow-lg transition-shadow dark:bg-dark-700 dark:hover:bg-dark-600">
                <div className="text-3xl mb-4 dark:text-white">{feature.icon}</div>
                <h3 className="text-xl font-semibold text-gray-900 mb-2 dark:text-white">{feature.title}</h3>
                <p className="text-gray-600 dark:text-gray-300">{feature.description}</p>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* CTA Section */}
      <div className="py-16 bg-gradient-to-r from-primary-500 to-secondary-500">
        <div className="max-w-4xl mx-auto text-center px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold text-white mb-4">
            Ready to Transform Your Productivity?
          </h2>
          <p className="text-xl text-primary-100 mb-8">
            Join thousands of users who have already transformed their workflow with Todo Pro.
          </p>
          <Link
            href="/signup"
            className="inline-block px-8 py-4 bg-white text-primary-600 font-semibold text-lg rounded-lg hover:bg-gray-100 transition-colors shadow-lg dark:bg-dark-700 dark:text-white dark:hover:bg-dark-600"
          >
            Get Started Free
          </Link>
        </div>
      </div>
    </div>
  );
}
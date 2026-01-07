const Footer = () => {
  return (
    <footer className="bg-white border-t border-gray-200 mt-16 dark:bg-dark-800 dark:border-dark-700">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          <div>
            <h3 className="text-lg font-semibold text-gray-900 mb-4 dark:text-white">Todo Pro</h3>
            <p className="text-gray-600 text-sm dark:text-gray-300">
              Transform your productivity with intelligent task management, smart prioritization and seamless collaboration tools.
            </p>
          </div>

          <div>
            <h4 className="text-sm font-semibold text-gray-900 uppercase tracking-wider mb-4 dark:text-white">Product</h4>
            <ul className="space-y-2">
              <li><a href="#" className="text-gray-600 hover:text-primary-600 text-sm dark:text-gray-400 dark:hover:text-primary-400">Features</a></li>
              <li><a href="#" className="text-gray-600 hover:text-primary-600 text-sm dark:text-gray-400 dark:hover:text-primary-400">Pricing</a></li>
              <li><a href="#" className="text-gray-600 hover:text-primary-600 text-sm dark:text-gray-400 dark:hover:text-primary-400">Integrations</a></li>
              <li><a href="#" className="text-gray-600 hover:text-primary-600 text-sm dark:text-gray-400 dark:hover:text-primary-400">Updates</a></li>
            </ul>
          </div>

          <div>
            <h4 className="text-sm font-semibold text-gray-900 uppercase tracking-wider mb-4 dark:text-white">Resources</h4>
            <ul className="space-y-2">
              <li><a href="#" className="text-gray-600 hover:text-primary-600 text-sm dark:text-gray-400 dark:hover:text-primary-400">Documentation</a></li>
              <li><a href="#" className="text-gray-600 hover:text-primary-600 text-sm dark:text-gray-400 dark:hover:text-primary-400">Tutorials</a></li>
              <li><a href="#" className="text-gray-600 hover:text-primary-600 text-sm dark:text-gray-400 dark:hover:text-primary-400">Blog</a></li>
              <li><a href="#" className="text-gray-600 hover:text-primary-600 text-sm dark:text-gray-400 dark:hover:text-primary-400">Support</a></li>
            </ul>
          </div>

          <div>
            <h4 className="text-sm font-semibold text-gray-900 uppercase tracking-wider mb-4 dark:text-white">Company</h4>
            <ul className="space-y-2">
              <li><a href="#" className="text-gray-600 hover:text-primary-600 text-sm dark:text-gray-400 dark:hover:text-primary-400">About</a></li>
              <li><a href="#" className="text-gray-600 hover:text-primary-600 text-sm dark:text-gray-400 dark:hover:text-primary-400">Careers</a></li>
              <li><a href="#" className="text-gray-600 hover:text-primary-600 text-sm dark:text-gray-400 dark:hover:text-primary-400">Contact</a></li>
              <li><a href="#" className="text-gray-600 hover:text-primary-600 text-sm dark:text-gray-400 dark:hover:text-primary-400">Partners</a></li>
            </ul>
          </div>
        </div>

        <div className="mt-12 pt-8 border-t border-gray-200 dark:border-dark-700">
          <p className="text-center text-gray-600 text-sm dark:text-gray-400">
            © 2026 Todo Pro. All rights reserved.
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
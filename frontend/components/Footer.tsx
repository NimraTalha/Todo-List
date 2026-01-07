const Footer = () => {
  return (
    <footer className="bg-white border-t border-gray-200 mt-16">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          <div>
            <h3 className="text-lg font-semibold text-gray-900 mb-4">Todo Pro</h3>
            <p className="text-gray-600 text-sm">
              Transform your productivity with intelligent task management, smart prioritization and seamless collaboration tools.
            </p>
          </div>

          <div>
            <h4 className="text-sm font-semibold text-gray-900 uppercase tracking-wider mb-4">Product</h4>
            <ul className="space-y-2">
              <li><a href="#" className="text-gray-600 hover:text-primary-600 text-sm">Features</a></li>
              <li><a href="#" className="text-gray-600 hover:text-primary-600 text-sm">Pricing</a></li>
              <li><a href="#" className="text-gray-600 hover:text-primary-600 text-sm">Integrations</a></li>
              <li><a href="#" className="text-gray-600 hover:text-primary-600 text-sm">Updates</a></li>
            </ul>
          </div>

          <div>
            <h4 className="text-sm font-semibold text-gray-900 uppercase tracking-wider mb-4">Resources</h4>
            <ul className="space-y-2">
              <li><a href="#" className="text-gray-600 hover:text-primary-600 text-sm">Documentation</a></li>
              <li><a href="#" className="text-gray-600 hover:text-primary-600 text-sm">Tutorials</a></li>
              <li><a href="#" className="text-gray-600 hover:text-primary-600 text-sm">Blog</a></li>
              <li><a href="#" className="text-gray-600 hover:text-primary-600 text-sm">Support</a></li>
            </ul>
          </div>

          <div>
            <h4 className="text-sm font-semibold text-gray-900 uppercase tracking-wider mb-4">Company</h4>
            <ul className="space-y-2">
              <li><a href="#" className="text-gray-600 hover:text-primary-600 text-sm">About</a></li>
              <li><a href="#" className="text-gray-600 hover:text-primary-600 text-sm">Careers</a></li>
              <li><a href="#" className="text-gray-600 hover:text-primary-600 text-sm">Contact</a></li>
              <li><a href="#" className="text-gray-600 hover:text-primary-600 text-sm">Partners</a></li>
            </ul>
          </div>
        </div>

        <div className="mt-12 pt-8 border-t border-gray-200">
          <p className="text-center text-gray-600 text-sm">
            © 2026 Todo Pro. All rights reserved.
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
import React from 'react';
import { Link } from 'react-router-dom';
import { Zap } from 'lucide-react';

export default function Navbar() {
  return (
    <nav className="w-full bg-navy-900/80 backdrop-blur-md border-b border-white/10 sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          <Link to="/" className="flex items-center space-x-2 group">
            <Zap className="w-6 h-6 text-violet group-hover:text-emerald transition-colors duration-300" />
            <span className="font-bold text-xl tracking-tight text-white group-hover:text-emerald transition-colors duration-300">
              Smash AI
            </span>
          </Link>
          <div className="flex items-center space-x-4">
            
          </div>
        </div>
      </div>
    </nav>
  );
}

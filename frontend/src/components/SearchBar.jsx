import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Search, Sparkles, Link2 } from 'lucide-react';

export default function SearchBar({ initialValue = "" }) {
  const [query, setQuery] = useState(initialValue);
  const [isUrl, setIsUrl] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    const trimmed = query.trim();
    if (trimmed.startsWith('http://') || trimmed.startsWith('https://')) {
      setIsUrl(true);
    } else {
      setIsUrl(false);
    }
  }, [query]);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (query.trim()) {
      if (isUrl) {
        navigate(`/analyze?url=${encodeURIComponent(query.trim())}`);
      } else {
        navigate(`/results?q=${encodeURIComponent(query.trim())}`);
      }
    }
  };

  return (
    <form onSubmit={handleSubmit} className="w-full max-w-3xl relative group">
      <div className="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
        {isUrl ? (
          <Link2 className="h-6 w-6 text-emerald-400 group-focus-within:text-emerald-300 transition-colors duration-300" />
        ) : (
          <Search className="h-6 w-6 text-gray-400 group-focus-within:text-violet transition-colors duration-300" />
        )}
      </div>
      <input
        type="text"
        className="block w-full pl-12 pr-32 py-4 bg-white/5 border border-white/20 rounded-full text-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-violet focus:border-transparent transition-all duration-300 shadow-xl"
        placeholder="Search product or paste a link... (e.g. iPhone 15 or https://amazon.in/...)"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button
        type="submit"
        className={`absolute inset-y-1 right-1 flex items-center px-6 text-white font-semibold rounded-full transition-all duration-300 hover:scale-105 ${isUrl
            ? 'bg-gradient-to-r from-emerald-500 to-teal-600 hover:from-teal-600 hover:to-emerald-500'
            : 'bg-gradient-to-r from-violet to-fuchsia-600 hover:from-fuchsia-600 hover:to-violet'
          }`}
      >
        <Sparkles className="w-5 h-5 mr-2" />
        {isUrl ? 'Analyze' : 'Find'}
      </button>
    </form>
  );
}
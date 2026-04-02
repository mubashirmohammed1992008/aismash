import React, { useEffect } from 'react';
import Navbar from '../components/Navbar';
import SearchBar from '../components/SearchBar';
import { Search, BrainCircuit, Zap } from 'lucide-react';
import { useNavigate, useSearchParams } from 'react-router-dom';

const EXAMPLES = ["iPhone 15", "Sony WH-1000XM5", "Samsung 4K TV"];

export default function Home() {
  const navigate = useNavigate();
  const [searchParams] = useSearchParams();

  // Flash.co-style: if ?url= is in the query string, go straight to analyze
  useEffect(() => {
    const url = searchParams.get('url');
    if (url) {
      navigate(`/analyze?url=${encodeURIComponent(url)}`, { replace: true });
    }
  }, []);

  return (
    <div className="min-h-screen flex flex-col relative overflow-hidden">
      <div className="absolute inset-0 bg-gradient-to-b from-slate-900 via-violet-950/20 to-slate-900 pointer-events-none z-0"></div>
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[60vw] h-[60vw] bg-violet/10 rounded-full blur-[120px] pointer-events-none z-0"></div>

      <Navbar />

      <main className="flex-1 flex flex-col items-center justify-center p-4 relative z-10 w-full max-w-7xl mx-auto">
        <div className="text-center mb-10 w-full flex flex-col items-center">
          <div className="inline-flex items-center space-x-2 bg-white/5 border border-white/10 rounded-full px-4 py-1.5 mb-6">
            <span className="flex h-2 w-2 relative">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald opacity-75"></span>
              <span className="relative inline-flex rounded-full h-2 w-2 bg-emerald"></span>
            </span>
            <span className="text-xs font-semibold text-gray-300 uppercase tracking-wider">GPT-4 Powered</span>
          </div>
          <h1 className="text-5xl md:text-7xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-white to-gray-400 mb-4 tracking-tight drop-shadow-sm">
            AI that shops<br />smarter than you
          </h1>
          <p className="text-lg md:text-xl text-gray-400 max-w-2xl mx-auto">
            Smash AI browses the web, compares prices across Amazon and Flipkart, and analyzes reviews to find you the ultimate best deal.
          </p>
        </div>

        <div className="w-full flex justify-center mb-6">
          <SearchBar />
        </div>

        <div className="flex flex-wrap justify-center gap-3 mb-16">
          <span className="text-sm text-gray-500 py-1.5">Try searching:</span>
          {EXAMPLES.map((ex, idx) => (
            <button
              key={idx}
              onClick={() => navigate(`/results?q=${encodeURIComponent(ex)}`)}
              className="bg-white/5 hover:bg-white/10 border border-white/10 hover:border-violet/50 rounded-full px-4 py-1.5 text-sm font-medium text-gray-300 transition-colors"
            >
              {ex}
            </button>
          ))}
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 w-full max-w-5xl">
          <div className="glass-card p-6 rounded-2xl flex flex-col items-center text-center">
            <div className="bg-blue-500/20 p-3 rounded-xl mb-4">
              <Search className="w-6 h-6 text-blue-400" />
            </div>
            <h3 className="text-white font-semibold mb-2">Automated Browsing</h3>
            <p className="text-gray-400 text-sm">We scan multiple e-commerce sites simultaneously using Playwright.</p>
          </div>
          <div className="glass-card p-6 rounded-2xl flex flex-col items-center text-center">
            <div className="bg-violet/20 p-3 rounded-xl mb-4">
              <BrainCircuit className="w-6 h-6 text-violet" />
            </div>
            <h3 className="text-white font-semibold mb-2">AI Review Analysis</h3>
            <p className="text-gray-400 text-sm">GPT-4 processes thousands of reviews to generate accurate pros & cons.</p>
          </div>
          <div className="glass-card p-6 rounded-2xl flex flex-col items-center text-center">
            <div className="bg-emerald/20 p-3 rounded-xl mb-4">
              <Zap className="w-6 h-6 text-emerald" />
            </div>
            <h3 className="text-white font-semibold mb-2">Best Deal Finder</h3>
            <p className="text-gray-400 text-sm">Smart scoring algorithm balances price and ratings to spot the best value.</p>
          </div>
        </div>
      </main>
    </div>
  );
}

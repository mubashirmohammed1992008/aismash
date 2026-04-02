import React, { useState, useEffect } from 'react';
import { Bot } from 'lucide-react';

const messages = [
  "Launching AI browser...",
  "Scanning Amazon...",
  "Scanning Flipkart...",
  "Comparing prices...",
  "Analyzing reviews with GPT...",
  "Finding best deal..."
];

export default function Loader() {
  const [msgIndex, setMsgIndex] = useState(0);
  const [progress, setProgress] = useState(0);

  useEffect(() => {
    // Cycle messages every 1.5s
    const msgInterval = setInterval(() => {
      setMsgIndex((prev) => (prev + 1) % messages.length);
    }, 1500);

    // Increment progress from 0 to 90% over ~8 seconds
    // We achieve this by incrementing by 1% every 80ms approx
    const progInterval = setInterval(() => {
      setProgress((prev) => {
        if (prev >= 90) return 90;
        return prev + Math.random() * 2;
      });
    }, 150);

    return () => {
      clearInterval(msgInterval);
      clearInterval(progInterval);
    };
  }, []);

  return (
    <div className="fixed inset-0 min-h-screen bg-slate-900 z-50 flex items-center justify-center p-4">
      <div className="w-full max-w-md flex flex-col items-center">
        <div className="relative mb-8">
          <div className="absolute inset-0 bg-violet rounded-full blur-xl opacity-50 animate-pulse-slow"></div>
          <div className="bg-navy-900 border-2 border-violet/50 p-6 rounded-full relative z-10 shadow-[0_0_30px_rgba(124,58,237,0.4)]">
            <Bot className="w-16 h-16 text-white animate-bounce" />
          </div>
        </div>
        
        <h2 className="text-2xl font-bold text-white mb-2 text-center h-8 transition-opacity duration-300">
          {messages[msgIndex]}
        </h2>
        <p className="text-gray-400 text-sm mb-8 text-center animate-pulse">
          Please wait while Smash AI analyzes the web
        </p>

        <div className="w-full bg-white/10 rounded-full h-3 mb-2 overflow-hidden border border-white/5">
          <div 
            className="bg-gradient-to-r from-violet to-emerald h-3 rounded-full transition-all duration-300 ease-out relative"
            style={{ width: `${Math.min(90, progress)}%` }}
          >
            <div className="absolute top-0 bottom-0 left-0 right-0 bg-white/20 animate-pulse"></div>
          </div>
        </div>
        <div className="w-full flex justify-between text-xs text-gray-500 font-mono">
          <span>0%</span>
          <span>{Math.floor(progress)}%</span>
        </div>
      </div>
    </div>
  );
}

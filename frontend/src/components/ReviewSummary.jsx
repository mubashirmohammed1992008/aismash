import React from 'react';
import { CheckCircle2, XCircle, Bot } from 'lucide-react';

export default function ReviewSummary({ review_summary }) {
  if (!review_summary) return null;
  const { pros, cons, verdict } = review_summary;

  return (
    <div className="glass-card rounded-2xl p-6 mt-8">
      <div className="flex items-center space-x-3 mb-6">
        <Bot className="w-8 h-8 text-violet" />
        <h3 className="text-2xl font-bold text-white">AI Verdict</h3>
      </div>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-6">
        <div>
          <h4 className="text-emerald font-semibold mb-4 flex items-center">
            <CheckCircle2 className="w-5 h-5 mr-2" />
            Pros
          </h4>
          <div className="space-y-3">
            {pros.map((pro, idx) => (
              <div key={idx} className="bg-emerald/10 border border-emerald/20 text-emerald-400 px-4 py-2 rounded-lg text-sm">
                {pro}
              </div>
            ))}
          </div>
        </div>
        <div>
          <h4 className="text-red-400 font-semibold mb-4 flex items-center">
            <XCircle className="w-5 h-5 mr-2" />
            Cons
          </h4>
          <div className="space-y-3">
            {cons.map((con, idx) => (
              <div key={idx} className="bg-red-500/10 border border-red-500/20 text-red-400 px-4 py-2 rounded-lg text-sm">
                {con}
              </div>
            ))}
          </div>
        </div>
      </div>
      
      <div className="bg-white/5 rounded-xl p-5 border border-white/10">
        <p className="text-gray-200 leading-relaxed italic">
          "{verdict}"
        </p>
      </div>
    </div>
  );
}

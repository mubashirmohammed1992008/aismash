import React, { useEffect, useState } from 'react';
import { useSearchParams, useNavigate, useLocation } from 'react-router-dom';
import Navbar from '../components/Navbar';
import Loader from '../components/Loader';
import BestDealBadge from '../components/BestDealBadge';
import ProductCard from '../components/ProductCard';
import ReviewSummary from '../components/ReviewSummary';
import { searchProducts, analyzeUrl } from '../api/search';
import { ArrowLeft, AlertCircle, Link2 } from 'lucide-react';

export default function Results() {
  const [searchParams] = useSearchParams();
  const location = useLocation();
  const navigate = useNavigate();

  const isAnalyze = location.pathname.includes('/analyze');
  const query = isAnalyze ? searchParams.get('url') : searchParams.get('q');

  const [displayTitle, setDisplayTitle] = useState(query);
  const [loading, setLoading] = useState(true);
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!query) {
      navigate('/');
      return;
    }

    const fetchData = async () => {
      setLoading(true);
      setError(null);
      try {
        let result;
        if (isAnalyze) {
          result = await analyzeUrl(query);
          if (result.query) setDisplayTitle(result.query);
        } else {
          result = await searchProducts(query);
          setDisplayTitle(query);
        }
        setData(result);
      } catch (err) {
        setError(err.response?.data?.detail || err.message || "Failed to fetch results");
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [query, isAnalyze, navigate]);

  if (loading) {
    return <Loader />;
  }

  return (
    <div className="min-h-screen flex flex-col relative">
      <div className="absolute inset-0 bg-slate-900 pointer-events-none z-0"></div>

      <Navbar />

      <main className="flex-1 w-full max-w-7xl mx-auto px-4 py-8 relative z-10">
        <button
          onClick={() => navigate('/')}
          className="flex items-center text-gray-400 hover:text-white mb-6 transition-colors group"
        >
          <ArrowLeft className="w-4 h-4 mr-2 group-hover:-translate-x-1 transition-transform" />
          Back to Search
        </button>

        <div className="flex items-end justify-between mb-8 pb-4 border-b border-white/10">
          <div>
            <h1 className="text-3xl font-bold text-white mb-2 flex items-center">
              {isAnalyze && <Link2 className="w-8 h-8 mr-3 text-emerald-400 shrink-0" />}
              {isAnalyze && loading ? "Analyzing Link..." : "Results for: "}
              <span className={`ml-2 ${isAnalyze ? 'text-emerald-400' : 'text-violet'} line-clamp-1`} title={displayTitle}>
                "{displayTitle}"
              </span>
            </h1>
            {data && (
              <p className="text-gray-400 text-sm">
                Found {data.total_found} products in {data.scrape_time_seconds}s
              </p>
            )}
          </div>
        </div>

        {error && (
          <div className="bg-red-500/10 border border-red-500/50 rounded-xl p-6 flex items-start text-red-100 mb-8 max-w-2xl">
            <AlertCircle className="w-6 h-6 mr-3 text-red-500 flex-shrink-0" />
            <div>
              <h3 className="font-bold text-red-400 mb-1">Search Failed</h3>
              <p className="text-sm opacity-90">{error}</p>
            </div>
          </div>
        )}

        {!error && data && (
          <>
            <section className="mb-12">
              <BestDealBadge product={data.best_product} />
            </section>
            <section className="mb-12">
              <ReviewSummary review_summary={data.review_summary} />
            </section>
            <section>
              <h2 className="text-2xl font-bold text-white mb-6">Compare All Options</h2>
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                {data.all_results?.map((product, idx) => (
                  <ProductCard key={idx} product={product} />
                ))}
              </div>
            </section>
          </>
        )}
      </main>
    </div>
  );
}
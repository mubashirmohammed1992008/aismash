import React from 'react';
import StarRating from './StarRating';
import { ExternalLink, Tag, Trophy, CreditCard } from 'lucide-react';

export default function ProductCard({ product }) {
  const { title, site, price, currency, rating, review_count, url, image_url, is_cheapest, is_top_rated, original_price, discount_percentage, offers } = product;
  
  const siteColor = site.toLowerCase() === 'amazon' ? 'text-amber-500' : 'text-blue-500';

  return (
    <div className="glass-card rounded-xl p-5 flex flex-col h-full hover:-translate-y-1 transition-transform duration-300 relative overflow-hidden group">
      {is_cheapest && (
        <div className="absolute top-0 left-0 bg-blue-500 text-white text-xs font-bold px-3 py-1 rounded-br-lg flex items-center z-10">
          <Tag className="w-3 h-3 mr-1" /> Cheapest
        </div>
      )}
      {is_top_rated && !is_cheapest && (
        <div className="absolute top-0 left-0 bg-amber-500 text-white text-xs font-bold px-3 py-1 rounded-br-lg flex items-center z-10">
          <Trophy className="w-3 h-3 mr-1" /> Top Rated
        </div>
      )}

      <div className="h-48 w-full bg-white/5 rounded-lg mb-4 flex items-center justify-center p-2 relative">
        {image_url ? (
          <img src={image_url} alt={title} className="max-h-full max-w-full object-contain rounded-md" />
        ) : (
          <div className="text-gray-500">No Image</div>
        )}
        <div className="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center rounded-lg">
          <a href={url} target="_blank" rel="noreferrer" className="bg-white/20 hover:bg-white/40 text-white backdrop-blur-md px-4 py-2 rounded-full font-medium flex items-center transition-colors">
            View <ExternalLink className="w-4 h-4 ml-2" />
          </a>
        </div>
      </div>
      
      <div className="flex-1 flex flex-col">
        <h3 className="text-white font-medium line-clamp-2 mb-2 hover:text-violet transition-colors">
          <a href={url} target="_blank" rel="noreferrer">{title}</a>
        </h3>
        
        <div className="mt-auto space-y-3">
          <StarRating rating={rating} />
          <div className="text-xs text-gray-400 mb-1">{review_count.toLocaleString()} reviews</div>
          
          {offers && offers.length > 0 && (
            <div className="mt-3 bg-white/5 rounded-lg p-2 border border-white/5">
              <div className="text-[10px] uppercase font-bold text-gray-400 mb-1.5 flex items-center">
                <Tag className="w-3 h-3 mr-1 text-emerald-500" /> Offers
              </div>
              <ul className="space-y-1.5">
                {offers.slice(0, 2).map((offer, idx) => (
                  <li key={idx} className="text-[10px] sm:text-[11px] text-gray-300 line-clamp-1 flex items-start leading-tight">
                    <CreditCard className="w-3 h-3 mr-1.5 mt-0.5 text-indigo-400 shrink-0" />
                    <span className="flex-1">{offer}</span>
                  </li>
                ))}
              </ul>
            </div>
          )}
          
          <div className="flex items-end justify-between pt-3 border-t border-white/10 mt-3">
            <div className="flex flex-col">
              {original_price && original_price > price && (
                <div className="flex items-center space-x-1.5 mb-0.5">
                  <span className="text-xs text-gray-500 line-through">
                    {currency === 'INR' ? '₹' : '$'}{original_price.toLocaleString()}
                  </span>
                  {discount_percentage > 0 && (
                     <span className="text-[10px] text-emerald-400 font-bold bg-emerald-400/10 px-1 rounded">
                       {discount_percentage}% OFF
                     </span>
                  )}
                </div>
              )}
              <div className="text-xl font-bold font-mono text-white">
                {currency === 'INR' ? '₹' : '$'}{price.toLocaleString()}
              </div>
            </div>
            <div className={`text-sm font-semibold capitalize ${siteColor}`}>
              {site}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
